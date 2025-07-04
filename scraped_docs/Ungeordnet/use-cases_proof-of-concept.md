---
url: https://docs.runbear.io/use-cases/proof-of-concept/
scraped_at: 2025-05-25T08:55:57.484829
title: Proof of Concept for LLM Apps | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/proof-of-concept/#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/proof-of-concept/)
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
  * Proof of Concept for LLM Apps


On this page
# Proof of Concept for LLM Apps
PoC (Proof of Concept) should be done within days, not weeks or months. Meanwhile, testing LLM Apps with real-world users is challenging if the app is not easily accessible. This guide provides a step-by-step guide to building LLM Apps for PoC and comparing results.
## Expectation[​](https://docs.runbear.io/use-cases/proof-of-concept/#expectation "Direct link to Expectation")
This example demonstrates polishing English text using multiple prompts:
  * Slack
  * Microsoft Teams


![](https://docs.runbear.io/assets/images/slack-answer-comparison-f03ae445c16054ffbcc5dbd976bfa21d.png)
![](https://docs.runbear.io/assets/images/teams-answer-comparison-4d3535fa731497850a1872e0119d37cb.png)
## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/proof-of-concept/#step-by-step-guide "Direct link to Step-by-Step Guide")
### 1. Creating new LLM Apps[​](https://docs.runbear.io/use-cases/proof-of-concept/#1-creating-new-llm-apps "Direct link to 1. Creating new LLM Apps")
Create LLM Apps using any tool that works best for you. You can use OpenAI Assistants, GPTs, LangChain, or native Python applications. Visit other use cases to learn more about creating LLM Apps.
### 2. Adding the Apps to Runbear[​](https://docs.runbear.io/use-cases/proof-of-concept/#2-adding-the-apps-to-runbear "Direct link to 2. Adding the Apps to Runbear")
Add the LLM Apps to Runbear with just a few clicks. Visit the [Integrations](https://docs.runbear.io/integrations) page, choose the tool you used, and follow the instructions.
### 3. Connecting the Apps to a single channel[​](https://docs.runbear.io/use-cases/proof-of-concept/#3-connecting-the-apps-to-a-single-channel "Direct link to 3. Connecting the Apps to a single channel")
Using Runbear, connecting the LLM Apps and channels is straightforward. Visit the [Connecting Channels with LLM Apps ](https://docs.runbear.io/get-started/connection) page and follow the guide.
### 4. (Optional) Updating Configs for Comparison[​](https://docs.runbear.io/use-cases/proof-of-concept/#4-optional-updating-configs-for-comparison "Direct link to 4. \(Optional\) Updating Configs for Comparison")
Make sure the **"Description-Based LLM App Selection"** option is **disabled** to receive answers from the LLM Apps rather than receiving an answer from the most relevant one. You can locate this option on the **[Channel Preferences](https://runbear.io/channels)** page.
![](https://docs.runbear.io/assets/images/auto-app-selection-option-f8c9dd8b6dbaf2168bcf3783679949ed.png)
## Testing[​](https://docs.runbear.io/use-cases/proof-of-concept/#testing "Direct link to Testing")
Open the channel (e.g., Slack channel) and start testing the LLM Apps. For example, invoke the LLM Apps by mentioning `@Runbear` with a query.
  * Slack
  * Microsoft Teams


![](https://docs.runbear.io/assets/images/slack-answer-comparison-f03ae445c16054ffbcc5dbd976bfa21d.png)
![](https://docs.runbear.io/assets/images/teams-answer-comparison-4d3535fa731497850a1872e0119d37cb.png)
## All Done! 🎉[​](https://docs.runbear.io/use-cases/proof-of-concept/#all-done-tada "Direct link to all-done-tada")
Introduce your LLM Apps to the real world and start collecting feedback. If you have any questions, please ask us at [Runbear](https://runbear.io).
[PreviousOpenAI Assistants](https://docs.runbear.io/use-cases/jira-overdue-tracker/openai-assistants)[NextBuilding a Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
  * [Expectation](https://docs.runbear.io/use-cases/proof-of-concept/#expectation)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/proof-of-concept/#step-by-step-guide)
    * [1. Creating new LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/#1-creating-new-llm-apps)
    * [2. Adding the Apps to Runbear](https://docs.runbear.io/use-cases/proof-of-concept/#2-adding-the-apps-to-runbear)
    * [3. Connecting the Apps to a single channel](https://docs.runbear.io/use-cases/proof-of-concept/#3-connecting-the-apps-to-a-single-channel)
    * [4. (Optional) Updating Configs for Comparison](https://docs.runbear.io/use-cases/proof-of-concept/#4-optional-updating-configs-for-comparison)
  * [Testing](https://docs.runbear.io/use-cases/proof-of-concept/#testing)
  * [All Done! 🎉](https://docs.runbear.io/use-cases/proof-of-concept/#all-done-tada)


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

