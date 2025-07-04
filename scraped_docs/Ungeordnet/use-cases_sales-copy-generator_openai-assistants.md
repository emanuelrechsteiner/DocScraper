---
url: https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants
scraped_at: 2025-05-25T08:58:27.007200
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
  * OpenAI Assistants


On this page
# Building Sales Copy Generator Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#prerequisites "Direct link to Prerequisites")
  * **[OpenAI Account](https://platform.openai.com)** : Ensure that the account is subscribed to a paid plan.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
  1. Visit the [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the **Create** button.
  2. Enter a name for your assistant, e.g., `Sales Copy Generator`.
  3. Add the following instructions to the Instructions section. Adjust the instructions for your needs using your business information.
> As a sales manager for AwesomeCRM, the CRM designed for growth, start with a personalized greeting using the recipient's name. If you have the recipient's company name, use the `plugbear_web_search` function to gather information and address their industry-specific challenges, highlighting the urgency of these issues.
> Introduce AwesomeCRM as a custom solution, emphasizing its effectiveness with relevant success stories or testimonials.
> Conclude by proposing a brief, commitment-free meeting to discuss their particular needs and the benefits of AwesomeCRM. Offer convenient meeting times and end with a professional, friendly sign-off. Keep the message clear and concise, under three paragraphs and 100 words, maintaining a professional yet engaging tone.
  4. Click the **Add** button next to the **Functions** section. Copy and paste this function definition, then adjust the description fields to suit your requirements. Check [Web Browsing Tool](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing) for more details.
```
{"name":"plugbear_web_search","description":"Search the company on the web","parameters":{"type":"object","properties":{"query":{"type":"string","description":"The company name of the prospect"}},"required":["query"]}}
```

  5. Click the **Model** combobox and select a model, such as `gpt-4-turbo-preview`. You can compare the models on the [OpenAI Models](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) page.
  6. Click the **Save** button to create the assistant.


## Testing[​](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#testing "Direct link to Testing")
You can test the bot using the OpenAI Playground. Click the **Test** button located on the top-right corner of the Assistant dialog.
## What's Next[​](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistants can be integrated into communication channels, like Slack, by utilizing **Runbear**. Check [Integrating OpenAI Assistants into Channels](https://docs.runbear.io/integrations/apps/openai-assistants) to learn more.
[PreviousSales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)[NextBuilding a Bot for Sentiment Analysis](https://docs.runbear.io/use-cases/sentiment-analyzer/)
  * [Prerequisites](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#step-by-step-guide)
  * [Testing](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#testing)
  * [What's Next](https://docs.runbear.io/use-cases/sales-copy-generator/openai-assistants#whats-next)


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

