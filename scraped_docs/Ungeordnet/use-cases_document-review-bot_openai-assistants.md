---
url: https://docs.runbear.io/use-cases/document-review-bot/openai-assistants
scraped_at: 2025-05-25T08:56:07.458556
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
  * OpenAI Assistants


On this page
# Building a Document Review Bot Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
### Creating OpenAI Assistants[​](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#creating-openai-assistants "Direct link to Creating OpenAI Assistants")
  1. Visit the [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the Create button.
  2. Enter a name for your assistant, e.g., `Contract Review Bot`.
  3. Add the following instructions to the Instructions section. You can adjust the instructions for your needs.
> Your role is to review contracts or legal documents for our company. Please read the uploaded document file and answer users' questions based on its content. Your responses should be concise, clear, and directly related to the information in the uploaded file.
  4. Click the Model combobox and select `gpt-4-1106-preview`.
  5. Check the `Retrieval` checkbox. It's not necessary to upload files to the assistant at this point.
  6. Click the Save button to create the assistant.


![OpenAI Assistant Document Review Bot](https://docs.runbear.io/assets/images/openai-assistants-document-review-bot-a15e8ef4f01c06fb182f453eb9947619.png)
## What's Next[​](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistant can now be integrated into communication channels such as Slack by utilizing Runbear. Visit [Integrating OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants) for detailed instructions.
Simply mention `@Runbear` in your connected channel along with document files to engage the OpenAI Assistant. The context of the document will be accessible witin the conversation(i.e. Slack thread).
![Slack Attachment Sample](https://docs.runbear.io/assets/images/slack-attachment-sample-d73769b56bcc4ea17192d150ead17be5.png)
[PreviousBuilding a Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)[NextJira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
  * [Prerequisites](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#step-by-step-guide)
    * [Creating OpenAI Assistants](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#creating-openai-assistants)
  * [What's Next](https://docs.runbear.io/use-cases/document-review-bot/openai-assistants#whats-next)


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

