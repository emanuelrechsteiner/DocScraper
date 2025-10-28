#!/usr/bin/env python3
"""
Scraper Factory
Creates the appropriate scraper based on configuration.
"""

import logging
from typing import Optional

from scraper_config import ScraperConfig
from DocScraper import DocumentationScraper
from firecrawl_scraper import FirecrawlDocumentationScraper

logger = logging.getLogger(__name__)


class ScraperFactory:
    """Factory for creating documentation scrapers."""

    @staticmethod
    def create_scraper(output_dir: str = "scraped_docs", config: Optional[ScraperConfig] = None):
        """
        Create a documentation scraper based on configuration.

        Args:
            output_dir: Directory to save scraped content
            config: Configuration object (if None, will create new one)

        Returns:
            DocumentationScraper or FirecrawlDocumentationScraper instance

        Raises:
            ValueError: If configuration is invalid
        """
        if config is None:
            config = ScraperConfig()

        engine = config.get_scraper_engine()

        logger.info(f"Creating scraper with engine: {engine}")

        if engine == ScraperConfig.ENGINE_CRAWL4AI:
            # Use crawl4ai (free, open source)
            logger.info("Using Crawl4AI scraper (free)")
            return DocumentationScraper(output_dir)

        elif engine == ScraperConfig.ENGINE_FIRECRAWL:
            # Use Firecrawl API
            api_key = config.get_firecrawl_api_key()

            if not api_key or not api_key.strip():
                raise ValueError(
                    "Firecrawl API key is required but not configured. "
                    "Please go to Settings and enter your Firecrawl API key."
                )

            logger.info("Using Firecrawl scraper (API)")
            return FirecrawlDocumentationScraper(api_key, output_dir)

        else:
            raise ValueError(f"Unknown scraper engine: {engine}")

    @staticmethod
    def get_scraper_info(config: Optional[ScraperConfig] = None) -> dict:
        """
        Get information about the configured scraper.

        Args:
            config: Configuration object (if None, will create new one)

        Returns:
            Dictionary with scraper information
        """
        if config is None:
            config = ScraperConfig()

        engine = config.get_scraper_engine()
        is_configured = True
        message = ""

        if engine == ScraperConfig.ENGINE_CRAWL4AI:
            message = "Using Crawl4AI (Free, Open Source)"

        elif engine == ScraperConfig.ENGINE_FIRECRAWL:
            if config.is_firecrawl_configured():
                message = "Using Firecrawl API (Configured)"
            else:
                is_configured = False
                message = "Firecrawl selected but API key not configured"

        return {
            'engine': engine,
            'is_configured': is_configured,
            'message': message
        }
