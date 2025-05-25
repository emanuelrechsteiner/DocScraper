---
url: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency
scraped_at: 2025-05-24T19:41:51.229838
title: Reducing latency - Anthropic
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
Strengthen guardrails
Reducing latency
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
  * [Computer use (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)
  * [Google Sheets add-on](https://docs.anthropic.com/en/docs/agents-and-tools/claude-for-sheets)


##### Test & evaluate
  * [Define success criteria](https://docs.anthropic.com/en/docs/test-and-evaluate/define-success)
  * [Develop test cases](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests)
  * Strengthen guardrails
    * [Reduce hallucinations](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
    * [Increase output consistency](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency)
    * [Mitigate jailbreaks](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
    * [Streaming refusals](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)
    * [Reduce prompt leak](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)
    * [Keep Claude in character](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character)
    * [Reducing latency](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency)
  * [Using the Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)


##### Legal center
  * [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
  * [Security and compliance](https://trust.anthropic.com/)


Strengthen guardrails
# Reducing latency
Latency refers to the time it takes for the model to process a prompt and and generate an output. Latency can be influenced by various factors, such as the size of the model, the complexity of the prompt, and the underlying infrastucture supporting the model and point of interaction.
It’s always better to first engineer a prompt that works well without model or prompt constraints, and then try latency reduction strategies afterward. Trying to reduce latency prematurely might prevent you from discovering what top performance looks like.
## 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#how-to-measure-latency)
How to measure latency
When discussing latency, you may come across several terms and measurements:
  * **Baseline latency** : This is the time taken by the model to process the prompt and generate the response, without considering the input and output tokens per second. It provides a general idea of the model’s speed.
  * **Time to first token (TTFT)** : This metric measures the time it takes for the model to generate the first token of the response, from when the prompt was sent. It’s particularly relevant when you’re using streaming (more on that later) and want to provide a responsive experience to your users.


For a more in-depth understanding of these terms, check out our [glossary](https://docs.anthropic.com/en/docs/glossary).
## 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#how-to-reduce-latency)
How to reduce latency
### 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#1-choose-the-right-model)
1. Choose the right model
One of the most straightforward ways to reduce latency is to select the appropriate model for your use case. Anthropic offers a [range of models](https://docs.anthropic.com/en/docs/about-claude/models) with different capabilities and performance characteristics. Consider your specific requirements and choose the model that best fits your needs in terms of speed and output quality. For more details about model metrics, see our [models overview](https://docs.anthropic.com/en/docs/models-overview) page.
### 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#2-optimize-prompt-and-output-length)
2. Optimize prompt and output length
Minimize the number of tokens in both your input prompt and the expected output, while still maintaining high performance. The fewer tokens the model has to process and generate, the faster the response will be.
Here are some tips to help you optimize your prompts and outputs:
  * **Be clear but concise** : Aim to convey your intent clearly and concisely in the prompt. Avoid unnecessary details or redundant information, while keeping in mind that [claude lacks context](https://docs.anthropic.com/en/docs/be-clear-direct) on your use case and may not make the intended leaps of logic if instructions are unclear.
  * **Ask for shorter responses:** : Ask Claude directly to be concise. The Claude 3 family of models has improved steerability over previous generations. If Claude is outputting unwanted length, ask Claude to [curb its chattiness](https://docs.anthropic.com/en/docs/be-clear-direct#provide-detailed-context-and-instructions). 
Due to how LLMs count [tokens](https://docs.anthropic.com/en/docs/glossary#tokens) instead of words, asking for an exact word count or a word count limit is not as effective a strategy as asking for paragraph or sentence count limits.
  * **Set appropriate output limits** : Use the `max_tokens` parameter to set a hard limit on the maximum length of the generated response. This prevents Claude from generating overly long outputs. 
> **Note** : When the response reaches `max_tokens` tokens, the response will be cut off, perhaps midsentence or mid-word, so this is a blunt technique that may require post-processing and is usually most appropriate for multiple choice or short answer responses where the answer comes right at the beginning.
  * **Experiment with temperature** : The `temperature` [parameter](https://docs.anthropic.com/en/api/messages) controls the randomness of the output. Lower values (e.g., 0.2) can sometimes lead to more focused and shorter responses, while higher values (e.g., 0.8) may result in more diverse but potentially longer outputs.


Finding the right balance between prompt clarity, output quality, and token count may require some experimentation.
### 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#3-leverage-streaming)
3. Leverage streaming
Streaming is a feature that allows the model to start sending back its response before the full output is complete. This can significantly improve the perceived responsiveness of your application, as users can see the model’s output in real-time.
With streaming enabled, you can process the model’s output as it arrives, updating your user interface or performing other tasks in parallel. This can greatly enhance the user experience and make your application feel more interactive and responsive.
Visit [streaming Messages](https://docs.anthropic.com/en/api/messages-streaming) to learn about how you can implement streaming for your use case.
Was this page helpful?
YesNo
[Keep Claude in character](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character)[Using the Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [How to measure latency](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#how-to-measure-latency)
  * [How to reduce latency](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#how-to-reduce-latency)
  * [1. Choose the right model](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#1-choose-the-right-model)
  * [2. Optimize prompt and output length](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#2-optimize-prompt-and-output-length)
  * [3. Leverage streaming](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency#3-leverage-streaming)



