"""Health check endpoint."""
from fastapi import APIRouter
from app.models.schemas import HealthResponse
from app.config import get_settings

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    settings = get_settings()
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        ai_providers={
            "openai": bool(settings.OPENAI_API_KEY),
            "anthropic": bool(settings.ANTHROPIC_API_KEY),
            "google": bool(settings.GOOGLE_API_KEY),
        },
    )
