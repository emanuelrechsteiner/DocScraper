"""Process router — POST /api/v1/process endpoint (#18)."""

import uuid

from fastapi import APIRouter

from ..models.schemas import (
    APIResponse,
    MetaResponse,
    ProcessRequest,
    ProcessResponse,
    JobStatus,
)
from ..services.job_store import job_store

router = APIRouter(tags=["process"])


@router.post("/process", response_model=APIResponse, status_code=202)
async def create_process_job(request: ProcessRequest) -> APIResponse:
    """Submit a new document processing job (#18).

    Processes previously scraped markdown files through the cleaning
    and classification pipeline (PostScraperCleaner + DocPostProcessor).

    The job runs asynchronously. Use GET /api/v1/jobs/{id} to check status.

    Args:
        request: Validated process request with input directory and options.

    Returns:
        APIResponse wrapping a ProcessResponse with the new job_id.
    """
    job = job_store.create_job(
        url=request.input_dir,
        job_type="process",
        output_format=request.output_format,
        webhook_url=str(request.webhook_url) if request.webhook_url else None,
    )

    return APIResponse(
        data=ProcessResponse(
            job_id=job.job_id,
            status=JobStatus.PENDING,
            message="Process job submitted successfully",
            created_at=job.created_at,
        ).model_dump(mode="json"),
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )
