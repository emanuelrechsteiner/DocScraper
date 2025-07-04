---
url: https://docs.firecrawl.dev/features/llm-extract
scraped_at: 2025-05-25T08:58:19.178252
title: JSON mode | Firecrawl
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
Scrape
JSON mode - LLM Extract
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
    * [Scrape](https://docs.firecrawl.dev/features/scrape)
    * [Batch Scrape](https://docs.firecrawl.dev/features/batch-scrape)
    * [JSON mode](https://docs.firecrawl.dev/features/llm-extract)
    * [Change Tracking (New)](https://docs.firecrawl.dev/features/change-tracking)
    * [Stealth Mode](https://docs.firecrawl.dev/features/stealth-mode)
    * [Proxies](https://docs.firecrawl.dev/features/proxies)
    * [Webhooks](https://docs.firecrawl.dev/features/webhooks)
  * Crawl
    * [Crawl](https://docs.firecrawl.dev/features/crawl)
    * [JSON mode](https://docs.firecrawl.dev/features/llm-extract)
    * [Change Tracking with Crawl (New)](https://docs.firecrawl.dev/features/change-tracking-crawl)
    * [Webhooks](https://docs.firecrawl.dev/features/webhooks)
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


Scrape
# JSON mode - LLM Extract
Copy page
Extract structured data from pages via LLMs
## 
[​](https://docs.firecrawl.dev/features/llm-extract#scrape-and-extract-structured-data-with-firecrawl)
Scrape and extract structured data with Firecrawl
Firecrawl uses AI to get structured data from web pages in 3 steps:
  1. **Set the Schema:** Tell us what data you want by defining a JSON schema (using OpenAI’s format) along with the webpage URL.
  2. **Make the Request:** Send your URL and schema to our scrape endpoint. See how here: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
  3. **Get Your Data:** Get back clean, structured data matching your schema that you can use right away.


This makes getting web data in the format you need quick and easy.
## 
[​](https://docs.firecrawl.dev/features/llm-extract#extract-structured-data)
Extract structured data
### 
[​](https://docs.firecrawl.dev/features/llm-extract#%2Fscrape-with-json-endpoint)
/scrape (with json) endpoint
Used to extract structured data from scraped pages.
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp, JsonConfig
from pydantic import BaseModel, Field
# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key')
class ExtractSchema(BaseModel):
  company_mission: str
  supports_sso: bool
  is_open_source: bool
  is_in_yc: bool
json_config = JsonConfig(
  extractionSchema=ExtractSchema.model_json_schema(),
  mode="llm-extraction",
  pageOptions={"onlyMainContent": True}
)
llm_extraction_result = app.scrape_url(
  'https://firecrawl.dev',
  formats=["json"],
  json_options=json_config
)
print(llm_extraction_result)

```

Output:
JSON
Copy
```
{
  "success": true,
  "data": {
   "json": {
    "company_mission": "AI-powered web scraping and data extraction",
    "supports_sso": true,
    "is_open_source": true,
    "is_in_yc": true
   },
   "metadata": {
    "title": "Firecrawl",
    "description": "AI-powered web scraping and data extraction",
    "robots": "follow, index",
    "ogTitle": "Firecrawl",
    "ogDescription": "AI-powered web scraping and data extraction",
    "ogUrl": "https://firecrawl.dev/",
    "ogImage": "https://firecrawl.dev/og.png",
    "ogLocaleAlternate": [],
    "ogSiteName": "Firecrawl",
    "sourceURL": "https://firecrawl.dev/"
   },
  }
}

```

### 
[​](https://docs.firecrawl.dev/features/llm-extract#extracting-without-schema-new)
Extracting without schema (New)
You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.
cURL
Copy
```
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
   "url": "https://docs.firecrawl.dev/",
   "formats": ["json"],
   "jsonOptions": {
    "prompt": "Extract the company mission from the page."
   }
  }'

```

Output:
JSON
Copy
```
{
  "success": true,
  "data": {
   "json": {
    "company_mission": "AI-powered web scraping and data extraction",
   },
   "metadata": {
    "title": "Firecrawl",
    "description": "AI-powered web scraping and data extraction",
    "robots": "follow, index",
    "ogTitle": "Firecrawl",
    "ogDescription": "AI-powered web scraping and data extraction",
    "ogUrl": "https://firecrawl.dev/",
    "ogImage": "https://firecrawl.dev/og.png",
    "ogLocaleAlternate": [],
    "ogSiteName": "Firecrawl",
    "sourceURL": "https://firecrawl.dev/"
   },
  }
}

```

### 
[​](https://docs.firecrawl.dev/features/llm-extract#extract-object)
Extract object
The `extract` object accepts the following parameters:
  * `schema`: The schema to use for the extraction.
  * `systemPrompt`: The system prompt to use for the extraction.
  * `prompt`: The prompt to use for the extraction without a schema.


[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/llm-extract.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/llm-extract)
[Batch Scrape](https://docs.firecrawl.dev/features/batch-scrape)[Change Tracking (New)](https://docs.firecrawl.dev/features/change-tracking)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Scrape and extract structured data with Firecrawl](https://docs.firecrawl.dev/features/llm-extract#scrape-and-extract-structured-data-with-firecrawl)
  * [Extract structured data](https://docs.firecrawl.dev/features/llm-extract#extract-structured-data)
  * [/scrape (with json) endpoint](https://docs.firecrawl.dev/features/llm-extract#%2Fscrape-with-json-endpoint)
  * [Extracting without schema (New)](https://docs.firecrawl.dev/features/llm-extract#extracting-without-schema-new)
  * [Extract object](https://docs.firecrawl.dev/features/llm-extract#extract-object)


Assistant
Responses are generated using AI and may contain mistakes.

