---
url: https://supabase.com/docs/guides/functions/secrets
scraped_at: 2025-05-25T09:42:27.246157
title: Managing Secrets (Environment Variables) | Supabase Docs
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
  3. [Managing environment variables](https://supabase.com/docs/guides/functions/secrets)


Managing Secrets (Environment Variables)
Managing secrets and environment variables.
It's common that you will need to use environment variables or other sensitive information Edge Functions. You can manage secrets using the CLI or the Dashboard.
You can access these using Deno's built-in handler
```

1
Deno.env.get('MY_SECRET_NAME')

```

## Default secrets[#](https://supabase.com/docs/guides/functions/secrets#default-secrets)
Edge Functions have access to these secrets by default:
  * `SUPABASE_URL`: The API gateway for your Supabase project.
  * `SUPABASE_ANON_KEY`: The `anon` key for your Supabase API. This is safe to use in a browser when you have [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) enabled.
  * `SUPABASE_SERVICE_ROLE_KEY`: The `service_role` key for your Supabase API. This is safe to use in Edge Functions, but it should NEVER be used in a browser. This key will bypass [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security).
  * `SUPABASE_DB_URL`: The URL for your [Postgres database](https://supabase.com/docs/guides/database). You can use this to connect directly to your database.


## Local secrets[#](https://supabase.com/docs/guides/functions/secrets#local-secrets)
You can load environment variables in two ways:
  1. Through an `.env` file placed at `supabase/functions/.env`, which is automatically loaded on `supabase start`
  2. Through the `--env-file` option for `supabase functions serve`, for example: `supabase functions serve --env-file ./path/to/.env-file`


Let's create a local file for storing our secrets, and inside it we can store a secret `MY_NAME`:
```

1
echo"MY_NAME=Yoda">>./supabase/.env.local

```

This creates a new file `./supabase/.env.local` for storing your local development secrets.
Never check your .env files into Git!
Now let's access this environment variable `MY_NAME` inside our Function. Anywhere in your function, add this line:
```

1
console.log(Deno.env.get('MY_NAME'))

```

Now we can invoke our function locally, by serving it with our new `.env.local` file:
```

1
supabasefunctionsserve--env-file./supabase/.env.local

```

When the function starts you should see the name “Yoda” output to the terminal.
## Production secrets[#](https://supabase.com/docs/guides/functions/secrets#production-secrets)
You will also need to set secrets for your production Edge Functions. You can do this via the Dashboard or using the CLI.
### Using the Dashboard[#](https://supabase.com/docs/guides/functions/secrets#using-the-dashboard)
  1. Visit [Edge Function Secrets Management](https://supabase.com/dashboard/project/_/settings/functions) page in your Dashboard.
  2. Add the Key and Value for your secret and press Save.
  3. Note that you can paste multiple secrets at a time.

![Edge Functions Secrets Management](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fedge-functions-secrets--light.jpg&w=3840&q=75)
### Using the CLI[#](https://supabase.com/docs/guides/functions/secrets#using-the-cli)
Let's create a `.env` to help us deploy our secrets to production. In this case we'll just use the same as our local secrets:
```

1
cp./supabase/.env.local./supabase/.env

```

This creates a new file `./supabase/.env` for storing your production secrets.
Never check your `.env` files into Git! You only use the `.env` file to help deploy your secrets to production. Don't commit it to your repository.
Let's push all the secrets from the `.env` file to our remote project using [`supabase secrets set`](https://supabase.com/docs/reference/cli/usage#supabase-secrets-set):
```

1
2
3
4
supabasesecretsset--env-file./supabase/.env# You can also set secrets individually using:supabasesecretssetMY_NAME=Chewbacca

```

You don't need to re-deploy after setting your secrets.
To see all the secrets which you have set remotely, use [`supabase secrets list`](https://supabase.com/docs/reference/cli/usage#supabase-secrets-list):
```

1
supabasesecretslist

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/secrets.mdx)
### Is this helpful?
No Yes
### On this page
[Default secrets](https://supabase.com/docs/guides/functions/secrets#default-secrets)[Local secrets](https://supabase.com/docs/guides/functions/secrets#local-secrets)[Production secrets](https://supabase.com/docs/guides/functions/secrets#production-secrets)[Using the Dashboard](https://supabase.com/docs/guides/functions/secrets#using-the-dashboard)[Using the CLI](https://supabase.com/docs/guides/functions/secrets#using-the-cli)
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



