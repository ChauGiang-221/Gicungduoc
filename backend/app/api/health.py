"""Health check endpoint."""
from fastapi import APIRouter
from app.config import get_settings

router = APIRouter()


@router.get("/health")
async def health_check():
    settings = get_settings()
    return {
        "status": "healthy",
        "version": "1.0.0",
        "ai": {
            "provider": "fpt",
            "endpoint": settings.AI_ENDPOINT,
            "model": settings.MODEL_NAME,
            "configured": bool(settings.AI_TOKEN),
        },
    }
