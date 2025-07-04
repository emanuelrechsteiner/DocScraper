---
url: https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants
scraped_at: 2025-05-25T09:00:22.373595
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants)
      * [Automated Knowledge Investigation](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/)
        * [OpenAI Assistants](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants)
      * [Response Assistant](https://docs.runbear.io/use-cases/customer-service/response-assistant/)
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
  * Customer Service
  * [Automated Knowledge Investigation](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/)
  * OpenAI Assistants


On this page
# Building a Customer Support Bot Using OpenAI Assistants
## Prerequisites[​](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.
  * Knowledge Base: Create or download knowledge files. For example, you can export [Notion](https://notion.so) documents in markdown format and combine them into one to create a knowledge file.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
  1. Visit [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the Create button.
  2. Enter a name for your assistant, e.g. `Help Mate`.
  3. Add the following instruction to the Instructions section. You can adjust the instruction for your needs.
> You are a bot assisting the CS help desk agent. Your role involves reviewing customer inquiries, finding solutions within the uploaded manual files, and proposing preliminary solutions to the CS agent before they review the inquiries. You must be helpful yet concise, and you should not guess or provide speculative answers to information you are uncertain about. If you cannot be certain, you must respond that you do not know. The only information you can accurately respond with is contained within the manual. The manual is the file uploaded when creating the Assistant, and you must read this file and base your responses solely on the information obtained from it.
  4. Click the Model combobox and select `gpt-4-1106-preview`.
  5. Lastly, Tick the Retrieval checkbox and click the Add button next to the Files label. Upload your knowledge files.


## Testing[​](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#testing "Direct link to Testing")
You can test the bot using the OpenAI Playground. Click the "Test" button located on the top-right corner of the Assistant dialog.
## What's Next[​](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistant can be integrated into communication channels such as Slack by utilizing Runbear. Check [Integrating OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants) to learn more.
[PreviousAutomated Knowledge Investigation](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/)[NextResponse Assistant](https://docs.runbear.io/use-cases/customer-service/response-assistant/)
  * [Prerequisites](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#step-by-step-guide)
  * [Testing](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#testing)
  * [What's Next](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/openai-assistants#whats-next)


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

