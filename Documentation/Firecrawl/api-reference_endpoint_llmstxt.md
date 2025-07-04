---
url: https://docs.firecrawl.dev/api-reference/endpoint/llmstxt
scraped_at: 2025-05-25T08:35:24.793829
title: Generate LLMs.txt - Firecrawl Docs
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
Generate LLMs.txt
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


# Generate LLMs.txt
Copy page
POST
/
llmstxt
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
 --url https://api.firecrawl.dev/v1/llmstxt \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "url": "<string>",
 "maxUrls": 2,
 "showFullText": false
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

The LLMs.txt generation endpoint creates LLMs.txt and LLMs-full.txt files for any website. These files provide a structured, LLM-friendly format of the website’s content, making it easier for language models to understand and process the information.
Looking for the status endpoint? Check out the [LLMs.txt Status](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt-get) endpoint.
### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#response-structure)
Response Structure
The response includes:
  * **success** : Boolean indicating if the request was successful
  * **id** : Unique identifier for the generation job


### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#output-format)
Output Format
  1. **LLMs.txt**
     * Concise, structured summary of the website
     * Contains key links and descriptions
     * Formatted in markdown for easy parsing
     * Example:
Copy
```
# http://example.com llms.txt
- [Page Title](https://example.com/page): Brief description
- [Another Page](https://example.com/another): Another description

```

  2. **LLMs-full.txt** (when showFullText is true)
     * Contains full content of processed pages
     * Maintains hierarchical structure
     * Includes more detailed information
     * Example:
Copy
```
# http://example.com llms-full.txt
## Page Title
Full content of the page...
## Another Page
More detailed content...

```



### 
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#billing)
Billing
Billing is based on API calls and URLs processed:
  * Base cost: 1 credit per API call
  * Additional: 1 credit per URL processed
  * Control URL costs with `maxUrls` parameter


#### Authorizations
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#body-url)
url
string
required
The URL to generate LLMs.txt from
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#body-max-urls)
maxUrls
integer
default:2
Maximum number of URLs to analyze
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#body-show-full-text)
showFullText
boolean
default:false
Include full text content in the response
#### Response
200
200400
application/json
LLMs.txt generation job started successfully
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#response-success)
success
boolean
Example:
`true`
[​](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt#response-id)
id
string
ID of the LLMs.txt generation job
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/api-reference/endpoint/llmstxt.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /api-reference/endpoint/llmstxt)
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
 --url https://api.firecrawl.dev/v1/llmstxt \
 --header 'Authorization: Bearer <token>' \
 --header 'Content-Type: application/json' \
 --data '{
 "url": "<string>",
 "maxUrls": 2,
 "showFullText": false
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

