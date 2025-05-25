---
url: https://docs.anthropic.com/en/docs/overview
scraped_at: 2025-05-24T19:57:40.317069
title: Building with Claude - Anthropic
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
Learn about Claude
Building with Claude
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


Learn about Claude
# Building with Claude
Claude is a family of [highly performant and intelligent AI models](https://docs.anthropic.com/en/docs/about-claude/models) built by Anthropic. While Claude is powerful and extensible, it’s also the most trustworthy and reliable AI available. It follows critical protocols, makes fewer mistakes, and is resistant to jailbreaks—allowing [enterprise customers](https://www.anthropic.com/customers) to build the safest AI-powered applications at scale.
This guide introduces Claude’s enterprise capabilities, the end-to-end flow for developing with Claude, and how to start building.
## 
[​](https://docs.anthropic.com/en/docs/overview#what-you-can-do-with-claude)
What you can do with Claude
Claude is designed to empower enterprises at scale with strong performance across benchmark evaluations for reasoning, math, coding, and fluency in English and non-English languages.
Here’s a non-exhaustive list of Claude’s capabilities and common uses.
Capability| Enables you to…  
---|---  
Text and code generation| 
  * Adhere to brand voice for excellent customer-facing experiences such as copywriting and chatbots
  * Create production-level code and operate (in-line code generation, debugging, and conversational querying) within complex codebases
  * Build automatic translation features between languages
  * Conduct complex financial forecasts
  * Support legal use cases that require high-quality technical analysis, long context windows for processing detailed documents, and fast outputs

  
Vision| 
  * Process and analyze visual input, such as extracting insights from charts and graphs
  * Generate code from images with code snippets or templates based on diagrams
  * Describe an image for a user with low vision

  
Tool use| 
  * Interact with external client-side tools and functions, allowing Claude to reason, plan, and execute actions by generating structured outputs through API calls

  
## 
[​](https://docs.anthropic.com/en/docs/overview#enterprise-considerations)
Enterprise considerations
Along with an extensive set of features, tools, and capabilities, Claude is also built to be secure, trustworthy, and scalable for wide-reaching enterprise needs.
Feature| Description  
---|---  
**Secure**| 
  * [Enterprise-grade](https://trust.anthropic.com/) security and data handling for API
  * SOC II Type 2 certified, HIPAA compliance options for API
  * Accessible through AWS (GA) and GCP (in private preview)

  
**Trustworthy**| 
  * Resistant to jailbreaks and misuse. We continuously monitor prompts and outputs for harmful, malicious use cases that violate our [AUP](https://www.anthropic.com/legal/aup).
  * Copyright indemnity protections for paid commercial services
  * Uniquely positioned to serve high trust industries that process large volumes of sensitive user data

  
**Capable**| 
  * 200K token context window for expanded use cases, with future support for 1M
  * [Tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use), also known as function calling, which allows seamless integration of Claude into specialized applications and custom workflows
  * Multimodal input capabilities with text output, allowing you to upload images (such as tables, graphs, and photos) along with text prompts for richer context and complex use cases
  * [Developer Console](https://console.anthropic.com) with Workbench and prompt generation tool for easier, more powerful prompting and experimentation
  * [SDKs](https://docs.anthropic.com/en/api/client-sdks) and [APIs](https://docs.anthropic.com/en/api) to expedite and enhance development

  
**Reliable**| 
  * Very low hallucination rates
  * Accurate over long documents

  
**Global**| 
  * Great for coding tasks and fluency in English and non-English languages like Spanish and Japanese
  * Enables use cases like translation services and broader global utility

  
**Cost conscious**| 
  * Family of models balances cost, performance, and intelligence

  
## 
[​](https://docs.anthropic.com/en/docs/overview#implementing-claude)
Implementing Claude
1
Scope your use case
  * Identify a problem to solve or tasks to automate with Claude.
  * Define requirements: features, performance, and cost.


2
Design your integration
  * Select Claude’s capabilities (e.g., vision, tool use) and models (Opus, Sonnet, Haiku) based on needs.
  * Choose a deployment method, such as the Anthropic API, AWS Bedrock, or Vertex AI.


3
Prepare your data
  * Identify and clean relevant data (databases, code repos, knowledge bases) for Claude’s context.


4
Develop your prompts
  * Use Workbench to create evals, draft prompts, and iteratively refine based on test results.
  * Deploy polished prompts and monitor real-world performance for further refinement.


5
Implement Claude
  * Set up your environment, integrate Claude with your systems (APIs, databases, UIs), and define human-in-the-loop requirements.


6
Test your system
  * Conduct red teaming for potential misuse and A/B test improvements.


7
Deploy to production
  * Once your application runs smoothly end-to-end, deploy to production.


8
Monitor and improve
  * Monitor performance and effectiveness to make ongoing improvements.


## 
[​](https://docs.anthropic.com/en/docs/overview#start-building-with-claude)
Start building with Claude
When you’re ready, start building with Claude:
  * Follow the [Quickstart](https://docs.anthropic.com/en/docs/quickstart) to make your first API call
  * Check out the [API Reference](https://docs.anthropic.com/en/api)
  * Explore the [Prompt Library](https://docs.anthropic.com/en/prompt-library/library) for example prompts
  * Experiment and start building with the [Workbench](https://console.anthropic.com)
  * Check out the [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) for working code examples


Was this page helpful?
YesNo
[Pricing](https://docs.anthropic.com/en/docs/about-claude/pricing)[Overview](https://docs.anthropic.com/en/docs/about-claude/use-case-guides/overview)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [What you can do with Claude](https://docs.anthropic.com/en/docs/overview#what-you-can-do-with-claude)
  * [Enterprise considerations](https://docs.anthropic.com/en/docs/overview#enterprise-considerations)
  * [Implementing Claude](https://docs.anthropic.com/en/docs/overview#implementing-claude)
  * [Start building with Claude](https://docs.anthropic.com/en/docs/overview#start-building-with-claude)



