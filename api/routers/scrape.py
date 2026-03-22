"""Scrape router — POST /api/v1/scrape endpoint."""

import uuid

from fastapi import APIRouter

from ..models.schemas import (
    APIResponse,
    JobStatus,
    MetaResponse,
    ScrapeRequest,
    ScrapeResponse,
)
from ..services.job_store import job_store

router = APIRouter(tags=["scrape"])


@router.post("/scrape", response_model=APIResponse, status_code=202)
async def create_scrape_job(request: ScrapeRequest) -> APIResponse:
    """Submit a new documentation scrape job.

    The job runs asynchronously. Use GET /api/v1/jobs/{id} to check status.

    Args:
        request: Validated scrape request containing URL and options.

    Returns:
        APIResponse wrapping a ScrapeResponse with the new job_id.
    """
    job = job_store.create_job(
        url=str(request.url),
        job_type="scrape",
        max_pages=request.max_pages,
        output_format=request.output_format,
        webhook_url=str(request.webhook_url) if request.webhook_url else None,
    )

    return APIResponse(
        data=ScrapeResponse(
            job_id=job.job_id,
            status=JobStatus.PENDING,
            message="Scrape job submitted successfully",
            created_at=job.created_at,
        ).model_dump(mode="json"),
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )
