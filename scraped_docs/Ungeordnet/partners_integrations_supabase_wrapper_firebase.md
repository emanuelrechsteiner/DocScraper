---
url: https://supabase.com/partners/integrations/supabase_wrapper_firebase
scraped_at: 2025-05-25T09:17:40.259507
title: Firebase Wrapper | Works With Supabase
---

  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
  * Product 
  * Developers 
  * [Enterprise](https://supabase.com/enterprise)
  * [Pricing](https://supabase.com/pricing)
  * [Docs](https://supabase.com/docs)
  * [Blog](https://supabase.com/blog)


[83.3K](https://github.com/supabase/supabase)[Sign in](https://supabase.com/dashboard)[Start your project](https://supabase.com/dashboard)
Open main menu
[Back](https://supabase.com/partners/integrations)
![Firebase Wrapper](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Ffirebase%2Ffirebase-logo-256.webp&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Firebase Wrapper
## Overview
[Firebase](https://firebase.google.com/) is an app development platform built around non-relational technologies. The Firebase Wrapper supports connecting to below objects.
  1. [Authentication Users](https://firebase.google.com/docs/auth/users) (_read only_)
  2. [Firestore Database Documents](https://firebase.google.com/docs/firestore) (_read only_)


## Preparation
Before you get started, make sure the `wrappers` extension is installed on your database:
`
1
create extension if not exists wrappers with schema extensions;
`
and then create the foreign data wrapper:
`
1
create foreign data wrapper firebase_wrapper
2
 handler firebase_fdw_handler
3
 validator firebase_fdw_validator;
`
### Secure your credentials (optional)
By default, Postgres stores FDW credentials inide `pg_catalog.pg_foreign_server` in plain text. Anyone with access to this table will be able to view these credentials. Wrappers is designed to work with [Vault](https://supabase.com/docs/guides/database/vault), which provides an additional level of security for storing credentials. We recommend using Vault to store your credentials.
`
1
-- Save your Firebase credentials in Vault and retrieve the `key_id`
2
insert into vault.secrets (name, secret)
3
values (
4
 'firebase',
5
 '{
6
   "type": "service_account",
7
   "project_id": "your_gcp_project_id",
8
   ...
9
 }'
10
)
11
returning key_id;
`
### Connecting to Firebase
We need to provide Postgres with the credentials to connect to Firebase, and any additional options. We can do this using the `create server` command:
=== "With Vault"
`
1
create server firebase_server
2
 foreign data wrapper firebase_wrapper
3
 options (
4
  sa_key_id '<key_ID>', -- The Key ID from above.
5
  project_id '<firebase_project_id>'
6
);
`
=== "Without Vault"
`
1
create server firebase_server
2
 foreign data wrapper firebase_wrapper
3
  options (
4
   sa_key '
5
   {
6
    "type": "service_account",
7
    "project_id": "your_gcp_project_id",
8
    ...
9
   }
10
  ',
11
   project_id 'firebase_project_id'
12
  );
`
Learn more on our [doc page](https://supabase.com/docs/guides/database/extensions/wrappers/firebase).
## Resources
  * Official [`supabase/wrappers` documentation](https://supabase.github.io/wrappers/)


## Details
DeveloperSupabase
Category[Foreign Data Wrapper](https://supabase.com/partners/integrations#foreign%20data%20wrapper)
Website[supabase.com](https://supabase.com/docs/guides/database/extensions/wrappers/firebase)
Documentation[Learn](https://supabase.com/docs/guides/database/extensions/wrappers/firebase)
Third-party integrations and docs are managed by Supabase partners.
## Footer
We protect your data.[More on Security](https://supabase.com/security)
  * SOC2 Type 2 Certified
  * HIPAA Compliant


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)
###### Product
  * [Database](https://supabase.com/database)
  * [Auth](https://supabase.com/auth)
  * [Functions](https://supabase.com/edge-functions)
  * [Realtime](https://supabase.com/realtime)
  * [Storage](https://supabase.com/storage)
  * [Vector](https://supabase.com/modules/vector)
  * [Cron](https://supabase.com/modules/cron)
  * [Pricing](https://supabase.com/pricing)
  * [Launch Week](https://supabase.com/launch-week)
  * [AI Builders](https://supabase.com/solutions/ai-builders)


###### Resources
  * [Support](https://supabase.com/support)
  * [System Status](https://status.supabase.com/)
  * [Become a Partner](https://supabase.com/partners)
  * [Integrations](https://supabase.com/partners/integrations)
  * [Brand Assets / Logos](https://supabase.com/brand-assets)
  * [Security and Compliance](https://supabase.com/security)
  * [DPA](https://supabase.com/legal/dpa)
  * [SOC2](https://supabase.com/security)
  * [HIPAA](https://forms.supabase.com/hipaa2)


###### Developers
  * [Documentation](https://supabase.com/docs)
  * [Supabase UI](https://supabase.com/ui)
  * [Changelog](https://supabase.com/changelog)
  * [Contributing](https://github.com/supabase/supabase/blob/master/CONTRIBUTING.md)
  * [Open Source](https://supabase.com/open-source)
  * [SupaSquad](https://supabase.com/supasquad)
  * [DevTo](https://dev.to/supabase)
  * [RSS](https://supabase.com/rss.xml)


###### Company
  * [Blog](https://supabase.com/blog)
  * [Customer Stories](https://supabase.com/customers)
  * [Careers](https://supabase.com/careers)
  * [Company](https://supabase.com/company)
  * [Events & Webinars](https://supabase.com/events)
  * [General Availability](https://supabase.com/ga)
  * [Terms of Service](https://supabase.com/terms)
  * [Privacy Policy](https://supabase.com/privacy)
  * Privacy Settings
  * [Acceptable Use Policy](https://supabase.com/aup)
  * [Support Policy](https://supabase.com/support-policy)
  * [Service Level Agreement](https://supabase.com/sla)
  * [Humans.txt](https://supabase.com/humans.txt)
  * [Lawyers.txt](https://supabase.com/lawyers.txt)
  * [Security.txt](https://supabase.com/.well-known/security.txt)


© Supabase Inc
Toggle theme

