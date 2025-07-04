---
url: https://docs.firecrawl.dev/api-reference/endpoint/extract
scraped_at: 2025-05-25T08:57:39.618367
title: Extract - Firecrawl Docs
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
Extract Endpoints
Extract
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


Extract Endpoints
# Extract
Copy page
POST
/
extract
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
 --url https://api.firecrawl.dev/v1/extract \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "urls": [
  "<string>"
 ],
 "prompt": "<string>",
 "schema": {},
 "enableWebSearch": false,
 "ignoreSitemap": false,
 "includeSubdomains": true,
 "showSources": false,
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
 },
 "ignoreInvalidURLs": false
}'
```

200
400
500
Copy
```
{
 "success": true,
 "id": "<string>",
 "invalidURLs": [
  "<string>"
 ]
}
```

#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-urls)
urls
string[]
required
The URLs to extract data from. URLs should be in glob format.
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-prompt)
prompt
string
Prompt to guide the extraction process
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-schema)
schema
object
Schema to define the structure of the extracted data. Must conform to [JSON Schema](https://json-schema.org/).
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-enable-web-search)
enableWebSearch
boolean
default:false
When true, the extraction will use web search to find additional data
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-ignore-sitemap)
ignoreSitemap
boolean
default:false
When true, sitemap.xml files will be ignored during website scanning
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-include-subdomains)
includeSubdomains
boolean
default:true
When true, subdomains of the provided URLs will also be scanned
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-show-sources)
showSources
boolean
default:false
When true, the sources used to extract the data will be included in the response as `sources` key
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-scrape-options)
scrapeOptions
object
Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#body-ignore-invalid-urls)
ignoreInvalidURLs
boolean
default:false
If invalid URLs are specified in the urls array, they will be ignored. Instead of them failing the entire request, an extract using the remaining valid URLs will be performed, and the invalid URLs will be returned in the invalidURLs field of the response.
#### Response
200
200400500
application/json
Successful extraction
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#response-success)
success
boolean
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#response-id)
id
string
[​](https://docs.firecrawl.dev/api-reference/endpoint/extract#response-invalid-urls)
invalidURLs
string[] | null
If ignoreInvalidURLs is true, this is an array containing the invalid URLs that were specified in the request. If there were no invalid URLs, this will be an empty array. If ignoreInvalidURLs is false, this field will be undefined.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/extract.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/extract)
[Search](https://docs.firecrawl.dev/api-reference/endpoint/search)[Get Extract Status](https://docs.firecrawl.dev/api-reference/endpoint/extract-get)
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
 --url https://api.firecrawl.dev/v1/extract \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "urls": [
  "<string>"
 ],
 "prompt": "<string>",
 "schema": {},
 "enableWebSearch": false,
 "ignoreSitemap": false,
 "includeSubdomains": true,
 "showSources": false,
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
 },
 "ignoreInvalidURLs": false
}'
```

200
400
500
Copy
```
{
 "success": true,
 "id": "<string>",
 "invalidURLs": [
  "<string>"
 ]
}
```

Assistant
Responses are generated using AI and may contain mistakes.

