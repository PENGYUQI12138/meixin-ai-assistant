from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    """由环境变量驱动的应用配置。"""

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "美心 AI 行政助手"
    app_env: Literal["development", "test", "production"] = "development"
    app_timezone: str = "Asia/Shanghai"
    log_level: str = "INFO"
    database_url: str = "sqlite:///./database/meixin_dev.db"
    secret_key: str = Field(default="development-only-change-me", min_length=16)
    ai_provider: str = "disabled"
    ai_api_key: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
