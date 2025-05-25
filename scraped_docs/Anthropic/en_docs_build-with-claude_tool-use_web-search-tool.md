---
url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool
scraped_at: 2025-05-24T19:43:30.794688
title: Web search tool - Anthropic
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
Server tools
Web search tool
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
      * [Web search tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool)
      * [Code execution tool (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool)
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


Server tools
# Web search tool
The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. Claude automatically cites sources from search results as part of its answer.
Please reach out through our [feedback form](https://forms.gle/sWjBtsrNEY2oKGuE8) to share your experience with the web search tool.
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#supported-models)
Supported models
Web search is available on:
  * Claude Opus 4 (`claude-opus-4-20250514`)
  * Claude Sonnet 4 (`claude-sonnet-4-20250514`)
  * Claude Sonnet 3.7 (`claude-3-7-sonnet-20250219`)
  * Claude Sonnet 3.5 (new) (`claude-3-5-sonnet-latest`)
  * Claude Haiku 3.5 (`claude-3-5-haiku-latest`)


## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#how-web-search-works)
How web search works
When you add the web search tool to your API request:
  1. Claude decides when to search based on the prompt.
  2. The API executes the searches and provides Claude with the results. This process may repeat multiple times throughout a single request.
  3. At the end of its turn, Claude provides a final response with cited sources.


## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#how-to-use-web-search)
How to use web search
Your organization’s administrator must enable web search in [Console](https://console.anthropic.com/settings/privacy).
Provide the web search tool in your API request:
Shell
Python
TypeScript
Copy
```
curl https://api.anthropic.com/v1/messages \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data '{
    "model": "claude-3-7-sonnet-latest",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "How do I update a web app to TypeScript 5.5?"
      }
    ],
    "tools": [{
      "type": "web_search_20250305",
      "name": "web_search",
      "max_uses": 5
    }]
  }'

```

### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#tool-definition)
Tool definition
The web search tool supports the following parameters:
JSON
Copy
```
{
 "type": "web_search_20250305",
 "name": "web_search",
 // Optional: Limit the number of searches per request
 "max_uses": 5,
 // Optional: Only include results from these domains
 "allowed_domains": ["example.com", "trusteddomain.org"],
 // Optional: Never include results from these domains
 "blocked_domains": ["untrustedsource.com"],
 // Optional: Localize search results
 "user_location": {
  "type": "approximate",
  "city": "San Francisco",
  "region": "California",
  "country": "US",
  "timezone": "America/Los_Angeles"
 }
}

```

#### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#max-uses)
Max uses
The `max_uses` parameter limits the number of searches performed. If Claude attempts more searches than allowed, the `web_search_tool_result` will be an error with the `max_uses_exceeded` error code.
#### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#domain-filtering)
Domain filtering
When using domain filters:
  * Domains should not include the HTTP/HTTPS scheme (use `example.com` instead of `https://example.com`)
  * Subdomains are automatically included (`example.com` covers `docs.example.com`)
  * Subpaths are supported (`example.com/blog`)
  * You can use either `allowed_domains` or `blocked_domains`, but not both in the same request.


#### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#localization)
Localization
The `user_location` parameter allows you to localize search results based on a user’s location.
  * `type`: The type of location (must be `approximate`)
  * `city`: The city name
  * `region`: The region or state
  * `country`: The country
  * `timezone`: The [IANA timezone ID](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).


### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#response)
Response
Here’s an example response structure:
Copy
```
{
 "role": "assistant",
 "content": [
  // 1. Claude's decision to search
  {
   "type": "text",
   "text": "I'll search for when Claude Shannon was born."
  },
  // 2. The search query used
  {
   "type": "server_tool_use",
   "id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
   "name": "web_search",
   "input": {
    "query": "claude shannon birth date"
   }
  },
  // 3. Search results
  {
   "type": "web_search_tool_result",
   "tool_use_id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
   "content": [
    {
     "type": "web_search_result",
     "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
     "title": "Claude Shannon - Wikipedia",
     "encrypted_content": "EqgfCioIARgBIiQ3YTAwMjY1Mi1mZjM5LTQ1NGUtODgxNC1kNjNjNTk1ZWI3Y...",
     "page_age": "April 30, 2025"
    }
   ]
  },
  {
   "text": "Based on the search results, ",
   "type": "text"
  },
  // 4. Claude's response with citations
  {
   "text": "Claude Shannon was born on April 30, 1916, in Petoskey, Michigan",
   "type": "text",
   "citations": [
    {
     "type": "web_search_result_location",
     "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
     "title": "Claude Shannon - Wikipedia",
     "encrypted_index": "Eo8BCioIAhgBIiQyYjQ0OWJmZi1lNm..",
     "cited_text": "Claude Elwood Shannon (April 30, 1916 – February 24, 2001) was an American mathematician, electrical engineer, computer scientist, cryptographer and i..."
    }
   ]
  }
 ],
 "id": "msg_a930390d3a",
 "usage": {
  "input_tokens": 6039,
  "output_tokens": 931,
  "server_tool_use": {
   "web_search_requests": 1
  }
 },
 "stop_reason": "end_turn"
}

```

#### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#search-results)
Search results
Search results include:
  * `url`: The URL of the source page
  * `title`: The title of the source page
  * `page_age`: When the site was last updated
  * `encrypted_content`: Encrypted content that must be passed back in multi-turn conversations for citations


#### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#citations)
Citations
Citations are always enabled for web search, and each `web_search_result_location` includes:
  * `url`: The URL of the cited source
  * `title`: The title of the cited source
  * `encrypted_index`: A reference that must be passed back for multi-turn conversations.
  * `cited_text`: Up to 150 characters of the cited content


The web search citation fields `cited_text`, `title`, and `url` do not count towards input or output token usage.
When displaying web results or information contained in web results to end users, inline citations must be made clearly visible and clickable in your user interface.
#### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#errors)
Errors
If an error occurs during web search, you’ll receive a response that takes the following form:
Copy
```
{
 "type": "web_search_tool_result",
 "tool_use_id": "servertoolu_a93jad",
 "content": {
  "type": "web_search_tool_result_error",
  "error_code": "max_uses_exceeded"
 }
}

```

These are the possible error codes:
  * `too_many_requests`: Rate limit exceeded
  * `invalid_input`: Invalid search query parameter
  * `max_uses_exceeded`: Maximum web search tool uses exceeded
  * `query_too_long`: Query exceeds maximum length
  * `unavailable`: An internal error occurred


#### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#pause-turn-stop-reason)
`pause_turn` stop reason
The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation.
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#prompt-caching)
Prompt caching
Web search works with [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching). To enable prompt caching, add at least one `cache_control` breakpoint in your request. The system will automatically cache up until the last `web_search_tool_result` block when executing the tool.
For multi-turn conversations, set a `cache_control` breakpoint on or after the last `web_search_tool_result` block to reuse cached content.
For example, to use prompt caching with web search for a multi-turn conversation:
Copy
```
import anthropic
client = anthropic.Anthropic()
# First request with web search and cache breakpoint
messages = [
  {
    "role": "user",
    "content": "What's the current weather in San Francisco today?"
  }
]
response1 = client.messages.create(
  model="claude-3-7-sonnet-latest",
  max_tokens=1024,
  messages=messages,
  tools=[{
    "type": "web_search_20250305",
    "name": "web_search",
    "user_location": {
      "type": "approximate",
      "city": "San Francisco",
      "region": "California",
      "country": "US",
      "timezone": "America/Los_Angeles"
    }
  }]
)
# Add Claude's response to the conversation
messages.append({
  "role": "assistant",
  "content": response1.content
})
# Second request with cache breakpoint after the search results
messages.append({
  "role": "user",
  "content": "Should I expect rain later this week?",
  "cache_control": {"type": "ephemeral"} # Cache up to this point
})
response2 = client.messages.create(
  model="claude-3-7-sonnet-latest",
  max_tokens=1024,
  messages=messages,
  tools=[{
    "type": "web_search_20250305",
    "name": "web_search",
    "user_location": {
      "type": "approximate",
      "city": "San Francisco",
      "region": "California",
      "country": "US",
      "timezone": "America/Los_Angeles"
    }
  }]
)
# The second response will benefit from cached search results
# while still being able to perform new searches if needed
print(f"Cache read tokens: {response2.usage.get('cache_read_input_tokens', 0)}")

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#streaming)
Streaming
With streaming enabled, you’ll receive search events as part of the stream. There will be a pause while the search executes:
Copy
```
event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}
event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}
// Claude's decision to search
event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_search"}}
// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"latest quantum computing breakthroughs 2025\"}"}}
// Pause while search executes
// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": [{"type": "web_search_result", "title": "Quantum Computing Breakthroughs in 2025", "url": "https://example.com"}]}}
// Claude's response with citations (omitted in this example)

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#batch-requests)
Batch requests
You can include the web search tool in the [Messages Batches API](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing). Web search tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#usage-and-pricing)
Usage and pricing
Web search usage is charged in addition to token usage:
Copy
```
"usage": {
 "input_tokens": 105,
 "output_tokens": 6039,
 "cache_read_input_tokens": 7123,
 "cache_creation_input_tokens": 7345,
 "server_tool_use": {
  "web_search_requests": 1
 }
}

```

Web search is available on the Anthropic API for $10 per 1,000 searches, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.
Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.
Was this page helpful?
YesNo
[Text editor tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool)[Code execution tool (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Supported models](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#supported-models)
  * [How web search works](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#how-web-search-works)
  * [How to use web search](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#how-to-use-web-search)
  * [Tool definition](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#tool-definition)
  * [Max uses](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#max-uses)
  * [Domain filtering](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#domain-filtering)
  * [Localization](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#localization)
  * [Response](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#response)
  * [Search results](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#search-results)
  * [Citations](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#citations)
  * [Errors](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#errors)
  * [pause_turn stop reason](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#pause-turn-stop-reason)
  * [Prompt caching](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#prompt-caching)
  * [Streaming](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#streaming)
  * [Batch requests](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#batch-requests)
  * [Usage and pricing](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool#usage-and-pricing)



