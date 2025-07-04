---
url: https://supabase.com/docs/guides/functions/wasm
scraped_at: 2025-05-25T09:34:40.141423
title: Using Wasm modules | Supabase Docs
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
  3. [Wasm modules](https://supabase.com/docs/guides/functions/wasm)


Using Wasm modules
How to use WebAssembly in Edge Functions.
Edge Functions supports running [WebAssembly (Wasm)](https://developer.mozilla.org/en-US/docs/WebAssembly) modules. WebAssembly is useful if you want to optimize code that's slower to run in JavaScript or require low-level manipulation.
It also gives you the option to port existing libraries written in other languages to be used with JavaScript. For example, [magick-wasm](https://supabase.com/docs/guides/functions/examples/image-manipulation), which does image manipulation and transforms, is a port of an existing C library to WebAssembly.
### Writing a Wasm module[#](https://supabase.com/docs/guides/functions/wasm#writing-a-wasm-module)
You can use different languages and SDKs to write Wasm modules. For this tutorial, we will write a simple Wasm module in Rust that adds two numbers.
Follow this [guide on writing Wasm modules in Rust](https://developer.mozilla.org/en-US/docs/WebAssembly/Rust_to_Wasm) to setup your dev environment.
Create a new Edge Function called `wasm-add`.
```

1
supabasefunctionsnewwasm-add

```

Create a new Cargo project for the Wasm module inside the function's directory:
```

1
2
cdsupabase/functions/wasm-addcargonew--libadd-wasm

```

Add the following code to `add-wasm/src/lib.rs`.
```

1
2
3
4
5
6
use wasm_bindgen::prelude::*;#[wasm_bindgen]pub fn add(a: u32, b: u32) -> u32 {  a + b}

```

[View source](https://github.com/supabase/supabase/blob/d218d9190b87d81519f20b5705c7e88ef8bc32b3/examples/edge-functions/supabase/functions/wasm-modules/add-wasm/src/lib.rs)
Update the `add-wasm/Cargo.toml` to include the `wasm-bindgen` dependency.
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
[package]name = "add-wasm"version = "0.1.0"description = "A simple wasm module that adds two numbers"license = "MIT/Apache-2.0"edition = "2021"[lib]crate-type = ["cdylib"][dependencies]wasm-bindgen = "0.2"

```

[View source](https://github.com/supabase/supabase/blob/d218d9190b87d81519f20b5705c7e88ef8bc32b3/examples/edge-functions/supabase/functions/wasm-modules/add-wasm/Cargo.toml)
After that we can build the package, by running:
```

1
wasm-packbuild--targetdeno

```

This will produce a Wasm binary file inside `add-wasm/pkg` directory.
### Calling the Wasm module from the Edge Function[#](https://supabase.com/docs/guides/functions/wasm#calling-the-wasm-module-from-the-edge-function)
Now let's update the Edge Function to call `add` from the Wasm module.
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
import{add}from"./add-wasm/pkg/add_wasm.js";Deno.serve(async(req)=>{const{a,b}=awaitreq.json();returnnewResponse(JSON.stringify({result:add(a,b) }),{headers:{"Content-Type":"application/json"}}, );});

```

[View source](https://github.com/supabase/supabase/blob/d218d9190b87d81519f20b5705c7e88ef8bc32b3/examples/edge-functions/supabase/functions/wasm-modules/index.ts)
Supabase Edge Functions currently use Deno 1.46. From [Deno 2.1, importing Wasm modules](https://deno.com/blog/v2.1) will require even less boilerplate code.
### Bundle and deploy the Edge Function[#](https://supabase.com/docs/guides/functions/wasm#bundle-and-deploy-the-edge-function)
Before deploying the Edge Function, we need to ensure it bundles the Wasm module with it. We can do this by defining it in the `static_files` for the function in `superbase/config.toml`.
You will need update Supabase CLI to 2.7.0 or higher for the `static_files` support.
```

1
2
[functions.wasm-add]static_files=["./functions/wasm-add/add-wasm/pkg/*"]

```

Deploy the function by running:
```

1
supabasefunctionsdeploywasm-add

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/wasm.mdx)
### Is this helpful?
No Yes
### On this page
[Writing a Wasm module](https://supabase.com/docs/guides/functions/wasm#writing-a-wasm-module)[Calling the Wasm module from the Edge Function](https://supabase.com/docs/guides/functions/wasm#calling-the-wasm-module-from-the-edge-function)[Bundle and deploy the Edge Function](https://supabase.com/docs/guides/functions/wasm#bundle-and-deploy-the-edge-function)
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



