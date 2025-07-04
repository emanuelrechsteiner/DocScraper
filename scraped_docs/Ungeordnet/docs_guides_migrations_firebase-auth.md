---
url: https://supabase.com/docs/guides/migrations/firebase-auth
scraped_at: 2025-05-25T08:38:05.667633
title: Migrate from Firebase Auth to Supabase | Supabase Docs
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
  4. [Firebase Auth](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth)


Migrate from Firebase Auth to Supabase
Migrate Firebase auth users to Supabase Auth.
Supabase provides several [tools](https://github.com/supabase-community/firebase-to-supabase/tree/main/auth) to help migrate auth users from a Firebase project to a Supabase project. There are two parts to the migration process:
  * `firestoreusers2json` ([TypeScript](https://github.com/supabase-community/firebase-to-supabase/blob/main/auth/firestoreusers2json.ts), [JavaScript](https://github.com/supabase-community/firebase-to-supabase/blob/main/auth/firestoreusers2json.js)) exports users from an existing Firebase project to a `.json` file on your local system.
  * `import_users` ([TypeScript](https://github.com/supabase-community/firebase-to-supabase/blob/main/auth/import_users.ts), [JavaScript](https://github.com/supabase-community/firebase-to-supabase/blob/main/auth/import_users.js)) imports users from a saved `.json` file into your Supabase project (inserting those users into the `auth.users` table of your `Postgres` database instance).


## Set up the migration tool [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#set-up-migration-tool)
  1. Clone the [`firebase-to-supabase`](https://github.com/supabase-community/firebase-to-supabase) repository:
```

1
gitclonehttps://github.com/supabase-community/firebase-to-supabase.git

```

  2. In the `/auth` directory, create a file named `supabase-service.json` with the following contents:
```

1
2
3
4
5
6
7
{"host":"database.server.com","password":"secretpassword","user":"postgres","database":"postgres","port":5432}

```

  3. On your project dashboard, click [Connect](https://supabase.com/dashboard/project/_?showConnect=true)
  4. Under the Session pooler, click on the View parameters under the connect string. Replace the `Host` and `User` fields with the values shown.
  5. Enter the password you used when you created your Supabase project in the `password` entry in the `supabase-service.json` file.


## Generate a Firebase private key [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#generate-firebase-private-key)
  1. Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project.
  2. Click the gear icon next to **Project Overview** in the sidebar and select **Project Settings**.
  3. Click **Service Accounts** and select **Firebase Admin SDK**.
  4. Click **Generate new private key**.
  5. Rename the downloaded file to `firebase-service.json`.


## Save your Firebase password hash parameters [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#save-firebase-hash-parameters)
  1. Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project.
  2. Select **Authentication** (Build section) in the sidebar.
  3. Select **Users** in the top menu.
  4. At the top right of the users list, open the menu (3 dots) and click **Password hash parameters**.
  5. Copy and save the parameters for `base64_signer_key`, `base64_salt_separator`, `rounds`, and `mem_cost`.


```

1
2
3
4
5
6
7
hash_config { algorithm: SCRYPT, base64_signer_key: XXXX/XXX+XXXXXXXXXXXXXXXXX+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==, base64_salt_separator: Aa==, rounds: 8, mem_cost: 14,}

```

## Command line options[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#command-line-options)
### Dump Firestore users to a JSON file [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#dump-firestore-users)
`node firestoreusers2json.js [<filename.json>] [<batch_size>]`
  * `filename.json`: (optional) output filename (defaults to `./users.json`)
  * `batchSize`: (optional) number of users to fetch in each batch (defaults to 100)


### Import JSON users file to Supabase Auth (Postgres: `auth.users`[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#import-json-users-file)
`node import_users.js <path_to_json_file> [<batch_size>]`
  * `path_to_json_file`: full local path and filename of JSON input file (of users)
  * `batch_size`: (optional) number of users to process in a batch (defaults to 100)


## Notes[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#notes)
For more advanced migrations, including the use of a middleware server component for verifying a user's existing Firebase password and updating that password in your Supabase project the first time a user logs in, see the [`firebase-to-supabase` repo](https://github.com/supabase-community/firebase-to-supabase/tree/main/auth).
## Resources[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#resources)
  * [Supabase vs Firebase](https://supabase.com/alternatives/supabase-vs-firebase)
  * [Firestore Data Migration](https://supabase.com/docs/guides/migrations/firestore-data)
  * [Firestore Storage Migration](https://supabase.com/docs/guides/migrations/firebase-storage)


## Enterprise[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#enterprise)
[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/platform/migrating-to-supabase/firebase-auth.mdx)
### Is this helpful?
No Yes
### On this page
[Set up the migration tool ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#set-up-migration-tool)[Generate a Firebase private key ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#generate-firebase-private-key)[Save your Firebase password hash parameters ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#save-firebase-hash-parameters)[Command line options](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#command-line-options)[Dump Firestore users to a JSON file ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#dump-firestore-users)[Import JSON users file to Supabase Auth (Postgres: auth.users](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#import-json-users-file)[Notes](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#notes)[Resources](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#resources)[Enterprise](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth#enterprise)
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



