---
url: https://docs.anthropic.com/en/docs/about-claude/pricing
scraped_at: 2025-05-24T19:39:31.178851
title: Pricing - Anthropic
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
Pricing
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
# Pricing
Learn about Anthropic’s pricing structure for models and features
This page provides detailed pricing information for Anthropic’s models and features. All prices are in USD.
For the most current pricing information, please visit [anthropic.com/pricing](https://www.anthropic.com/pricing).
## 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#model-pricing)
Model pricing
The following table shows pricing for all Claude models across different usage tiers:
Model| Base Input Tokens| 5m Cache Writes| 1h Cache Writes| Cache Hits & Refreshes| Output Tokens  
---|---|---|---|---|---  
Claude Opus 4| $15 / MTok| $18.75 / MTok| $30 / MTok| $1.50 / MTok| $75 / MTok  
Claude Sonnet 4| $3 / MTok| $3.75 / MTok| $6 / MTok| $0.30 / MTok| $15 / MTok  
Claude Sonnet 3.7| $3 / MTok| $3.75 / MTok| $6 / MTok| $0.30 / MTok| $15 / MTok  
Claude Sonnet 3.5| $3 / MTok| $3.75 / MTok| $6 / MTok| $0.30 / MTok| $15 / MTok  
Claude Haiku 3.5| $0.80 / MTok| $1 / MTok| $1.6 / MTok| $0.08 / MTok| $4 / MTok  
Claude Opus 3| $15 / MTok| $18.75 / MTok| $30 / MTok| $1.50 / MTok| $75 / MTok  
Claude Haiku 3| $0.25 / MTok| $0.30 / MTok| $0.50 / MTok| $0.03 / MTok| $1.25 / MTok  
MTok = Million tokens. The “Base Input Tokens” column shows standard input pricing, “Cache Writes” and “Cache Hits” are specific to [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching), and “Output Tokens” shows output pricing.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#feature-specific-pricing)
Feature-specific pricing
### 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#batch-processing)
Batch processing
The Batch API allows asynchronous processing of large volumes of requests with a 50% discount on both input and output tokens.
Model| Batch input| Batch output  
---|---|---  
Claude Opus 4| $7.50 / MTok| $37.50 / MTok  
Claude Sonnet 4| $1.50 / MTok| $7.50 / MTok  
Claude Sonnet 3.7| $1.50 / MTok| $7.50 / MTok  
Claude Sonnet 3.5| $1.50 / MTok| $7.50 / MTok  
Claude Haiku 3.5| $0.40 / MTok| $2 / MTok  
Claude Opus 3| $7.50 / MTok| $37.50 / MTok  
Claude Haiku 3| $0.125 / MTok| $0.625 / MTok  
For more information about batch processing, see our [batch processing documentation](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing).
### 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#tool-use-pricing)
Tool use pricing
Tool use requests are priced based on:
  1. The total number of input tokens sent to the model (including in the `tools` parameter)
  2. The number of output tokens generated
  3. For server-side tools, additional usage-based pricing (e.g., web search charges per search performed)


Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage.
The additional tokens from tool use come from:
  * The `tools` parameter in API requests (tool names, descriptions, and schemas)
  * `tool_use` content blocks in API requests and responses
  * `tool_result` content blocks in API requests


When you use `tools`, we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.
Model| Tool choice| Tool use system prompt token count  
---|---|---  
Claude Opus 4| `auto`, `none``any`, `tool`| 346 tokens313 tokens  
Claude Sonnet 4| `auto`, `none``any`, `tool`| 346 tokens313 tokens  
Claude Sonnet 3.7| `auto`, `none``any`, `tool`| 346 tokens313 tokens  
Claude Sonnet 3.5 (Oct)| `auto`, `none``any`, `tool`| 346 tokens313 tokens  
Claude Sonnet 3.5 (June)| `auto`, `none``any`, `tool`| 294 tokens261 tokens  
Claude Haiku 3.5| `auto`, `none``any`, `tool`| 264 tokens340 tokens  
Claude Opus 3| `auto`, `none``any`, `tool`| 530 tokens281 tokens  
Claude Sonnet 3| `auto`, `none``any`, `tool`| 159 tokens235 tokens  
Claude Haiku 3| `auto`, `none``any`, `tool`| 264 tokens340 tokens  
These token counts are added to your normal input and output tokens to calculate the total cost of a request.
For current per-model prices, refer to our [model pricing](https://docs.anthropic.com/en/docs/about-claude/pricing#model-pricing) section above.
For more information about tool use implementation and best practices, see our [tool use documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview).
## 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#agent-use-case-pricing-examples)
Agent use case pricing examples
Understanding pricing for agent applications is crucial when building with Claude. These real-world examples can help you estimate costs for different agent patterns.
### 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#customer-support-agent-example)
Customer support agent example
When building a customer support agent, here’s how costs might break down:
Example calculation for processing 10,000 support tickets:
  * Average ~3,700 tokens per conversation
  * Using Claude Sonnet 4 at 3/MTokinput,3/MTok input, 3/MTokinput,15/MTok output
  * Total cost: ~$22.20 per 10,000 tickets


For a detailed walkthrough of this calculation, see our [customer support agent guide](https://docs.anthropic.com/en/docs/build-with-claude/customer-support-agent).
### 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#general-agent-workflow-pricing)
General agent workflow pricing
For more complex agent architectures with multiple steps:
  1. **Initial request processing**
     * Typical input: 500-1,000 tokens
     * Processing cost: ~$0.003 per request
  2. **Memory and context retrieval**
     * Retrieved context: 2,000-5,000 tokens
     * Cost per retrieval: ~$0.015 per operation
  3. **Action planning and execution**
     * Planning tokens: 1,000-2,000
     * Execution feedback: 500-1,000
     * Combined cost: ~$0.045 per action


For a comprehensive guide on agent pricing patterns, see our [agent use cases guide](https://docs.anthropic.com/en/docs/build-with-claude/agent-use-cases).
### 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#cost-optimization-strategies)
Cost optimization strategies
When building agents with Claude:
  1. **Use appropriate models** : Choose Haiku for simple tasks, Sonnet for complex reasoning
  2. **Implement prompt caching** : Reduce costs for repeated context
  3. **Batch operations** : Use the Batch API for non-time-sensitive tasks
  4. **Monitor usage patterns** : Track token consumption to identify optimization opportunities


For high-volume agent applications, consider contacting our [enterprise sales team](https://www.anthropic.com/contact-sales) for custom pricing arrangements.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#additional-pricing-considerations)
Additional pricing considerations
### 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#rate-limits)
Rate limits
Rate limits vary by usage tier and affect how many requests you can make:
  * **Tier 1** : Entry-level usage with basic limits
  * **Tier 2** : Increased limits for growing applications
  * **Tier 3** : Higher limits for established applications
  * **Tier 4** : Maximum standard limits
  * **Enterprise** : Custom limits available


For detailed rate limit information, see our [rate limits documentation](https://docs.anthropic.com/en/api/rate-limits).
### 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#volume-discounts)
Volume discounts
Volume discounts may be available for high-volume users. These are negotiated on a case-by-case basis.
  * Standard tiers use the pricing shown above
  * Enterprise customers can contact sales for custom pricing
  * Academic and research discounts may be available


### 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#enterprise-pricing)
Enterprise pricing
For enterprise customers with specific needs:
  * Custom rate limits
  * Volume discounts
  * Dedicated support
  * Custom terms


Contact our sales team at sales@anthropic.com or through the [Anthropic Console](https://console.anthropic.com/settings/limits) to discuss enterprise pricing options.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#billing-and-payment)
Billing and payment
  * Billing is calculated monthly based on actual usage
  * Payments are processed in USD
  * Credit card and invoicing options available
  * Usage tracking available in the [Anthropic Console](https://console.anthropic.com)


## 
[​](https://docs.anthropic.com/en/docs/about-claude/pricing#frequently-asked-questions)
Frequently asked questions
**How is token usage calculated?**
Tokens are pieces of text that models process. As a rough estimate, 1 token is approximately 4 characters or 0.75 words in English. The exact count varies by language and content type.
**Are there free tiers or trials?**
New users receive a small amount of free credits to test the API. Contact sales for information about extended trials for enterprise evaluation.
**How do discounts stack?**
Batch API and prompt caching discounts can be combined. For example, using both features together provides significant cost savings compared to standard API calls.
**What payment methods are accepted?**
We accept major credit cards for standard accounts. Enterprise customers can arrange invoicing and other payment methods.
For additional questions about pricing, contact support@anthropic.com.
Was this page helpful?
YesNo
[Model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)[Building with Claude](https://docs.anthropic.com/en/docs/overview)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Model pricing](https://docs.anthropic.com/en/docs/about-claude/pricing#model-pricing)
  * [Feature-specific pricing](https://docs.anthropic.com/en/docs/about-claude/pricing#feature-specific-pricing)
  * [Batch processing](https://docs.anthropic.com/en/docs/about-claude/pricing#batch-processing)
  * [Tool use pricing](https://docs.anthropic.com/en/docs/about-claude/pricing#tool-use-pricing)
  * [Agent use case pricing examples](https://docs.anthropic.com/en/docs/about-claude/pricing#agent-use-case-pricing-examples)
  * [Customer support agent example](https://docs.anthropic.com/en/docs/about-claude/pricing#customer-support-agent-example)
  * [General agent workflow pricing](https://docs.anthropic.com/en/docs/about-claude/pricing#general-agent-workflow-pricing)
  * [Cost optimization strategies](https://docs.anthropic.com/en/docs/about-claude/pricing#cost-optimization-strategies)
  * [Additional pricing considerations](https://docs.anthropic.com/en/docs/about-claude/pricing#additional-pricing-considerations)
  * [Rate limits](https://docs.anthropic.com/en/docs/about-claude/pricing#rate-limits)
  * [Volume discounts](https://docs.anthropic.com/en/docs/about-claude/pricing#volume-discounts)
  * [Enterprise pricing](https://docs.anthropic.com/en/docs/about-claude/pricing#enterprise-pricing)
  * [Billing and payment](https://docs.anthropic.com/en/docs/about-claude/pricing#billing-and-payment)
  * [Frequently asked questions](https://docs.anthropic.com/en/docs/about-claude/pricing#frequently-asked-questions)



