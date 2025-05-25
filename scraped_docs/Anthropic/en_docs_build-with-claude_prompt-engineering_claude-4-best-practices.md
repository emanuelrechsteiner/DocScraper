---
url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
scraped_at: 2025-05-24T19:59:34.352572
title: Claude 4 prompt engineering best practices - Anthropic
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
Prompt engineering
Claude 4 prompt engineering best practices
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
    * [Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
    * [Claude 4 best practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
    * [Prompt generator](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator)
    * [Use prompt templates](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables)
    * [Prompt improver](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver)
    * [Be clear and direct](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)
    * [Use examples (multishot prompting)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
    * [Let Claude think (CoT)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
    * [Use XML tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
    * [Give Claude a role (system prompts)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
    * [Prefill Claude's response](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)
    * [Chain complex prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts)
    * [Long context tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips)
    * [Extended thinking tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips)


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


Prompt engineering
# Claude 4 prompt engineering best practices
This guide provides specific prompt engineering techniques for Claude 4 models (Opus 4 and Sonnet 4) to help you achieve optimal results in your applications. These models have been trained for more precise instruction following than previous generations of Claude models.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles)
General principles
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#be-explicit-with-your-instructions)
Be explicit with your instructions
Claude 4 models respond well to clear, explicit instructions. Being specific about your desired output can help enhance results. Customers who desire the “above and beyond” behavior from previous Claude models might need to more explicitly request these behaviors with Claude 4.
Example: Creating an analytics dashboard
**Less effective:**
Copy
```
Create an analytics dashboard

```

**More effective:**
Copy
```
Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.

```

### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#add-context-to-improve-performance)
Add context to improve performance
Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude 4 better understand your goals and deliver more targeted responses.
Example: Formatting preferences
**Less effective:**
Copy
```
NEVER use ellipses

```

**More effective:**
Copy
```
Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them.

```

Claude is smart enough to generalize from the explanation.
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#be-vigilant-with-examples-%26-details)
Be vigilant with examples & details
Claude 4 models pay attention to details and examples as part of instruction following. Ensure that your examples align with the behaviors you want to encourage and minimize behaviors you want to avoid.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#guidance-for-specific-situations)
Guidance for specific situations
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#control-the-format-of-responses)
Control the format of responses
There are a few ways that we have found to be particularly effective in seering output formatting in Claude 4 models:
  1. **Tell Claude what to do instead of what not to do**
     * Instead of: “Do not use markdown in your response”
     * Try: “Your response should be composed of smoothly flowing prose paragraphs.”
  2. **Use XML format indicators**
     * Try: “Write the prose sections of your response in <smoothly_flowing_prose_paragraphs> tags.”
  3. **Match your prompt style to the desired output**
The formatting style used in your prompt may influence Claude’s response style. If you are still experiencing steerability issues with output formatting, we recommend as best as you can matching your prompt style to your desired output style. For exmaple, removing markdown from your prompt can reduce the volume of markdown in the output.


### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#leverage-thinking-%26-interleaved-thinking-capabilities)
Leverage thinking & interleaved thinking capabilities
Claude 4 offers thinking capabilities that can be especially helpful for tasks involving reflection after tool use or complex multi-step reasoning. You can guide its initial or interleaved thinking for better results.
Example prompt
Copy
```
After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.

```

For more information on thinking capabilities, see [Extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking).
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#optimize-parallel-tool-calling)
Optimize parallel tool calling
Claude 4 models excel at parallel tool execution. They have a high success rate in using parallel tool calling without any prompting to do so, but some minor prompting can boost this behavior to ~100% parallel tool use success rate. We have found this prompt to be most effective:
Sample prompt for agents
Copy
```
For maximum efficiency, whenever you need to perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially.

```

### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#reduce-file-creation-in-agentic-coding)
Reduce file creation in agentic coding
Claude 4 models may sometimes create new files for testing and iteration purposes, particularly when working with code. This approach allows Claude to use files, especially python scripts, as a ‘temporary scratchpad’ before saving its final output. Using temporary files can improve outcomes particularly for agentic coding use cases.
If you’d prefer to minimize net new file creation, you can instruct Claude to clean up after itself:
Sample prompt
Copy
```
If you create any temporary new files, scripts, or helper files for iteration, clean up these files by removing them at the end of the task.

```

### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#enhance-visual-and-frontend-code-generation)
Enhance visual and frontend code generation
For frontend code generation, you can steer Claude 4 models to create complex, detailed, and interactive designs by providing explicit encouragement:
Sample prompt
Copy
```
Don't hold back. Give it your all.

```

You can also improve Claude’s frontend performance in specific areas by providing additional modifiers and details on what to focus on:
  * “Include as many relevant features and interactions as possible”
  * “Add thoughtful details like hover states, transitions, and micro-interactions”
  * “Create an impressive demonstration showcasing web development capabilities”
  * “Apply design principles: hierarchy, contrast, balance, and movement”


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#migration-considerations)
Migration considerations
When migrating from Sonnet 3.7 to Claude 4:
  1. **Be specific about desired behavior** : Consider describing exactly what you’d like to see in the output.
  2. **Frame your instructions with modifiers** : Adding modifiers that encourage Claude to increase the quality and detail of its output can help better shape Claude’s performance. For example, instead of “Create an analytics dashboard”, use “Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.”
  3. **Request specific features explicitly** : Animations and interactive elements should be requested explicitly when desired.


Was this page helpful?
YesNo
[Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)[Prompt generator](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [General principles](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles)
  * [Be explicit with your instructions](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#be-explicit-with-your-instructions)
  * [Add context to improve performance](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#add-context-to-improve-performance)
  * [Be vigilant with examples & details](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#be-vigilant-with-examples-%26-details)
  * [Guidance for specific situations](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#guidance-for-specific-situations)
  * [Control the format of responses](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#control-the-format-of-responses)
  * [Leverage thinking & interleaved thinking capabilities](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#leverage-thinking-%26-interleaved-thinking-capabilities)
  * [Optimize parallel tool calling](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#optimize-parallel-tool-calling)
  * [Reduce file creation in agentic coding](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#reduce-file-creation-in-agentic-coding)
  * [Enhance visual and frontend code generation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#enhance-visual-and-frontend-code-generation)
  * [Migration considerations](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#migration-considerations)



