---
url: https://docs.anthropic.com/en/docs/about-claude/model-deprecations
scraped_at: 2025-05-24T19:40:18.120550
title: Model deprecations - Anthropic
---

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)
English
Search...
⌘K
  * [Research](https://www.anthropic.com/research)
  * [News](https://www.anthropic.com/news)
  * [Go to claude.ai](https://claude.ai/)
  * [Go to claude.ai](https://claude.ai/)


Search...
Navigation
Models & pricing
Model deprecations
[Welcome](https://docs.anthropic.com/en/home)[Developer Guide](https://docs.anthropic.com/en/docs/welcome)[API Guide](https://docs.anthropic.com/en/api/overview)[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)[Resources](https://docs.anthropic.com/en/resources/overview)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)
* [Documentation](https://docs.anthropic.com/en/home)
* [Developer Console](https://console.anthropic.com/)
* [Developer Discord](https://www.anthropic.com/discord)
* [Support](https://support.anthropic.com/)
##### First steps
  * [Intro to Claude](https://docs.anthropic.com/en/docs/welcome)
  * [Get started](https://docs.anthropic.com/en/docs/get-started)


##### Models & pricing
  * [Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)
  * [Choosing a model](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model)
  * [Migrating to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4)
  * [Model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)
  * [Pricing](https://docs.anthropic.com/en/docs/about-claude/pricing)


##### Learn about Claude
  * [Building with Claude](https://docs.anthropic.com/en/docs/overview)
  * Use cases
  * [Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)
  * [Glossary](https://docs.anthropic.com/en/docs/about-claude/glossary)
  * Prompt engineering


##### Explore features
  * [Features overview](https://docs.anthropic.com/en/docs/build-with-claude/overview)
  * [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
  * [Extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
  * [Streaming Messages](https://docs.anthropic.com/en/docs/build-with-claude/streaming)
  * [Batch processing](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)
  * [Citations](https://docs.anthropic.com/en/docs/build-with-claude/citations)
  * [Multilingual support](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support)
  * [Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)
  * [Embeddings](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)
  * [Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)
  * [PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support)
  * [Files API (beta)](https://docs.anthropic.com/en/docs/build-with-claude/files)


##### Agent components
  * Tools
  * Model Context Protocol (MCP)
  * [Computer use (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)
  * [Google Sheets add-on](https://docs.anthropic.com/en/docs/agents-and-tools/claude-for-sheets)


##### Test & evaluate
  * [Define success criteria](https://docs.anthropic.com/en/docs/test-and-evaluate/define-success)
  * [Develop test cases](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests)
  * Strengthen guardrails
  * [Using the Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)


##### Legal center
  * [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
  * [Security and compliance](https://trust.anthropic.com/)


Models & pricing
# Model deprecations
As we launch safer and more capable models, we regularly retire older models. Applications relying on Anthropic models may need occasional updates to keep working. Impacted customers will always be notified by email and in our documentation.
This page lists all API deprecations, along with recommended replacements.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#overview)
Overview
Anthropic uses the following terms to describe the lifecycle of our models:
  * **Active** : The model is fully supported and recommended for use.
  * **Legacy** : The model will no longer receive updates and may be deprecated in the future.
  * **Deprecated** : The model is no longer available for new customers but continues to be available for existing users until retirement. We assign a retirement date at this point.
  * **Retired** : The model is no longer available for use. Requests to retired models will fail.


## 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#migrating-to-replacements)
Migrating to replacements
Once a model is deprecated, please migrate all usage to a suitable replacement before the retirement date. Requests to models past the retirement date will fail.
To help measure the performance of replacement models on your tasks, we recommend thorough testing of your applications with the new models well before the retirement date.
For specific instructions on migrating from Claude 3.7 to Claude 4 models, see [Migrating to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4).
## 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#notifications)
Notifications
Anthropic notifies customers with active deployments for models with upcoming retirements. We provide at least 6 months† notice before model retirement for publicly released models.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#auditing-model-usage)
Auditing model usage
To help identify usage of deprecated models, customers can access an audit of their API usage. Follow these steps:
  1. Go to <https://console.anthropic.com/settings/usage>
  2. Click the “Export” button
  3. Review the downloaded CSV to see usage broken down by API key and model


This audit will help you locate any instances where your application is still using deprecated models, allowing you to prioritize updates to newer models before the retirement date.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#model-status)
Model status
All publicly released models are listed below with their status:
API Model Name| Current State| Deprecated| Retired  
---|---|---|---  
`claude-1.0`| Retired| September 4, 2024| November 6, 2024  
`claude-1.1`| Retired| September 4, 2024| November 6, 2024  
`claude-1.2`| Retired| September 4, 2024| November 6, 2024  
`claude-1.3`| Retired| September 4, 2024| November 6, 2024  
`claude-instant-1.0`| Retired| September 4, 2024| November 6, 2024  
`claude-instant-1.1`| Retired| September 4, 2024| November 6, 2024  
`claude-instant-1.2`| Retired| September 4, 2024| November 6, 2024  
`claude-2.0`| Deprecated| January 21, 2025| N/A  
`claude-2.1`| Deprecated| January 21, 2025| N/A  
`claude-3-sonnet-20240229`| Deprecated| January 21, 2025| N/A  
`claude-3-haiku-20240307`| Active| N/A| N/A  
`claude-3-opus-20240229`| Active| N/A| N/A  
`claude-3-5-sonnet-20240620`| Active| N/A| N/A  
`claude-3-5-haiku-20241022`| Active| N/A| N/A  
`claude-3-5-sonnet-20241022`| Active| N/A| N/A  
`claude-3-7-sonnet-20250219`| Active| N/A| N/A  
`claude-sonnet-4-20250514`| Active| N/A| N/A  
`claude-opus-4-20250514`| Active| N/A| N/A  
## 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#deprecation-history)
Deprecation history
All deprecations are listed below, with the most recent announcements at the top.
### 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#2025-01-21%3A-claude-2%2C-claude-2-1%2C-and-claude-sonnet-3-models)
2025-01-21: Claude 2, Claude 2.1, and Claude Sonnet 3 models
On January 21, 2025, we notified developers using Claude 2, Claude 2.1, and Claude Sonnet 3 models of their upcoming retirements.
Retirement Date| Deprecated Model| Recommended Replacement  
---|---|---  
July 21, 2025| `claude-2.0`| `claude-3-5-sonnet-20241022`  
July 21, 2025| `claude-2.1`| `claude-3-5-sonnet-20241022`  
July 21, 2025| `claude-3-sonnet-20240229`| `claude-3-5-sonnet-20241022`  
### 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#2024-09-04%3A-claude-1-and-instant-models)
2024-09-04: Claude 1 and Instant models
On September 4, 2024, we notified developers using Claude 1 and Instant models of their upcoming retirements.
Retirement Date| Deprecated Model| Recommended Replacement  
---|---|---  
November 6, 2024| `claude-1.0`| `claude-3-5-haiku-20241022`  
November 6, 2024| `claude-1.1`| `claude-3-5-haiku-20241022`  
November 6, 2024| `claude-1.2`| `claude-3-5-haiku-20241022`  
November 6, 2024| `claude-1.3`| `claude-3-5-haiku-20241022`  
November 6, 2024| `claude-instant-1.0`| `claude-3-5-haiku-20241022`  
November 6, 2024| `claude-instant-1.1`| `claude-3-5-haiku-20241022`  
November 6, 2024| `claude-instant-1.2`| `claude-3-5-haiku-20241022`  
## 
[​](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#best-practices)
Best practices
  1. Regularly check our documentation for updates on model deprecations.
  2. Test your applications with newer models well before the retirement date of your current model.
  3. Update your code to use the recommended replacement model as soon as possible.
  4. Contact our support team if you need assistance with migration or have any questions.


† The Claude 1 family of models have a 60-day notice period due to their limited usage compared to our newer models.
Was this page helpful?
YesNo
[Migrating to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4)[Pricing](https://docs.anthropic.com/en/docs/about-claude/pricing)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Overview](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#overview)
  * [Migrating to replacements](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#migrating-to-replacements)
  * [Notifications](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#notifications)
  * [Auditing model usage](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#auditing-model-usage)
  * [Model status](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#model-status)
  * [Deprecation history](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#deprecation-history)
  * [2025-01-21: Claude 2, Claude 2.1, and Claude Sonnet 3 models](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#2025-01-21%3A-claude-2%2C-claude-2-1%2C-and-claude-sonnet-3-models)
  * [2024-09-04: Claude 1 and Instant models](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#2024-09-04%3A-claude-1-and-instant-models)
  * [Best practices](https://docs.anthropic.com/en/docs/about-claude/model-deprecations#best-practices)



