---
url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts
scraped_at: 2025-05-24T19:43:54.578717
title: Giving Claude a role with a system prompt - Anthropic
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
Giving Claude a role with a system prompt
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
# Giving Claude a role with a system prompt
While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
When using Claude, you can dramatically improve its performance by using the `system` parameter to give it a role. This technique, known as role prompting, is the most powerful way to use system prompts with Claude.
The right role can turn Claude from a general assistant into your virtual domain expert!
**System prompt tips** : Use the `system` parameter to set Claude’s role. Put everything else, like task-specific instructions, in the `user` turn instead.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#why-use-role-prompting%3F)
Why use role prompting?
  * **Enhanced accuracy:** In complex scenarios like legal analysis or financial modeling, role prompting can significantly boost Claude’s performance.
  * **Tailored tone:** Whether you need a CFO’s brevity or a copywriter’s flair, role prompting adjusts Claude’s communication style.
  * **Improved focus:** By setting the role context, Claude stays more within the bounds of your task’s specific requirements.


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#how-to-give-claude-a-role)
How to give Claude a role
Use the `system` parameter in the [Messages API](https://docs.anthropic.com/en/api/messages) to set Claude’s role:
Copy
```
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
  model="claude-3-7-sonnet-20250219",
  max_tokens=2048,
  system="You are a seasoned data scientist at a Fortune 500 company.", # <-- role prompt
  messages=[
    {"role": "user", "content": "Analyze this dataset for anomalies: <dataset>{{DATASET}}</dataset>"}
  ]
)
print(response.content)

```

**Role prompting tip** : Experiment with roles! A `data scientist` might see different insights than a `marketing strategist` for the same data. A `data scientist specializing in customer insight analysis for Fortune 500 companies` might yield different results still!
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#examples)
Examples
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#example-1%3A-legal-contract-analysis)
Example 1: Legal contract analysis
Without a role, Claude might miss critical issues:
Legal contract analysis without role prompting
Role| Content  
---|---  
User| Analyze this software licensing agreement for potential risks:<contract>{{CONTRACT}}</contract>Focus on indemnification, liability, and IP ownership.  
Assistant| Here’s a summary of the key points in the software licensing agreement:1. Indemnification (Section 8): - We indemnify the vendor against claims arising from our use.2. Limitation of Liability (Section 9): - Damages capped at $500.3. IP Ownership (Section 12): - We retain ownership of our modifications.Overall, the agreement seems standard. The indemnification and liability clauses are typical, and we maintain our IP rights.  
With a role, Claude catches critical issues that could cost millions:
Legal contract analysis with role prompting
Role| Content  
---|---  
User| You are the General Counsel of a Fortune 500 tech company. We’re considering this software licensing agreement for our core data infrastructure:<contract>{{CONTRACT}}</contract>Analyze it for potential risks, focusing on indemnification, liability, and IP ownership. Give your professional opinion.  
Assistant| I’ve reviewed the software licensing agreement, and I have serious concerns that could expose our company to significant risks:1. Indemnification (Section 8): - Critical Issue: We indemnify the vendor against “any and all claims” arising from our use. - Risk: This could hold us liable even for the vendor’s negligence or product defects. - Recommendation: Reject. Limit our indemnity to claims arising from our violation of the agreement.2. Limitation of Liability (Section 9): - Critical Issue: Damages capped at $500, including direct damages. - Risk: Grossly inadequate. A critical failure in our data infrastructure could cost us millions in lost revenue and reputational damage. - Recommendation: Reject. Negotiate for cap at 12 months of fees for direct damages, and carve-outs for data breaches.3. IP Ownership (Section 12): - Critical Issue: Vendor gains joint ownership of our modifications and integrations. - Risk: They could use or sell our proprietary algorithms or data insights to competitors. - Recommendation: Reject. We must retain full ownership of our work.Professional Opinion: Do not sign this agreement. It is grossly unfavorable and exposes us to unacceptable levels of risk. If the vendor refuses to renegotiate these terms, I strongly advise exploring alternative providers or accelerating our in-house solution. The potential costs of proceeding with this agreement far outweigh any short-term gains.  
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#example-2%3A-financial-analysis)
Example 2: Financial analysis
Without a role, Claude’s analysis lacks depth:
Financial analysis without role prompting
Role| Content  
---|---  
User| Analyze this dataset of our Q2 financials:<data>{{FINANCIALS}}</data>Highlight key trends and recommend actions.  
Assistant| Here’s a summary of your Q2 financials:1. Revenue: $15.2M, up 22% YoY. Enterprise client base grew 30%.2. Gross Margin: 72%, up 3% from Q1.3. EBITDA Margin: 18%, down 2% due to R&D investments.4. Cash Flow: $4.1M operating, $28M in reserves.Overall, financials look strong with revenue growth and healthy margins. Increased R&D spending is impacting profitability but could pay off long-term. Maintain current course.  
With a role, Claude delivers actionable insights:
Financial analysis with role prompting
Role| Content  
---|---  
User| You are the CFO of a high-growth B2B SaaS company. We’re in a board meeting discussing our Q2 financials:<data>{{FINANCIALS}}</data>Analyze key trends, flag concerns, and recommend strategic actions. Our investors want aggressive growth but are wary of our burn rate.  
Assistant| Board members, here’s my analysis of our Q2 financials:1. Revenue ($15.2M, +22% YoY): - Insight: Enterprise growth (+30%) is outpacing overall growth. - Flag: SMB segment declined 5%. - Action: Reallocate 20% of SMB marketing budget to enterprise sales. Task product to simplify SMB onboarding.2. Margins (Gross: 72%, +3% QoQ; EBITDA: 18%, -2% QoQ): - Insight: Infrastructure optimizations boosted gross margins. - Flag: R&D spend on AI features dented EBITDA. - Action: No change. Our AI roadmap is critical for enterprise stickiness.3. Cash ($4.1M OCF, $28M reserves): - Insight: 15-month runway at current burn. - Flag: CAC up 20%, eroding LTV/CAC. - Action: Freeze non-essential hires. Implement sales funnel analytics to cut CAC by 15% in Q3.Strategic Stance: We’re threading the needle between growth and burn. Enterprise focus is our growth engine—invest there. But watch SMB churn; it could bleed into enterprise. Our AI bet is sound, but we must convert it to ARR by Q4, or we cut R&D by 30%.In sum: Double down on enterprise, streamline SMB, optimize sales, and monetize AI. Questions?  
## [Prompt libraryGet inspired by a curated selection of prompts for various tasks and use cases.](https://docs.anthropic.com/en/prompt-library/library)## [GitHub prompting tutorialAn example-filled tutorial that covers the prompt engineering concepts found in our docs.](https://github.com/anthropics/prompt-eng-interactive-tutorial)## [Google Sheets prompting tutorialA lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)
Was this page helpful?
YesNo
[Use XML tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)[Prefill Claude's response](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Why use role prompting?](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#why-use-role-prompting%3F)
  * [How to give Claude a role](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#how-to-give-claude-a-role)
  * [Examples](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#examples)
  * [Example 1: Legal contract analysis](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#example-1%3A-legal-contract-analysis)
  * [Example 2: Financial analysis](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#example-2%3A-financial-analysis)



