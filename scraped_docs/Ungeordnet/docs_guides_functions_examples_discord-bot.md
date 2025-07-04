---
url: https://supabase.com/docs/guides/functions/examples/discord-bot
scraped_at: 2025-05-25T08:39:04.889438
title: Building a Discord Bot | Supabase Docs
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
  3. [Building a Discord Bot](https://supabase.com/docs/guides/functions/examples/discord-bot)


Building a Discord Bot
## Create an application on Discord Developer portal[#](https://supabase.com/docs/guides/functions/examples/discord-bot#create-an-application-on-discord-developer-portal)
  1. Go to <https://discord.com/developers/applications> (login using your discord account if required).
  2. Click on **New Application** button available at left side of your profile picture.
  3. Name your application and click on **Create**.
  4. Go to **Bot** section, click on **Add Bot** , and finally on **Yes, do it!** to confirm.


A new application is created which will hold our Slash Command. Don't close the tab as we need information from this application page throughout our development.
Before we can write some code, we need to curl a discord endpoint to register a Slash Command in our app.
Fill `DISCORD_BOT_TOKEN` with the token available in the **Bot** section and `CLIENT_ID` with the ID available on the **General Information** section of the page and run the command on your terminal.
```

1
2
3
4
5
6
7
BOT_TOKEN='replace_me_with_bot_token'CLIENT_ID='replace_me_with_client_id'curl-XPOST\-H 'Content-Type: application/json'\-H "Authorization: Bot $BOT_TOKEN"\-d '{"name":"hello","description":"Greet a person","options":[{"name":"name","description":"The name of the person","type":3,"required":true}]}'\"https://discord.com/api/v8/applications/$CLIENT_ID/commands"

```

This will register a Slash Command named `hello` that accepts a parameter named `name` of type string.
## Code[#](https://supabase.com/docs/guides/functions/examples/discord-bot#code)
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
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
// Sift is a small routing library that abstracts away details like starting a// listener on a port, and provides a simple function (serve) that has an API// to invoke a function for a specific path.import{json,serve,validateRequest}from'https://deno.land/x/sift@0.6.0/mod.ts'// TweetNaCl is a cryptography library that we use to verify requests// from Discord.importnaclfrom'https://cdn.skypack.dev/tweetnacl@v1.0.3?dts'enumDiscordCommandType{Ping=1,ApplicationCommand=2,}// For all requests to "/" endpoint, we want to invoke home() handler.serve({'/discord-bot':home,})// The main logic of the Discord Slash Command is defined in this function.asyncfunctionhome(request:Request){// validateRequest() ensures that a request is of POST method and// has the following headers.const{error}=awaitvalidateRequest(request,{POST:{headers:['X-Signature-Ed25519','X-Signature-Timestamp'],},})if (error) {returnjson({error:error.message},{status:error.status})}// verifySignature() verifies if the request is coming from Discord.// When the request's signature is not valid, we return a 401 and this is// important as Discord sends invalid requests to test our verification.const{valid,body}=awaitverifySignature(request)if (!valid) {returnjson({error:'Invalid request'},{status:401,}  )}const{type=0,data={options:[]}}=JSON.parse(body)// Discord performs Ping interactions to test our application.// Type 1 in a request implies a Ping interaction.if (type===DiscordCommandType.Ping) {returnjson({type:1,// Type 1 in a response is a Pong interaction response type.})}// Type 2 in a request is an ApplicationCommand interaction.// It implies that a user has issued a command.if (type===DiscordCommandType.ApplicationCommand) {const{value}=data.options.find((option:{name:string;value:string})=>option.name==='name')returnjson({// Type 4 responds with the below message retaining the user's// input at the top.type:4,data:{content:`Hello, ${value}!`,},})}// We will return a bad request error as a valid Discord request// shouldn't reach here.returnjson({error:'bad request'},{status:400})}/** Verify whether the request is coming from Discord. */asyncfunctionverifySignature(request:Request):Promise<{valid:boolean;body:string}>{constPUBLIC_KEY=Deno.env.get('DISCORD_PUBLIC_KEY')!// Discord sends these headers with every request.constsignature=request.headers.get('X-Signature-Ed25519')!consttimestamp=request.headers.get('X-Signature-Timestamp')!constbody=awaitrequest.text()constvalid=nacl.sign.detached.verify(newTextEncoder().encode(timestamp+body),hexToUint8Array(signature),hexToUint8Array(PUBLIC_KEY))return{valid,body}}/** Converts a hexadecimal string to Uint8Array. */functionhexToUint8Array(hex:string){returnnewUint8Array(hex.match(/.{1,2}/g)!.map((val)=>parseInt(val,16)))}

```

## Deploy the slash command handler[#](https://supabase.com/docs/guides/functions/examples/discord-bot#deploy-the-slash-command-handler)
```

1
2
supabasefunctionsdeploydiscord-bot--no-verify-jwtsupabasesecretssetDISCORD_PUBLIC_KEY=your_public_key

```

Navigate to your Function details in the Supabase Dashboard to get your Endpoint URL.
### Configure Discord application to use our URL as interactions endpoint URL[#](https://supabase.com/docs/guides/functions/examples/discord-bot#configure-discord-application-to-use-our-url-as-interactions-endpoint-url)
  1. Go back to your application (Greeter) page on Discord Developer Portal
  2. Fill **INTERACTIONS ENDPOINT URL** field with the URL and click on **Save Changes**.


The application is now ready. Let's proceed to the next section to install it.
## Install the slash command on your Discord server[#](https://supabase.com/docs/guides/functions/examples/discord-bot#install-the-slash-command-on-your-discord-server)
So to use the `hello` Slash Command, we need to install our Greeter application on our Discord server. Here are the steps:
  1. Go to **OAuth2** section of the Discord application page on Discord Developer Portal
  2. Select `applications.commands` scope and click on the **Copy** button below.
  3. Now paste and visit the URL on your browser. Select your server and click on **Authorize**.


Open Discord, type `/Promise` and press **Enter**.
## Run locally[#](https://supabase.com/docs/guides/functions/examples/discord-bot#run-locally)
```

1
2
supabasefunctionsservediscord-bot--no-verify-jwt--env-file./supabase/.env.localngrokhttp54321

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/examples/discord-bot.mdx)
### Is this helpful?
No Yes
### On this page
[Create an application on Discord Developer portal](https://supabase.com/docs/guides/functions/examples/discord-bot#create-an-application-on-discord-developer-portal)[Code](https://supabase.com/docs/guides/functions/examples/discord-bot#code)[Deploy the slash command handler](https://supabase.com/docs/guides/functions/examples/discord-bot#deploy-the-slash-command-handler)[Configure Discord application to use our URL as interactions endpoint URL](https://supabase.com/docs/guides/functions/examples/discord-bot#configure-discord-application-to-use-our-url-as-interactions-endpoint-url)[Install the slash command on your Discord server](https://supabase.com/docs/guides/functions/examples/discord-bot#install-the-slash-command-on-your-discord-server)[Run locally](https://supabase.com/docs/guides/functions/examples/discord-bot#run-locally)
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



