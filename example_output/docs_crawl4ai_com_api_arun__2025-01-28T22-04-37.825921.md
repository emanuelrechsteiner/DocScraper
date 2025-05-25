# Developer Documentation
URL: https://docs.crawl4ai.com/api/arun/
Processed: 2025-01-28T22:04:37.825921

## Document Statistics
- Original Length: 13168 characters
- Generated Length: 8301 characters
- Content Ratio: 63.04%
- Code Blocks: 0

## Technical Analysis
# Crawl4AI Developer Guide

## 1. Overview and Purpose

Crawl4AI is a powerful web crawling framework designed to facilitate the extraction of content from websites. Its core functionality revolves around the ability to navigate web pages, execute JavaScript, and extract structured data efficiently. 

### Key Capabilities and Limitations
- **Capabilities**:
  - Asynchronous crawling with support for JavaScript execution.
  - Flexible configuration options for caching, content filtering, and session management.
  - Built-in strategies for data extraction using CSS selectors and LLM-based approaches.

- **Limitations**:
  - May encounter restrictions from websites that employ anti-bot measures.
  - Performance can vary based on the complexity of the target website and the configuration used.

### Target Use Cases
- Data scraping for research and analytics.
- Automated testing of web applications.
- Content aggregation from multiple sources.

## 2. Technical Implementation

### Architecture and Design Patterns
Crawl4AI employs an asynchronous architecture, allowing multiple web pages to be crawled simultaneously. The design pattern follows a modular approach where different components handle specific tasks such as navigation, data extraction, and session management.

### Component Interactions
The main components include:
- **AsyncWebCrawler**: Manages the crawling process.
- **CrawlerRunConfig**: Encapsulates configuration settings for each crawl.
- **Extraction Strategies**: Define how data is extracted from the crawled pages.

### Data Flow and State Management
Data flows from the web page through the crawler, which processes it according to the specified configuration. State management is handled through session IDs, allowing continuity across multiple requests.

## 3. Code Implementation

### Setup and Configuration
To get started with Crawl4AI, ensure you have Python installed along with the necessary dependencies. You can install Crawl4AI via pip:

```bash
pip install crawl4ai
```

### Integration Steps
Integrate Crawl4AI into your project by importing the necessary classes:

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
```

### All Code Examples

#### Core Usage
```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  run_config = CrawlerRunConfig(
    verbose=True,      # Detailed logging
    cache_mode=CacheMode.ENABLED, # Use normal read/write cache
    check_robots_txt=True,  # Respect robots.txt rules
    # ... other parameters
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_config
    )
    # Check if blocked by robots.txt
    if not result.success and result.status_code == 403:
      print(f"Error: {result.error_message}")
```

#### Cache Control
```python
run_config = CrawlerRunConfig(
  cache_mode=CacheMode.BYPASS
)
```

#### Content Processing & Selection

##### Text Processing
```python
run_config = CrawlerRunConfig(
  word_count_threshold=10,  # Ignore text blocks <10 words
  only_text=False,      # If True, tries to remove non-text elements
  keep_data_attributes=False # Keep or discard data-* attributes
)
```

##### Content Selection
```python
run_config = CrawlerRunConfig(
  css_selector=".main-content", # Focus on .main-content region only
  excluded_tags=["form", "nav"], # Remove entire tag blocks
  remove_forms=True,       # Specifically strip <form> elements
  remove_overlay_elements=True, # Attempt to remove modals/popups
)
```

##### Link Handling
```python
run_config = CrawlerRunConfig(
  exclude_external_links=True,     # Remove external links from final content
  exclude_social_media_links=True,   # Remove links to known social sites
  exclude_domains=["ads.example.com"], # Exclude links to these domains
  exclude_social_media_domains=["facebook.com","twitter.com"], # Extend the default list
)
```

##### Media Filtering
```python
run_config = CrawlerRunConfig(
  exclude_external_images=True # Strip images from other domains
)
```

#### Page Navigation & Timing

##### Basic Browser Flow
```python
run_config = CrawlerRunConfig(
  wait_for="css:.dynamic-content", # Wait for .dynamic-content
  delay_before_return_html=2.0,  # Wait 2s before capturing final HTML
  page_timeout=60000,       # Navigation & script timeout (ms)
)
```

##### JavaScript Execution
```python
run_config = CrawlerRunConfig(
  js_code=[
    "window.scrollTo(0, document.body.scrollHeight);",
    "document.querySelector('.load-more')?.click();"
  ],
  js_only=False
)
```

##### Anti-Bot Measures
```python
run_config = CrawlerRunConfig(
  magic=True,
  simulate_user=True,
  override_navigator=True
)
```

#### Session Management
```python
run_config = CrawlerRunConfig(
  session_id="my_session123"
)
```

#### Screenshot, PDF & Media Options
```python
run_config = CrawlerRunConfig(
  screenshot=True,       # Grab a screenshot as base64
  screenshot_wait_for=1.0,   # Wait 1s before capturing
  pdf=True,          # Also produce a PDF
  image_description_min_word_threshold=5, # If analyzing alt text
  image_score_threshold=3,        # Filter out low-score images
)
```

#### Extraction Strategy
```python
run_config = CrawlerRunConfig(
  extraction_strategy=my_css_or_llm_strategy
)
```

#### Comprehensive Example
```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def main():
  schema = {
    "name": "Articles",
    "baseSelector": "article.post",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  
  run_config = CrawlerRunConfig(
    verbose=True,
    cache_mode=CacheMode.ENABLED,
    check_robots_txt=True,
    word_count_threshold=10,
    css_selector="main.content",
    excluded_tags=["nav", "footer"],
    exclude_external_links=True,
    js_code="document.querySelector('.show-more')?.click();",
    wait_for="css:.loaded-block",
    page_timeout=30000,
    extraction_strategy=JsonCssExtractionStrategy(schema),
    session_id="persistent_session",
    screenshot=True,
    pdf=True,
    simulate_user=True,
    magic=True,
  )
  
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com/posts", config=run_config)
    
    if result.success:
      print("HTML length:", len(result.cleaned_html))
      print("Extraction JSON:", result.extracted_content)
      if result.screenshot:
        print("Screenshot length:", len(result.screenshot))
      if result.pdf:
        print("PDF bytes length:", len(result.pdf))
    else:
      print("Error:", result.error_message)

if __name__ == "__main__":
  asyncio.run(main())
```

## 4. Advanced Usage

### Optimization Techniques
- Utilize caching effectively to reduce load times.
- Adjust concurrency settings based on server response times.

### Performance Considerations
- Monitor response times and adjust `page_timeout` accordingly.
- Use `wait_for` judiciously to ensure all dynamic content is loaded.

### Security Considerations
- Always respect `robots.txt` rules to avoid legal issues.
- Implement proper error handling to manage failed requests gracefully.

### Error Handling
Utilize the `result` object to check for errors after each crawl attempt. Implement retries for transient errors.

## 5. Troubleshooting

### Common Issues
- Blocked requests due to anti-bot measures.
- Missing content due to incorrect CSS selectors.

### Debugging Strategies
- Enable verbose logging in `CrawlerRunConfig` to track the crawling process.
- Test CSS selectors independently in browser developer tools.

### Known Limitations
- Some websites may have aggressive anti-scraping measures that can block requests.
- Dynamic content may not load if JavaScript execution is not properly configured.

### Best Practices
- Regularly update your extraction strategies based on changes in website structures.
- Document your configurations for easier maintenance and updates.

Happy crawling with your structured, flexible config approach! For a full reference, check out the [CrawlerRunConfig Docs](https://docs.crawl4ai.com/api/arun/<../parameters/>).

## Processing Metadata
- Source: terminal-mkdocs-main-content
- Type: developer_documentation
- URL: https://docs.crawl4ai.com/api/arun/
