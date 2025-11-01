from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "rag-absa"
    ENV: str = "dev"
    OPENAI_API_KEY: str
    SUPABASE_DB_URL: str
    OPENAI_EMBED_MODEL: str = "text-embedding-3-small"
    OPENAI_CHAT_MODEL: str = "gpt-4o-mini"
    RETRIEVAL_TOP_K: int = 3
    MIN_SIM_THRESHOLD: float = 0.70

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()
