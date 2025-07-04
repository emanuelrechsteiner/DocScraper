---
url: https://supabase.com/docs/guides/functions/deno2
scraped_at: 2025-05-25T08:42:01.071128
title: Using Deno 2 | Supabase Docs
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
  3. [Using Deno 2](https://supabase.com/docs/guides/functions/deno2)


Using Deno 2
Everything you need to know about the Deno 2 runtime
This feature is in Public Alpha. [Submit a support ticket](https://supabase.help) if you have any issues.
### What is Deno 2?[#](https://supabase.com/docs/guides/functions/deno2#what-is-deno-2)
Deno 2 is a major upgrade to the Deno runtime that powers Supabase Edge Functions. It focuses on scalability and seamless ecosystem compatibility while maintaining Deno's core principles of security, simplicity, and developer experience.
**Key improvements include**
  * **Node.js and npm compatibility** : Dramatically improved support for npm packages and Node.js code
  * **Better dependency management** : New tools like `deno install`, `deno add`, and `deno remove` for simplified package management
  * **Improved performance** : Enhanced runtime execution and startup times
  * **Workspace and monorepo support** : Better handling of complex project structures
  * **Framework compatibility** : Support for Next.js, SvelteKit, Remix, and other popular frameworks
  * **Full package.json support** : Works seamlessly with existing Node.js projects and npm workspaces


While these improvements are exciting, they come with some changes that may affect your existing functions. We'll support Deno 1.x functions for a limited time, but we recommend migrating to Deno 2 within the next few months to ensure continued functionality.
### How to use Deno 2[#](https://supabase.com/docs/guides/functions/deno2#how-to-use-deno-2)
Deno 2 will soon become the default choice for creating new functions. For now, Deno 2 is available in preview mode for local development.
Here's how you can build and deploy a function with Deno 2:
  * [Install Deno 2.1](https://docs.deno.com/runtime/getting_started/installation/) or newer version on your machine
  * Go to your Supabase project. `cd my-supabase-project`
  * Open `supabase/config.toml` and set `deno_version = 2`


```

1
2
[edge_runtime]deno_version=2

```

  * All your existing functions should work as before.


To scaffold a new function as a Deno 2 project:
```

1
denoinit--servehello-world

```

  * Open `supabase/config.toml` and add the following:


```

1
2
[functions.hello-world]entrypoint = "./functions/hello-world/main.ts"

```

  * Open supabase/functions/hello-world/main.ts and modify line 10 to:


```

1
if (url.pathname==="/hello-world") {

```

  * Use `npx supabase@beta functions serve --no-verify-jwt` to start the dev server.
  * Visit <http://localhost:54321/functions/v1/hello-world>.
  * To run built-in tests, `cd supabase/functions/hello-world; deno test`


### How to migrate existing functions from Deno 1 to Deno 2[#](https://supabase.com/docs/guides/functions/deno2#how-to-migrate-existing-functions-from-deno-1-to-deno-2)
For a comprehensive migration guide, see the [official Deno 1.x to 2.x migration guide](https://docs.deno.com/runtime/reference/migration_guide/#content).
Most Deno 1 Edge Functions will be compatible out of the box with Deno 2, and no action needs to be taken. When we upgrade our hosted runtime, your functions will automatically be deployed on a Deno 2 cluster.
However, for a small number of functions, this may break existing functionality.
The most common issue to watch for is that some Deno 1 API calls are incompatible with Deno 2 runtime.
For instance if you are using:
  * `Deno.Closer`


Use [`Closer`](https://jsr.io/@std/io/doc/types/~/Closer) from the Standard Library instead.
```

1
2
3
4
5
+importtype{Closer}from"jsr:@std/io/types";-functionfoo(closer:Deno.Closer){+functionfoo(closer:Closer){// ...}

```

The best way to validate your APIs are up to date is to use the Deno lint, which has [rules to disallow deprecated APIs](https://docs.deno.com/lint/rules/no-deprecated-deno-api/).
```

1
denolint

```

For a full list of API changes, see the [official Deno 2 list](https://docs.deno.com/runtime/reference/migration_guide/#api-changes).
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/deno2.mdx)
### Is this helpful?
No Yes
### On this page
[What is Deno 2?](https://supabase.com/docs/guides/functions/deno2#what-is-deno-2)[How to use Deno 2](https://supabase.com/docs/guides/functions/deno2#how-to-use-deno-2)[How to migrate existing functions from Deno 1 to Deno 2](https://supabase.com/docs/guides/functions/deno2#how-to-migrate-existing-functions-from-deno-1-to-deno-2)
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



