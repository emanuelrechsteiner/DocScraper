---
url: https://docs.runbear.io/integrations/apps/openai-gpts/
scraped_at: 2025-05-25T08:58:23.586597
title: Introduction | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-gpts/#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-gpts/)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
      * [LangChain](https://docs.runbear.io/integrations/apps/langchain/)
      * [Python Application](https://docs.runbear.io/integrations/apps/python-sdk/)
      * [Anthropic Claude](https://docs.runbear.io/integrations/apps/anthropic-claude/)
  * [FAQs](https://docs.runbear.io/faq)


  * [](https://docs.runbear.io/)
  * [Integrations](https://docs.runbear.io/integrations)
  * LLM Apps
  * OpenAI GPTs


On this page
# OpenAI GPTs
[OpenAI GPTs](https://openai.com/blog/introducing-gpts) allow you to create personalized ChatGPTs by mixing special instructions, additional knowledge, and a range of skills. This is very useful for making custom AI models. However, only OpenAI Plus subscribers can use these custom GPTs through the ChatGPT app.
**Runbear simplifies bringing custom GPTs into other services like Slack or Discord.**
note
Pricing for OpenAI Assistants varies from the ChatGPT Plus Plan, as charges are based on usage. For more information, please refer to the [OpenAI Pricing](https://openai.com/pricing). To review your current usage plans and limits, visit the [OpenAI Billings](https://platform.openai.com/account/billing) and [OpenAI Limits](https://platform.openai.com/account/limits) pages.
## Importing OpenAI GPTs to Runbear[​](https://docs.runbear.io/integrations/apps/openai-gpts/#importing-openai-gpts-to-runbear "Direct link to Importing OpenAI GPTs to Runbear")
There are two ways to import GPTs.
### Using the Bookmarklet[​](https://docs.runbear.io/integrations/apps/openai-gpts/#using-the-bookmarklet "Direct link to Using the Bookmarklet")
  1. Display your Bookmarks Bar. For example, you can display Google Chrome's Bookmarks Bar by selecting the menu `View > Always Show Bookmarks Bar` from the menu bar.
  2. Drag this link [GPTs ➜ Runbear v3.5](javascript:throw new Error\('React has blocked a javascript: URL as a security precaution.'\)) to your bookmarks bar.
  3. Go to [chatgpt.com](https://chatgpt.com) and open the GPTs you want to convert to an Assistant.
  4. Click the **Import GPTs** button in your bookmarks bar.


### Using the Address Bar[​](https://docs.runbear.io/integrations/apps/openai-gpts/#using-the-address-bar "Direct link to Using the Address Bar")
![OpenAI GPTs Bookmarklet](https://docs.runbear.io/assets/images/openai-gpts-address-bar-02ecc985c1beed8f60130a7ee575f310.gif)
  1. Copy the following code:

```
void function(){const t=/\/(g-[0-9a-zA-Z]+)/;if('chatgpt.com'!==window.location.hostname||null===t.exec(window.location.pathname))return alert('Please open a GPTs app in chatgpt.com to import it.');const e=t.exec(window.location.pathname)[1],n=Object.fromEntries(document.cookie.split('; ').map((t=>t.split('='))))._account;document.body.outerHTML='<body style="background-color: #1E1E1E; display: flex; justify-content: center; align-items: center;"><article style="display: flex; flex-direction: column; align-items: center; row-gap: 0.5rem;"><img src="undefined/apple-icon.png" width=180 height=auto><div style="display: flex; align-self: flex-start; align-items: center; column-gap: 0.25rem; padding-left: 0.25rem; padding-right: 0.25rem;"><img src="undefined/images/slack/spinner.png" width=32 height=32><p><span id=status style="flex: 1 1 0%; color: rgb(255 255 255);">Initiating</span><span id=dots>.</span></p></div></article><form id=import method=post action="https://runbear.io/api/apps/import/gpts?ver=3.5"><input id=gizmoId type=hidden name=gizmoId> <input id=name type=hidden name=name> <input id=instructions type=hidden name=instructions> <input id=description type=hidden name=description> <input id=tools type=hidden name=tools> <input id=files type=hidden name=files></form></body>';const i=document.getElementById('status'),o=document.getElementById('dots'),a=setInterval((()=>{o.textContent=o.textContent.length<3?o.textContent+'.':'.'}),500);void fetch('https://chatgpt.com/api/auth/session').then((t=>t.json())).then((t=>fetch(`https://chatgpt.com/backend-api/gizmos/${e}?draft=true`,{headers:{authorization:`Bearer ${t.accessToken}`,'Chatgpt-Account-Id':n}}).then((t=>{if(!t.ok)throw new Error('Unable to retrieve GPTs data. This function is limited to GPTs that you own.');return t.json()})).then((e=>({session:t,body:e}))))).then((({session:t,body:o})=>o.files.length<=0?o:(i.textContent='Loading Files',Promise.all(o.files.map((i=>fetch(`https://chatgpt.com/backend-api/files/${i.file_id}/download?gizmo_id=${e}`,{headers:{authorization:`Bearer ${t.accessToken}`,'Chatgpt-Account-Id':n}}).then((t=>t.json())).then((t=>({...i,body:t})))))).then((t=>(o.files=t,o)))))).then((t=>{i.textContent='Transferring GPT to Runbear',document.getElementById('gizmoId').value=e,document.getElementById('name').value=t.gizmo.display.name,document.getElementById('instructions').value=t.gizmo.instructions,document.getElementById('description').value=t.gizmo.display.description,document.getElementById('tools').value=JSON.stringify(t.tools),document.getElementById('files').value=JSON.stringify(t.files),document.getElementById('import').submit(),clearInterval(a),o.textContent='',i.textContent='Redirecting to Runbear'})).catch((t=>{alert('Error fetching GPT. '+t.message),window.location.reload()})).finally((()=>clearInterval(a)))}();
```

  1. Go to [chatgpt.com](https://chatgpt.com) and open the GPTs you want to convert to an Assistant.
  2. In the address bar, type `javascript:`. Then, paste the copied code next to it.
  3. Press enter and wait to import the GPTs.


## Getting OpenAI API Key[​](https://docs.runbear.io/integrations/apps/openai-gpts/#getting-openai-api-key "Direct link to Getting OpenAI API Key")
You need to get or create the OpenAI API key to integrate OpenAI Assistants.
  1. Visit the [OpenAI API keys](https://platform.openai.com/api-keys) page and click the `Create new secret key` button.
  2. Click the `Create secret key` button on the dialog to create one.
  3. Copy the created key to use it later.


![OpenAI API Keys](https://docs.runbear.io/assets/images/openai-api-keys-1c315257eb787665b06556c285ee6ede.png)
## Selecting Models[​](https://docs.runbear.io/integrations/apps/openai-gpts/#selecting-models "Direct link to Selecting Models")
Select the model to use. (e.g., `gpt-4-1106-preview`) You can find the details about each model at the [OpenAI Models](https://platform.openai.com/docs/models) page.
## What's Next[​](https://docs.runbear.io/integrations/apps/openai-gpts/#whats-next "Direct link to What's Next")
Connect the app you added to communication channels. Check [Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection) for more details. Or, continue reading to learn how to utilize Tools.
[PreviousCustom Branded Bot](https://docs.runbear.io/integrations/channels/teams/branded-bot/)[NextIntroduction](https://docs.runbear.io/integrations/apps/openai-assistants/)
  * [Importing OpenAI GPTs to Runbear](https://docs.runbear.io/integrations/apps/openai-gpts/#importing-openai-gpts-to-runbear)
    * [Using the Bookmarklet](https://docs.runbear.io/integrations/apps/openai-gpts/#using-the-bookmarklet)
    * [Using the Address Bar](https://docs.runbear.io/integrations/apps/openai-gpts/#using-the-address-bar)
  * [Getting OpenAI API Key](https://docs.runbear.io/integrations/apps/openai-gpts/#getting-openai-api-key)
  * [Selecting Models](https://docs.runbear.io/integrations/apps/openai-gpts/#selecting-models)
  * [What's Next](https://docs.runbear.io/integrations/apps/openai-gpts/#whats-next)


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

