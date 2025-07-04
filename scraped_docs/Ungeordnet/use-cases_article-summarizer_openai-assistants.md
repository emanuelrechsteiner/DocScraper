---
url: https://docs.runbear.io/use-cases/article-summarizer/openai-assistants
scraped_at: 2025-05-25T08:58:46.693943
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants)
    * [Customer Service](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
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
  * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
  * OpenAI Assistants


On this page
# Building a Article Summarizer Bot Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
  1. Visit [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the Create button.
  2. Enter a name for your assistant, e.g. `Article Summarizer`.
  3. Add the following instruction to the Instructions section. You can adjust the instruction for your needs.
> Your role is to summarize articles clearly and concisely. Summarize the article into bullet points. Each bullet point should have less than 3 sentences. Use easy words and sentences. The total number of bullet points should generally be around 3-7.
  4. Click the Model combobox and select `gpt-4-1106-preview`.
  5. Click 'Add' button next to the 'Functions' section and paste the JSON below:
note
This JSON defines a function that fetches website content from a URL. Check [Web browsing of OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing) to learn more.
```
{"name":"plugbear_web_search","description":"It fetches the website content","parameters":{"type":"object","properties":{"query":{"type":"string","description":"URL of the article"}},"required":["query"]}}
```

  6. Click the Save button to create the assistant.


## What's Next[​](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistant can be integrated into communication channels such as Slack by utilizing Runbear. Check [Integrating OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants) to learn more.
[PreviousBuilding a Bot for Summarizing Articles](https://docs.runbear.io/use-cases/article-summarizer/)[NextAutomated Knowledge Investigation](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/)
  * [Prerequisites](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants#step-by-step-guide)
  * [What's Next](https://docs.runbear.io/use-cases/article-summarizer/openai-assistants#whats-next)


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

