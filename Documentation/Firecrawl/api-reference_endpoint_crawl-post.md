---
url: https://docs.firecrawl.dev/api-reference/endpoint/crawl-post
scraped_at: 2025-05-25T08:34:56.117377
title: Crawl - Firecrawl Docs
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
Crawl Endpoints
Crawl
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


Crawl Endpoints
# Crawl
Copy page
POST
/
crawl
Try it
cURL
Python
JavaScript
PHP
Go
Java
Copy
```
curl --request POST \
 --url https://api.firecrawl.dev/v1/crawl \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "url": "<string>",
 "excludePaths": [
  "<string>"
 ],
 "includePaths": [
  "<string>"
 ],
 "maxDepth": 10,
 "maxDiscoveryDepth": 123,
 "ignoreSitemap": false,
 "ignoreQueryParameters": false,
 "limit": 10000,
 "allowBackwardLinks": false,
 "allowExternalLinks": false,
 "delay": 123,
 "webhook": {
  "url": "<string>",
  "headers": {},
  "metadata": {},
  "events": [
   "completed"
  ]
 },
 "scrapeOptions": {
  "formats": [
   "markdown"
  ],
  "onlyMainContent": true,
  "includeTags": [
   "<string>"
  ],
  "excludeTags": [
   "<string>"
  ],
  "headers": {},
  "waitFor": 0,
  "mobile": false,
  "skipTlsVerification": false,
  "timeout": 30000,
  "jsonOptions": {
   "schema": {},
   "systemPrompt": "<string>",
   "prompt": "<string>"
  },
  "actions": [
   {
    "type": "wait",
    "milliseconds": 2,
    "selector": "#my-element"
   }
  ],
  "location": {
   "country": "US",
   "languages": [
    "en-US"
   ]
  },
  "removeBase64Images": true,
  "blockAds": true,
  "proxy": "basic",
  "changeTrackingOptions": {
   "modes": [
    "git-diff"
   ],
   "schema": {},
   "prompt": "<string>"
  }
 }
}'
```

200
402
429
500
Copy
```
{
 "success": true,
 "id": "<string>",
 "url": "<string>"
}
```

#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-url)
url
string
required
The base URL to start crawling from
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-exclude-paths)
excludePaths
string[]
URL pathname regex patterns that exclude matching URLs from the crawl. For example, if you set "excludePaths": ["blog/.*"] for the base URL firecrawl.dev, any results matching that pattern will be excluded, such as <https://www.firecrawl.dev/blog/firecrawl-launch-week-1-recap>.
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-include-paths)
includePaths
string[]
URL pathname regex patterns that include matching URLs in the crawl. Only the paths that match the specified patterns will be included in the response. For example, if you set "includePaths": ["blog/.*"] for the base URL firecrawl.dev, only results matching that pattern will be included, such as <https://www.firecrawl.dev/blog/firecrawl-launch-week-1-recap>.
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-max-depth)
maxDepth
integer
default:10
Maximum depth to crawl relative to the base URL. Basically, the max number of slashes the pathname of a scraped URL may contain.
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-max-discovery-depth)
maxDiscoveryDepth
integer
Maximum depth to crawl based on discovery order. The root site and sitemapped pages has a discovery depth of 0. For example, if you set it to 1, and you set ignoreSitemap, you will only crawl the entered URL and all URLs that are linked on that page.
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-ignore-sitemap)
ignoreSitemap
boolean
default:false
Ignore the website sitemap when crawling
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-ignore-query-parameters)
ignoreQueryParameters
boolean
default:false
Do not re-scrape the same path with different (or none) query parameters
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-limit)
limit
integer
default:10000
Maximum number of pages to crawl. Default limit is 10000.
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-allow-backward-links)
allowBackwardLinks
boolean
default:false
Allows the crawler to follow internal links to sibling or parent URLs, not just child paths.
false: Only crawls deeper (child) URLs. → e.g. /features/feature-1 → /features/feature-1/tips ✅ → Won't follow /pricing or / ❌
true: Crawls any internal links, including siblings and parents. → e.g. /features/feature-1 → /pricing, /, etc. ✅
Use true for broader internal coverage beyond nested paths.
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-allow-external-links)
allowExternalLinks
boolean
default:false
Allows the crawler to follow links to external websites.
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-delay)
delay
number
Delay in seconds between scrapes. This helps respect website rate limits.
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-webhook)
webhook
object
A webhook specification object.
Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#body-scrape-options)
scrapeOptions
object
Show child attributes
#### Response
200
200402429500
application/json
Successful response
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#response-success)
success
boolean
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#response-id)
id
string
[​](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post#response-url)
url
string
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/crawl-post.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/crawl-post)
[Get Batch Scrape Errors](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get-errors)[Get Crawl Status](https://docs.firecrawl.dev/api-reference/endpoint/crawl-get)
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
curl --request POST \
 --url https://api.firecrawl.dev/v1/crawl \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "url": "<string>",
 "excludePaths": [
  "<string>"
 ],
 "includePaths": [
  "<string>"
 ],
 "maxDepth": 10,
 "maxDiscoveryDepth": 123,
 "ignoreSitemap": false,
 "ignoreQueryParameters": false,
 "limit": 10000,
 "allowBackwardLinks": false,
 "allowExternalLinks": false,
 "delay": 123,
 "webhook": {
  "url": "<string>",
  "headers": {},
  "metadata": {},
  "events": [
   "completed"
  ]
 },
 "scrapeOptions": {
  "formats": [
   "markdown"
  ],
  "onlyMainContent": true,
  "includeTags": [
   "<string>"
  ],
  "excludeTags": [
   "<string>"
  ],
  "headers": {},
  "waitFor": 0,
  "mobile": false,
  "skipTlsVerification": false,
  "timeout": 30000,
  "jsonOptions": {
   "schema": {},
   "systemPrompt": "<string>",
   "prompt": "<string>"
  },
  "actions": [
   {
    "type": "wait",
    "milliseconds": 2,
    "selector": "#my-element"
   }
  ],
  "location": {
   "country": "US",
   "languages": [
    "en-US"
   ]
  },
  "removeBase64Images": true,
  "blockAds": true,
  "proxy": "basic",
  "changeTrackingOptions": {
   "modes": [
    "git-diff"
   ],
   "schema": {},
   "prompt": "<string>"
  }
 }
}'
```

200
402
429
500
Copy
```
{
 "success": true,
 "id": "<string>",
 "url": "<string>"
}
```

Assistant
Responses are generated using AI and may contain mistakes.

