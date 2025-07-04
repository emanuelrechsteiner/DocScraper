---
url: https://docs.runbear.io/integrations/apps/langchain/langserve
scraped_at: 2025-05-25T09:01:11.494948
title: LangServe | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/langchain/langserve#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/langchain/langserve)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/langchain/langserve)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
      * [LangChain](https://docs.runbear.io/integrations/apps/langchain/)
        * [LangServe](https://docs.runbear.io/integrations/apps/langchain/langserve)
        * [FastAPI](https://docs.runbear.io/integrations/apps/langchain/fastapi)
      * [Python Application](https://docs.runbear.io/integrations/apps/python-sdk/)
      * [Anthropic Claude](https://docs.runbear.io/integrations/apps/anthropic-claude/)
  * [FAQs](https://docs.runbear.io/faq)


  * [](https://docs.runbear.io/)
  * [Integrations](https://docs.runbear.io/integrations)
  * LLM Apps
  * [LangChain](https://docs.runbear.io/integrations/apps/langchain/)
  * LangServe


On this page
# LangServe
[LangServe](https://github.com/langchain-ai/langserve) is a library designed for deploying LLM applications built with LangChain.
First, ensure your LangServe application is up and running. Check the [LangServe Server Guide](https://python.langchain.com/docs/langserve#server) for more details. You only need the LangServe server component for Runbear.
## Getting the Endpoint[​](https://docs.runbear.io/integrations/apps/langchain/langserve#getting-the-endpoint "Direct link to Getting the Endpoint")
Note the path for your LangServe app. For example, the code below uses `/chat` as the path.
```
add_routes(  app,  ChatOpenAI(),  path="/chat",)
```

## Adding Custom System Prompt[​](https://docs.runbear.io/integrations/apps/langchain/langserve#adding-custom-system-prompt "Direct link to Adding Custom System Prompt")
Runbear will invoke the runnable function with ChatPromptTemplate JSON. Each message includes `role` and `content` data. You can use the `convert_to_messages` function to convert the data into the `BaseMessage` list. Check the example below to learn adding the custom system prompt. You can find an example project on [Proofreading Bot LangServe Example](https://github.com/runbear-io/plugbear-python-sdk/tree/main/examples/proofreading-bot-langserve).
```
from fastapi import FastAPIfrom langchain.prompts import ChatPromptTemplate, MessagesPlaceholderfrom langchain_core.messages import convert_to_messagesfrom langchain_core.output_parsers import StrOutputParserfrom langchain_openai import ChatOpenAIfrom langserve import add_routesapp = FastAPI()llm = ChatOpenAI()output_parser = StrOutputParser()prompt = ChatPromptTemplate.from_messages([("system","You are a Proofreading Bot."),    MessagesPlaceholder("conversation"),])runnable ={"conversation": convert_to_messages}| prompt | llm | output_parseradd_routes(  app,  runnable,  path="/chat",)
```

## Configuring Runbear[​](https://docs.runbear.io/integrations/apps/langchain/langserve#configuring-runbear "Direct link to Configuring Runbear")
You can now configure your app in Runbear:
  1. Open the [Runbear Assistants](https://runbear.io/assistants) page and click the `Add App` button.
  2. Choose 'LangServe' as your app type.
  3. In the 'LangServe endpoint' field, enter your LagnServe URL (e.g., <https://your.domain/chat>).
  4. (Optional) If you need to set up a secret header for your LangServe app, you can configure the 'Security Settings' with your secret header name and corresponding value.
  5. Click the `Create` button.


## What's Next[​](https://docs.runbear.io/integrations/apps/langchain/langserve#whats-next "Direct link to What's Next")
Connect the app you added to communication channels. Check [Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection) for more details.
[PreviousLangChain](https://docs.runbear.io/integrations/apps/langchain/)[NextFastAPI](https://docs.runbear.io/integrations/apps/langchain/fastapi)
  * [Getting the Endpoint](https://docs.runbear.io/integrations/apps/langchain/langserve#getting-the-endpoint)
  * [Adding Custom System Prompt](https://docs.runbear.io/integrations/apps/langchain/langserve#adding-custom-system-prompt)
  * [Configuring Runbear](https://docs.runbear.io/integrations/apps/langchain/langserve#configuring-runbear)
  * [What's Next](https://docs.runbear.io/integrations/apps/langchain/langserve#whats-next)


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

