---
url: https://docs.firecrawl.dev/features/map
scraped_at: 2025-05-25T08:34:27.526832
title: Map | Firecrawl
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
Standard Features
Map
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


Standard Features
# Map
Copy page
Input a website and get all the urls on the website - extremely fast
## 
[​](https://docs.firecrawl.dev/features/map#introducing-%2Fmap)
Introducing /map
The easiest way to go from a single url to a map of the entire website. This is extremely useful for:
  * When you need to prompt the end-user to choose which links to scrape
  * Need to quickly know the links on a website
  * Need to scrape pages of a website that are related to a specific topic (use the `search` parameter)
  * Only need to scrape specific pages of a website


## 
[​](https://docs.firecrawl.dev/features/map#alpha-considerations)
Alpha Considerations
This endpoint prioritizes speed, so it may not capture all website links. We are working on improvements. Feedback and suggestions are very welcome.
## 
[​](https://docs.firecrawl.dev/features/map#mapping)
Mapping
### 
[​](https://docs.firecrawl.dev/features/map#%2Fmap-endpoint)
/map endpoint
Used to map a URL and get urls of the website. This returns most links present on the website.
### 
[​](https://docs.firecrawl.dev/features/map#installation)
Installation
Python
Node
Go
Rust
Copy
```
pip install firecrawl-py

```

### 
[​](https://docs.firecrawl.dev/features/map#usage)
Usage
Python
Node
Go
Rust
cURL
Copy
```
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Map a website:
map_result = app.map_url('https://firecrawl.dev')
print(map_result)

```

### 
[​](https://docs.firecrawl.dev/features/map#response)
Response
SDKs will return the data object directly. cURL will return the payload exactly as shown below.
Copy
```
{
 "status": "success",
 "links": [
  "https://firecrawl.dev",
  "https://www.firecrawl.dev/pricing",
  "https://www.firecrawl.dev/blog",
  "https://www.firecrawl.dev/playground",
  "https://www.firecrawl.dev/smart-crawl",
  ...
 ]
}

```

#### 
[​](https://docs.firecrawl.dev/features/map#map-with-search)
Map with search
Map with `search` param allows you to search for specific urls inside a website.
cURL
Copy
```
curl -X POST https://api.firecrawl.dev/v1/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
   "url": "https://firecrawl.dev",
   "search": "docs"
  }'

```

Response will be an ordered list from the most relevant to the least relevant.
Copy
```
{
 "status": "success",
 "links": [
  "https://docs.firecrawl.dev",
  "https://docs.firecrawl.dev/sdks/python",
  "https://docs.firecrawl.dev/learn/rag-llama3",
 ]
}

```

[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/map.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/map)
[Webhooks](https://docs.firecrawl.dev/features/webhooks)[Search](https://docs.firecrawl.dev/features/search)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Introducing /map](https://docs.firecrawl.dev/features/map#introducing-%2Fmap)
  * [Alpha Considerations](https://docs.firecrawl.dev/features/map#alpha-considerations)
  * [Mapping](https://docs.firecrawl.dev/features/map#mapping)
  * [/map endpoint](https://docs.firecrawl.dev/features/map#%2Fmap-endpoint)
  * [Installation](https://docs.firecrawl.dev/features/map#installation)
  * [Usage](https://docs.firecrawl.dev/features/map#usage)
  * [Response](https://docs.firecrawl.dev/features/map#response)
  * [Map with search](https://docs.firecrawl.dev/features/map#map-with-search)


Assistant
Responses are generated using AI and may contain mistakes.

