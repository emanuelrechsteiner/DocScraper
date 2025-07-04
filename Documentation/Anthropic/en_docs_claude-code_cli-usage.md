---
url: https://docs.anthropic.com/en/docs/claude-code/cli-usage
scraped_at: 2025-05-24T19:46:09.412568
title: CLI usage and controls - Anthropic
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
CLI usage and controls
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
# CLI usage and controls
Learn how to use Claude Code from the command line, including CLI commands, flags, and slash commands.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-usage#getting-started)
Getting started
Claude Code provides two main ways to interact:
  * **Interactive mode** : Run `claude` to start a REPL session
  * **One-shot mode** : Use `claude -p "query"` for quick commands


Copy
```
# Start interactive mode
claude
# Start with an initial query
claude "explain this project"
# Run a single command and exit
claude -p "what does this function do?"
# Process piped content
cat logs.txt | claude -p "analyze these errors"

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-usage#cli-commands)
CLI commands
Command| Description| Example  
---|---|---  
`claude`| Start interactive REPL| `claude`  
`claude "query"`| Start REPL with initial prompt| `claude "explain this project"`  
`claude -p "query"`| Run one-off query, then exit| `claude -p "explain this function"`  
`cat file | claude -p "query"`| Process piped content| `cat logs.txt | claude -p "explain"`  
`claude -c`| Continue most recent conversation| `claude -c`  
`claude -c -p "query"`| Continue in print mode| `claude -c -p "Check for type errors"`  
`claude -r "<session-id>" "query"`| Resume session by ID| `claude -r "abc123" "Finish this PR"`  
`claude config`| Configure settings| `claude config set --global theme dark`  
`claude update`| Update to latest version| `claude update`  
`claude mcp`| Configure Model Context Protocol servers| [See MCP section in tutorials](https://docs.anthropic.com/en/docs/claude-code/tutorials#set-up-model-context-protocol-mcp)  
## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-usage#cli-flags)
CLI flags
Customize Claude Code’s behavior with these command-line flags:
Flag| Description| Example  
---|---|---  
`--print`, `-p`| Print response without interactive mode (see [SDK documentation](https://docs.anthropic.com/en/docs/claude-code/sdk) for programmatic usage details)| `claude -p "query"`  
`--output-format`| Specify output format for print mode (options: `text`, `json`, `stream-json`)| `claude -p "query" --output-format json`  
`--verbose`| Enable verbose logging, shows full turn-by-turn output (helpful for debugging in both print and interactive modes)| `claude --verbose`  
`--max-turns`| Limit the number of agentic turns in non-interactive mode| `claude -p --max-turns 3 "query"`  
`--model`| Sets the model for the current session with an alias for the latest model (`sonnet` or `opus`) or a model’s full name| `claude --model claude-sonnet-4-20250514`  
`--permission-prompt-tool`| Specify an MCP tool to handle permission prompts in non-interactive mode| `claude -p --permission-prompt-tool mcp_auth_tool "query"`  
`--resume`| Resume a specific session by ID, or by choosing in interactive mode| `claude --resume abc123 "query"`  
`--continue`| Load the most recent conversation in the current directory| `claude --continue`  
`--dangerously-skip-permissions`| Skip permission prompts (use with caution)| `claude --dangerously-skip-permissions`  
The `--output-format json` flag is particularly useful for scripting and automation, allowing you to parse Claude’s responses programmatically.
For detailed information about print mode (`-p`) including output formats, streaming, verbose logging, and programmatic usage, see the [SDK documentation](https://docs.anthropic.com/en/docs/claude-code/sdk).
## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-usage#slash-commands)
Slash commands
Control Claude’s behavior during an interactive session:
Command| Purpose  
---|---  
`/bug`| Report bugs (sends conversation to Anthropic)  
`/clear`| Clear conversation history  
`/compact [instructions]`| Compact conversation with optional focus instructions  
`/config`| View/modify configuration  
`/cost`| Show token usage statistics  
`/doctor`| Checks the health of your Claude Code installation  
`/help`| Get usage help  
`/init`| Initialize project with CLAUDE.md guide  
`/login`| Switch Anthropic accounts  
`/logout`| Sign out from your Anthropic account  
`/memory`| Edit CLAUDE.md memory files  
`/model`| Select or change the AI model  
`/pr_comments`| View pull request comments  
`/review`| Request code review  
`/status`| View account and system statuses  
`/terminal-setup`| Install Shift+Enter key binding for newlines (iTerm2 and VSCode only)  
`/vim`| Enter vim mode for alternating insert and command modes  
## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-usage#special-shortcuts)
Special shortcuts
### 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-usage#quick-memory-with-%23)
Quick memory with `#`
Add memories instantly by starting your input with `#`:
Copy
```
# Always use descriptive variable names

```

You’ll be prompted to select which memory file to store this in.
### 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-usage#line-breaks-in-terminal)
Line breaks in terminal
Enter multiline commands using:
  * **Quick escape** : Type `\` followed by Enter
  * **Keyboard shortcut** : Option+Enter (or Shift+Enter if configured)


To set up Option+Enter in your terminal:
**For Mac Terminal.app:**
  1. Open Settings → Profiles → Keyboard
  2. Check “Use Option as Meta Key”


**For iTerm2 and VSCode terminal:**
  1. Open Settings → Profiles → Keys
  2. Under General, set Left/Right Option key to “Esc+”


**Tip for iTerm2 and VSCode users** : Run `/terminal-setup` within Claude Code to automatically configure Shift+Enter as a more intuitive alternative.
See [terminal setup in settings](https://docs.anthropic.com/en/docs/claude-code/settings#line-breaks) for configuration details.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/cli-usage#vim-mode)
Vim Mode
Claude Code supports a subset of Vim keybindings that can be enabled with `/vim` or configured via `/config`.
The supported subset includes:
  * Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
  * Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`
  * Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)


Was this page helpful?
YesNo
[Common tasks](https://docs.anthropic.com/en/docs/claude-code/common-tasks)[IDE integrations](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Getting started](https://docs.anthropic.com/en/docs/claude-code/cli-usage#getting-started)
  * [CLI commands](https://docs.anthropic.com/en/docs/claude-code/cli-usage#cli-commands)
  * [CLI flags](https://docs.anthropic.com/en/docs/claude-code/cli-usage#cli-flags)
  * [Slash commands](https://docs.anthropic.com/en/docs/claude-code/cli-usage#slash-commands)
  * [Special shortcuts](https://docs.anthropic.com/en/docs/claude-code/cli-usage#special-shortcuts)
  * [Quick memory with #](https://docs.anthropic.com/en/docs/claude-code/cli-usage#quick-memory-with-%23)
  * [Line breaks in terminal](https://docs.anthropic.com/en/docs/claude-code/cli-usage#line-breaks-in-terminal)
  * [Vim Mode](https://docs.anthropic.com/en/docs/claude-code/cli-usage#vim-mode)



