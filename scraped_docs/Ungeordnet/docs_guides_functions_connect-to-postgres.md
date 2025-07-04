---
url: https://supabase.com/docs/guides/functions/connect-to-postgres
scraped_at: 2025-05-25T09:07:16.757253
title: Connecting directly to Postgres | Supabase Docs
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
  3. [Integrating with Postgres](https://supabase.com/docs/guides/functions/connect-to-postgres)


Connecting directly to Postgres
Connecting to Postgres from Edge Functions.
Connect to your Postgres database from an Edge Function by using the `supabase-js` client. You can also use other Postgres clients like [Deno Postgres](https://deno.land/x/postgres)
## Using supabase-js[#](https://supabase.com/docs/guides/functions/connect-to-postgres#using-supabase-js)
The `supabase-js` client is a great option for connecting to your Supabase database since it handles authorization with Row Level Security, and it automatically formats your response as JSON.
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
import{createClient}from'jsr:@supabase/supabase-js@2'Deno.serve(async(req)=>{try{constsupabase=createClient(Deno.env.get('SUPABASE_URL')??'',Deno.env.get('SUPABASE_ANON_KEY')??'',{global:{headers:{Authorization:req.headers.get('Authorization')!}}})const{data,error}=awaitsupabase.from('countries').select('*')if (error) {throwerror}returnnewResponse(JSON.stringify({data}),{headers:{'Content-Type':'application/json'},status:200,})}catch (err) {returnnewResponse(String(err?.message??err),{status:500})}})

```

## Using a Postgres client[#](https://supabase.com/docs/guides/functions/connect-to-postgres#using-a-postgres-client)
Because Edge Functions are a server-side technology, it's safe to connect directly to your database using any popular Postgres client. This means you can run raw SQL from your Edge Functions.
Here is how you can connect to the database using Deno Postgres driver and run raw SQL.
Check out the [full example](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/postgres-on-the-edge).
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
import*aspostgresfrom'https://deno.land/x/postgres@v0.17.0/mod.ts'// Get the connection string from the environment variable "SUPABASE_DB_URL"constdatabaseUrl=Deno.env.get('SUPABASE_DB_URL')!// Create a database pool with three connections that are lazily establishedconstpool=newpostgres.Pool(databaseUrl,3,true)Deno.serve(async(_req)=>{try{// Grab a connection from the poolconstconnection=awaitpool.connect()try{// Run a queryconstresult=awaitconnection.queryObject`SELECT * FROM animals`constanimals=result.rows// [{ id: 1, name: "Lion" }, ...]// Encode the result as pretty printed JSONconstbody=JSON.stringify(animals,(key,value)=>(typeofvalue==='bigint'?value.toString():value),2)// Return the response with the correct content type headerreturnnewResponse(body,{status:200,headers:{'Content-Type':'application/json; charset=utf-8'},})}finally{// Release the connection back into the poolconnection.release()}}catch (err) {console.error(err)returnnewResponse(String(err?.message??err),{status:500})}})

```

## Using Drizzle[#](https://supabase.com/docs/guides/functions/connect-to-postgres#using-drizzle)
You can use Drizzle together with [Postgres.js](https://github.com/porsager/postgres). Both can be loaded directly from npm:
```

1
2
3
4
5
6
7
{"imports":{"drizzle-orm":"npm:drizzle-orm@0.29.1","drizzle-orm/":"npm:/drizzle-orm@0.29.1/","postgres":"npm:postgres@3.4.3"}}

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
import{drizzle}from'drizzle-orm/postgres-js'importpostgresfrom'postgres'import{countries}from'../_shared/schema.ts'constconnectionString=Deno.env.get('SUPABASE_DB_URL')!Deno.serve(async(_req)=>{// Disable prefetch as it is not supported for "Transaction" pool modeconstclient=postgres(connectionString,{prepare:false})constdb=drizzle(client)constallCountries=awaitdb.select().from(countries)returnResponse.json(allCountries)})

```

You can find the full example on [GitHub](https://github.com/thorwebdev/edgy-drizzle).
## SSL connections[#](https://supabase.com/docs/guides/functions/connect-to-postgres#ssl-connections)
Deployed edge functions are pre-configured to use SSL for connections to the Supabase database. You don't need to add any extra configurations.
If you want to use SSL connections during local development, follow these steps:
  * Download the SSL certificate from [Database settings](https://supabase.com/dashboard/project/_/settings/database)
  * In your [local .env file](https://supabase.com/docs/guides/functions/secrets), add these two variables:


```

1
2
SSL_CERT_FILE=/path/to/cert.crt# set the path to the downloaded certDENO_TLS_CA_STORE=mozilla,system

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/connect-to-postgres.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2Fcl7EuF1-RsY%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Using supabase-js](https://supabase.com/docs/guides/functions/connect-to-postgres#using-supabase-js)[Using a Postgres client](https://supabase.com/docs/guides/functions/connect-to-postgres#using-a-postgres-client)[Using Drizzle](https://supabase.com/docs/guides/functions/connect-to-postgres#using-drizzle)[SSL connections](https://supabase.com/docs/guides/functions/connect-to-postgres#ssl-connections)
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



