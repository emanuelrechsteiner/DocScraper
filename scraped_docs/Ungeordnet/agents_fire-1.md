---
url: https://docs.firecrawl.dev/agents/fire-1
scraped_at: 2025-05-25T08:57:20.627907
title: FIRE-1 AI Agent | Firecrawl
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
FIRE-1 Agent
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
# FIRE-1 Agent
Copy page
AI agent that enables intelligent navigation and interaction with web pages
FIRE-1 is an AI agent that enhances Firecrawl’s scraping capabilities. It can controls browser actions and navigates complex website structures to enable comprehensive data extraction beyond traditional scraping methods.
### 
[​](https://docs.firecrawl.dev/agents/fire-1#what-fire-1-can-do%3A)
What FIRE-1 Can Do:
  * Plan and take actions to uncover data
  * Interact with buttons, links, inputs, and dynamic elements.
  * Get mulitple pages of data that require pagination, multiple steps, etc.


## 
[​](https://docs.firecrawl.dev/agents/fire-1#how-to-enable-fire-1)
How to Enable FIRE-1
Activating FIRE-1 is straightforward. Simply include an `agent` object in your scrape API request:
Copy
```
"agent": {
 "model": "FIRE-1",
 "prompt": "Your detailed navigation instructions here."
}

```

_Note:_ The `prompt` field is required for scrape requests, instructing FIRE-1 precisely how to interact with the webpage. For `/extract` it will use the prompt provided in the `prompt` parameter on the body of the request so you can omit the above `agent.prompt` field.
## 
[​](https://docs.firecrawl.dev/agents/fire-1#example-usage-with-scrape-endpoint)
Example Usage with Scrape Endpoint
Here’s a quick example using FIRE-1 with the scrape endpoint to get the companies on the consumer space from Y Combinator:
Python
Node
curl
Copy
```
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Scrape a website:
scrape_result = app.scrape_url('firecrawl.dev',
 formats=['markdown', 'html'],
 agent={
  'model': 'FIRE-1',
  'prompt': 'Navigate through the product listings by clicking the \'Next Page\' button until disabled. Scrape each page.'
 }
)
print(scrape_result)

```

In this scenario, FIRE-1 intelligently clicks the W22 button, the Consumer space button and scrapes the companies.
## 
[​](https://docs.firecrawl.dev/agents/fire-1#using-fire-1-with-the-extract-endpoint)
Using FIRE-1 with the Extract Endpoint
Similarly, you can leverage the FIRE-1 agent with the `/v1/extract` endpoint for complex extraction tasks that require navigation across multiple pages or interaction with elements.
**Example:**
Python
Node
curl
Copy
```
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Extract data from a website:
extract_result = app.extract(['firecrawl.dev'],
 prompt="Extract all user comments from this forum thread.",
 schema={
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
 agent={
  "model": "FIRE-1"
 }
)
print(extract_result)

```

> FIRE-1 is already live and available under preview.
## 
[​](https://docs.firecrawl.dev/agents/fire-1#billing)
Billing
During this experimental phase:
  * `/scrape`: 150 credits
  * `/extract`: See our [token calculator](https://www.firecrawl.dev/pricing?extract-pricing=true#token-calculator). Around 8x the cost of non-agent extract.


## 
[​](https://docs.firecrawl.dev/agents/fire-1#rate-limits)
Rate limits
  * `/scrape`: 10 requests per minute
  * `/extract`: 10 requests per minute


[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/agents/fire-1.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /agents/fire-1)
[Extract](https://docs.firecrawl.dev/features/extract)[Generate with API](https://docs.firecrawl.dev/features/alpha/llmstxt)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [What FIRE-1 Can Do:](https://docs.firecrawl.dev/agents/fire-1#what-fire-1-can-do%3A)
  * [How to Enable FIRE-1](https://docs.firecrawl.dev/agents/fire-1#how-to-enable-fire-1)
  * [Example Usage with Scrape Endpoint](https://docs.firecrawl.dev/agents/fire-1#example-usage-with-scrape-endpoint)
  * [Using FIRE-1 with the Extract Endpoint](https://docs.firecrawl.dev/agents/fire-1#using-fire-1-with-the-extract-endpoint)
  * [Billing](https://docs.firecrawl.dev/agents/fire-1#billing)
  * [Rate limits](https://docs.firecrawl.dev/agents/fire-1#rate-limits)


Assistant
Responses are generated using AI and may contain mistakes.

