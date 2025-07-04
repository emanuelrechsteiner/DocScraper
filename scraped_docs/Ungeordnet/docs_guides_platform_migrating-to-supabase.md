---
url: https://supabase.com/docs/guides/platform/migrating-to-supabase
scraped_at: 2025-05-25T09:37:50.990575
title: Migrating to Supabase | Supabase Docs
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
  2. Upgrades & Migrations
  3. [Migrating to Supabase](https://supabase.com/docs/guides/platform/migrating-to-supabase)


Migrating to Supabase
Learn how to migrate to Supabase from another database service.
## Migration guides[#](https://supabase.com/docs/guides/platform/migrating-to-supabase#migration-guides)
[![Auth0](https://supabase.com/docs/img/icons/auth0-icon-light.svg)Auth0](https://supabase.com/docs/guides/platform/migrating-to-supabase/auth0)[![Firebase Auth](https://supabase.com/docs/img/icons/firebase-icon.svg)Firebase Auth](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth)[![Firestore Data](https://supabase.com/docs/img/icons/firebase-icon.svg)Firestore Data](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data)[![Firebase Storage](https://supabase.com/docs/img/icons/firebase-icon.svg)Firebase Storage](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage)[![Heroku](https://supabase.com/docs/img/icons/heroku-icon.svg)Heroku](https://supabase.com/docs/guides/platform/migrating-to-supabase/heroku)[![Render](https://supabase.com/docs/img/icons/render-icon.svg)Render](https://supabase.com/docs/guides/platform/migrating-to-supabase/render)[![Amazon RDS](https://supabase.com/docs/img/icons/aws-rds-icon.svg)Amazon RDS](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds)[![Postgres](https://supabase.com/docs/img/icons/postgres-icon.svg)Postgres](https://supabase.com/docs/guides/platform/migrating-to-supabase/postgres)[![Vercel Postgres](https://supabase.com/docs/img/icons/vercel-icon-light.svg)Vercel Postgres](https://supabase.com/docs/guides/platform/migrating-to-supabase/vercel-postgres)[![Neon](https://supabase.com/docs/img/icons/neon-icon-light.svg)Neon](https://supabase.com/docs/guides/platform/migrating-to-supabase/neon)[![MySQL](https://supabase.com/docs/img/icons/mysql-icon.svg)MySQL](https://supabase.com/docs/guides/platform/migrating-to-supabase/mysql)[![MSSQL](https://supabase.com/docs/img/icons/mssql-icon.svg)MSSQL](https://supabase.com/docs/guides/platform/migrating-to-supabase/mssql)
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/platform/migrating-to-supabase.mdx)
### Is this helpful?
No Yes
### On this page
[Migration guides](https://supabase.com/docs/guides/platform/migrating-to-supabase#migration-guides)
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



