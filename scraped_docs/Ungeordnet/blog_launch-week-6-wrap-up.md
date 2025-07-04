---
url: https://supabase.com/blog/launch-week-6-wrap-up
scraped_at: 2025-05-25T09:15:44.431972
title: Launch Week 6: Wrap Up
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
[Back](https://supabase.com/blog)
[Blog](https://supabase.com/blog)
# Launch Week 6: Wrap Up
16 Dec 2022
•
6 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Launch Week 6: Wrap Up](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fwrap-up%2Fog-wrap-up.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
That's a wrap on Supabase Launch Week Day 6. Here's everything we shipped in one long blog post.
## New Docs, built with Next.js[#](https://supabase.com/blog/launch-week-6-wrap-up#new-docs-built-with-nextjs)
![New Docs, built with Next.js](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-day-1%2Flw6-day1-docs.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Monday
For a developer tool, documentation is more than a resource - it's part of the product. For the past two years at Supabase, this part of our product hasn't been great. Our new docs, built with Next.js, feature a completely new design, better navigation, and the promise of a fully-integrated experience.
  * Read the [announcement](https://supabase.com/blog/new-supabase-docs-built-with-nextjs)
  * Watch the [recap on YouTube](https://www.youtube.com/watch?v=Q1Amk6iDlF8)
  * Check out [the new docs](https://supabase.com/docs)


## Storage v2: Image resizing and Smart CDN[#](https://supabase.com/blog/launch-week-6-wrap-up#storage-v2-image-resizing-and-smart-cdn)
![Storage v2: Image resizing and Smart CDN](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-storage%2FImage-resizing.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Tuesday
We're introducing three new features for Supabase Storage: Image resizing, webhooks, and a Smart CDN. These features are designed to work together to deliver a next-gen image resizing system.
  * Read the [announcement](https://supabase.com/blog/storage-image-resizing-smart-cdn)
  * Watch the [recap on YouTube](https://www.youtube.com/watch?v=NpEl20iuOtg)
  * Browse the docs for [Image Transformations](https://supabase.com/docs/guides/storage/serving/image-transformations)
  * Browse the docs for our [Smart CDN](https://supabase.com/docs/guides/storage/cdn/smart-cdn)
  * Discuss it on [HackerNews](https://news.ycombinator.com/item?id=33969076)


## Auth: Multi-factor Authentication with RLS[#](https://supabase.com/blog/launch-week-6-wrap-up#auth-multi-factor-authentication-with-rls)
![Auth: Multi-factor Authentication with RLS](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-auth%2Fmfa-banner.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Wednesday
We released Multi Factor Authentication for you to build more secure applications. We built a unique twist so that you can use MFA within your Row Level Security Policies.
  * Read the [announcement](https://supabase.com/blog/mfa-auth-via-rls)
  * Watch the [recap on YouTube](https://www.youtube.com/watch?v=He7LI2mv9v0)
  * Browse the [docs](https://supabase.com/docs/guides/auth/auth-mfa)
  * Discuss it on [HackerNews](https://news.ycombinator.com/item?id=33984104)


## Wrappers, a FDW framework for Postgres[#](https://supabase.com/blog/launch-week-6-wrap-up#wrappers-a-fdw-framework-for-postgres)
![Wrappers, a FDW framework for Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fwrappers%2Fwrappers-og.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Thursday
We announced [Supabase Wrappers](https://github.com/supabase/wrappers), a framework for building Postgres Foreign Data Wrappers (FDW) which connects Postgres to external systems. We're releasing Wrappers today in Alpha, with support for Firebase and Stripe. Wrappers for Clickhouse, BigQuery, and Airtable are under development.
  * Read the [announcement](https://supabase.com/blog/postgres-foreign-data-wrappers-rust)
  * Watch the [recap on YouTube](https://www.youtube.com/watch?v=He7LI2mv9v0)
  * Browse the [docs](https://supabase.github.io)
  * Discuss it on [HackerNews](https://news.ycombinator.com/item?id=34001493)


## Vault: secrets and encryption in Postgres[#](https://supabase.com/blog/launch-week-6-wrap-up#vault-secrets-and-encryption-in-postgres)
![Vault: secrets and encryption in Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fvault%2Fog-vault.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Friday
Vault is a new Postgres extension and accompanying Supabase UI that makes it safe and easy to store encrypted secrets and encrypt other stored data in your database. We're releasing it progressively across the platform and you can expect to see it appear in the Supabase Dashboard in the coming weeks.
  * Read the [announcement](https://supabase.com/blog/vault-now-in-beta)
  * Learn about [Transparent Column Encryption](https://supabase.com/blog/transparent-column-encryption-with-postgres)


## pg_graphql v1: GraphQL in Postgres[#](https://supabase.com/blog/launch-week-6-wrap-up#pg_graphql-v1-graphql-in-postgres)
![pg_graphql v1: GraphQL in Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fpggraphql%2Fog-pg-graphql.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One more thing
Today released pg_graphql 1.0 release and its general availability on our platform. pg_graphql is a PostgreSQL extension that allows you to query your database using GraphQL. It is the foundation of GraphQL support in the Supabase stack.
  * Read the [announcement](https://supabase.com/blog/pg-graphql-v1)
  * Browse the [GitHub repo](https://github.com/supabase/pg_graphql/)
  * View the [docs](https://supabase.com/docs/guides/api#graphql-api-overview)


## Postgres Point-in-Time Recovery[#](https://supabase.com/blog/launch-week-6-wrap-up#postgres-point-in-time-recovery)
![FDW](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fpitr%2Fog-pitr.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One more thing
Point In Time Recovery (PITR) is now enabled from the dashboard for Pro Projects. With PITR, you can restore your database at any specified time in the past.
  * Read the [announcement](https://supabase.com/blog/postgres-point-in-time-recovery)
  * Review the [Production Readiness docs](https://supabase.com/docs/guides/platform/going-into-prod)


## Custom domains[#](https://supabase.com/blog/launch-week-6-wrap-up#custom-domains)
![FDW](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fcustom-domains%2Fog-custom-domains.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One more thing
Custom domains allow you to use your own domain for your Supabase project. We've released custom domains as an upgrade option for all projects, and vanity domains for Pro projects.
  * Read the [announcement](https://supabase.com/blog/custom-domain-names)
  * Visit the [Custom Domains docs](https://supabase.com/docs/guides/platform/custom-domains)


## pg_crdt: a Postgres extension for CRDTs[#](https://supabase.com/blog/launch-week-6-wrap-up#pg_crdt-a-postgres-extension-for-crdts)
![pg_crdt: a Postgres extension for CRDTs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fcrdt%2Fog-pg-crdt.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One more thing
We open-sourced an experimental extension for CRDTs, pg_crdt. If you're familiar with Yjs or Automerge, then check out the work we're doing here. It's a PostgreSQL extension that allows you to use CRDTs in your database.
  * Read the [announcement](https://supabase.com/blog/postgres-crdt)
  * Browse the [GitHub repo](https://github.com/supabase/pg_crdt)
  * Discuss it on [HackerNews](https://news.ycombinator.com/item?id=33931971)


## PostgreSQL 15: we support it[#](https://supabase.com/blog/launch-week-6-wrap-up#postgresql-15-we-support-it)
![PostgreSQL 15: we support it](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-community%2Fpg15.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One more thing
All new projects created on the Supabase platform are now on version 15. The PostgreSQL community released version 15 (stable) in October 2022.
  * Learn what's [new in PostgreSQL 15](https://supabase.com/blog/new-in-postgres-15)
  * View the full PostgreSQL 15 [release notes](https://www.postgresql.org/docs/15/release-15.html)


## PostgREST 11: pre-release[#](https://supabase.com/blog/launch-week-6-wrap-up#postgrest-11-pre-release)
![PostgREST 11: pre-release](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-community%2Fpostgrest.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One more thing
You can now test the PostgREST 11 pre-release locally with the Supabase CLI. Some of the new features include: spreading related tables, related orders and anti-joins.
  * Learn more about [PostgREST 11](https://supabase.com/blog/postgrest-11-prerelease)
  * Visit the [CLI docs](https://supabase.com/docs/guides/resources/supabase-cli)


## Multilingual search in Postgres[#](https://supabase.com/blog/launch-week-6-wrap-up#multilingual-search-in-postgres)
![Multilingual search in Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-community%2Fpgroonga.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One more thing
We've released a new multilingual Full Text Search extension, PGroonga. It's fast, it's open source, and it's available on our platform today. If you've ever wanted to build a search engine for your app, then check out PGroonga.
  * Visit the [PGroonga website](https://pgroonga.github.io)
  * Read the [Extensions Docs](https://supabase.com/docs/guides/database/extensions)


## Flutterflow for Flutter App Development[#](https://supabase.com/blog/launch-week-6-wrap-up#flutterflow-for-flutter-app-development)
Community Spotlight
We partnered with the team at [Flutterflow](https://flutterflow.io/) to bring you a new way to build Flutter apps. Flutterflow is a low-code platform that allows you to build Flutter apps without writing any code. It's a great way to get started with Flutter and Supabase.
  * Watch the [tutorial](https://www.youtube.com/watch?v=hw9Q-NjASbU)
  * Get Started with [Flutterflow](https://flutterflow.io/)


## OneSignal for Push Notifications[#](https://supabase.com/blog/launch-week-6-wrap-up#onesignal-for-push-notifications)
Community Spotlight
We partnered with the team at [OneSignal](https://onesignal.com/) to offer push notifications in Supabase. OneSignal is a messaging platform allowing you to deliver push notifications, in-app messages, SMS, and emails to your users.
  * Watch the [tutorial](https://www.youtube.com/watch?v=mw0DLwItue4)
  * Get Started with [OneSignal](https://onesignal.com/)


## Getting Started[#](https://supabase.com/blog/launch-week-6-wrap-up#getting-started)
Get started today with Supabase. It's free and open source.
  * [Like some memes on Twitter](https://twitter.com/supabase)
  * [Star us on GitHub](https://github.com/supabase/supabase)
  * [Join the Discord](https://discord.supabase.com)
  * [Read the docs](https://supabase.com/docs)
  * [Sign up](https://app.supabase.io/)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-6-wrap-up&text=Launch%20Week%206%3A%20Wrap%20Up)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-6-wrap-up&text=Launch%20Week%206%3A%20Wrap%20Up)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-6-wrap-up&t=Launch%20Week%206%3A%20Wrap%20Up)
[Last postCommunity Day16 December 2022](https://supabase.com/blog/launch-week-6-community-day)
[Next postWhat's new in Postgres 15?16 December 2022](https://supabase.com/blog/new-in-postgres-15)
[launch-week](https://supabase.com/blog/tags/launch-week)
On this page
  * [New Docs, built with Next.js](https://supabase.com/blog/launch-week-6-wrap-up#new-docs-built-with-nextjs)
  * [Storage v2: Image resizing and Smart CDN](https://supabase.com/blog/launch-week-6-wrap-up#storage-v2-image-resizing-and-smart-cdn)
  * [Auth: Multi-factor Authentication with RLS](https://supabase.com/blog/launch-week-6-wrap-up#auth-multi-factor-authentication-with-rls)
  * [Wrappers, a FDW framework for Postgres](https://supabase.com/blog/launch-week-6-wrap-up#wrappers-a-fdw-framework-for-postgres)
  * [Vault: secrets and encryption in Postgres](https://supabase.com/blog/launch-week-6-wrap-up#vault-secrets-and-encryption-in-postgres)
  * [pg_graphql v1: GraphQL in Postgres](https://supabase.com/blog/launch-week-6-wrap-up#pg_graphql-v1-graphql-in-postgres)
  * [Postgres Point-in-Time Recovery](https://supabase.com/blog/launch-week-6-wrap-up#postgres-point-in-time-recovery)
  * [Custom domains](https://supabase.com/blog/launch-week-6-wrap-up#custom-domains)
  * [pg_crdt: a Postgres extension for CRDTs](https://supabase.com/blog/launch-week-6-wrap-up#pg_crdt-a-postgres-extension-for-crdts)
  * [PostgreSQL 15: we support it](https://supabase.com/blog/launch-week-6-wrap-up#postgresql-15-we-support-it)
  * [PostgREST 11: pre-release](https://supabase.com/blog/launch-week-6-wrap-up#postgrest-11-pre-release)
  * [Multilingual search in Postgres](https://supabase.com/blog/launch-week-6-wrap-up#multilingual-search-in-postgres)
  * [Flutterflow for Flutter App Development](https://supabase.com/blog/launch-week-6-wrap-up#flutterflow-for-flutter-app-development)
  * [OneSignal for Push Notifications](https://supabase.com/blog/launch-week-6-wrap-up#onesignal-for-push-notifications)
  * [Getting Started](https://supabase.com/blog/launch-week-6-wrap-up#getting-started)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-6-wrap-up&text=Launch%20Week%206%3A%20Wrap%20Up)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-6-wrap-up&text=Launch%20Week%206%3A%20Wrap%20Up)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-6-wrap-up&t=Launch%20Week%206%3A%20Wrap%20Up)
## Build in a weekend, scale to millions
[Start your project](https://supabase.com/dashboard)[Request a demo](https://supabase.com/contact/sales)
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

