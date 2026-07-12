"""Chat API endpoint with SSE streaming."""
import json
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from app.models.schemas import ChatRequest, ChatResponse
from app.services.fpt_ai import FPTInference

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Non-streaming chat endpoint."""
    ai = FPTInference()

    response = ai.chat_complete(
        messages=[m.model_dump() for m in request.messages],
        temperature=request.temperature,
        max_tokens=request.max_tokens,
        stream=False,
    )

    return ChatResponse(
        content=response["choices"][0]["message"]["content"],
        model=response.get("model", "unknown"),
    )


@router.post("/stream")
async def chat_stream(request: ChatRequest):
    """SSE streaming chat endpoint."""
    ai = FPTInference()

    def generate():
        for chunk in ai.chat_stream(
            messages=[m.model_dump() for m in request.messages],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        ):
            yield f"data: {json.dumps({'content': chunk})}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
