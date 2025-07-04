---
url: https://docs.anthropic.com/en/docs/claude-code/memory
scraped_at: 2025-05-24T19:41:19.687031
title: Manage Claude's memory - Anthropic
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
Manage Claude's memory
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
# Manage Claude's memory
Learn how to manage Claude Code’s memory across sessions with different memory locations and best practices.
Claude Code can remember your preferences across sessions, like style guidelines and common commands in your workflow.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#determine-memory-type)
Determine memory type
Claude Code offers three memory locations, each serving a different purpose:
Memory Type| Location| Purpose| Use Case Examples  
---|---|---|---  
**Project memory**| `./CLAUDE.md`|  Team-shared instructions for the project| Project architecture, coding standards, common workflows  
**User memory**| `~/.claude/CLAUDE.md`|  Personal preferences for all projects| Code styling preferences, personal tooling shortcuts  
**Project memory (local)**| `./CLAUDE.local.md`|  Personal project-specific preferences|  _(Deprecated, see below)_ Your sandbox URLs, preferred test data  
All memory files are automatically loaded into Claude Code’s context when launched.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#claude-md-imports)
CLAUDE.md imports
CLAUDE.md files can import additional files using `@path/to/import` syntax. The following example imports 3 files:
Copy
```
See @README for project overview and @package.json for available npm commands for this project.
# Additional Instructions
- git workflow @docs/git-instructions.md

```

Both relative and absolute paths are allowed. In particular, importing files in user’s home dir is a convenient way for your team members to provide individual instructions that are not checked into the repository. Previously CLAUDE.local.md served a similar purpose, but is now deprecated in favor of imports since they work better across multiple git worktrees.
Copy
```
# Individual Preferences
- @~/.claude/my-project-instructions.md

```

To avoid potential collisions, imports are not evaluated inside markdown code spans and code blocks.
Copy
```
This code span will not be treated as an import: `@anthropic-ai/claude-code`

```

Imported files can recursively import additional files, with a max-depth of 5 hops. You can see what memory files are loaded by running `/memory` command.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#how-claude-looks-up-memories)
How Claude looks up memories
Claude Code reads memories recursively: starting in the cwd, Claude Code recurses up to _/_ and reads any CLAUDE.md or CLAUDE.local.md files it finds. This is especially convenient when working in large repositories where you run Claude Code in _foo/bar/_ , and have memories in both _foo/CLAUDE.md_ and _foo/bar/CLAUDE.md_.
Claude will also discover CLAUDE.md nested in subtrees under your current working directory. Instead of loading them at launch, they are only included when Claude reads files in those subtrees.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#quickly-add-memories-with-the-%23-shortcut)
Quickly add memories with the `#` shortcut
The fastest way to add a memory is to start your input with the `#` character:
Copy
```
# Always use descriptive variable names

```

You’ll be prompted to select which memory file to store this in.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#directly-edit-memories-with-%2Fmemory)
Directly edit memories with `/memory`
Use the `/memory` slash command during a session to open any memory file in your system editor for more extensive additions or organization.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/memory#memory-best-practices)
Memory best practices
  * **Be specific** : “Use 2-space indentation” is better than “Format code properly”.
  * **Use structure to organize** : Format each individual memory as a bullet point and group related memories under descriptive markdown headings.
  * **Review periodically** : Update memories as your project evolves to ensure Claude is always using the most up to date information and context.


Was this page helpful?
YesNo
[IDE integrations](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)[Settings](https://docs.anthropic.com/en/docs/claude-code/settings)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Determine memory type](https://docs.anthropic.com/en/docs/claude-code/memory#determine-memory-type)
  * [CLAUDE.md imports](https://docs.anthropic.com/en/docs/claude-code/memory#claude-md-imports)
  * [How Claude looks up memories](https://docs.anthropic.com/en/docs/claude-code/memory#how-claude-looks-up-memories)
  * [Quickly add memories with the # shortcut](https://docs.anthropic.com/en/docs/claude-code/memory#quickly-add-memories-with-the-%23-shortcut)
  * [Directly edit memories with /memory](https://docs.anthropic.com/en/docs/claude-code/memory#directly-edit-memories-with-%2Fmemory)
  * [Memory best practices](https://docs.anthropic.com/en/docs/claude-code/memory#memory-best-practices)



