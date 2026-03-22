"""In-memory job store.

Provides CRUD operations for job state. Will be replaced by
PostgreSQL in Phase 3 (see ADR-002).
"""

import logging
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional

from ..models.schemas import JobStatus

logger = logging.getLogger(__name__)


@dataclass
class JobData:
    """Internal representation of a job."""

    job_id: str
    status: JobStatus
    url: str
    job_type: str = "scrape"  # "scrape" or "process"
    max_pages: int = 100
    output_format: str = "markdown"
    webhook_url: Optional[str] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    pages_scraped: int = 0
    pages_failed: int = 0
    progress: float = 0.0
    error_message: Optional[str] = None
    output_files: list[str] = field(default_factory=list)
    summary: Optional[dict[str, Any]] = None
    owner_key_id: Optional[str] = None


class JobStore:
    """In-memory job storage with CRUD operations.

    Thread-safe for single-process use. In Phase 3, this will be
    replaced by SQLAlchemy models backed by PostgreSQL.
    """

    def __init__(self) -> None:
        self._jobs: dict[str, JobData] = {}

    def create_job(
        self,
        url: str,
        job_type: str = "scrape",
        max_pages: int = 100,
        output_format: str = "markdown",
        webhook_url: Optional[str] = None,
        owner_key_id: Optional[str] = None,
    ) -> JobData:
        """Create a new job and return its data."""
        job_id = f"job_{uuid.uuid4().hex[:12]}"
        job = JobData(
            job_id=job_id,
            status=JobStatus.PENDING,
            url=url,
            job_type=job_type,
            max_pages=max_pages,
            output_format=output_format,
            webhook_url=webhook_url,
            owner_key_id=owner_key_id,
        )
        self._jobs[job_id] = job
        logger.info("Created %s job %s for %s", job_type, job_id, url)
        return job

    def get_job(self, job_id: str) -> Optional[JobData]:
        """Get a job by ID, or None if not found."""
        return self._jobs.get(job_id)

    def update_job(self, job_id: str, **kwargs: Any) -> Optional[JobData]:
        """Update job fields. Returns updated job or None if not found."""
        job = self._jobs.get(job_id)
        if job is None:
            return None
        for key, value in kwargs.items():
            if hasattr(job, key):
                setattr(job, key, value)
        return job

    def list_jobs(
        self,
        owner_key_id: Optional[str] = None,
        status: Optional[JobStatus] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> tuple[list[JobData], int]:
        """List jobs with optional filtering. Returns (jobs, total_count)."""
        jobs = list(self._jobs.values())
        if owner_key_id is not None:
            jobs = [j for j in jobs if j.owner_key_id == owner_key_id]
        if status is not None:
            jobs = [j for j in jobs if j.status == status]
        jobs.sort(key=lambda j: j.created_at, reverse=True)
        total = len(jobs)
        return jobs[offset : offset + limit], total

    def delete_job(self, job_id: str) -> bool:
        """Delete a job. Returns True if it existed."""
        return self._jobs.pop(job_id, None) is not None


# Singleton instance — shared across the application
job_store = JobStore()
