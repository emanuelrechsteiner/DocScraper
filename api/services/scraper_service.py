"""Scraper service — wraps existing scraping engines for API use."""

import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


class ScraperService:
    """Thin wrapper around DocumentationScraper for API integration.

    Args:
        output_base_dir: Base directory for all scrape job outputs.
    """

    def __init__(self, output_base_dir: Path = Path("scrape_output")) -> None:
        self.output_base_dir = output_base_dir
        self.output_base_dir.mkdir(parents=True, exist_ok=True)

    async def start_scrape(
        self,
        url: str,
        max_pages: int = 100,
        job_id: Optional[str] = None,
    ) -> dict[str, object]:
        """Start a scrape job using the existing DocumentationScraper engine.

        Args:
            url: Documentation website URL to scrape.
            max_pages: Maximum number of pages to scrape.
            job_id: Optional job identifier for output directory naming.

        Returns:
            Dict with scrape results summary including pages_scraped,
            pages_failed, output_dir, visited_urls, and failed_urls.

        Raises:
            RuntimeError: If the underlying scraper encounters a fatal error.
        """
        from docscraper.core.scraper import DocumentationScraper

        output_dir = self.output_base_dir / (job_id or "default")
        scraper = DocumentationScraper(output_dir=str(output_dir))

        logger.info(
            "Starting scrape job %s for %s (max %d pages)", job_id, url, max_pages
        )
        await scraper.scrape_documentation(start_url=url, max_pages=max_pages)

        return {
            "pages_scraped": len(scraper.visited_urls),
            "pages_failed": len(scraper.failed_urls),
            "output_dir": str(output_dir),
            "visited_urls": list(scraper.visited_urls),
            "failed_urls": list(scraper.failed_urls),
        }
