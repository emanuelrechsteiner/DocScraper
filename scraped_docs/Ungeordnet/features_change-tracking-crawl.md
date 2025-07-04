---
url: https://docs.firecrawl.dev/features/change-tracking-crawl
scraped_at: 2025-05-25T08:35:46.375020
title: Change Tracking with Crawl | Firecrawl
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
Crawl
Change Tracking with Crawl
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


Crawl
# Change Tracking with Crawl
Copy page
Track changes across your entire website, including new, removed, and hidden pages
Change tracking becomes even more powerful when combined with crawling. While change tracking on individual pages shows you content changes, using it with crawl lets you monitor your entire website structure - showing new pages, removed pages, and pages that have become hidden.
## 
[​](https://docs.firecrawl.dev/features/change-tracking-crawl#basic-usage)
Basic Usage
To enable change tracking during a crawl, include it in the `formats` array of your `scrapeOptions`:
Copy
```
// JavaScript/TypeScript
const app = new FirecrawlApp({ apiKey: 'your-api-key' });
const result = await app.crawl('https://example.com', {
 scrapeOptions: {
  formats: ['markdown', 'changeTracking']
 }
});

```

Copy
```
# Python
app = FirecrawlApp(api_key='your-api-key')
result = app.crawl('https://firecrawl.dev', {
  'scrapeOptions': {
    'formats': ['markdown', 'changeTracking']
  }
})

```

Copy
```
{
 "success": true,
 "status": "completed",
 "completed": 2,
 "total": 2,
 "creditsUsed": 2,
 "expiresAt": "2025-04-14T18:44:13.000Z",
 "data": [
  {
   "markdown": "# Turn websites into LLM-ready data\n\nPower your AI apps with clean data crawled from any website...",
   "metadata": {},
   "changeTracking": {
    "previousScrapeAt": "2025-04-10T12:00:00Z",
    "changeStatus": "changed",
    "visibility": "visible"
   }
  },
  {
   "markdown": "## Flexible Pricing\n\nStart for free, then scale as you grow...",
   "metadata": {},
   "changeTracking": {
    "previousScrapeAt": "2025-04-10T12:00:00Z",
    "changeStatus": "changed",
    "visibility": "visible"
   }
  }
 ]
}

```

## 
[​](https://docs.firecrawl.dev/features/change-tracking-crawl#understanding-change-status)
Understanding Change Status
When using change tracking with crawl, the `changeStatus` field becomes especially valuable:
  * `new`: A page that didn’t exist in your previous crawl
  * `same`: A page that exists and hasn’t changed since your last crawl
  * `changed`: A page that exists but has been modified since your last crawl
  * `removed`: A page that existed in your previous crawl but is no longer found


## 
[​](https://docs.firecrawl.dev/features/change-tracking-crawl#page-visibility)
Page Visibility
The `visibility` field helps you understand how pages are discovered:
  * `visible`: The page is discoverable through links or the sitemap
  * `hidden`: The page still exists but is no longer linked or in the sitemap


This is particularly useful for:
  * Detecting orphaned content
  * Finding pages accidentally removed from navigation
  * Monitoring site structure changes
  * Identifying content that should be re-linked or removed


## 
[​](https://docs.firecrawl.dev/features/change-tracking-crawl#full-diff-support)
Full Diff Support
For detailed change tracking with diffs, you can use the same options as described in the [Change Tracking for Scrape](https://docs.firecrawl.dev/features/change-tracking) documentation.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/change-tracking-crawl.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/change-tracking-crawl)
[JSON mode](https://docs.firecrawl.dev/features/llm-extract)[Webhooks](https://docs.firecrawl.dev/features/webhooks)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Basic Usage](https://docs.firecrawl.dev/features/change-tracking-crawl#basic-usage)
  * [Understanding Change Status](https://docs.firecrawl.dev/features/change-tracking-crawl#understanding-change-status)
  * [Page Visibility](https://docs.firecrawl.dev/features/change-tracking-crawl#page-visibility)
  * [Full Diff Support](https://docs.firecrawl.dev/features/change-tracking-crawl#full-diff-support)


Assistant
Responses are generated using AI and may contain mistakes.

