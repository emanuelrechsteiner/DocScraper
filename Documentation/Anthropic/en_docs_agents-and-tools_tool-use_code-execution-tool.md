---
url: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool
scraped_at: 2025-05-24T19:40:26.698661
title: Code execution tool - Anthropic
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
Code execution tool
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
# Code execution tool
The code execution tool allows Claude to execute Python code in a secure, sandboxed environment. Claude can analyze data, create visualizations, perform complex calculations, and process uploaded files directly within the API conversation.
This feature requires the [beta header](https://docs.anthropic.com/en/api/beta-headers): `"anthropic-beta": "code-execution-2025-05-22"`
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#supported-models)
Supported models
The code execution tool is available on:
  * Claude Opus 4 (`claude-opus-4-20250514`)
  * Claude Sonnet 4 (`claude-sonnet-4-20250514`)
  * Claude Sonnet 3.7 (`claude-3-7-sonnet-20250219`)
  * Claude Haiku 3.5 (`claude-3-5-haiku-latest`)


## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#quick-start)
Quick start
Here’s a simple example that asks Claude to perform a calculation:
Shell
Python
TypeScript
Copy
```
curl https://api.anthropic.com/v1/messages \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "anthropic-beta: code-execution-2025-05-22" \
  --header "content-type: application/json" \
  --data '{
    "model": "claude-opus-4-20250514",
    "max_tokens": 4096,
    "messages": [
      {
        "role": "user",
        "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      }
    ],
    "tools": [{
      "type": "code_execution_20250522",
      "name": "code_execution"
    }]
  }'

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#how-code-execution-works)
How code execution works
When you add the code execution tool to your API request:
  1. Claude evaluates whether code execution would help answer your question
  2. Claude writes and executes Python code in a secure sandbox environment
  3. Code execution may occur multiple times throughout a single request
  4. Claude provides results with any generated charts, calculations, or analysis


## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#tool-definition)
Tool definition
The code execution tool requires no additional parameters:
JSON
Copy
```
{
 "type": "code_execution_20250522",
 "name": "code_execution"
}

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#response-format)
Response format
Here’s an example response with code execution:
Copy
```
{
 "role": "assistant",
 "content": [
  {
   "type": "text",
   "text": "I'll calculate the mean and standard deviation for you."
  },
  {
   "type": "server_tool_use",
   "id": "srvtoolu_01A2B3C4D5E6F7G8H9I0J1K2",
   "name": "code_execution",
   "input": {
    "code": "import numpy as np\ndata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nmean = np.mean(data)\nstd = np.std(data)\nprint(f\"Mean: {mean}\")\nprint(f\"Standard deviation: {std}\")"
   }
  },
  {
   "type": "code_execution_tool_result",
   "tool_use_id": "srvtoolu_01A2B3C4D5E6F7G8H9I0J1K2",
   "content": {
    "type": "code_execution_result",
    "stdout": "Mean: 5.5\nStandard deviation: 2.8722813232690143\n",
    "stderr": "",
    "return_code": 0
   }
  },
  {
   "type": "text",
   "text": "The mean of the dataset is 5.5 and the standard deviation is approximately 2.87."
  }
 ],
 "id": "msg_01BqK2v4FnRs4xTjgL8EuZxz",
 "model": "claude-opus-4-20250514",
 "stop_reason": "end_turn",
 "usage": {
  "input_tokens": 45,
  "output_tokens": 187,
  "server_tool_use": {
   "execution_time_seconds": 1.5
  }
 }
}

```

### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#results)
Results
Code execution results include:
  * `stdout`: Output from print statements and successful execution
  * `stderr`: Error messages if code execution fails
  * `return_code` (0 for success, non-zero for failure)


Copy
```
{
 "type": "code_execution_tool_result",
 "tool_use_id": "srvtoolu_01ABC123",
 "content": {
  "type": "code_execution_result",
  "stdout": "",
  "stderr": "NameError: name 'undefined_variable' is not defined",
  "return_code": 1
 }
}

```

### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#errors)
Errors
If there is an error using the tool there will be a `code_execution_tool_result_error`
Copy
```
{
 "type": "code_execution_tool_result",
 "tool_use_id": "srvtoolu_01VfmxgZ46TiHbmXgy928hQR",
 "content": {
  "type": "code_execution_tool_result_error",
  "error_code": "unavailable"
 }
}

```

Possible errors include
  * `unavailable`: The code execution tool is unavailable
  * `code_execution_exceeded`: Execution time exceeded the maximum allowed
  * `container_expired`: The container is expired and not available


#### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#pause-turn-stop-reason)
`pause_turn` stop reason
The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation.
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#containers)
Containers
The code execution tool runs in a secure, containerized environment designed specifically for Python code execution.
### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#runtime-environment)
Runtime environment
  * **Python version** : 3.11.12
  * **Operating system** : Linux-based container
  * **Architecture** : x86_64 (AMD64)


### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#resource-limits)
Resource limits
  * **Memory** : 1GiB RAM
  * **Disk space** : 5GiB workspace storage
  * **CPU** : 1 CPU
  * **Execution timeout** : Execution is limited per messages request and can be controlled with the `max_execution_duration` parameter
  * **Container Expiration** : After 1 hour of inactivity, the container can’t be accessed again


### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#networking-and-security)
Networking and security
  * **Internet access** : Completely disabled for security
  * **External connections** : No outbound network requests permitted
  * **Sandbox isolation** : Full isolation from host system and other containers
  * **File access** : Limited to workspace directory only


### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#pre-installed-libraries)
Pre-installed libraries
The sandboxed Python environment includes these commonly used libraries:
  * **Data Science** : pandas, numpy, scipy, scikit-learn, statsmodels
  * **Visualization** : matplotlib, seaborn
  * **File Processing** : pyarrow, openpyxl, xlrd, pillow
  * **Math & Computing**: sympy, mpmath
  * **Utilities** : tqdm, python-dateutil, pytz, joblib


## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#working-with-files-in-code-execution)
Working with Files in Code Execution
Code execution can analyze files uploaded via the Files API, such as CSV files, Excel files, and other data formats. This allows Claude to read, process, and generate insights from your data.
Using the Files API with Code Execution requires two beta headers: `"anthropic-beta": "code-execution-2025-05-22,files-api-2025-04-14"`
### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#supported-file-types)
Supported file types
The Python environment is capable of working with but not limited to the following file types
  * CSV
  * Excel (.xlsx, .xls)
  * JSON
  * XML
  * Images (JPEG, PNG, GIF, WebP)
  * Text files (.txt, .md, .py, etc)


### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#example)
Example
  1. **Upload your file** using the [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files)
  2. **Reference the file** in your message using a `container_upload` content block
  3. **Include the code execution tool** in your API request


Shell
Python
TypeScript
Copy
```
# First, upload a file
curl https://api.anthropic.com/v1/files \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "anthropic-beta: files-api-2025-04-14" \
  --form 'file=@"data.csv"' \
# Then use the file_id with code execution
curl https://api.anthropic.com/v1/messages \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "anthropic-beta: code-execution-2025-05-22,files-api-2025-04-14" \
  --header "content-type: application/json" \
  --data '{
    "model": "claude-opus-4-20250514",
    "max_tokens": 4096,
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "Analyze this CSV data"},
        {"type": "container_upload", "file_id": "file_abc123"}
      ]
    }],
    "tools": [{
      "type": "code_execution_20250522",
      "name": "code_execution"
    }]
  }'

```

### 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#retrieving-files-created-by-code-execution)
Retrieving files created by code execution
When Claude creates files during code execution (e.g., saving matplotlib plots, generating CSVs), you can retrieve these files using the Files API:
Python
TypeScript
Copy
```
from anthropic import Anthropic
# Initialize with both beta headers
client = Anthropic(
  default_headers={
    "anthropic-beta": "code-execution-2025-05-22,files-api-2025-04-14"
  }
)
# Request code execution that creates files
response = client.messages.create(
  model="claude-opus-4-20250514",
  max_tokens=4096,
  messages=[{
    "role": "user",
    "content": "Create a matplotlib visualization and save it as output.png"
  }],
  tools=[{
    "type": "code_execution_20250522",
    "name": "code_execution"
  }]
)
# Extract file IDs from the response
def extract_file_ids(response):
  file_ids = []
  for item in response.content:
    if item.type == 'code_execution_tool_result':
      content_item = item.content
      if content_item.get('type') == 'code_execution_result':
        for file in content_item.get('content', []):
          file_ids.append(file['file_id'])
  return file_ids
# Download the created files
for file_id in extract_file_ids(response):
  file_metadata = client.beta.files.retrieve_metadata(file_id)
  file_content = client.beta.files.download(file_id)
  file_content.write_to_file(file_metadata.filename)
  print(f"Downloaded: {file_metadata.filename}")

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#streaming)
Streaming
With streaming enabled, you’ll receive code execution events as they occur:
Copy
```
event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "code_execution"}}
// Code execution streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"code\":\"import pandas as pd\\ndf = pd.read_csv('data.csv')\\nprint(df.head())\"}"}}
// Pause while code executes
// Execution results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "code_execution_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"stdout": "  A B C\n0 1 2 3\n1 4 5 6", "stderr": ""}}}

```

## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#batch-requests)
Batch requests
You can include the code execution tool in the [Messages Batches API](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing). Code execution tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.
## 
[​](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#usage-and-pricing)
Usage and pricing
The code execution tool usage is tracked separately from token usage. Execution time is a minimum of 5 minutes. If files are included in the request, execution time is billed even if the tool is not used due to files being preloaded onto the container.
**Pricing** : $0.05 per session-hour.
Was this page helpful?
YesNo
[Web search tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool)[MCP overview](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Supported models](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#supported-models)
  * [Quick start](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#quick-start)
  * [How code execution works](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#how-code-execution-works)
  * [Tool definition](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#tool-definition)
  * [Response format](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#response-format)
  * [Results](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#results)
  * [Errors](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#errors)
  * [pause_turn stop reason](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#pause-turn-stop-reason)
  * [Containers](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#containers)
  * [Runtime environment](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#runtime-environment)
  * [Resource limits](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#resource-limits)
  * [Networking and security](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#networking-and-security)
  * [Pre-installed libraries](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#pre-installed-libraries)
  * [Working with Files in Code Execution](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#working-with-files-in-code-execution)
  * [Supported file types](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#supported-file-types)
  * [Example](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#example)
  * [Retrieving files created by code execution](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#retrieving-files-created-by-code-execution)
  * [Streaming](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#streaming)
  * [Batch requests](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#batch-requests)
  * [Usage and pricing](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool#usage-and-pricing)



