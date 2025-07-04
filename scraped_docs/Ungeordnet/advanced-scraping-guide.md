---
url: https://docs.firecrawl.dev/advanced-scraping-guide
scraped_at: 2025-05-25T08:32:56.450222
title: Advanced Scraping Guide | Firecrawl
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
Get Started
Advanced Scraping Guide
[Documentation](https://docs.firecrawl.dev/introduction)[SDKs](https://docs.firecrawl.dev/sdks/overview)[Learn](https://www.firecrawl.dev/blog/category/tutorials)[Integrations](https://www.firecrawl.dev/app)[API Reference](https://docs.firecrawl.dev/api-reference/introduction)
* [Playground](https://firecrawl.dev/playground)
* [Blog](https://firecrawl.dev/blog)
* [Community](https://discord.gg/gSmWdAkdwd)
* [Changelog](https://firecrawl.dev/changelog)
##### Get Started
  * [Quickstart](https://docs.firecrawl.dev/introduction)
  * [MCP Server](https://docs.firecrawl.dev/mcp)
  * [Launch Week III (New)](https://docs.firecrawl.dev/launch-week)
  * [Rate Limits](https://docs.firecrawl.dev/rate-limits)
  * [Advanced Scraping Guide](https://docs.firecrawl.dev/advanced-scraping-guide)


##### Standard Features
  * Scrape
  * Crawl
  * [Map](https://docs.firecrawl.dev/features/map)
  * [Search](https://docs.firecrawl.dev/features/search)


##### Agentic Features
  * [Extract](https://docs.firecrawl.dev/features/extract)
  * [FIRE-1](https://docs.firecrawl.dev/agents/fire-1)


##### Alpha tools
  * LLMs.txt API
  * Deep Research API


##### Contributing
  * [Open Source vs Cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud)
  * [Running locally](https://docs.firecrawl.dev/contributing/guide)
  * [Self-hosting](https://docs.firecrawl.dev/contributing/self-host)


Get Started
# Advanced Scraping Guide
Copy page
Learn how to improve your Firecrawl scraping with advanced options.
This guide will walk you through the different endpoints of Firecrawl and how to use them fully with all its parameters.
## 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#basic-scraping-with-firecrawl-%2Fscrape)
Basic scraping with Firecrawl (/scrape)
To scrape a single page and get clean markdown content, you can use the `/scrape` endpoint.
Python
JavaScript
Go
Rust
cURL
Copy
```
# pip install firecrawl-py
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="YOUR_API_KEY")
content = app.scrape_url("https://docs.firecrawl.dev")

```

## 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#scraping-pdfs)
Scraping PDFs
**Firecrawl supports scraping PDFs by default.** You can use the `/scrape` endpoint to scrape a PDF link and get the text content of the PDF. You can disable this by setting `parsePDF` to `false`.
## 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#scrape-options)
Scrape Options
When using the `/scrape` endpoint, you can customize the scraping behavior with many parameters. Here are the available options:
### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-content-formats-on-response-with-formats)
Setting the content formats on response with `formats`
  * **Type** : `array`
  * **Enum** : `["markdown", "links", "html", "rawHtml", "screenshot", "json"]`
  * **Description** : Specify the formats to include in the response. Options include: 
    * `markdown`: Returns the scraped content in Markdown format.
    * `links`: Includes all hyperlinks found on the page.
    * `html`: Provides the content in HTML format.
    * `rawHtml`: Delivers the raw HTML content, without any processing.
    * `screenshot`: Includes a screenshot of the page as it appears in the browser.
    * `json`: Extracts structured information from the page using the LLM.
  * **Default** : `["markdown"]`


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#getting-the-full-page-content-as-markdown-with-onlymaincontent)
Getting the full page content as markdown with `onlyMainContent`
  * **Type** : `boolean`
  * **Description** : By default, the scraper will only return the main content of the page, excluding headers, navigation bars, footers, etc. Set this to `false` to return the full page content.
  * **Default** : `true`


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-tags-to-include-with-includetags)
Setting the tags to include with `includeTags`
  * **Type** : `array`
  * **Description** : Specify the HTML tags, classes and ids to include in the response.
  * **Default** : undefined


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-tags-to-exclude-with-excludetags)
Setting the tags to exclude with `excludeTags`
  * **Type** : `array`
  * **Description** : Specify the HTML tags, classes and ids to exclude from the response.
  * **Default** : undefined


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#waiting-for-the-page-to-load-with-waitfor)
Waiting for the page to load with `waitFor`
  * **Type** : `integer`
  * **Description** : To be used only as a last resort. Wait for a specified amount of milliseconds for the page to load before fetching content.
  * **Default** : `0`


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-maximum-timeout)
Setting the maximum `timeout`
  * **Type** : `integer`
  * **Description** : Set the maximum duration in milliseconds that the scraper will wait for the page to respond before aborting the operation.
  * **Default** : `30000` (30 seconds)


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#example-usage)
Example Usage
Copy
```
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H '
  Content-Type: application/json' \
  -H 'Authorization : Bearer YOUR_API_KEY' \
  -d '{
   "url": "https://docs.firecrawl.dev",
   "formats": ["markdown", "links", "html", "rawHtml", "screenshot"],
   "includeTags": ["h1", "p", "a", ".main-content"],
   "excludeTags": ["#ad", "#footer"],
   "onlyMainContent": false,
   "waitFor": 1000,
   "timeout": 15000
  }'

```

In this example, the scraper will:
  * Return the full page content as markdown.
  * Include the markdown, raw HTML, HTML, links and screenshot in the response.
  * The response will include only the HTML tags `<h1>`, `<p>`, `<a>`, and elements with the class `.main-content`, while excluding any elements with the IDs `#ad` and `#footer`.
  * Wait for 1000 milliseconds (1 second) for the page to load before fetching the content.
  * Set the maximum duration of the scrape request to 15000 milliseconds (15 seconds).


Here is the API Reference for it: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
## 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#extractor-options)
Extractor Options
When using the `/scrape` endpoint, you can specify options for **extracting structured information** from the page content using the `extract` parameter. Here are the available options:
### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#using-the-llm-extraction)
Using the LLM Extraction
### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#schema)
schema
  * **Type** : `object`
  * **Required** : False if prompt is provided
  * **Description** : The schema for the data to be extracted. This defines the structure of the extracted data.


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#system-prompt)
system prompt
  * **Type** : `string`
  * **Required** : False
  * **Description** : System prompt for the LLM.


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#prompt)
prompt
  * **Type** : `string`
  * **Required** : False if schema is provided
  * **Description** : A prompt for the LLM to extract the data in the correct structure.
  * **Example** : `"Extract the features of the product"`


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#example-usage-2)
Example Usage
Copy
```
curl -X POST https://api.firecrawl.dev/v0/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
   "url": "https://firecrawl.dev",
   "formats": ["markdown", "json"],
   "json": {
    "prompt": "Extract the features of the product"
   }
  }'

```

Copy
```
{
 "success": true,
 "data": {
  "content": "Raw Content",
  "metadata": {
   "title": "Mendable",
   "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
   "robots": "follow, index",
   "ogTitle": "Mendable",
   "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
   "ogUrl": "https://docs.firecrawl.dev/",
   "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
   "ogLocaleAlternate": [],
   "ogSiteName": "Mendable",
   "sourceURL": "https://docs.firecrawl.dev/",
   "statusCode": 200
  },
  "extract": {
   "product": "Firecrawl",
   "features": {
    "general": {
     "description": "Turn websites into LLM-ready data.",
     "openSource": true,
     "freeCredits": 500,
     "useCases": [
      "AI applications",
      "Data science",
      "Market research",
      "Content aggregation"
     ]
    },
    "crawlingAndScraping": {
     "crawlAllAccessiblePages": true,
     "noSitemapRequired": true,
     "dynamicContentHandling": true,
     "dataCleanliness": {
      "process": "Advanced algorithms",
      "outputFormat": "Markdown"
     }
    },
    ...
   }
  }
 }
}

```

## 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#actions)
Actions
When using the `/scrape` endpoint, Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#available-actions)
Available Actions
#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#wait)
wait
  * **Type** : `object`
  * **Description** : Wait for a specified amount of milliseconds.
  * **Properties** : 
    * `type`: `"wait"`
    * `milliseconds`: Number of milliseconds to wait.
  * **Example** : 
Copy
```
{
 "type": "wait",
 "milliseconds": 2000
}

```



#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#screenshot)
screenshot
  * **Type** : `object`
  * **Description** : Take a screenshot.
  * **Properties** : 
    * `type`: `"screenshot"`
    * `fullPage`: Should the screenshot be full-page or viewport sized? (default: `false`)
  * **Example** : 
Copy
```
{
 "type": "screenshot",
 "fullPage": true
}

```



#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#click)
click
  * **Type** : `object`
  * **Description** : Click on an element.
  * **Properties** : 
    * `type`: `"click"`
    * `selector`: Query selector to find the element by.
  * **Example** : 
Copy
```
{
 "type": "click",
 "selector": "#load-more-button"
}

```



#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#write)
write
  * **Type** : `object`
  * **Description** : Write text into an input field.
  * **Properties** : 
    * `type`: `"write"`
    * `text`: Text to type.
    * `selector`: Query selector for the input field.
  * **Example** : 
Copy
```
{
 "type": "write",
 "text": "Hello, world!",
 "selector": "#search-input"
}

```



#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#press)
press
  * **Type** : `object`
  * **Description** : Press a key on the page.
  * **Properties** : 
    * `type`: `"press"`
    * `key`: Key to press.
  * **Example** : 
Copy
```
{
 "type": "press",
 "key": "Enter"
}

```



#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#scroll)
scroll
  * **Type** : `object`
  * **Description** : Scroll the page.
  * **Properties** : 
    * `type`: `"scroll"`
    * `direction`: Direction to scroll (`"up"` or `"down"`).
    * `amount`: Amount to scroll in pixels.
  * **Example** : 
Copy
```
{
 "type": "scroll",
 "direction": "down",
 "amount": 500
}

```



For more details about the actions parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).
## 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#crawling-multiple-pages)
Crawling Multiple Pages
To crawl multiple pages, you can use the `/crawl` endpoint. This endpoint allows you to specify a base URL you want to crawl and all accessible subpages will be crawled.
Copy
```
curl -X POST https://api.firecrawl.dev/v1/crawl \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
   "url": "https://docs.firecrawl.dev"
  }'

```

Returns a id
Copy
```
{ "id": "1234-5678-9101" }

```

### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#check-crawl-job)
Check Crawl Job
Used to check the status of a crawl job and get its result.
Copy
```
curl -X GET https://api.firecrawl.dev/v1/crawl/1234-5678-9101 \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer YOUR_API_KEY'

```

#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#pagination%2Fnext-url)
Pagination/Next URL
If the content is larger than 10MB or if the crawl job is still running, the response will include a `next` parameter. This parameter is a URL to the next page of results. You can use this parameter to get the next page of results.
### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#crawler-options)
Crawler Options
When using the `/crawl` endpoint, you can customize the crawling behavior with request body parameters. Here are the available options:
#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#includepaths)
`includePaths`
  * **Type** : `array`
  * **Description** : Regex patterns to include in the crawl. Only URLs matching these patterns will be crawled. For example, `^/blog/.*` will match any URL that starts with `/blog/`.
  * **Example** : `["^/blog/.*$", "^/docs/.*$"]`


#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#excludepaths)
`excludePaths`
  * **Type** : `array`
  * **Description** : Regex patterns to exclude from the crawl. URLs matching these patterns will be skipped. For example, `^/admin/.*` will exclude any URL that starts with `/admin/`.
  * **Example** : `["^/admin/.*$", "^/private/.*$"]`


#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#maxdepth)
`maxDepth`
  * **Type** : `integer`
  * **Description** : Maximum depth to crawl relative to the entered URL. A maxDepth of 0 scrapes only the entered URL. A maxDepth of 1 scrapes the entered URL and all pages one level deep. A maxDepth of 2 scrapes the entered URL and all pages up to two levels deep. Higher values follow the same pattern.
  * **Example** : `2`


#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#limit)
`limit`
  * **Type** : `integer`
  * **Description** : Maximum number of pages to crawl.
  * **Default** : `10000`


#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#allowbackwardlinks)
`allowBackwardLinks`
  * **Type** : `boolean`
  * **Description** : Allows the crawler to follow internal links to sibling or parent URLs, not just child paths. 
    * **false** : Only crawls deeper (child) URLs. 
      * e.g. /features/feature-1 → /features/feature-1/tips ✅
      * Won’t follow /pricing or / ❌
    * **true** : Crawls any internal links, including siblings and parents. 
      * e.g. /features/feature-1 → /pricing, /, etc. ✅
    * Use true for broader internal coverage beyond nested paths.
  * **Default** : `false`


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#allowexternallinks)
`allowExternalLinks`
  * **Type** : `boolean`
  * **Description** : This option allows the crawler to follow links that point to external domains. Be careful with this option, as it can cause the crawl to stop only based only on the`limit` and `maxDepth` values.
  * **Default** : `false`


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#delay)
`delay`
  * **Type** : `number`
  * **Description** : Delay in seconds between scrapes. This helps respect website rate limits and prevent overwhelming the target website. If not provided, the crawler may use the robots.txt crawl delay if available.
  * **Default** : `undefined`


#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#scrapeoptions)
scrapeOptions
As part of the crawler options, you can also specify the `scrapeOptions` parameter. This parameter allows you to customize the scraping behavior for each page.
  * **Type** : `object`
  * **Description** : Options for the scraper.
  * **Example** : `{"formats": ["markdown", "links", "html", "rawHtml", "screenshot"], "includeTags": ["h1", "p", "a", ".main-content"], "excludeTags": ["#ad", "#footer"], "onlyMainContent": false, "waitFor": 1000, "timeout": 15000}`
  * **Default** : `{ "formats": ["markdown"] }`
  * **See** : [Scrape Options](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-content-formats-on-response-with-formats)


### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#example-usage-3)
Example Usage
Copy
```
curl -X POST https://api.firecrawl.dev/v1/crawl \
  -H 'Content-Type: application/json' \
  -H 'Authorization : Bearer YOUR_API_KEY' \
  -d '{
   "url": "https://docs.firecrawl.dev",
   "includePaths": ["^/blog/.*$", "^/docs/.*$"],
   "excludePaths": ["^/admin/.*$", "^/private/.*$"],
   "maxDepth": 2,
   "limit": 1000
  }'

```

In this example, the crawler will:
  * Only crawl URLs that match the patterns `^/blog/.*$` and `^/docs/.*$`.
  * Skip URLs that match the patterns `^/admin/.*$` and `^/private/.*$`.
  * Return the full document data for each page.
  * Crawl up to a maximum depth of 2.
  * Crawl a maximum of 1000 pages.


## 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#mapping-website-links-with-%2Fmap)
Mapping Website Links with `/map`
The `/map` endpoint is adept at identifying URLs that are contextually related to a given website. This feature is crucial for understanding a site’s contextual link environment, which can greatly aid in strategic site analysis and navigation planning.
### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#usage)
Usage
To use the `/map` endpoint, you need to send a GET request with the URL of the page you want to map. Here is an example using `curl`:
Copy
```
curl -X POST https://api.firecrawl.dev/v1/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
   "url": "https://docs.firecrawl.dev"
  }'

```

This will return a JSON object containing links contextually related to the url.
### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#example-response)
Example Response
Copy
```
 {
  "success":true,
  "links":[
   "https://docs.firecrawl.dev",
   "https://docs.firecrawl.dev/api-reference/endpoint/crawl-delete",
   "https://docs.firecrawl.dev/api-reference/endpoint/crawl-get",
   "https://docs.firecrawl.dev/api-reference/endpoint/crawl-post",
   "https://docs.firecrawl.dev/api-reference/endpoint/map",
   "https://docs.firecrawl.dev/api-reference/endpoint/scrape",
   "https://docs.firecrawl.dev/api-reference/introduction",
   "https://docs.firecrawl.dev/articles/search-announcement",
   ...
  ]
 }

```

### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#map-options)
Map Options
#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#search)
`search`
  * **Type** : `string`
  * **Description** : Search for links containing specific text.
  * **Example** : `"blog"`


#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#limit-2)
`limit`
  * **Type** : `integer`
  * **Description** : Maximum number of links to return.
  * **Default** : `100`


#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#ignoresitemap)
`ignoreSitemap`
  * **Type** : `boolean`
  * **Description** : Ignore the website sitemap when crawling
  * **Default** : `true`


#### 
[​](https://docs.firecrawl.dev/advanced-scraping-guide#includesubdomains)
`includeSubdomains`
  * **Type** : `boolean`
  * **Description** : Include subdomains of the website
  * **Default** : `false`


Here is the API Reference for it: [Map Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/map)
Thanks for reading!
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/advanced-scraping-guide.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /advanced-scraping-guide)
[Rate Limits](https://docs.firecrawl.dev/rate-limits)[Scrape](https://docs.firecrawl.dev/features/scrape)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Basic scraping with Firecrawl (/scrape)](https://docs.firecrawl.dev/advanced-scraping-guide#basic-scraping-with-firecrawl-%2Fscrape)
  * [Scraping PDFs](https://docs.firecrawl.dev/advanced-scraping-guide#scraping-pdfs)
  * [Scrape Options](https://docs.firecrawl.dev/advanced-scraping-guide#scrape-options)
  * [Setting the content formats on response with formats](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-content-formats-on-response-with-formats)
  * [Getting the full page content as markdown with onlyMainContent](https://docs.firecrawl.dev/advanced-scraping-guide#getting-the-full-page-content-as-markdown-with-onlymaincontent)
  * [Setting the tags to include with includeTags](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-tags-to-include-with-includetags)
  * [Setting the tags to exclude with excludeTags](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-tags-to-exclude-with-excludetags)
  * [Waiting for the page to load with waitFor](https://docs.firecrawl.dev/advanced-scraping-guide#waiting-for-the-page-to-load-with-waitfor)
  * [Setting the maximum timeout](https://docs.firecrawl.dev/advanced-scraping-guide#setting-the-maximum-timeout)
  * [Example Usage](https://docs.firecrawl.dev/advanced-scraping-guide#example-usage)
  * [Extractor Options](https://docs.firecrawl.dev/advanced-scraping-guide#extractor-options)
  * [Using the LLM Extraction](https://docs.firecrawl.dev/advanced-scraping-guide#using-the-llm-extraction)
  * [schema](https://docs.firecrawl.dev/advanced-scraping-guide#schema)
  * [system prompt](https://docs.firecrawl.dev/advanced-scraping-guide#system-prompt)
  * [prompt](https://docs.firecrawl.dev/advanced-scraping-guide#prompt)
  * [Example Usage](https://docs.firecrawl.dev/advanced-scraping-guide#example-usage-2)
  * [Actions](https://docs.firecrawl.dev/advanced-scraping-guide#actions)
  * [Available Actions](https://docs.firecrawl.dev/advanced-scraping-guide#available-actions)
  * [wait](https://docs.firecrawl.dev/advanced-scraping-guide#wait)
  * [screenshot](https://docs.firecrawl.dev/advanced-scraping-guide#screenshot)
  * [click](https://docs.firecrawl.dev/advanced-scraping-guide#click)
  * [write](https://docs.firecrawl.dev/advanced-scraping-guide#write)
  * [press](https://docs.firecrawl.dev/advanced-scraping-guide#press)
  * [scroll](https://docs.firecrawl.dev/advanced-scraping-guide#scroll)
  * [Crawling Multiple Pages](https://docs.firecrawl.dev/advanced-scraping-guide#crawling-multiple-pages)
  * [Check Crawl Job](https://docs.firecrawl.dev/advanced-scraping-guide#check-crawl-job)
  * [Pagination/Next URL](https://docs.firecrawl.dev/advanced-scraping-guide#pagination%2Fnext-url)
  * [Crawler Options](https://docs.firecrawl.dev/advanced-scraping-guide#crawler-options)
  * [includePaths](https://docs.firecrawl.dev/advanced-scraping-guide#includepaths)
  * [excludePaths](https://docs.firecrawl.dev/advanced-scraping-guide#excludepaths)
  * [maxDepth](https://docs.firecrawl.dev/advanced-scraping-guide#maxdepth)
  * [limit](https://docs.firecrawl.dev/advanced-scraping-guide#limit)
  * [allowBackwardLinks](https://docs.firecrawl.dev/advanced-scraping-guide#allowbackwardlinks)
  * [allowExternalLinks](https://docs.firecrawl.dev/advanced-scraping-guide#allowexternallinks)
  * [delay](https://docs.firecrawl.dev/advanced-scraping-guide#delay)
  * [scrapeOptions](https://docs.firecrawl.dev/advanced-scraping-guide#scrapeoptions)
  * [Example Usage](https://docs.firecrawl.dev/advanced-scraping-guide#example-usage-3)
  * [Mapping Website Links with /map](https://docs.firecrawl.dev/advanced-scraping-guide#mapping-website-links-with-%2Fmap)
  * [Usage](https://docs.firecrawl.dev/advanced-scraping-guide#usage)
  * [Example Response](https://docs.firecrawl.dev/advanced-scraping-guide#example-response)
  * [Map Options](https://docs.firecrawl.dev/advanced-scraping-guide#map-options)
  * [search](https://docs.firecrawl.dev/advanced-scraping-guide#search)
  * [limit](https://docs.firecrawl.dev/advanced-scraping-guide#limit-2)
  * [ignoreSitemap](https://docs.firecrawl.dev/advanced-scraping-guide#ignoresitemap)
  * [includeSubdomains](https://docs.firecrawl.dev/advanced-scraping-guide#includesubdomains)


Assistant
Responses are generated using AI and may contain mistakes.

