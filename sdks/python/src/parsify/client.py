"""Parsify API client with sync and async support."""

from __future__ import annotations

import asyncio
import logging
import time
from typing import Any, Optional

import httpx

from .models import Job, JobStatus

logger = logging.getLogger(__name__)

DEFAULT_BASE_URL = "https://api.parsify.dev"
DEFAULT_TIMEOUT = 30.0
DEFAULT_POLL_INTERVAL = 5.0


class ParsifyError(Exception):
    """Base exception for Parsify SDK errors.

    Args:
        message: Human-readable error description.
        status_code: HTTP status code from the API response, if applicable.
        code: Machine-readable error code returned by the API.
    """

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        code: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code


def _parse_error(body: dict[str, Any]) -> tuple[str, Optional[str]]:
    """Extract a human-readable message and error code from an API error body.

    Args:
        body: Raw response body dictionary.

    Returns:
        Tuple of (message, code).
    """
    error = body.get("error", body.get("detail", {}))
    if isinstance(error, dict):
        return error.get("message", str(error)), error.get("code")
    return str(error), None


class ParsifyClient:
    """Synchronous client for the Parsify documentation processing API.

    Args:
        api_key: Your Parsify API key (starts with ``pk_``).
        base_url: API base URL. Defaults to ``https://api.parsify.dev``.
        timeout: Per-request timeout in seconds.

    Example:
        ```python
        from parsify import ParsifyClient

        with ParsifyClient(api_key="pk_your_key_here") as client:
            job = client.scrape("https://docs.example.com", max_pages=50)
            result = client.wait_for_completion(job.job_id)
            print(result.output_files)
        ```
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._client = httpx.Client(
            base_url=self._base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )

    def close(self) -> None:
        """Close the underlying HTTP client and release connections."""
        self._client.close()

    def __enter__(self) -> ParsifyClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Execute an HTTP request and return the unwrapped response payload.

        Args:
            method: HTTP method (GET, POST, etc.).
            path: URL path relative to the base URL.
            **kwargs: Additional arguments forwarded to httpx.

        Returns:
            Parsed response data (``data`` key unwrapped when present).

        Raises:
            ParsifyError: On any 4xx or 5xx response.
        """
        response = self._client.request(method, path, **kwargs)
        body: dict[str, Any] = response.json()
        if response.status_code >= 400:
            msg, code = _parse_error(body)
            raise ParsifyError(msg, status_code=response.status_code, code=code)
        return body.get("data", body)

    def scrape(
        self,
        url: str,
        max_pages: int = 100,
        output_format: str = "markdown",
        webhook_url: Optional[str] = None,
    ) -> Job:
        """Submit a new scrape job.

        Args:
            url: Documentation website URL to scrape.
            max_pages: Maximum number of pages to scrape.
            output_format: Output format (default: ``"markdown"``).
            webhook_url: Optional URL for a job-completion webhook callback.

        Returns:
            Job object containing the new job ID and initial status.
        """
        payload: dict[str, Any] = {
            "url": url,
            "max_pages": max_pages,
            "output_format": output_format,
        }
        if webhook_url:
            payload["webhook_url"] = webhook_url

        data = self._request("POST", "/api/v1/scrape", json=payload)
        assert isinstance(data, dict)
        return Job.from_api_response(data)

    def get_job(self, job_id: str) -> Job:
        """Fetch the current status of a job.

        Args:
            job_id: The job identifier.

        Returns:
            Job object reflecting the current state.
        """
        data = self._request("GET", f"/api/v1/jobs/{job_id}")
        assert isinstance(data, dict)
        return Job.from_api_response(data)

    def get_result(self, job_id: str) -> Job:
        """Fetch the result of a completed job, including output files.

        Args:
            job_id: The job identifier.

        Returns:
            Job object populated with output files and summary.
        """
        data = self._request("GET", f"/api/v1/jobs/{job_id}/result")
        assert isinstance(data, dict)
        return Job.from_api_response(data)

    def wait_for_completion(
        self,
        job_id: str,
        poll_interval: float = DEFAULT_POLL_INTERVAL,
        timeout: float = 1800.0,
    ) -> Job:
        """Poll a job until it reaches a terminal state.

        Args:
            job_id: The job identifier.
            poll_interval: Seconds to wait between poll requests.
            timeout: Maximum total wait time in seconds before raising.

        Returns:
            Completed Job object (calls ``get_result`` internally).

        Raises:
            ParsifyError: If the job fails or the timeout is exceeded.
        """
        start = time.monotonic()
        while True:
            job = self.get_job(job_id)
            if job.status == JobStatus.COMPLETED:
                return self.get_result(job_id)
            if job.status == JobStatus.FAILED:
                raise ParsifyError(
                    f"Job {job_id} failed: {job.error_message}",
                    code="JOB_FAILED",
                )
            if time.monotonic() - start > timeout:
                raise ParsifyError(
                    f"Job {job_id} timed out after {timeout}s",
                    code="TIMEOUT",
                )
            logger.debug(
                "Job %s: %s (%.0f%%), polling in %ss",
                job_id,
                job.status.value,
                job.progress,
                poll_interval,
            )
            time.sleep(poll_interval)

    def list_jobs(
        self,
        status: Optional[str] = None,
        limit: int = 50,
    ) -> list[Job]:
        """List jobs with optional status filtering.

        Args:
            status: Optional status string to filter results.
            limit: Maximum number of results to return.

        Returns:
            List of Job objects.
        """
        params: dict[str, Any] = {"limit": limit}
        if status:
            params["status"] = status
        data = self._request("GET", "/api/v1/jobs", params=params)
        if isinstance(data, list):
            return [Job.from_api_response(j) for j in data]
        return []


class AsyncParsifyClient:
    """Async client for the Parsify documentation processing API.

    Args:
        api_key: Your Parsify API key (starts with ``pk_``).
        base_url: API base URL. Defaults to ``https://api.parsify.dev``.
        timeout: Per-request timeout in seconds.

    Example:
        ```python
        import asyncio
        from parsify import AsyncParsifyClient

        async def main():
            async with AsyncParsifyClient(api_key="pk_...") as client:
                job = await client.scrape("https://docs.example.com")
                result = await client.wait_for_completion(job.job_id)
                print(result.output_files)

        asyncio.run(main())
        ```
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self._base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        """Close the underlying async HTTP client."""
        await self._client.aclose()

    async def __aenter__(self) -> AsyncParsifyClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()

    async def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Execute an async HTTP request and return the unwrapped payload.

        Args:
            method: HTTP method.
            path: URL path relative to the base URL.
            **kwargs: Additional arguments forwarded to httpx.

        Returns:
            Parsed response data.

        Raises:
            ParsifyError: On any 4xx or 5xx response.
        """
        response = await self._client.request(method, path, **kwargs)
        body: dict[str, Any] = response.json()
        if response.status_code >= 400:
            msg, code = _parse_error(body)
            raise ParsifyError(msg, status_code=response.status_code, code=code)
        return body.get("data", body)

    async def scrape(
        self,
        url: str,
        max_pages: int = 100,
        output_format: str = "markdown",
        webhook_url: Optional[str] = None,
    ) -> Job:
        """Submit a new scrape job asynchronously.

        Args:
            url: Documentation website URL to scrape.
            max_pages: Maximum number of pages to scrape.
            output_format: Output format (default: ``"markdown"``).
            webhook_url: Optional webhook URL for job-completion callback.

        Returns:
            Job object with the new job ID and initial status.
        """
        payload: dict[str, Any] = {
            "url": url,
            "max_pages": max_pages,
            "output_format": output_format,
        }
        if webhook_url:
            payload["webhook_url"] = webhook_url
        data = await self._request("POST", "/api/v1/scrape", json=payload)
        assert isinstance(data, dict)
        return Job.from_api_response(data)

    async def get_job(self, job_id: str) -> Job:
        """Fetch the current status of a job asynchronously.

        Args:
            job_id: The job identifier.

        Returns:
            Job object reflecting the current state.
        """
        data = await self._request("GET", f"/api/v1/jobs/{job_id}")
        assert isinstance(data, dict)
        return Job.from_api_response(data)

    async def get_result(self, job_id: str) -> Job:
        """Fetch the result of a completed job asynchronously.

        Args:
            job_id: The job identifier.

        Returns:
            Job object with output files and summary.
        """
        data = await self._request("GET", f"/api/v1/jobs/{job_id}/result")
        assert isinstance(data, dict)
        return Job.from_api_response(data)

    async def wait_for_completion(
        self,
        job_id: str,
        poll_interval: float = DEFAULT_POLL_INTERVAL,
        timeout: float = 1800.0,
    ) -> Job:
        """Async poll a job until it reaches a terminal state.

        Args:
            job_id: The job identifier.
            poll_interval: Seconds between poll requests.
            timeout: Maximum wait time in seconds.

        Returns:
            Completed Job object.

        Raises:
            ParsifyError: If the job fails or the timeout is exceeded.
        """
        start = time.monotonic()
        while True:
            job = await self.get_job(job_id)
            if job.status == JobStatus.COMPLETED:
                return await self.get_result(job_id)
            if job.status == JobStatus.FAILED:
                raise ParsifyError(
                    f"Job {job_id} failed: {job.error_message}",
                    code="JOB_FAILED",
                )
            if time.monotonic() - start > timeout:
                raise ParsifyError(
                    f"Job {job_id} timed out after {timeout}s",
                    code="TIMEOUT",
                )
            logger.debug(
                "Job %s: %s (%.0f%%), polling in %ss",
                job_id,
                job.status.value,
                job.progress,
                poll_interval,
            )
            await asyncio.sleep(poll_interval)

    async def list_jobs(
        self,
        status: Optional[str] = None,
        limit: int = 50,
    ) -> list[Job]:
        """List jobs asynchronously with optional status filtering.

        Args:
            status: Optional status string to filter results.
            limit: Maximum number of results to return.

        Returns:
            List of Job objects.
        """
        params: dict[str, Any] = {"limit": limit}
        if status:
            params["status"] = status
        data = await self._request("GET", "/api/v1/jobs", params=params)
        if isinstance(data, list):
            return [Job.from_api_response(j) for j in data]
        return []
