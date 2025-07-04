---
url: https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator
scraped_at: 2025-05-25T09:19:24.106348
title: Generate Images with Amazon Bedrock | Supabase Docs
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
  2. Examples
  3. [Generating AI images](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator)


Generate Images with Amazon Bedrock
[Amazon Bedrock](https://aws.amazon.com/bedrock) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.
This guide will walk you through an example using the Amazon Bedrock JavaScript SDK in Supabase Edge Functions to generate images using the [Amazon Titan Image Generator G1](https://aws.amazon.com/blogs/machine-learning/use-amazon-titan-models-for-image-generation-editing-and-searching/) model.
## Setup[#](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#setup)
  * In your AWS console, navigate to Amazon Bedrock and under "Request model access", select the Amazon Titan Image Generator G1 model.
  * In your Supabase project, create a `.env` file in the `supabase` directory with the following contents:


```

1
2
3
4
5
6
7
8
AWS_DEFAULT_REGION="<your_region>"AWS_ACCESS_KEY_ID="<replace_your_own_credentials>"AWS_SECRET_ACCESS_KEY="<replace_your_own_credentials>"AWS_SESSION_TOKEN="<replace_your_own_credentials>"# Mocked config filesAWS_SHARED_CREDENTIALS_FILE="./aws/credentials"AWS_CONFIG_FILE="./aws/config"

```

### Configure Storage[#](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#configure-storage)
  * [locally] Run `supabase start`
  * Open Studio URL: [locally](http://127.0.0.1:54323/project/default/storage/buckets) | [hosted](https://app.supabase.com/project/_/storage/buckets)
  * Navigate to Storage
  * Click "New bucket"
  * Create a new public bucket called "images"


## Code[#](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#code)
Create a new function in your project:
```

1
supabasefunctionsnewamazon-bedrock

```

And add the code to the `index.ts` file:
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
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
// We need to mock the file system for the AWS SDK to work.import{prepareVirtualFile}from'https://deno.land/x/mock_file@v1.1.2/mod.ts'import{BedrockRuntimeClient,InvokeModelCommand}from'npm:@aws-sdk/client-bedrock-runtime'import{createClient}from'npm:@supabase/supabase-js'import{decode}from'npm:base64-arraybuffer'console.log('Hello from Amazon Bedrock!')Deno.serve(async(req)=>{prepareVirtualFile('./aws/config')prepareVirtualFile('./aws/credentials')constclient=newBedrockRuntimeClient({region:Deno.env.get('AWS_DEFAULT_REGION')??'us-west-2',credentials:{accessKeyId:Deno.env.get('AWS_ACCESS_KEY_ID')??'',secretAccessKey:Deno.env.get('AWS_SECRET_ACCESS_KEY')??'',sessionToken:Deno.env.get('AWS_SESSION_TOKEN')??'',},})const{prompt,seed}=awaitreq.json()console.log(prompt)constinput={contentType:'application/json',accept:'*/*',modelId:'amazon.titan-image-generator-v1',body:JSON.stringify({taskType:'TEXT_IMAGE',textToImageParams:{text:prompt},imageGenerationConfig:{numberOfImages:1,quality:'standard',cfgScale:8.0,height:512,width:512,seed:seed??0,},}),}constcommand=newInvokeModelCommand(input)constresponse=awaitclient.send(command)console.log(response)if (response.$metadata.httpStatusCode===200) {const{body,$metadata}=responseconsttextDecoder=newTextDecoder('utf-8')constjsonString=textDecoder.decode(body.buffer)constparsedData=JSON.parse(jsonString)console.log(parsedData)constimage=parsedData.images[0]constsupabaseClient=createClient(// Supabase API URL - env var exported by default.Deno.env.get('SUPABASE_URL')!,// Supabase API ANON KEY - env var exported by default.Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!)const{data:upload,error:uploadError}=awaitsupabaseClient.storage.from('images').upload(`${$metadata.requestId??''}.png`,decode(image),{contentType:'image/png',cacheControl:'3600',upsert:false,})if (!upload) {returnResponse.json(uploadError)}const{data}=supabaseClient.storage.from('images').getPublicUrl(upload.path!)returnResponse.json(data)}returnResponse.json(response)})

```

## Run the function locally[#](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#run-the-function-locally)
  1. Run `supabase start` (see: <https://supabase.com/docs/reference/cli/supabase-start>)
  2. Start with env: `supabase functions serve --env-file supabase/.env`
  3. Make an HTTP request:


```

1
2
3
4
curl-i--location--requestPOST'http://127.0.0.1:54321/functions/v1/amazon-bedrock'\--header'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0'\--header'Content-Type: application/json'\--data'{"prompt":"A beautiful picture of a bird"}'

```

  1. Navigate back to your storage bucket. You might have to hit the refresh button to see the uploaded image.


## Deploy to your hosted project[#](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#deploy-to-your-hosted-project)
```

1
2
3
supabaselinksupabasefunctionsdeployamazon-bedrocksupabasesecretsset--env-filesupabase/.env

```

You've now deployed a serverless function that uses AI to generate and upload images to your Supabase storage bucket.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/examples/amazon-bedrock-image-generator.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FKIwN2TmkTlg%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Setup](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#setup)[Configure Storage](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#configure-storage)[Code](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#code)[Run the function locally](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#run-the-function-locally)[Deploy to your hosted project](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator#deploy-to-your-hosted-project)
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



