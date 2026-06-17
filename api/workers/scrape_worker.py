"""ARQ background job workers (#19).

Defines async task functions that process scrape and process jobs
in the background. Workers are managed by ARQ (Redis-backed).

Workers run outside of the FastAPI request context, so they create
their own database sessions via ``async_session_factory()``.

See ADR-003 for design rationale.

Usage:
    arq api.workers.scrape_worker.WorkerSettings
"""

import logging
from datetime import datetime, timezone
from typing import Any

from ..db.engine import async_session_factory
from ..db.repositories import JobRepository
from ..models.schemas import JobStatus
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
    factory = async_session_factory()
    async with factory() as session:
        repo = JobRepository(session)
        job = await repo.get(job_id)
        if job is None:
            logger.error("Scrape job %s not found in store", job_id)
            return {"error": "Job not found"}

        if not job.url:
            logger.error("Scrape job %s has no target URL", job_id)
            await repo.update(
                job_id, status=JobStatus.FAILED.value, error="Missing target URL"
            )
            return {"error": "Job has no URL"}

        now = datetime.now(timezone.utc)
        await repo.update(job_id, status=JobStatus.RUNNING.value, started_at=now)
        logger.info("Starting scrape job %s for %s", job_id, job.url)

        try:
            from ..services.scraper_service import ScraperService

            service = ScraperService()
            result = await service.start_scrape(
                url=job.url,
                max_pages=job.max_pages if job.max_pages is not None else 100,
                job_id=job_id,
            )

            await repo.update(
                job_id,
                status=JobStatus.COMPLETED.value,
                completed_at=datetime.now(timezone.utc),
                pages_scraped=result.get("pages_scraped", 0),
                pages_failed=result.get("pages_failed", 0),
                output_files=list(result.get("visited_urls", [])),
                summary=result,
                progress=100.0,
            )
            await session.commit()
            logger.info(
                "Scrape job %s completed: %d pages",
                job_id,
                result.get("pages_scraped", 0),
            )

            webhook_url = job.webhook_url
            if webhook_url:
                await webhook_service.send_job_completed(
                    webhook_url=webhook_url,
                    job_id=job_id,
                    status=JobStatus.COMPLETED,
                    result=result,
                )

            return result

        except Exception as exc:
            error_msg = str(exc)
            await repo.update(
                job_id,
                status=JobStatus.FAILED.value,
                completed_at=datetime.now(timezone.utc),
                error_message=error_msg,
            )
            await session.commit()
            logger.error(
                "Scrape job %s failed: %s", job_id, error_msg, exc_info=True
            )

            webhook_url = job.webhook_url
            if webhook_url:
                await webhook_service.send_job_failed(
                    webhook_url=webhook_url,
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
    factory = async_session_factory()
    async with factory() as session:
        repo = JobRepository(session)
        job = await repo.get(job_id)
        if job is None:
            logger.error("Process job %s not found in store", job_id)
            return {"error": "Job not found"}

        if not job.url:
            logger.error("Process job %s has no input directory", job_id)
            await repo.update(
                job_id, status=JobStatus.FAILED.value, error="Missing input path"
            )
            return {"error": "Job has no input path"}

        now = datetime.now(timezone.utc)
        await repo.update(job_id, status=JobStatus.RUNNING.value, started_at=now)
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

            await repo.update(
                job_id,
                status=JobStatus.COMPLETED.value,
                completed_at=datetime.now(timezone.utc),
                summary=result,
                progress=100.0,
            )
            await session.commit()
            logger.info("Process job %s completed", job_id)

            webhook_url = job.webhook_url
            if webhook_url:
                await webhook_service.send_job_completed(
                    webhook_url=webhook_url,
                    job_id=job_id,
                    status=JobStatus.COMPLETED,
                    result=result,
                )

            return result

        except Exception as exc:
            error_msg = str(exc)
            await repo.update(
                job_id,
                status=JobStatus.FAILED.value,
                completed_at=datetime.now(timezone.utc),
                error_message=error_msg,
            )
            await session.commit()
            logger.error(
                "Process job %s failed: %s", job_id, error_msg, exc_info=True
            )

            webhook_url = job.webhook_url
            if webhook_url:
                await webhook_service.send_job_failed(
                    webhook_url=webhook_url,
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
