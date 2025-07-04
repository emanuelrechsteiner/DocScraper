---
url: https://docs.firecrawl.dev/features/change-tracking
scraped_at: 2025-05-25T08:35:03.344020
title: Change tracking (New) | Firecrawl
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
Change Tracking
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
# Change Tracking
Copy page
Firecrawl can track changes between the current page and a previous version, and tell you if it updated or not
![Change Tracking](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/launch-week/lw3d12.webp)
Change tracking allows you to monitor and detect changes in web content over time. This feature is available in both the JavaScript and Python SDKs.
## 
[​](https://docs.firecrawl.dev/features/change-tracking#overview)
Overview
Change tracking enables you to:
  * Detect if a webpage has changed since the last scrape
  * View the specific changes between scrapes
  * Get structured data about what has changed
  * Control the visibility of changes


Using the `changeTracking` format, you can monitor changes on a website and receive information about:
  * `previousScrapeAt`: The timestamp of the previous scrape that the current page is being compared against (`null` if no previous scrape)
  * `changeStatus`: The result of the comparison between the two page versions 
    * `new`: This page did not exist or was not discovered before (usually has a `null` `previousScrapeAt`)
    * `same`: This page’s content has not changed since the last scrape
    * `changed`: This page’s content has changed since the last scrape
    * `removed`: This page was removed since the last scrape
  * `visibility`: The visibility of the current page/URL 
    * `visible`: This page is visible, meaning that its URL was discovered through an organic route (through links on other visible pages or the sitemap)
    * `hidden`: This page is not visible, meaning it is still available on the web, but no longer discoverable via the sitemap or crawling the site. We can only identify invisible links if they had been visible, and captured, during a previous crawl or scrape


## 
[​](https://docs.firecrawl.dev/features/change-tracking#javascript-sdk)
JavaScript SDK
### 
[​](https://docs.firecrawl.dev/features/change-tracking#basic-usage)
Basic Usage
To use change tracking in the JavaScript SDK, include `'changeTracking'` in the formats array when scraping a URL:
Copy
```
const app = new FirecrawlApp({ apiKey: 'your-api-key' });
const result = await app.scrapeUrl('https://example.com', {
 formats: ['markdown', 'changeTracking']
});
// Access change tracking data
console.log(result.changeTracking.changeStatus); // 'new', 'same', 'changed', or 'removed'
console.log(result.changeTracking.visibility); // 'visible' or 'hidden'
console.log(result.changeTracking.previousScrapeAt); // ISO timestamp of previous scrape

```

Example Response:
Copy
```
{
 "url": "https://firecrawl.dev",
 "markdown": "# AI Agents for great customer experiences\n\nChatbots that delight your users...",
 "changeTracking": {
  "previousScrapeAt": "2025-04-10T12:00:00Z",
  "changeStatus": "changed",
  "visibility": "visible"
 }
}

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#advanced-options)
Advanced Options
You can configure change tracking with additional options:
Copy
```
const result = await app.scrapeUrl('https://example.com', {
 formats: ['markdown', 'changeTracking'],
 changeTrackingOptions: {
  modes: ['git-diff', 'json'], // Enable specific change tracking modes
  schema: { 
   type: 'object', 
   properties: { 
    title: { type: 'string' },
    content: { type: 'string' }
   } 
  }, // Schema for structured JSON comparison
  prompt: 'Custom prompt for extraction' // Optional custom prompt
 }
});
// Access git-diff format changes
if (result.changeTracking.diff) {
 console.log(result.changeTracking.diff.text); // Git-style diff text
 console.log(result.changeTracking.diff.json); // Structured diff data
}
// Access JSON comparison changes
if (result.changeTracking.json) {
 console.log(result.changeTracking.json.title.previous); // Previous title
 console.log(result.changeTracking.json.title.current); // Current title
}

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#git-diff-results-example%3A)
Git-Diff Results Example:
Copy
```
 **April, 13 2025**
 
-**05:55:05 PM**
+**05:58:57 PM**
...

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#json-comparison-results-example%3A)
JSON Comparison Results Example:
Copy
```
{
 "time": { 
  "previous": "2025-04-13T17:54:32Z", 
  "current": "2025-04-13T17:55:05Z" 
 }
}

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#typescript-interface)
TypeScript Interface
The change tracking feature includes the following TypeScript interfaces:
Copy
```
interface FirecrawlDocument {
 // ... other properties
 changeTracking?: {
  previousScrapeAt: string | null;
  changeStatus: "new" | "same" | "changed" | "removed";
  visibility: "visible" | "hidden";
  diff?: {
   text: string;
   json: {
    files: Array<{
     from: string | null;
     to: string | null;
     chunks: Array<{
      content: string;
      changes: Array<{
       type: string;
       normal?: boolean;
       ln?: number;
       ln1?: number;
       ln2?: number;
       content: string;
      }>;
     }>;
    }>;
   };
  };
  json?: any;
 };
}
interface ScrapeParams {
 // ... other properties
 changeTrackingOptions?: {
  prompt?: string;
  schema?: any;
  modes?: ("json" | "git-diff")[];
 }
}

```

## 
[​](https://docs.firecrawl.dev/features/change-tracking#python-sdk)
Python SDK
### 
[​](https://docs.firecrawl.dev/features/change-tracking#basic-usage-2)
Basic Usage
To use change tracking in the Python SDK, include `'changeTracking'` in the formats list when scraping a URL:
Copy
```
from firecrawl import FirecrawlApp, ChangeTrackingOptions
app = FirecrawlApp(api_key='your-api-key')
result = app.scrape_url('https://example.com',
  formats=['markdown', 'changeTracking']
)
# Access change tracking data
print("Change Status:", result.changeTracking.changeStatus) # 'new', 'same', 'changed', or 'removed'
print("Visibility:", result.changeTracking.visibility) # 'visible' or 'hidden'
print("Previous Scrape At:", result.changeTracking.previousScrapeAt) # ISO timestamp of previous scrape

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#advanced-options-2)
Advanced Options
You can configure change tracking with additional options:
Copy
```
result = app.scrape_url('https://example.com',
  formats=['markdown', 'changeTracking'],
  change_tracking_options=ChangeTrackingOptions(
    modes=['git-diff', 'json'], # Enable specific change tracking modes
    schema={
      'type': 'object',
      'properties': {
        'title': {'type': 'string'},
        'content': {'type': 'string'}
      }
    }, # Schema for structured JSON comparison
    prompt='Custom prompt for extraction' # Optional custom prompt
  )
)
# Access git-diff format changes
if 'diff' in result.changeTracking:
  print(result.changeTracking.diff.text) # Git-style diff text
  print(result.changeTracking.diff.json) # Structured diff data
# Access JSON comparison changes
if 'json' in result.changeTracking:
  print(result.changeTracking.json.title.previous) # Previous title
  print(result.changeTracking.json.title.current) # Current title

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#python-data-model)
Python Data Model
The change tracking feature includes the following Python data model:
Copy
```
class ChangeTrackingData(pydantic.BaseModel):
  """
  Data for the change tracking format.
  """
  previousScrapeAt: Optional[str] = None
  changeStatus: str # "new" | "same" | "changed" | "removed"
  visibility: str # "visible" | "hidden"
  diff: Optional[Dict[str, Any]] = None
  json: Optional[Any] = None

```

## 
[​](https://docs.firecrawl.dev/features/change-tracking#change-tracking-modes)
Change Tracking Modes
The change tracking feature supports two modes:
### 
[​](https://docs.firecrawl.dev/features/change-tracking#git-diff-mode)
Git-Diff Mode
The `git-diff` mode provides a traditional diff format similar to Git’s output. It shows line-by-line changes with additions and deletions marked.
Example output:
Copy
```
@@ -1,1 +1,1 @@
-old content
+new content

```

The structured JSON representation of the diff includes:
  * `files`: Array of changed files (in web context, typically just one)
  * `chunks`: Sections of changes within a file
  * `changes`: Individual line changes with type (add, delete, normal)


### 
[​](https://docs.firecrawl.dev/features/change-tracking#json-mode)
JSON Mode
The `json` mode provides a structured comparison of specific fields extracted from the content. This is useful for tracking changes in specific data points rather than the entire content.
Example output:
Copy
```
{
 "title": {
  "previous": "Old Title",
  "current": "New Title"
 },
 "price": {
  "previous": "$19.99",
  "current": "$24.99"
 }
}

```

To use JSON mode, you need to provide a schema that defines the fields to extract and compare.
## 
[​](https://docs.firecrawl.dev/features/change-tracking#important-facts)
Important Facts
Here are some important details to know when using the change tracking feature:
  * **Comparison Method** : Scrapes are always compared via their markdown response.
    * The `markdown` format must also be specified when using the `changeTracking` format. Other formats may also be specified in addition.
    * The comparison algorithm is resistant to changes in whitespace and content order. iframe source URLs are currently ignored for resistance against captchas and antibots with randomized URLs.
  * **Matching Previous Scrapes** : Previous scrapes to compare against are currently only matched on the source URL, the team ID, and the `markdown` format, and not on any other scrape or crawl options.
    * For an effective comparison, the input URL should be exactly the same as the previous request for the same content.
    * Crawling the same URLs with different `includePaths`/`excludePaths` will have inconsistencies when using `changeTracking`.
    * Scraping the same URLs with different `includeTags`/`excludeTags`/`onlyMainContent` will have inconsistencies when using `changeTracking`.
    * Compared pages will also be compared against previous scrapes that only have the `markdown` format without the `changeTracking` format.
    * Comparisons are scoped to your team. If you scrape a URL for the first time with your API key, its `changeStatus` will always be `new`, even if other Firecrawl users have scraped it before.
  * **Beta Status** : While in Beta, it is recommended to monitor the `warning` field of the resulting document, and to handle the `changeTracking` object potentially missing from the response.
    * This may occur when the database lookup to find the previous scrape to compare against times out.


## 
[​](https://docs.firecrawl.dev/features/change-tracking#examples)
Examples
### 
[​](https://docs.firecrawl.dev/features/change-tracking#basic-scrape-example)
Basic Scrape Example
Copy
```
// Request
{
  "url": "https://firecrawl.dev",
  "formats": ["markdown", "changeTracking"]
}
// Response
{
 "success": true,
 "data": {
  "markdown": "...",
  "metadata": {...},
  "changeTracking": {
   "previousScrapeAt": "2025-03-30T15:07:17.543071+00:00",
   "changeStatus": "same",
   "visibility": "visible"
  }
 }
}

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#crawl-example)
Crawl Example
Copy
```
// Request
{
  "url": "https://firecrawl.dev",
  "scrapeOptions": {
    "formats": ["markdown", "changeTracking"]
  }
}

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#tracking-product-price-changes)
Tracking Product Price Changes
Copy
```
// JavaScript
const result = await app.scrapeUrl('https://example.com/product', {
 formats: ['markdown', 'changeTracking'],
 changeTrackingOptions: {
  modes: ['json'],
  schema: {
   type: 'object',
   properties: {
    price: { type: 'string' },
    availability: { type: 'string' }
   }
  }
 }
});
if (result.changeTracking.changeStatus === 'changed') {
 console.log(`Price changed from ${result.changeTracking.json.price.previous} to ${result.changeTracking.json.price.current}`);
}

```

Copy
```
# Python
result = app.scrape_url('https://example.com/product',
  formats=['markdown', 'changeTracking'],
  changeTrackingOptions={
    'modes': ['json'],
    'schema': {
      'type': 'object',
      'properties': {
        'price': {'type': 'string'},
        'availability': {'type': 'string'}
      }
    }
  }
)
if result.changeTracking.changeStatus == 'changed':
  print(f"Price changed from {result.changeTracking.json.price.previous} to {result.changeTracking.json.price.current}")

```

### 
[​](https://docs.firecrawl.dev/features/change-tracking#monitoring-content-changes-with-git-diff)
Monitoring Content Changes with Git-Diff
Copy
```
// JavaScript
const result = await app.scrapeUrl('https://example.com/blog', {
 formats: ['markdown', 'changeTracking'],
 changeTrackingOptions: {
  modes: ['git-diff']
 }
});
if (result.changeTracking.changeStatus === 'changed') {
 console.log('Content changes:');
 console.log(result.changeTracking.diff.text);
}

```

Copy
```
# Python
result = app.scrape_url('https://example.com/blog',
  formats=['markdown', 'changeTracking'],
  changeTrackingOptions={
    'modes': ['git-diff']
  }
)
if result.changeTracking.changeStatus == 'changed':
  print('Content changes:')
  print(result.changeTracking.diff.text)

```

## 
[​](https://docs.firecrawl.dev/features/change-tracking#billing)
Billing
The change tracking feature is currently in beta. Using the basic change tracking functionality and `git-diff` mode has no additional cost. However, if you use the `json` mode for structured data comparison, the page scrape will cost 5 credits per page.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/change-tracking.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/change-tracking)
[JSON mode](https://docs.firecrawl.dev/features/llm-extract)[Stealth Mode](https://docs.firecrawl.dev/features/stealth-mode)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Overview](https://docs.firecrawl.dev/features/change-tracking#overview)
  * [JavaScript SDK](https://docs.firecrawl.dev/features/change-tracking#javascript-sdk)
  * [Basic Usage](https://docs.firecrawl.dev/features/change-tracking#basic-usage)
  * [Advanced Options](https://docs.firecrawl.dev/features/change-tracking#advanced-options)
  * [Git-Diff Results Example:](https://docs.firecrawl.dev/features/change-tracking#git-diff-results-example%3A)
  * [JSON Comparison Results Example:](https://docs.firecrawl.dev/features/change-tracking#json-comparison-results-example%3A)
  * [TypeScript Interface](https://docs.firecrawl.dev/features/change-tracking#typescript-interface)
  * [Python SDK](https://docs.firecrawl.dev/features/change-tracking#python-sdk)
  * [Basic Usage](https://docs.firecrawl.dev/features/change-tracking#basic-usage-2)
  * [Advanced Options](https://docs.firecrawl.dev/features/change-tracking#advanced-options-2)
  * [Python Data Model](https://docs.firecrawl.dev/features/change-tracking#python-data-model)
  * [Change Tracking Modes](https://docs.firecrawl.dev/features/change-tracking#change-tracking-modes)
  * [Git-Diff Mode](https://docs.firecrawl.dev/features/change-tracking#git-diff-mode)
  * [JSON Mode](https://docs.firecrawl.dev/features/change-tracking#json-mode)
  * [Important Facts](https://docs.firecrawl.dev/features/change-tracking#important-facts)
  * [Examples](https://docs.firecrawl.dev/features/change-tracking#examples)
  * [Basic Scrape Example](https://docs.firecrawl.dev/features/change-tracking#basic-scrape-example)
  * [Crawl Example](https://docs.firecrawl.dev/features/change-tracking#crawl-example)
  * [Tracking Product Price Changes](https://docs.firecrawl.dev/features/change-tracking#tracking-product-price-changes)
  * [Monitoring Content Changes with Git-Diff](https://docs.firecrawl.dev/features/change-tracking#monitoring-content-changes-with-git-diff)
  * [Billing](https://docs.firecrawl.dev/features/change-tracking#billing)


Assistant
Responses are generated using AI and may contain mistakes.
![Change Tracking](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/launch-week/lw3d12.webp)

