---
url: https://docs.anthropic.com/en/docs/about-claude/models
scraped_at: 2025-05-24T19:39:47.943553
title: Models overview - Anthropic
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
Models overview
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
# Models overview
Claude is a family of state-of-the-art large language models developed by Anthropic. This guide introduces our models and compares their performance with legacy models.
Introducing Claude 4, our latest generation of models: **Claude Opus 4** - Our most capable and intelligent model yet. Claude Opus 4 sets new standards in complex reasoning and advanced coding **Claude Sonnet 4** - Our high-performance model with exceptional reasoning and efficiency Learn more in our [blog post](https://www.anthropic.com/news/claude-4).
## [Claude Opus 4Our most powerful and capable model
  * Text and image input
  * Text output
  * 200k context window
  * Superior reasoning capabilities

](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table)## [Claude Sonnet 4High-performance model with exceptional reasoning capabilities
  * Text and image input
  * Text output
  * 200k context window

](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table)
## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-names)
Model names
Model| Anthropic API| AWS Bedrock| GCP Vertex AI  
---|---|---|---  
Claude Opus 4| `claude-opus-4-20250514`| `anthropic.claude-opus-4-20250514-v1:0`| `claude-opus-4@20250514`  
Claude Sonnet 4| `claude-sonnet-4-20250514`| `anthropic.claude-sonnet-4-20250514-v1:0`| `claude-sonnet-4@20250514`  
Claude Sonnet 3.7| `claude-3-7-sonnet-20250219` (`claude-3-7-sonnet-latest`)| `anthropic.claude-3-7-sonnet-20250219-v1:0`| `claude-3-7-sonnet@20250219`  
Claude Haiku 3.5| `claude-3-5-haiku-20241022` (`claude-3-5-haiku-latest`)| `anthropic.claude-3-5-haiku-20241022-v1:0`| `claude-3-5-haiku@20241022`  
Model| Anthropic API| AWS Bedrock| GCP Vertex AI  
---|---|---|---  
Claude Sonnet 3.5 v2| `claude-3-5-sonnet-20241022` (`claude-3-5-sonnet-latest`)| `anthropic.claude-3-5-sonnet-20241022-v2:0`| `claude-3-5-sonnet-v2@20241022`  
Claude Sonnet 3.5| `claude-3-5-sonnet-20240620`| `anthropic.claude-3-5-sonnet-20240620-v1:0`| `claude-3-5-sonnet-v1@20240620`  
Claude Opus 3| `claude-3-opus-20240229` (`claude-3-opus-latest`)| `anthropic.claude-3-opus-20240229-v1:0`| `claude-3-opus@20240229`  
Claude Sonnet 3| `claude-3-sonnet-20240229`| `anthropic.claude-3-sonnet-20240229-v1:0`| `claude-3-sonnet@20240229`  
Claude Haiku 3| `claude-3-haiku-20240307`| `anthropic.claude-3-haiku-20240307-v1:0`| `claude-3-haiku@20240307`  
Models with the same snapshot date (e.g., 20240620) are identical across all platforms and do not change. The snapshot date in the model name ensures consistency and allows developers to rely on stable performance across different environments.
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-aliases)
Model aliases
For convenience during development and testing, we offer aliases for our model ids. These aliases automatically point to the most recent snapshot of a given model. When we release new model snapshots, we migrate aliases to point to the newest version of a model, typically within a week of the new release.
While aliases are useful for experimentation, we recommend using specific model versions (e.g., `claude-sonnet-4-20250514`) in production applications to ensure consistent behavior.
Model| Alias| Model ID  
---|---|---  
Claude Opus 4| `claude-opus-4-0`| `claude-opus-4-20250514`  
Claude Sonnet 4| `claude-sonnet-4-0`| `claude-sonnet-4-20250514`  
Claude Sonnet 3.7| `claude-3-7-sonnet-latest`| `claude-3-7-sonnet-20250219`  
Claude Sonnet 3.5| `claude-3-5-sonnet-latest`| `claude-3-5-sonnet-20241022`  
Claude Haiku 3.5| `claude-3-5-haiku-latest`| `claude-3-5-haiku-20241022`  
Claude Opus 3| `claude-3-opus-latest`| `claude-3-opus-20240229`  
Aliases are subject to the same rate limits and pricing as the underlying model version they reference.
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-comparison-table)
Model comparison table
To help you choose the right model for your needs, we’ve compiled a table comparing the key features and capabilities of each model in the Claude family:
Feature| Claude Opus 4| Claude Sonnet 4| Claude Sonnet 3.7| Claude Sonnet 3.5| Claude Haiku 3.5| Claude Opus 3| Claude Haiku 3  
---|---|---|---|---|---|---|---  
**Description**|  Our most capable model| High-performance model| High-performance model with early extended thinking| Our previous intelligent model| Our fastest model| Powerful model for complex tasks| Fast and compact model for near-instant responsiveness  
**Strengths**|  Highest level of intelligence and capability| High intelligence and balanced performance| High intelligence with toggleable extended thinking| High level of intelligence and capability| Intelligence at blazing speeds| Top-level intelligence, fluency, and understanding| Quick and accurate targeted performance  
**Multilingual**|  Yes| Yes| Yes| Yes| Yes| Yes| Yes  
**Vision**|  Yes| Yes| Yes| Yes| Yes| Yes| Yes  
**[Extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)**|  Yes| Yes| Yes| No| No| No| No  
**[Priority Tier](https://docs.anthropic.com/en/api/service-tiers)**|  Yes| Yes| Yes| Yes| Yes| No| No  
**API model name**| `claude-opus-4-20250514`| `claude-sonnet-4-20250514`| `claude-3-7-sonnet-20250219`| **Upgraded version:** `claude-3-5-sonnet-20241022`**Previous version:** `claude-3-5-sonnet-20240620`| `claude-3-5-haiku-20241022`| `claude-3-opus-20240229`| `claude-3-haiku-20240307`  
**Comparative latency**|  Moderately Fast| Fast| Fast| Fast| Fastest| Moderately fast| Fast  
**Context window**|  200K| 200K| 200K| 200K| 200K| 200K| 200K  
**Max output**|  32000 tokens| 64000 tokens| 64000 tokens| 8192 tokens| 8192 tokens| 4096 tokens| 4096 tokens  
**Training data cut-off**|  Mar 2025| Mar 2025| Nov 20241| Apr 2024| July 2024| Aug 2023| Aug 2023  
_1 - While trained on publicly available information on the internet through November 2024, Claude Sonnet 3.7’s knowledge cut-off date is the end of October 2024. This means the models’ knowledge base is most extensive and reliable on information and events up to October 2024._
Include the beta header `output-128k-2025-02-19` in your API request to increase the maximum output token length to 128k tokens for Claude Sonnet 3.7.
We strongly suggest using our [streaming Messages API](https://docs.anthropic.com/en/api/messages-streaming) to avoid timeouts when generating longer outputs. See our guidance on [long requests](https://docs.anthropic.com/en/api/errors#long-requests) for more details.
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
Model pricing
The table below shows the price per million tokens for each model:
Model| Base Input Tokens| 5m Cache Writes| 1h Cache Writes| Cache Hits & Refreshes| Output Tokens  
---|---|---|---|---|---  
Claude Opus 4| $15 / MTok| $18.75 / MTok| $30 / MTok| $1.50 / MTok| $75 / MTok  
Claude Sonnet 4| $3 / MTok| $3.75 / MTok| $6 / MTok| $0.30 / MTok| $15 / MTok  
Claude Sonnet 3.7| $3 / MTok| $3.75 / MTok| $6 / MTok| $0.30 / MTok| $15 / MTok  
Claude Sonnet 3.5| $3 / MTok| $3.75 / MTok| $6 / MTok| $0.30 / MTok| $15 / MTok  
Claude Haiku 3.5| $0.80 / MTok| $1 / MTok| $1.6 / MTok| $0.08 / MTok| $4 / MTok  
Claude Opus 3| $15 / MTok| $18.75 / MTok| $30 / MTok| $1.50 / MTok| $75 / MTok  
Claude Haiku 3| $0.25 / MTok| $0.30 / MTok| $0.50 / MTok| $0.03 / MTok| $1.25 / MTok  
## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/overview#prompt-and-output-performance)
Prompt and output performance
Claude 4 models excel in:
  * **Performance** : Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the [Claude 4 blog post](http://www.anthropic.com/news/claude-4) for more information.
  * **Engaging responses** : Claude models are ideal for applications that require rich, human-like interactions.
    * If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to our [prompt engineering guides](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) for details.
    * For specific Claude 4 prompting best practices, see our [Claude 4 best practices guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices).
  * **Output quality** : When migrating from previous model generations to Claude 4, you may notice larger improvements in overall performance.


## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/overview#migrating-to-claude-4)
Migrating to Claude 4
In most cases, you can switch from Claude 3.7 models to Claude 4 models with minimal changes:
  1. Update your model name:
     * From: `claude-3-7-sonnet-20250219`
     * To: `claude-sonnet-4-20250514` or `claude-opus-4-20250514`
  2. Your existing API calls will continue to work without modification, although API behavior has changed slightly in Claude 4 models (see [API release notes](https://docs.anthropic.com/en/release-notes/api) for details).


For more details, see [Migrating to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4).
## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/overview#get-started-with-claude)
Get started with Claude
If you’re ready to start exploring what Claude can do for you, let’s dive in! Whether you’re a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, we’ve got you covered.
Looking to chat with Claude? Visit [claude.ai](http://www.claude.ai)!
## [Intro to ClaudeExplore Claude’s capabilities and development flow.](https://docs.anthropic.com/en/docs/intro-to-claude)## [QuickstartLearn how to make your first API call in minutes.](https://docs.anthropic.com/en/docs/quickstart)## [Anthropic ConsoleCraft and test powerful prompts directly in your browser.](https://console.anthropic.com)
If you have any questions or need assistance, don’t hesitate to reach out to our [support team](https://support.anthropic.com/) or consult the [Discord community](https://www.anthropic.com/discord).
Was this page helpful?
YesNo
[Get started](https://docs.anthropic.com/en/docs/get-started)[Choosing a model](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Model names](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-names)
  * [Model aliases](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-aliases)
  * [Model comparison table](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-comparison-table)
  * [Model pricing](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
  * [Prompt and output performance](https://docs.anthropic.com/en/docs/about-claude/models/overview#prompt-and-output-performance)
  * [Migrating to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/overview#migrating-to-claude-4)
  * [Get started with Claude](https://docs.anthropic.com/en/docs/about-claude/models/overview#get-started-with-claude)



