#!/usr/bin/env python3
"""
Firecrawl Documentation Scraper
Uses Firecrawl API to scrape documentation websites.
"""

import asyncio
import os
import re
import json
import logging
from datetime import datetime
from urllib.parse import urljoin, urlparse
from typing import Set, List, Dict, Optional
from pathlib import Path

from firecrawl import FirecrawlApp
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class FirecrawlDocumentationScraper:
    """Scrapes documentation websites using Firecrawl API."""

    def __init__(self, api_key: str, output_dir: str = "scraped_docs"):
        """
        Initialize Firecrawl scraper.

        Args:
            api_key: Firecrawl API key
            output_dir: Directory to save scraped content
        """
        self.api_key = api_key
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.visited_urls: Set[str] = set()
        self.failed_urls: Set[str] = set()
        self.domain = None
        self.firecrawl = None

        # Initialize Firecrawl
        try:
            self.firecrawl = FirecrawlApp(api_key=api_key)
            logger.info("Firecrawl API initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Firecrawl: {e}")
            raise

    def _is_valid_doc_url(self, url: str) -> bool:
        """Check if URL is a valid documentation page."""
        if not url or not self.domain:
            return False

        parsed = urlparse(url)

        # Must be same domain
        if parsed.netloc != self.domain:
            return False

        # Skip non-documentation URLs
        skip_patterns = [
            r'/api/', r'/login', r'/signup', r'/auth/',
            r'\.pdf$', r'\.zip$', r'\.tar\.gz$',
            r'#', r'mailto:', r'javascript:',
            r'/download/', r'/releases/download/'
        ]

        for pattern in skip_patterns:
            if re.search(pattern, url.lower()):
                return False

        return True

    def _clean_filename(self, url: str) -> str:
        """Convert URL to a safe filename."""
        parsed = urlparse(url)
        path = parsed.path.strip('/')

        if not path:
            path = "index"

        # Replace special characters
        filename = re.sub(r'[^\w\-_\.]', '_', path)
        filename = re.sub(r'_+', '_', filename)

        if not filename.endswith('.md'):
            filename += '.md'

        return filename

    def _extract_internal_links(self, content: str, base_url: str) -> List[str]:
        """
        Extract all internal documentation links from content.

        Args:
            content: HTML or markdown content
            base_url: Base URL for resolving relative links

        Returns:
            List of absolute URLs
        """
        links = set()

        # Try to extract links from HTML if present
        try:
            soup = BeautifulSoup(content, 'html.parser')
            for tag in soup.find_all('a'):
                href = tag.get('href')
                if href:
                    absolute_url = urljoin(base_url, href)
                    if self._is_valid_doc_url(absolute_url):
                        # Remove fragments and normalize
                        parsed = urlparse(absolute_url)
                        clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                        if parsed.query:
                            clean_url += f"?{parsed.query}"
                        links.add(clean_url)
        except Exception as e:
            logger.debug(f"Could not extract links from content: {e}")

        return list(links)

    def _save_content(self, url: str, content: str, metadata: Dict) -> str:
        """Save content to markdown file."""
        filename = self._clean_filename(url)
        filepath = self.output_dir / filename

        # Create subdirectories if needed
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Add metadata header
        markdown_content = f"""---
url: {url}
scraped_at: {metadata.get('scraped_at', datetime.now().isoformat())}
title: {metadata.get('title', 'Untitled')}
scraper: firecrawl
---

{content}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        return str(filepath)

    async def scrape_page(self, url: str) -> Optional[Dict]:
        """
        Scrape a single page using Firecrawl.

        Args:
            url: URL to scrape

        Returns:
            Dictionary with scraping results or None if failed
        """
        try:
            # Add delay to avoid rate limiting
            await asyncio.sleep(1)

            logger.info(f"Scraping with Firecrawl: {url}")

            # Use Firecrawl to scrape the page
            result = self.firecrawl.scrape_url(
                url,
                params={
                    'formats': ['markdown', 'html'],
                    'onlyMainContent': True
                }
            )

            if not result or not result.get('success', False):
                error = result.get('error', 'Unknown error') if result else 'No result'
                logger.error(f"Failed to scrape {url}: {error}")
                self.failed_urls.add(url)
                return None

            # Extract content
            markdown_content = result.get('markdown', '')
            html_content = result.get('html', '')
            metadata = result.get('metadata', {})

            if not markdown_content and not html_content:
                logger.warning(f"No content extracted from {url}")
                return None

            # Prefer markdown content
            content = markdown_content if markdown_content else html_content

            # Extract internal links for further crawling
            internal_links = self._extract_internal_links(html_content or content, url)

            # Get page title
            title = metadata.get('title', 'Untitled')

            # Save the content
            save_metadata = {
                'scraped_at': datetime.now().isoformat(),
                'title': title,
                'links_found': len(internal_links)
            }

            filepath = self._save_content(url, content, save_metadata)

            logger.info(f"Saved {url} -> {filepath} (found {len(internal_links)} links)")

            return {
                'url': url,
                'links': internal_links,
                'filepath': filepath
            }

        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            self.failed_urls.add(url)
            return None

    async def scrape_documentation(self, start_url: str, max_pages: int = 1000):
        """
        Scrape entire documentation website starting from a URL.

        Args:
            start_url: Starting URL for scraping
            max_pages: Maximum number of pages to scrape
        """
        # Parse domain
        parsed = urlparse(start_url)
        self.domain = parsed.netloc

        logger.info(f"Starting Firecrawl documentation scrape for domain: {self.domain}")
        logger.info(f"Output directory: {self.output_dir}")

        # URLs to process
        urls_to_crawl = {start_url}
        self.visited_urls = set()

        while urls_to_crawl and len(self.visited_urls) < max_pages:
            # Get next URL
            url = urls_to_crawl.pop()

            if url in self.visited_urls:
                continue

            logger.info(f"Scraping page {len(self.visited_urls) + 1}/{max_pages}: {url}")

            # Scrape the page
            result = await self.scrape_page(url)

            if result:
                self.visited_urls.add(result['url'])

                # Add new links to queue
                for link in result['links']:
                    if link not in self.visited_urls and link not in self.failed_urls:
                        urls_to_crawl.add(link)

            # Progress update
            if len(self.visited_urls) % 10 == 0:
                logger.info(f"Progress: {len(self.visited_urls)} pages scraped, "
                          f"{len(urls_to_crawl)} in queue, "
                          f"{len(self.failed_urls)} failed")

        # Save crawl summary
        summary = {
            'start_url': start_url,
            'domain': self.domain,
            'scraper': 'firecrawl',
            'total_pages_scraped': len(self.visited_urls),
            'failed_urls': list(self.failed_urls),
            'visited_urls': list(self.visited_urls),
            'scrape_completed_at': datetime.now().isoformat()
        }

        summary_path = self.output_dir / '_scrape_summary.json'
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)

        logger.info(f"\nScraping completed!")
        logger.info(f"Total pages scraped: {len(self.visited_urls)}")
        logger.info(f"Failed URLs: {len(self.failed_urls)}")
        logger.info(f"Summary saved to: {summary_path}")
