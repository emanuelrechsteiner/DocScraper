---
url: https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech
scraped_at: 2025-05-25T09:00:04.238396
title: Transcription Telegram Bot | Supabase Docs
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
  2. Third-Party Tools
  3. [Speech Transcription with ElevenLabs](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech)


Transcription Telegram Bot
Build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript with Deno in Supabase Edge Functions.
## Introduction[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#introduction)
In this tutorial you will learn how to build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript and the ElevenLabs Scribe model via the [speech to text API](https://elevenlabs.io/speech-to-text).
To check out what the end result will look like, you can test out the [t.me/ElevenLabsScribeBot](https://t.me/ElevenLabsScribeBot)
Find the [example project on GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/speech-to-text/telegram-transcription-bot).
## Requirements[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#requirements)
  * An ElevenLabs account with an [API key](https://supabase.com/app/settings/api-keys).
  * A [Supabase](https://supabase.com) account (you can sign up for a free account via [database.new](https://database.new)).
  * The [Supabase CLI](https://supabase.com/docs/guides/local-development) installed on your machine.
  * The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed on your machine and optionally [setup in your favourite IDE](https://docs.deno.com/runtime/getting_started/setup_your_environment).
  * A [Telegram](https://telegram.org) account.


## Setup[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#setup)
### Register a Telegram bot[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#register-a-telegram-bot)
Use the [BotFather](https://t.me/BotFather) to create a new Telegram bot. Run the `/newbot` command and follow the instructions to create a new bot. At the end, you will receive your secret bot token. Note it down securely for the next step.
![BotFather](https://supabase.com/docs/img/guides/functions/elevenlabs/bot-father.png)
### Create a Supabase project locally[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#create-a-supabase-project-locally)
After installing the [Supabase CLI](https://supabase.com/docs/guides/local-development), run the following command to create a new Supabase project locally:
```

1
supabaseinit

```

### Create a database table to log the transcription results[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#create-a-database-table-to-log-the-transcription-results)
Next, create a new database table to log the transcription results:
```

1
supabasemigrationsnewinit

```

This will create a new migration file in the `supabase/migrations` directory. Open the file and add the following SQL:
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
CREATETABLEIFNOTEXISTS transcription_logs ( id BIGSERIALPRIMARY KEY, file_type VARCHARNOT NULL, duration INTEGERNOT NULL, chat_id BIGINTNOT NULL, message_id BIGINTNOT NULL, username VARCHAR, transcript TEXT, language_code VARCHAR, created_at TIMESTAMP WITH TIME ZONEDEFAULT CURRENT_TIMESTAMP, error TEXT);ALTERTABLE transcription_logs ENABLEROWLEVELSECURITY;

```

### Create a Supabase Edge Function to handle Telegram webhook requests[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#create-a-supabase-edge-function-to-handle-telegram-webhook-requests)
Next, create a new Edge Function to handle Telegram webhook requests:
```

1
supabasefunctionsnewscribe-bot

```

If you're using VS Code or Cursor, select `y` when the CLI prompts "Generate VS Code settings for Deno? [y/N]"!
### Set up the environment variables[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#set-up-the-environment-variables)
Within the `supabase/functions` directory, create a new `.env` file and add the following variables:
```

1
2
3
4
5
6
7
8
# Find / create an API key at https://elevenlabs.io/app/settings/api-keysELEVENLABS_API_KEY=your_api_key# The bot token you received from the BotFather.TELEGRAM_BOT_TOKEN=your_bot_token# A random secret chosen by you to secure the function.FUNCTION_SECRET=random_secret

```

### Dependencies[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#dependencies)
The project uses a couple of dependencies:
  * The open-source [grammY Framework](https://grammy.dev/) to handle the Telegram webhook requests.
  * The [@supabase/supabase-js](https://supabase.com/docs/reference/javascript) library to interact with the Supabase database.
  * The ElevenLabs [JavaScript SDK](https://supabase.com/docs/quickstart) to interact with the speech-to-text API.


Since Supabase Edge Function uses the [Deno runtime](https://deno.land/), you don't need to install the dependencies, rather you can [import](https://docs.deno.com/examples/npm/) them via the `npm:` prefix.
## Code the Telegram bot[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#code-the-telegram-bot)
In your newly created `scribe-bot/index.ts` file, add the following code:
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
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
import{Bot,webhookCallback}from'https://deno.land/x/grammy@v1.34.0/mod.ts'import'jsr:@supabase/functions-js/edge-runtime.d.ts'import{createClient}from'jsr:@supabase/supabase-js@2'import{ElevenLabsClient}from'npm:elevenlabs@1.50.5'console.log(`Function "elevenlabs-scribe-bot" up and running!`)constelevenLabsClient=newElevenLabsClient({apiKey:Deno.env.get('ELEVENLABS_API_KEY')||'',})constsupabase=createClient(Deno.env.get('SUPABASE_URL')||'',Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')||'')asyncfunctionscribe({fileURL,fileType,duration,chatId,messageId,username,}:{fileURL:stringfileType:stringduration:numberchatId:numbermessageId:numberusername:string}){lettranscript:string|null=nullletlanguageCode:string|null=nullleterrorMsg:string|null=nulltry{constsourceFileArrayBuffer=awaitfetch(fileURL).then((res)=>res.arrayBuffer())constsourceBlob=newBlob([sourceFileArrayBuffer],{type:fileType,})constscribeResult=awaitelevenLabsClient.speechToText.convert({file:sourceBlob,model_id:'scribe_v1',tag_audio_events:false,})transcript=scribeResult.textlanguageCode=scribeResult.language_code// Reply to the user with the transcriptawaitbot.api.sendMessage(chatId,transcript,{reply_parameters:{message_id:messageId},})}catch (error) {errorMsg=error.messageconsole.log(errorMsg)awaitbot.api.sendMessage(chatId,'Sorry, there was an error. Please try again.',{reply_parameters:{message_id:messageId},})}// Write log to Supabase.constlogLine={file_type:fileType,duration,chat_id:chatId,message_id:messageId,username,language_code:languageCode,error:errorMsg,}console.log({logLine})awaitsupabase.from('transcription_logs').insert({...logLine,transcript})}consttelegramBotToken=Deno.env.get('TELEGRAM_BOT_TOKEN')constbot=newBot(telegramBotToken||'')conststartMessage=`Welcome to the ElevenLabs Scribe Bot\\! I can transcribe speech in 99 languages with super high accuracy\\!\nTry it out by sending or forwarding me a voice message, video, or audio file\\!\n[Learn more about Scribe](https://elevenlabs.io/speech-to-text) or [build your own bot](https://elevenlabs.io/docs/cookbooks/speech-to-text/telegram-bot)\\!`bot.command('start',(ctx)=>ctx.reply(startMessage.trim(),{parse_mode:'MarkdownV2'}))bot.on([':voice',':audio',':video'],async(ctx)=>{try{constfile=awaitctx.getFile()constfileURL=`https://api.telegram.org/file/bot${telegramBotToken}/${file.file_path}`constfileMeta=ctx.message?.video??ctx.message?.voice??ctx.message?.audioif (!fileMeta) {returnctx.reply('No video|audio|voice metadata found. Please try again.')}// Run the transcription in the background.EdgeRuntime.waitUntil(scribe({fileURL,fileType:fileMeta.mime_type!,duration:fileMeta.duration,chatId:ctx.chat.id,messageId:ctx.message?.message_id!,username:ctx.from?.username||'',})  )// Reply to the user immediately to let them know we received their file.returnctx.reply('Received. Scribing...')}catch (error) {console.error(error)returnctx.reply('Sorry, there was an error getting the file. Please try again with a smaller file!'  )}})consthandleUpdate=webhookCallback(bot,'std/http')Deno.serve(async(req)=>{try{consturl=newURL(req.url)if (url.searchParams.get('secret') !==Deno.env.get('FUNCTION_SECRET')) {returnnewResponse('not allowed',{status:405})}returnawaithandleUpdate(req)}catch (err) {console.error(err)}})

```

## Deploy to Supabase[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#deploy-to-supabase)
If you haven't already, create a new Supabase account at [database.new](https://database.new) and link the local project to your Supabase account:
```

1
supabaselink

```

### Apply the database migrations[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#apply-the-database-migrations)
Run the following command to apply the database migrations from the `supabase/migrations` directory:
```

1
supabasedbpush

```

Navigate to the [table editor](https://supabase.com/dashboard/project/_/editor) in your Supabase dashboard and you should see and empty `transcription_logs` table.
![Empty table](https://supabase.com/docs/img/guides/functions/elevenlabs/supa-empty-table.png)
Lastly, run the following command to deploy the Edge Function:
```

1
supabasefunctionsdeploy--no-verify-jwtscribe-bot

```

Navigate to the [Edge Functions view](https://supabase.com/dashboard/project/_/functions) in your Supabase dashboard and you should see the `scribe-bot` function deployed. Make a note of the function URL as you'll need it later, it should look something like `https://<project-ref>.functions.supabase.co/scribe-bot`.
![Edge Function deployed](https://supabase.com/docs/img/guides/functions/elevenlabs/supa-edge-function-deployed.png)
### Set up the webhook[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#set-up-the-webhook)
Set your bot's webhook URL to `https://<PROJECT_REFERENCE>.functions.supabase.co/telegram-bot` (Replacing `<...>` with respective values). In order to do that, run a GET request to the following URL (in your browser, for example):
```

1
https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook?url=https://<PROJECT_REFERENCE>.supabase.co/functions/v1/scribe-bot?secret=<FUNCTION_SECRET>

```

Note that the `FUNCTION_SECRET` is the secret you set in your `.env` file.
![Set webhook](https://supabase.com/docs/img/guides/functions/elevenlabs/set-webhook.png)
### Set the function secrets[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#set-the-function-secrets)
Now that you have all your secrets set locally, you can run the following command to set the secrets in your Supabase project:
```

1
supabasesecretsset--env-filesupabase/functions/.env

```

## Test the bot[#](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#test-the-bot)
Finally you can test the bot by sending it a voice message, audio or video file.
![Test the bot](https://supabase.com/docs/img/guides/functions/elevenlabs/test-bot.png)
After you see the transcript as a reply, navigate back to your table editor in the Supabase dashboard and you should see a new row in your `transcription_logs` table.
![New row in table](https://supabase.com/docs/img/guides/functions/elevenlabs/supa-new-row.png)
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/examples/elevenlabs-transcribe-speech.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FCE4iPp7kd7Q%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Introduction](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#introduction)[Requirements](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#requirements)[Setup](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#setup)[Register a Telegram bot](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#register-a-telegram-bot)[Create a Supabase project locally](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#create-a-supabase-project-locally)[Create a database table to log the transcription results](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#create-a-database-table-to-log-the-transcription-results)[Create a Supabase Edge Function to handle Telegram webhook requests](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#create-a-supabase-edge-function-to-handle-telegram-webhook-requests)[Set up the environment variables](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#set-up-the-environment-variables)[Dependencies](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#dependencies)[Code the Telegram bot](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#code-the-telegram-bot)[Deploy to Supabase](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#deploy-to-supabase)[Apply the database migrations](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#apply-the-database-migrations)[Set up the webhook](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#set-up-the-webhook)[Set the function secrets](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#set-the-function-secrets)[Test the bot](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech#test-the-bot)
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



