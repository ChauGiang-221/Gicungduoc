from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o"

    # Anthropic
    ANTHROPIC_API_KEY: str = ""
    ANTHROPIC_MODEL: str = "claude-3-5-sonnet-20241022"

    # Google Gemini
    GOOGLE_API_KEY: str = ""
    GOOGLE_MODEL: str = "gemini-1.5-pro"

    # App
    DEFAULT_AI_PROVIDER: str = "openai"
    MAX_TOKENS: int = 2000
    TEMPERATURE: float = 0.7

    # CORS
    ALLOWED_ORIGINS: str = "http://localhost:3000,https://*.vercel.app"

    # Firebase
    FIREBASE_PROJECT_ID: str = ""
    FIREBASE_CREDENTIALS_PATH: str = ""

    # Security
    APP_ENV: str = "development"
    APP_SECRET_KEY: str = "change-this"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
