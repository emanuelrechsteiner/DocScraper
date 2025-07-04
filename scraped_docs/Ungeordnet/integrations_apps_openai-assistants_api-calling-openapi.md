---
url: https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi
scraped_at: 2025-05-25T08:58:59.859705
title: OpenAPI Function Calling | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
        * [Knowledge Bases](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi)
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
  * OpenAPI Function Calling


On this page
# OpenAPI Function Calling
Runbear can construct Assistant to consume arbitrary APIs. You can define custom actions add-on by integrating one or more APIs with Runbear, where APIs are defined using the OpenAPI specification. While our previous approach enabled [API Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling) via custom `__api__` field, we have now support utilizing the OpenAPI specification for defining API functions within Runbear. This functionality is similar to [Actions in OpenAI GPTs](https://platform.openai.com/docs/actions).
## Common Use Cases[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#common-use-cases "Direct link to Common Use Cases")
API function calls enable utilizing external services. For example, you can:
  * Create assistants that answer questions by calling external APIs, e.g., `GET https://weatherapi.com/new-york`
  * Convert natural language into API calls, e.g., convert `"Who are my top customers?"` to `GET https://internal.service.com/customers/leaderboard` and call your internal API


⋯ And much more!
## Setting Up Function Calling with OpenAPI[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#setting-up-function-calling-with-openapi "Direct link to Setting Up Function Calling with OpenAPI")
To use OpenAPI function calling, you need to add the OpenAPI specification when you create an LLM app in Runbear. Runbear parses the OpenAPI specification and creates API functions that you can use in your Assistant.
First, navigate to [Assistants](https://runbear.io/assistants) and create a new assistant. Then, select the OpenAPI Assistants as the type. Enter your OpenAI API key and select the assistant you want to use.
![New Assistant](https://docs.runbear.io/assets/images/openapi-new-app-978d03f9214436e4eb3423d13869d4d4.png)
Next, scroll down to find the Add-ons section and click "Configure Add-ons". Enter your OpenAPI specification in the text area If you see list of Add-ons, it means Runbear has successfully parsed the OpenAPI specification.
![Configure Add-ons](https://docs.runbear.io/assets/images/openapi-configure-addons-0da76f96e54284f7e50b24d7d58c09e1.png)
Click "Done" and then "Create" to create the assistant.
### Requirements for OpenAPI Specification[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#requirements-for-openapi-specification "Direct link to Requirements for OpenAPI Specification")
  * OpenAPI 3.0.0 or later.
  * `servers` field in the OpenAPI specification should be defined.


### Authentication[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#authentication "Direct link to Authentication")
If your API requires authentication, you can define the authentication method while you're configuring the Add-ons. Runbear currently supports header-based authentication, including basic auth, bearer tokens, and customizable headers. It also supports placing API credentials in the query string.
[PreviousWeb Browsing](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing)[NextAPI Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling)
  * [Common Use Cases](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#common-use-cases)
  * [Setting Up Function Calling with OpenAPI](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#setting-up-function-calling-with-openapi)
    * [Requirements for OpenAPI Specification](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#requirements-for-openapi-specification)
    * [Authentication](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi#authentication)


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

