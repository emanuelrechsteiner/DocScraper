"""Sentry error monitoring integration (#52).

Initializes Sentry SDK for FastAPI with environment-based configuration.
DSN is read from PARSIFY_SENTRY_DSN environment variable.
"""

import logging

import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from ..config import settings

logger = logging.getLogger(__name__)


def init_sentry() -> None:
    """Initialize Sentry SDK if DSN is configured.

    Reads PARSIFY_SENTRY_DSN from environment. If empty or unset,
    Sentry is silently disabled (no-op in development).
    """
    dsn = getattr(settings, "sentry_dsn", "")
    if not dsn:
        logger.debug("Sentry DSN not configured — error monitoring disabled")
        return

    environment = "production" if not settings.debug else "development"

    sentry_sdk.init(
        dsn=dsn,
        environment=environment,
        traces_sample_rate=0.1 if environment == "production" else 1.0,
        profiles_sample_rate=0.1 if environment == "production" else 0.0,
        integrations=[
            FastApiIntegration(transaction_style="endpoint"),
            SqlalchemyIntegration(),
        ],
        send_default_pii=False,
    )
    logger.info("Sentry initialized (environment: %s)", environment)
