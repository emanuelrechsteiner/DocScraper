---
url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/token-efficient-tool-use
scraped_at: 2025-05-24T20:04:13.259286
title: Token-efficient tool use (beta) - Anthropic
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
Tools
Token-efficient tool use (beta)
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
    * [Overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
    * [How to implement tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use)
    * [Token-efficient tool use (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/token-efficient-tool-use)
    * Client tools
    * Server tools
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


Tools
# Token-efficient tool use (beta)
Claude Sonnet 3.7 is capable of calling tools in a token-efficient manner. Requests save an average of 14% in output tokens, up to 70%, which also reduces latency. Exact token reduction and latency improvements depend on the overall response shape and size.
Token-efficient tool use is a beta feature. Please make sure to evaluate your responses before using it in production.
Please use [this form](https://forms.gle/iEG7XgmQgzceHgQKA) to provide feedback on the quality of the model responses, the API itself, or the quality of the documentation—we cannot wait to hear from you!
If you choose to experiment with this feature, we recommend using the [Prompt Improver](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver) in the [Console](https://console.anthropic.com/) to improve your prompt.
Token-efficient tool use does not currently work with [`disable_parallel_tool_use`](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#disabling-parallel-tool-use).
Claude 4 models (Opus and Sonnet) do not support this feature. The beta header `token-efficient-tools-2025-02-19` will not break an API request, but it will result in a no-op.
To use this beta feature, simply add the beta header `token-efficient-tools-2025-02-19` to a tool use request. If you are using the SDK, ensure that you are using the beta SDK with `anthropic.beta.messages`.
Here’s an example of how to use token-efficient tools with the API:
Shell
Python
TypeScript
Java
Copy
```
curl https://api.anthropic.com/v1/messages \
 -H "content-type: application/json" \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: token-efficient-tools-2025-02-19" \
 -d '{
  "model": "claude-3-7-sonnet-20250219",
  "max_tokens": 1024,
  "tools": [
   {
    "name": "get_weather",
    "description": "Get the current weather in a given location",
    "input_schema": {
     "type": "object",
     "properties": {
      "location": {
       "type": "string",
       "description": "The city and state, e.g. San Francisco, CA"
      }
     },
     "required": [
      "location"
     ]
    }
   }
  ],
  "messages": [
   {
    "role": "user",
    "content": "Tell me the weather in San Francisco."
   }
  ]
 }' | jq '.usage'

```

The above request should, on average, use fewer input and output tokens than a normal request. To confirm this, try making the same request but remove `token-efficient-tools-2025-02-19` from the beta headers list.
To keep the benefits of prompt caching, use the beta header consistently for requests you’d like to cache. If you selectively use it, prompt caching will fail.
Was this page helpful?
YesNo
[How to implement tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use)[Text editor tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

