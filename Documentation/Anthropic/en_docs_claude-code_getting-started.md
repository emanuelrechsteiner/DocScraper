---
url: https://docs.anthropic.com/en/docs/claude-code/getting-started
scraped_at: 2025-05-24T19:39:51.995759
title: Getting started with Claude Code - Anthropic
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
Getting started with Claude Code
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
# Getting started with Claude Code
Learn how to install, authenticate, and start using Claude Code.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/getting-started#check-system-requirements)
Check system requirements
  * **Operating Systems** : macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows via WSL
  * **Hardware** : 4GB RAM minimum
  * **Software** : 
    * Node.js 18+
    * [git](https://git-scm.com/downloads) 2.23+ (optional)
    * [GitHub](https://cli.github.com/) or [GitLab](https://gitlab.com/gitlab-org/cli) CLI for PR workflows (optional)
    * [ripgrep](https://github.com/BurntSushi/ripgrep?tab=readme-ov-file#installation) (rg) for enhanced file search (optional)
  * **Network** : Internet connection required for authentication and AI processing
  * **Location** : Available only in [supported countries](https://www.anthropic.com/supported-countries)


**Troubleshooting WSL installation**
Currently, Claude Code does not run directly in Windows, and instead requires WSL. If you encounter issues in WSL:
  1. **OS/platform detection issues** : If you receive an error during installation, WSL may be using Windows `npm`. Try:
     * Run `npm config set os linux` before installation
     * Install with `npm install -g @anthropic-ai/claude-code --force --no-os-check` (Do NOT use `sudo`)
  2. **Node not found errors** : If you see `exec: node: not found` when running `claude`, your WSL environment may be using a Windows installation of Node.js. You can confirm this with `which npm` and `which node`, which should point to Linux paths starting with `/usr/` rather than `/mnt/c/`. To fix this, try installing Node via your Linux distribution’s package manager or via [`nvm`](https://github.com/nvm-sh/nvm).


## 
[​](https://docs.anthropic.com/en/docs/claude-code/getting-started#install-and-authenticate)
Install and authenticate
1
Install Claude Code
Install [NodeJS 18+](https://nodejs.org/en/download), then run:
Copy
```
npm install -g @anthropic-ai/claude-code

```

Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks. If you encounter permission errors, see [configure Claude Code](https://docs.anthropic.com/en/docs/claude-code/configuration#auto-updater-permission-options) for recommended solutions.
2
Navigate to your project
Copy
```
cd your-project-directory 

```

3
Start Claude Code
Copy
```
claude

```

4
Complete authentication
Claude Code offers multiple authentication options:
  1. **Anthropic Console** : The default option. Connect through the Anthropic Console and complete the OAuth process. Requires active billing at [console.anthropic.com](https://console.anthropic.com).
  2. **Claude App (with Max plan)** : Subscribe to Claude’s [Max plan](https://www.anthropic.com/pricing) for a single subscription that includes both Claude Code and the web interface. Get more value at the same price point while managing your account in one place. Log in with your Claude.ai account. During launch, choose the option that matches your subscription type.
  3. **Enterprise platforms** : Configure Claude Code to use [Amazon Bedrock or Google Vertex AI](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies) for enterprise deployments with your existing cloud infrastructure.


## 
[​](https://docs.anthropic.com/en/docs/claude-code/getting-started#initialize-your-project)
Initialize your project
For first-time users, we recommend:
1
Start Claude Code
Copy
```
claude

```

2
Run a simple command
Copy
```
summarize this project

```

3
Generate a CLAUDE.md project guide
Copy
```
/init 

```

4
Commit the generated CLAUDE.md file
Ask Claude to commit the generated CLAUDE.md file to your repository.
Was this page helpful?
YesNo
[Overview](https://docs.anthropic.com/en/docs/claude-code/overview)[Common tasks](https://docs.anthropic.com/en/docs/claude-code/common-tasks)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Check system requirements](https://docs.anthropic.com/en/docs/claude-code/getting-started#check-system-requirements)
  * [Install and authenticate](https://docs.anthropic.com/en/docs/claude-code/getting-started#install-and-authenticate)
  * [Initialize your project](https://docs.anthropic.com/en/docs/claude-code/getting-started#initialize-your-project)



