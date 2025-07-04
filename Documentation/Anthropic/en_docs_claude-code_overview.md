---
url: https://docs.anthropic.com/en/docs/claude-code/overview
scraped_at: 2025-05-24T19:37:42.259517
title: Claude Code overview - Anthropic
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
Claude Code overview
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
# Claude Code overview
Learn about Claude Code, an agentic coding tool made by Anthropic.
Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster through natural language commands. By integrating directly with your development environment, Claude Code streamlines your workflow without requiring additional servers or complex setup.
Copy
```
npm install -g @anthropic-ai/claude-code

```

Claude Code’s key capabilities include:
  * Editing files and fixing bugs across your codebase
  * Answering questions about your code’s architecture and logic
  * Executing and fixing tests, linting, and other commands
  * Searching through git history, resolving merge conflicts, and creating commits and PRs
  * Browsing documentation and resources from the internet using web search
  * Works with [Amazon Bedrock and Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies) for enterprise deployments


## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#why-claude-code%3F)
Why Claude Code?
Claude Code operates directly in your terminal, understanding your project context and taking real actions. No need to manually add files to context - Claude will explore your codebase as needed.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#enterprise-integration)
Enterprise integration
Claude Code seamlessly integrates with enterprise AI platforms. You can connect to [Amazon Bedrock or Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies) for secure, compliant deployments that meet your organization’s requirements.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#security-and-privacy-by-design)
Security and privacy by design
Your code’s security is paramount. Claude Code’s architecture ensures:
  * **Direct API connection** : Your queries go straight to Anthropic’s API without intermediate servers
  * **Works where you work** : Operates directly in your terminal
  * **Understands context** : Maintains awareness of your entire project structure
  * **Takes action** : Performs real operations like editing files and creating commits


## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#getting-started)
Getting started
To get started with Claude Code, follow our [installation guide](https://docs.anthropic.com/en/docs/claude-code/getting-started) which covers system requirements, installation steps, and authentication process.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#quick-tour)
Quick tour
Here’s what you can accomplish with Claude Code:
### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#from-questions-to-solutions-in-seconds)
From questions to solutions in seconds
Copy
```
# Ask questions about your codebase
claude
> how does our authentication system work?
# Create a commit with one command
claude commit
# Fix issues across multiple files
claude "fix the type errors in the auth module"

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#understand-unfamiliar-code)
Understand unfamiliar code
Copy
```
> what does the payment processing system do?
> find where user permissions are checked
> explain how the caching layer works

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#automate-git-operations)
Automate Git operations
Copy
```
> commit my changes
> create a pr
> which commit added tests for markdown back in December?
> rebase on main and resolve any merge conflicts

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#next-steps)
Next steps
## [Getting startedInstall Claude Code and get up and running](https://docs.anthropic.com/en/docs/claude-code/getting-started)## [Core featuresExplore what Claude Code can do for you](https://docs.anthropic.com/en/docs/claude-code/common-tasks)## [CommandsLearn about CLI commands and controls](https://docs.anthropic.com/en/docs/claude-code/cli-usage)## [ConfigurationCustomize Claude Code for your workflow](https://docs.anthropic.com/en/docs/claude-code/settings)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#additional-resources)
Additional resources
## [Claude Code tutorialsStep-by-step guides for common tasks](https://docs.anthropic.com/en/docs/claude-code/tutorials)## [TroubleshootingSolutions for common issues with Claude Code](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)## [Bedrock & Vertex integrationsConfigure Claude Code with Amazon Bedrock or Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies)## [Reference implementationClone our development container reference implementation.](https://github.com/anthropics/claude-code/tree/main/.devcontainer)
## 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#license-and-data-usage)
License and data usage
Claude Code is provided under Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#how-we-use-your-data)
How we use your data
We aim to be fully transparent about how we use your data. We may use feedback to improve our products and services, but we will not train generative models using your feedback from Claude Code. Given their potentially sensitive nature, we store user feedback transcripts for only 30 days.
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#feedback-transcripts)
Feedback transcripts
If you choose to send us feedback about Claude Code, such as transcripts of your usage, Anthropic may use that feedback to debug related issues and improve Claude Code’s functionality (e.g., to reduce the risk of similar bugs occurring in the future). We will not train generative models using this feedback.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#privacy-safeguards)
Privacy safeguards
We have implemented several safeguards to protect your data, including limited retention periods for sensitive information, restricted access to user session data, and clear policies against using feedback for model training.
For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Privacy Policy](https://www.anthropic.com/legal/privacy).
### 
[​](https://docs.anthropic.com/en/docs/claude-code/overview#license)
License
© Anthropic PBC. All rights reserved. Use is subject to Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).
Was this page helpful?
YesNo
[Getting started](https://docs.anthropic.com/en/docs/claude-code/getting-started)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Why Claude Code?](https://docs.anthropic.com/en/docs/claude-code/overview#why-claude-code%3F)
  * [Enterprise integration](https://docs.anthropic.com/en/docs/claude-code/overview#enterprise-integration)
  * [Security and privacy by design](https://docs.anthropic.com/en/docs/claude-code/overview#security-and-privacy-by-design)
  * [Getting started](https://docs.anthropic.com/en/docs/claude-code/overview#getting-started)
  * [Quick tour](https://docs.anthropic.com/en/docs/claude-code/overview#quick-tour)
  * [From questions to solutions in seconds](https://docs.anthropic.com/en/docs/claude-code/overview#from-questions-to-solutions-in-seconds)
  * [Understand unfamiliar code](https://docs.anthropic.com/en/docs/claude-code/overview#understand-unfamiliar-code)
  * [Automate Git operations](https://docs.anthropic.com/en/docs/claude-code/overview#automate-git-operations)
  * [Next steps](https://docs.anthropic.com/en/docs/claude-code/overview#next-steps)
  * [Additional resources](https://docs.anthropic.com/en/docs/claude-code/overview#additional-resources)
  * [License and data usage](https://docs.anthropic.com/en/docs/claude-code/overview#license-and-data-usage)
  * [How we use your data](https://docs.anthropic.com/en/docs/claude-code/overview#how-we-use-your-data)
  * [Feedback transcripts](https://docs.anthropic.com/en/docs/claude-code/overview#feedback-transcripts)
  * [Privacy safeguards](https://docs.anthropic.com/en/docs/claude-code/overview#privacy-safeguards)
  * [License](https://docs.anthropic.com/en/docs/claude-code/overview#license)



