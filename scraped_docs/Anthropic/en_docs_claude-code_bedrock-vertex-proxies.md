---
url: https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies
scraped_at: 2025-05-24T19:54:16.194520
title: Bedrock, Vertex, and proxies - Anthropic
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
Bedrock, Vertex, and proxies
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
# Bedrock, Vertex, and proxies
Configure Claude Code to work with Amazon Bedrock and Google Vertex AI, and connect through proxies.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#model-configuration)
Model configuration
Claude Code uses the following defaults:
Provider| Default Model  
---|---  
Anthropic Console| `claude-sonnet-4-20250514`  
Claude Max| `claude-opus-4-20250514` or `claude-sonnet-4-20250514` based on Max usage limits  
Amazon Bedrock| `claude-3-7-sonnet-20250219`  
Google Vertex AI| `claude-sonnet-4-20250514`  
The default values can be overridden in several ways based on the following precedence from top to bottom:
  * `--model` CLI flag. Applies within the session only.
  * `ANTHROPIC_MODEL` environment variable. Applies within the session only.
  * User Settings `~/.claude/settings.json`: Persists across sessions.


Copy
```
claude --model sonnet

```

Copy
```
# Anthropic API
ANTHROPIC_MODEL='claude-opus-4-20250514'
ANTHROPIC_SMALL_FAST_MODEL='claude-3-5-haiku-20241022'
# Amazon Bedrock (with model ID)
ANTHROPIC_MODEL='us.anthropic.claude-opus-4-20250514-v1:0'
ANTHROPIC_SMALL_FAST_MODEL='us.anthropic.claude-3-5-haiku-20241022-v1:0'
# Amazon Bedrock (with inference profile ARN)
ANTHROPIC_MODEL='arn:aws:bedrock:us-east-2:your-account-id:application-inference-profile/your-model-id'
ANTHROPIC_SMALL_FAST_MODEL='arn:aws:bedrock:us-east-2:your-account-id:application-inference-profile/your-small-model-id'
# Google Vertex AI
ANTHROPIC_MODEL='claude-3-7-sonnet@20250219'
ANTHROPIC_SMALL_FAST_MODEL='claude-3-5-haiku@20241022'

```

Copy
```
{
 "permissions": {
  ...
 },
 "model": "sonnet"
}

```

You can supply a full model name, the alias `sonnet` for the latest Claude Sonnet model for your provider, or the alias `opus` for the latest Claude Opus model for your provider.
See our [model names reference](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-names) for all available models across different providers.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#use-with-third-party-apis)
Use with third-party APIs
Claude Code requires access to both Claude Sonnet 3.7 and Claude Haiku 3.5 models, regardless of which API provider you use.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#connect-to-amazon-bedrock)
Connect to Amazon Bedrock
Copy
```
CLAUDE_CODE_USE_BEDROCK=1

```

If you don’t have prompt caching enabled, also set:
Copy
```
DISABLE_PROMPT_CACHING=1

```

Contact Amazon Bedrock for prompt caching for reduced costs and higher rate limits.
Requires standard AWS SDK credentials (e.g., `~/.aws/credentials` or relevant environment variables like `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`). To set up AWS credentials, run:
Copy
```
aws configure

```

If you’d like to access Claude Code via proxy, you can use the `ANTHROPIC_BEDROCK_BASE_URL` environment variable:
Copy
```
ANTHROPIC_BEDROCK_BASE_URL='https://your-proxy-url'

```

If your proxy maintains its own AWS credentials, you can use the `CLAUDE_CODE_SKIP_BEDROCK_AUTH` environment variable to remove Claude Code’s requirement for AWS credentials.
Copy
```
CLAUDE_CODE_SKIP_BEDROCK_AUTH=1

```

Users will need access to both Claude Sonnet 3.7 and Claude Haiku 3.5 models in their AWS account. If you have a model access role, you may need to request access to these models if they’re not already available. Access to Bedrock in each region is necessary because inference profiles require cross-region capability.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#connect-to-google-vertex-ai)
Connect to Google Vertex AI
Copy
```
CLAUDE_CODE_USE_VERTEX=1
CLOUD_ML_REGION=us-east5
ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

```

If you don’t have prompt caching enabled, also set:
Copy
```
DISABLE_PROMPT_CACHING=1

```

Claude Code on Vertex AI currently only supports the `us-east5` region. Make sure your project has quota allocated in this specific region.
Users will need access to both Claude Sonnet 3.7 and Claude Haiku 3.5 models in their Vertex AI project.
Requires standard GCP credentials configured through google-auth-library. To set up GCP credentials, run:
Copy
```
gcloud auth application-default login

```

If you’d like to access Claude Code via proxy, you can use the `ANTHROPIC_VERTEX_BASE_URL` environment variable:
Copy
```
ANTHROPIC_VERTEX_BASE_URL='https://your-proxy-url'

```

If your proxy maintains its own GCP credentials, you can use the `CLAUDE_CODE_SKIP_VERTEX_AUTH` environment variable to remove Claude Code’s requirement for GCP credentials.
Copy
```
CLAUDE_CODE_SKIP_VERTEX_AUTH=1

```

For the best experience, contact Google for heightened rate limits.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#connect-through-a-proxy)
Connect through a proxy
When using Claude Code with an LLM proxy, you can control authentication behavior using the following environment variables and configs. Note that you can mix and match these with Bedrock and Vertex-specific settings.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#settings)
Settings
Claude Code supports a number of settings controlled via environment variables to configure usage with Bedrock and Vertex. See [Environment variables](https://docs.anthropic.com/en/docs/claude-code/settings#environment-variables) for a complete reference.
If you prefer to configure via a file instead of environment variables, you can add any of these settings to the `env` object in your [Claude Code settings](https://docs.anthropic.com/en/docs/claude-code/settings#available-settings) files.
You can also configure the `apiKeyHelper` setting, to set a custom shell script to get an API key (invoked once at startup, and cached for the duration of each session, or until `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` elapses).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#litellm)
LiteLLM
LiteLLM is a third-party proxy service. Anthropic doesn’t endorse, maintain, or audit LiteLLM’s security or functionality. This guide is provided for informational purposes and may become outdated. Use at your own discretion.
This section shows configuration of Claude Code with LiteLLM Proxy Server, a third-party LLM proxy which offers usage and spend tracking, centralized authentication, per-user budgeting, and more.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#step-1%3A-prerequisites)
Step 1: Prerequisites
  * Claude Code updated to the latest version
  * LiteLLM Proxy Server running and network-accessible to Claude Code
  * Your LiteLLM proxy key


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#step-2%3A-set-up-proxy-authentication)
Step 2: Set up proxy authentication
Choose one of these authentication methods:
**Option A: Static proxy key** Set your proxy key as an environment variable:
Copy
```
ANTHROPIC_AUTH_TOKEN=your-proxy-key

```

**Option B: Dynamic proxy key** If your organization uses rotating keys or dynamic authentication:
  1. Do not set the `ANTHROPIC_AUTH_TOKEN` environment variable
  2. Author a key helper script to provide authentication tokens
  3. Register the script under `apiKeyHelper` configuration in your Claude Code settings
  4. Set the token lifetime to enable automatic refresh: 
Copy
```
CLAUDE_CODE_API_KEY_HELPER_TTL_MS=3600000

```

Set this to the lifetime (in milliseconds) of tokens returned by your `apiKeyHelper`.


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#step-3%3A-configure-your-deployment)
Step 3: Configure your deployment
Choose which Claude deployment you want to use through LiteLLM:
  * **Anthropic API** : Direct connection to Anthropic’s API
  * **Bedrock** : Amazon Bedrock with Claude models
  * **Vertex AI** : Google Cloud Vertex AI with Claude models


##### Option A: Anthropic API through LiteLLM
  1. Configure the LiteLLM endpoint: 
Copy
```
ANTHROPIC_BASE_URL=https://litellm-url:4000/anthropic

```



##### Option B: Bedrock through LiteLLM
  1. Configure Bedrock settings: 
Copy
```
ANTHROPIC_BEDROCK_BASE_URL=https://litellm-url:4000/bedrock
CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
CLAUDE_CODE_USE_BEDROCK=1

```



##### Option C: Vertex AI through LiteLLM
**Recommended: Proxy-specified credentials**
  1. Configure Vertex settings: 
Copy
```
ANTHROPIC_VERTEX_BASE_URL=https://litellm-url:4000/vertex_ai/v1
CLAUDE_CODE_SKIP_VERTEX_AUTH=1
CLAUDE_CODE_USE_VERTEX=1

```



**Alternative: Client-specified credentials**
If you prefer to use local GCP credentials:
  1. Authenticate with GCP locally:
Copy
```
gcloud auth application-default login

```

  2. Configure Vertex settings:
Copy
```
ANTHROPIC_VERTEX_BASE_URL=https://litellm-url:4000/vertex_ai/v1
ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
CLAUDE_CODE_USE_VERTEX=1
CLOUD_ML_REGION=your-gcp-region

```

  3. Update LiteLLM header configuration:
Ensure your LiteLLM config has `general_settings.litellm_key_header_name` set to `Proxy-Authorization`, since the pass-through GCP token will be located on the `Authorization` header.


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#step-4-selecting-a-model)
Step 4. Selecting a model
By default, the models will use those specified in [Model configuration](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#model-configuration).
If you have configured custom model names in LiteLLM, set the aforementioned environment variables to those custom names.
For more detailed information, refer to the [LiteLLM documentation](https://docs.litellm.ai/).
Was this page helpful?
YesNo
[Costs](https://docs.anthropic.com/en/docs/claude-code/costs)[GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Model configuration](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#model-configuration)
  * [Use with third-party APIs](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#use-with-third-party-apis)
  * [Connect to Amazon Bedrock](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#connect-to-amazon-bedrock)
  * [Connect to Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#connect-to-google-vertex-ai)
  * [Connect through a proxy](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#connect-through-a-proxy)
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#settings)
  * [LiteLLM](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#litellm)
  * [Step 1: Prerequisites](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#step-1%3A-prerequisites)
  * [Step 2: Set up proxy authentication](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#step-2%3A-set-up-proxy-authentication)
  * [Step 3: Configure your deployment](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#step-3%3A-configure-your-deployment)
  * [Step 4. Selecting a model](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies#step-4-selecting-a-model)



