---
url: https://docs.firecrawl.dev/api-reference/endpoint/deep-research-get
scraped_at: 2025-05-25T08:35:53.543545
title: Deep Research - Firecrawl Docs
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
Deep Research
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


# Deep Research
Copy page
GET
/
deep-research
/
{id}
Try it
cURL
Python
JavaScript
PHP
Go
Java
Copy
```
curl --request GET \
 --url https://api.firecrawl.dev/v1/deep-research/{id} \
 --header 'Authorization: Bearer <token>'
```

200
404
Copy
```
{
 "success": true,
 "data": {
  "finalAnalysis": "<string>",
  "json": {},
  "activities": [
   {
    "type": "<string>",
    "status": "<string>",
    "message": "<string>",
    "timestamp": "2023-11-07T05:31:56Z",
    "depth": 123
   }
  ],
  "sources": [
   {
    "url": "<string>",
    "title": "<string>",
    "description": "<string>",
    "favicon": "<string>"
   }
  ],
  "status": "processing",
  "error": "<string>",
  "expiresAt": "2023-11-07T05:31:56Z",
  "currentDepth": 123,
  "maxDepth": 123,
  "totalUrls": 123
 }
}
```

#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research-get#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Path Parameters
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research-get#parameter-id)
id
string
required
The ID of the research job
#### Response
200
200404
application/json
Successful response
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research-get#response-success)
success
boolean
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research-get#response-data)
data
object
Show child attributes
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/deep-research-get.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/deep-research-get)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
cURL
Python
JavaScript
PHP
Go
Java
Copy
```
curl --request GET \
 --url https://api.firecrawl.dev/v1/deep-research/{id} \
 --header 'Authorization: Bearer <token>'
```

200
404
Copy
```
{
 "success": true,
 "data": {
  "finalAnalysis": "<string>",
  "json": {},
  "activities": [
   {
    "type": "<string>",
    "status": "<string>",
    "message": "<string>",
    "timestamp": "2023-11-07T05:31:56Z",
    "depth": 123
   }
  ],
  "sources": [
   {
    "url": "<string>",
    "title": "<string>",
    "description": "<string>",
    "favicon": "<string>"
   }
  ],
  "status": "processing",
  "error": "<string>",
  "expiresAt": "2023-11-07T05:31:56Z",
  "currentDepth": 123,
  "maxDepth": 123,
  "totalUrls": 123
 }
}
```

Assistant
Responses are generated using AI and may contain mistakes.

