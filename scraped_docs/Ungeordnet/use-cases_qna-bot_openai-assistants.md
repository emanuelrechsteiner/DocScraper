---
url: https://docs.runbear.io/use-cases/qna-bot/openai-assistants
scraped_at: 2025-05-25T08:58:13.932284
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/qna-bot/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
      * Preparing Knowledge Files
        * [Notion](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/qna-bot/openai-assistants)
      * [OpenAI GPTs](https://docs.runbear.io/use-cases/qna-bot/openai-gpts)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
  * OpenAI Assistants


On this page
# Building a Q&A Bot Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
### Prepare Knowledge Files[​](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#prepare-knowledge-files "Direct link to Prepare Knowledge Files")
Create or download knowledge files. For example, you can export [Notion](https://notion.so) documents in markdown format and combine them into one to create a knowledge file.
Follow the [Converting Notion Pages into the OpenAI Knowledge Files](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion) page to make yours.
### Creating OpenAI Assistants[​](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#creating-openai-assistants "Direct link to Creating OpenAI Assistants")
  1. Visit the [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the Create button.
  2. Enter a name for your assistant, e.g., `ACME Onboarding Assistant`.
  3. Add the following instructions to the Instructions section. You can adjust the instructions for your needs.
> You are ACME onboarding assistant bot. Your primary role is to assist the ACME People Team by offering informative responses to inquiries related to new employee onboarding and existing employee questions. Please ensure your responses are based on the information contained in the provided file. If a question arises for which you do not have an answer, it's important to acknowledge — never fabricate responses.
  4. Click the Model combobox and select `gpt-4-1106-preview`.
  5. Tick the `Retrieval` checkbox and click the `Add` button next to the `Files` label. Upload your knowledge files.
  6. Click the Save button to create the assistant.


![OpenAI Assistant Q&amp;A Bot](https://docs.runbear.io/assets/images/openai-assistants-qna-bot-86244938a94008d08d690a646d277cf1.png)
## Testing[​](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#testing "Direct link to Testing")
You can test the bot using the OpenAI Playground. Click the "Test" button on the Assistant dialog's top-right corner.
## What's Next[​](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistant can be integrated into communication channels such as Slack by utilizing Runbear. Check [Integrating OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants) to learn more.
[PreviousNotion](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion)[NextOpenAI GPTs](https://docs.runbear.io/use-cases/qna-bot/openai-gpts)
  * [Prerequisites](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#step-by-step-guide)
    * [Prepare Knowledge Files](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#prepare-knowledge-files)
    * [Creating OpenAI Assistants](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#creating-openai-assistants)
  * [Testing](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#testing)
  * [What's Next](https://docs.runbear.io/use-cases/qna-bot/openai-assistants#whats-next)


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

