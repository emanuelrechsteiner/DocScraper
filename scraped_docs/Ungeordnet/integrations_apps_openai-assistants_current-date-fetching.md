---
url: https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching
scraped_at: 2025-05-25T09:00:45.106337
title: How to Get the Current Date for OpenAI Assistants
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
        * [Knowledge Bases](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching)
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
  * Current Date Fetching


On this page
# Current Date Fetching
Runbear provides a date fetching tool that allows your OpenAI Assistants to fetch the current date, enabling responses to queries involving relative dates, such as “Show me the data from the past week.”
## Use Cases[​](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching#use-cases "Direct link to Use Cases")
  * Answer questions that involve relative dates, e.g., “How many visitors did we get in the past week?” ![use case](https://docs.runbear.io/img/date-fetching-usecase.png)
  * Generate reports based on recent data.


⋯ And much more!
## How to Use Current Date Fetching[​](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching#how-to-use-current-date-fetching "Direct link to How to Use Current Date Fetching")
The date fetching tool uses OpenAI Assistant’s [Function Calling](https://platform.openai.com/docs/guides/function-calling) tool.
  1. Open the OpenAI Assistants form.
  2. Click the **“+ Functions”** button next to the **“Functions”** section.

![add-functions](https://docs.runbear.io/img/add-functions-button.png)
  1. Copy and paste this function definition, then adjust the description fields to suit your requirements.


```
{"name":"plugbear_get_current_date","description":"This function returns the current date.","parameters":{"type":"object","properties":{"timezone":{"type":"string","description":"TODO: The timezone to get the current date in. e.g., America/Los_Angeles"}},"required":["timezone"]}}
```

note
Ensure that the function name is **`plugbear_get_current_date`**.
  1. Click the “Save” button to add the function.


Your assistant can now fetch and utilize the current date, enabling it to handle queries involving relative dates and perform tasks such as generating timely reports and answering date-related questions.
[PreviousAPI Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling)[NextZapier AI Actions](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions)
  * [Use Cases](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching#use-cases)
  * [How to Use Current Date Fetching](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching#how-to-use-current-date-fetching)


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

