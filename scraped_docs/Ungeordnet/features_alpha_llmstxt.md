---
url: https://docs.firecrawl.dev/features/alpha/llmstxt
scraped_at: 2025-05-25T08:35:17.512806
title: LLMs.txt Generator | Firecrawl
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
LLMs.txt API
Generate LLMs.txt with an API
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
    * [Generate with API](https://docs.firecrawl.dev/features/alpha/llmstxt)
    * [Generate with NPX](https://docs.firecrawl.dev/features/alpha/llmstxt-npx)
  * Deep Research API


##### Contributing
  * [Open Source vs Cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud)
  * [Running locally](https://docs.firecrawl.dev/contributing/guide)
  * [Self-hosting](https://docs.firecrawl.dev/contributing/self-host)


LLMs.txt API
# Generate LLMs.txt with an API
Copy page
Generate LLMs.txt files from any website for LLM training and analysis
## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#introducing-llms-txt-generator-endpoint-alpha-%F0%9F%93%83)
Introducing LLMs.txt Generator Endpoint (Alpha) 📃
The `/llmstxt` endpoint allows you to transform any website into clean, [LLM-ready text files](https://www.firecrawl.dev/blog/How-to-Create-an-llms-txt-File-for-Any-Website). Simply provide a URL, and Firecrawl will crawl the site and generate both `llms.txt` and `llms-full.txt` files that can be used for training or analysis with any LLM.
## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#how-it-works)
How It Works
The LLMs.txt Generator:
  1. Crawls the provided website URL and its linked pages
  2. Extracts clean, meaningful text content
  3. Generates two formats: 
     * `llms.txt`: Concise summaries and key information
     * `llms-full.txt`: Complete text content with more detail


### 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#example-usage)
Example Usage
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client
firecrawl = FirecrawlApp(api_key="your_api_key")
# Generate LLMs.txt with polling
results = firecrawl.generate_llms_text(
  url="https://example.com",
  max_urls=2,
  show_full_text=True
)
# Access generation results
if results.success:
  print(f"Status: {results.status}")
  print(f"Generated Data: {results.data}")
else:
  print(f"Error: {results.error}")

```

**Key Parameters:**
  * **url** : The website URL to generate LLMs.txt files from
  * **maxUrls** (Optional): Maximum number of pages to crawl (1-100, default: 10)
  * **showFullText** (Optional): Generate llms-full.txt in addition to llms.txt (default: false)


See [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/llmstxt) for more details.
## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#checking-generation-status)
Checking Generation Status
LLMs.txt generation runs asynchronously. Make the aync call and monitor the status with:
Python
Node
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client
firecrawl = FirecrawlApp(api_key="your_api_key")
# Create async job
job = firecrawl.async_generate_llms_text(
  url="https://example.com",
)
if job.success:
  job_id = job.id
# Check LLMs.txt generation status
status = firecrawl.check_generate_llms_text_status("job_id")
# Print current status
print(f"Status: {status.status}")
if status.status == 'completed':
  print("LLMs.txt Content:", status.data.llmstxt)
  if 'llmsfulltxt' in status.data:
    print("Full Text Content:", status.data.llmsfulltxt)
  print(f"Processed URLs: {len(status.data.processed_urls)}")

```

### 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#status-examples)
Status Examples
#### 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#in-progress)
In Progress
Copy
```
{
 "success": true,
 "data": {
  "llmstxt": "# Firecrawl.dev llms.txt\n\n- [Web Data Extraction Tool](https://www.firecrawl.dev/)...",
  "llmsfulltxt": "# Firecrawl.dev llms-full.txt\n\n"
 },
 "status": "processing",
 "expiresAt": "2025-03-03T23:19:18.000Z"
}

```

#### 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#completed)
Completed
Copy
```
{
 "success": true,
 "data": {
  "llmstxt": "# http://firecrawl.dev llms.txt\n\n- [Web Data Extraction Tool](https://www.firecrawl.dev/): Transform websites into clean, LLM-ready data effortlessly.\n- [Flexible Web Scraping Pricing](https://www.firecrawl.dev/pricing): Flexible pricing plans for web scraping and data extraction.\n- [Web Scraping and AI](https://www.firecrawl.dev/blog): Explore tutorials and articles on web scraping and AI...",
  "llmsfulltxt": "# http://firecrawl.dev llms-full.txt\n\n## Web Data Extraction Tool\nIntroducing /extract - Get web data with a prompt [Try now](https://www.firecrawl.dev/extract)\n\n[💥Get 2 months free with yearly plan](https://www.firecrawl.dev/pricing)..."
 },
 "status": "completed",
 "expiresAt": "2025-03-03T22:45:50.000Z"
}

```

## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#known-limitations-alpha)
Known Limitations (Alpha)
  1. **Access Restrictions** Only publicly accessible pages can be processed. Login-protected or paywalled content is not supported.
  2. **Site Size** We are only are allowing processing for up to 5000 URLs during the alpha stage.
  3. **Alpha State** As an Alpha feature, the output format and processing may evolve based on feedback.


## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt#billing-and-usage)
Billing and Usage
Billing is based on the number of URLs processed:
  * Base cost: 1 credit per URL processed
  * Control URL costs with `maxUrls` parameter


Have feedback or need help? Email help@firecrawl.com.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/alpha/llmstxt.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/alpha/llmstxt)
[FIRE-1](https://docs.firecrawl.dev/agents/fire-1)[Generate with NPX](https://docs.firecrawl.dev/features/alpha/llmstxt-npx)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Introducing LLMs.txt Generator Endpoint (Alpha) 📃](https://docs.firecrawl.dev/features/alpha/llmstxt#introducing-llms-txt-generator-endpoint-alpha-%F0%9F%93%83)
  * [How It Works](https://docs.firecrawl.dev/features/alpha/llmstxt#how-it-works)
  * [Example Usage](https://docs.firecrawl.dev/features/alpha/llmstxt#example-usage)
  * [Checking Generation Status](https://docs.firecrawl.dev/features/alpha/llmstxt#checking-generation-status)
  * [Status Examples](https://docs.firecrawl.dev/features/alpha/llmstxt#status-examples)
  * [In Progress](https://docs.firecrawl.dev/features/alpha/llmstxt#in-progress)
  * [Completed](https://docs.firecrawl.dev/features/alpha/llmstxt#completed)
  * [Known Limitations (Alpha)](https://docs.firecrawl.dev/features/alpha/llmstxt#known-limitations-alpha)
  * [Billing and Usage](https://docs.firecrawl.dev/features/alpha/llmstxt#billing-and-usage)


Assistant
Responses are generated using AI and may contain mistakes.

