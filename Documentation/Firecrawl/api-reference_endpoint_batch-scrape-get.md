---
url: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get
scraped_at: 2025-05-25T08:33:25.575042
title: Get Batch Scrape Status - Firecrawl Docs
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
Scrape Endpoints
Get Batch Scrape Status
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


Scrape Endpoints
# Get Batch Scrape Status
Copy page
GET
/
batch
/
scrape
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
 --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
 --header 'Authorization: Bearer <token>'
```

200
402
429
500
Copy
```
{
 "status": "<string>",
 "total": 123,
 "completed": 123,
 "creditsUsed": 123,
 "expiresAt": "2023-11-07T05:31:56Z",
 "next": "<string>",
 "data": [
  {
   "markdown": "<string>",
   "html": "<string>",
   "rawHtml": "<string>",
   "links": [
    "<string>"
   ],
   "screenshot": "<string>",
   "metadata": {
    "title": "<string>",
    "description": "<string>",
    "language": "<string>",
    "sourceURL": "<string>",
    "<any other metadata> ": "<string>",
    "statusCode": 123,
    "error": "<string>"
   }
  }
 ]
}
```

#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Path Parameters
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#parameter-id)
id
string
required
The ID of the batch scrape job
#### Response
200
200402429500
application/json
Successful response
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#response-status)
status
string
The current status of the batch scrape. Can be `scraping`, `completed`, or `failed`.
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#response-total)
total
integer
The total number of pages that were attempted to be scraped.
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#response-completed)
completed
integer
The number of pages that have been successfully scraped.
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#response-credits-used)
creditsUsed
integer
The number of credits used for the batch scrape.
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#response-expires-at)
expiresAt
string
The date and time when the batch scrape will expire.
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#response-next)
next
string | null
The URL to retrieve the next 10MB of data. Returned if the batch scrape is not completed or if the response is larger than 10MB.
[​](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get#response-data)
data
object[]
The data of the batch scrape.
Show child attributes
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/batch-scrape-get.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/batch-scrape-get)
[Batch Scrape](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape)[Cancel Batch Scrape](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-delete)
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
 --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
 --header 'Authorization: Bearer <token>'
```

200
402
429
500
Copy
```
{
 "status": "<string>",
 "total": 123,
 "completed": 123,
 "creditsUsed": 123,
 "expiresAt": "2023-11-07T05:31:56Z",
 "next": "<string>",
 "data": [
  {
   "markdown": "<string>",
   "html": "<string>",
   "rawHtml": "<string>",
   "links": [
    "<string>"
   ],
   "screenshot": "<string>",
   "metadata": {
    "title": "<string>",
    "description": "<string>",
    "language": "<string>",
    "sourceURL": "<string>",
    "<any other metadata> ": "<string>",
    "statusCode": 123,
    "error": "<string>"
   }
  }
 ]
}
```

Assistant
Responses are generated using AI and may contain mistakes.

