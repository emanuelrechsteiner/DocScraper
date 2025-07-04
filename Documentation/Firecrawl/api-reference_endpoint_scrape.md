---
url: https://docs.firecrawl.dev/api-reference/endpoint/scrape
scraped_at: 2025-05-25T08:58:05.002214
title: Scrape - Firecrawl Docs
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
Scrape Endpoints
Scrape
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
# Scrape
Copy page
POST
/
scrape
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
 --url https://api.firecrawl.dev/v1/scrape \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "url": "<string>",
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
 "data": {
  "markdown": "<string>",
  "html": "<string>",
  "rawHtml": "<string>",
  "screenshot": "<string>",
  "links": [
   "<string>"
  ],
  "actions": {
   "screenshots": [
    "<string>"
   ],
   "scrapes": [
    {
     "url": "<string>",
     "html": "<string>"
    }
   ],
   "javascriptReturns": [
    {
     "type": "<string>",
     "value": "<any>"
    }
   ]
  },
  "metadata": {
   "title": "<string>",
   "description": "<string>",
   "language": "<string>",
   "sourceURL": "<string>",
   "<any other metadata> ": "<string>",
   "statusCode": 123,
   "error": "<string>"
  },
  "llm_extraction": {},
  "warning": "<string>",
  "changeTracking": {
   "previousScrapeAt": "2023-11-07T05:31:56Z",
   "changeStatus": "new",
   "visibility": "visible",
   "diff": "<string>",
   "json": {}
  }
 }
}
```

#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-url)
url
string
required
The URL to scrape
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-formats)
formats
enum<string>[]
Formats to include in the output.
Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-only-main-content)
onlyMainContent
boolean
default:true
Only return the main content of the page excluding headers, navs, footers, etc.
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-include-tags)
includeTags
string[]
Tags to include in the output.
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-exclude-tags)
excludeTags
string[]
Tags to exclude from the output.
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-headers)
headers
object
Headers to send with the request. Can be used to send cookies, user-agent, etc.
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-wait-for)
waitFor
integer
default:0
Specify a delay in milliseconds before fetching the content, allowing the page sufficient time to load.
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-mobile)
mobile
boolean
default:false
Set to true if you want to emulate scraping from a mobile device. Useful for testing responsive pages and taking mobile screenshots.
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-skip-tls-verification)
skipTlsVerification
boolean
default:false
Skip TLS certificate verification when making requests
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-timeout)
timeout
integer
default:30000
Timeout in milliseconds for the request
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-json-options)
jsonOptions
object
Extract object
Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-actions)
actions
object[]
Actions to perform on the page before grabbing the content
  * Wait
  * Screenshot
  * Click
  * Write text
  * Press a key
  * Scroll
  * Scrape
  * Execute JavaScript


Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-location)
location
object
Location settings for the request. When specified, this will use an appropriate proxy if available and emulate the corresponding language and timezone settings. Defaults to 'US' if not specified.
Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-remove-base64-images)
removeBase64Images
boolean
Removes all base 64 images from the output, which may be overwhelmingly long. The image's alt text remains in the output, but the URL is replaced with a placeholder.
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-block-ads)
blockAds
boolean
default:true
Enables ad-blocking and cookie popup blocking.
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-proxy)
proxy
enum<string>
Specifies the type of proxy to use.
  * **basic** : Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
  * **stealth** : Stealth proxies for scraping sites with advanced anti-bot solutions. Slower, but more reliable on certain sites. Starting May 8th, stealth will cost 5 credits per request.


If you do not specify a proxy, Firecrawl will default to basic.
Available options: 
`basic`, 
`stealth`
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-change-tracking-options)
changeTrackingOptions
object
Options for change tracking (Beta). Only applicable when 'changeTracking' is included in formats. The 'markdown' format must also be specified when using change tracking.
Show child attributes
#### Response
200
200402429500
application/json
Successful response
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#response-success)
success
boolean
[​](https://docs.firecrawl.dev/api-reference/endpoint/scrape#response-data)
data
object
Show child attributes
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/scrape.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/scrape)
[Introduction](https://docs.firecrawl.dev/api-reference/introduction)[Batch Scrape](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape)
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
 --url https://api.firecrawl.dev/v1/scrape \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "url": "<string>",
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
 "data": {
  "markdown": "<string>",
  "html": "<string>",
  "rawHtml": "<string>",
  "screenshot": "<string>",
  "links": [
   "<string>"
  ],
  "actions": {
   "screenshots": [
    "<string>"
   ],
   "scrapes": [
    {
     "url": "<string>",
     "html": "<string>"
    }
   ],
   "javascriptReturns": [
    {
     "type": "<string>",
     "value": "<any>"
    }
   ]
  },
  "metadata": {
   "title": "<string>",
   "description": "<string>",
   "language": "<string>",
   "sourceURL": "<string>",
   "<any other metadata> ": "<string>",
   "statusCode": 123,
   "error": "<string>"
  },
  "llm_extraction": {},
  "warning": "<string>",
  "changeTracking": {
   "previousScrapeAt": "2023-11-07T05:31:56Z",
   "changeStatus": "new",
   "visibility": "visible",
   "diff": "<string>",
   "json": {}
  }
 }
}
```

Assistant
Responses are generated using AI and may contain mistakes.

