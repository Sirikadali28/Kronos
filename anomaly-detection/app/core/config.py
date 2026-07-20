from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized application configuration.
    """

    app_name: str = "KRONOS"
    app_version: str = "1.0.0"

    debug: bool = False

    host: str = "0.0.0.0"
    port: int = 8000

    log_level: str = "INFO"

    database_url: str

    # JWT Configuration
    secret_key: str
    access_token_expire_minutes: int = 60

    # Redis
    redis_url: str = "redis://redis:6379/0"

    # Celery
    celery_broker_url: str = "redis://redis:6379/0"
    celery_result_backend: str = "redis://redis:6379/0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()  # type: ignore[call-arg]
