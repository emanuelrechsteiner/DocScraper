---
url: https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing
scraped_at: 2025-05-25T08:58:30.313978
title: Web Browsing | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
        * [Knowledge Bases](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing)
        * [Web Browsing](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing)
        * [OpenAPI Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi)
        * [API Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling)
        * [Current Date Fetching](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching)
        * [Zapier AI Actions](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions)
      * [LangChain](https://docs.runbear.io/integrations/apps/langchain/)
      * [Python Application](https://docs.runbear.io/integrations/apps/python-sdk/)
      * [Anthropic Claude](https://docs.runbear.io/integrations/apps/anthropic-claude/)
  * [FAQs](https://docs.runbear.io/faq)


  * [](https://docs.runbear.io/)
  * [Integrations](https://docs.runbear.io/integrations)
  * LLM Apps
  * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
  * Web Browsing


On this page
# Web Browsing
Runbear created a web browsing tool that gives your OpenAI Assistants access to a web browser, enabling utilize massive amounts of information.
## Common Use Case[​](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing#common-use-case "Direct link to Common Use Case")
  * Generate content based on web search results, e.g., [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator)
  * Create assistants that answer questions using web search results, e.g., "Who was the president of the US in 2023?"


⋯ And much more!
## How to Use Web Browsing[​](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing#how-to-use-web-browsing "Direct link to How to Use Web Browsing")
The web browsing tool uses OpenAI Assistant's [Function Calling](https://platform.openai.com/docs/guides/function-calling) tool.
  1. Open the OpenAI Assistants form.
  2. Click the **"Add"** button next to the **"Functions"** section.
  3. Copy and paste this function definition, then adjust the description fields to suit your requirements.
```
{"name":"plugbear_web_search","description":"TODO: Describe the purpose of the function. e.g., Search a company","parameters":{"type":"object","properties":{"query":{"type":"string","description":"TODO: Describe the query string you want to inject. e.g., Company name"}},"required":["query"]}}
```

note
Ensure that the function name is **`plugbear_web_search`**.
  4. Click the **"Save"** button to add the function.


All done 🎉
Now, your assistants will utilize web search results when necessary.
[PreviousSlack](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack)[NextOpenAPI Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi)
  * [Common Use Case](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing#common-use-case)
  * [How to Use Web Browsing](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing#how-to-use-web-browsing)


Docs
  * [Docs](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)


Community
  * [Twitter](https://twitter.com/runbear_io)
  * [LinkedIn](https://www.linkedin.com/company/runbear)


More
  * [Runbear](https://runbear.io)
  * [GitHub](https://github.com/runbear-io/plugbear-python-sdk)


Copyright © 2025 Runbear, Inc.

