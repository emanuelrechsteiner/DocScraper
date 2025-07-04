---
url: https://docs.firecrawl.dev/features/search
scraped_at: 2025-05-25T08:57:13.548558
title: Search | Firecrawl
---

[Firecrawl Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo-dark.png)](https://firecrawl.dev)
v1
Search...
⌘KAsk AI
  * [Status](https://firecrawl.betteruptime.com)
  * Support
  * [mendableai/firecrawl38.790](https://github.com/mendableai/firecrawl)
  * [mendableai/firecrawl38.790](https://github.com/mendableai/firecrawl)


Search...
Navigation
Standard Features
Search
[Documentation](https://docs.firecrawl.dev/introduction)[SDKs](https://docs.firecrawl.dev/sdks/overview)[Learn](https://www.firecrawl.dev/blog/category/tutorials)[Integrations](https://www.firecrawl.dev/app)[API Reference](https://docs.firecrawl.dev/api-reference/introduction)
* [Playground](https://firecrawl.dev/playground)
* [Blog](https://firecrawl.dev/blog)
* [Community](https://discord.gg/gSmWdAkdwd)
* [Changelog](https://firecrawl.dev/changelog)
##### Get Started
  * [Quickstart](https://docs.firecrawl.dev/introduction)
  * [MCP Server](https://docs.firecrawl.dev/mcp)
  * [Launch Week III (New)](https://docs.firecrawl.dev/launch-week)
  * [Rate Limits](https://docs.firecrawl.dev/rate-limits)
  * [Advanced Scraping Guide](https://docs.firecrawl.dev/advanced-scraping-guide)


##### Standard Features
  * Scrape
  * Crawl
  * [Map](https://docs.firecrawl.dev/features/map)
  * [Search](https://docs.firecrawl.dev/features/search)


##### Agentic Features
  * [Extract](https://docs.firecrawl.dev/features/extract)
  * [FIRE-1](https://docs.firecrawl.dev/agents/fire-1)


##### Alpha tools
  * LLMs.txt API
  * Deep Research API


##### Contributing
  * [Open Source vs Cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud)
  * [Running locally](https://docs.firecrawl.dev/contributing/guide)
  * [Self-hosting](https://docs.firecrawl.dev/contributing/self-host)


Standard Features
# Search
Copy page
Search the web and get full content from results
Firecrawl’s search API allows you to perform web searches and optionally scrape the search results in one operation.
  * Choose specific output formats (markdown, HTML, links, screenshots)
  * Search the web with customizable parameters (language, country, etc.)
  * Optionally retrieve content from search results in various formats
  * Control the number of results and set timeouts


For details, see the [Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search).
## 
[​](https://docs.firecrawl.dev/features/search#performing-a-search-with-firecrawl)
Performing a Search with Firecrawl
### 
[​](https://docs.firecrawl.dev/features/search#%2Fsearch-endpoint)
/search endpoint
Used to perform web searches and optionally retrieve content from the results.
### 
[​](https://docs.firecrawl.dev/features/search#installation)
Installation
Python
Node
Go
Rust
Copy
```
pip install firecrawl-py

```

### 
[​](https://docs.firecrawl.dev/features/search#basic-usage)
Basic Usage
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client with your API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Perform a basic search
search_result = app.search("firecrawl web scraping", limit=5)
# Print the search results
for result in search_result.data:
  print(f"Title: {result['title']}")
  print(f"URL: {result['url']}")
  print(f"Description: {result['description']}") 

```

### 
[​](https://docs.firecrawl.dev/features/search#response)
Response
SDKs will return the data object directly. cURL will return the complete payload.
Copy
```
{
 "success": true,
 "data": [
  {
   "title": "Firecrawl - The Ultimate Web Scraping API",
   "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
   "url": "https://firecrawl.dev/"
  },
  {
   "title": "Web Scraping with Firecrawl - A Complete Guide",
   "description": "Learn how to use Firecrawl to extract data from websites effortlessly.",
   "url": "https://firecrawl.dev/guides/web-scraping/"
  },
  {
   "title": "Firecrawl Documentation - Getting Started",
   "description": "Official documentation for the Firecrawl web scraping API.",
   "url": "https://docs.firecrawl.dev/"
  }
  // ... more results
 ]
}

```

## 
[​](https://docs.firecrawl.dev/features/search#search-with-content-scraping)
Search with Content Scraping
Search and retrieve content from the search results in one operation.
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp, ScrapeOptions
# Initialize the client with your API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Search and scrape content
search_result = app.search(
  "firecrawl web scraping",
  limit=3,
  scrape_options=ScrapeOptions(formats=["markdown", "links"])
)
# Process the results
for result in search_result.data:
  print(f"Title: {result['title']}")
  print(f"URL: {result['url']}")
  print(f"Content: {result['markdown'][:150]}...") # first 150 chars
  print(f"Links: {', '.join(result['links'][:3])}...") # first 3 links

```

### 
[​](https://docs.firecrawl.dev/features/search#response-with-scraped-content)
Response with Scraped Content
Copy
```
{
 "success": true,
 "data": [
  {
   "title": "Firecrawl - The Ultimate Web Scraping API",
   "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
   "url": "https://firecrawl.dev/",
   "markdown": "# Firecrawl\n\nThe Ultimate Web Scraping API\n\n## Turn any website into clean, structured data\n\nFirecrawl makes it easy to extract data from websites for AI applications, market research, content aggregation, and more...",
   "links": [
    "https://firecrawl.dev/pricing",
    "https://firecrawl.dev/docs",
    "https://firecrawl.dev/guides",
    // ... more links
   ],
   "metadata": {
    "title": "Firecrawl - The Ultimate Web Scraping API",
    "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
    "sourceURL": "https://firecrawl.dev/",
    "statusCode": 200
   }
  },
  // ... more results
 ]
}

```

## 
[​](https://docs.firecrawl.dev/features/search#advanced-search-options)
Advanced Search Options
Firecrawl’s search API supports various parameters to customize your search:
### 
[​](https://docs.firecrawl.dev/features/search#language-and-country-customization)
Language and Country Customization
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client with your API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Search in German (Germany)
search_result = app.search(
  "web scraping tools",
  limit=5,
  lang="de",
  country="de"
)
# Process the results
for result in search_result.data:
  print(f"Title: {result['title']}")
  print(f"URL: {result['url']}") 

```

### 
[​](https://docs.firecrawl.dev/features/search#time-based-search)
Time-Based Search
Use the `tbs` parameter to filter results by time:
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client with your API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Search for results from the past week
search_result = app.search(
  "latest web scraping techniques",
  limit=5,
  tbs="qdr:w" # qdr:w = past week
)
# Process the results
for result in search_result.data:
  print(f"Title: {result['title']}")
  print(f"URL: {result['url']}") 

```

Common `tbs` values:
  * `qdr:h` - Past hour
  * `qdr:d` - Past 24 hours
  * `qdr:w` - Past week
  * `qdr:m` - Past month
  * `qdr:y` - Past year


### 
[​](https://docs.firecrawl.dev/features/search#custom-timeout)
Custom Timeout
Set a custom timeout for search operations:
Python
JavaScript
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client with your API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Set a 30-second timeout
search_result = app.search(
  "complex search query",
  limit=10,
  timeout=30000 # 30 seconds in milliseconds
)

```

## 
[​](https://docs.firecrawl.dev/features/search#scraping-options)
Scraping Options
When scraping search results, you can specify multiple output formats:
Python
JavaScript
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client with your API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Get search results with multiple formats
search_result = app.search(
  "firecrawl features",
  limit=3,
  scrape_options={
    "formats": ["markdown", "html", "links", "screenshot"]
  }
)

```

Available formats:
  * `markdown`: Clean, formatted markdown content
  * `html`: Processed HTML content
  * `rawHtml`: Unmodified HTML content
  * `links`: List of links found on the page
  * `screenshot`: Screenshot of the page
  * `screenshot@fullPage`: Full-page screenshot
  * `extract`: Structured data extraction


For more details about format options, refer to the [Scrape Feature documentation](https://docs.firecrawl.dev/features/scrape).
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/search.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/search)
[Map](https://docs.firecrawl.dev/features/map)[Extract](https://docs.firecrawl.dev/features/extract)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Performing a Search with Firecrawl](https://docs.firecrawl.dev/features/search#performing-a-search-with-firecrawl)
  * [/search endpoint](https://docs.firecrawl.dev/features/search#%2Fsearch-endpoint)
  * [Installation](https://docs.firecrawl.dev/features/search#installation)
  * [Basic Usage](https://docs.firecrawl.dev/features/search#basic-usage)
  * [Response](https://docs.firecrawl.dev/features/search#response)
  * [Search with Content Scraping](https://docs.firecrawl.dev/features/search#search-with-content-scraping)
  * [Response with Scraped Content](https://docs.firecrawl.dev/features/search#response-with-scraped-content)
  * [Advanced Search Options](https://docs.firecrawl.dev/features/search#advanced-search-options)
  * [Language and Country Customization](https://docs.firecrawl.dev/features/search#language-and-country-customization)
  * [Time-Based Search](https://docs.firecrawl.dev/features/search#time-based-search)
  * [Custom Timeout](https://docs.firecrawl.dev/features/search#custom-timeout)
  * [Scraping Options](https://docs.firecrawl.dev/features/search#scraping-options)


Assistant
Responses are generated using AI and may contain mistakes.

