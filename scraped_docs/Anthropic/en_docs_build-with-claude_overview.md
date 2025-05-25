---
url: https://docs.anthropic.com/en/docs/build-with-claude/overview
scraped_at: 2025-05-24T19:37:38.140505
title: Features overview - Anthropic
---

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)
English
Search...
⌘K
  * [Research](https://www.anthropic.com/research)
  * [News](https://www.anthropic.com/news)
  * [Go to claude.ai](https://claude.ai/)
  * [Go to claude.ai](https://claude.ai/)


Search...
Navigation
Explore features
Features overview
[Welcome](https://docs.anthropic.com/en/home)[Developer Guide](https://docs.anthropic.com/en/docs/welcome)[API Guide](https://docs.anthropic.com/en/api/overview)[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)[Resources](https://docs.anthropic.com/en/resources/overview)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)
* [Documentation](https://docs.anthropic.com/en/home)
* [Developer Console](https://console.anthropic.com/)
* [Developer Discord](https://www.anthropic.com/discord)
* [Support](https://support.anthropic.com/)
##### First steps
  * [Intro to Claude](https://docs.anthropic.com/en/docs/welcome)
  * [Get started](https://docs.anthropic.com/en/docs/get-started)


##### Models & pricing
  * [Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)
  * [Choosing a model](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model)
  * [Migrating to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4)
  * [Model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)
  * [Pricing](https://docs.anthropic.com/en/docs/about-claude/pricing)


##### Learn about Claude
  * [Building with Claude](https://docs.anthropic.com/en/docs/overview)
  * Use cases
  * [Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)
  * [Glossary](https://docs.anthropic.com/en/docs/about-claude/glossary)
  * Prompt engineering


##### Explore features
  * [Features overview](https://docs.anthropic.com/en/docs/build-with-claude/overview)
  * [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
  * [Extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
  * [Streaming Messages](https://docs.anthropic.com/en/docs/build-with-claude/streaming)
  * [Batch processing](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)
  * [Citations](https://docs.anthropic.com/en/docs/build-with-claude/citations)
  * [Multilingual support](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support)
  * [Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)
  * [Embeddings](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)
  * [Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)
  * [PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support)
  * [Files API (beta)](https://docs.anthropic.com/en/docs/build-with-claude/files)


##### Agent components
  * Tools
  * Model Context Protocol (MCP)
  * [Computer use (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)
  * [Google Sheets add-on](https://docs.anthropic.com/en/docs/agents-and-tools/claude-for-sheets)


##### Test & evaluate
  * [Define success criteria](https://docs.anthropic.com/en/docs/test-and-evaluate/define-success)
  * [Develop test cases](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests)
  * Strengthen guardrails
  * [Using the Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)


##### Legal center
  * [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
  * [Security and compliance](https://trust.anthropic.com/)


Explore features
# Features overview
Explore Claude’s advanced features and capabilities.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#batch-processing)
Batch processing
Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Each batch is processed in less than 24 hours and costs 50% less than standard API calls. [Learn more](https://docs.anthropic.com/en/api/creating-message-batches).
**Available on:**
  * Anthropic API
  * Amazon Bedrock
  * Google Cloud’s Vertex AI


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#citations)
Citations
Ground Claude’s responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/citations).
**Available on:**
  * Anthropic API
  * Google Cloud’s Vertex AI


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#computer-use-public-beta)
Computer use (public beta)
Computer use is Claude’s ability to perform tasks by interpreting screenshots and automatically generating the necessary computer commands (like mouse movements and keystrokes). [Learn more](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use).
**Available on:**
  * Anthropic API
  * Amazon Bedrock
  * Google Cloud’s Vertex AI


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#pdf-support)
PDF support
Process and analyze text and visual content from PDF documents. [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support).
**Available on:**
  * Anthropic API
  * Google Cloud’s Vertex AI


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#mcp-connector-public-beta)
MCP connector (public beta)
Connect to Model Context Protocol (MCP) servers directly from the Messages API. The Remote MCP connector allows Claude to access external tools and services without requiring you to build an MCP client. [Learn more](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector).
**Available on:**
  * Anthropic API


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#prompt-caching)
Prompt caching
Provide Claude with more background knowledge and example outputs to reduce costs by up to 90% and latency by up to 85% for long prompts. [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching).
**Available on:**
  * Anthropic API
  * Amazon Bedrock
  * Google Cloud’s Vertex AI


### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#1-hour-cache-duration-beta)
1-hour cache duration (beta)
Anthropic offers a 1-hour cache duration for prompt caching.
To use the extended cache, add `extended-cache-ttl-2025-04-11` as a [beta header](https://docs.anthropic.com/en/api/beta-headers) to your request.
**Available on:**
  * Anthropic API


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#token-counting)
Token counting
Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. [Learn more](https://docs.anthropic.com/en/api/messages-count-tokens).
**Available on:**
  * Anthropic API
  * Google Cloud’s Vertex AI


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#tool-use)
Tool use
Enable Claude to interact with external tools and APIs to perform a wider variety of tasks. [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview).
**Available on:**
  * Anthropic API
  * Amazon Bedrock
  * Google Cloud’s Vertex AI


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#web-search)
Web search
Augment Claude’s comprehensive knowledge with current, real-world data from across the web. [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool).
**Available on:**
  * Anthropic API


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#files-api-public-beta)
Files API (public beta)
Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files up to 32 MB per file. [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/files).
**Available on:**
  * Anthropic API


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/overview#code-execution-public-beta)
Code execution (public beta)
Run Python code in a sandboxed environment for advanced data analysis. [Learn more](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool).
**Available on:**
  * Anthropic API


Was this page helpful?
YesNo
[Extended thinking tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips)[Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Batch processing](https://docs.anthropic.com/en/docs/build-with-claude/overview#batch-processing)
  * [Citations](https://docs.anthropic.com/en/docs/build-with-claude/overview#citations)
  * [Computer use (public beta)](https://docs.anthropic.com/en/docs/build-with-claude/overview#computer-use-public-beta)
  * [PDF support](https://docs.anthropic.com/en/docs/build-with-claude/overview#pdf-support)
  * [MCP connector (public beta)](https://docs.anthropic.com/en/docs/build-with-claude/overview#mcp-connector-public-beta)
  * [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/overview#prompt-caching)
  * [1-hour cache duration (beta)](https://docs.anthropic.com/en/docs/build-with-claude/overview#1-hour-cache-duration-beta)
  * [Token counting](https://docs.anthropic.com/en/docs/build-with-claude/overview#token-counting)
  * [Tool use](https://docs.anthropic.com/en/docs/build-with-claude/overview#tool-use)
  * [Web search](https://docs.anthropic.com/en/docs/build-with-claude/overview#web-search)
  * [Files API (public beta)](https://docs.anthropic.com/en/docs/build-with-claude/overview#files-api-public-beta)
  * [Code execution (public beta)](https://docs.anthropic.com/en/docs/build-with-claude/overview#code-execution-public-beta)



