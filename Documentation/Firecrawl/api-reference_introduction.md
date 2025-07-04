---
url: https://docs.firecrawl.dev/api-reference/introduction
scraped_at: 2025-05-25T08:57:35.979909
title: Introduction - Firecrawl Docs
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
Using the API
Introduction
[Documentation](https://docs.firecrawl.dev/introduction)[SDKs](https://docs.firecrawl.dev/sdks/overview)[Learn](https://www.firecrawl.dev/blog/category/tutorials)[Integrations](https://www.firecrawl.dev/app)[API Reference](https://docs.firecrawl.dev/api-reference/introduction)
* [Playground](https://firecrawl.dev/playground)
* [Blog](https://firecrawl.dev/blog)
* [Community](https://discord.gg/gSmWdAkdwd)
* [Changelog](https://firecrawl.dev/changelog)
##### Using the API
  * [Introduction](https://docs.firecrawl.dev/api-reference/introduction)


##### Scrape Endpoints
  * [POSTScrape](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
  * [POSTBatch Scrape](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape)
  * [GETGet Batch Scrape Status](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get)
  * [DELCancel Batch Scrape](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-delete)
  * [GETGet Batch Scrape Errors](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get-errors)


##### Crawl Endpoints
  * [POSTCrawl](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post)
  * [GETGet Crawl Status](https://docs.firecrawl.dev/api-reference/endpoint/crawl-get)
  * [DELCancel Crawl](https://docs.firecrawl.dev/api-reference/endpoint/crawl-delete)
  * [GETGet Crawl Errors](https://docs.firecrawl.dev/api-reference/endpoint/crawl-get-errors)


##### Map Endpoints
  * [POSTMap](https://docs.firecrawl.dev/api-reference/endpoint/map)


##### Search Endpoints
  * [POSTSearch](https://docs.firecrawl.dev/api-reference/endpoint/search)


##### Extract Endpoints
  * [POSTExtract](https://docs.firecrawl.dev/api-reference/endpoint/extract)
  * [GETGet Extract Status](https://docs.firecrawl.dev/api-reference/endpoint/extract-get)


##### Account Endpoints
  * [GETCredit Usage](https://docs.firecrawl.dev/api-reference/endpoint/credit-usage)
  * [GETToken Usage](https://docs.firecrawl.dev/api-reference/endpoint/token-usage)


Using the API
# Introduction
Copy page
Firecrawl API Reference
## 
[​](https://docs.firecrawl.dev/api-reference/introduction#features)
Features
## [ScrapeExtract content from any webpage in markdown or json format.](https://docs.firecrawl.dev/api-reference/endpoint/scrape)## [CrawlCrawl entire websites, extract their content and metadata.](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post)## [MapGet a complete list of URLs from any website quickly and reliably.](https://docs.firecrawl.dev/api-reference/endpoint/map)## [SearchSearch the web and get full page content in any format.](https://docs.firecrawl.dev/api-reference/endpoint/search)## [ExtractExtract structured data from entire webpages using natural language.](https://docs.firecrawl.dev/api-reference/endpoint/extract)
## 
[​](https://docs.firecrawl.dev/api-reference/introduction#base-url)
Base URL
All requests contain the following base URL:
Copy
```
https://api.firecrawl.dev 

```

## 
[​](https://docs.firecrawl.dev/api-reference/introduction#authentication)
Authentication
For authentication, it’s required to include an Authorization header. The header should contain `Bearer fc-123456789`, where `fc-123456789` represents your API Key.
Copy
```
Authorization: Bearer fc-123456789

```

​
## 
[​](https://docs.firecrawl.dev/api-reference/introduction#response-codes)
Response codes
Firecrawl employs conventional HTTP status codes to signify the outcome of your requests.
Typically, 2xx HTTP status codes denote success, 4xx codes represent failures related to the user, and 5xx codes signal infrastructure problems.
Status| Description  
---|---  
200| Request was successful.  
400| Verify the correctness of the parameters.  
401| The API key was not provided.  
402| Payment required  
404| The requested resource could not be located.  
429| The rate limit has been surpassed.  
5xx| Signifies a server error with Firecrawl.  
Refer to the Error Codes section for a detailed explanation of all potential API errors.
​
## 
[​](https://docs.firecrawl.dev/api-reference/introduction#rate-limit)
Rate limit
The Firecrawl API has a rate limit to ensure the stability and reliability of the service. The rate limit is applied to all endpoints and is based on the number of requests made within a specific time frame.
When you exceed the rate limit, you will receive a 429 response code.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/introduction.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/introduction)
[Scrape](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Features](https://docs.firecrawl.dev/api-reference/introduction#features)
  * [Base URL](https://docs.firecrawl.dev/api-reference/introduction#base-url)
  * [Authentication](https://docs.firecrawl.dev/api-reference/introduction#authentication)
  * [Response codes](https://docs.firecrawl.dev/api-reference/introduction#response-codes)
  * [Rate limit](https://docs.firecrawl.dev/api-reference/introduction#rate-limit)


Assistant
Responses are generated using AI and may contain mistakes.

