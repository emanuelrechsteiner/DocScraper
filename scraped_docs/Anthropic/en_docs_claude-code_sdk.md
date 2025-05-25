---
url: https://docs.anthropic.com/en/docs/claude-code/sdk
scraped_at: 2025-05-24T19:38:24.260143
title: SDK - Anthropic
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
Claude Code
SDK
[Welcome](https://docs.anthropic.com/en/home)[Developer Guide](https://docs.anthropic.com/en/docs/welcome)[API Guide](https://docs.anthropic.com/en/api/overview)[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)[Resources](https://docs.anthropic.com/en/resources/overview)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)
* [Documentation](https://docs.anthropic.com/en/home)
* [Developer Console](https://console.anthropic.com/)
* [Developer Discord](https://www.anthropic.com/discord)
* [Support](https://support.anthropic.com/)
##### Claude Code
  * [Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
  * [Getting started](https://docs.anthropic.com/en/docs/claude-code/getting-started)
  * [Common tasks](https://docs.anthropic.com/en/docs/claude-code/common-tasks)
  * [CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage)
  * [IDE integrations](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
  * [Memory management](https://docs.anthropic.com/en/docs/claude-code/memory)
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/settings)
  * [Security](https://docs.anthropic.com/en/docs/claude-code/security)
  * [Team setup](https://docs.anthropic.com/en/docs/claude-code/team)
  * [Monitoring usage](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage)
  * [Costs](https://docs.anthropic.com/en/docs/claude-code/costs)
  * [Bedrock, Vertex, and proxies](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies)
  * [GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
  * [SDK](https://docs.anthropic.com/en/docs/claude-code/sdk)
  * [Tutorials](https://docs.anthropic.com/en/docs/claude-code/tutorials)
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)


Claude Code
# SDK
Programmatically integrate Claude Code into your applications using the SDK.
The Claude Code SDK allows developers to programmatically integrate Claude Code into their applications. It enables running Claude Code as a subprocess, providing a way to build AI-powered coding assistants and tools that leverage Claude’s capabilities.
The SDK currently support command line usage. TypeScript and Python SDKs are coming soon.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#basic-sdk-usage)
Basic SDK usage
The Claude Code SDK allows you to use Claude Code in non-interactive mode from your applications. Here’s a basic example:
Copy
```
# Run a single prompt and exit (print mode)
$ claude -p "Write a function to calculate Fibonacci numbers"
# Using a pipe to provide stdin
$ echo "Explain this code" | claude -p
# Output in JSON format with metadata
$ claude -p "Generate a hello world function" --output-format json
# Stream JSON output as it arrives
$ claude -p "Build a React component" --output-format stream-json

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#advanced-usage)
Advanced usage
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#multi-turn-conversations)
Multi-turn conversations
For multi-turn conversations, you can resume conversations or continue from the most recent session:
Copy
```
# Continue the most recent conversation
$ claude --continue
# Continue and provide a new prompt
$ claude --continue "Now refactor this for better performance"
# Resume a specific conversation by session ID
$ claude --resume 550e8400-e29b-41d4-a716-446655440000
# Resume in print mode (non-interactive)
$ claude -p --resume 550e8400-e29b-41d4-a716-446655440000 "Update the tests"
# Continue in print mode (non-interactive)
$ claude -p --continue "Add error handling"

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#custom-system-prompts)
Custom system prompts
You can provide custom system prompts to guide Claude’s behavior:
Copy
```
# Override system prompt (only works with --print)
$ claude -p "Build a REST API" --system-prompt "You are a senior backend engineer. Focus on security, performance, and maintainability."
# System prompt with specific requirements
$ claude -p "Create a database schema" --system-prompt "You are a database architect. Use PostgreSQL best practices and include proper indexing."

```

You can also append instructions to the default system prompt:
Copy
```
# Append system prompt (only works with --print)
$ claude -p "Build a REST API" --append-system-prompt "After writing code, be sure to code review yourself."

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#mcp-configuration)
MCP Configuration
The Model Context Protocol (MCP) allows you to extend Claude Code with additional tools and resources from external servers. Using the `--mcp-config` flag, you can load MCP servers that provide specialized capabilities like database access, API integrations, or custom tooling.
Create a JSON configuration file with your MCP servers:
Copy
```
{
 "mcpServers": {
  "filesystem": {
   "command": "npx",
   "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/path/to/allowed/files"
   ]
  },
  "github": {
   "command": "npx",
   "args": ["-y", "@modelcontextprotocol/server-github"],
   "env": {
    "GITHUB_TOKEN": "your-github-token"
   }
  }
 }
}

```

Then use it with Claude Code:
Copy
```
# Load MCP servers from configuration
$ claude -p "List all files in the project" --mcp-config mcp-servers.json
# Important: MCP tools must be explicitly allowed using --allowedTools
# MCP tools follow the format: mcp__$serverName__$toolName
$ claude -p "Search for TODO comments" \
 --mcp-config mcp-servers.json \
 --allowedTools "mcp__filesystem__read_file,mcp__filesystem__list_directory"
# Use an MCP tool for handling permission prompts in non-interactive mode
$ claude -p "Deploy the application" \
 --mcp-config mcp-servers.json \
 --allowedTools "mcp__permissions__approve" \
 --permission-prompt-tool mcp__permissions__approve

```

Note: When using MCP tools, you must explicitly allow them using the `--allowedTools` flag. MCP tool names follow the pattern `mcp__<serverName>__<toolName>` where:
  * `serverName` is the key from your MCP configuration file
  * `toolName` is the specific tool provided by that server


This security measure ensures that MCP tools are only used when explicitly permitted.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#available-cli-options)
Available CLI options
The SDK leverages all the CLI options available in Claude Code. Here are the key ones for SDK usage:
Flag| Description| Example  
---|---|---  
`--print`, `-p`| Run in non-interactive mode| `claude -p "query"`  
`--output-format`| Specify output format (`text`, `json`, `stream-json`)| `claude -p --output-format json`  
`--resume`, `-r`| Resume a conversation by session ID| `claude --resume abc123`  
`--continue`, `-c`| Continue the most recent conversation| `claude --continue`  
`--verbose`| Enable verbose logging| `claude --verbose`  
`--max-turns`| Limit agentic turns in non-interactive mode| `claude --max-turns 3`  
`--system-prompt`| Override system prompt (only with `--print`)| `claude --system-prompt "Custom instruction"`  
`--append-system-prompt`| Append to system prompt (only with `--print`)| `claude --append-system-prompt "Custom instruction"`  
`--allowedTools`| Comma/space-separated list of allowed tools (includes MCP tools)| `claude --allowedTools "Bash(npm install),mcp__filesystem__*"`  
`--disallowedTools`| Comma/space-separated list of denied tools| `claude --disallowedTools "Bash(git commit),mcp__github__*"`  
`--mcp-config`| Load MCP servers from a JSON file| `claude --mcp-config servers.json`  
`--permission-prompt-tool`| MCP tool for handling permission prompts (only with `--print`)| `claude --permission-prompt-tool mcp__auth__prompt`  
For a complete list of CLI options and features, see the [CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage) documentation.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#output-formats)
Output formats
The SDK supports multiple output formats:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#text-output-default)
Text output (default)
Returns just the response text:
Copy
```
$ claude -p "Explain file src/components/Header.tsx"
# Output: This is a React component showing...

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#json-output)
JSON output
Returns structured data including metadata:
Copy
```
$ claude -p "How does the data layer work?" --output-format json

```

Response format:
Copy
```
{
 "type": "result",
 "subtype": "success",
 "cost_usd": 0.003,
 "is_error": false,
 "duration_ms": 1234,
 "duration_api_ms": 800,
 "num_turns": 6,
 "result": "The response text here...",
 "session_id": "abc123"
}

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#streaming-json-output)
Streaming JSON output
Streams each message as it is received:
Copy
```
$ claude -p "Build an application" --output-format stream-json

```

Each conversation begins with an initial `init` system message, followed by a list of user and assistant messages, followed by a final `result` system message with stats. Each message is emitted as a separate JSON object.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#message-schema)
Message schema
Messages returned from the JSON API are strictly typed according to the following schema:
Copy
```
type Message =
 // An assistant message
 | {
   type: "assistant";
   message: APIAssistantMessage; // from Anthropic SDK
   session_id: string;
  }
 // A user message
 | {
   type: "user";
   message: APIUserMessage; // from Anthropic SDK
   session_id: string;
  }
 // Emitted as the last message
 | {
   type: "result";
   subtype: "success";
   cost_usd: float;
   duration_ms: float;
   duration_api_ms: float;
   is_error: boolean;
   num_turns: int;
   result: string;
   session_id: string;
  }
 // Emitted as the last message, when we've reached the maximum number of turns
 | {
   type: "result";
   subtype: "error_max_turns";
   cost_usd: float;
   duration_ms: float;
   duration_api_ms: float;
   is_error: boolean;
   num_turns: int;
   session_id: string;
  }
 // Emitted as the first message at the start of a conversation
 | {
   type: "system";
   subtype: "init";
   session_id: string;
   tools: string[];
   mcp_servers: {
    name: string;
    status: string;
   }[];
  };

```

We will soon publish these types in a JSONSchema-compatible format. We use semantic versioning for the main Claude Code package to communicate breaking changes to this format.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#examples)
Examples
### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#simple-script-integration)
Simple script integration
Copy
```
#!/bin/bash
# Simple function to run Claude and check exit code
run_claude() {
  local prompt="$1"
  local output_format="${2:-text}"
  if claude -p "$prompt" --output-format "$output_format"; then
    echo "Success!"
  else
    echo "Error: Claude failed with exit code $?" >&2
    return 1
  fi
}
# Usage examples
run_claude "Write a Python function to read CSV files"
run_claude "Optimize this database query" "json"

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#processing-files-with-claude)
Processing files with Claude
Copy
```
# Process a file through Claude
$ cat mycode.py | claude -p "Review this code for bugs"
# Process multiple files
$ for file in *.js; do
  echo "Processing $file..."
  claude -p "Add JSDoc comments to this file:" < "$file" > "${file}.documented"
done
# Use Claude in a pipeline
$ grep -l "TODO" *.py | while read file; do
  claude -p "Fix all TODO items in this file" < "$file"
done

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#session-management)
Session management
Copy
```
# Start a session and capture the session ID
$ claude -p "Initialize a new project" --output-format json | jq -r '.session_id' > session.txt
# Continue with the same session
$ claude -p --resume "$(cat session.txt)" "Add unit tests"

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#best-practices)
Best practices
  1. **Use JSON output format** for programmatic parsing of responses:
Copy
```
# Parse JSON response with jq
result=$(claude -p "Generate code" --output-format json)
code=$(echo "$result" | jq -r '.result')
cost=$(echo "$result" | jq -r '.cost_usd')

```

  2. **Handle errors gracefully** - check exit codes and stderr:
Copy
```
if ! claude -p "$prompt" 2>error.log; then
  echo "Error occurred:" >&2
  cat error.log >&2
  exit 1
fi

```

  3. **Use session management** for maintaining context in multi-turn conversations
  4. **Consider timeouts** for long-running operations:
Copy
```
timeout 300 claude -p "$complex_prompt" || echo "Timed out after 5 minutes"

```

  5. **Respect rate limits** when making multiple requests by adding delays between calls


## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#real-world-applications)
Real-world applications
The Claude Code SDK enables powerful integrations with your development workflow. One notable example is the [Claude Code GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions), which uses the SDK to provide automated code review, PR creation, and issue triage capabilities directly in your GitHub workflow.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/sdk#related-resources)
Related resources
  * [CLI usage and controls](https://docs.anthropic.com/en/docs/claude-code/cli-usage) - Complete CLI documentation
  * [GitHub Actions integration](https://docs.anthropic.com/en/docs/claude-code/github-actions) - Automate your GitHub workflow with Claude
  * [Tutorials](https://docs.anthropic.com/en/docs/claude-code/tutorials) - Step-by-step guides for common use cases


Was this page helpful?
YesNo
[GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)[Tutorials](https://docs.anthropic.com/en/docs/claude-code/tutorials)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Basic SDK usage](https://docs.anthropic.com/en/docs/claude-code/sdk#basic-sdk-usage)
  * [Advanced usage](https://docs.anthropic.com/en/docs/claude-code/sdk#advanced-usage)
  * [Multi-turn conversations](https://docs.anthropic.com/en/docs/claude-code/sdk#multi-turn-conversations)
  * [Custom system prompts](https://docs.anthropic.com/en/docs/claude-code/sdk#custom-system-prompts)
  * [MCP Configuration](https://docs.anthropic.com/en/docs/claude-code/sdk#mcp-configuration)
  * [Available CLI options](https://docs.anthropic.com/en/docs/claude-code/sdk#available-cli-options)
  * [Output formats](https://docs.anthropic.com/en/docs/claude-code/sdk#output-formats)
  * [Text output (default)](https://docs.anthropic.com/en/docs/claude-code/sdk#text-output-default)
  * [JSON output](https://docs.anthropic.com/en/docs/claude-code/sdk#json-output)
  * [Streaming JSON output](https://docs.anthropic.com/en/docs/claude-code/sdk#streaming-json-output)
  * [Message schema](https://docs.anthropic.com/en/docs/claude-code/sdk#message-schema)
  * [Examples](https://docs.anthropic.com/en/docs/claude-code/sdk#examples)
  * [Simple script integration](https://docs.anthropic.com/en/docs/claude-code/sdk#simple-script-integration)
  * [Processing files with Claude](https://docs.anthropic.com/en/docs/claude-code/sdk#processing-files-with-claude)
  * [Session management](https://docs.anthropic.com/en/docs/claude-code/sdk#session-management)
  * [Best practices](https://docs.anthropic.com/en/docs/claude-code/sdk#best-practices)
  * [Real-world applications](https://docs.anthropic.com/en/docs/claude-code/sdk#real-world-applications)
  * [Related resources](https://docs.anthropic.com/en/docs/claude-code/sdk#related-resources)



