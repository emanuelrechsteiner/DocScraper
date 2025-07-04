---
url: https://supabase.com/docs/guides/migrations/firebase-storage
scraped_at: 2025-05-25T08:58:43.850808
title: Migrated from Firebase Storage to Supabase | Supabase Docs
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
[Platform](https://supabase.com/docs/guides/platform)
Add-ons
  * [Custom Domains](https://supabase.com/docs/guides/platform/custom-domains)
  * [Database Backups](https://supabase.com/docs/guides/platform/backups)
  * [IPv4 Address](https://supabase.com/docs/guides/platform/ipv4-address)
  * [Read Replicas](https://supabase.com/docs/guides/platform/read-replicas)
Upgrades & Migrations
  * [Upgrading](https://supabase.com/docs/guides/platform/upgrading)
  * [Migrating within Supabase](https://supabase.com/docs/guides/platform/migrating-within-supabase)
  * [Migrating to Supabase](https://supabase.com/docs/guides/platform/migrating-to-supabase)
  * [Auth0](https://supabase.com/docs/guides/platform/migrating-to-supabase/auth0)
  * [Firebase Auth](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth)
  * [Firestore Data](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data)
  * [Firebase Storage](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage)
  * [Heroku](https://supabase.com/docs/guides/platform/migrating-to-supabase/heroku)
  * [Render](https://supabase.com/docs/guides/platform/migrating-to-supabase/render)
  * [Amazon RDS](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds)
  * [Postgres](https://supabase.com/docs/guides/platform/migrating-to-supabase/postgres)
  * [Vercel Postgres](https://supabase.com/docs/guides/platform/migrating-to-supabase/vercel-postgres)
  * [Neon](https://supabase.com/docs/guides/platform/migrating-to-supabase/neon)
  * [MySQL](https://supabase.com/docs/guides/platform/migrating-to-supabase/mysql)
  * [MSSQL](https://supabase.com/docs/guides/platform/migrating-to-supabase/mssql)
Project & Account Management
  * [Access Control](https://supabase.com/docs/guides/platform/access-control)
  * [Multi-factor Authentication](https://supabase.com/docs/guides/platform/multi-factor-authentication)
  * [Transfer Project](https://supabase.com/docs/guides/platform/project-transfer)
  * [Single Sign-On](https://supabase.com/docs/guides/platform/sso)
Platform Configuration
  * [Regions](https://supabase.com/docs/guides/platform/regions)
  * [Compute and Disk](https://supabase.com/docs/guides/platform/compute-and-disk)
  * [Database Size](https://supabase.com/docs/guides/platform/database-size)
  * [HIPAA Projects](https://supabase.com/docs/guides/platform/hipaa-projects)
  * [Network Restrictions](https://supabase.com/docs/guides/platform/network-restrictions)
  * [Performance Tuning](https://supabase.com/docs/guides/platform/performance)
  * [SSL Enforcement](https://supabase.com/docs/guides/platform/ssl-enforcement)
  * [Default Platform Permissions](https://supabase.com/docs/guides/platform/permissions)
Billing
  * [About billing on Supabase](https://supabase.com/docs/guides/platform/billing-on-supabase)
  * [Get set up for billing](https://supabase.com/docs/guides/platform/get-set-up-for-billing)
  * [Manage your subscription](https://supabase.com/docs/guides/platform/manage-your-subscription)
  * [Manage your usage](https://supabase.com/docs/guides/platform/manage-your-usage)
  * [Your monthly invoice](https://supabase.com/docs/guides/platform/your-monthly-invoice)
  * [Control your costs](https://supabase.com/docs/guides/platform/cost-control)
  * [Credits](https://supabase.com/docs/guides/platform/credits)
  * [Billing FAQ](https://supabase.com/docs/guides/platform/billing-faq)


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
Platform
  1. [Platform](https://supabase.com/docs/guides/platform)
  2. More
  3. [Migrating to Supabase](https://supabase.com/docs/guides/platform/migrating-to-supabase)
  4. [Firebase Storage](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage)


Migrated from Firebase Storage to Supabase
Migrate Firebase Storage files to Supabase Storage.
Supabase provides several [tools](https://github.com/supabase-community/firebase-to-supabase/tree/main/storage) to convert storage files from Firebase Storage to Supabase Storage. Conversion is a two-step process:
  1. Files are downloaded from a Firebase storage bucket to a local filesystem.
  2. Files are uploaded from the local filesystem to a Supabase storage bucket.


## Set up the migration tool [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#set-up-migration-tool)
  1. Clone the [`firebase-to-supabase`](https://github.com/supabase-community/firebase-to-supabase) repository:
```

1
gitclonehttps://github.com/supabase-community/firebase-to-supabase.git

```

  2. In the `/storage` directory, rename [supabase-keys-sample.js](https://github.com/supabase-community/firebase-to-supabase/blob/main/storage/supabase-keys-sample.js) to `supabase-keys.js`.
  3. Go to your Supabase project's [API settings](https://supabase.com/dashboard/project/_/settings/api) in the Dashboard.
  4. Copy the **Project URL** and update the `SUPABASE_URL` value in `supabase-keys.js`.
  5. Under **Project API keys** , copy the **service_role** key and update the `SUPABASE_KEY` value in `supabase-keys.js`.


## Generate a Firebase private key [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#generate-firebase-private-key)
  1. Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project.
  2. Click the gear icon next to **Project Overview** in the sidebar and select **Project Settings**.
  3. Click **Service Accounts** and select **Firebase Admin SDK**.
  4. Click **Generate new private key**.
  5. Rename the downloaded file to `firebase-service.json`.


## Command line options[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#command-line-options)
### Download Firestore Storage bucket to a local filesystem folder [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#download-firestore-storage-bucket)
`node download.js <prefix> [<folder>] [<batchSize>] [<limit>] [<token>]`
  * `<prefix>`: The prefix of the files to download. To process the root bucket, use an empty prefix: "".
  * `<folder>`: (optional) Name of subfolder for downloaded files. The selected folder is created as a subfolder of the current folder (e.g., `./downloads/`). The default is `downloads`.
  * `<batchSize>`: (optional) The default is 100.
  * `<limit>`: (optional) Stop after processing this many files. For no limit, use `0`.
  * `<token>`: (optional) Begin processing at this `pageToken`.


To process in batches using multiple command-line executions, you must use the same parameters with a new `<token>` on subsequent calls. Use the token displayed on the last call to continue the process at a given point.
### Upload files to Supabase Storage bucket [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#upload-to-supabase-storage-bucket)
`node upload.js <prefix> <folder> <bucket>`
  * `<prefix>`: The prefix of the files to download. To process all files, use an empty prefix: "".
  * `<folder>`: Name of subfolder of files to upload. The selected folder is read as a subfolder of the current folder (e.g., `./downloads/`). The default is `downloads`.
  * `<bucket>`: Name of the bucket to upload to.


If the bucket doesn't exist, it's created as a `non-public` bucket. You must set permissions on this new bucket in the [Supabase Dashboard](https://supabase.com/dashboard/project/_/storage/buckets) before users can download any files.
## Resources[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#resources)
  * [Supabase vs Firebase](https://supabase.com/alternatives/supabase-vs-firebase)
  * [Firestore Data Migration](https://supabase.com/docs/guides/migrations/firestore-data)
  * [Firebase Auth Migration](https://supabase.com/docs/guides/migrations/firebase-auth)


## Enterprise[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#enterprise)
[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/platform/migrating-to-supabase/firebase-storage.mdx)
### Is this helpful?
No Yes
### On this page
[Set up the migration tool ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#set-up-migration-tool)[Generate a Firebase private key ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#generate-firebase-private-key)[Command line options](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#command-line-options)[Download Firestore Storage bucket to a local filesystem folder ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#download-firestore-storage-bucket)[Upload files to Supabase Storage bucket ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#upload-to-supabase-storage-bucket)[Resources](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#resources)[Enterprise](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage#enterprise)
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



