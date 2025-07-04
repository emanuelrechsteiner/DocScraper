---
url: https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants
scraped_at: 2025-05-25T08:55:25.350974
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
  * OpenAI Assistants


On this page
# Building a Jira Overdue Tracker Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
### 1. On OpenAI Platform[​](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#1-on-openai-platform "Direct link to 1. On OpenAI Platform")
  1. Visit [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the `Create` button.
  2. Enter a name for your assistant, e.g. `Jira Overdue Tracker`.
  3. Add the following instruction to the Instructions section. You can adjust the instruction for your needs.
> As the **Jira Overdue Tracker** , your primary function is to generate concise daily reports for Jira projects. You are equipped to start this process with just a Jira project ID or key, which is all you need to access the relevant details for the current ongoing sprint. Your reports focus solely on listing issues that are not marked as 'done' and have surpassed their due date. You will provide this information in a straightforward manner, including only the project name, sprint name, and key, name, and assignee of each overdue issue. Your communication style is direct and to the point, prioritizing clarity and efficiency by strictly sticking to the essential details and avoiding any extraneous information.
  4. Click the Model combobox and select `gpt-4-turbo-preview`.


### 2. On Runbear[​](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#2-on-runbear "Direct link to 2. On Runbear")
  1. Download the [Jira OpenAPI Spec](https://docs.runbear.io/assets/files/jira-openapi-spec-b66615293070367622dd19af5d9e1922.yaml) and open it in any text editor.
  2. Modify the `servers` section to include your Jira server domain and save the file. ![](https://docs.runbear.io/assets/images/edit-server-c21aed5b2c2563741fee1cfc1aefb655.png)
  3. Follow the [OpenAP Assistants Integration guide](https://docs.runbear.io/integrations/apps/openai-assistants) to create an OpenAPI integration on Runbear. 
     * But before creating the app, follow the [OpenAPI Function Calling guide](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi) and paste the modified Jira OpenAPI Spec file.
     * For `Auth Method`, follow the [Jira API Token guide](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token) to create Jira API Token. Use an online base64 encoder like [this one](https://www.base64encode.org/) to generate the base64 encoded value of `JIRA_USER_EMAIL:API_TOKEN` and paste this value in the generated API key field. ![](https://docs.runbear.io/assets/images/app-addon-948d9fbd4bac3f0c460cc6a0010e5cad.png)


## What's Next[​](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#whats-next "Direct link to What's Next")
Connect the app you added to communication channels. Check [Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection) for more details.
[PreviousJira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)[NextProof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
  * [Prerequisites](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#step-by-step-guide)
    * [1. On OpenAI Platform](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#1-on-openai-platform)
    * [2. On Runbear](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#2-on-runbear)
  * [What's Next](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants#whats-next)


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

