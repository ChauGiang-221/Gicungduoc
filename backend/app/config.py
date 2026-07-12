from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # FPT AI Inference
    AI_TOKEN: str = ""
    MODEL_NAME: str = "SaoLa-Llama3.1-planner"
    AI_ENDPOINT: str = "https://mkp-api.fptcloud.com"

    # Generation params
    MAX_TOKENS: int = 2048
    TEMPERATURE: float = 0.7

    # CORS
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://localhost:19000,http://localhost:4000"

    # Firebase (optional)
    FIREBASE_PROJECT_ID: str = ""
    FIREBASE_CREDENTIALS_PATH: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
