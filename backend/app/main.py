"""
Gicungduoc - Backend API
FPT AI Inference with SSE Streaming
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.api.chat import router as chat_router
from app.api.health import router as health_router

settings = get_settings()

app = FastAPI(
    title="Gicungduoc API",
    version="1.0.0",
    description="AI Chatbot API với FPT AI Inference",
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
app.include_router(chat_router)


@app.get("/")
async def root():
    return {
        "name": "Gicungduoc API",
        "version": "1.0.0",
        "docs": "/docs",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
