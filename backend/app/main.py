"""
VN AI Innovation Hackathon - Backend API

Multi-provider AI service: OpenAI, Claude, Gemini
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.api.ai import router as ai_router
from app.api.health import router as health_router

settings = get_settings()

app = FastAPI(
    title="VN AI Innovation API",
    version="1.0.0",
    description="Multi-provider AI API for hackathon - OpenAI, Claude, Gemini",
)

# CORS
origins = [o.strip() for o in settings.ALLOWED_ORIGINS.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health_router)
app.include_router(ai_router)


@app.get("/")
async def root():
    return {
        "name": "VN AI Innovation API",
        "version": "1.0.0",
        "docs": "/docs",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
