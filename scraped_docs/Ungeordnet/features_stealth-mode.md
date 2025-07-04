---
url: https://docs.firecrawl.dev/features/stealth-mode
scraped_at: 2025-05-25T08:35:28.381561
title: Stealth Mode | Firecrawl
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
Scrape
Stealth Mode
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
# Stealth Mode
Copy page
Use stealth proxies for sites with advanced anti-bot solutions
Firecrawl provides different proxy types to help you scrape websites with varying levels of anti-bot protection. The proxy type can be specified using the `proxy` parameter.
### 
[​](https://docs.firecrawl.dev/features/stealth-mode#proxy-types)
Proxy Types
Firecrawl supports two types of proxies:
  * **basic** : Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
  * **stealth** : Stealth proxies for scraping sites with advanced anti-bot solutions. Slower, but more reliable on certain sites.


If you do not specify a proxy, Firecrawl will automatically attempt to determine which one you need based on the target site.
### 
[​](https://docs.firecrawl.dev/features/stealth-mode#using-stealth-mode)
Using Stealth Mode
When scraping websites with advanced anti-bot protection, you can use the stealth proxy mode to improve your success rate.
Python
Node
cURL
Copy
```
# pip install firecrawl-py
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="YOUR_API_KEY")
# Using stealth proxy for sites with advanced anti-bot solutions
content = app.scrape_url("https://example.com", proxy="stealth")
print(content["markdown"])

```

**Note:** Starting May 8th, stealth proxy requests cost 5 credits per request.
## 
[​](https://docs.firecrawl.dev/features/stealth-mode#using-stealth-as-a-retry-mechanism)
Using Stealth as a Retry Mechanism
A common pattern is to first try scraping with the default proxy settings, and then retry with stealth mode if you encounter specific error status codes (401, 403, or 500) in the `metadata.statusCode` field of the response. These status codes can be indicative of the website blocking your request.
Python
Node
cURL
Copy
```
# pip install firecrawl-py
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="YOUR_API_KEY")
# First try with basic proxy
try:
  content = app.scrape_url("https://example.com")
  
  # Check if we got an error status code
  status_code = content.get("metadata", {}).get("statusCode")
  if status_code in [401, 403, 500]:
    print(f"Got status code {status_code}, retrying with stealth proxy")
    # Retry with stealth proxy
    content = app.scrape_url("https://example.com", proxy="stealth")
  
  print(content["markdown"])
except Exception as e:
  print(f"Error: {e}")
  # Retry with stealth proxy on exception
  try:
    content = app.scrape_url("https://example.com", proxy="stealth")
    print(content["markdown"])
  except Exception as e:
    print(f"Stealth proxy also failed: {e}")

```

This approach allows you to optimize your credit usage by only using stealth mode when necessary.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/stealth-mode.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/stealth-mode)
[Change Tracking (New)](https://docs.firecrawl.dev/features/change-tracking)[Proxies](https://docs.firecrawl.dev/features/proxies)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Proxy Types](https://docs.firecrawl.dev/features/stealth-mode#proxy-types)
  * [Using Stealth Mode](https://docs.firecrawl.dev/features/stealth-mode#using-stealth-mode)
  * [Using Stealth as a Retry Mechanism](https://docs.firecrawl.dev/features/stealth-mode#using-stealth-as-a-retry-mechanism)


Assistant
Responses are generated using AI and may contain mistakes.

