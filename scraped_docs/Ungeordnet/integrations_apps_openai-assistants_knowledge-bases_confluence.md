---
url: https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence
scraped_at: 2025-05-25T09:01:31.820851
title: Sync Confluence Documents | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
        * [Knowledge Bases](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence)
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
  * Confluence


On this page
# Sync Confluence Documents
The Confluence integration for OpenAI Assistants on Runbear allows your assistant to access and synchronize information directly from your Confluence pages. This ensures your assistant is always up-to-date with the latest content from your organization’s knowledge base, without manual updates.
## How it Works[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#how-it-works "Direct link to How it Works")
Runbear leverages the Confluence API to access and synchronize pages from your Confluence account. We periodically check for updates on the pages you’ve selected to sync with your assistant. When changes are detected, we automatically update the assistant’s vector store with the updated information.
### How Often Does Runbear Update My Content[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#how-often-does-runbear-update-my-content "Direct link to How Often Does Runbear Update My Content")
Your Confluence content is automatically kept up-to-date with your OpenAI Assistant:
  * Runbear automatically checks for changes in your Confluence documents every 5 minutes
  * This includes checking for new pages you've added, updates to existing pages, and deleted pages
  * Only content that has changed since the last check will be updated, making the process quick and efficient


### What Happens During Synchronization[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#what-happens-during-synchronization "Direct link to What Happens During Synchronization")
When Runbear syncs your Confluence content:
  * Any new pages you've added to Confluence (and configured in Runbear) will appear in your assistant's knowledge
  * Pages that have been removed from Confluence will no longer be referenced by your assistant
  * Your assistant will use the most up-to-date information from Confluence when responding to questions


## Setting Up Confluence Integration[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#setting-up-confluence-integration "Direct link to Setting Up Confluence Integration")
To access your Confluence pages, Runbear uses OAuth authentication. This provides a secure and seamless connection between Runbear and your Confluence workspace.
### Before You Begin[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#before-you-begin "Direct link to Before You Begin")
Make sure you have:
  * An active Atlassian account with access to your Confluence workspace
  * If you don't have an Atlassian account yet, [create one here](https://id.atlassian.com/signup)
  * If you already have an Atlassian account, make sure you're logged in or have your login credentials ready


### Connecting Your Confluence Workspace[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#connecting-your-confluence-workspace "Direct link to Connecting Your Confluence Workspace")
  1. **Select Confluence as a knowledge source** : In your assistant's edit page, find the "Add Knowledge Sources" section and click on the "Confluence" tile. ![Knowledge Sources Selection](https://docs.runbear.io/assets/images/confluence-knowledge-sources-button-1df480b68771627ce0c029b2a49981e5.png)
  2. **Connect your account** : In the Confluence sheet that appears, click the "Connect Confluence" button. ![Connect Confluence](https://docs.runbear.io/assets/images/confluence-connect-button-38db11afe8b04e86844f2a56e33a9f41.png)
  3. **Authorize Runbear** : You'll be redirected to an Atlassian authorization page. Review the permissions Runbear is requesting and click "Accept" to authorize the connection.
  4. **Return to Runbear** : After successful authorization, you'll be automatically redirected back to Runbear. The setup is now complete, and you'll see your connected Confluence workspace ready for use.


[PreviousGoogle Drive](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive)[NextSlack](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack)
  * [How it Works](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#how-it-works)
    * [How Often Does Runbear Update My Content](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#how-often-does-runbear-update-my-content)
    * [What Happens During Synchronization](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#what-happens-during-synchronization)
  * [Setting Up Confluence Integration](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#setting-up-confluence-integration)
    * [Before You Begin](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#before-you-begin)
    * [Connecting Your Confluence Workspace](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence#connecting-your-confluence-workspace)


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

