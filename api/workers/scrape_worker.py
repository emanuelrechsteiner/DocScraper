"""ARQ background job workers (#19).

Defines async task functions that process scrape and process jobs
in the background. Workers are managed by ARQ (Redis-backed).

See ADR-003 for design rationale.

Usage:
    arq api.workers.scrape_worker.WorkerSettings
"""

import logging
from datetime import datetime, timezone
from typing import Any

from ..models.schemas import JobStatus
from ..services.job_store import job_store
from ..services.webhook import webhook_service

logger = logging.getLogger(__name__)


async def run_scrape_job(ctx: dict[str, Any], job_id: str) -> dict[str, Any]:
    """Execute a scrape job in the background.

    Args:
        ctx: ARQ worker context (contains Redis connection).
        job_id: The job to execute.

    Returns:
        Dict with scrape results.
    """
    job = job_store.get_job(job_id)
    if job is None:
        logger.error("Scrape job %s not found in store", job_id)
        return {"error": "Job not found"}

    now = datetime.now(timezone.utc)
    job_store.update_job(job_id, status=JobStatus.RUNNING, started_at=now)
    logger.info("Starting scrape job %s for %s", job_id, job.url)

    try:
        from ..services.scraper_service import ScraperService

        service = ScraperService()
        result = await service.start_scrape(
            url=job.url, max_pages=job.max_pages, job_id=job_id
        )

        job_store.update_job(
            job_id,
            status=JobStatus.COMPLETED,
            completed_at=datetime.now(timezone.utc),
            pages_scraped=result.get("pages_scraped", 0),
            pages_failed=result.get("pages_failed", 0),
            output_files=list(result.get("visited_urls", [])),
            summary=result,
            progress=100.0,
        )
        logger.info("Scrape job %s completed: %d pages", job_id, result.get("pages_scraped", 0))

        # Send webhook callback if URL was provided (#22)
        if job.webhook_url:
            await webhook_service.send_job_completed(
                webhook_url=job.webhook_url,
                job_id=job_id,
                status=JobStatus.COMPLETED,
                result=result,
            )

        return result

    except Exception as exc:
        error_msg = str(exc)
        job_store.update_job(
            job_id,
            status=JobStatus.FAILED,
            completed_at=datetime.now(timezone.utc),
            error_message=error_msg,
        )
        logger.error("Scrape job %s failed: %s", job_id, error_msg, exc_info=True)

        if job.webhook_url:
            await webhook_service.send_job_failed(
                webhook_url=job.webhook_url,
                job_id=job_id,
                error_message=error_msg,
            )

        return {"error": error_msg}


async def run_process_job(ctx: dict[str, Any], job_id: str) -> dict[str, Any]:
    """Execute a document processing job in the background.

    Args:
        ctx: ARQ worker context.
        job_id: The job to execute.

    Returns:
        Dict with processing results.
    """
    job = job_store.get_job(job_id)
    if job is None:
        logger.error("Process job %s not found in store", job_id)
        return {"error": "Job not found"}

    now = datetime.now(timezone.utc)
    job_store.update_job(job_id, status=JobStatus.RUNNING, started_at=now)
    logger.info("Starting process job %s for %s", job_id, job.url)

    try:
        from pathlib import Path

        from docscraper.core.processor import DocPostProcessor

        input_dir = Path(job.url)
        output_dir = Path("process_output") / job_id
        output_dir.mkdir(parents=True, exist_ok=True)

        processor = DocPostProcessor(
            input_dir=str(input_dir),
            output_dir=str(output_dir),
        )
        await processor.process_all()

        result = {
            "input_dir": str(input_dir),
            "output_dir": str(output_dir),
            "status": "completed",
        }

        job_store.update_job(
            job_id,
            status=JobStatus.COMPLETED,
            completed_at=datetime.now(timezone.utc),
            summary=result,
            progress=100.0,
        )
        logger.info("Process job %s completed", job_id)

        if job.webhook_url:
            await webhook_service.send_job_completed(
                webhook_url=job.webhook_url,
                job_id=job_id,
                status=JobStatus.COMPLETED,
                result=result,
            )

        return result

    except Exception as exc:
        error_msg = str(exc)
        job_store.update_job(
            job_id,
            status=JobStatus.FAILED,
            completed_at=datetime.now(timezone.utc),
            error_message=error_msg,
        )
        logger.error("Process job %s failed: %s", job_id, error_msg, exc_info=True)

        if job.webhook_url:
            await webhook_service.send_job_failed(
                webhook_url=job.webhook_url,
                job_id=job_id,
                error_message=error_msg,
            )

        return {"error": error_msg}


class WorkerSettings:
    """ARQ worker configuration.

    Start the worker with:
        arq api.workers.scrape_worker.WorkerSettings
    """

    functions = [run_scrape_job, run_process_job]
    redis_settings = None  # Will use default localhost:6379

    # Job settings
    max_jobs = 5
    job_timeout = 1800  # 30 minutes max per job
    keep_result = 86400  # Keep results for 24 hours
