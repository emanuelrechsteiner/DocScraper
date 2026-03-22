"""Scrape router — POST /api/v1/scrape endpoint."""

import uuid
from datetime import datetime

from fastapi import APIRouter, HTTPException

from ..models.schemas import (
    APIResponse,
    ErrorResponse,
    JobStatus,
    MetaResponse,
    ScrapeRequest,
    ScrapeResponse,
)

router = APIRouter(tags=["scrape"])

# In-memory job store (will be replaced by PostgreSQL in Phase 3)
_jobs: dict[str, dict] = {}


@router.post("/scrape", response_model=APIResponse, status_code=202)
async def create_scrape_job(request: ScrapeRequest) -> APIResponse:
    """Submit a new documentation scrape job.

    The job runs asynchronously. Use GET /api/v1/jobs/{id} to check status.

    Args:
        request: Validated scrape request containing URL and options.

    Returns:
        APIResponse wrapping a ScrapeResponse with the new job_id.

    Raises:
        HTTPException: 500 if job creation fails unexpectedly.
    """
    job_id = f"job_{uuid.uuid4().hex[:12]}"
    request_id = f"req_{uuid.uuid4().hex[:12]}"
    now = datetime.utcnow()

    try:
        _jobs[job_id] = {
            "job_id": job_id,
            "status": JobStatus.PENDING,
            "url": str(request.url),
            "max_pages": request.max_pages,
            "output_format": request.output_format,
            "webhook_url": str(request.webhook_url) if request.webhook_url else None,
            "created_at": now,
            "started_at": None,
            "completed_at": None,
            "pages_scraped": 0,
            "pages_failed": 0,
            "error_message": None,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=ErrorResponse(
                code="JOB_CREATION_FAILED",
                message="Failed to create scrape job.",
                details={"reason": str(exc)},
            ).model_dump(),
        ) from exc

    return APIResponse(
        data=ScrapeResponse(
            job_id=job_id,
            status=JobStatus.PENDING,
            message="Scrape job submitted successfully",
            created_at=now,
        ).model_dump(),
        meta=MetaResponse(request_id=request_id),
    )
