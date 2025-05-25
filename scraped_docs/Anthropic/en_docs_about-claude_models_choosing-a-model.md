---
url: https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model
scraped_at: 2025-05-24T19:39:07.376105
title: Choosing the right model - Anthropic
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
Choosing the right model
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
# Choosing the right model
Selecting the optimal Claude model for your application involves balancing three key considerations: capabilities, speed, and cost. This guide helps you make an informed decision based on your specific requirements.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#establish-key-criteria)
Establish key criteria
When choosing a Claude model, we recommend first evaluating these factors:
  * **Capabilities:** What specific features or capabilities will you need the model to have in order to meet your needs?
  * **Speed:** How quickly does the model need to respond in your application?
  * **Cost:** What’s your budget for both development and production usage?


Knowing these answers in advance will make narrowing down and deciding which model to use much easier.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#choose-the-best-model-to-start-with)
Choose the best model to start with
There are two general approaches you can use to start testing which Claude model best works for your needs.
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#option-1%3A-start-with-a-fast%2C-cost-effective-model)
Option 1: Start with a fast, cost-effective model
For many applications, starting with a faster, more cost-effective model like Claude 3.5 Haiku can be the optimal approach:
  1. Begin implementation with Claude 3.5 Haiku
  2. Test your use case thoroughly
  3. Evaluate if performance meets your requirements
  4. Upgrade only if necessary for specific capability gaps


This approach allows for quick iteration, lower development costs, and is often sufficient for many common applications. This approach is best for:
  * Initial prototyping and development
  * Applications with tight latency requirements
  * Cost-sensitive implementations
  * High-volume, straightforward tasks


### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#option-2%3A-start-with-the-most-capable-model)
Option 2: Start with the most capable model
For complex tasks where intelligence and advanced capabilities are paramount, you may want to start with the most capable model and then consider optimizing to more efficient models down the line:
  1. Implement with Claude Opus 4 or Claude Sonnet 4
  2. Optimize your prompts for these models
  3. Evaluate if performance meets your requirements
  4. Consider increasing efficiency by downgrading intelligence over time with greater workflow optimization


This approach is best for:
  * Complex reasoning tasks
  * Scientific or mathematical applications
  * Tasks requiring nuanced understanding
  * Applications where accuracy outweighs cost considerations
  * Advanced coding


## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#model-selection-matrix)
Model selection matrix
When you need…| We recommend starting with…| Example use cases  
---|---|---  
Highest intelligence and reasoning, superior capabilities for the most complex tasks, such as multi agent coding| Claude Opus 4| Multi agent frameworks, complex codebase refactoring, nuanced creative writing, complex financial or scientific analysis  
Balance of intelligence and speed, strong performance but with faster response times| Claude Sonnet 4| Complex customer chatbot inquiries, complex code generation, straightforward agentic loops, data analysis  
Fast responses at lower cost, optimized for high volume, straightforward appications with no need for extended thinking| Claude 3.5 Haiku| Basic customer support, high volume formulaic content generation, straightforward data extraction  
## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#decide-whether-to-upgrade-or-change-models)
Decide whether to upgrade or change models
To determine if you need to upgrade or change models, you should:
  1. [Create benchmark tests](https://docs.anthropic.com/en/docs/about-claude/models/en/docs/build-with-claude/develop-tests.mdx) specific to your use case - having a good evaluation set is the most important step in the process
  2. Test with your actual prompts and data
  3. Compare performance across models for: 
     * Accuracy of responses
     * Response quality
     * Handling of edge cases
  4. Weigh performance and cost tradeoffs


## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#next-steps)
Next steps
## [Model comparison chartSee detailed specifications and pricing for the latest Claude models](https://docs.anthropic.com/en/docs/about-claude/models/all-models)## [Migrate to Claude 4Follow the checklist for an easy migration to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4)## [Start buildingGet started with your first API call](https://docs.anthropic.com/en/docs/initial-setup)
Was this page helpful?
YesNo
[Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)[Migrating to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Establish key criteria](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#establish-key-criteria)
  * [Choose the best model to start with](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#choose-the-best-model-to-start-with)
  * [Option 1: Start with a fast, cost-effective model](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#option-1%3A-start-with-a-fast%2C-cost-effective-model)
  * [Option 2: Start with the most capable model](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#option-2%3A-start-with-the-most-capable-model)
  * [Model selection matrix](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#model-selection-matrix)
  * [Decide whether to upgrade or change models](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#decide-whether-to-upgrade-or-change-models)
  * [Next steps](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model#next-steps)



