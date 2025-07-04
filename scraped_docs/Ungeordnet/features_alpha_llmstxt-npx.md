---
url: https://docs.firecrawl.dev/features/alpha/llmstxt-npx
scraped_at: 2025-05-25T08:35:31.946387
title: LLMs.txt NPX Generator | Firecrawl
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
Generate LLMs.txt with NPX
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
# Generate LLMs.txt with NPX
Copy page
Generate LLMs.txt files from any website in CLI using our NPX package
## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#generate-llmstxt)
generate-llmstxt
A simple NPX package that generates LLMs.txt files in the CLI using the Firecrawl API. This package creates two files in your specified output directory (defaults to ‘public’ folder):
  * `llms.txt`: Contains a summary of the LLM-related content
  * `llms-full.txt`: Contains the full text content


## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#usage)
Usage
You can run this package using NPX without installing it. There are two ways to provide your Firecrawl API key:
### 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#1-using-command-line-arguments)
1. Using Command Line Arguments
Copy
```
npx generate-llmstxt --api-key YOUR_FIRECRAWL_API_KEY

```

### 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#2-using-environment-variables)
2. Using Environment Variables
Create a `.env` file in your project root and add your API key:
Copy
```
FIRECRAWL_API_KEY=your_api_key_here

```

Then run the command without the —api-key option:
Copy
```
npx generate-llmstxt

```

### 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#options)
Options
  * `-k, --api-key <key>` (optional if set in .env): Your Firecrawl API key
  * `-u, --url <url>` (optional): URL to analyze (default: <https://example.com>)
  * `-m, --max-urls <number>` (optional): Maximum number of URLs to analyze (default: 50)
  * `-o, --output-dir <path>` (optional): Output directory path (default: ‘public’)


### 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#examples)
Examples
Copy
```
# Using command line argument with default output directory
npx generate-llmstxt -k your_api_key -u https://your-website.com -m 20
# Using .env file with default output directory
npx generate-llmstxt -u https://your-website.com -m 20
# Specifying a custom output directory
npx generate-llmstxt -k your_api_key -u https://your-website.com -o custom/path/to/output
# Using .env file and custom output directory
npx generate-llmstxt -u https://your-website.com -o content/llms

```

## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#requirements)
Requirements
  * Node.js 14 or higher
  * A valid Firecrawl API key (via command line or .env file)


## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#output)
Output
The package will create two files in your specified output directory (defaults to ‘public’):
  1. `llms.txt`: Contains a summary of the LLM-related content
  2. `llms-full.txt`: Contains the full text content


## 
[​](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#license)
License
MIT
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/alpha/llmstxt-npx.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/alpha/llmstxt-npx)
[Generate with API](https://docs.firecrawl.dev/features/alpha/llmstxt)[Deep Research API](https://docs.firecrawl.dev/features/alpha/deep-research)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [generate-llmstxt](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#generate-llmstxt)
  * [Usage](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#usage)
  * [1. Using Command Line Arguments](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#1-using-command-line-arguments)
  * [2. Using Environment Variables](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#2-using-environment-variables)
  * [Options](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#options)
  * [Examples](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#examples)
  * [Requirements](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#requirements)
  * [Output](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#output)
  * [License](https://docs.firecrawl.dev/features/alpha/llmstxt-npx#license)


Assistant
Responses are generated using AI and may contain mistakes.

