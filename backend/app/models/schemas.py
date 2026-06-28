from pydantic import BaseModel, Field
from typing import Literal, Optional

AIProvider = Literal["openai", "anthropic", "google"]


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(..., examples=[[{"role": "user", "content": "Xin chào"}]])
    provider: AIProvider = "openai"
    stream: bool = False
    temperature: float = Field(0.7, ge=0.0, le=1.0)
    max_tokens: int = Field(2000, ge=1, le=8000)
    system_prompt: Optional[str] = None
    user_id: Optional[str] = "anonymous"


class ChatResponse(BaseModel):
    content: str
    provider: str
    model: str
    tokens_used: Optional[int] = None


class Conversation(BaseModel):
    id: str
    title: str
    user_id: str
    created_at: str
    updated_at: str
    message_count: int = 0


class HealthResponse(BaseModel):
    status: str
    version: str
    ai_providers: dict[str, bool]
