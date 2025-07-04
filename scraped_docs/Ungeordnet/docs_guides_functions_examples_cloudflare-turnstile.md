---
url: https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile
scraped_at: 2025-05-25T09:05:32.197634
title: CAPTCHA support with Cloudflare Turnstile | Supabase Docs
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
  3. [CAPTCHA support with Cloudflare Turnstile](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile)


CAPTCHA support with Cloudflare Turnstile
[Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) is a friendly, free CAPTCHA replacement, and it works seamlessly with Supabase Edge Functions to protect your forms. [View on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/cloudflare-turnstile).
## Setup[#](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile#setup)
  * Follow these steps to set up a new site: <https://developers.cloudflare.com/turnstile/get-started/>
  * Add the Cloudflare Turnstile widget to your site: <https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/>


## Code[#](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile#code)
Create a new function in your project:
```

1
supabasefunctionsnewcloudflare-turnstile

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
import{corsHeaders}from'../_shared/cors.ts'console.log('Hello from Cloudflare Trunstile!')functionips(req:Request){returnreq.headers.get('x-forwarded-for')?.split(/\s*,\s*/)}Deno.serve(async(req)=>{// This is needed if you're planning to invoke your function from a browser.if (req.method==='OPTIONS') {returnnewResponse('ok',{headers:corsHeaders})}const{token}=awaitreq.json()constclientIps=ips(req)||['']constip=clientIps[0]// Validate the token by calling the// "/siteverify" API endpoint.letformData=newFormData()formData.append('secret',Deno.env.get('CLOUDFLARE_SECRET_KEY') ??'')formData.append('response',token)formData.append('remoteip',ip)consturl='https://challenges.cloudflare.com/turnstile/v0/siteverify'constresult=awaitfetch(url,{body:formData,method:'POST',})constoutcome=awaitresult.json()console.log(outcome)if (outcome.success) {returnnewResponse('success',{headers:corsHeaders})}returnnewResponse('failure',{headers:corsHeaders})})

```

## Deploy the server-side validation Edge Functions[#](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile#deploy-the-server-side-validation-edge-functions)
  * <https://developers.cloudflare.com/turnstile/get-started/server-side-validation/>


```

1
2
supabasefunctionsdeploycloudflare-turnstilesupabasesecretssetCLOUDFLARE_SECRET_KEY=your_secret_key

```

## Invoke the function from your site[#](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile#invoke-the-function-from-your-site)
```

1
2
3
const{data,error}=awaitsupabase.functions.invoke('cloudflare-turnstile',{body:{token},})

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/examples/cloudflare-turnstile.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FOwW0znboh60%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Setup](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile#setup)[Code](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile#code)[Deploy the server-side validation Edge Functions](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile#deploy-the-server-side-validation-edge-functions)[Invoke the function from your site](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile#invoke-the-function-from-your-site)
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



