"""
Adam Gateway Configuration Module.

This module provides centralized configuration management
using pydantic-settings for environment variable handling.
"""

from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    log_level: str = "INFO"

    # Security Configuration
    master_key: str = ""
    jwt_secret: str = "change-me-in-production"
    jwt_expire_hours: int = 24

    # Database Configuration
    db_type: str = "sqlite"
    db_url: str = "sqlite:///./adam.db"

    # Redis Configuration
    redis_url: str = "redis://localhost:6379/0"
    enable_cache: bool = False
    cache_ttl: int = 3600

    # Rate Limiting Configuration
    enable_rate_limit: bool = True
    rate_limit_rpm: int = 120
    user_rate_limit_rpm: int = 60

    # Provider Configuration
    provider_config_dir: str = "configs/providers"

    # MCP Configuration
    enable_mcp: bool = False
    mcp_port: int = 8001

    # Logging Configuration
    log_file: str = "logs/adam-gateway.log"
    json_logging: bool = False

    class Config:
        env_prefix = "ADAM_"
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """Get application settings singleton."""
    return settings
