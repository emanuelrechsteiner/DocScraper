---
url: https://docs.anthropic.com/en/api
scraped_at: 2025-05-24T19:47:28.672051
title: Overview - Anthropic
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
Using the APIs
Overview
[Welcome](https://docs.anthropic.com/en/home)[Developer Guide](https://docs.anthropic.com/en/docs/welcome)[API Guide](https://docs.anthropic.com/en/api/overview)[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)[Resources](https://docs.anthropic.com/en/resources/overview)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)
* [Documentation](https://docs.anthropic.com/en/home)
* [Developer Console](https://console.anthropic.com/)
* [Developer Discord](https://www.anthropic.com/discord)
* [Support](https://support.anthropic.com/)
##### Using the APIs
  * [Overview](https://docs.anthropic.com/en/api/overview)
  * Forming requests
  * Handling responses


##### API reference
  * Messages
  * Models
  * Message Batches
  * Files
  * Admin API
  * Experimental APIs
  * Text Completions (Legacy)


##### SDKs
  * [Client SDKs](https://docs.anthropic.com/en/api/client-sdks)
  * [OpenAI SDK compatibility (beta)](https://docs.anthropic.com/en/api/openai-sdk)


##### Examples
  * [Messages examples](https://docs.anthropic.com/en/api/messages-examples)
  * [Message Batches examples](https://docs.anthropic.com/en/api/messages-batch-examples)


##### 3rd-party APIs
  * [Amazon Bedrock API](https://docs.anthropic.com/en/api/claude-on-amazon-bedrock)
  * [Vertex AI API](https://docs.anthropic.com/en/api/claude-on-vertex-ai)


##### Support & configuration
  * [IP addresses](https://docs.anthropic.com/en/api/ip-addresses)
  * [Supported regions](https://docs.anthropic.com/en/api/supported-regions)
  * [Using the Admin API](https://docs.anthropic.com/en/api/administration-api)
  * [Getting help](https://docs.anthropic.com/en/api/getting-help)


Using the APIs
# Overview
## 
[​](https://docs.anthropic.com/en/api/overview#accessing-the-api)
Accessing the API
The API is made available via our web [Console](https://console.anthropic.com/). You can use the [Workbench](https://console.anthropic.com/workbench/3b57d80a-99f2-4760-8316-d3bb14fbfb1e) to try out the API in the browser and then generate API keys in [Account Settings](https://console.anthropic.com/account/keys). Use [workspaces](https://console.anthropic.com/settings/workspaces) to segment your API keys and [control spend](https://docs.anthropic.com/en/api/rate-limits) by use case.
## 
[​](https://docs.anthropic.com/en/api/overview#authentication)
Authentication
All requests to the Anthropic API must include an `x-api-key` header with your API key. If you are using the Client SDKs, you will set the API when constructing a client, and then the SDK will send the header on your behalf with every request. If integrating directly with the API, you’ll need to send this header yourself.
## 
[​](https://docs.anthropic.com/en/api/overview#content-types)
Content types
The Anthropic API always accepts JSON in request bodies and returns JSON in response bodies. You will need to send the `content-type: application/json` header in requests. If you are using the Client SDKs, this will be taken care of automatically.
## 
[​](https://docs.anthropic.com/en/api/overview#response-headers)
Response Headers
The Anthropic API includes the following headers in every response:
  * `request-id`: A globally unique identifier for the request.
  * `anthropic-organization-id`: The organization ID associated with the API key used in the request.


## 
[​](https://docs.anthropic.com/en/api/overview#examples)
Examples
  * curl
  * Python
  * TypeScript


Shell
Copy
```
curl https://api.anthropic.com/v1/messages \
   --header "x-api-key: $ANTHROPIC_API_KEY" \
   --header "anthropic-version: 2023-06-01" \
   --header "content-type: application/json" \
   --data \
'{
  "model": "claude-opus-4-20250514",
  "max_tokens": 1024,
  "messages": [
    {"role": "user", "content": "Hello, world"}
  ]
}'

```

Shell
Copy
```
curl https://api.anthropic.com/v1/messages \
   --header "x-api-key: $ANTHROPIC_API_KEY" \
   --header "anthropic-version: 2023-06-01" \
   --header "content-type: application/json" \
   --data \
'{
  "model": "claude-opus-4-20250514",
  "max_tokens": 1024,
  "messages": [
    {"role": "user", "content": "Hello, world"}
  ]
}'

```

Install via PyPI:
Copy
```
pip install anthropic

```

Python
Copy
```
import anthropic
client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-opus-4-20250514",
  max_tokens=1024,
  messages=[
    {"role": "user", "content": "Hello, Claude"}
  ]
)
print(message.content)

```

Install via npm:
Copy
```
npm install @anthropic-ai/sdk

```

TypeScript
Copy
```
import Anthropic from '@anthropic-ai/sdk';
const anthropic = new Anthropic({
 apiKey: 'my_api_key', // defaults to process.env["ANTHROPIC_API_KEY"]
});
const msg = await anthropic.messages.create({
 model: "claude-opus-4-20250514",
 max_tokens: 1024,
 messages: [{ role: "user", content: "Hello, Claude" }],
});
console.log(msg);

```

Was this page helpful?
YesNo
[Versions](https://docs.anthropic.com/en/api/versioning)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Accessing the API](https://docs.anthropic.com/en/api/overview#accessing-the-api)
  * [Authentication](https://docs.anthropic.com/en/api/overview#authentication)
  * [Content types](https://docs.anthropic.com/en/api/overview#content-types)
  * [Response Headers](https://docs.anthropic.com/en/api/overview#response-headers)
  * [Examples](https://docs.anthropic.com/en/api/overview#examples)



