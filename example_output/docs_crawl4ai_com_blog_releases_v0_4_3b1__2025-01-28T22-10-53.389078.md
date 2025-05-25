# Developer Documentation
URL: https://docs.crawl4ai.com/blog/releases/v0.4.3b1/
Processed: 2025-01-28T22:10:53.389078

## Document Statistics
- Original Length: 8524 characters
- Generated Length: 5472 characters
- Content Ratio: 64.2%
- Code Blocks: 0

## Technical Analysis
# Crawl4AI Developer Guide (v0.4.3)

## 1. Overview and Purpose

Crawl4AI is a powerful web crawling framework designed to enhance the efficiency and effectiveness of data extraction from web pages. The core functionality revolves around intelligent resource management, real-time monitoring, and advanced scraping techniques. 

### Key Capabilities
- **Memory-Adaptive Dispatcher System**: Optimizes resource usage based on current memory consumption.
- **LLM Integration**: Leverages large language models for enhanced content filtering and schema generation.
- **Real-Time Processing**: Allows for immediate processing of crawled URLs.

### Limitations
- Requires a stable internet connection for optimal performance.
- Performance may vary based on the complexity of the target websites.

### Target Use Cases
- Data extraction for research purposes.
- Content aggregation for news or blogs.
- E-commerce product scraping.

## 2. Technical Implementation

### Architecture and Design Patterns
Crawl4AI employs an asynchronous architecture that allows for concurrent URL processing, significantly improving crawling speed and efficiency. The design pattern follows a dispatcher model that intelligently manages crawling sessions based on system resources.

### Component Interactions
The main components include:
- **AsyncWebCrawler**: The core class responsible for initiating crawls.
- **MemoryAdaptiveDispatcher**: Manages the allocation of resources dynamically.
- **CrawlerMonitor**: Provides real-time feedback on the crawling process.

### Data Flow and State Management
Data flows from the target URLs through the dispatcher, which manages the state of each crawl session. Results are processed in real-time, allowing for immediate feedback and adjustments.

## 3. Code Implementation

### Setup and Configuration
To get started with Crawl4AI, install the package using pip:

```bash
pip install -U crawl4ai
```

### Integration Steps
Integrate Crawl4AI into your project by importing the necessary classes and configuring your crawler.

### Code Examples

#### Memory-Adaptive Dispatcher System
```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DisplayMode
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher, CrawlerMonitor

async def main():
  urls = ["https://example1.com", "https://example2.com"] * 50
  # Configure memory-aware dispatch
  dispatcher = MemoryAdaptiveDispatcher(
    memory_threshold_percent=80.0, # Auto-throttle at 80% memory
    check_interval=0.5,       # Check every 0.5 seconds
    max_session_permit=20,     # Max concurrent sessions
    monitor=CrawlerMonitor(     # Real-time monitoring
      display_mode=DisplayMode.DETAILED
    )
  )
  async with AsyncWebCrawler() as crawler:
    results = await dispatcher.run_urls(
      urls=urls,
      crawler=crawler,
      config=CrawlerRunConfig()
    )
```

#### Streaming Support
```python
config = CrawlerRunConfig(stream=True)
async with AsyncWebCrawler() as crawler:
  async for result in await crawler.arun_many(urls, config=config):
    print(f"Got result for {result.url}")
    # Process each result immediately
```

#### LXML-Based Scraping
```python
config = CrawlerRunConfig(
  scraping_strategy=LXMLWebScrapingStrategy(),
  cache_mode=CacheMode.ENABLED
)
```

#### LLM-Powered Markdown Generation
```python
config = CrawlerRunConfig(
  markdown_generator=DefaultMarkdownGenerator(
    content_filter=LLMContentFilter(
      provider="openai/gpt-4o",
      instruction="Extract technical documentation and code examples"
    )
  )
)
```

#### Automatic Schema Generation
```python
schema = JsonCssExtractionStrategy.generate_schema(
  html_content,
  schema_type="CSS",
  query="Extract product name, price, and description"
)
```

#### Proxy Support & Rotation
```python
config = CrawlerRunConfig(
  proxy_config={
    "server": "http://proxy:8080",
    "username": "user",
    "password": "pass"
  }
)
```

#### Robots.txt Compliance
```python
config = CrawlerRunConfig(check_robots_txt=True)
result = await crawler.arun(url, config=config)
if result.status_code == 403:
  print("Access blocked by robots.txt")
```

#### URL Redirection Tracking
```python
result = await crawler.arun(url)
print(f"Initial URL: {url}")
print(f"Final URL: {result.redirected_url}")
```

## 4. Advanced Usage

### Optimization Techniques
Utilize the memory-adaptive dispatcher to optimize resource usage during large crawls.

### Performance Considerations
- Monitor memory usage to avoid throttling.
- Use LXML scraping for faster parsing.

### Security Considerations
Ensure that proxy configurations are secure and that sensitive information is not exposed.

### Error Handling
Implement robust error handling to manage HTTP errors and connection issues gracefully.

## 5. Troubleshooting

### Common Issues
- Crawling may fail due to robots.txt restrictions.
- Memory issues can arise if too many concurrent sessions are initiated.

### Debugging Strategies
Utilize the `CrawlerMonitor` to gain insights into the crawling process and identify bottlenecks.

### Known Limitations
- Some websites may block crawlers; consider using proxies or rotating user agents.

### Best Practices
- Always check robots.txt before crawling.
- Limit concurrent sessions based on available system resources.

For complete examples, check our [demo repository](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/<https:/github.com/unclecode/crawl4ai/examples>).

Happy crawling! 🕷️

## Processing Metadata
- Source: terminal-mkdocs-main-content
- Type: developer_documentation
- URL: https://docs.crawl4ai.com/blog/releases/v0.4.3b1/
