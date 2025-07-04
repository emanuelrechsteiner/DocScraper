---
url: https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions
scraped_at: 2025-05-25T08:59:16.451354
title: Zapier AI Actions | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
        * [Knowledge Bases](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions)
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
  * Zapier AI Actions


On this page
# Zapier AI Actions
[Zapier AI Actions](https://actions.zapier.com/) is a tool that allows you to equip AI platforms with the ability to run any Zapier action. The 20,000+ searches and actions available on the Zapier automation platform can be utilized within Runbear.
## Common Use Cases[​](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#common-use-cases "Direct link to Common Use Cases")
Zapier AI actions enable you to automate tasks and integrate various apps and services. With this integration, you can:
  * Automate workflows by triggering actions in other apps, e.g., sending a message in Slack when an event occurs.
  * Connect different services and automate data transfer between them, e.g., adding a new row in Google Sheets when a new contact is added in CRM.
  * Perform complex automation tasks using natural language commands, e.g., “Add this email to my CRM.”


## Setting Up Zapier AI Actions with Runbear[​](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#setting-up-zapier-ai-actions-with-runbear "Direct link to Setting Up Zapier AI Actions with Runbear")
To use Zapier AI actions, you need to set them up as add-ons in Runbear.
### Step 1. Get API Key[​](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#step-1-get-api-key "Direct link to Step 1. Get API Key")
First, configure custom integration app on the [Zapier platform](https://actions.zapier.com/custom/actions/). Once connected, the API key will be available at [Zapier Credentials](https://actions.zapier.com/credentials/). ![Zapier Credentials](https://docs.runbear.io/assets/images/zapier-credentials-5dd4e7444f48d0a87273c1c7a458b8ec.png)
### Step 2. Set Up Allowed Apps[​](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#step-2-set-up-allowed-apps "Direct link to Step 2. Set Up Allowed Apps")
Set up allowed actions [here](https://actions.zapier.com/custom/start) ![Zapier Actions](https://docs.runbear.io/assets/images/zapier-actions-a5f095115bb2e4340e74091494da2001.png)
### Step 3. Set Up Zapier AI Actions as Add-ons in Runbear[​](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#step-3-set-up-zapier-ai-actions-as-add-ons-in-runbear "Direct link to Step 3. Set Up Zapier AI Actions as Add-ons in Runbear")
  1. Navigate to the Runbear [Assistants page](https://runbear.io/assistants) and create a new app.
  2. Select "OpenAPI Assistants" as the app type.
  3. Configure the app as per your requirements.
  4. Expand "Advanced Optiosn" and click "Configure Add-ons".
  5. For authentication, select "API Key" and enter the API key obtained from Zapier. For auth type, select `Custom Header`, and set the auth header to `x-api-key`.
  6. Paste the [OpenAPI specification](https://actions.zapier.com/api/v2/openapi.json) in the provided text area.


![Configure Add-ons](https://docs.runbear.io/assets/images/zapier-configure-addons-3d79c73c018735ff689f4a76113f7423.png)
[PreviousCurrent Date Fetching](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching)[NextLangChain](https://docs.runbear.io/integrations/apps/langchain/)
  * [Common Use Cases](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#common-use-cases)
  * [Setting Up Zapier AI Actions with Runbear](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#setting-up-zapier-ai-actions-with-runbear)
    * [Step 1. Get API Key](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#step-1-get-api-key)
    * [Step 2. Set Up Allowed Apps](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#step-2-set-up-allowed-apps)
    * [Step 3. Set Up Zapier AI Actions as Add-ons in Runbear](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions#step-3-set-up-zapier-ai-actions-as-add-ons-in-runbear)


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

