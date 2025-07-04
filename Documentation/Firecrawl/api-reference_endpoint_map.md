---
url: https://docs.firecrawl.dev/api-reference/endpoint/map
scraped_at: 2025-05-25T08:34:07.115182
title: Map - Firecrawl Docs
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
Map Endpoints
Map
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


Map Endpoints
# Map
Copy page
POST
/
map
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
 --url https://api.firecrawl.dev/v1/map \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "url": "<string>",
 "search": "<string>",
 "ignoreSitemap": true,
 "sitemapOnly": false,
 "includeSubdomains": false,
 "limit": 5000,
 "timeout": 123
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
 "links": [
  "<string>"
 ]
}
```

#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#body-url)
url
string
required
The base URL to start crawling from
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#body-search)
search
string
Search query to use for mapping. During the Alpha phase, the 'smart' part of the search functionality is limited to 1000 search results. However, if map finds more results, there is no limit applied.
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#body-ignore-sitemap)
ignoreSitemap
boolean
default:true
Ignore the website sitemap when crawling.
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#body-sitemap-only)
sitemapOnly
boolean
default:false
Only return links found in the website sitemap
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#body-include-subdomains)
includeSubdomains
boolean
default:false
Include subdomains of the website
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#body-limit)
limit
integer
default:5000
Maximum number of links to return
Required range: `x <= 30000`
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#body-timeout)
timeout
integer
Timeout in milliseconds. There is no timeout by default.
#### Response
200
200402429500
application/json
Successful response
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#response-success)
success
boolean
[​](https://docs.firecrawl.dev/api-reference/endpoint/map#response-links)
links
string[]
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/map.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/map)
[Get Crawl Errors](https://docs.firecrawl.dev/api-reference/endpoint/crawl-get-errors)[Search](https://docs.firecrawl.dev/api-reference/endpoint/search)
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
 --url https://api.firecrawl.dev/v1/map \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "url": "<string>",
 "search": "<string>",
 "ignoreSitemap": true,
 "sitemapOnly": false,
 "includeSubdomains": false,
 "limit": 5000,
 "timeout": 123
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
 "links": [
  "<string>"
 ]
}
```

Assistant
Responses are generated using AI and may contain mistakes.

