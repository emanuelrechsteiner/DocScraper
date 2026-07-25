"""Data models for Parsify API responses."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class JobStatus(str, Enum):
    """Enumeration of possible job states."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class ScrapeConfig:
    """Configuration for a scrape job submission.

    Args:
        url: Documentation website URL to scrape.
        max_pages: Maximum number of pages to scrape.
        output_format: Desired output format (e.g. "markdown").
        webhook_url: Optional URL for job completion callback.
    """

    url: str
    max_pages: int = 100
    output_format: str = "markdown"
    webhook_url: str | None = None


@dataclass
class Job:
    """Represents a Parsify scrape job and its current state.

    Args:
        job_id: Unique job identifier.
        status: Current job status.
        job_type: Type of job (default: "scrape").
        progress: Completion percentage (0.0–100.0).
        pages_scraped: Number of pages successfully scraped.
        pages_failed: Number of pages that failed to scrape.
        created_at: Timestamp when the job was created.
        started_at: Timestamp when the job started running.
        completed_at: Timestamp when the job finished.
        error_message: Human-readable error message if the job failed.
        output_files: List of output file paths or URLs.
        summary: Optional metadata summary from the completed job.
    """

    job_id: str
    status: JobStatus
    job_type: str = "scrape"
    progress: float = 0.0
    pages_scraped: int = 0
    pages_failed: int = 0
    created_at: datetime | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    error_message: str | None = None
    output_files: list[str] = field(default_factory=list)
    summary: dict[str, Any] | None = None

    @classmethod
    def from_api_response(cls, data: dict[str, Any]) -> Job:
        """Construct a Job from a raw API response dictionary.

        Args:
            data: Raw dictionary returned by the Parsify API.

        Returns:
            Populated Job instance.
        """
        return cls(
            job_id=data["job_id"],
            status=JobStatus(data["status"]),
            job_type=data.get("job_type", "scrape"),
            progress=data.get("progress", 0.0),
            pages_scraped=data.get("pages_scraped", 0),
            pages_failed=data.get("pages_failed", 0),
            error_message=data.get("error_message"),
            output_files=data.get("output_files", []),
            summary=data.get("summary"),
        )
