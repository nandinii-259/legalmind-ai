from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    GEMINI_API_KEY: str

    LLM_PROVIDER: str = "gemini"

    MODEL_NAME: str = "gemini-2.5-flash"

    TEMPERATURE: float = 0.2

    MAX_TOKENS: int = 1024

    DATABASE_URL: str = "sqlite:///legalmind.db"

    CHROMA_PATH: str = "vector_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()


print("=" * 50)
print("Loaded Configuration")
print("MODEL_NAME:", settings.MODEL_NAME)
print("=" * 50)