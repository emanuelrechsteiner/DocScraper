---
url: https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants
scraped_at: 2025-05-25T08:57:41.234495
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants)
      * [LangChain](https://docs.runbear.io/use-cases/proofreading-bot/langchain)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
  * OpenAI Assistants


On this page
# Building a Proofreading Bot Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
  1. Visit [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the Create button.
  2. Enter a name for your assistant, e.g. `Proofreading Bot`.
  3. Add the following instruction to the Instructions section. You can adjust the instruction for your needs.
> You are the Proofreading Bot, an editor bot designed to proofread technical manuals with the precision and style of a professional technical writer. Your primary function is to make the text clear, concise, and professional. You avoid jargon, ambiguous expressions, and emotional language, aiming for straightforward, easy-to-understand, yet professional sentences. You specialize in improving the readability and accuracy of technical manuals, adhering to high standards of technical writing. While maintaining professionalism, your interaction style is helpful, providing guidance and suggestions to enhance the user's text. Answer the revised version of the text only. Do not add any other descriptions.
  4. Click the Model combobox and select `gpt-4-1106-preview`.
  5. Click the Save button to create the assistant.


![OpenAI Assistant Proofreading Bot](https://docs.runbear.io/assets/images/openai-assistant-proofreading-bot-444f7d01c8a7aeb0f6a6f9a2c68fc200.png)
## Testing[​](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#testing "Direct link to Testing")
You can test the bot using the OpenAI Playground. Click the "Test" button located on the top-right corner of the Assistant dialog.
## What's Next[​](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistant can be integrated into communication channels such as Slack by utilizing Runbear. Check [Integrating OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants) to learn more.
[PreviousBuilding a Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)[NextLangChain](https://docs.runbear.io/use-cases/proofreading-bot/langchain)
  * [Prerequisites](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#step-by-step-guide)
  * [Testing](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#testing)
  * [What's Next](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants#whats-next)


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

