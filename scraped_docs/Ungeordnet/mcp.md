---
url: https://docs.firecrawl.dev/mcp
scraped_at: 2025-05-25T08:34:49.134761
title: Firecrawl MCP Server
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
Get Started
Firecrawl MCP Server
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


Get Started
# Firecrawl MCP Server
Copy page
Use Firecrawl’s API through the Model Context Protocol
A Model Context Protocol (MCP) server implementation that integrates [Firecrawl](https://github.com/mendableai/firecrawl) for web scraping capabilities. Our MCP server is open-source and available on [GitHub](https://github.com/mendableai/firecrawl-mcp-server).
## 
[​](https://docs.firecrawl.dev/mcp#features)
Features
  * Web scraping, crawling, and discovery
  * Search and content extraction
  * Deep research and batch scraping
  * Cloud and self-hosted support
  * SSE support


## 
[​](https://docs.firecrawl.dev/mcp#installation)
Installation
You can either use our remote hosted URL or run the server locally. Get your API key from [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
### 
[​](https://docs.firecrawl.dev/mcp#remote-hosted-url)
Remote hosted URL
Copy
```
https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/sse

```

### 
[​](https://docs.firecrawl.dev/mcp#running-with-npx)
Running with npx
Copy
```
env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp

```

### 
[​](https://docs.firecrawl.dev/mcp#manual-installation)
Manual Installation
Copy
```
npm install -g firecrawl-mcp

```

> Play around with [our MCP Server on MCP.so’s playground](https://mcp.so/playground?server=firecrawl-mcp-server) or on [Klavis AI](https://www.klavis.ai/mcp-servers).
### 
[​](https://docs.firecrawl.dev/mcp#running-on-cursor)
Running on Cursor
Configuring Cursor 🖥️ Note: Requires Cursor version 0.45.6+ For the most up-to-date configuration instructions, please refer to the official Cursor documentation on configuring MCP servers: [Cursor MCP Server Configuration Guide](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers)
To configure Firecrawl MCP in Cursor **v0.48.6**
  1. Open Cursor Settings
  2. Go to Features > MCP Servers
  3. Click ”+ Add new global MCP server”
  4. Enter the following code: 
Copy
```
{
 "mcpServers": {
  "firecrawl-mcp": {
   "command": "npx",
   "args": ["-y", "firecrawl-mcp"],
   "env": {
    "FIRECRAWL_API_KEY": "YOUR-API-KEY"
   }
  }
 }
}

```



To configure Firecrawl MCP in Cursor **v0.45.6**
  1. Open Cursor Settings
  2. Go to Features > MCP Servers
  3. Click ”+ Add New MCP Server”
  4. Enter the following: 
     * Name: “firecrawl-mcp” (or your preferred name)
     * Type: “command”
     * Command: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`


> If you are using Windows and are running into issues, try `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`
Replace `your-api-key` with your Firecrawl API key. If you don’t have one yet, you can create an account and get it from <https://www.firecrawl.dev/app/api-keys>
After adding, refresh the MCP server list to see the new tools. The Composer Agent will automatically use Firecrawl MCP when appropriate, but you can explicitly request it by describing your web scraping needs. Access the Composer via Command+L (Mac), select “Agent” next to the submit button, and enter your query.
### 
[​](https://docs.firecrawl.dev/mcp#running-on-windsurf)
Running on Windsurf
Add this to your `./codeium/windsurf/model_config.json`:
Copy
```
{
 "mcpServers": {
  "mcp-server-firecrawl": {
   "command": "npx",
   "args": ["-y", "firecrawl-mcp"],
   "env": {
    "FIRECRAWL_API_KEY": "YOUR_API_KEY"
   }
  }
 }
}

```

### 
[​](https://docs.firecrawl.dev/mcp#running-with-sse-mode)
Running with SSE Mode
To run the server using Server-Sent Events (SSE) locally instead of the default stdio transport:
Copy
```
env SSE_LOCAL=true FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp

```

Use the url: <http://localhost:3000/sse> or [https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/sse](https://mcp.firecrawl.dev/%7BFIRECRAWL_API_KEY%7D/sse)
### 
[​](https://docs.firecrawl.dev/mcp#installing-via-smithery-legacy)
Installing via Smithery (Legacy)
To install Firecrawl for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@mendableai/mcp-server-firecrawl):
Copy
```
npx -y @smithery/cli install @mendableai/mcp-server-firecrawl --client claude

```

### 
[​](https://docs.firecrawl.dev/mcp#running-on-vs-code)
Running on VS Code
For one-click installation, click one of the install buttons below…
[![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D) [![Install with NPX in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D&quality=insiders)
For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code. You can do this by pressing `Ctrl + Shift + P` and typing `Preferences: Open User Settings (JSON)`.
Copy
```
{
 "mcp": {
  "inputs": [
   {
    "type": "promptString",
    "id": "apiKey",
    "description": "Firecrawl API Key",
    "password": true
   }
  ],
  "servers": {
   "firecrawl": {
    "command": "npx",
    "args": ["-y", "firecrawl-mcp"],
    "env": {
     "FIRECRAWL_API_KEY": "${input:apiKey}"
    }
   }
  }
 }
}

```

Optionally, you can add it to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others:
Copy
```
{
 "inputs": [
  {
   "type": "promptString",
   "id": "apiKey",
   "description": "Firecrawl API Key",
   "password": true
  }
 ],
 "servers": {
  "firecrawl": {
   "command": "npx",
   "args": ["-y", "firecrawl-mcp"],
   "env": {
    "FIRECRAWL_API_KEY": "${input:apiKey}"
   }
  }
 }
}

```

### 
[​](https://docs.firecrawl.dev/mcp#running-on-claude-desktop)
Running on Claude Desktop
Add this to the Claude config file:
Copy
```
{
 "mcpServers": {
  "firecrawl": {
   "url": "https://mcp.firecrawl.dev/{YOUR_API_KEY}/sse"
  }
 }
}

```

## 
[​](https://docs.firecrawl.dev/mcp#configuration)
Configuration
### 
[​](https://docs.firecrawl.dev/mcp#environment-variables)
Environment Variables
#### 
[​](https://docs.firecrawl.dev/mcp#required-for-cloud-api)
Required for Cloud API
  * `FIRECRAWL_API_KEY`: Your Firecrawl API key 
    * Required when using cloud API (default)
    * Optional when using self-hosted instance with `FIRECRAWL_API_URL`
  * `FIRECRAWL_API_URL` (Optional): Custom API endpoint for self-hosted instances 
    * Example: `https://firecrawl.your-domain.com`
    * If not provided, the cloud API will be used (requires API key)


#### 
[​](https://docs.firecrawl.dev/mcp#optional-configuration)
Optional Configuration
##### Retry Configuration
  * `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Maximum number of retry attempts (default: 3)
  * `FIRECRAWL_RETRY_INITIAL_DELAY`: Initial delay in milliseconds before first retry (default: 1000)
  * `FIRECRAWL_RETRY_MAX_DELAY`: Maximum delay in milliseconds between retries (default: 10000)
  * `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Exponential backoff multiplier (default: 2)


##### Credit Usage Monitoring
  * `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Credit usage warning threshold (default: 1000)
  * `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Credit usage critical threshold (default: 100)


### 
[​](https://docs.firecrawl.dev/mcp#configuration-examples)
Configuration Examples
For cloud API usage with custom retry and credit monitoring:
Copy
```
# Required for cloud API
export FIRECRAWL_API_KEY=your-api-key
# Optional retry configuration
export FIRECRAWL_RETRY_MAX_ATTEMPTS=5    # Increase max retry attempts
export FIRECRAWL_RETRY_INITIAL_DELAY=2000  # Start with 2s delay
export FIRECRAWL_RETRY_MAX_DELAY=30000    # Maximum 30s delay
export FIRECRAWL_RETRY_BACKOFF_FACTOR=3   # More aggressive backoff
# Optional credit monitoring
export FIRECRAWL_CREDIT_WARNING_THRESHOLD=2000  # Warning at 2000 credits
export FIRECRAWL_CREDIT_CRITICAL_THRESHOLD=500  # Critical at 500 credits

```

For self-hosted instance:
Copy
```
# Required for self-hosted
export FIRECRAWL_API_URL=https://firecrawl.your-domain.com
# Optional authentication for self-hosted
export FIRECRAWL_API_KEY=your-api-key # If your instance requires auth
# Custom retry configuration
export FIRECRAWL_RETRY_MAX_ATTEMPTS=10
export FIRECRAWL_RETRY_INITIAL_DELAY=500   # Start with faster retries

```

### 
[​](https://docs.firecrawl.dev/mcp#custom-configuration-with-claude-desktop)
Custom configuration with Claude Desktop
Add this to your `claude_desktop_config.json`:
Copy
```
{
 "mcpServers": {
  "mcp-server-firecrawl": {
   "command": "npx",
   "args": ["-y", "firecrawl-mcp"],
   "env": {
    "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE",
    "FIRECRAWL_RETRY_MAX_ATTEMPTS": "5",
    "FIRECRAWL_RETRY_INITIAL_DELAY": "2000",
    "FIRECRAWL_RETRY_MAX_DELAY": "30000",
    "FIRECRAWL_RETRY_BACKOFF_FACTOR": "3",
    "FIRECRAWL_CREDIT_WARNING_THRESHOLD": "2000",
    "FIRECRAWL_CREDIT_CRITICAL_THRESHOLD": "500"
   }
  }
 }
}

```

### 
[​](https://docs.firecrawl.dev/mcp#system-configuration)
System Configuration
The server includes several configurable parameters that can be set via environment variables. Here are the default values if not configured:
Copy
```
const CONFIG = {
 retry: {
  maxAttempts: 3, // Number of retry attempts for rate-limited requests
  initialDelay: 1000, // Initial delay before first retry (in milliseconds)
  maxDelay: 10000, // Maximum delay between retries (in milliseconds)
  backoffFactor: 2, // Multiplier for exponential backoff
 },
 credit: {
  warningThreshold: 1000, // Warn when credit usage reaches this level
  criticalThreshold: 100, // Critical alert when credit usage reaches this level
 },
};

```

These configurations control:
  1. **Retry Behavior**
     * Automatically retries failed requests due to rate limits
     * Uses exponential backoff to avoid overwhelming the API
     * Example: With default settings, retries will be attempted at: 
       * 1st retry: 1 second delay
       * 2nd retry: 2 seconds delay
       * 3rd retry: 4 seconds delay (capped at maxDelay)
  2. **Credit Usage Monitoring**
     * Tracks API credit consumption for cloud API usage
     * Provides warnings at specified thresholds
     * Helps prevent unexpected service interruption
     * Example: With default settings: 
       * Warning at 1000 credits remaining
       * Critical alert at 100 credits remaining


### 
[​](https://docs.firecrawl.dev/mcp#rate-limiting-and-batch-processing)
Rate Limiting and Batch Processing
The server utilizes Firecrawl’s built-in rate limiting and batch processing capabilities:
  * Automatic rate limit handling with exponential backoff
  * Efficient parallel processing for batch operations
  * Smart request queuing and throttling
  * Automatic retries for transient errors


## 
[​](https://docs.firecrawl.dev/mcp#available-tools)
Available Tools
### 
[​](https://docs.firecrawl.dev/mcp#1-scrape-tool-firecrawl-scrape)
1. Scrape Tool (`firecrawl_scrape`)
Scrape content from a single URL with advanced options.
Copy
```
{
 "name": "firecrawl_scrape",
 "arguments": {
  "url": "https://example.com",
  "formats": ["markdown"],
  "onlyMainContent": true,
  "waitFor": 1000,
  "timeout": 30000,
  "mobile": false,
  "includeTags": ["article", "main"],
  "excludeTags": ["nav", "footer"],
  "skipTlsVerification": false
 }
}

```

### 
[​](https://docs.firecrawl.dev/mcp#2-batch-scrape-tool-firecrawl-batch-scrape)
2. Batch Scrape Tool (`firecrawl_batch_scrape`)
Scrape multiple URLs efficiently with built-in rate limiting and parallel processing.
Copy
```
{
 "name": "firecrawl_batch_scrape",
 "arguments": {
  "urls": ["https://example1.com", "https://example2.com"],
  "options": {
   "formats": ["markdown"],
   "onlyMainContent": true
  }
 }
}

```

Response includes operation ID for status checking:
Copy
```
{
 "content": [
  {
   "type": "text",
   "text": "Batch operation queued with ID: batch_1. Use firecrawl_check_batch_status to check progress."
  }
 ],
 "isError": false
}

```

### 
[​](https://docs.firecrawl.dev/mcp#3-check-batch-status-firecrawl-check-batch-status)
3. Check Batch Status (`firecrawl_check_batch_status`)
Check the status of a batch operation.
Copy
```
{
 "name": "firecrawl_check_batch_status",
 "arguments": {
  "id": "batch_1"
 }
}

```

### 
[​](https://docs.firecrawl.dev/mcp#4-search-tool-firecrawl-search)
4. Search Tool (`firecrawl_search`)
Search the web and optionally extract content from search results.
Copy
```
{
 "name": "firecrawl_search",
 "arguments": {
  "query": "your search query",
  "limit": 5,
  "lang": "en",
  "country": "us",
  "scrapeOptions": {
   "formats": ["markdown"],
   "onlyMainContent": true
  }
 }
}

```

### 
[​](https://docs.firecrawl.dev/mcp#5-crawl-tool-firecrawl-crawl)
5. Crawl Tool (`firecrawl_crawl`)
Start an asynchronous crawl with advanced options.
Copy
```
{
 "name": "firecrawl_crawl",
 "arguments": {
  "url": "https://example.com",
  "maxDepth": 2,
  "limit": 100,
  "allowExternalLinks": false,
  "deduplicateSimilarURLs": true
 }
}

```

### 
[​](https://docs.firecrawl.dev/mcp#6-extract-tool-firecrawl-extract)
6. Extract Tool (`firecrawl_extract`)
Extract structured information from web pages using LLM capabilities. Supports both cloud AI and self-hosted LLM extraction.
Copy
```
{
 "name": "firecrawl_extract",
 "arguments": {
  "urls": ["https://example.com/page1", "https://example.com/page2"],
  "prompt": "Extract product information including name, price, and description",
  "systemPrompt": "You are a helpful assistant that extracts product information",
  "schema": {
   "type": "object",
   "properties": {
    "name": { "type": "string" },
    "price": { "type": "number" },
    "description": { "type": "string" }
   },
   "required": ["name", "price"]
  },
  "allowExternalLinks": false,
  "enableWebSearch": false,
  "includeSubdomains": false
 }
}

```

Example response:
Copy
```
{
 "content": [
  {
   "type": "text",
   "text": {
    "name": "Example Product",
    "price": 99.99,
    "description": "This is an example product description"
   }
  }
 ],
 "isError": false
}

```

#### 
[​](https://docs.firecrawl.dev/mcp#extract-tool-options%3A)
Extract Tool Options:
  * `urls`: Array of URLs to extract information from
  * `prompt`: Custom prompt for the LLM extraction
  * `systemPrompt`: System prompt to guide the LLM
  * `schema`: JSON schema for structured data extraction
  * `allowExternalLinks`: Allow extraction from external links
  * `enableWebSearch`: Enable web search for additional context
  * `includeSubdomains`: Include subdomains in extraction


When using a self-hosted instance, the extraction will use your configured LLM. For cloud API, it uses Firecrawl’s managed LLM service.
### 
[​](https://docs.firecrawl.dev/mcp#7-deep-research-tool-firecrawl-deep-research)
7. Deep Research Tool (firecrawl_deep_research)
Conduct deep web research on a query using intelligent crawling, search, and LLM analysis.
Copy
```
{
 "name": "firecrawl_deep_research",
 "arguments": {
  "query": "how does carbon capture technology work?",
  "maxDepth": 3,
  "timeLimit": 120,
  "maxUrls": 50
 }
}

```

Arguments:
  * query (string, required): The research question or topic to explore.
  * maxDepth (number, optional): Maximum recursive depth for crawling/search (default: 3).
  * timeLimit (number, optional): Time limit in seconds for the research session (default: 120).
  * maxUrls (number, optional): Maximum number of URLs to analyze (default: 50).


Returns:
  * Final analysis generated by an LLM based on research. (data.finalAnalysis)
  * May also include structured activities and sources used in the research process.


### 
[​](https://docs.firecrawl.dev/mcp#8-generate-llms-txt-tool-firecrawl-generate-llmstxt)
8. Generate LLMs.txt Tool (firecrawl_generate_llmstxt)
Generate a standardized llms.txt (and optionally llms-full.txt) file for a given domain. This file defines how large language models should interact with the site.
Copy
```
{
 "name": "firecrawl_generate_llmstxt",
 "arguments": {
  "url": "https://example.com",
  "maxUrls": 20,
  "showFullText": true
 }
}

```

Arguments:
  * url (string, required): The base URL of the website to analyze.
  * maxUrls (number, optional): Max number of URLs to include (default: 10).
  * showFullText (boolean, optional): Whether to include llms-full.txt contents in the response.


Returns:
  * Generated llms.txt file contents and optionally the llms-full.txt (data.llmstxt and/or data.llmsfulltxt)


## 
[​](https://docs.firecrawl.dev/mcp#logging-system)
Logging System
The server includes comprehensive logging:
  * Operation status and progress
  * Performance metrics
  * Credit usage monitoring
  * Rate limit tracking
  * Error conditions


Example log messages:
Copy
```
[INFO] Firecrawl MCP Server initialized successfully
[INFO] Starting scrape for URL: https://example.com
[INFO] Batch operation queued with ID: batch_1
[WARNING] Credit usage has reached warning threshold
[ERROR] Rate limit exceeded, retrying in 2s...

```

## 
[​](https://docs.firecrawl.dev/mcp#error-handling)
Error Handling
The server provides robust error handling:
  * Automatic retries for transient errors
  * Rate limit handling with backoff
  * Detailed error messages
  * Credit usage warnings
  * Network resilience


Example error response:
Copy
```
{
 "content": [
  {
   "type": "text",
   "text": "Error: Rate limit exceeded. Retrying in 2 seconds..."
  }
 ],
 "isError": true
}

```

## 
[​](https://docs.firecrawl.dev/mcp#development)
Development
Copy
```
# Install dependencies
npm install
# Build
npm run build
# Run tests
npm test

```

### 
[​](https://docs.firecrawl.dev/mcp#contributing)
Contributing
  1. Fork the repository
  2. Create your feature branch
  3. Run tests: `npm test`
  4. Submit a pull request


### 
[​](https://docs.firecrawl.dev/mcp#thanks-to-contributors)
Thanks to contributors
Thanks to [@vrknetha](https://github.com/vrknetha), [@cawstudios](https://caw.tech) for the initial implementation!
Thanks to MCP.so and Klavis AI for hosting and [@gstarwd](https://github.com/gstarwd), [@xiangkaiz](https://github.com/xiangkaiz) and [@zihaolin96](https://github.com/zihaolin96) for integrating our server.
## 
[​](https://docs.firecrawl.dev/mcp#license)
License
MIT License - see LICENSE file for details
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/mcp.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /mcp)
[Quickstart](https://docs.firecrawl.dev/introduction)[Launch Week III (New)](https://docs.firecrawl.dev/launch-week)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Features](https://docs.firecrawl.dev/mcp#features)
  * [Installation](https://docs.firecrawl.dev/mcp#installation)
  * [Remote hosted URL](https://docs.firecrawl.dev/mcp#remote-hosted-url)
  * [Running with npx](https://docs.firecrawl.dev/mcp#running-with-npx)
  * [Manual Installation](https://docs.firecrawl.dev/mcp#manual-installation)
  * [Running on Cursor](https://docs.firecrawl.dev/mcp#running-on-cursor)
  * [Running on Windsurf](https://docs.firecrawl.dev/mcp#running-on-windsurf)
  * [Running with SSE Mode](https://docs.firecrawl.dev/mcp#running-with-sse-mode)
  * [Installing via Smithery (Legacy)](https://docs.firecrawl.dev/mcp#installing-via-smithery-legacy)
  * [Running on VS Code](https://docs.firecrawl.dev/mcp#running-on-vs-code)
  * [Running on Claude Desktop](https://docs.firecrawl.dev/mcp#running-on-claude-desktop)
  * [Configuration](https://docs.firecrawl.dev/mcp#configuration)
  * [Environment Variables](https://docs.firecrawl.dev/mcp#environment-variables)
  * [Required for Cloud API](https://docs.firecrawl.dev/mcp#required-for-cloud-api)
  * [Optional Configuration](https://docs.firecrawl.dev/mcp#optional-configuration)
  * [Configuration Examples](https://docs.firecrawl.dev/mcp#configuration-examples)
  * [Custom configuration with Claude Desktop](https://docs.firecrawl.dev/mcp#custom-configuration-with-claude-desktop)
  * [System Configuration](https://docs.firecrawl.dev/mcp#system-configuration)
  * [Rate Limiting and Batch Processing](https://docs.firecrawl.dev/mcp#rate-limiting-and-batch-processing)
  * [Available Tools](https://docs.firecrawl.dev/mcp#available-tools)
  * [1. Scrape Tool (firecrawl_scrape)](https://docs.firecrawl.dev/mcp#1-scrape-tool-firecrawl-scrape)
  * [2. Batch Scrape Tool (firecrawl_batch_scrape)](https://docs.firecrawl.dev/mcp#2-batch-scrape-tool-firecrawl-batch-scrape)
  * [3. Check Batch Status (firecrawl_check_batch_status)](https://docs.firecrawl.dev/mcp#3-check-batch-status-firecrawl-check-batch-status)
  * [4. Search Tool (firecrawl_search)](https://docs.firecrawl.dev/mcp#4-search-tool-firecrawl-search)
  * [5. Crawl Tool (firecrawl_crawl)](https://docs.firecrawl.dev/mcp#5-crawl-tool-firecrawl-crawl)
  * [6. Extract Tool (firecrawl_extract)](https://docs.firecrawl.dev/mcp#6-extract-tool-firecrawl-extract)
  * [Extract Tool Options:](https://docs.firecrawl.dev/mcp#extract-tool-options%3A)
  * [7. Deep Research Tool (firecrawl_deep_research)](https://docs.firecrawl.dev/mcp#7-deep-research-tool-firecrawl-deep-research)
  * [8. Generate LLMs.txt Tool (firecrawl_generate_llmstxt)](https://docs.firecrawl.dev/mcp#8-generate-llms-txt-tool-firecrawl-generate-llmstxt)
  * [Logging System](https://docs.firecrawl.dev/mcp#logging-system)
  * [Error Handling](https://docs.firecrawl.dev/mcp#error-handling)
  * [Development](https://docs.firecrawl.dev/mcp#development)
  * [Contributing](https://docs.firecrawl.dev/mcp#contributing)
  * [Thanks to contributors](https://docs.firecrawl.dev/mcp#thanks-to-contributors)
  * [License](https://docs.firecrawl.dev/mcp#license)


Assistant
Responses are generated using AI and may contain mistakes.
![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)
![Install with NPX in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)

