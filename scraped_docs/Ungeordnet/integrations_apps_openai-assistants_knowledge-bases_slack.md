---
url: https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack
scraped_at: 2025-05-25T08:59:59.280196
title: Sync Slack Channels as a Knowledge Base | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
        * [Knowledge Bases](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack)
          * [Google Drive](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive)
          * [Confluence](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence)
          * [Slack](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack)
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
  * Knowledge Bases
  * Slack


On this page
# Sync Slack Channels as a Knowledge Base
Many teams spend countless hours answering the same questions in Slack channels. While documenting these conversations is important, it's time-consuming and often impractical.
Runbear solves this by connecting your OpenAI Assistant to Slack. Your AI can now search through conversation history and automatically answer recurring questions, letting your team focus on what matters.
## How it Works[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack#how-it-works "Direct link to How it Works")
Runbear uses Slack's [Conversations API](https://api.slack.com/methods/conversations.history) to sync messages from your Slack channels. We periodically check for updates in your selected channels and automatically refresh your assistant's knowledge base with the latest information.
note
Looking to create daily recaps or summaries of recent Slack messages? Check out the `Fetch Messages Action` instead, which provides real-time access to messages from the last 30 days.
## Setting Up Slack Sync[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack#setting-up-slack-sync "Direct link to Setting Up Slack Sync")
Set up Slack synchronization directly from your assistant's configuration page:
  1. Navigate to your assistant's create/edit page
  2. In the Knowledge Sources section, click `Slack`
![Slack Component](https://docs.runbear.io/img/slack-sync-component.png)Knowledge Sources section
  3. Connect your Slack workspace and select channels to sync
![Slack Sync Connect](https://docs.runbear.io/img/slack-sync-sheet.png)Slack workspace connection and channel selection
note
Connect only the channels that are essential for your Assistant to answer questions. This will improve the accuracy and relevance of its responses.
  4. Click Confirm to save your sync configuration
  5. Click Create/Update to save your assistant


Your assistant will now start syncing with Slack. The initial sync time varies depending on the volume of messages in your selected channels.
[PreviousConfluence](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence)[NextWeb Browsing](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing)
  * [How it Works](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack#how-it-works)
  * [Setting Up Slack Sync](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack#setting-up-slack-sync)


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

