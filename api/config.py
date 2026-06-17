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

    # Clerk (dashboard auth)
    clerk_jwks_url: str = ""
    clerk_publishable_key: str = ""
    # Expected token issuer (Clerk Frontend API URL, e.g.
    # "https://clerk.your-domain.com"). When set, the `iss` claim is verified.
    clerk_issuer: str = ""
    # Comma-separated allowlist of authorized parties (`azp` claim). Defaults to
    # ``dashboard_origin`` when empty. Tokens whose `azp` is not allowed are rejected.
    clerk_authorized_parties: str = ""

    # Dashboard
    dashboard_origin: str = "http://localhost:5173"

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
