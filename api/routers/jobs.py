"""Jobs router — GET /api/v1/jobs endpoints (#16, #17)."""

import uuid

from fastapi import APIRouter, HTTPException, Query

from ..models.schemas import (
    APIResponse,
    JobResultResponse,
    JobStatus,
    JobStatusResponse,
    MetaResponse,
)
from ..services.job_store import job_store

router = APIRouter(tags=["jobs"])


@router.get("/jobs/{job_id}", response_model=APIResponse)
async def get_job_status(job_id: str) -> APIResponse:
    """Get the current status of a job (#16).

    Args:
        job_id: Unique job identifier returned by POST /scrape or /process.

    Returns:
        APIResponse wrapping a JobStatusResponse.

    Raises:
        HTTPException: 404 if job not found.
    """
    job = job_store.get_job(job_id)
    if job is None:
        raise HTTPException(
            status_code=404,
            detail={"code": "JOB_NOT_FOUND", "message": f"Job {job_id} not found"},
        )

    return APIResponse(
        data=JobStatusResponse(
            job_id=job.job_id,
            status=job.status,
            job_type=job.job_type,
            progress=job.progress,
            pages_scraped=job.pages_scraped,
            pages_failed=job.pages_failed,
            created_at=job.created_at,
            started_at=job.started_at,
            completed_at=job.completed_at,
            error_message=job.error_message,
        ).model_dump(mode="json"),
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )


@router.get("/jobs/{job_id}/result", response_model=APIResponse)
async def get_job_result(job_id: str) -> APIResponse:
    """Get the result of a completed job (#17).

    Args:
        job_id: Unique job identifier.

    Returns:
        APIResponse wrapping a JobResultResponse.

    Raises:
        HTTPException: 404 if job not found, 409 if job not yet completed.
    """
    job = job_store.get_job(job_id)
    if job is None:
        raise HTTPException(
            status_code=404,
            detail={"code": "JOB_NOT_FOUND", "message": f"Job {job_id} not found"},
        )

    if job.status not in (JobStatus.COMPLETED, JobStatus.FAILED):
        raise HTTPException(
            status_code=409,
            detail={
                "code": "JOB_NOT_COMPLETE",
                "message": f"Job {job_id} is still {job.status.value}. Poll GET /jobs/{job_id} for status.",
            },
        )

    return APIResponse(
        data=JobResultResponse(
            job_id=job.job_id,
            status=job.status,
            total_pages=job.pages_scraped,
            failed_pages=job.pages_failed,
            output_files=job.output_files,
            summary=job.summary,
            completed_at=job.completed_at,
        ).model_dump(mode="json"),
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )


@router.get("/jobs", response_model=APIResponse)
async def list_jobs(
    status: JobStatus | None = Query(default=None, description="Filter by status"),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> APIResponse:
    """List jobs with optional filtering.

    Args:
        status: Optional status filter.
        limit: Maximum results to return.
        offset: Pagination offset.

    Returns:
        APIResponse with paginated job list.
    """
    jobs, total = job_store.list_jobs(status=status, limit=limit, offset=offset)

    return APIResponse(
        data=[
            JobStatusResponse(
                job_id=j.job_id,
                status=j.status,
                job_type=j.job_type,
                progress=j.progress,
                pages_scraped=j.pages_scraped,
                pages_failed=j.pages_failed,
                created_at=j.created_at,
                started_at=j.started_at,
                completed_at=j.completed_at,
                error_message=j.error_message,
            ).model_dump(mode="json")
            for j in jobs
        ],
        meta=MetaResponse(
            request_id=f"req_{uuid.uuid4().hex[:12]}",
            page=(offset // limit) + 1,
            per_page=limit,
            total=total,
        ),
    )
