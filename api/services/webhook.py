"""Webhook callback service (#22).

Sends HTTP POST callbacks to user-provided URLs when jobs complete.
Implements retry with exponential backoff via tenacity.
"""

import logging
from datetime import datetime, timezone
from typing import Any, Optional

import httpx
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from ..config import settings
from ..models.schemas import JobStatus, WebhookPayload

logger = logging.getLogger(__name__)


class WebhookService:
    """Delivers webhook callbacks for job lifecycle events."""

    def __init__(self) -> None:
        self._delivery_log: list[dict[str, Any]] = []

    async def send_job_completed(
        self,
        webhook_url: str,
        job_id: str,
        status: JobStatus,
        result: Optional[dict[str, Any]] = None,
    ) -> bool:
        """Send a job completion webhook.

        Args:
            webhook_url: Target URL to POST to.
            job_id: The completed job ID.
            status: Final job status.
            result: Optional result summary.

        Returns:
            True if delivery succeeded, False otherwise.
        """
        payload = WebhookPayload(
            event="job.completed",
            job_id=job_id,
            status=status,
            result=result,
            timestamp=datetime.now(timezone.utc),
        )
        return await self._deliver(webhook_url, payload)

    async def send_job_failed(
        self,
        webhook_url: str,
        job_id: str,
        error_message: str,
    ) -> bool:
        """Send a job failure webhook.

        Args:
            webhook_url: Target URL to POST to.
            job_id: The failed job ID.
            error_message: Description of the failure.

        Returns:
            True if delivery succeeded, False otherwise.
        """
        payload = WebhookPayload(
            event="job.failed",
            job_id=job_id,
            status=JobStatus.FAILED,
            result={"error": error_message},
            timestamp=datetime.now(timezone.utc),
        )
        return await self._deliver(webhook_url, payload)

    async def _deliver(self, url: str, payload: WebhookPayload) -> bool:
        """Deliver a webhook payload with retries.

        Uses exponential backoff: 1s, 2s, 4s up to max_retries.
        """
        delivery_record: dict[str, Any] = {
            "url": url,
            "event": payload.event,
            "job_id": payload.job_id,
            "attempts": 0,
            "success": False,
        }

        try:
            await self._post_with_retry(url, payload.model_dump(mode="json"))
            delivery_record["success"] = True
            logger.info(
                "Webhook delivered: %s to %s for job %s",
                payload.event, url, payload.job_id,
            )
        except Exception:
            logger.warning(
                "Webhook delivery failed after retries: %s to %s for job %s",
                payload.event, url, payload.job_id,
                exc_info=True,
            )
        finally:
            self._delivery_log.append(delivery_record)

        return delivery_record["success"]

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=8),
        retry=retry_if_exception_type((httpx.HTTPStatusError, httpx.ConnectError)),
        reraise=True,
    )
    async def _post_with_retry(self, url: str, payload: dict[str, Any]) -> None:
        """POST payload to URL with automatic retries."""
        async with httpx.AsyncClient(timeout=settings.webhook_timeout) as client:
            response = await client.post(
                url,
                json=payload,
                headers={"Content-Type": "application/json", "User-Agent": "Parsify-Webhook/1.0"},
            )
            response.raise_for_status()


# Singleton instance
webhook_service = WebhookService()
