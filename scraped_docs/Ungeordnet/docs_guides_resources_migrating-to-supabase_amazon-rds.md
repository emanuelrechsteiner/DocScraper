---
url: https://supabase.com/docs/guides/resources/migrating-to-supabase/amazon-rds
scraped_at: 2025-05-25T09:49:49.309200
title: Migrate from Amazon RDS to Supabase | Supabase Docs
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
  4. [Amazon RDS](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds)


Migrate from Amazon RDS to Supabase
Migrate your Amazon RDS MySQL or MS SQL database to Supabase.
This guide aims to exhibit the process of transferring your Amazon RDS database from any of these engines Postgres, MySQL or MS SQL to Supabase's Postgres database. Although Amazon RDS is a favored managed database service provided by AWS, it may not suffice for all use cases. Supabase, on the other hand, provides an excellent free and open source option that encompasses all the necessary backend features to develop a product: a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage.
Supabase's core is Postgres, enabling the use of row-level security and providing access to over 40 Postgres extensions. By migrating from Amazon RDS to Supabase, you can leverage Postgres to its fullest potential and acquire all the features you need to complete your project.
## Retrieve your Amazon RDS database credentials [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds#retrieve-rds-credentials)
  1. Log in to your [Amazon RDS account](https://aws.amazon.com/rds/).
  2. Select the region where your RDS database is located.
  3. Navigate to the **Databases** tab.
  4. Select the database that you want to migrate.
  5. In the **Connectivity & Security** tab, note down the Endpoint and the port number.
  6. In the **Configuration** tab, note down the Database name and the Username.
  7. If you do not have the password, create a new one and note it down.


![Copying RDS credentials from AWS Management Console](https://supabase.com/docs/img/guides/resources/migrating-to-supabase/amazon-rds/amazon-rds_credentials.png)
## Retrieve your Supabase host [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds#retrieve-supabase-host)
  1. If you're new to Supabase, [create a project](https://database.new). Make a note of your password, you will need this later. If you forget it, you can [reset it here](https://supabase.com/dashboard/project/_/settings/database).
  2. On your project dashboard, click [Connect](https://supabase.com/dashboard/project/_?showConnect=true)
  3. Under the Session pooler, click on the View parameters under the connect string. Note your Host (`$SUPABASE_HOST`).


![Finding Supabase host address](https://supabase.com/docs/img/guides/resources/migrating-to-supabase/amazon-rds/database-settings-host.png)
## Migrate the database[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds#migrate-the-database)
The fastest way to migrate your database is with the Supabase migration tool on [Google Colab](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb).
Alternatively, you can use [pgloader](https://github.com/dimitri/pgloader), a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the [`pg_dump`](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full Postgres installation.
Migrate using ColabMigrate from MySQL with pgloaderMigrate from MSSQL
  1. Select the Database Engine from the Source database in the dropdown
  2. Set the environment variables (`HOST`, `USER`, `SOURCE_DB`,`PASSWORD`, `SUPABASE_URL`, and `SUPABASE_PASSWORD`) in the Colab notebook.
  3. Run the first two steps in [the notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb) in order. The first sets engine and installs the necessary files.
  4. Run the third step to start the migration. This will take a few minutes.


  * If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](https://supabase.com/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.
  * For databases smaller than 150 GB, you can increase the size of the disk on paid projects by navigating to the [Compute and Disk Settings](https://supabase.com/docs/guides/platform/migrating-to-supabase/dashboard/project/_/settings/compute-and-disk) page.
  * If you're dealing with a database larger than 150 GB, we strongly advise you to [contact our support team](https://supabase.com/dashboard/support/new) for assistance in provisioning the required resources and ensuring a smooth migration process.


## Enterprise[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds#enterprise)
[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/platform/migrating-to-supabase/amazon-rds.mdx)
### Is this helpful?
No Yes
### On this page
[Retrieve your Amazon RDS database credentials ](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds#retrieve-rds-credentials)[Retrieve your Supabase host ](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds#retrieve-supabase-host)[Migrate the database](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds#migrate-the-database)[Enterprise](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds#enterprise)
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



