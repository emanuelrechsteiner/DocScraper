---
url: https://docs.runbear.io/use-cases/proofreading-bot/langchain
scraped_at: 2025-05-25T08:55:35.075222
title: LangChain | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/proofreading-bot/langchain#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/proofreading-bot/langchain)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants)
      * [LangChain](https://docs.runbear.io/use-cases/proofreading-bot/langchain)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
  * LangChain


On this page
# Building a Proofreading Bot Using LangChain
You can build a proofreading bot utilizing LangChain and Runbear by following the instructions. You can find a working code example in the [LangChain Proofreading Bot Example](https://github.com/runbear-io/plugbear-python-sdk/tree/main/examples/proofreading-bot-langchain) repository.
## Prerequisites[​](https://docs.runbear.io/use-cases/proofreading-bot/langchain#prerequisites "Direct link to Prerequisites")
This guide assumes that you have an existing LLM application built using LangChain.
## Installation[​](https://docs.runbear.io/use-cases/proofreading-bot/langchain#installation "Direct link to Installation")
To install the Runbear Python SDK, run the following command:
```
pip install 'plugbear[fastapi]'
```

## Step-by-Step Guide[​](https://docs.runbear.io/use-cases/proofreading-bot/langchain#step-by-step-guide "Direct link to Step-by-Step Guide")
### Getting a Runbear API Key[​](https://docs.runbear.io/use-cases/proofreading-bot/langchain#getting-a-runbear-api-key "Direct link to Getting a Runbear API Key")
You can create or manage Runbear API keys on the [Runbear API Keys](https://auth.runbear.io/org/api_keys) page. Please copy the key for use in the subsequent step.
### Configuring FastAPI with Runbear Endpoint[​](https://docs.runbear.io/use-cases/proofreading-bot/langchain#configuring-fastapi-with-runbear-endpoint "Direct link to Configuring FastAPI with Runbear Endpoint")
Register an endpoint for Runbear using FastAPI. Adjust the endpoint to meet your requirements.
```
import contextlibimport plugbear.fastapifrom fastapi import FastAPI# Find your API key on the Runbear API Keys page.PLUGBEAR_API_KEY = os.environ["PLUGBEAR_API_KEY"]@contextlib.asynccontextmanagerasyncdeflifespan(app: FastAPI):await plugbear.fastapi.register(    app,    llm_func=handle_request,    api_key=PLUGBEAR_API_KEY,    endpoint="/plugbear",)yieldapp = FastAPI(lifespan=lifespan)
```

### Defining the Handling Function[​](https://docs.runbear.io/use-cases/proofreading-bot/langchain#defining-the-handling-function "Direct link to Defining the Handling Function")
You can easily convert Runbear messages into LangChain messages and invoke the LangChain pipeline. Follow the code example below:
```
asyncdefhandle_request(request: plugbear.fastapi.Request)->str:""" Handle the request received from Runbear.  """# Convert Runbear messages to LangChain messages.  messages =[(message.role, message.content)for message in request.messages]# Build prompt using the system message and Runbear messages.  system_prompt =("system","You are the Proofreading Bot, an editor bot designed to proofread technical manuals with the precision and style of a professional technical writer. Your primary function is to make the text clear, concise, and professional. You avoid jargon, ambiguous expressions, and emotional language, aiming for straightforward, easy-to-understand, yet professional sentences. You specialize in improving the readability and accuracy of technical manuals, adhering to high standards of technical writing. While maintaining professionalism, your interaction style is helpful, providing guidance and suggestions to enhance the user's text. Answer the revised version of the text only. Do not add any other descriptions.")  prompt = ChatPromptTemplate.from_messages([system_prompt]+ messages)# Invoke the LangChain pipeline.  output_parser = StrOutputParser()  chain = prompt | llm | output_parser  answer = chain.invoke({})# Returning the generated message.return answer
```

### Configure Your App in Runbear[​](https://docs.runbear.io/use-cases/proofreading-bot/langchain#configure-your-app-in-runbear "Direct link to Configure Your App in Runbear")
  1. Navigate to the **[Assistatns](https://runbear.io/assistants)** menu and click **Add App**.
  2. Select **Runbear Python SDK** as your app type.
  3. In the **Your LLM App Endpoint** field, enter the endpoint with the path you set earlier. e.g., `https://your.domain.com/plugbear`


## What's Next[​](https://docs.runbear.io/use-cases/proofreading-bot/langchain#whats-next "Direct link to What's Next")
You have successfully developed a proofreading bot 🎉 You are now ready to integrate the application into your communication channels, such as Slack.
Connect the app you added to communication channels. Check [Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection) for more details.
[PreviousOpenAI Assistants](https://docs.runbear.io/use-cases/proofreading-bot/openai-assistants)[NextBuilding a Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
  * [Prerequisites](https://docs.runbear.io/use-cases/proofreading-bot/langchain#prerequisites)
  * [Installation](https://docs.runbear.io/use-cases/proofreading-bot/langchain#installation)
  * [Step-by-Step Guide](https://docs.runbear.io/use-cases/proofreading-bot/langchain#step-by-step-guide)
    * [Getting a Runbear API Key](https://docs.runbear.io/use-cases/proofreading-bot/langchain#getting-a-runbear-api-key)
    * [Configuring FastAPI with Runbear Endpoint](https://docs.runbear.io/use-cases/proofreading-bot/langchain#configuring-fastapi-with-runbear-endpoint)
    * [Defining the Handling Function](https://docs.runbear.io/use-cases/proofreading-bot/langchain#defining-the-handling-function)
    * [Configure Your App in Runbear](https://docs.runbear.io/use-cases/proofreading-bot/langchain#configure-your-app-in-runbear)
  * [What's Next](https://docs.runbear.io/use-cases/proofreading-bot/langchain#whats-next)


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

