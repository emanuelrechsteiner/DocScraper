"""Pydantic request/response models for the Parsify API."""

from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field, HttpUrl


class JobStatus(str, Enum):
    """Status of a scrape/process job."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ScrapeRequest(BaseModel):
    """Request body for POST /api/v1/scrape."""

    url: HttpUrl = Field(..., description="Documentation website URL to scrape")
    max_pages: int = Field(
        default=100, ge=1, le=10000, description="Maximum pages to scrape"
    )
    output_format: str = Field(default="markdown", description="Output format")
    webhook_url: Optional[HttpUrl] = Field(
        default=None, description="URL for job completion callback"
    )


class ScrapeResponse(BaseModel):
    """Response body for POST /api/v1/scrape."""

    job_id: str = Field(..., description="Unique job identifier")
    status: JobStatus = Field(default=JobStatus.PENDING)
    message: str = Field(default="Job submitted successfully")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class JobStatusResponse(BaseModel):
    """Response body for GET /api/v1/jobs/{id}."""

    job_id: str
    status: JobStatus
    progress: float = Field(
        default=0.0, ge=0.0, le=100.0, description="Progress percentage"
    )
    pages_scraped: int = Field(default=0)
    pages_failed: int = Field(default=0)
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None


class JobResultResponse(BaseModel):
    """Response body for GET /api/v1/jobs/{id}/result."""

    job_id: str
    status: JobStatus
    total_pages: int = Field(default=0)
    failed_pages: int = Field(default=0)
    output_files: list[str] = Field(default_factory=list)
    summary: Optional[dict[str, Any]] = None
    completed_at: Optional[datetime] = None


class ErrorResponse(BaseModel):
    """Standard error response."""

    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Human-readable error message")
    details: Optional[dict[str, Any]] = None


class MetaResponse(BaseModel):
    """Metadata included in all API responses."""

    request_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class APIResponse(BaseModel):
    """Standard API response wrapper."""

    data: Optional[Any] = None
    error: Optional[ErrorResponse] = None
    meta: MetaResponse
