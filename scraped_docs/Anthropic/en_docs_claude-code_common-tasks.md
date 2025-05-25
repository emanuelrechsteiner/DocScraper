---
url: https://docs.anthropic.com/en/docs/claude-code/common-tasks
scraped_at: 2025-05-24T19:47:09.323656
title: Core tasks and workflows - Anthropic
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
Core tasks and workflows
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
# Core tasks and workflows
Explore Claude Code’s powerful features for editing, searching, testing, and automating your development workflow.
Claude Code operates directly in your terminal, understanding your project context and taking real actions. No need to manually add files to context - Claude will explore your codebase as needed.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-tasks#understand-unfamiliar-code)
Understand unfamiliar code
Copy
```
> what does the payment processing system do?
> find where user permissions are checked
> explain how the caching layer works

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-tasks#automate-git-operations)
Automate Git operations
Copy
```
> commit my changes
> create a pr
> which commit added tests for markdown back in December?
> rebase on main and resolve any merge conflicts

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-tasks#edit-code-intelligently)
Edit code intelligently
Copy
```
> add input validation to the signup form
> refactor the logger to use the new API
> fix the race condition in the worker queue

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-tasks#test-and-debug-your-code)
Test and debug your code
Copy
```
> run tests for the auth module and fix failures
> find and fix security vulnerabilities
> explain why this test is failing

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-tasks#encourage-deeper-thinking)
Encourage deeper thinking
For complex problems, explicitly ask Claude to think more deeply:
Copy
```
> think about how we should architect the new payment service
> think hard about the edge cases in our authentication flow

```

Claude Code will show when the model is using extended thinking. You can proactively prompt Claude to “think” or “think deeply” for more planning-intensive tasks. We suggest that you first tell Claude about your task and let it gather context from your project. Then, ask it to “think” to create a plan.
Claude will think more based on the words you use. For example, “think hard” will trigger more extended thinking than saying “think” alone.
For more tips, see [Extended thinking tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/common-tasks#automate-ci-and-infra-workflows)
Automate CI and infra workflows
Claude Code comes with a non-interactive mode for headless execution. This is especially useful for running Claude Code in non-interactive contexts like scripts, pipelines, and Github Actions.
Use `--print` (`-p`) to run Claude in non-interactive mode. In this mode, you can set the `ANTHROPIC_API_KEY` environment variable to provide a custom API key.
Non-interactive mode is especially useful when you pre-configure the set of commands Claude is allowed to use:
Copy
```
export ANTHROPIC_API_KEY=sk_...
claude -p "update the README with the latest changes" --allowedTools "Bash(git diff:*)" "Bash(git log:*)" Write --disallowedTools ...

```

Was this page helpful?
YesNo
[Getting started](https://docs.anthropic.com/en/docs/claude-code/getting-started)[CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Understand unfamiliar code](https://docs.anthropic.com/en/docs/claude-code/common-tasks#understand-unfamiliar-code)
  * [Automate Git operations](https://docs.anthropic.com/en/docs/claude-code/common-tasks#automate-git-operations)
  * [Edit code intelligently](https://docs.anthropic.com/en/docs/claude-code/common-tasks#edit-code-intelligently)
  * [Test and debug your code](https://docs.anthropic.com/en/docs/claude-code/common-tasks#test-and-debug-your-code)
  * [Encourage deeper thinking](https://docs.anthropic.com/en/docs/claude-code/common-tasks#encourage-deeper-thinking)
  * [Automate CI and infra workflows](https://docs.anthropic.com/en/docs/claude-code/common-tasks#automate-ci-and-infra-workflows)



