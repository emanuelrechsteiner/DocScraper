"""Application configuration using Pydantic settings."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Parsify API configuration.

    All settings can be overridden via environment variables.
    """

    # App
    app_name: str = "Parsify API"
    debug: bool = False

    # Redis
    redis_url: str = "redis://localhost:6379"

    # Authentication
    api_key_prefix: str = "pk_"

    # Rate limiting (default per-key)
    rate_limit_free: str = "100/hour"
    rate_limit_pro: str = "1000/hour"
    rate_limit_enterprise: str = "10000/hour"

    # Stripe billing
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_free: str = ""
    stripe_price_pro: str = ""
    stripe_price_enterprise: str = ""

    # Database
    database_url: str = "postgresql+asyncpg://parsify:parsify@localhost:5432/parsify"
    database_echo: bool = False

    # Monitoring
    sentry_dsn: str = ""

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"  # "json" or "text"

    # Webhooks
    webhook_timeout: int = 30
    webhook_max_retries: int = 3

    # Job defaults
    max_concurrent_jobs: int = 5
    job_result_ttl: int = 86400  # 24 hours in seconds

    model_config = {"env_file": ".env", "env_prefix": "PARSIFY_", "extra": "ignore"}


settings = Settings()
