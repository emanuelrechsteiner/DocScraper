---
url: https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants
scraped_at: 2025-05-25T08:59:26.730204
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
  * OpenAI Assistants


On this page
# Building a Sentiment Analyzer Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
  1. Visit [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the `Create` button.
  2. Enter a name for your assistant, e.g. `Sentiment Analyzer`.
  3. Add the following instruction to the Instructions section. You can adjust the instruction for your needs.
> **Sentiment Analyzer** is a sentiment analysis bot designed to analyze user sentiments from inquiries and determine their priorities, extracting up to three main keywords to highlight the primary concerns. When encountering inquiries with a lukewarm sentiment—indicating dissatisfaction or a lack of enthusiasm—it's adept at identifying potential issues, providing clues as keywords. Furthermore, **Sentiment Analyzer** now employs a more nuanced sentiment analysis, moving beyond basic categorization to offer a detailed spectrum of emotional tones. This enables a more precise understanding of user sentiments, ranging from highly positive to highly negative, with nuanced stages in between, ensuring a comprehensive and accurate sentiment and priority assessment in every response. Exclude extraneous information to streamline the assessment process.
> Example of an enhanced response: Keywords: Delay, Communication, Expectations Sentiment: Mildly Dissatisfied Priority: Medium
  4. Click the Model combobox and select `gpt-4-turbo-preview`.


## What's Next[​](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistant can be integrated into communication channels such as Zendesk or HubSpot by utilizing Runbear. Check [Integrating OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants) to learn more.
[PreviousBuilding a Bot for Sentiment Analysis](https://docs.runbear.io/use-cases/sentiment-analyzer/)[NextTeam Deputy](https://docs.runbear.io/use-cases/team-deputy/)
  * [Prerequisites](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants#step-by-step-guide)
  * [What's Next](https://docs.runbear.io/use-cases/sentiment-analyzer/openai-assistants#whats-next)


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

