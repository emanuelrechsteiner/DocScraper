"""Process router — POST /api/v1/process endpoint (#18)."""

import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.repositories import JobRepository
from ..db.session import get_db_session
from ..models.schemas import (
    APIResponse,
    JobStatus,
    MetaResponse,
    ProcessRequest,
    ProcessResponse,
)

router = APIRouter(tags=["process"])


@router.post("/process", response_model=APIResponse, status_code=202)
async def create_process_job(
    request: ProcessRequest,
    db: AsyncSession = Depends(get_db_session),
) -> APIResponse:
    """Submit a new document processing job (#18).

    Processes previously scraped markdown files through the cleaning
    and classification pipeline (PostScraperCleaner + DocPostProcessor).

    The job runs asynchronously. Use GET /api/v1/jobs/{id} to check status.

    Args:
        request: Validated process request with input directory and options.
        db: Injected async database session.

    Returns:
        APIResponse wrapping a ProcessResponse with the new job_id.
    """
    repo = JobRepository(db)
    job = await repo.create(
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
