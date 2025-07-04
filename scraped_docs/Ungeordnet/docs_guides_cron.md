---
url: https://supabase.com/docs/guides/cron
scraped_at: 2025-05-25T08:54:06.338208
title: Cron | Supabase Docs
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
[Cron](https://supabase.com/docs/guides/cron)
  * [Overview](https://supabase.com/docs/guides/cron)
Getting Started
  * [Install](https://supabase.com/docs/guides/cron/install)
  * [Quickstart](https://supabase.com/docs/guides/cron/quickstart)


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
Cron
  1. [Cron](https://supabase.com/docs/guides/cron)
  2. [Overview](https://supabase.com/docs/guides/cron)


Cron
Schedule Recurring Jobs with Cron Syntax in Postgres
Supabase Cron is a Postgres Module that simplifies scheduling recurring Jobs with cron syntax and monitoring Job runs inside Postgres.
Cron Jobs can be created via SQL or the [Integrations -> Cron](https://supabase.com/dashboard/project/_/integrations) interface inside the Dashboard, and can run anywhere from every second to once a year depending on your use case.
![Manage cron jobs via the Dashboard](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fcron%2Fcron--light.jpg&w=3840&q=75)
Every Job can run SQL snippets or database functions with zero network latency or make an HTTP request, such as invoking a Supabase Edge Function, with ease.
For best performance, we recommend no more than 8 Jobs run concurrently. Each Job should run no more than 10 minutes.
## How does Cron work?[#](https://supabase.com/docs/guides/cron#how-does-cron-work)
Under the hood, Supabase Cron uses the [`pg_cron`](https://github.com/citusdata/pg_cron) Postgres database extension which is the scheduling and execution engine for your Jobs.
The extension creates a `cron` schema in your database and all Jobs are stored on the `cron.job` table. Every Job's run and its status is recorded on the `cron.job_run_details` table.
The Supabase Dashboard provides and interface for you to schedule Jobs and monitor Job runs. You can also do the same with SQL.
## Resources[#](https://supabase.com/docs/guides/cron#resources)
  * [`pg_cron` GitHub Repository](https://github.com/citusdata/pg_cron)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/cron.mdx)
### Is this helpful?
No Yes
### On this page
[How does Cron work?](https://supabase.com/docs/guides/cron#how-does-cron-work)[Resources](https://supabase.com/docs/guides/cron#resources)
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



