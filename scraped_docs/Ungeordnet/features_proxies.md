---
url: https://docs.firecrawl.dev/features/proxies
scraped_at: 2025-05-25T08:58:01.279229
title: Proxies | Firecrawl
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
Proxies
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
# Proxies
Copy page
Learn about proxy types, locations, and how Firecrawl selects proxies for your requests.
Firecrawl provides different proxy types to help you scrape websites with varying levels of anti-bot protection. The proxy type can be specified using the `proxy` parameter.
> By default, Firecrawl routes all requests through proxies to help ensure reliability and access, even if you do not specify a proxy type or location.
## 
[​](https://docs.firecrawl.dev/features/proxies#location-based-proxy-selection)
Location-Based Proxy Selection
Firecrawl automatically selects the best proxy based on your specified or detected location. This helps optimize scraping performance and reliability. However, not all locations are currently supported. The following locations are available:
Country Code| Country Name| Stealth Mode Support  
---|---|---  
AE| United Arab Emirates| No  
AU| Australia| No  
BR| Brazil| Yes  
CN| China| No  
DE| Germany| No  
GB| United Kingdom| No  
JP| Japan| No  
QA| Qatar| No  
TR| Turkey| No  
US| United States| Yes  
VN| Vietnam| No  
The list of supported proxy locations was last updated on May 15, 2025. Availability may change over time.
If you need proxies in a location not listed above, please contact us and let us know your requirements.
If you do not specify a proxy or location, Firecrawl will automatically select the best option based on the target site and your request.
## 
[​](https://docs.firecrawl.dev/features/proxies#how-to-specify-proxy-location)
How to Specify Proxy Location
You can request a specific proxy location by setting the `location.country` parameter in your request. For example, to use a Brazilian proxy, set `location.country` to `BR`.
For full details, see the [API reference for `location.country`](http://localhost:3001/api-reference/endpoint/scrape#body-location-country).
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
# Scrape a website:
scrape_result = app.scrape_url('airbnb.com', 
  formats=['markdown', 'html'], 
  location={
    'country': 'BR',
    'languages': ['pt-BR']
  }
)
print(scrape_result)

```

If you request a country where a proxy is not available, Firecrawl will use the closest available region (EU or US) and set the browser location to your requested country.
## 
[​](https://docs.firecrawl.dev/features/proxies#proxy-types)
Proxy Types
Firecrawl supports two types of proxies:
  * **basic** : Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
  * **stealth** : Stealth proxies for scraping sites with advanced anti-bot solutions, or for sites that block regular proxies. Slower, but more reliable on certain sites. [Learn more about Stealth Mode →](https://docs.firecrawl.dev/features/stealth-mode)


> **Note:** For detailed information on using stealth proxies, including credit costs and retry strategies, see the [Stealth Mode documentation](https://docs.firecrawl.dev/features/stealth-mode).
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/proxies.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/proxies)
[Stealth Mode](https://docs.firecrawl.dev/features/stealth-mode)[Webhooks](https://docs.firecrawl.dev/features/webhooks)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Location-Based Proxy Selection](https://docs.firecrawl.dev/features/proxies#location-based-proxy-selection)
  * [How to Specify Proxy Location](https://docs.firecrawl.dev/features/proxies#how-to-specify-proxy-location)
  * [Proxy Types](https://docs.firecrawl.dev/features/proxies#proxy-types)


Assistant
Responses are generated using AI and may contain mistakes.

