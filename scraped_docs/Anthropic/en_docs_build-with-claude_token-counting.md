---
url: https://docs.anthropic.com/en/docs/build-with-claude/token-counting
scraped_at: 2025-05-24T19:52:45.435690
title: Token counting - Anthropic
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
Token counting
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
# Token counting
Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. With token counting, you can
  * Proactively manage rate limits and costs
  * Make smart model routing decisions
  * Optimize prompts to be a specific length


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#how-to-count-message-tokens)
How to count message tokens
The [token counting](https://docs.anthropic.com/en/api/messages-count-tokens) endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](https://docs.anthropic.com/en/docs/build-with-claude/tool-use), [images](https://docs.anthropic.com/en/docs/build-with-claude/vision), and [PDFs](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support). The response contains the total number of input tokens.
The token count should be considered an **estimate**. In some cases, the actual number of input tokens used when creating a message may differ by a small amount.
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#supported-models)
Supported models
The token counting endpoint supports the following models:
  * Claude Opus 4
  * Claude Sonnet 4
  * Claude Sonnet 3.7
  * Claude Sonnet 3.5
  * Claude Haiku 3.5
  * Claude Haiku 3
  * Claude Opus 3


### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-basic-messages)
Count tokens in basic messages
Python
TypeScript
Shell
Java
Copy
```
import anthropic
client = anthropic.Anthropic()
response = client.messages.count_tokens(
  model="claude-opus-4-20250514",
  system="You are a scientist",
  messages=[{
    "role": "user",
    "content": "Hello, Claude"
  }],
)
print(response.json())

```

JSON
Copy
```
{ "input_tokens": 14 }

```

### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-messages-with-tools)
Count tokens in messages with tools
[Server tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview#server-tools) token counts only apply to the first sampling call.
Python
TypeScript
Shell
Java
Copy
```
import anthropic
client = anthropic.Anthropic()
response = client.messages.count_tokens(
  model="claude-opus-4-20250514",
  tools=[
    {
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA",
          }
        },
        "required": ["location"],
      },
    }
  ],
  messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}]
)
print(response.json())

```

JSON
Copy
```
{ "input_tokens": 403 }

```

### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-messages-with-images)
Count tokens in messages with images
Shell
Python
TypeScript
Java
Copy
```
#!/bin/sh
IMAGE_URL="https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
IMAGE_MEDIA_TYPE="image/jpeg"
IMAGE_BASE64=$(curl "$IMAGE_URL" | base64)
curl https://api.anthropic.com/v1/messages/count_tokens \
   --header "x-api-key: $ANTHROPIC_API_KEY" \
   --header "anthropic-version: 2023-06-01" \
   --header "content-type: application/json" \
   --data \
'{
  "model": "claude-opus-4-20250514",
  "messages": [
    {"role": "user", "content": [
      {"type": "image", "source": {
        "type": "base64",
        "media_type": "'$IMAGE_MEDIA_TYPE'",
        "data": "'$IMAGE_BASE64'"
      }},
      {"type": "text", "text": "Describe this image"}
    ]}
  ]
}'

```

JSON
Copy
```
{ "input_tokens": 1551 }

```

### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-messages-with-extended-thinking)
Count tokens in messages with extended thinking
See [here](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#how-context-window-is-calculated-with-extended-thinking) for more details about how the context window is calculated with extended thinking
  * Thinking blocks from **previous** assistant turns are ignored and **do not** count toward your input tokens
  * **Current** assistant turn thinking **does** count toward your input tokens


Shell
Python
TypeScript
Java
Copy
```
curl https://api.anthropic.com/v1/messages/count_tokens \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "content-type: application/json" \
  --header "anthropic-version: 2023-06-01" \
  --data '{
   "model": "claude-opus-4-20250514",
   "thinking": {
    "type": "enabled",
    "budget_tokens": 16000
   },
   "messages": [
    {
     "role": "user",
     "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?"
    },
    {
     "role": "assistant",
     "content": [
      {
       "type": "thinking",
       "thinking": "This is a nice number theory question. Lets think about it step by step...",
       "signature": "EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV..."
      },
      {
       "type": "text",
       "text": "Yes, there are infinitely many prime numbers p such that p mod 4 = 3..."
      }
     ]
    },
    {
     "role": "user",
     "content": "Can you write a formal proof?"
    }
   ]
  }'

```

JSON
Copy
```
{ "input_tokens": 88 }

```

### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-messages-with-pdfs)
Count tokens in messages with PDFs
Token counting supports PDFs with the same [limitations](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#pdf-support-limitations) as the Messages API.
Shell
Python
TypeScript
Java
Copy
```
curl https://api.anthropic.com/v1/messages/count_tokens \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "content-type: application/json" \
  --header "anthropic-version: 2023-06-01" \
  --data '{
   "model": "claude-opus-4-20250514",
   "messages": [{
    "role": "user",
    "content": [
     {
      "type": "document",
      "source": {
       "type": "base64",
       "media_type": "application/pdf",
       "data": "'$(base64 -i document.pdf)'"
      }
     },
     {
      "type": "text",
      "text": "Please summarize this document."
     }
    ]
   }]
  }'

```

JSON
Copy
```
{ "input_tokens": 2188 }

```

## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#pricing-and-rate-limits)
Pricing and rate limits
Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](https://docs.anthropic.com/en/api/rate-limits#rate-limits). If you need higher limits, contact sales through the [Anthropic Console](https://console.anthropic.com/settings/limits).
Usage tier| Requests per minute (RPM)  
---|---  
1| 100  
2| 2,000  
3| 4,000  
4| 8,000  
Token counting and message creation have separate and independent rate limits — usage of one does not count against the limits of the other.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#faq)
FAQ
Does token counting use prompt caching?
No, token counting provides an estimate without using caching logic. While you may provide `cache_control` blocks in your token counting request, prompt caching only occurs during actual message creation.
Was this page helpful?
YesNo
[Multilingual support](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support)[Embeddings](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [How to count message tokens](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#how-to-count-message-tokens)
  * [Supported models](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#supported-models)
  * [Count tokens in basic messages](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-basic-messages)
  * [Count tokens in messages with tools](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-messages-with-tools)
  * [Count tokens in messages with images](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-messages-with-images)
  * [Count tokens in messages with extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-messages-with-extended-thinking)
  * [Count tokens in messages with PDFs](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#count-tokens-in-messages-with-pdfs)
  * [Pricing and rate limits](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#pricing-and-rate-limits)
  * [FAQ](https://docs.anthropic.com/en/docs/build-with-claude/token-counting#faq)



