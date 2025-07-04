---
url: https://docs.firecrawl.dev/sdks/python
scraped_at: 2025-05-25T08:33:56.520877
title: Python SDK | Firecrawl
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
Official
Python
[Documentation](https://docs.firecrawl.dev/introduction)[SDKs](https://docs.firecrawl.dev/sdks/overview)[Learn](https://www.firecrawl.dev/blog/category/tutorials)[Integrations](https://www.firecrawl.dev/app)[API Reference](https://docs.firecrawl.dev/api-reference/introduction)
* [Playground](https://firecrawl.dev/playground)
* [Blog](https://firecrawl.dev/blog)
* [Community](https://discord.gg/gSmWdAkdwd)
* [Changelog](https://firecrawl.dev/changelog)
##### Overall
  * [Overview](https://docs.firecrawl.dev/sdks/overview)


##### Official
  * [Python](https://docs.firecrawl.dev/sdks/python)
  * [Node](https://docs.firecrawl.dev/sdks/node)


##### Community
  * [Go](https://docs.firecrawl.dev/sdks/go)
  * [Rust](https://docs.firecrawl.dev/sdks/rust)


Official
# Python
Copy page
Firecrawl Python SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.
## 
[​](https://docs.firecrawl.dev/sdks/python#installation)
Installation
To install the Firecrawl Python SDK, you can use pip:
Python
Copy
```
pip install firecrawl-py

```

## 
[​](https://docs.firecrawl.dev/sdks/python#usage)
Usage
  1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
  2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.


Here’s an example of how to use the SDK:
Python
Copy
```
from firecrawl import FirecrawlApp, ScrapeOptions
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Scrape a website:
scrape_status = app.scrape_url(
 'https://firecrawl.dev', 
 formats=['markdown', 'html']
)
print(scrape_status)
# Crawl a website:
crawl_status = app.crawl_url(
 'https://firecrawl.dev', 
 limit=100, 
 scrape_options=ScrapeOptions(formats=['markdown', 'html'])
)
print(crawl_status)

```

### 
[​](https://docs.firecrawl.dev/sdks/python#scraping-a-url)
Scraping a URL
To scrape a single URL, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a dictionary.
Python
Copy
```
# Scrape a website:
scrape_result = app.scrape_url('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)

```

### 
[​](https://docs.firecrawl.dev/sdks/python#crawling-a-website)
Crawling a Website
To crawl a website, use the `crawl_url` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.
Python
Copy
```
crawl_status = app.crawl_url(
 'https://firecrawl.dev', 
 limit=100, 
 scrape_options=ScrapeOptions(formats=['markdown', 'html']),
 poll_interval=30
)
print(crawl_status)

```

### 
[​](https://docs.firecrawl.dev/sdks/python#asynchronous-crawling)
Asynchronous Crawling
Looking for async operations? Check out the [Async Class](https://docs.firecrawl.dev/sdks/python#async-class) section below.
To crawl a website asynchronously, use the `crawl_url_async` method. It returns the crawl `ID` which you can use to check the status of the crawl job. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.
Python
Copy
```
crawl_status = app.async_crawl_url(
 'https://firecrawl.dev', 
 limit=100, 
 scrape_options=ScrapeOptions(formats=['markdown', 'html']),
)
print(crawl_status)

```

### 
[​](https://docs.firecrawl.dev/sdks/python#checking-crawl-status)
Checking Crawl Status
To check the status of a crawl job, use the `check_crawl_status` method. It takes the job ID as a parameter and returns the current status of the crawl job.
Python
Copy
```
crawl_status = app.check_crawl_status("<crawl_id>")
print(crawl_status)

```

### 
[​](https://docs.firecrawl.dev/sdks/python#cancelling-a-crawl)
Cancelling a Crawl
To cancel an asynchronous crawl job, use the `cancel_crawl` method. It takes the job ID of the asynchronous crawl as a parameter and returns the cancellation status.
Python
Copy
```
cancel_crawl = app.cancel_crawl(id)
print(cancel_crawl)

```

### 
[​](https://docs.firecrawl.dev/sdks/python#map-a-website)
Map a Website
Use `map_url` to generate a list of URLs from a website. The `params` argument let you customize the mapping process, including options to exclude subdomains or to utilize the sitemap.
Python
Copy
```
# Map a website:
map_result = app.map_url('https://firecrawl.dev')
print(map_result)

```

### 
[​](https://docs.firecrawl.dev/sdks/python#crawling-a-website-with-websockets)
Crawling a Website with WebSockets
To crawl a website with WebSockets, use the `crawl_url_and_watch` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.
Python
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
[​](https://docs.firecrawl.dev/sdks/python#error-handling)
Error Handling
The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.
## 
[​](https://docs.firecrawl.dev/sdks/python#async-class)
Async Class
For async operations, you can use the `AsyncFirecrawlApp` class. Its methods are the same as the `FirecrawlApp` class, but they don’t block the main thread.
Python
Copy
```
from firecrawl import AsyncFirecrawlApp
app = AsyncFirecrawlApp(api_key="YOUR_API_KEY")
# Async Scrape
async def example_scrape():
 scrape_result = await app.scrape_url(url="https://example.com")
 print(scrape_result)
# Async Crawl
async def example_crawl():
 crawl_result = await app.crawl_url(url="https://example.com")
 print(crawl_result)

```

[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/sdks/python.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /sdks/python)
[Overview](https://docs.firecrawl.dev/sdks/overview)[Node](https://docs.firecrawl.dev/sdks/node)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Installation](https://docs.firecrawl.dev/sdks/python#installation)
  * [Usage](https://docs.firecrawl.dev/sdks/python#usage)
  * [Scraping a URL](https://docs.firecrawl.dev/sdks/python#scraping-a-url)
  * [Crawling a Website](https://docs.firecrawl.dev/sdks/python#crawling-a-website)
  * [Asynchronous Crawling](https://docs.firecrawl.dev/sdks/python#asynchronous-crawling)
  * [Checking Crawl Status](https://docs.firecrawl.dev/sdks/python#checking-crawl-status)
  * [Cancelling a Crawl](https://docs.firecrawl.dev/sdks/python#cancelling-a-crawl)
  * [Map a Website](https://docs.firecrawl.dev/sdks/python#map-a-website)
  * [Crawling a Website with WebSockets](https://docs.firecrawl.dev/sdks/python#crawling-a-website-with-websockets)
  * [Error Handling](https://docs.firecrawl.dev/sdks/python#error-handling)
  * [Async Class](https://docs.firecrawl.dev/sdks/python#async-class)


Assistant
Responses are generated using AI and may contain mistakes.

