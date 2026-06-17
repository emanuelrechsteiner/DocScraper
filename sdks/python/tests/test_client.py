"""Tests for the Parsify Python SDK client."""

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, patch

import pytest

from parsify import AsyncParsifyClient, Job, JobStatus, ParsifyClient
from parsify.client import ParsifyError


# ---------------------------------------------------------------------------
# ParsifyClient (sync)
# ---------------------------------------------------------------------------


class TestParsifyClientInit:
    def test_stores_api_key(self) -> None:
        client = ParsifyClient(api_key="pk_test123")
        assert client._api_key == "pk_test123"
        client.close()

    def test_strips_trailing_slash_from_base_url(self) -> None:
        client = ParsifyClient(api_key="pk_x", base_url="https://example.com/")
        assert client._base_url == "https://example.com"
        client.close()

    def test_context_manager_closes_client(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            assert client._api_key == "pk_test"


class TestParsifyClientScrape:
    def test_scrape_sends_correct_payload(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "_request") as mock_req:
                mock_req.return_value = {
                    "job_id": "job_abc",
                    "status": "pending",
                }
                job = client.scrape("https://docs.example.com", max_pages=50)
                mock_req.assert_called_once_with(
                    "POST",
                    "/api/v1/scrape",
                    json={
                        "url": "https://docs.example.com",
                        "max_pages": 50,
                        "output_format": "markdown",
                    },
                )
                assert job.job_id == "job_abc"
                assert job.status == JobStatus.PENDING

    def test_scrape_includes_webhook_url_when_provided(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "_request") as mock_req:
                mock_req.return_value = {"job_id": "job_wh", "status": "pending"}
                client.scrape("https://docs.example.com", webhook_url="https://hook.example.com")
                _, kwargs = mock_req.call_args
                assert kwargs["json"]["webhook_url"] == "https://hook.example.com"

    def test_scrape_omits_webhook_url_when_not_provided(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "_request") as mock_req:
                mock_req.return_value = {"job_id": "job_nowh", "status": "pending"}
                client.scrape("https://docs.example.com")
                _, kwargs = mock_req.call_args
                assert "webhook_url" not in kwargs["json"]


class TestParsifyClientGetJob:
    def test_get_job_calls_correct_endpoint(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "_request") as mock_req:
                mock_req.return_value = {"job_id": "job_xyz", "status": "running"}
                job = client.get_job("job_xyz")
                mock_req.assert_called_once_with("GET", "/api/v1/jobs/job_xyz")
                assert job.status == JobStatus.RUNNING


class TestParsifyClientListJobs:
    def test_list_jobs_returns_empty_list_on_non_list_response(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "_request") as mock_req:
                mock_req.return_value = {"items": []}
                result = client.list_jobs()
                assert result == []

    def test_list_jobs_parses_list_response(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "_request") as mock_req:
                mock_req.return_value = [
                    {"job_id": "j1", "status": "completed"},
                    {"job_id": "j2", "status": "pending"},
                ]
                result = client.list_jobs()
                assert len(result) == 2
                assert result[0].job_id == "j1"

    def test_list_jobs_forwards_status_filter(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "_request") as mock_req:
                mock_req.return_value = []
                client.list_jobs(status="completed", limit=10)
                mock_req.assert_called_once_with(
                    "GET", "/api/v1/jobs", params={"limit": 10, "status": "completed"}
                )


class TestParsifyClientWaitForCompletion:
    def test_returns_result_when_job_completes(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            completed_job = Job.from_api_response(
                {"job_id": "j1", "status": "completed", "output_files": ["out.md"]}
            )
            with patch.object(client, "get_job") as mock_get, patch.object(
                client, "get_result"
            ) as mock_result:
                mock_get.return_value = Job.from_api_response(
                    {"job_id": "j1", "status": "completed"}
                )
                mock_result.return_value = completed_job
                result = client.wait_for_completion("j1", poll_interval=0)
                assert result.output_files == ["out.md"]

    def test_raises_on_failed_job(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "get_job") as mock_get:
                mock_get.return_value = Job.from_api_response(
                    {"job_id": "j1", "status": "failed", "error_message": "network error"}
                )
                with pytest.raises(ParsifyError) as exc_info:
                    client.wait_for_completion("j1", poll_interval=0)
                assert exc_info.value.code == "JOB_FAILED"
                assert "network error" in str(exc_info.value)

    def test_raises_on_timeout(self) -> None:
        with ParsifyClient(api_key="pk_test") as client:
            with patch.object(client, "get_job") as mock_get:
                mock_get.return_value = Job.from_api_response(
                    {"job_id": "j1", "status": "running"}
                )
                with pytest.raises(ParsifyError) as exc_info:
                    client.wait_for_completion("j1", poll_interval=0, timeout=0.0)
                assert exc_info.value.code == "TIMEOUT"


# ---------------------------------------------------------------------------
# Job model
# ---------------------------------------------------------------------------


class TestJob:
    def test_from_api_response_minimal(self) -> None:
        data = {"job_id": "job_123", "status": "completed"}
        job = Job.from_api_response(data)
        assert job.job_id == "job_123"
        assert job.status == JobStatus.COMPLETED
        assert job.output_files == []
        assert job.pages_scraped == 0

    def test_from_api_response_full(self) -> None:
        data = {
            "job_id": "job_456",
            "status": "completed",
            "pages_scraped": 10,
            "pages_failed": 1,
            "output_files": ["a.md", "b.md"],
            "summary": {"total": 10},
        }
        job = Job.from_api_response(data)
        assert job.pages_scraped == 10
        assert job.pages_failed == 1
        assert len(job.output_files) == 2
        assert job.summary == {"total": 10}

    def test_job_status_enum_values(self) -> None:
        assert JobStatus.PENDING == "pending"
        assert JobStatus.RUNNING == "running"
        assert JobStatus.COMPLETED == "completed"
        assert JobStatus.FAILED == "failed"
        assert JobStatus.CANCELLED == "cancelled"


# ---------------------------------------------------------------------------
# ParsifyError
# ---------------------------------------------------------------------------


class TestParsifyError:
    def test_message_accessible_as_string(self) -> None:
        err = ParsifyError("bad request")
        assert str(err) == "bad request"

    def test_stores_status_code_and_code(self) -> None:
        err = ParsifyError("bad request", status_code=400, code="VALIDATION_ERROR")
        assert err.status_code == 400
        assert err.code == "VALIDATION_ERROR"

    def test_optional_fields_default_to_none(self) -> None:
        err = ParsifyError("oops")
        assert err.status_code is None
        assert err.code is None


# ---------------------------------------------------------------------------
# AsyncParsifyClient
# ---------------------------------------------------------------------------


class TestAsyncParsifyClient:
    def test_async_context_manager(self) -> None:
        async def run() -> None:
            async with AsyncParsifyClient(api_key="pk_async") as client:
                assert client._api_key == "pk_async"

        asyncio.run(run())

    def test_async_scrape_returns_job(self) -> None:
        async def run() -> None:
            async with AsyncParsifyClient(api_key="pk_async") as client:
                with patch.object(client, "_request", new_callable=AsyncMock) as mock_req:
                    mock_req.return_value = {"job_id": "async_job_1", "status": "pending"}
                    job = await client.scrape("https://docs.example.com")
                    assert job.job_id == "async_job_1"
                    assert job.status == JobStatus.PENDING

        asyncio.run(run())

    def test_async_wait_for_completion_raises_on_failure(self) -> None:
        async def run() -> None:
            async with AsyncParsifyClient(api_key="pk_async") as client:
                with patch.object(client, "get_job", new_callable=AsyncMock) as mock_get:
                    mock_get.return_value = Job.from_api_response(
                        {"job_id": "j2", "status": "failed", "error_message": "disk full"}
                    )
                    with pytest.raises(ParsifyError) as exc_info:
                        await client.wait_for_completion("j2", poll_interval=0)
                    assert exc_info.value.code == "JOB_FAILED"

        asyncio.run(run())

    def test_async_list_jobs_parses_list(self) -> None:
        async def run() -> None:
            async with AsyncParsifyClient(api_key="pk_async") as client:
                with patch.object(client, "_request", new_callable=AsyncMock) as mock_req:
                    mock_req.return_value = [
                        {"job_id": "a1", "status": "completed"},
                    ]
                    jobs = await client.list_jobs()
                    assert len(jobs) == 1
                    assert jobs[0].job_id == "a1"

        asyncio.run(run())
