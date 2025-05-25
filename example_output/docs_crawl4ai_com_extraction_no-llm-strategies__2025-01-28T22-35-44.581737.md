# Developer Documentation
URL: https://docs.crawl4ai.com/extraction/no-llm-strategies/
Processed: 2025-01-28T22:35:44.581737

## Document Statistics
- Original Length: 24420 characters
- Generated Length: 6961 characters
- Content Ratio: 28.51%
- Code Blocks: 0

## Technical Analysis
# Crawl4AI Developer Guide

## 1. Overview and Purpose
Crawl4AI is designed to extract structured JSON data from websites without relying on large language models (LLMs). This approach allows developers to define schemas using CSS or XPath selectors, enabling efficient data extraction from complex or nested HTML structures.

### Core Functionality and Purpose
- **Schema-Based Extraction**: Define a schema to extract data efficiently.
- **No LLM Dependency**: Avoid the costs and latency associated with LLMs.
- **Structured Output**: Produce consistent JSON output for downstream processing.

### Key Capabilities and Limitations
- **Capabilities**:
  - Fast and cost-effective data extraction.
  - Precise control over the extraction process using CSS/XPath.
  - Scalable for large datasets.

- **Limitations**:
  - Requires well-defined schemas for effective extraction.
  - May not handle extremely unstructured data as effectively as LLMs.

### Target Use Cases
- E-commerce product catalogs.
- Blog post extraction.
- Data aggregation from structured websites.

## 2. Technical Implementation
Crawl4AI employs a modular architecture that separates concerns between crawling, extraction, and data management.

### Architecture and Design Patterns
- **Asynchronous Processing**: Utilizes asynchronous programming for efficient crawling.
- **Strategy Pattern**: Supports multiple extraction strategies (CSS and XPath).

### Component Interactions
- **Crawler**: Initiates requests and manages the crawling process.
- **Extraction Strategy**: Defines how data is extracted based on the provided schema.

### Data Flow and State Management
Data flows from the crawler to the extraction strategy, which processes the HTML content and outputs structured JSON.

## 3. Code Implementation

### Setup and Configuration
To set up Crawl4AI, ensure you have Python installed along with the required libraries. Install Crawl4AI using pip:

```bash
pip install crawl4ai
```

### Integration Steps
Integrate Crawl4AI into your application by importing the necessary classes and defining your extraction schema.

### Code Examples

#### Simple Example: Crypto Prices
Here’s a simple schema-based extraction using the `JsonCssExtractionStrategy`:

```python
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def extract_crypto_prices():
  # 1. Define a simple extraction schema
  schema = {
    "name": "Crypto Prices",
    "baseSelector": "div.crypto-row",  # Repeated elements
    "fields": [
      {
        "name": "coin_name",
        "selector": "h2.coin-name",
        "type": "text"
      },
      {
        "name": "price",
        "selector": "span.coin-price",
        "type": "text"
      }
    ]
  }
  # 2. Create the extraction strategy
  extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
  # 3. Set up your crawler config (if needed)
  config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    extraction_strategy=extraction_strategy,
  )
  async with AsyncWebCrawler(verbose=True) as crawler:
    # 4. Run the crawl and extraction
    result = await crawler.arun(
      url="https://example.com/crypto-prices",
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    # 5. Parse the extracted JSON
    data = json.loads(result.extracted_content)
    print(f"Extracted {len(data)} coin entries")
    print(json.dumps(data[0], indent=2) if data else "No data found")

asyncio.run(extract_crypto_prices())
```

#### XPath Example with `raw://` HTML
Here’s an example demonstrating XPath extraction:

```python
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonXPathExtractionStrategy

async def extract_crypto_prices_xpath():
  # 1. Minimal dummy HTML with some repeating rows
  dummy_html = """
  <html>
   <body>
    <div class='crypto-row'>
     <h2 class='coin-name'>Bitcoin</h2>
     <span class='coin-price'>$28,000</span>
    </div>
    <div class='crypto-row'>
     <h2 class='coin-name'>Ethereum</h2>
     <span class='coin-price'>$1,800</span>
    </div>
   </body>
  </html>
  """
  # 2. Define the JSON schema (XPath version)
  schema = {
    "name": "Crypto Prices via XPath",
    "baseSelector": "//div[@class='crypto-row']",
    "fields": [
      {
        "name": "coin_name",
        "selector": ".//h2[@class='coin-name']",
        "type": "text"
      },
      {
        "name": "price",
        "selector": ".//span[@class='coin-price']",
        "type": "text"
      }
    ]
  }
  # 3. Place the strategy in the CrawlerRunConfig
  config = CrawlerRunConfig(
    extraction_strategy=JsonXPathExtractionStrategy(schema, verbose=True)
  )
  # 4. Use raw:// scheme to pass dummy_html directly
  raw_url = f"raw://{dummy_html}"
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url=raw_url,
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    data = json.loads(result.extracted_content)
    print(f"Extracted {len(data)} coin rows")
    if data:
      print("First item:", data[0])

asyncio.run(extract_crypto_prices_xpath())
```

## 4. Advanced Usage

### Optimization Techniques
- Use specific selectors to minimize the amount of HTML processed.
- Leverage caching strategies to avoid redundant requests.

### Performance Considerations
- Monitor response times and optimize schemas for speed.
- Test schemas on smaller datasets before scaling up.

### Security Considerations
- Sanitize inputs to prevent injection attacks.
- Use secure connections (HTTPS) when making requests.

### Error Handling
Implement robust error handling to manage network issues or unexpected HTML structures gracefully.

## 5. Troubleshooting

### Common Issues
- Incorrect selectors leading to empty results.
- Network timeouts or connection errors.

### Debugging Strategies
- Enable verbose logging to trace issues during extraction.
- Test selectors in browser developer tools before implementing them in code.

### Known Limitations
- May struggle with highly dynamic content loaded via JavaScript.
- Complex nested structures may require careful schema design.

### Best Practices
- Start with simple schemas and gradually add complexity.
- Regularly review and update schemas as website structures change.

## Conclusion
Crawl4AI provides a powerful framework for extracting structured data from websites without relying on LLMs. By leveraging schema-based approaches with CSS or XPath, developers can efficiently scrape consistent data for various applications. 

Next steps include integrating extracted JSON with other processing tools or enhancing scraping capabilities for dynamic content. Enjoy building robust scrapers that deliver reliable results!

## Processing Metadata
- Source: terminal-mkdocs-main-content
- Type: developer_documentation
- URL: https://docs.crawl4ai.com/extraction/no-llm-strategies/
