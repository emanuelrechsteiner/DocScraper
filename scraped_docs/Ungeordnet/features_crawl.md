---
url: https://docs.firecrawl.dev/features/crawl
scraped_at: 2025-05-25T08:35:42.807888
title: Crawl | Firecrawl
---

[Firecrawl Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo-dark.png)](https://firecrawl.dev)
v1
Search...
⌘KAsk AI
  * [Status](https://firecrawl.betteruptime.com)
  * Support
  * [mendableai/firecrawl38.791](https://github.com/mendableai/firecrawl)
  * [mendableai/firecrawl38.791](https://github.com/mendableai/firecrawl)


Search...
Navigation
Crawl
Crawl
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
    * [Crawl](https://docs.firecrawl.dev/features/crawl)
    * [JSON mode](https://docs.firecrawl.dev/features/llm-extract)
    * [Change Tracking with Crawl (New)](https://docs.firecrawl.dev/features/change-tracking-crawl)
    * [Webhooks](https://docs.firecrawl.dev/features/webhooks)
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


Crawl
# Crawl
Copy page
Firecrawl can recursively search through a urls subdomains, and gather the content
Firecrawl efficiently crawls websites to extract comprehensive data while bypassing blockers. The process:
  1. **URL Analysis:** Scans sitemap and crawls website to identify links
  2. **Traversal:** Recursively follows links to find all subpages
  3. **Scraping:** Extracts content from each page, handling JS and rate limits
  4. **Output:** Converts data to clean markdown or structured format


This ensures thorough data collection from any starting URL.
## 
[​](https://docs.firecrawl.dev/features/crawl#crawling)
Crawling
### 
[​](https://docs.firecrawl.dev/features/crawl#%2Fcrawl-endpoint)
/crawl endpoint
Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.
By default - Crawl will ignore sublinks of a page if they aren’t children of the url you provide. So, the website.com/other-parent/blog-1 wouldn’t be returned if you crawled website.com/blogs/. If you want website.com/other-parent/blog-1, use the `allowBackwardLinks` parameter
### 
[​](https://docs.firecrawl.dev/features/crawl#installation)
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
[​](https://docs.firecrawl.dev/features/crawl#usage)
Usage
Python
Node
Go
Rust
cURL
Copy
```
from firecrawl import FirecrawlApp, ScrapeOptions
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Crawl a website:
crawl_result = app.crawl_url(
 'https://firecrawl.dev', 
 limit=10, 
 scrape_options=ScrapeOptions(formats=['markdown', 'html']),
)
print(crawl_result)

```

### 
[​](https://docs.firecrawl.dev/features/crawl#api-response)
API Response
If you’re using cURL or `async crawl` functions on SDKs, this will return an `ID` where you can use to check the status of the crawl.
If you’re using the SDK, check the SDK response section [below](https://docs.firecrawl.dev/features/crawl#sdk-response).
Copy
```
{
 "success": true,
 "id": "123-456-789",
 "url": "https://api.firecrawl.dev/v1/crawl/123-456-789"
}

```

### 
[​](https://docs.firecrawl.dev/features/crawl#check-crawl-job)
Check Crawl Job
Used to check the status of a crawl job and get its result.
This endpoint only works for crawls that are in progress or crawls that have completed recently. 
Python
Node
Go
Rust
cURL
Copy
```
crawl_status = app.check_crawl_status("<crawl_id>")
print(crawl_status)

```

#### 
[​](https://docs.firecrawl.dev/features/crawl#response-handling)
Response Handling
The response varies based on the crawl’s status.
For not completed or large responses exceeding 10MB, a `next` URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the `next` parameter is absent, it indicates the end of the crawl data.
The skip parameter sets the maximum number of results returned for each chunk of results returned.
The skip and next parameter are only relavent when hitting the api directly. If you’re using the SDK, we handle this for you and will return all the results at once.
Scraping
Completed
Copy
```
{
 "status": "scraping",
 "total": 36,
 "completed": 10,
 "creditsUsed": 10,
 "expiresAt": "2024-00-00T00:00:00.000Z",
 "next": "https://api.firecrawl.dev/v1/crawl/123-456-789?skip=10",
 "data": [
  {
   "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
   "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
   "metadata": {
    "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
    "language": "en",
    "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
    "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
    "ogLocaleAlternate": [],
    "statusCode": 200
   }
  },
  ...
 ]
}

```

### 
[​](https://docs.firecrawl.dev/features/crawl#sdk-response)
SDK Response
The SDK provides two ways to crawl URLs:
  1. **Synchronous Crawling** (`crawl_url`/`crawlUrl`): 
     * Waits for the crawl to complete and returns the full response
     * Handles pagination automatically
     * Recommended for most use cases


Python
Node
Copy
```
from firecrawl import FirecrawlApp, ScrapeOptions
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Crawl a website:
crawl_status = app.crawl_url(
 'https://firecrawl.dev', 
 limit=100, 
 scrape_options=ScrapeOptions(formats=['markdown', 'html']),
 poll_interval=30
)
print(crawl_status)

```

The response includes the crawl status and all scraped data:
Python
Node
Copy
```
success=True
status='completed'
completed=100
total=100
creditsUsed=100
expiresAt=datetime.datetime(2025, 4, 23, 19, 21, 17, tzinfo=TzInfo(UTC))
next=None
data=[
 FirecrawlDocument(
  markdown='[Day 7 - Launch Week III.Integrations DayApril 14th to 20th](...',
  metadata={
   'title': '15 Python Web Scraping Projects: From Beginner to Advanced',
   ...
   'scrapeId': '97dcf796-c09b-43c9-b4f7-868a7a5af722',
   'sourceURL': 'https://www.firecrawl.dev/blog/python-web-scraping-projects',
   'url': 'https://www.firecrawl.dev/blog/python-web-scraping-projects',
   'statusCode': 200
  }
 ),
 ...
]

```

  1. **Asynchronous Crawling** (`async_crawl_url`/`asyncCrawlUrl`): 
     * Returns immediately with a crawl ID
     * Allows manual status checking
     * Useful for long-running crawls or custom polling logic


## 
[​](https://docs.firecrawl.dev/features/crawl#crawl-websocket)
Crawl WebSocket
Firecrawl’s WebSocket-based method, `Crawl URL and Watch`, enables real-time data extraction and monitoring. Start a crawl with a URL and customize it with options like page limits, allowed domains, and output formats, ideal for immediate data processing needs.
Python
Node
Copy
```
# inside an async function...
nest_asyncio.apply()
# Define event handlers
def on_document(detail):
  print("DOC", detail)
def on_error(detail):
  print("ERR", detail['error'])
def on_done(detail):
  print("DONE", detail['status'])
  # Function to start the crawl and watch process
async def start_crawl_and_watch():
  # Initiate the crawl job and get the watcher
  watcher = app.crawl_url_and_watch('firecrawl.dev', limit=5)
  # Add event listeners
  watcher.add_event_listener("document", on_document)
  watcher.add_event_listener("error", on_error)
  watcher.add_event_listener("done", on_done)
  # Start the watcher
  await watcher.connect()
# Run the event loop
await start_crawl_and_watch()

```

## 
[​](https://docs.firecrawl.dev/features/crawl#crawl-webhook)
Crawl Webhook
You can configure webhooks to receive real-time notifications as your crawl progresses. This allows you to process pages as they’re scraped instead of waiting for the entire crawl to complete.
cURL
Copy
```
curl -X POST https://api.firecrawl.dev/v1/crawl \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
   "url": "https://docs.firecrawl.dev",
   "limit": 100,
   "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
     "any_key": "any_value"
    },
    "events": ["started", "page", "completed"]
   }
  }'

```

For comprehensive webhook documentation including event types, payload structure, and implementation examples, see the [Webhooks documentation](https://docs.firecrawl.dev/features/webhooks).
### 
[​](https://docs.firecrawl.dev/features/crawl#quick-reference)
Quick Reference
**Event Types:**
  * `crawl.started` - When the crawl begins
  * `crawl.page` - For each page successfully scraped
  * `crawl.completed` - When the crawl finishes
  * `crawl.failed` - If the crawl encounters an error


**Basic Payload:**
Copy
```
{
 "success": true,
 "type": "crawl.page",
 "id": "crawl-job-id",
 "data": [...], // Page data for 'page' events
 "metadata": {}, // Your custom metadata
 "error": null
}

```

For detailed webhook configuration, security best practices, and troubleshooting, visit the [Webhooks documentation](https://docs.firecrawl.dev/features/webhooks).
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/crawl.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/crawl)
[Webhooks](https://docs.firecrawl.dev/features/webhooks)[JSON mode](https://docs.firecrawl.dev/features/llm-extract)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Crawling](https://docs.firecrawl.dev/features/crawl#crawling)
  * [/crawl endpoint](https://docs.firecrawl.dev/features/crawl#%2Fcrawl-endpoint)
  * [Installation](https://docs.firecrawl.dev/features/crawl#installation)
  * [Usage](https://docs.firecrawl.dev/features/crawl#usage)
  * [API Response](https://docs.firecrawl.dev/features/crawl#api-response)
  * [Check Crawl Job](https://docs.firecrawl.dev/features/crawl#check-crawl-job)
  * [Response Handling](https://docs.firecrawl.dev/features/crawl#response-handling)
  * [SDK Response](https://docs.firecrawl.dev/features/crawl#sdk-response)
  * [Crawl WebSocket](https://docs.firecrawl.dev/features/crawl#crawl-websocket)
  * [Crawl Webhook](https://docs.firecrawl.dev/features/crawl#crawl-webhook)
  * [Quick Reference](https://docs.firecrawl.dev/features/crawl#quick-reference)


Assistant
Responses are generated using AI and may contain mistakes.

