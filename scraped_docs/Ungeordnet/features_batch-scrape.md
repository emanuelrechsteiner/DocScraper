---
url: https://docs.firecrawl.dev/features/batch-scrape
scraped_at: 2025-05-25T08:35:14.052951
title: Batch Scrape | Firecrawl
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
Scrape
Batch Scrape
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
    * [Scrape](https://docs.firecrawl.dev/features/scrape)
    * [Batch Scrape](https://docs.firecrawl.dev/features/batch-scrape)
    * [JSON mode](https://docs.firecrawl.dev/features/llm-extract)
    * [Change Tracking (New)](https://docs.firecrawl.dev/features/change-tracking)
    * [Stealth Mode](https://docs.firecrawl.dev/features/stealth-mode)
    * [Proxies](https://docs.firecrawl.dev/features/proxies)
    * [Webhooks](https://docs.firecrawl.dev/features/webhooks)
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


Scrape
# Batch Scrape
Copy page
Batch scrape multiple URLs
## 
[​](https://docs.firecrawl.dev/features/batch-scrape#batch-scraping-multiple-urls)
Batch scraping multiple URLs
You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.
### 
[​](https://docs.firecrawl.dev/features/batch-scrape#how-it-works)
How it works
It is very similar to how the `/crawl` endpoint works. It submits a batch scrape job and returns a job ID to check the status of the batch scrape.
The sdk provides 2 methods, synchronous and asynchronous. The synchronous method will return the results of the batch scrape job, while the asynchronous method will return a job ID that you can use to check the status of the batch scrape.
### 
[​](https://docs.firecrawl.dev/features/batch-scrape#usage)
Usage
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Scrape multiple websites:
batch_scrape_result = app.batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], formats=['markdown', 'html'])
print(batch_scrape_result)
# Or, you can use the asynchronous method:
batch_scrape_job = app.async_batch_scrape_urls(['firecrawl.dev', 'mendable.ai'], formats=['markdown', 'html'])
print(batch_scrape_job)
# (async) You can then use the job ID to check the status of the batch scrape:
batch_scrape_status = app.check_batch_scrape_status(batch_scrape_job.id)
print(batch_scrape_status)

```

### 
[​](https://docs.firecrawl.dev/features/batch-scrape#response)
Response
If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.
#### 
[​](https://docs.firecrawl.dev/features/batch-scrape#synchronous)
Synchronous
Completed
Copy
```
{
 "status": "completed",
 "total": 36,
 "completed": 36,
 "creditsUsed": 36,
 "expiresAt": "2024-00-00T00:00:00.000Z",
 "next": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789?skip=26",
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

#### 
[​](https://docs.firecrawl.dev/features/batch-scrape#asynchronous)
Asynchronous
You can then use the job ID to check the status of the batch scrape by calling the `/batch/scrape/{id}` endpoint. This endpoint is meant to be used while the job is still running or right after it has completed **as batch scrape jobs expire after 24 hours**.
Copy
```
{
 "success": true,
 "id": "123-456-789",
 "url": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789"
}

```

## 
[​](https://docs.firecrawl.dev/features/batch-scrape#batch-scrape-with-extraction)
Batch scrape with extraction
You can also use the batch scrape endpoint to extract structured data from the pages. This is useful if you want to get the same structured data from a list of URLs.
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Scrape multiple websites:
batch_scrape_result = app.batch_scrape_urls(
  ['https://docs.firecrawl.dev', 'https://docs.firecrawl.dev/sdks/overview'], 
  formats=['extract'],
  extract={
    'prompt': 'Extract the title and description from the page.',
    'schema': {
      'type': 'object',
      'properties': {
        'title': {'type': 'string'},
        'description': {'type': 'string'}
      },
      'required': ['title', 'description']
    }
  }
)
print(batch_scrape_result)
# Or, you can use the asynchronous method:
batch_scrape_job = app.async_batch_scrape_urls(
  ['https://docs.firecrawl.dev', 'https://docs.firecrawl.dev/sdks/overview'], 
  formats=['extract'],
  extract={
  'prompt': 'Extract the title and description from the page.',
  'schema': {
    'type': 'object',
      'properties': {
        'title': {'type': 'string'},
        'description': {'type': 'string'}
      },
      'required': ['title', 'description']
    }
  }
)
print(batch_scrape_job)
# (async) You can then use the job ID to check the status of the batch scrape:
batch_scrape_status = app.check_batch_scrape_status(batch_scrape_job.id)
print(batch_scrape_status)

```

### 
[​](https://docs.firecrawl.dev/features/batch-scrape#response-2)
Response
#### 
[​](https://docs.firecrawl.dev/features/batch-scrape#synchronous-2)
Synchronous
Completed
Copy
```
{
 "status": "completed",
 "total": 36,
 "completed": 36,
 "creditsUsed": 36,
 "expiresAt": "2024-00-00T00:00:00.000Z",
 "next": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789?skip=26",
 "data": [
  {
   "extract": {
    "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
    "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot."
   }
  },
  ...
 ]
}

```

#### 
[​](https://docs.firecrawl.dev/features/batch-scrape#asynchronous-2)
Asynchronous
Copy
```
{
 "success": true,
 "id": "123-456-789",
 "url": "https://api.firecrawl.dev/v1/batch/scrape/123-456-789"
}

```

## 
[​](https://docs.firecrawl.dev/features/batch-scrape#batch-scrape-with-webhooks)
Batch Scrape with Webhooks
You can configure webhooks to receive real-time notifications as each URL in your batch is scraped. This allows you to process results immediately instead of waiting for the entire batch to complete.
cURL
Copy
```
curl -X POST https://api.firecrawl.dev/v1/batch/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
   "urls": [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
   ],
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
[​](https://docs.firecrawl.dev/features/batch-scrape#quick-reference)
Quick Reference
**Event Types:**
  * `batch_scrape.started` - When the batch scrape begins
  * `batch_scrape.page` - For each URL successfully scraped
  * `batch_scrape.completed` - When all URLs are processed
  * `batch_scrape.failed` - If the batch scrape encounters an error


**Basic Payload:**
Copy
```
{
 "success": true,
 "type": "batch_scrape.page",
 "id": "batch-job-id",
 "data": [...], // Page data for 'page' events
 "metadata": {}, // Your custom metadata
 "error": null
}

```

For detailed webhook configuration, security best practices, and troubleshooting, visit the [Webhooks documentation](https://docs.firecrawl.dev/features/webhooks).
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/batch-scrape.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/batch-scrape)
[Scrape](https://docs.firecrawl.dev/features/scrape)[JSON mode](https://docs.firecrawl.dev/features/llm-extract)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Batch scraping multiple URLs](https://docs.firecrawl.dev/features/batch-scrape#batch-scraping-multiple-urls)
  * [How it works](https://docs.firecrawl.dev/features/batch-scrape#how-it-works)
  * [Usage](https://docs.firecrawl.dev/features/batch-scrape#usage)
  * [Response](https://docs.firecrawl.dev/features/batch-scrape#response)
  * [Synchronous](https://docs.firecrawl.dev/features/batch-scrape#synchronous)
  * [Asynchronous](https://docs.firecrawl.dev/features/batch-scrape#asynchronous)
  * [Batch scrape with extraction](https://docs.firecrawl.dev/features/batch-scrape#batch-scrape-with-extraction)
  * [Response](https://docs.firecrawl.dev/features/batch-scrape#response-2)
  * [Synchronous](https://docs.firecrawl.dev/features/batch-scrape#synchronous-2)
  * [Asynchronous](https://docs.firecrawl.dev/features/batch-scrape#asynchronous-2)
  * [Batch Scrape with Webhooks](https://docs.firecrawl.dev/features/batch-scrape#batch-scrape-with-webhooks)
  * [Quick Reference](https://docs.firecrawl.dev/features/batch-scrape#quick-reference)


Assistant
Responses are generated using AI and may contain mistakes.

