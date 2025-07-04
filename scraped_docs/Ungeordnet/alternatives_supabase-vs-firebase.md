---
url: https://supabase.com/alternatives/supabase-vs-firebase
scraped_at: 2025-05-25T08:50:16.334299
title: Supabase vs Firebase
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
Alternative
# Supabase vs Firebase
2022-05-26
•
4 minute read
[![author avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Ant WilsonCTO and Co-Founder](https://github.com/awalias)
## What is Firebase?[#](https://supabase.com/alternatives/supabase-vs-firebase#what-is-firebase)
Now owned by Google, Firebase is a collection of tools aimed at mobile and web developers. At its core is the Firestore database.
Firestore allows you to store “documents”. These are collections of key:value pairs where the value can be another sub-document. Document based storage is perfect for unstructured data, since two documents in a collection do not necessarily need to have the same structure.
Firebase also offers other things that web developers find useful like an auth service for user management, and wrappers for other Google services such as Cloud Functions, and File Storage.
## What is Supabase?[#](https://supabase.com/alternatives/supabase-vs-firebase#what-is-supabase)
Supabase is an open source firebase alternative, but instead of being built around a document-based datastore, Supabase offers a relational database management system called PostgreSQL. This comes with a few advantages:
  * It’s open source, so there is zero lock in.
  * You can query it with SQL, a proven and powerful query language.
  * It has a long track record of being used at scale.
  * It’s the database of choice for transactional workloads (think apps and websites, or other things that require near-instant responses to queries).
  * It comes with decades of [useful postgres extensions and plug-ins](https://supabase.com/docs/guides/database/extensions).


At Supabase we’ve always been huge fans of Firebase - so we started adding a few things on top of PostgreSQL in an attempt to reach feature parity, including:
  * Auto-generated API - [query your data straight from the client](https://supabase.com/docs/guides/api#rest-api-overview).
  * Realtime - [changes in your data will be streamed directly to your application](https://supabase.com/docs/reference/dart/subscribe).
  * Auth - [a simple to integrate auth system and SQL based rules engine](https://supabase.com/auth).
  * Functions - [javascript and typescript functions that deploy out globally](https://supabase.com/edge-functions).
  * Storage - [hosting images, videos, and pdfs easily](https://supabase.com/storage).


## How are they similar?[#](https://supabase.com/alternatives/supabase-vs-firebase#how-are-they-similar)
Both Firebase and Supabase are based on the idea of bringing a superior developer experience to databases. With both platforms you can spin up a new project from directly inside the browser without the need to download any extra tools or software to your machine. Both platforms come with a useful dashboard UI for debugging your data in realtime, which is especially useful for fast iterations when in development.
Both Firebase and Supabase have invested heavily in client side libraries so you can communicate with your database directly from the client. Firebase has their [Firebase Javascript SDK](https://github.com/firebase/firebase-js-sdk) and Supabase has [supabase-js an isomorphic client](https://github.com/supabase/supabase-js/) that can be used both on the client also on the server in a node-js environment.
## How are they different?[#](https://supabase.com/alternatives/supabase-vs-firebase#how-are-they-different)
Firebase and Supabase differ in several ways. The main one being that Firebase is a document store, whereas Supabase is based on PostgreSQL - a relational, SQL-based database management system.
There are some other important differences.
### Open Source[#](https://supabase.com/alternatives/supabase-vs-firebase#open-source)
Supabase is open source. Along with the hosted cloud platform, you can also take the Supabase stack and host it inside your own cloud or run it locally on your machine. There is no vendor lock in.
### Pricing[#](https://supabase.com/alternatives/supabase-vs-firebase#pricing)
[Firebase charges for reads, writes and deletes](https://firebase.google.com/pricing), which can lead to some unpredictability, especially in the early stages of a project when your application is in heavy development. Supabase [charges based on the amount of data stored](https://supabase.com/pricing), with breathing room for unlimited API requests and an unlimited number of Auth users.
### Performance[#](https://supabase.com/alternatives/supabase-vs-firebase#performance)
We created a benchmarking repo where you can compare the performance of both services in different scenarios. Our most recent results show that [Supabase outperforms Firebase by up to 4x](https://github.com/supabase/benchmarks/issues/8) on number of reads per second, and 3.1x on writes per second.
## How do I migrate from Firebase to Supabase?[#](https://supabase.com/alternatives/supabase-vs-firebase#how-do-i-migrate-from-firebase-to-supabase)
Since Firebase is document based, migrating into a relational database requires you to map your data structure across into a SQL schema. Luckily we’ve built a [handy conversion tool to do it for you](https://supabase.com/docs/guides/migrations/firestore-data).
We also have guides and tools for [migrating Firebase Auth to Supabase Auth](https://supabase.com/docs/guides/migrations/firebase-auth) for [migrating Firebase Storage files to Supabase Storage](https://supabase.com/docs/guides/migrations/firebase-storage).
These are by far the most complete Firebase to Postgres migration tools available anywhere on the web.
You can [try Supabase for free](https://supabase.com/dashboard). If you require Enterprise level support with your project or migration, please get in touch using our [Enterprise contact form](https://forms.supabase.com/enterprise).
Share this article
[](https://twitter.com/share?text=Supabase vs Firebase&url=https://supabase.com/blog/supabase-vs-firebase)[](https://www.linkedin.com/shareArticle?url=https://supabase.com/blog/supabase-vs-firebase&title=Supabase vs Firebase)
[Previous comparisonSupabase vs Auth02023-11-24](https://supabase.com/alternatives/supabase-vs-auth0)
[Next comparisonSupabase vs Heroku Postgres2022-05-26](https://supabase.com/alternatives/supabase-vs-heroku-postgres)
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

