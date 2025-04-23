from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str  # No hardcoding here!
    MODEL_NAME: str = "gpt-4"
    TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 500

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

