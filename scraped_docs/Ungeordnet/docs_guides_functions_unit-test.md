---
url: https://supabase.com/docs/guides/functions/unit-test
scraped_at: 2025-05-25T08:52:18.134970
title: Testing your Edge Functions | Supabase Docs
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
  2. Debugging
  3. [Testing your Edge Functions](https://supabase.com/docs/guides/functions/unit-test)


Testing your Edge Functions
Writing Unit Tests for Edge Functions using Deno Test
Testing is an essential step in the development process to ensure the correctness and performance of your Edge Functions.
## Testing in Deno[#](https://supabase.com/docs/guides/functions/unit-test#testing-in-deno)
Deno has a built-in test runner that you can use for testing JavaScript or TypeScript code. You can read the [official documentation](https://docs.deno.com/runtime/manual/basics/testing/) for more information and details about the available testing functions.
## Folder structure[#](https://supabase.com/docs/guides/functions/unit-test#folder-structure)
We recommend creating your testing in a `supabase/functions/tests` directory, using the same name as the Function followed by `-test.ts`:
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
└──supabase├──functions│├──function-one││└──index.ts│└──function-two││└──index.ts│└──tests│└──function-one-test.ts# Tests for function-one│└──function-two-test.ts# Tests for function-two└──config.toml

```

## Example script[#](https://supabase.com/docs/guides/functions/unit-test#example-script)
The following script is a good example to get started with testing your Edge Functions:
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
// Import required libraries and modulesimport{assert,assertEquals}from'jsr:@std/assert@1'import{createClient,SupabaseClient}from'jsr:@supabase/supabase-js@2'// Will load the .env file to Deno.envimport'jsr:@std/dotenv/load'// Set up the configuration for the Supabase clientconstsupabaseUrl=Deno.env.get('SUPABASE_URL')??''constsupabaseKey=Deno.env.get('SUPABASE_ANON_KEY')??''constoptions={auth:{autoRefreshToken:false,persistSession:false,detectSessionInUrl:false,},}// Test the creation and functionality of the Supabase clientconsttestClientCreation=async()=>{varclient:SupabaseClient=createClient(supabaseUrl,supabaseKey,options)// Verify if the Supabase URL and key are providedif (!supabaseUrl) thrownewError('supabaseUrl is required.')if (!supabaseKey) thrownewError('supabaseKey is required.')// Test a simple query to the databaseconst{data:table_data,error:table_error}=awaitclient.from('my_table').select('*').limit(1)if (table_error) {thrownewError('Invalid Supabase client: '+table_error.message)}assert(table_data,'Data should be returned from the query.')}// Test the 'hello-world' functionconsttestHelloWorld=async()=>{varclient:SupabaseClient=createClient(supabaseUrl,supabaseKey,options)// Invoke the 'hello-world' function with a parameterconst{data:func_data,error:func_error}=awaitclient.functions.invoke('hello-world',{body:{name:'bar'},})// Check for errors from the function invocationif (func_error) {thrownewError('Invalid response: '+func_error.message)}// Log the response from the functionconsole.log(JSON.stringify(func_data,null,2))// Assert that the function returned the expected resultassertEquals(func_data.message,'Hello bar!')}// Register and run the testsDeno.test('Client Creation Test',testClientCreation)Deno.test('Hello-world Function Test',testHelloWorld)

```

This test case consists of two parts. The first part tests the client library and verifies that the database can be connected to and returns values from a table (`my_table`). The second part tests the edge function and checks if the received value matches the expected value. Here's a brief overview of the code:
  * We import various testing functions from the Deno standard library, including `assert`, `assertExists`, and `assertEquals`.
  * We import the `createClient` and `SupabaseClient` classes from the `@supabase/supabase-js` library to interact with the Supabase client.
  * We define the necessary configuration for the Supabase client, including the Supabase URL, API key, and authentication options.
  * The `testClientCreation` function tests the creation of a Supabase client instance and queries the database for data from a table. It verifies that data is returned from the query.
  * The `testHelloWorld` function tests the "Hello-world" Edge Function by invoking it using the Supabase client's `functions.invoke` method. It checks if the response message matches the expected greeting.
  * We run the tests using the `Deno.test` function, providing a descriptive name for each test case and the corresponding test function.


Make sure to replace the placeholders (`supabaseUrl`, `supabaseKey`, `my_table`) with the actual values relevant to your Supabase setup.
## Running Edge Functions locally[#](https://supabase.com/docs/guides/functions/unit-test#running-edge-functions-locally)
To locally test and debug Edge Functions, you can utilize the Supabase CLI. Let's explore how to run Edge Functions locally using the Supabase CLI:
  1. Ensure that the Supabase server is running by executing the following command:
```

1
supabasestart

```

  2. In your terminal, use the following command to serve the Edge Functions locally:
```

1
supabasefunctionsserve

```

This command starts a local server that runs your Edge Functions, enabling you to test and debug them in a development environment.
  3. Create the environment variables file:
```

1
2
3
4
5
6
7
8
# creates the filetouch.env# adds the SUPABASE_URL secretecho"SUPABASE_URL=http://localhost:54321">>.env# adds the SUPABASE_ANON_KEY secretecho"SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0">>.env# Alternatively, you can open it in your editor:open.env

```

  4. To run the tests, use the following command in your terminal:
```

1
denotest--allow-allsupabase/functions/tests/function-one-test.ts

```



## Resources[#](https://supabase.com/docs/guides/functions/unit-test#resources)
  * Full guide on Testing Supabase Edge Functions on [Mansueli's tips](https://blog.mansueli.com/testing-supabase-edge-functions-with-deno-test)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/unit-test.mdx)
### Is this helpful?
No Yes
### On this page
[Testing in Deno](https://supabase.com/docs/guides/functions/unit-test#testing-in-deno)[Folder structure](https://supabase.com/docs/guides/functions/unit-test#folder-structure)[Example script](https://supabase.com/docs/guides/functions/unit-test#example-script)[Running Edge Functions locally](https://supabase.com/docs/guides/functions/unit-test#running-edge-functions-locally)[Resources](https://supabase.com/docs/guides/functions/unit-test#resources)
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



