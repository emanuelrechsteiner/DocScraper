---
url: https://docs.firecrawl.dev/api-reference/endpoint/search
scraped_at: 2025-05-25T08:33:21.875155
title: Search - Firecrawl Docs
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
Search Endpoints
Search
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


Search Endpoints
# Search
Copy page
POST
/
search
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
 --url https://api.firecrawl.dev/v1/search \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "query": "<string>",
 "limit": 5,
 "tbs": "<string>",
 "lang": "en",
 "country": "us",
 "location": "<string>",
 "timeout": 60000,
 "ignoreInvalidURLs": false,
 "scrapeOptions": {}
}'
```

200
408
500
Copy
```
{
 "success": true,
 "data": [
  {
   "title": "<string>",
   "description": "<string>",
   "url": "<string>",
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
    "sourceURL": "<string>",
    "statusCode": 123,
    "error": "<string>"
   }
  }
 ],
 "warning": "<string>"
}
```

The search endpoint combines web search (SERP) with Firecrawl’s scraping capabilities to return full page content for any query.
Include `scrapeOptions` with `formats: ["markdown"]` to get complete markdown content for each search result otherwise you will default to getting the SERP results (url, title, description).
## 
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#supported-query-operators)
Supported query operators
We support a variety of query operators that allow you to filter your searches better.
Operator| Functionality| Examples  
---|---|---  
`""`| Non-fuzzy matches a string of text| `"Firecrawl"`  
`-`| Excludes certain keywords or negates other operators| `-bad`, `-site:firecrawl.dev`  
`site:`| Only returns results from a specified website| `site:firecrawl.dev`  
`inurl:`| Only returns results that include a word in the URL| `inurl:firecrawl`  
`allinurl:`| Only returns results that include multiple words in the URL| `allinurl:git firecrawl`  
`intitle:`| Only returns results that include a word in the title of the page| `intitle:Firecrawl`  
`allintitle:`| Only returns results that include multiple words in the title of the page| `allintitle:firecrawl playground`  
`related:`| Only returns results that are related to a specific domain| `related:firecrawl.dev`  
#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-query)
query
string
required
The search query
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-limit)
limit
integer
default:5
Maximum number of results to return
Required range: `1 <= x <= 100`
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-tbs)
tbs
string
Time-based search parameter
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-lang)
lang
string
default:en
Language code for search results
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-country)
country
string
default:us
Country code for search results
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-location)
location
string
Location parameter for search results
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-timeout)
timeout
integer
default:60000
Timeout in milliseconds
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-ignore-invalid-urls)
ignoreInvalidURLs
boolean
default:false
Excludes URLs from the search results that are invalid for other Firecrawl endpoints. This helps reduce errors if you are piping data from search into other Firecrawl API endpoints.
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#body-scrape-options)
scrapeOptions
object
Options for scraping search results
Show child attributes
#### Response
200
200408500
application/json
Successful response
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#response-success)
success
boolean
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#response-data)
data
object[]
Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/search#response-warning)
warning
string | null
Warning message if any issues occurred
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/search.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/search)
[Map](https://docs.firecrawl.dev/api-reference/endpoint/map)[Extract](https://docs.firecrawl.dev/api-reference/endpoint/extract)
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
 --url https://api.firecrawl.dev/v1/search \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "query": "<string>",
 "limit": 5,
 "tbs": "<string>",
 "lang": "en",
 "country": "us",
 "location": "<string>",
 "timeout": 60000,
 "ignoreInvalidURLs": false,
 "scrapeOptions": {}
}'
```

200
408
500
Copy
```
{
 "success": true,
 "data": [
  {
   "title": "<string>",
   "description": "<string>",
   "url": "<string>",
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
    "sourceURL": "<string>",
    "statusCode": 123,
    "error": "<string>"
   }
  }
 ],
 "warning": "<string>"
}
```

Assistant
Responses are generated using AI and may contain mistakes.

