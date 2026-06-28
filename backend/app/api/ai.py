"""AI endpoints - Chat completion with streaming support."""
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.models.schemas import ChatRequest, ChatResponse
from app.services.ai_service import ai_service
from app.services.database import db_service
from app.config import get_settings

router = APIRouter(prefix="/api/v1/ai", tags=["AI"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Non-streaming chat completion."""
    try:
        if request.stream:
            raise HTTPException(400, "Use /chat/stream for streaming")

        messages = [m.model_dump() for m in request.messages]
        content = await ai_service.chat(
            messages=messages,
            provider=request.provider,
            stream=False,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            system_prompt=request.system_prompt,
        )

        if request.user_id:
            import uuid
            conv_id = str(uuid.uuid4())
            await db_service.save_message(request.user_id, conv_id, "user", request.messages[-1].content, request.provider)
            await db_service.save_message(request.user_id, conv_id, "assistant", content, request.provider)

        return ChatResponse(
            content=content,
            provider=request.provider,
            model=ai_service._get_model(request.provider),
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI request failed: {str(e)}")


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Streaming chat completion (SSE)."""
    try:
        messages = [m.model_dump() for m in request.messages]
        stream = await ai_service.chat(
            messages=messages,
            provider=request.provider,
            stream=True,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            system_prompt=request.system_prompt,
        )

        async def event_generator():
            try:
                async for chunk in stream:
                    yield f"data: {chunk}\n\n"
                yield "data: [DONE]\n\n"
            except Exception as e:
                yield f"event: error\ndata: {str(e)}\n\n"

        return StreamingResponse(event_generator(), media_type="text/event-stream")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI stream failed: {str(e)}")


@router.get("/providers")
async def list_providers():
    """List available AI providers and their status."""
    settings = get_settings()
    return {
        "providers": {
            "openai": {"available": bool(settings.OPENAI_API_KEY), "model": settings.OPENAI_MODEL},
            "anthropic": {"available": bool(settings.ANTHROPIC_API_KEY), "model": settings.ANTHROPIC_MODEL},
            "google": {"available": bool(settings.GOOGLE_API_KEY), "model": settings.GOOGLE_MODEL},
        },
        "default": settings.DEFAULT_AI_PROVIDER,
    }
