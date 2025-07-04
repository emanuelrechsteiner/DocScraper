---
url: https://docs.firecrawl.dev/features/extract
scraped_at: 2025-05-25T08:58:15.595114
title: Extract | Firecrawl
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
Agentic Features
Extract
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


Agentic Features
# Extract
Copy page
Extract structured data from pages using LLMs
The `/extract` endpoint simplifies collecting structured data from any number of URLs or entire domains. Provide a list of URLs, optionally with wildcards (e.g., `example.com/*`), and a prompt or schema describing the information you want. Firecrawl handles the details of crawling, parsing, and collating large or small datasets.
Extract is billed differently than other endpoints. See the [Extract pricing](https://www.firecrawl.dev/extract#pricing) for details.
## 
[​](https://docs.firecrawl.dev/features/extract#using-%2Fextract)
Using `/extract`
You can extract structured data from one or multiple URLs, including wildcards:
  * **Single Page** Example: `https://firecrawl.dev/some-page`
  * **Multiple Pages / Full Domain** Example: `https://firecrawl.dev/*`


When you use `/*`, Firecrawl will automatically crawl and parse all URLs it can discover in that domain, then extract the requested data. This feature is experimental; email help@firecrawl.com if you have issues.
### 
[​](https://docs.firecrawl.dev/features/extract#example-usage)
Example Usage
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field
# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key')
class ExtractSchema(BaseModel):
  company_mission: str
  supports_sso: bool
  is_open_source: bool
  is_in_yc: bool
data = app.extract([
 'https://docs.firecrawl.dev/*', 
 'https://firecrawl.dev/', 
 'https://www.ycombinator.com/companies/'
], prompt='Extract the company mission, whether it supports SSO, whether it is open source, and whether it is in Y Combinator from the page.', schema=ExtractSchema.model_json_schema())
print(data)

```

**Key Parameters:**
  * **urls** : An array of one or more URLs. Supports wildcards (`/*`) for broader crawling.
  * **prompt** (Optional unless no schema): A natural language prompt describing the data you want or specifying how you want that data structured.
  * **schema** (Optional unless no prompt): A more rigid structure if you already know the JSON layout.
  * **enableWebSearch** (Optional): When `true`, extraction can follow links outside the specified domain.


See [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/extract) for more details.
### 
[​](https://docs.firecrawl.dev/features/extract#response-sdks)
Response (sdks)
JSON
Copy
```
{
 "success": true,
 "data": {
  "company_mission": "Firecrawl is the easiest way to extract data from the web. Developers use us to reliably convert URLs into LLM-ready markdown or structured data with a single API call.",
  "supports_sso": false,
  "is_open_source": true,
  "is_in_yc": true
 }
}

```

## 
[​](https://docs.firecrawl.dev/features/extract#asynchronous-extraction-%26-status-checking)
Asynchronous Extraction & Status Checking
When you submit an extraction job—either directly via the API or through the SDK’s asynchronous methods—you’ll receive a Job ID. You can use this ID to:
  * Check Job Status: Send a request to the /extract/ endpoint to see if the job is still running or has finished.
  * Automatically Poll (Default SDK Behavior): If you use the default extract method (Python/Node), the SDK automatically polls this endpoint for you and returns the final results once the job completes.
  * Manually Poll (Async SDK Methods): If you use the asynchronous methods—async_extract (Python) or asyncExtract (Node)—the SDK immediately returns a Job ID that you can track. Use get_extract_status (Python) or getExtractStatus (Node) to check the job’s progress on your own schedule.


This endpoint only works for jobs in progress or recently completed (within 24 hours).
Below are code examples for checking an extraction job’s status using Python, Node.js, and cURL:
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
app = FirecrawlApp(
  api_key="fc-YOUR_API_KEY"
)
# Start an extraction job first
extract_job = app.async_extract([
  'https://docs.firecrawl.dev/*', 
  'https://firecrawl.dev/'
], prompt="Extract the company mission and features from these pages.")
# Get the status of the extraction job
job_status = app.get_extract_status(extract_job.id)
print(job_status)
# Example output:
# id=None
# status='completed'
# expiresAt=datetime.datetime(...)
# success=True
# data=[{ ... }]
# error=None
# warning=None
# sources=None

```

### 
[​](https://docs.firecrawl.dev/features/extract#possible-states)
Possible States
  * **completed** : The extraction finished successfully.
  * **processing** : Firecrawl is still processing your request.
  * **failed** : An error occurred; data was not fully extracted.
  * **cancelled** : The job was cancelled by the user.


#### 
[​](https://docs.firecrawl.dev/features/extract#pending-example)
Pending Example
JSON
Copy
```
{
 "success": true,
 "data": [],
 "status": "processing",
 "expiresAt": "2025-01-08T20:58:12.000Z"
}

```

#### 
[​](https://docs.firecrawl.dev/features/extract#completed-example)
Completed Example
JSON
Copy
```
{
 "success": true,
 "data": {
   "company_mission": "Firecrawl is the easiest way to extract data from the web. Developers use us to reliably convert URLs into LLM-ready markdown or structured data with a single API call.",
   "supports_sso": false,
   "is_open_source": true,
   "is_in_yc": true
  },
 "status": "completed",
 "expiresAt": "2025-01-08T20:58:12.000Z"
}

```

## 
[​](https://docs.firecrawl.dev/features/extract#extracting-without-a-schema)
Extracting without a Schema
If you prefer not to define a strict structure, you can simply provide a `prompt`. The underlying model will choose a structure for you, which can be useful for more exploratory or flexible requests.
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key')
data = app.extract([
 'https://docs.firecrawl.dev/',
 'https://firecrawl.dev/'
], prompt="Extract Firecrawl's mission from the page.")
print(data)

```

JSON
Copy
```
{
 "success": true,
 "data": {
  "company_mission": "Turn websites into LLM-ready data. Power your AI apps with clean data crawled from any website."
 }
}

```

## 
[​](https://docs.firecrawl.dev/features/extract#improving-results-with-web-search)
Improving Results with Web Search
Setting `enableWebSearch = true` in your request will expand the crawl beyond the provided URL set. This can capture supporting or related information from linked pages.
Here’s an example that extracts information about dash cams, enriching the results with data from related pages:
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key')
data = app.extract([
'https://nextbase.com/dash-cams/622gw-dash-cam'
], prompt="Extract details about the best dash cams including prices, features, pros/cons and reviews.", enable_web_search=True)
print(data)

```

### 
[​](https://docs.firecrawl.dev/features/extract#example-response-with-web-search)
Example Response with Web Search
JSON
Copy
```
{
 "success": true,
 "data": {
  "dash_cams": [
   {
    "name": "Nextbase 622GW",
    "price": "$399.99",
    "features": [
     "4K video recording",
     "Image stabilization",
     "Alexa built-in",
     "What3Words integration"
    ],
    /* Information below enriched with other websites like 
    https://www.techradar.com/best/best-dash-cam found 
    via enableWebSearch parameter */
    "pros": [
     "Excellent video quality",
     "Great night vision",
     "Built-in GPS"
    ],
    "cons": ["Premium price point", "App can be finicky"]
   }
  ],
 }

```

The response includes additional context gathered from related pages, providing more comprehensive and accurate information.
## 
[​](https://docs.firecrawl.dev/features/extract#extracting-without-urls)
Extracting without URLs
The `/extract` endpoint now supports extracting structured data using a prompt without needing specific URLs. This is useful for research or when exact URLs are unknown. Currently in Alpha.
Python
Node
cURL
Copy
```
from pydantic import BaseModel
class ExtractSchema(BaseModel):
  company_mission: str

# Define the prompt for extraction
prompt = 'Extract the company mission from Firecrawl\'s website.'
# Perform the extraction
scrape_result = app.extract(prompt=prompt, schema=ExtractSchema.model_json_schema())
# Check if the extraction was successful
if not scrape_result.success:
  raise Exception(f"Failed to scrape: {scrape_result.error}")
# Print the extracted data
print(scrape_result.data)

```

## 
[​](https://docs.firecrawl.dev/features/extract#known-limitations-beta)
Known Limitations (Beta)
  1. **Large-Scale Site Coverage** Full coverage of massive sites (e.g., “all products on Amazon”) in a single request is not yet supported.
  2. **Complex Logical Queries** Requests like “find every post from 2025” may not reliably return all expected data. More advanced query capabilities are in progress.
  3. **Occasional Inconsistencies** Results might differ across runs, particularly for very large or dynamic sites. Usually it captures core details, but some variation is possible.
  4. **Beta State** Since `/extract` is still in Beta, features and performance will continue to evolve. We welcome bug reports and feedback to help us improve.


## 
[​](https://docs.firecrawl.dev/features/extract#using-fire-1)
Using FIRE-1
FIRE-1 is an AI agent that enhances Firecrawl’s scraping capabilities. It can controls browser actions and navigates complex website structures to enable comprehensive data extraction beyond traditional scraping methods.
You can leverage the FIRE-1 agent with the `/v1/extract` endpoint for complex extraction tasks that require navigation across multiple pages or interaction with elements.
**Example (cURL):**
Copy
```
curl -X POST https://api.firecrawl.dev/v1/extract \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
   "urls": ["https://example-forum.com/topic/123"],
   "prompt": "Extract all user comments from this forum thread.",
   "schema": {
    "type": "object",
    "properties": {
     "comments": {
      "type": "array",
      "items": {
       "type": "object",
       "properties": {
        "author": {"type": "string"},
        "comment_text": {"type": "string"}
       },
       "required": ["author", "comment_text"]
      }
     }
    },
    "required": ["comments"]
   },
   "agent": {
    "model": "FIRE-1"
   }
  }'

```

> FIRE-1 is already live and available under preview.
## 
[​](https://docs.firecrawl.dev/features/extract#billing-and-usage-tracking)
Billing and Usage Tracking
You can check our the pricing for /extract on the [Extract landing page pricing page](https://www.firecrawl.dev/extract#pricing) and monitor usage via the [Extract page on the dashboard](https://www.firecrawl.dev/app/extract).
Have feedback or need help? Email help@firecrawl.com.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/extract.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/extract)
[Search](https://docs.firecrawl.dev/features/search)[FIRE-1](https://docs.firecrawl.dev/agents/fire-1)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Using /extract](https://docs.firecrawl.dev/features/extract#using-%2Fextract)
  * [Example Usage](https://docs.firecrawl.dev/features/extract#example-usage)
  * [Response (sdks)](https://docs.firecrawl.dev/features/extract#response-sdks)
  * [Asynchronous Extraction & Status Checking](https://docs.firecrawl.dev/features/extract#asynchronous-extraction-%26-status-checking)
  * [Possible States](https://docs.firecrawl.dev/features/extract#possible-states)
  * [Pending Example](https://docs.firecrawl.dev/features/extract#pending-example)
  * [Completed Example](https://docs.firecrawl.dev/features/extract#completed-example)
  * [Extracting without a Schema](https://docs.firecrawl.dev/features/extract#extracting-without-a-schema)
  * [Improving Results with Web Search](https://docs.firecrawl.dev/features/extract#improving-results-with-web-search)
  * [Example Response with Web Search](https://docs.firecrawl.dev/features/extract#example-response-with-web-search)
  * [Extracting without URLs](https://docs.firecrawl.dev/features/extract#extracting-without-urls)
  * [Known Limitations (Beta)](https://docs.firecrawl.dev/features/extract#known-limitations-beta)
  * [Using FIRE-1](https://docs.firecrawl.dev/features/extract#using-fire-1)
  * [Billing and Usage Tracking](https://docs.firecrawl.dev/features/extract#billing-and-usage-tracking)


Assistant
Responses are generated using AI and may contain mistakes.

