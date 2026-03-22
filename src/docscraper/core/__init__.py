"""Core scraping and processing engines.

Classes:
    DocumentationScraper: Advanced async scraper with rate limiting and
        parallel crawling. Use for production scrape jobs.
    SimpleDocumentationScraper: Basic sequential scraper for quick,
        single-threaded documentation scraping.
    DocPostProcessor: Post-processes scraped markdown with AI classification
        and semantic chunking.
"""

from .scraper import DocumentationScraper
from .simple import SimpleDocumentationScraper

__all__ = [
    "DocumentationScraper",
    "SimpleDocumentationScraper",
]
