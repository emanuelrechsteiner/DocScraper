---
url: https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support
scraped_at: 2025-05-24T19:39:12.844041
title: Multilingual support - Anthropic
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
Explore features
Multilingual support
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


Explore features
# Multilingual support
Claude excels at tasks across multiple languages, maintaining strong cross-lingual performance relative to English.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support#overview)
Overview
Claude demonstrates robust multilingual capabilities, with particularly strong performance in zero-shot tasks across languages. The model maintains consistent relative performance across both widely-spoken and lower-resource languages, making it a reliable choice for multilingual applications.
Note that Claude is capable in many languages beyond those benchmarked below. We encourage testing with any languages relevant to your specific use cases.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support#performance-data)
Performance data
Below are the zero-shot chain-of-thought evaluation scores for Claude 4, Claude 3.7 Sonnet and Claude 3.5 models across different languages, shown as a percent relative to English performance (100%):
Language| Claude Opus 41| Claude Sonnet 41| Claude Sonnet 3.71| Claude Sonnet 3.5 v2| Claude Haiku 3.5  
---|---|---|---|---|---  
English (baseline, fixed to 100%)| 100%| 100%| 100%| 100%| 100%  
Spanish| 98.0%| 97.5%| 97.6%| 96.9%| 94.6%  
Portuguese (Brazil)| 97.3%| 97.2%| 97.3%| 96.0%| 94.6%  
Italian| 97.5%| 97.3%| 97.2%| 95.6%| 95.0%  
French| 97.7%| 97.1%| 96.9%| 96.2%| 95.3%  
Indonesian| 97.2%| 96.2%| 96.3%| 94.0%| 91.2%  
German| 97.1%| 94.7%| 96.2%| 94.0%| 92.5%  
Arabic| 96.9%| 96.1%| 95.4%| 92.5%| 84.7%  
Chinese (Simplified)| 96.7%| 95.9%| 95.3%| 92.8%| 90.9%  
Korean| 96.4%| 95.9%| 95.2%| 92.8%| 89.1%  
Japanese| 96.2%| 95.6%| 95.0%| 92.7%| 90.8%  
Hindi| 96.7%| 95.8%| 94.2%| 89.3%| 80.1%  
Bengali| 95.2%| 94.4%| 92.4%| 85.9%| 72.9%  
Swahili| 89.5%| 87.1%| 89.2%| 83.9%| 64.7%  
Yoruba| 78.9%| 76.4%| 76.7%| 64.9%| 46.1%  
1 With [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking).
These metrics are based on [MMLU (Massive Multitask Language Understanding)](https://en.wikipedia.org/wiki/MMLU) English test sets that were translated into 14 additional languages by professional human translators, as documented in [OpenAI’s simple-evals repository](https://github.com/openai/simple-evals/blob/main/multilingual_mmlu_benchmark_results.md). The use of human translators for this evaluation ensures high-quality translations, particularly important for languages with fewer digital resources.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support#best-practices)
Best practices
When working with multilingual content:
  1. **Provide clear language context** : While Claude can detect the target language automatically, explicitly stating the desired input/output language improves reliability. For enhanced fluency, you can prompt Claude to use “idiomatic speech as if it were a native speaker.”
  2. **Use native scripts** : Submit text in its native script rather than transliteration for optimal results
  3. **Consider cultural context** : Effective communication often requires cultural and regional awareness beyond pure translation


We also suggest following our general [prompt engineering guidelines](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) to better improve Claude’s performance.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support#language-support-considerations)
Language support considerations
  * Claude processes input and generates output in most world languages that use standard Unicode characters
  * Performance varies by language, with particularly strong capabilities in widely-spoken languages
  * Even in languages with fewer digital resources, Claude maintains meaningful capabilities


## [Prompt Engineering GuideMaster the art of prompt crafting to get the most out of Claude.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)## [Prompt LibraryFind a wide range of pre-crafted prompts for various tasks and industries. Perfect for inspiration or quick starts.](https://docs.anthropic.com/en/prompt-library)
Was this page helpful?
YesNo
[Citations](https://docs.anthropic.com/en/docs/build-with-claude/citations)[Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Overview](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support#overview)
  * [Performance data](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support#performance-data)
  * [Best practices](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support#best-practices)
  * [Language support considerations](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support#language-support-considerations)



