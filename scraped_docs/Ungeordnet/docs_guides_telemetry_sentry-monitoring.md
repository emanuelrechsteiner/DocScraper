---
url: https://supabase.com/docs/guides/telemetry/sentry-monitoring
scraped_at: 2025-05-25T09:41:11.328005
title: Sentry integration | Supabase Docs
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
[Telemetry](https://supabase.com/docs/guides/telemetry)
  * [Overview](https://supabase.com/docs/guides/telemetry)
Logging & observability
  * [Logging](https://supabase.com/docs/guides/telemetry/logs)
  * [Advanced log filtering](https://supabase.com/docs/guides/telemetry/advanced-log-filtering)
  * [Log drains](https://supabase.com/docs/guides/telemetry/log-drains)
  * [Metrics](https://supabase.com/docs/guides/telemetry/metrics)
  * [Sentry integration](https://supabase.com/docs/guides/telemetry/sentry-monitoring)


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
Telemetry
  1. [Telemetry](https://supabase.com/docs/guides/telemetry)
  2. Logging & observability
  3. [Sentry integration](https://supabase.com/docs/guides/telemetry/sentry-monitoring)


Sentry integration
Integrate Sentry to monitor errors from a Supabase client
You can use [Sentry](https://sentry.io/welcome/) to monitor errors thrown from a Supabase JavaScript client. Install the [Supabase Sentry integration](https://github.com/supabase-community/sentry-integration-js) to get started.
The Sentry integration supports browser, Node, and edge environments.
## Installation[#](https://supabase.com/docs/guides/telemetry/sentry-monitoring#installation)
Install the Sentry integration using your package manager:
npmyarnpnpm
```

1
npminstall@supabase/sentry-js-integration

```

## Use[#](https://supabase.com/docs/guides/telemetry/sentry-monitoring#use)
If you are using Sentry JavaScript SDK v7, reference [`supabase-community/sentry-integration-js` repository](https://github.com/supabase-community/sentry-integration-js/blob/master/README-7v.md) instead.
To use the Supabase Sentry integration, add it to your `integrations` list when initializing your Sentry client.
You can supply either the Supabase Client constructor or an already-initiated instance of a Supabase Client.
With constructorWith instance
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
import*asSentryfrom'@sentry/browser'import{SupabaseClient}from'@supabase/supabase-js'import{supabaseIntegration}from'@supabase/sentry-js-integration'Sentry.init({dsn:SENTRY_DSN,integrations:[supabaseIntegration(SupabaseClient,Sentry,{tracing:true,breadcrumbs:true,errors:true,}),],})

```

All available configuration options are available in our [`supabase-community/sentry-integration-js` repository](https://github.com/supabase-community/sentry-integration-js/blob/master/README.md#options).
## Deduplicating spans[#](https://supabase.com/docs/guides/telemetry/sentry-monitoring#deduplicating-spans)
If you're already monitoring HTTP errors in Sentry, for example with the HTTP, Fetch, or Undici integrations, you will get duplicate spans for Supabase calls. You can deduplicate the spans by skipping them in your other integration:
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
import*asSentryfrom'@sentry/browser'import{SupabaseClient}from'@supabase/supabase-js'import{supabaseIntegration}from'@supabase/sentry-js-integration'Sentry.init({dsn:SENTRY_DSN,integrations:[supabaseIntegration(SupabaseClient,Sentry,{tracing:true,breadcrumbs:true,errors:true,}),// @sentry/browserSentry.browserTracingIntegration({shouldCreateSpanForRequest:(url)=>{return!url.startsWith(`${SUPABASE_URL}/rest`)},}),// or @sentry/nodeSentry.httpIntegration({tracing:{ignoreOutgoingRequests:(url)=>{returnurl.startsWith(`${SUPABASE_URL}/rest`)},},}),// or @sentry/node with Fetch supportSentry.nativeNodeFetchIntegration({ignoreOutgoingRequests:(url)=>{returnurl.startsWith(`${SUPABASE_URL}/rest`)},}),// or @sentry/WinterCGFetch for Next.js Middleware & Edge FunctionsSentry.winterCGFetchIntegration({breadcrumbs:true,shouldCreateSpanForRequest:(url)=>{return!url.startsWith(`${SUPABASE_URL}/rest`)},}),],})

```

## Example Next.js configuration[#](https://supabase.com/docs/guides/telemetry/sentry-monitoring#example-nextjs-configuration)
See this example for a setup with Next.js to cover browser, server, and edge environments. First, run through the [Sentry Next.js wizard](https://docs.sentry.io/platforms/javascript/guides/nextjs/#install) to generate the base Next.js configuration. Then add the Supabase Sentry Integration to all your `Sentry.init` calls with the appropriate filters.
BrowserServerMiddleware & EdgeInstrumentation
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
import*asSentryfrom'@sentry/nextjs'import{SupabaseClient}from'@supabase/supabase-js'import{supabaseIntegration}from'@supabase/sentry-js-integration'Sentry.init({dsn:SENTRY_DSN,integrations:[supabaseIntegration(SupabaseClient,Sentry,{tracing:true,breadcrumbs:true,errors:true,}),Sentry.browserTracingIntegration({shouldCreateSpanForRequest:(url)=>{return!url.startsWith(`${process.env.NEXT_PUBLIC_SUPABASE_URL}/rest`)},}),],// Adjust this value in production, or use tracesSampler for greater controltracesSampleRate:1,// Setting this option to true will print useful information to the console while you're setting up Sentry.debug:true,})

```

Afterwards, build your application (`npm run build`) and start it locally (`npm run start`). You will now see the transactions being logged in the terminal when making supabase-js requests.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/telemetry/sentry-monitoring.mdx)
### Is this helpful?
No Yes
### On this page
[Installation](https://supabase.com/docs/guides/telemetry/sentry-monitoring#installation)[Use](https://supabase.com/docs/guides/telemetry/sentry-monitoring#use)[Deduplicating spans](https://supabase.com/docs/guides/telemetry/sentry-monitoring#deduplicating-spans)[Example Next.js configuration](https://supabase.com/docs/guides/telemetry/sentry-monitoring#example-nextjs-configuration)
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



