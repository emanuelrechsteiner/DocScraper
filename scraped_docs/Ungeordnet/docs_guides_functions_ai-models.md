---
url: https://supabase.com/docs/guides/functions/ai-models
scraped_at: 2025-05-25T09:13:24.368937
title: Running AI Models | Supabase Docs
---

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Main menu
[Edge Functions](https://supabase.com/docs/guides/functions)
  * [Overview](https://supabase.com/docs/guides/functions)
Getting started
  * [Quickstart](https://supabase.com/docs/guides/functions/quickstart)
  * [Create an Edge Function Locally](https://supabase.com/docs/guides/functions/local-quickstart)
  * [Deploy to Production](https://supabase.com/docs/guides/functions/deploy)
  * [Setting up your editor](https://supabase.com/docs/guides/functions/local-development)
  * [Development tips](https://supabase.com/docs/guides/functions/development-tips)
Guides
  * [Managing dependencies](https://supabase.com/docs/guides/functions/dependencies)
  * [Managing environment variables](https://supabase.com/docs/guides/functions/secrets)
  * [Integrating with Supabase Auth](https://supabase.com/docs/guides/functions/auth)
  * [Integrating with Postgres](https://supabase.com/docs/guides/functions/connect-to-postgres)
  * [Integrating with Supabase Storage](https://supabase.com/docs/guides/functions/storage-caching)
  * [Handling Routing in Functions](https://supabase.com/docs/guides/functions/routing)
  * [Background Tasks](https://supabase.com/docs/guides/functions/background-tasks)
  * [Ephemeral Storage](https://supabase.com/docs/guides/functions/ephemeral-storage)
  * [WebSockets](https://supabase.com/docs/guides/functions/websockets)
  * [Running AI Models](https://supabase.com/docs/guides/functions/ai-models)
  * [Wasm modules](https://supabase.com/docs/guides/functions/wasm)
  * [Deploying with CI / CD pipelines](https://supabase.com/docs/guides/functions/cicd-workflow)
  * [Integrating with Log Drains](https://supabase.com/docs/guides/platform/log-drains)
  * [Using Deno 2](https://supabase.com/docs/guides/functions/deno2)
Debugging
  * [Local Debugging with DevTools](https://supabase.com/docs/guides/functions/debugging-tools)
  * [Logging](https://supabase.com/docs/guides/functions/logging)
  * [Troubleshooting Common Issues](https://supabase.com/docs/guides/functions/troubleshooting)
  * [Testing your Edge Functions](https://supabase.com/docs/guides/functions/unit-test)
  * [Monitoring with Sentry](https://supabase.com/docs/guides/functions/examples/sentry-monitoring)
Platform
  * [Regional invocations](https://supabase.com/docs/guides/functions/regional-invocation)
  * [Status codes](https://supabase.com/docs/guides/functions/status-codes)
  * [Limits](https://supabase.com/docs/guides/functions/limits)
  * [Pricing](https://supabase.com/docs/guides/functions/pricing)
Examples
  * [Auth Send Email Hook](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend)
  * [CORS support for invoking from the browser](https://supabase.com/docs/guides/functions/cors)
  * [Scheduling Functions](https://supabase.com/docs/guides/functions/schedule-functions)
  * [Sending Push Notifications](https://supabase.com/docs/guides/functions/examples/push-notifications)
  * [Generating AI images](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator)
  * [Generating OG images ](https://supabase.com/docs/guides/functions/examples/og-image)
  * [Semantic AI Search](https://supabase.com/docs/guides/functions/examples/semantic-search)
  * [CAPTCHA support with Cloudflare Turnstile](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile)
  * [Building a Discord Bot](https://supabase.com/docs/guides/functions/examples/discord-bot)
  * [Building a Telegram Bot](https://supabase.com/docs/guides/functions/examples/telegram-bot)
  * [Handling Stripe Webhooks ](https://supabase.com/docs/guides/functions/examples/stripe-webhooks)
  * [Rate-limiting with Redis](https://supabase.com/docs/guides/functions/examples/rate-limiting)
  * [Taking Screenshots with Puppeteer](https://supabase.com/docs/guides/functions/examples/screenshots)
  * [Slack Bot responding to mentions](https://supabase.com/docs/guides/functions/examples/slack-bot-mention)
  * [Image Transformation & Optimization](https://supabase.com/docs/guides/functions/examples/image-manipulation)
Third-Party Tools
  * [Dart Edge on Supabase](https://supabase.com/docs/guides/functions/dart-edge)
  * [Browserless.io](https://supabase.com/docs/guides/functions/examples/screenshots)
  * [Hugging Face](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning)
  * [Monitoring with Sentry](https://supabase.com/docs/guides/functions/examples/sentry-monitoring)
  * [OpenAI API](https://supabase.com/docs/guides/ai/examples/openai)
  * [React Email](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend)
  * [Sending Emails with Resend](https://supabase.com/docs/guides/functions/examples/send-emails)
  * [Upstash Redis](https://supabase.com/docs/guides/functions/examples/upstash-redis)
  * [Type-Safe SQL with Kysely](https://supabase.com/docs/guides/functions/kysely-postgres)
  * [Text To Speech with ElevenLabs](https://supabase.com/docs/guides/functions/examples/elevenlabs-generate-speech-stream)
  * [Speech Transcription with ElevenLabs](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech)


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Edge Functions
  1. [Edge Functions](https://supabase.com/docs/guides/functions)
  2. Guides
  3. [Running AI Models](https://supabase.com/docs/guides/functions/ai-models)


Running AI Models
How to run AI models in Edge Functions.
[Supabase Edge Runtime](https://github.com/supabase/edge-runtime) has a built-in API for running AI models. You can use this API to generate embeddings, build conversational workflows, and do other AI related tasks in your Edge Functions.
## Setup[#](https://supabase.com/docs/guides/functions/ai-models#setup)
There are no external dependencies or packages to install to enable the API.
You can create a new inference session by doing:
```

1
constmodel=newSupabase.ai.Session('model-name')

```

To get type hints and checks for the API you can import types from `functions-js` at the top of your file:
```

1
import'jsr:@supabase/functions-js/edge-runtime.d.ts'

```

## Running a model inference[#](https://supabase.com/docs/guides/functions/ai-models#running-a-model-inference)
Once the session is instantiated, you can call it with inputs to perform inferences. Depending on the model you run, you may need to provide different options (discussed below).
```

1
constoutput=awaitmodel.run(input,options)

```

## How to generate text embeddings[#](https://supabase.com/docs/guides/functions/ai-models#how-to-generate-text-embeddings)
Now let's see how to write an Edge Function using the `Supabase.ai` API to generate text embeddings. Currently, `Supabase.ai` API only supports the [gte-small](https://huggingface.co/Supabase/gte-small) model.
`gte-small` model exclusively caters to English texts, and any lengthy texts will be truncated to a maximum of 512 tokens. While you can provide inputs longer than 512 tokens, truncation may affect the accuracy.
```

1
2
3
4
5
6
7
8
9
10
11
12
13
constmodel=newSupabase.ai.Session('gte-small')Deno.serve(async(req:Request)=>{constparams=newURL(req.url).searchParamsconstinput=params.get('input')constoutput=awaitmodel.run(input,{mean_pool:true,normalize:true})returnnewResponse(JSON.stringify(output),{headers:{'Content-Type':'application/json',Connection:'keep-alive',},})})

```

## Using Large Language Models (LLM)[#](https://supabase.com/docs/guides/functions/ai-models#using-large-language-models-llm)
Inference via larger models is supported via [Ollama](https://ollama.com/) and [Mozilla Llamafile](https://github.com/Mozilla-Ocho/llamafile). In the first iteration, you can use it with a self-managed Ollama or [Llamafile server](https://www.docker.com/blog/a-quick-guide-to-containerizing-llamafile-with-docker-for-ai-applications/). We are progressively rolling out support for the hosted solution. To sign up for early access, fill up [this form](https://forms.supabase.com/supabase.ai-llm-early-access).
### Running locally[#](https://supabase.com/docs/guides/functions/ai-models#running-locally)
OllamaMozilla Llamafile
[Install Ollama](https://github.com/ollama/ollama?tab=readme-ov-file#ollama) and pull the Mistral model
```

1
ollamapullmistral

```

Run the Ollama server locally
```

1
ollamaserve

```

Set a function secret called AI_INFERENCE_API_HOST to point to the Ollama server
```

1
echo"AI_INFERENCE_API_HOST=http://host.docker.internal:11434">>supabase/functions/.env

```

Create a new function with the following code
```

1
supabasefunctionsnewollama-test

```

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
import'jsr:@supabase/functions-js/edge-runtime.d.ts'constsession=newSupabase.ai.Session('mistral')Deno.serve(async(req:Request)=>{constparams=newURL(req.url).searchParamsconstprompt=params.get('prompt')??''// Get the output as a streamconstoutput=awaitsession.run(prompt,{stream:true})constheaders=newHeaders({'Content-Type':'text/event-stream',Connection:'keep-alive',})// Create a streamconststream=newReadableStream({asyncstart(controller){constencoder=newTextEncoder()try{forawait (constchunkofoutput) {controller.enqueue(encoder.encode(chunk.response??''))}}catch (err) {console.error('Stream error:',err)}finally{controller.close()}},})// Return the stream to the userreturnnewResponse(stream,{headers,})})

```

Serve the function
```

1
supabasefunctionsserve--env-filesupabase/functions/.env

```

Execute the function
```

1
2
3
curl--get"http://localhost:54321/functions/v1/ollama-test"\--data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj"\-H "Authorization: $ANON_KEY"

```

### Deploying to production[#](https://supabase.com/docs/guides/functions/ai-models#deploying-to-production)
Once the function is working locally, it's time to deploy to production.
Deploy an Ollama or Llamafile server and set a function secret called `AI_INFERENCE_API_HOST` to point to the deployed server
```

1
supabasesecretssetAI_INFERENCE_API_HOST=https://path-to-your-llm-server/

```

Deploy the Supabase function
```

1
supabasefunctionsdeploy

```

Execute the function
```

1
2
3
curl--get"https://project-ref.supabase.co/functions/v1/ollama-test"\--data-urlencode"prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj"\-H"Authorization: $ANON_KEY"

```

As demonstrated in the video above, running Ollama locally is typically slower than running it in on a server with dedicated GPUs. We are collaborating with the Ollama team to improve local performance.
In the future, a hosted LLM API, will be provided as part of the Supabase platform. Supabase will scale and manage the API and GPUs for you. To sign up for early access, fill up [this form](https://forms.supabase.com/supabase.ai-llm-early-access).
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/ai-models.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2Fw4Rr_1whU-U%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Setup](https://supabase.com/docs/guides/functions/ai-models#setup)[Running a model inference](https://supabase.com/docs/guides/functions/ai-models#running-a-model-inference)[How to generate text embeddings](https://supabase.com/docs/guides/functions/ai-models#how-to-generate-text-embeddings)[Using Large Language Models (LLM)](https://supabase.com/docs/guides/functions/ai-models#using-large-language-models-llm)[Running locally](https://supabase.com/docs/guides/functions/ai-models#running-locally)[Deploying to production](https://supabase.com/docs/guides/functions/ai-models#deploying-to-production)
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings



