---
url: https://supabase.com/docs/guides/local-development/restoring-downloaded-backup
scraped_at: 2025-05-25T09:02:14.023007
title: Restoring a downloaded backup locally | Supabase Docs
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
[Local Dev / CLI](https://supabase.com/docs/guides/local-development)
  * [Overview](https://supabase.com/docs/guides/local-development)
CLI
  * [Getting started](https://supabase.com/docs/guides/local-development/cli/getting-started)
  * [Configuration](https://supabase.com/docs/guides/local-development/cli/config)
  * [CLI commands](https://supabase.com/docs/reference/cli)
Local development
  * [Getting started](https://supabase.com/docs/guides/local-development/overview)
  * [Declarative database schemas](https://supabase.com/docs/guides/local-development/declarative-database-schemas)
  * [Seeding your database](https://supabase.com/docs/guides/local-development/seeding-your-database)
  * [Managing config and secrets](https://supabase.com/docs/guides/local-development/managing-config)
  * [Restoring downloaded backup](https://supabase.com/docs/guides/local-development/restoring-downloaded-backup)
  * [Customizing email templates](https://supabase.com/docs/guides/local-development/customizing-email-templates)
Testing
  * [Getting started](https://supabase.com/docs/guides/local-development/testing/overview)
  * [pgTAP advanced guide](https://supabase.com/docs/guides/local-development/testing/pgtap-extended)
  * [Database testing](https://supabase.com/docs/guides/database/testing)
  * [RLS policies testing](https://supabase.com/docs/guides/database/extensions/pgtap#testing-rls-policies)


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
Local Development
  1. [Local Dev / CLI](https://supabase.com/docs/guides/local-development)
  2. Local development
  3. [Restoring downloaded backup](https://supabase.com/docs/guides/local-development/restoring-downloaded-backup)


Restoring a downloaded backup locally
Restore a backup of a remote database on a local instance to inspect and extract data
You can restore a downloaded backup to a local Supabase instance. This might be useful if your paused project has exceeded its [restoring time limit](https://supabase.com/docs/guides/platform/upgrading#time-limits). You can download the latest backup, then load it locally to inspect and extract your data.
If you want to restore your backup to a hosted Supabase project, follow the [Migrating within Supabase guide](https://supabase.com/docs/guides/platform/migrating-within-supabase) instead.
## Downloading your backup[#](https://supabase.com/docs/guides/local-development/restoring-downloaded-backup#downloading-your-backup)
First, download your project's backup file from dashboard and identify its backup image version (following the `PG:` prefix):
![Project Paused: 90 Days Remaining](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fpaused-dl-image-version.png&w=3840&q=75)
## Restoring your backup[#](https://supabase.com/docs/guides/local-development/restoring-downloaded-backup#restoring-your-backup)
Given Postgres version `15.6.1.115`, start Postgres locally with `db_cluster.backup` being the path to your backup file.
```

1
2
3
supabaseinitecho'15.6.1.115'>supabase/.temp/postgres-versionsupabasedbstart--from-backupdb_cluster.backup

```

Note that the earliest Supabase Postgres version that supports a local restore is `15.1.0.55`. If your hosted project was running on earlier versions, you will likely run into errors during restore. Before submitting any support ticket, make sure you have attached the error logs from `supabase_db_*` docker container.
Once your local database starts up successfully, you can connect using psql to verify that all your data is restored.
```

1
psql'postgresql://postgres:postgres@localhost:54322/postgres'

```

If you want to use other services like Auth, Storage, and Studio dashboard together with your restored database, restart the local development stack.
```

1
2
supabasestopsupabasestart

```

A Postgres database started with Supabase CLI is not production ready and should not be used outside of local development.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/local-development/restoring-downloaded-backup.mdx)
### Is this helpful?
No Yes
### On this page
[Downloading your backup](https://supabase.com/docs/guides/local-development/restoring-downloaded-backup#downloading-your-backup)[Restoring your backup](https://supabase.com/docs/guides/local-development/restoring-downloaded-backup#restoring-your-backup)
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


![Project Paused: 90 Days Remaining](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fpaused-dl-image-version.png&w=1920&q=75)

