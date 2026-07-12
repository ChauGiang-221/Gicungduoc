from pydantic import BaseModel, Field
from typing import Optional


class ChatMessage(BaseModel):
    role: str = Field(default="user")
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(..., examples=[[{"role": "user", "content": "Xin chào"}]])
    temperature: float = Field(0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(2048, ge=1, le=8192)


class ChatResponse(BaseModel):
    content: str
    model: str


class HealthResponse(BaseModel):
    status: str
    version: str
    ai: dict
