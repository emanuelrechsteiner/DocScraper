---
url: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency
scraped_at: 2025-05-24T19:44:59.591986
title: Increase output consistency (JSON mode) - Anthropic
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
Increase output consistency (JSON mode)
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
# Increase output consistency (JSON mode)
Here’s how to make Claude’s responses more consistent:
## 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#specify-the-desired-output-format)
Specify the desired output format
Precisely define your desired output format using JSON, XML, or custom templates so that Claude understands every output formatting element you require.
Example: Standardizing customer feedback
Role| Content  
---|---  
User| You’re a Customer Insights AI. Analyze this feedback and output in JSON format with keys: “sentiment” (positive/negative/neutral), “key_issues” (list), and “action_items” (list of dicts with “team” and “task”).”I’ve been a loyal user for 3 years, but the recent UI update is a disaster. Finding basic features is now a scavenger hunt. Plus, the new ‘premium’ pricing is outrageous. I’m considering switching unless this is fixed ASAP.”  
Assistant| { “sentiment”: “negative”, “key_issues”: [ “Poor UI/UX in recent update”, “Difficulty finding basic features”, “Perceived high pricing (new ‘premium’ tier)” ], “action_items”: [ { “team”: “Product”, “task”: “Conduct usability testing and iterate on UI based on findings” }, { “team”: “UX”, “task”: “Create a feature discovery guide or onboarding flow” }, { “team”: “Marketing”, “task”: “Review pricing strategy and communicate value proposition” }, { “team”: “Customer Success”, “task”: “Reach out to user, offer concessions to prevent churn” } ]}  
## 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#prefill-claude%E2%80%99s-response)
Prefill Claude’s response
Prefill the `Assistant` turn with your desired format. This trick bypasses Claude’s friendly preamble and enforces your structure.
Example: Daily sales report
Role| Content  
---|---  
User| You’re an insightful Sales Intelligence AI. Generate today’s sales report.Structure the report like this:<report> <summary> <metric name=“total_revenue”>$0.00</metric> <metric name=“units_sold”>0</metric> <metric name=“avg_order_value”>$0.00</metric> </summary> <top_products> <product> <name>Product Name</name> <revenue>$0.00</revenue> <units>0</units> </product> … </top_products> <regional_performance> <region> <name>Region Name</name> <revenue>$0.00</revenue> <growth>0.0%</growth> </region> … </regional_performance> <action_items> <item>Action item.</item> … </action_items></report>  
Assistant (prefill)| <report> <summary> <metric name=  
Assistant| ”total_revenue”>$842,567.00</metric> <metric name=“units_sold”>15,238</metric> <metric name=“avg_order_value”>$55.29</metric> </summary> <top_products> <product> <name>AcmeGuard Pro</name> <revenue>$325,890.00</revenue> <units>3,621</units> </product> <product> <name>AcmeVault Enterprise</name> <revenue>$254,400.00</revenue> <units>1,272</units> </product> <product> <name>AcmeBoost XL</name> <revenue>$147,690.00</revenue> <units>4,923</units> </product> </top_products> <regional_performance> <region> <name>APAC</name> <revenue>$258,960.00</revenue> <growth>12.8%</growth> </region> <region> <name>EMEA</name> <revenue>$325,478.00</revenue> <growth>3.2%</growth> </region> <region> <name>Americas</name> <revenue>$258,129.00</revenue> <growth>-2.1%</growth> </region> </regional_performance> <action_items> <item>Investigate Americas revenue drop; schedule regional sales team meeting.</item> <item>Accelerate CloudGuard Pro rollout in APAC to capitalize on growth.</item> <item>Review NetBoost XL pricing; high volume but lower revenue.</item> </action_items></report>  
## 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#constrain-with-examples)
Constrain with examples
Provide examples of your desired output. This trains Claude’s understanding better than abstract instructions.
Example: Generating consistent market intelligence
Role| Content  
---|---  
User| As a Market Intelligence AI, your task is to analyze data about our competitors. Here is our competitor data:<data>{{DATA}}</data>Output following this example format:<competitor> <name>Rival Inc</name> <overview>A 50-word summary.</overview> <swot> <strengths>- Bullet points</strengths> <weaknesses>- Bullet points</weaknesses> <opportunities>- Bullet points</opportunities> <threats>- Bullet points</threats> </swot> <strategy>A 30-word strategic response.</strategy></competitor>Now, analyze AcmeGiant and AcmeDataCo using this format.  
Assistant| <competitor> <name>AcmeGiant</name> <overview>Global tech leader with a vast ecosystem of consumer and enterprise products. Known for innovation, strong brand, and deep customer lock-in through integrated hardware, software, and services.</overview> <swot> <strengths> - Massive R&D budget fuels continuous innovation - Loyal customer base and powerful brand recognition - Synergistic product ecosystem increases switching costs </strengths> <weaknesses> - High prices may deter cost-sensitive customers - Slow to address enterprise-specific customization needs - Privacy concerns and regulatory scrutiny in multiple markets </weaknesses> <opportunities> - Growing demand for AI and ML capabilities - Expansion into emerging markets - Acquisitions to fill product or talent gaps </opportunities> <threats> - Rapid rise of cloud-native competitors - Antitrust lawsuits and regulatory actions - Talent poaching by startups and competitors </threats> </swot> <strategy>Focus on our agility and customization. Target TechGiant’s slow enterprise response and privacy issues in our marketing.</strategy></competitor><competitor> <name>AcmeDataCo</name> <overview>Rising star in data analytics and visualization. Offers intuitive, self-service BI tools with a freemium model, appealing to startups and enterprise teams alike.</overview> <swot> <strengths> - User-friendly interface reduces need for specialized training - Freemium model lowers barrier to entry, drives viral growth - Strong product-market fit with rise of data-driven decisions </strengths> <weaknesses> - Limited advanced analytics compared to established BI tools - Scaling issues reported with very large datasets - Dependent on third-party cloud infrastructure (AWS) </weaknesses> <opportunities> - Expanding into predictive analytics and AI-driven insights - Forming strategic alliances with complementary tech vendors - Customizable dashboards for industry-specific solutions </opportunities> <threats> - Market saturation; many new entrants in self-service BI - Enterprise BI giants developing more user-friendly tools - Data privacy regulations increasing compliance complexity </threats> </swot> <strategy>Highlight our robust enterprise features and data governance. Target accounts struggling with DataCo’s scale limitations.</strategy></competitor>  
## 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#use-retrieval-for-contextual-consistency)
Use retrieval for contextual consistency
For tasks requiring consistent context (e.g., chatbots, knowledge bases), use retrieval to ground Claude’s responses in a fixed information set.
Example: Enhancing IT support consistency
Role| Content  
---|---  
User| You’re our IT Support AI that draws on knowledge base data. Here are entries from your knowledge base:<kb> <entry> <id>1</id> <title>Reset Active Directory password</title> <content>1. Go to password.ourcompany.com2. Enter your username3. Click “Forgot Password”4. Follow email instructions</content> </entry> <entry> <id>2</id> <title>Connect to VPN</title> <content>1. Install GlobalProtect from software center2. Open GlobalProtect, enter “vpn.ourcompany.com”3. Use AD credentials to log in</content> </entry></kb>When helping users, always check the knowledge base first. Respond in this format:<response> <kb_entry>Knowledge base entry used</kb_entry> <answer>Your response</answer></response> Write some test questions for yourself and answer them using the knowledge base, just to make sure you understand how to use the knowledge base properly.  
Assistant| Understood. I’ll use the knowledge base for consistent responses. Let’s test with a couple of scenarios.User: Hey, I can’t log into my email. I think I forgot my password.<response> <kb_entry>1: Reset Active Directory password</entry> <answer>I understand you’re having trouble logging into your email due to a forgotten password. No worries, this is a common issue. To reset your Active Directory password, which is used for email access, follow these steps:1. Go to password.ourcompany.com2. Enter your username (same as your email address)3. Click on the “Forgot Password” link4. You’ll receive an email with instructions. Follow them to reset your password.After resetting, you should be able to log into your email. Let me know if you need any further assistance.</answer></response>User: I’m working from home today. How do I access internal resources?<response> <kb_entry>2: Connect to VPN</entry> <answer>Great question! To access internal resources while working from home, you’ll need to connect to our company VPN (Virtual Private Network). Here’s how to set that up:1. First, install the GlobalProtect VPN client. You can find this in our software center.2. Once installed, open the GlobalProtect application.3. In the server field, enter “vpn.ourcompany.com”.4. Use your Active Directory (AD) credentials to log in - the same username and password you use for your email.Once connected, you’ll have secure access to all internal resources as if you were in the office. Let me know if you run into any issues during setup.</answer></response>  
## 
[​](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#chain-prompts-for-complex-tasks)
Chain prompts for complex tasks
Break down complex tasks into smaller, consistent subtasks. Each subtask gets Claude’s full attention, reducing inconsistency errors across scaled workflows.
Was this page helpful?
YesNo
[Reduce hallucinations](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)[Mitigate jailbreaks](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Specify the desired output format](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#specify-the-desired-output-format)
  * [Prefill Claude’s response](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#prefill-claude%E2%80%99s-response)
  * [Constrain with examples](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#constrain-with-examples)
  * [Use retrieval for contextual consistency](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#use-retrieval-for-contextual-consistency)
  * [Chain prompts for complex tasks](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#chain-prompts-for-complex-tasks)



