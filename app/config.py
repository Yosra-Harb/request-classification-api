from pydantic_settings import BaseSettings, SettingsConfigDict

from app.enums import Environment, LogLevel


class Settings(BaseSettings):
    app_name: str = "Version 0.6 — Production Foundation, Security & Observability"
    app_version: str = "0.6.0"

    environment: Environment = Environment.DEVELOPMENT
    log_level: LogLevel = LogLevel.INFO

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()