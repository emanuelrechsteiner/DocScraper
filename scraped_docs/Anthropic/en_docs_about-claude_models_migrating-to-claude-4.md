---
url: https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4
scraped_at: 2025-05-24T19:46:13.488411
title: Migrating to Claude 4 - Anthropic
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
Migrating to Claude 4
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
# Migrating to Claude 4
This page provides guidance on migrating from Claude 3.7 models to Claude 4 models (Opus 4 and Sonnet 4).
In most cases, you can switch to Claude 4 models with minimal changes:
  1. Update your model name:
     * From: `claude-3-7-sonnet-20250219`
     * To: `claude-sonnet-4-20250514` or `claude-opus-4-20250514`
  2. Existing API calls should continue to work without modification, although API behavior has changed slightly in Claude 4 models (see [API release notes](https://docs.anthropic.com/en/release-notes/api) for details).


## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#what%E2%80%99s-new-in-claude-4)
What’s new in Claude 4
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#new-refusal-stop-reason)
New refusal stop reason
Claude 4 models introduce a new `refusal` stop reason for content that the model declines to generate for safety reasons, due to the increased intelligence of Claude 4 models:
Copy
```
{"id":"msg_014XEDjypDjFzgKVWdFUXxZP",
"type":"message",
"role":"assistant",
"model":"claude-sonnet-4-20250514",
"content":[{"type":"text","text":"I would be happy to assist you. You can "}],
"stop_reason":"refusal",
"stop_sequence":null,
"usage":{"input_tokens":564,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"output_tokens":22}
}

```

When migrating to Claude 4, you should update your application to [handle `refusal` stop reasons](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals).
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#summarized-thinking)
Summarized thinking
With extended thinking enabled, the Messages API for Claude 4 models returns a summary of Claude’s full thinking process. Summarized thinking provides the full intelligence benefits of extended thinking, while preventing misuse.
While the API is consistent across Claude 3.7 and 4 models, streaming responses for extended thinking might return in a “chunky” delivery pattern, with possible delays between streaming events.
Summarization is processed by a different model than the one you target in your requests. The thinking model does not see the summarized output.
For more information, see the [Extended thinking documentation](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#summarized-thinking).
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#interleaved-thinking)
Interleaved thinking
Claude 4 models support interleaving tool use with extended thinking, allowing for more natural conversations where tool uses and responses can be mixed with regular messages.
Interleaved thinking is in beta. To enable interleaved thinking, add [the beta header](https://docs.anthropic.com/en/api/beta-headers) `interleaved-thinking-2025-05-14` to your API request.
For more information, see the [Extended thinking documentation](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking).
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#updated-text-editor-tool)
Updated text editor tool
The text editor tool has been updated for Claude 4 models with the following changes:
  * **Tool type** : `text_editor_20250429`
  * **Tool name** : `str_replace_based_edit_tool`
  * The `undo_edit` command is no longer supported in Claude 4 models.


The `str_replace_editor` text editor tool remains the same for Claude Sonnet 3.7.
If you’re migrating from Claude Sonnet 3.7 and using the text editor tool:
Copy
```
# Claude Sonnet 3.7
tools=[
  {
    "type": "text_editor_20250124",
    "name": "str_replace_editor"
  }
]
# Claude 4
tools=[
  {
    "type": "text_editor_20250429",
    "name": "str_replace_based_edit_tool"
  }
]

```

For more information, see the [Text editor tool documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool).
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#token-efficient-tool-use-no-longer-supported)
Token-efficient tool use no longer supported
[Token-efficient tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/token-efficient-tool-use) is only available in Claude Sonnet 3.7.
If you’re migrating from Claude Sonnet 3.7 and using token-efficient tool use, we recommend removing the `token-efficient-tools-2025-02-19` [beta header](https://docs.anthropic.com/en/api/beta-headers) from your requests.
The `token-efficient-tools-2025-02-19` beta header can still be included in Claude 4 requests, but it will have no effect.
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#extended-output-no-longer-supported)
Extended output no longer supported
The `output-128k-2025-02-19` [beta header](https://docs.anthropic.com/en/api/beta-headers) for extended output is only available in Claude Sonnet 3.7.
If you’re migrating from Claude Sonnet 3.7, we recommend removing `output-128k-2025-02-19` from your requests.
The `output-128k-2025-02-19` beta header can still be included in Claude 4 requests, but it will have no effect.
## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#performance-considerations)
Performance considerations
### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#claude-sonnet-4)
Claude Sonnet 4
  * Improved reasoning and intelligence capabilities compared to Claude Sonnet 3.7
  * Enhanced tool use accuracy


### 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#claude-opus-4)
Claude Opus 4
  * Most capable model with superior reasoning and intelligence
  * Slower than Sonnet models
  * Best for complex tasks requiring deep analysis


## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#migration-checklist)
Migration checklist
  * Update model id in your API calls
  * Test existing requests (should work without changes)
  * Remove `token-efficient-tools-2025-02-19` beta header if applicable
  * Remove `output-128k-2025-02-19` beta header if applicable
  * Handle new `refusal` stop reason
  * Update text editor tool type and name if using it
  * Remove any code that uses the `undo_edit` command
  * Explore new tool interleaving capabilities with extended thinking
  * Review [Claude 4 prompt engineering best practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices) for optimal results
  * Test in development before production deployment


## 
[​](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#need-help%3F)
Need help?
  * Check our [API documentation](https://docs.anthropic.com/en/api/overview) for detailed specifications.
  * Review [model capabilities](https://docs.anthropic.com/en/docs/about-claude/models/overview) for performance comparisons.
  * Review [API release notes](https://docs.anthropic.com/en/release-notes/api) for API updates.
  * Contact support if you encounter any issues during migration.


Was this page helpful?
YesNo
[Choosing a model](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model)[Model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [What’s new in Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#what%E2%80%99s-new-in-claude-4)
  * [New refusal stop reason](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#new-refusal-stop-reason)
  * [Summarized thinking](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#summarized-thinking)
  * [Interleaved thinking](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#interleaved-thinking)
  * [Updated text editor tool](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#updated-text-editor-tool)
  * [Token-efficient tool use no longer supported](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#token-efficient-tool-use-no-longer-supported)
  * [Extended output no longer supported](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#extended-output-no-longer-supported)
  * [Performance considerations](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#performance-considerations)
  * [Claude Sonnet 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#claude-sonnet-4)
  * [Claude Opus 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#claude-opus-4)
  * [Migration checklist](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#migration-checklist)
  * [Need help?](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4#need-help%3F)



