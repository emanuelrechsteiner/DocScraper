---
url: https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers
scraped_at: 2025-05-24T19:58:18.422214
title: Remote MCP servers - Anthropic
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
Model Context Protocol (MCP)
Remote MCP servers
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
    * [MCP overview](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
    * [MCP connector (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector)
    * [Remote MCP servers](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers)
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


Model Context Protocol (MCP)
# Remote MCP servers
Several companies have deployed remote MCP servers that developers can connect to via the Anthropic MCP connector API. These servers expand the capabilities available to developers and end users by providing remote access to various services and tools through the MCP protocol.
The remote MCP servers listed below are third-party services designed to work with the Anthropic API. These servers are not owned, operated, or endorsed by Anthropic. Users should only connect to remote MCP servers they trust and should review each server’s security practices and terms before connecting.
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers#connecting-to-remote-mcp-servers)
Connecting to remote MCP servers
To connect to a remote MCP server:
  1. Review the documentation for the specific server you want to use.
  2. Ensure you have the necessary authentication credentials.
  3. Follow the server-specific connection instructions provided by each company.


For more information about using remote MCP servers with the Anthropic API, see the [MCP connector docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector).
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers#remote-mcp-server-examples)
Remote MCP server examples
**Company**| **Description**| **Server URL**  
---|---|---  
**[Asana](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server)**|  Interact with your Asana workspace through AI tools to keep projects on track.| `https://mcp.asana.com/sse`  
**[Atlassian](https://www.atlassian.com/platform/remote-mcp-server)**|  Access Atlassian’s collaboration and productivity tools.| `https://mcp.atlassian.com/v1/sse`  
**[Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare/tree/main)**|  Build applications, analyze traffic, monitor performance, and manage security settings through Cloudflare.| See [`mcp-server-cloudflare` repo](https://github.com/cloudflare/mcp-server-cloudflare/tree/main) for server URLs  
**[Intercom](https://developers.intercom.com/docs/guides/mcp)**|  Access real-time customer conversations, tickets, and user data—from Intercom.| `https://mcp.intercom.com/sse`  
**[invideo](https://invideo.io/ai/mcp)**|  Build video creation capabilities into your applications.| `https://mcp.invideo.io/sse`  
**[Linear](https://linear.app/docs/mcp)**|  Integrate with Linear’s issue tracking and project management system.| `https://mcp.linear.app/sse`  
**[PayPal](https://www.paypal.ai/)**|  Integrate PayPal commerce capabilities.| `https://mcp.paypal.com/sse`  
**[Plaid](https://plaid.com/blog/plaid-mcp-ai-assistant-claude/)**|  Analyze, troubleshoot, and optimize Plaid integrations.| `https://api.dashboard.plaid.com/mcp/sse`  
**[Square](https://developer.squareup.com/docs/mcp)**|  Use an agent to build on Square APIs. Payments, inventory, orders, and more.| `https://mcp.squareup.com/sse`  
**[Workato](https://docs.workato.com/mcp.html)**|  Access any application, workflows or data via Workato, made accessible for AI| MCP servers are programmatically generated.  
**[Zapier](https://zapier.com/mcp)**|  Connect to nearly 8,000 apps through Zapier’s automation platform.| `https://mcp.zapier.com/`  
Was this page helpful?
YesNo
[MCP connector (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector)[Computer use (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Connecting to remote MCP servers](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers#connecting-to-remote-mcp-servers)
  * [Remote MCP server examples](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers#remote-mcp-server-examples)



