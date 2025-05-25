# Developer Documentation
URL: https://docs.crawl4ai.com/core/markdown-generation/
Processed: 2025-01-28T22:16:29.464921

## Document Statistics
- Original Length: 24303 characters
- Generated Length: 7131 characters
- Content Ratio: 29.34%
- Code Blocks: 0

## Technical Analysis
# Crawl4AI Developer Guide

## 1. Overview and Purpose
Crawl4AI is designed to generate **clean, structured markdown** from web pages, effectively extracting the actual content while discarding boilerplate or noise. This functionality is crucial for AI workflows that require high-quality data extraction.

### Core Functionality and Purpose
- **Content Extraction**: Extracts meaningful content from web pages.
- **Markdown Generation**: Converts HTML to markdown format.
- **Noise Reduction**: Filters out irrelevant elements like ads and navigation bars.

### Key Capabilities and Limitations
- **Capabilities**:
  - Supports various content filters (e.g., BM25, Pruning).
  - Provides options for customizing markdown output.
  
- **Limitations**:
  - Performance may vary based on page complexity.
  - Requires proper configuration for optimal results.

### Target Use Cases
- AI model training requiring clean text data.
- Documentation generation from web resources.
- Content summarization and analysis.

## 2. Technical Implementation
### Architecture and Design Patterns
Crawl4AI employs an asynchronous architecture, leveraging Python's `asyncio` for efficient web crawling and data processing.

### Component Interactions
- **AsyncWebCrawler**: Main component for initiating crawls.
- **Markdown Generators**: Convert HTML to markdown.
- **Content Filters**: Refine extracted content based on user-defined criteria.

### Data Flow and State Management
Data flows from the web page through the crawler, into the markdown generator, and finally through any applied content filters before being returned to the user.

## 3. Code Implementation
### Setup and Configuration
To get started with Crawl4AI, ensure you have the required packages installed. Use the following command:

```bash
pip install crawl4ai
```

### Integration Steps
Integrate Crawl4AI into your project by importing necessary classes and configuring your crawler.

### Code Examples

#### Basic Markdown Generation Example
Here’s a minimal code snippet that uses the **DefaultMarkdownGenerator** with no additional filtering:

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def main():
    config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator()
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com", config=config)
        if result.success:
            print("Raw Markdown Output:\n")
            print(result.markdown) # The unfiltered markdown from the page
        else:
            print("Crawl failed:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())
```

#### Configuring the Default Markdown Generator
You can tweak the output by passing an `options` dict to `DefaultMarkdownGenerator`. For example:

```python
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async def main():
    md_generator = DefaultMarkdownGenerator(
        options={
            "ignore_links": True,
            "escape_html": False,
            "body_width": 80
        }
    )
    config = CrawlerRunConfig(
        markdown_generator=md_generator
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com/docs", config=config)
        if result.success:
            print("Markdown:\n", result.markdown[:500]) # Just a snippet
        else:
            print("Crawl failed:", result.error_message)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## 4. Advanced Usage
### Optimization Techniques
Utilize content filters effectively to enhance the quality of extracted markdown.

### Performance Considerations
Be mindful of large pages and multiple filters which may slow down processing. Consider caching strategies to avoid redundant downloads.

### Security Considerations
Ensure that your API tokens and sensitive information are securely managed and not hard-coded in your scripts.

### Error Handling
Implement robust error handling to manage potential issues during crawling or markdown generation.

## 5. Troubleshooting
### Common Issues
- **No Markdown Output?**: Ensure the crawler retrieved HTML successfully.
- **Performance Issues**: Check if filters are too aggressive or if the page is too large.

### Debugging Strategies
Use logging to track the flow of data and identify where issues may arise.

### Known Limitations
Some sites may require dynamic rendering to extract content effectively.

### Best Practices
- Regularly update your dependencies.
- Test your configurations with various web pages to ensure reliability.

## 6. Combining Filters (BM25 + Pruning) in Two Passes
You might want to **prune out** noisy boilerplate first (with `PruningContentFilter`), and then **rank what’s left** against a user query (with `BM25ContentFilter`). You don’t have to crawl the page twice. Instead:

1. **First pass**: Apply `PruningContentFilter` directly to the raw HTML from `result.html`.
2. **Second pass**: Take the pruned HTML (or text) from step 1, and feed it into `BM25ContentFilter`, focusing on a user query.

### Two-Pass Example

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter

async def main():
    config = CrawlerRunConfig()
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com/tech-article", config=config)
        if not result.success or not result.html:
            print("Crawl failed or no HTML content.")
            return
        
        raw_html = result.html
        
        # First pass: PruningContentFilter on raw HTML
        pruning_filter = PruningContentFilter(threshold=0.5, min_word_threshold=50)
        pruned_chunks = pruning_filter.filter_content(raw_html)
        
        pruned_html = "\n".join(pruned_chunks)
        
        # Second pass: BM25ContentFilter with a user query
        bm25_filter = BM25ContentFilter(
            user_query="machine learning",
            bm25_threshold=1.2,
            language="english"
        )
        
        bm25_chunks = bm25_filter.filter_content(pruned_html) 
        if not bm25_chunks:
            print("Nothing matched the BM25 query after pruning.")
            return
        
        final_text = "\n---\n".join(bm25_chunks)
        print("==== PRUNED OUTPUT (first pass) ====")
        print(pruned_html[:500], "... (truncated)") 
        print("\n==== BM25 OUTPUT (second pass) ====")
        print(final_text[:500], "... (truncated)")

if __name__ == "__main__":
    asyncio.run(main())
```

## 7. Conclusion
In this guide, you learned how to effectively use Crawl4AI for generating high-quality markdown from web pages. By leveraging its powerful features such as content filtering and markdown generation, you can streamline your data extraction processes for AI applications and documentation needs.

## Processing Metadata
- Source: terminal-mkdocs-main-content
- Type: developer_documentation
- URL: https://docs.crawl4ai.com/core/markdown-generation/
