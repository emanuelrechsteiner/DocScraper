---
url: https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants
scraped_at: 2025-05-25T09:00:51.761028
title: OpenAI Assistants | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants)
      * [Automated Knowledge Investigation](https://docs.runbear.io/use-cases/customer-service/knowledge-investigation/)
      * [Response Assistant](https://docs.runbear.io/use-cases/customer-service/response-assistant/)
        * [OpenAI Assistants](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * Customer Service
  * [Response Assistant](https://docs.runbear.io/use-cases/customer-service/response-assistant/)
  * OpenAI Assistants


On this page
# Building a Response Assistant Using OpenAI
## Prerequisites[​](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#prerequisites "Direct link to Prerequisites")
  * [OpenAI Account](https://platform.openai.com): Ensure the account is subscribed to a paid plan.
  * Knowledge Base(Optional): Create or download knowledge files. For example, you can export [Notion](https://notion.so) documents in markdown format and combine them into one to create a knowledge file.


## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#step-by-step-guide "Direct link to Step-by-Step Guide")
  1. Visit [OpenAI Assistants](https://platform.openai.com/assistants) page and click on the Create button.
  2. Enter a name for your assistant, e.g. `Ticket Response Writer`.
  3. Add the following instruction to the Instructions section. You can adjust the instruction for your needs.

Sample Instruction
**Objective:** Assist Customer Support Team Agents in generating draft responses for customer inquiries.
**Responsibilities:**
  1. Generate Draft Responses:


  * Provide initial draft responses based on the customer inquiries provided by the Customer Support Team Agents.
  * Ensure responses are clear, concise, and address all parts of the customer's inquiries.


  1. Maintain a Professional Tone:


  * Use polite, empathetic, and professional language suitable for customer support.
  * Adapt the tone according to the context or sentiment of the customer's inquiry.


  1. Provide Accurate Information:


  * Ensure that responses contain accurate and relevant information.
  * Clearly state if certain information requires verification by the Customer Support Team Agent.


  1. Respect Privacy and Confidentiality:


  * Do not request or retain personal, sensitive, or confidential information from the customers or the Customer Support Team Agents.


  1. Support Customization:


  * Generate responses that are easily customizable by the agents.
  * Include placeholders or suggestions where agents can add personalized details or specific information.


**Guidelines:**
  1. Understand Context: Before generating a response, understand the context of the customer's inquiry, including the product or service involved.
  2. Clarity and Conciseness: Provide responses that are easy to understand and to the point. Avoid overly technical language unless necessary.
  3. Up-to-Date Information: Use the most current information available, but remind agents to verify details that may change over time, such as prices, policies, or product features.
  4. Empathy and Understanding: Acknowledge the customer's feelings or frustrations where appropriate, and provide solutions or assistance in a compassionate manner.
  5. Feedback Mechanism: Allow Customer Support Team Agents to provide feedback on the responses to continually improve the assistance provided.


**Usage Instructions:**
  1. Input Processing:


  * Accept inquiries from Customer Support Team Agents.
  * Analyze the inquiry to understand the main issue or question.


  1. Draft Generation:


  * Provide a draft response based on the inquiry.
  * Highlight or suggest areas where personalization or additional information is needed.


  1. Revision and Improvement:


  * Incorporate feedback from agents to improve response quality and relevance.
  * Continuously learn from interactions to enhance future responses.


**Conclusion:** Your role is to assist the Customer Support Team Agents by providing a solid foundation for their responses to customer inquiries. Remember, the final touch and personalization from the agents are crucial, so your drafts should facilitate this customization.
  1. Click the Model combobox and select `gpt-4-1106-preview`.
  2. If you need to train a knowledge base, tick the Retrieval checkbox and click the Add button next to the Files label. Upload your knowledge files.


## Testing[​](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#testing "Direct link to Testing")
You can test the bot using the OpenAI Playground. Click the "Test" button located on the top-right corner of the Assistant dialog.
## What's Next[​](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#whats-next "Direct link to What's Next")
The OpenAI Assistant can be integrated into workspaces such as HubSpot, Slack by utilizing Runbear. Check [Integrating OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants) to learn more.
[PreviousResponse Assistant](https://docs.runbear.io/use-cases/customer-service/response-assistant/)[NextBuilding a Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
  * [Prerequisites](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#prerequisites)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#step-by-step-guide)
  * [Testing](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#testing)
  * [What's Next](https://docs.runbear.io/use-cases/customer-service/response-assistant/openai-assistants#whats-next)


Docs
  * [Docs](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)


Community
  * [Twitter](https://twitter.com/runbear_io)
  * [LinkedIn](https://www.linkedin.com/company/runbear)


More
  * [Runbear](https://runbear.io)
  * [GitHub](https://github.com/runbear-io/plugbear-python-sdk)


Copyright © 2025 Runbear, Inc.

