#!/usr/bin/env python3
"""
Scraper Configuration Manager
Handles scraper settings and API keys stored in .env file.
"""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv, set_key, find_dotenv


class ScraperConfig:
    """Manages scraper configuration and settings."""

    # Scraper engine options
    ENGINE_CRAWL4AI = "crawl4ai"
    ENGINE_FIRECRAWL = "firecrawl"

    def __init__(self):
        """Initialize configuration manager."""
        self.env_path = Path(".env")

        # Create .env if it doesn't exist
        if not self.env_path.exists():
            self.env_path.touch()

        # Load environment variables
        load_dotenv(self.env_path)

    def get_scraper_engine(self) -> str:
        """Get the currently configured scraper engine."""
        engine = os.getenv("SCRAPER_ENGINE", self.ENGINE_CRAWL4AI)

        # Validate engine
        if engine not in [self.ENGINE_CRAWL4AI, self.ENGINE_FIRECRAWL]:
            return self.ENGINE_CRAWL4AI

        return engine

    def set_scraper_engine(self, engine: str) -> bool:
        """
        Set the scraper engine.

        Args:
            engine: Either 'crawl4ai' or 'firecrawl'

        Returns:
            True if successful, False otherwise
        """
        if engine not in [self.ENGINE_CRAWL4AI, self.ENGINE_FIRECRAWL]:
            return False

        self._set_env_value("SCRAPER_ENGINE", engine)
        return True

    def get_firecrawl_api_key(self) -> Optional[str]:
        """Get the Firecrawl API key."""
        return os.getenv("FIRECRAWL_API_KEY")

    def set_firecrawl_api_key(self, api_key: str) -> bool:
        """
        Set the Firecrawl API key.

        Args:
            api_key: The Firecrawl API key

        Returns:
            True if successful, False otherwise
        """
        if not api_key or not api_key.strip():
            return False

        self._set_env_value("FIRECRAWL_API_KEY", api_key.strip())
        return True

    def get_openai_api_key(self) -> Optional[str]:
        """Get the OpenAI API key (for post-processing)."""
        return os.getenv("OPENAI_API_KEY")

    def set_openai_api_key(self, api_key: str) -> bool:
        """
        Set the OpenAI API key.

        Args:
            api_key: The OpenAI API key

        Returns:
            True if successful, False otherwise
        """
        if not api_key or not api_key.strip():
            return False

        self._set_env_value("OPENAI_API_KEY", api_key.strip())
        return True

    def _set_env_value(self, key: str, value: str):
        """
        Set a value in the .env file.

        Args:
            key: The environment variable key
            value: The value to set
        """
        # Use dotenv's set_key to update .env file
        set_key(str(self.env_path), key, value)

        # Also update the current environment
        os.environ[key] = value

    def is_firecrawl_configured(self) -> bool:
        """Check if Firecrawl is properly configured."""
        api_key = self.get_firecrawl_api_key()
        return api_key is not None and len(api_key.strip()) > 0

    def get_config_summary(self) -> dict:
        """Get a summary of current configuration."""
        engine = self.get_scraper_engine()

        return {
            "scraper_engine": engine,
            "firecrawl_configured": self.is_firecrawl_configured(),
            "openai_configured": self.get_openai_api_key() is not None,
            "can_use_firecrawl": engine == self.ENGINE_FIRECRAWL and self.is_firecrawl_configured()
        }


# Global config instance
config = ScraperConfig()
