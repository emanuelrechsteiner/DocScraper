# Developer Documentation
URL: https://docs.crawl4ai.com/core/cache-modes/
Processed: 2025-01-28T22:11:41.250316

## Document Statistics
- Original Length: 6514 characters
- Generated Length: 2540 characters
- Content Ratio: 38.99%
- Code Blocks: 0

## Technical Analysis
# Crawl4AI Cache System and Migration Guide

## Overview
Starting from version 0.5.0, Crawl4AI introduces a new caching system that replaces the old boolean flags with a more intuitive `CacheMode` enum. This change simplifies cache control and makes the behavior more predictable.

## Old vs New Approach

### Old Way (Deprecated)
The old system used multiple boolean flags:
- `bypass_cache`: Skip cache entirely
- `disable_cache`: Disable all caching
- `no_cache_read`: Don't read from cache
- `no_cache_write`: Don't write to cache

### New Way (Recommended)
The new system uses a single `CacheMode` enum:
- `CacheMode.ENABLED`: Normal caching (read/write)
- `CacheMode.DISABLED`: No caching at all
- `CacheMode.READ_ONLY`: Only read from cache
- `CacheMode.WRITE_ONLY`: Only write to cache
- `CacheMode.BYPASS`: Skip cache for this operation

## Migration Example

### Old Code (Deprecated)
```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def use_proxy():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            bypass_cache=True # Old way
        )
        print(len(result.markdown))

async def main():
    await use_proxy()

if __name__ == "__main__":
    asyncio.run(main())
```

### New Code (Recommended)
```python
import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode
from crawl4ai.async_configs import CrawlerRunConfig

async def use_proxy():
    # Use CacheMode in CrawlerRunConfig
    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS) 
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=config # Pass the configuration object
        )
        print(len(result.markdown))

async def main():
    await use_proxy()

if __name__ == "__main__":
    asyncio.run(main())
```

## Common Migration Patterns

| Old Flag               | New Mode                          |
|-----------------------|-----------------------------------|
| `bypass_cache=True`   | `cache_mode=CacheMode.BYPASS`    |
| `disable_cache=True`  | `cache_mode=CacheMode.DISABLED`   |
| `no_cache_read=True`  | `cache_mode=CacheMode.WRITE_ONLY` |
| `no_cache_write=True` | `cache_mode=CacheMode.READ_ONLY`  |

Site built with [MkDocs](https://docs.crawl4ai.com/core/cache-modes/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/cache-modes/<https:/github.com/ntno/mkdocs-terminal>).

## Processing Metadata
- Source: terminal-mkdocs-main-content
- Type: developer_documentation
- URL: https://docs.crawl4ai.com/core/cache-modes/
