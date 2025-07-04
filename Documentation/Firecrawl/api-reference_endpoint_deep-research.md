---
url: https://docs.firecrawl.dev/api-reference/endpoint/deep-research
scraped_at: 2025-05-25T08:35:49.976288
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
POST
/
deep-research
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
 --url https://api.firecrawl.dev/v1/deep-research \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "query": "<string>",
 "maxDepth": 7,
 "timeLimit": 300,
 "maxUrls": 20,
 "analysisPrompt": "<string>",
 "systemPrompt": "<string>",
 "formats": [
  [
   "markdown"
  ]
 ],
 "jsonOptions": {
  "schema": {},
  "systemPrompt": "<string>",
  "prompt": "<string>"
 }
}'
```

200
400
Copy
```
{
 "success": true,
 "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
}
```

The Deep Research endpoint enables AI-powered deep research and analysis on any topic. Simply provide a research query, and Firecrawl will autonomously explore the web, gather relevant information, and synthesize findings into comprehensive insights.
Looking for the status endpoint? Check out the [Deep Research Status](https://docs.firecrawl.dev/api-reference/endpoint/deep-research-get) endpoint.
### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#response-structure)
Response Structure
The response includes:
  * **activities** : List of research activities with:
    * `type`: Activity type (‘search’, ‘extract’, ‘analyze’, ‘reasoning’, ‘synthesis’, ‘thought’)
    * `status`: Status (‘processing’, ‘complete’, ‘error’)
    * `message`: Description of activity/finding
    * `timestamp`: ISO timestamp
    * `depth`: Research depth level
  * **sources** : Referenced URLs with:
    * `title`: Source title
    * `description`: Source description
    * `url`: Source URL
    * `icon`: Source favicon
  * **finalAnalysis** : Comprehensive analysis (when completed)
  * **status** : Overall status (‘processing’, ‘completed’, ‘failed’)
  * **currentDepth** : Current research depth
  * **maxDepth** : Maximum research depth
  * **totalUrls** : Number of URLs analyzed
  * **expiresAt** : ISO timestamp when results expire


### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#limitations)
Limitations
  1. Best suited for topics with publicly available information
  2. Research jobs limited to 10 minutes maximum
  3. Manual verification recommended for critical information
  4. Alpha feature - methodology and output may evolve


### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#billing)
Billing
Billing is based on number of URLs analyzed:
  * Each URL = 1 credit
  * Control usage with `maxUrls` parameter


#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#body-query)
query
string
required
The query to research
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#body-max-depth)
maxDepth
integer
default:7
Maximum depth of research iterations
Required range: `1 <= x <= 12`
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#body-time-limit)
timeLimit
integer
default:300
Time limit in seconds
Required range: `30 <= x <= 600`
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#body-max-urls)
maxUrls
integer
default:20
Maximum number of URLs to analyze
Required range: `1 <= x <= 1000`
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#body-analysis-prompt)
analysisPrompt
string
The prompt to use for the final analysis. Useful to format the final analysis markdown in a specific way.
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#body-system-prompt)
systemPrompt
string
The system prompt to use for the research agent. Useful to steer the research agent to a specific direction.
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#body-formats)
formats
enum<string>[]
Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#body-json-options)
jsonOptions
object
Options for JSON output
Show child attributes
#### Response
200
200400
application/json
Research job started successfully
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#response-success)
success
boolean
Example:
`true`
[​](https://docs.firecrawl.dev/api-reference/endpoint/deep-research#response-id)
id
string
ID of the research job
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/deep-research.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/deep-research)
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
 --url https://api.firecrawl.dev/v1/deep-research \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "query": "<string>",
 "maxDepth": 7,
 "timeLimit": 300,
 "maxUrls": 20,
 "analysisPrompt": "<string>",
 "systemPrompt": "<string>",
 "formats": [
  [
   "markdown"
  ]
 ],
 "jsonOptions": {
  "schema": {},
  "systemPrompt": "<string>",
  "prompt": "<string>"
 }
}'
```

200
400
Copy
```
{
 "success": true,
 "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
}
```

Assistant
Responses are generated using AI and may contain mistakes.

