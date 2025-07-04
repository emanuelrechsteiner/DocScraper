---
url: https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector
scraped_at: 2025-05-24T19:52:13.419036
title: MCP connector - Anthropic
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
Model Context Protocol (MCP)
MCP connector
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
    * [MCP overview](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
    * [MCP connector (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector)
    * [Remote MCP servers](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers)
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


Model Context Protocol (MCP)
# MCP connector
Claude’s Model Context Protocol (MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API without a separate MCP client.
This feature requires the beta header: `"anthropic-beta": "mcp-client-2025-04-04"`
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#key-features)
Key features
  * **Direct API integration** : Connect to MCP servers without implementing an MCP client
  * **Tool calling support** : Access MCP tools through the Messages API
  * **OAuth authentication** : Support for OAuth Bearer tokens for authenticated servers
  * **Multiple servers** : Connect to multiple MCP servers in a single request


## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#limitations)
Limitations
  * Of the feature set of the MCP specification, only tool calls are currently supported.
  * The server must be publicly exposed through HTTP. Local STDIO servers cannot be connected directly.
  * The MCP connector is currently not supported on Amazon Bedrock and Google Vertex.


## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#using-the-mcp-connector-in-the-messages-api)
Using the MCP connector in the Messages API
To connect to a remote MCP server, include the `mcp_servers` parameter in your Messages API request:
cURL
TypeScript
Python
Copy
```
curl https://api.anthropic.com/v1/messages \
 -H "Content-Type: application/json" \
 -H "X-API-Key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: mcp-client-2025-04-04" \
 -d '{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 1000,
  "messages": [{"role": "user", "content": "What tools do you have available?"}],
  "mcp_servers": [
   {
    "type": "url",
    "url": "https://example-server.modelcontextprotocol.io/sse",
    "name": "example-mcp",
    "authorization_token": "YOUR_TOKEN"
   }
  ]
 }'

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#mcp-server-configuration)
MCP server configuration
Each MCP server in the `mcp_servers` array supports the following configuration:
Copy
```
{
 "type": "url",
 "url": "https://example-server.modelcontextprotocol.io/sse",
 "name": "example-mcp",
 "tool_configuration": {
  "enabled": true,
  "allowed_tools": ["example_tool_1", "example_tool_2"]
 },
 "authorization_token": "YOUR_TOKEN"
}

```

### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#field-descriptions)
Field descriptions
Property| Type| Required| Description  
---|---|---|---  
`type`| string| Yes| Currently only “url” is supported  
`url`| string| Yes| The URL of the MCP server. Must start with https://  
`name`| string| Yes| A unique identifier for this MCP server. It will be used in `mcp_tool_call` blocks to identify the server and to disambiguate tools to the model.  
`tool_configuration`| object| No| Configure tool usage  
`tool_configuration.enabled`| boolean| No| Whether to enable tools from this server (default: true)  
`tool_configuration.allowed_tools`| array| No| List to restrict the tools to allow (by default, all tools are allowed)  
`authorization_token`| string| No| OAuth authorization token if required by the MCP server. See [MCP specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization).  
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#response-content-types)
Response content types
When Claude uses MCP tools, the response will include two new content block types:
### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#mcp-tool-use-block)
MCP Tool Use Block
Copy
```
{
 "type": "mcp_tool_use",
 "id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
 "name": "echo",
 "server_name": "example-mcp",
 "input": { "param1": "value1", "param2": "value2" }
}

```

### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#mcp-tool-result-block)
MCP Tool Result Block
Copy
```
{
 "type": "mcp_tool_result",
 "tool_use_id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
 "is_error": false,
 "content": [
  {
   "type": "text",
   "text": "Hello"
  }
 ]
}

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#multiple-mcp-servers)
Multiple MCP servers
You can connect to multiple MCP servers by including multiple objects in the `mcp_servers` array:
Copy
```
{
 "model": "claude-sonnet-4-20250514",
 "max_tokens": 1000,
 "messages": [
  {
   "role": "user",
   "content": "Use tools from both mcp-server-1 and mcp-server-2 to complete this task"
  }
 ],
 "mcp_servers": [
  {
   "type": "url",
   "url": "https://mcp.example1.com/sse",
   "name": "mcp-server-1",
   "authorization_token": "TOKEN1"
  },
  {
   "type": "url",
   "url": "https://mcp.example2.com/sse",
   "name": "mcp-server-2",
   "authorization_token": "TOKEN2"
  }
 ]
}

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#authentication)
Authentication
For MCP servers that require OAuth authentication, you’ll need to obtain an access token. The MCP connector beta supports passing an `authorization_token` parameter in the MCP server definition. API consumers are expected to handle the OAuth flow and obtain the access token prior to making the API call, as well as refreshing the token as needed.
### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#obtaining-an-access-token-for-testing)
Obtaining an access token for testing
The MCP inspector can guide you through the process of obtaining an access token for testing purposes.
  1. Run the inspector with the following command. You need Node.js installed on your machine.
Copy
```
npx @modelcontextprotocol/inspector

```

  2. In the sidebar on the left, for “Transport type”, select either “SSE” or “Streamable HTTP”.
  3. Enter the URL of the MCP server.
  4. In the right area, click on the “Open Auth Settings” button after “Need to configure authentication?”.
  5. Click “Quick OAuth Flow” and authorize on the OAuth screen.
  6. Follow the steps in the “OAuth Flow Progress” section of the inspector and click “Continue” until you reach “Authentication complete”.
  7. Copy the `access_token` value.
  8. Paste it into the `authorization_token` field in your MCP server configuration.


### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#using-the-access-token)
Using the access token
Once you’ve obtained an access token using either OAuth flow above, you can use it in your MCP server configuration:
Copy
```
{
 "mcp_servers": [
  {
   "type": "url",
   "url": "https://example-server.modelcontextprotocol.io/sse",
   "name": "authenticated-server",
   "authorization_token": "YOUR_ACCESS_TOKEN_HERE"
  }
 ]
}

```

For detailed explanations of the OAuth flow, refer to the [Authorization section](https://modelcontextprotocol.io/docs/concepts/authentication) in the MCP specification.
Was this page helpful?
YesNo
[MCP overview](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)[Remote MCP servers](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Key features](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#key-features)
  * [Limitations](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#limitations)
  * [Using the MCP connector in the Messages API](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#using-the-mcp-connector-in-the-messages-api)
  * [MCP server configuration](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#mcp-server-configuration)
  * [Field descriptions](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#field-descriptions)
  * [Response content types](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#response-content-types)
  * [MCP Tool Use Block](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#mcp-tool-use-block)
  * [MCP Tool Result Block](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#mcp-tool-result-block)
  * [Multiple MCP servers](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#multiple-mcp-servers)
  * [Authentication](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#authentication)
  * [Obtaining an access token for testing](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#obtaining-an-access-token-for-testing)
  * [Using the access token](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector#using-the-access-token)



