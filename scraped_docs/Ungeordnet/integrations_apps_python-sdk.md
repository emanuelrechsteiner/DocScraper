---
url: https://docs.runbear.io/integrations/apps/python-sdk/
scraped_at: 2025-05-25T08:58:20.334764
title: Python Application | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/python-sdk/#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/python-sdk/)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/python-sdk/)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
      * [LangChain](https://docs.runbear.io/integrations/apps/langchain/)
      * [Python Application](https://docs.runbear.io/integrations/apps/python-sdk/)
      * [Anthropic Claude](https://docs.runbear.io/integrations/apps/anthropic-claude/)
  * [FAQs](https://docs.runbear.io/faq)


  * [](https://docs.runbear.io/)
  * [Integrations](https://docs.runbear.io/integrations)
  * LLM Apps
  * Python Application


On this page
# Python Application
With [Runbear Python SDK](https://pypi.org/project/plugbear), you can easily connect your custom LLM apps to Slack, Discord, and other channels. You can find working examples in the [Runbear SDK Examples](https://github.com/runbear-io/plugbear-python-sdk/tree/main/examples) repository.
## Installation[​](https://docs.runbear.io/integrations/apps/python-sdk/#installation "Direct link to Installation")
To install the Runbear Python SDK, run the following command:
```
pip install 'plugbear[fastapi]'
```

## Step 1. Getting Runbear API Key[​](https://docs.runbear.io/integrations/apps/python-sdk/#step-1-getting-runbear-api-key "Direct link to Step 1. Getting Runbear API Key")
To obtain your API key, visit the [Runbear API Keys](https://auth.runbear.io/org/api_keys) page accessible via the Profile menu and copy the generated key.
![Runbear API Keys](https://docs.runbear.io/assets/images/plugbear-api-key-2db4b5512aa2c320f673b5405fbad937.png)
## Step 2. Configure your Python LLM Application[​](https://docs.runbear.io/integrations/apps/python-sdk/#step-2-configure-your-python-llm-application "Direct link to Step 2. Configure your Python LLM Application")
Here's a simple example to get you started:
```
import contextlibimport plugbear.fastapifrom fastapi import FastAPIPLUGBEAR_API_KEY ="YOUR_PLUGBEAR_API_KEY_HERE"PLUGBEAR_ENDPOINT ="/plugbear"@contextlib.asynccontextmanagerasyncdeflifespan(app: FastAPI):await plugbear.fastapi.register(    app,    llm_func=some_llm,    api_key=PLUGBEAR_API_KEY,    endpoint=PLUGBEAR_ENDPOINT,)yieldapp = FastAPI(lifespan=lifespan)asyncdefsome_llm(context: plugbear.fastapi.Request)->str:# template prompt using `context` to your own LLM# and return result  result:str=...return result
```

For more examples, refer to our examples on [GitHub](https://github.com/runbear-io/plugbear-python-sdk/tree/main/examples/fastapi)
## Step 3. Configure Your App in Runbear[​](https://docs.runbear.io/integrations/apps/python-sdk/#step-3-configure-your-app-in-runbear "Direct link to Step 3. Configure Your App in Runbear")
  1. Navigate to the **[Assistants](https://runbear.io/assistants)** menu and click **Add App**.
  2. Select **Runbear Python SDK** as your app type.
  3. In the **Your LLM App Endpoint** field, enter the endpoint with the path you set earlier. e.g., `https://your.domain.com/runbear`


## What's Next[​](https://docs.runbear.io/integrations/apps/python-sdk/#whats-next "Direct link to What's Next")
Connect the app you added to communication channels. Check [Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection) for more details.
[PreviousFastAPI](https://docs.runbear.io/integrations/apps/langchain/fastapi)[NextAnthropic Claude](https://docs.runbear.io/integrations/apps/anthropic-claude/)
  * [Installation](https://docs.runbear.io/integrations/apps/python-sdk/#installation)
  * [Step 1. Getting Runbear API Key](https://docs.runbear.io/integrations/apps/python-sdk/#step-1-getting-runbear-api-key)
  * [Step 2. Configure your Python LLM Application](https://docs.runbear.io/integrations/apps/python-sdk/#step-2-configure-your-python-llm-application)
  * [Step 3. Configure Your App in Runbear](https://docs.runbear.io/integrations/apps/python-sdk/#step-3-configure-your-app-in-runbear)
  * [What's Next](https://docs.runbear.io/integrations/apps/python-sdk/#whats-next)


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

