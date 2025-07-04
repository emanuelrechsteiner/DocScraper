# Developer Documentation
URL: https://docs.crawl4ai.com/core/browser-crawler-config/
Processed: 2025-01-28T22:11:27.256368

## Document Statistics
- Original Length: 16096 characters
- Generated Length: 8173 characters
- Content Ratio: 50.78%
- Code Blocks: 0

## Technical Analysis
# Crawl4AI Developer Guide

## 1. Overview and Purpose
Crawl4AI is a powerful web crawling framework designed to facilitate the extraction of data from websites. Its core functionality revolves around two primary classes: `BrowserConfig` and `CrawlerRunConfig`, which dictate how the browser operates and how each crawl is executed, respectively.

### Key Capabilities
- **Flexible Browser Configuration**: Supports multiple browser types (Chromium, Firefox, WebKit) and modes (headless or visible).
- **Customizable Crawling Behavior**: Allows for detailed configuration of crawling parameters, including caching, extraction strategies, and JavaScript execution.
- **Rate Limiting and Resource Management**: Implements intelligent rate limiting to manage system resources effectively during batch processing.

### Limitations
- Requires a basic understanding of asynchronous programming in Python.
- Some advanced features may require additional setup or configuration.

### Target Use Cases
- Data extraction for research, analytics, or competitive analysis.
- Automated testing of web applications.
- Content aggregation from multiple sources.

## 2. Technical Implementation

### Architecture and Design Patterns
Crawl4AI employs an asynchronous architecture, leveraging Python's `asyncio` library to handle concurrent web requests efficiently. The design pattern focuses on separation of concerns, with distinct classes managing browser configuration and crawling behavior.

### Component Interactions
- **`AsyncWebCrawler`**: The main entry point for executing crawls. It utilizes the configurations provided by `BrowserConfig` and `CrawlerRunConfig`.
- **Extraction Strategies**: Custom strategies can be defined to tailor the data extraction process based on specific requirements.

### Data Flow and State Management
Data flows from the web through the configured browser, where it is processed according to the specified extraction strategy. State management is handled through the configuration objects, allowing for persistent settings across multiple crawl sessions.

## 3. Code Implementation

### Setup and Configuration
To get started with Crawl4AI, you need to configure your browser and crawler settings.

#### BrowserConfig Essentials
```python
class BrowserConfig:
  def __init__(
    browser_type="chromium",
    headless=True,
    proxy_config=None,
    viewport_width=1080,
    viewport_height=600,
    verbose=True,
    use_persistent_context=False,
    user_data_dir=None,
    cookies=None,
    headers=None,
    user_agent=None,
    text_mode=False,
    light_mode=False,
    extra_args=None,
    # ... other advanced parameters omitted here
  ):
    ...
```

#### Key Fields to Note
1. **`browser_type`**: Options: `"chromium"`, `"firefox"`, or `"webkit"`. Defaults to `"chromium"`.
2. **`headless`**: If `True`, runs the browser in headless mode.
3. **`proxy_config`**: A dictionary for proxy settings.
4. **`viewport_width` & `viewport_height`**: Initial window size.
5. **`verbose`**: If `True`, prints extra logs for debugging.

#### Minimal Example
```python
from crawl4ai import AsyncWebCrawler, BrowserConfig
browser_conf = BrowserConfig(
  browser_type="firefox",
  headless=False,
  text_mode=True
)
async with AsyncWebCrawler(config=browser_conf) as crawler:
  result = await crawler.arun("https://example.com")
  print(result.markdown[:300])
```

### CrawlerRunConfig Essentials
```python
class CrawlerRunConfig:
  def __init__(
    word_count_threshold=200,
    extraction_strategy=None,
    markdown_generator=None,
    cache_mode=None,
    js_code=None,
    wait_for=None,
    screenshot=False,
    pdf=False,
    enable_rate_limiting=False,
    rate_limit_config=None,
    memory_threshold_percent=70.0,
    check_interval=1.0,
    max_session_permit=20,
    display_mode=None,
    verbose=True,
    stream=False, # Enable streaming for arun_many()
    # ... other advanced parameters omitted
  ):
    ...
```

#### Key Fields to Note
1. **`word_count_threshold`**: Minimum word count for content blocks.
2. **`extraction_strategy`**: Defines how data is extracted.
3. **`cache_mode`**: Controls caching behavior.
4. **`js_code`**: JavaScript to execute during the crawl.

#### Minimal Example
```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
crawl_conf = CrawlerRunConfig(
  js_code="document.querySelector('button#loadMore')?.click()",
  wait_for="css:.loaded-content",
  screenshot=True,
  enable_rate_limiting=True,
  rate_limit_config=RateLimitConfig(
    base_delay=(1.0, 3.0),
    max_delay=60.0,
    max_retries=3,
    rate_limit_codes=[429, 503]
  ),
  stream=True # Enable streaming
)
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun(url="https://example.com", config=crawl_conf)
  print(result.screenshot[:100]) # Base64-encoded PNG snippet
```

### Putting It All Together
In a typical scenario, you define one `BrowserConfig` for your crawler session and create one or more `CrawlerRunConfig` depending on each call’s needs.
```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def main():
  # Browser config: headless, bigger viewport, no proxy
  browser_conf = BrowserConfig(
    headless=True,
    viewport_width=1280,
    viewport_height=720
  )
  
  # Example extraction strategy
  schema = {
    "name": "Articles",
    "baseSelector": "div.article",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  extraction = JsonCssExtractionStrategy(schema)
  
  # Crawler run config: skip cache, use extraction
  run_conf = CrawlerRunConfig(
    extraction_strategy=extraction,
    cache_mode=CacheMode.BYPASS,
    enable_rate_limiting=True,
    rate_limit_config=RateLimitConfig(
      base_delay=(1.0, 3.0),
      max_delay=60.0,
      max_retries=3,
      rate_limit_codes=[429, 503]
    )
  )
  
  async with AsyncWebCrawler(config=browser_conf) as crawler:
    # Execute the crawl
    result = await crawler.arun(url="https://example.com/news", config=run_conf)
    if result.success:
      print("Extracted content:", result.extracted_content)
    else:
      print("Error:", result.error_message)

if __name__ == "__main__":
  asyncio.run(main())
```

## 4. Advanced Usage

### Optimization Techniques
- Use headless mode for faster execution.
- Adjust `viewport_width` and `viewport_height` based on target site requirements.

### Performance Considerations
- Monitor memory usage with `memory_threshold_percent`.
- Use `check_interval` to balance performance with resource monitoring.

### Security Considerations
- Always validate external inputs when using JavaScript execution.
- Use secure proxy configurations to protect sensitive data.

### Error Handling
Implement robust error handling by checking the `result.success` flag after each crawl operation and logging errors appropriately.

## 5. Troubleshooting

### Common Issues
- **Timeout Errors**: Increase the timeout settings in `CrawlerRunConfig`.
- **Extraction Failures**: Verify the correctness of your extraction strategy schema.

### Debugging Strategies
- Enable verbose logging in both `BrowserConfig` and `CrawlerRunConfig`.
- Test configurations in isolation to identify issues.

### Known Limitations
- Some sites may block crawlers; consider using rotating proxies or user-agent randomization.

### Best Practices
- Regularly update your configurations based on site changes.
- Utilize caching effectively to reduce load times on repeated crawls.

## Conclusion
Crawl4AI provides a flexible framework for web crawling that allows developers to customize their crawling experience extensively. By utilizing `BrowserConfig` and `CrawlerRunConfig`, you can create efficient and maintainable crawling solutions tailored to your specific needs. For further details on available parameters and advanced features, refer to the [BrowserConfig and CrawlerRunConfig Reference](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>). Happy crawling!

## Processing Metadata
- Source: terminal-mkdocs-main-content
- Type: developer_documentation
- URL: https://docs.crawl4ai.com/core/browser-crawler-config/
