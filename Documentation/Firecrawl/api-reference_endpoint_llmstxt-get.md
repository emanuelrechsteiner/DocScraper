---
url: https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get
scraped_at: 2025-05-25T08:35:35.572644
title: LLMs.txt Status - Firecrawl Docs
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
LLMs.txt Status
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


# LLMs.txt Status
Copy page
GET
/
llmstxt
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
 --url https://api.firecrawl.dev/v1/llmstxt/{id} \
 --header 'Authorization: Bearer <token>'
```

200
404
Copy
```
{
 "success": true,
 "status": "processing",
 "data": {
  "llmstxt": "<string>",
  "llmsfulltxt": "<string>"
 },
 "expiresAt": "2023-11-07T05:31:56Z"
}
```

Get the status and results of an LLMs.txt generation job. This endpoint allows you to check if the generation is complete and retrieve the generated content.
### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#response-structure)
Response Structure
The response includes:
  * **success** : Boolean indicating if the request was successful
  * **status** : Current status of the generation job:
    * `processing`: Job is still running
    * `completed`: Job finished successfully
    * `failed`: Job encountered an error
  * **data** : Generated content (when status is `completed`):
    * `llmstxt`: The generated LLMs.txt content
    * `llmsfulltxt`: Full text content (if showFullText was true)
  * **expiresAt** : ISO timestamp indicating when the results will expire


### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#status-examples)
Status Examples
  1. **Processing Status**
Copy
```
{
 "success": true,
 "status": "processing",
 "data": {
  "llmstxt": "# Firecrawl.dev llms.txt\n\n- [Web Data Extraction Tool](https://www.firecrawl.dev/)...",
  "llmsfulltxt": "# Firecrawl.dev llms-full.txt\n\n"
 },
 "expiresAt": "2025-03-03T23:19:18.000Z"
}

```

  2. **Completed Status**
Copy
```
{
 "success": true,
 "status": "completed",
 "data": {
  "llmstxt": "# http://firecrawl.dev llms.txt\n\n- [Web Data Extraction Tool](https://www.firecrawl.dev/): Transform websites into clean, LLM-ready data effortlessly.\n- [Flexible Web Scraping Pricing](https://www.firecrawl.dev/pricing): Flexible pricing plans for web scraping and data extraction.",
  "llmsfulltxt": "# http://firecrawl.dev llms-full.txt\n\n## Web Data Extraction Tool\nIntroducing /extract - Get web data with a prompt..."
 },
 "expiresAt": "2025-03-03T22:45:50.000Z"
}

```



### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#error-handling)
Error Handling
If the generation job fails or cannot be found, you’ll receive an appropriate error response:
Copy
```
{
 "success": false,
 "error": "LLMs.txt generation job not found"
}

```

### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#polling-recommendations)
Polling Recommendations
  1. Poll every 2-3 seconds initially
  2. Increase interval if still processing after 30 seconds
  3. Stop polling if status is `completed` or `failed`
  4. Implement exponential backoff to avoid rate limits


#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Path Parameters
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#parameter-id)
id
string
required
The ID of the LLMs.txt generation job
#### Response
200
200404
application/json
Successful response
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#response-success)
success
boolean
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#response-status)
status
enum<string>
Available options: 
`processing`, 
`completed`, 
`failed`
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#response-data)
data
object
Show child attributes
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get#response-expires-at)
expiresAt
string
When the generated content will expire
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/llmstxt-get.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/llmstxt-get)
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
 --url https://api.firecrawl.dev/v1/llmstxt/{id} \
 --header 'Authorization: Bearer <token>'
```

200
404
Copy
```
{
 "success": true,
 "status": "processing",
 "data": {
  "llmstxt": "<string>",
  "llmsfulltxt": "<string>"
 },
 "expiresAt": "2023-11-07T05:31:56Z"
}
```

Assistant
Responses are generated using AI and may contain mistakes.

