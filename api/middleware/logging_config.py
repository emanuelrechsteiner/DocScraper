"""Structured JSON logging configuration (#40).

Sets up the root logger with either JSON-formatted or human-readable
text output, depending on ``settings.log_format``.  JSON format emits
a single-line object per log record that includes optional request
tracing fields (``request_id``, ``method``, ``path``, ``status_code``,
``duration_ms``) when they are present on the record.

Usage::

    from api.middleware.logging_config import setup_logging
    setup_logging()

The function is idempotent: calling it multiple times is safe.
"""

import json
import logging
import sys
import traceback
from datetime import datetime, timezone
from typing import Any

from ..config import settings

# ---------------------------------------------------------------------------
# JSON formatter
# ---------------------------------------------------------------------------

#: Extra fields that are forwarded from LogRecord attributes to the JSON body
#: when they exist on the record object.
_OPTIONAL_FIELDS: tuple[str, ...] = (
    "request_id",
    "method",
    "path",
    "status_code",
    "duration_ms",
)


class JSONFormatter(logging.Formatter):
    """Formats log records as single-line JSON objects.

    The output always contains:

    * ``timestamp`` — ISO-8601 UTC string
    * ``level`` — upper-case level name (e.g. ``"INFO"``)
    * ``logger`` — logger name (e.g. ``"api.routers.scrape"``)
    * ``message`` — formatted log message

    When the record carries any of the optional request-tracing attributes
    (``request_id``, ``method``, ``path``, ``status_code``, ``duration_ms``)
    they are included at the top level of the JSON object.

    If the record has exception information it is serialised into an
    ``exception`` object with ``type``, ``value``, and ``traceback`` keys.
    """

    def format(self, record: logging.LogRecord) -> str:
        """Serialize *record* to a single-line JSON string.

        Args:
            record: The log record to format.

        Returns:
            A JSON-encoded string (no trailing newline).
        """
        payload: dict[str, Any] = {
            "timestamp": datetime.fromtimestamp(
                record.created, tz=timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        # Attach optional request-tracing fields if present on the record.
        for field in _OPTIONAL_FIELDS:
            value = getattr(record, field, None)
            if value is not None:
                payload[field] = value

        # Serialise exception info when present.
        if record.exc_info:
            exc_type, exc_value, exc_tb = record.exc_info
            payload["exception"] = {
                "type": exc_type.__name__ if exc_type else None,
                "value": str(exc_value),
                "traceback": traceback.format_tb(exc_tb) if exc_tb else [],
            }

        return json.dumps(payload, default=str)


# ---------------------------------------------------------------------------
# Public setup function
# ---------------------------------------------------------------------------

_TEXT_FORMAT = "%(asctime)s %(levelname)-8s %(name)s — %(message)s"
_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


def setup_logging() -> None:
    """Configure the root logger for the Parsify API.

    Reads ``settings.log_level`` and ``settings.log_format`` to decide
    the output format and verbosity:

    * ``log_format == "json"`` → :class:`JSONFormatter` (one JSON object per line)
    * anything else → standard text format suitable for human reading

    Noisy third-party loggers are quieted regardless of the global log
    level:

    * ``uvicorn.access`` → WARNING
    * ``sqlalchemy.engine`` → WARNING (unless ``settings.database_echo`` is
      ``True``, in which case it stays at DEBUG)

    The function clears any handlers previously attached to the root logger
    so that calling it multiple times is safe and idempotent.
    """
    log_level_name: str = getattr(settings, "log_level", "INFO").upper()
    log_level: int = getattr(logging, log_level_name, logging.INFO)

    log_format: str = getattr(settings, "log_format", "text").lower()

    # Build the handler.
    handler = logging.StreamHandler(sys.stdout)

    if log_format == "json":
        handler.setFormatter(JSONFormatter())
    else:
        handler.setFormatter(
            logging.Formatter(fmt=_TEXT_FORMAT, datefmt=_DATE_FORMAT)
        )

    # Reconfigure the root logger from scratch.
    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.setLevel(log_level)
    root_logger.addHandler(handler)

    # Quiet noisy third-party loggers.
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    database_echo: bool = getattr(settings, "database_echo", False)
    sqlalchemy_level = logging.DEBUG if database_echo else logging.WARNING
    logging.getLogger("sqlalchemy.engine").setLevel(sqlalchemy_level)
