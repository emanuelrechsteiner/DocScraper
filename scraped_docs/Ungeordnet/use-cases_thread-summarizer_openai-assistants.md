---
url: https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants
scraped_at: 2025-05-25T08:56:49.810753
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants)
      * [LangChain](https://docs.runbear.io/use-cases/thread-summarizer/langchain)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)
  * OpenAI Assistants


On this page
# Building a Thread Summarizer Bot Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
  1. Visit [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the Create button.
  2. Enter a name for your assistant, e.g. `Thread Summarizer`.
  3. Add the following instruction to the Instructions section. You can adjust the instruction for your needs.
> Thread Summarizer is adept at summarizing Slack thread conversations, irrespective of the topic, into three concise sentences. It highlights key action items and decisions. The GPT adopts a casual yet professional tone, making its summaries approachable while maintaining accuracy. In situations with ambiguous or incomplete information, Thread Summarizer will use its judgment to provide the best possible summary without seeking additional information. This approach keeps the conversation flowing smoothly and ensures the summaries are focused on the essential points and actionable insights, tailored to the casual, professional nature of Slack interactions.
  4. Click the Model combobox and select `gpt-4-1106-preview`.
  5. Click the Save button to create the assistant.


## Testing[​](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#testing "Direct link to Testing")
You can test the bot using the OpenAI Playground. Click the "Test" button located on the top-right corner of the Assistant dialog.
## What's Next[​](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistant can be integrated into communication channels such as Slack by utilizing Runbear. Check [Integrating OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants) to learn more.
[PreviousBuilding a Bot for Summarizing Threads](https://docs.runbear.io/use-cases/thread-summarizer/)[NextLangChain](https://docs.runbear.io/use-cases/thread-summarizer/langchain)
  * [Prerequisites](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#step-by-step-guide)
  * [Testing](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#testing)
  * [What's Next](https://docs.runbear.io/use-cases/thread-summarizer/openai-assistants#whats-next)


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

