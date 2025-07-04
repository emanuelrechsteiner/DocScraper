---
url: https://supabase.com/blog/snaplet-is-now-open-source
scraped_at: 2025-05-25T08:38:12.654824
title: Snaplet is now open source
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
# Snaplet is now open source
14 Aug 2024
•
3 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Snaplet is now open source](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-3%2Fthumb-snaplet.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Startups are hard. One of our favorite startups, Snaplet, is [shutting down](https://www.snaplet.dev/post/snaplet-is-shutting-down). Despite that, they built an amazing team (some who now work at Supabase) and some incredible products.
One way to ensure that your products out-live your business is to open source what you've built. I'm a huge fan of what Snaplet built so I reached out to [Peter](https://x.com/appfactory/) to see if Snaplet were interested in open sourcing. He said yes:
> I built Snaplet because I believe developers write better software when they have access to production-like data. Although the company is closing, my belief remains strong, so we are open-sourcing the tools we've built.
> ![Peter Pistorius, Founder of Snaplet avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fpeter-snaplet.webp&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> Peter Pistorius, Founder of Snaplet
## Open source products[#](https://supabase.com/blog/snaplet-is-now-open-source#open-source-products)
There are 3 main tools that they are releasing under the MIT license:
### Copycat[#](https://supabase.com/blog/snaplet-is-now-open-source#copycat)
Copycat generates fake data. It's like faker.js, but deterministic: for any given input it'll always produce the same output. For example, if you generate an email with the user ID `user_1234`, the next time you generate an email with that email it will be the same, _guaranteed:_
![Fake data](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-3%2Fsnaplet-fake-data.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
  * Repo: [github.com/snaplet/copycat](https://github.com/snaplet/copycat)


### Snaplet Seed[#](https://supabase.com/blog/snaplet-is-now-open-source#snaplet-seed)
Seed generates realistic synthetic data based off a database schema. It automatically determines the values in your database so you don't have to define each value. For example, if you want to generate a 3 `comments` for one of your `posts` you simply point it at your schema and let it handle the rest:
![Seed data](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-3%2Fsnaplet-seed-data.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
  * Repo: [github.com/snaplet/seed](https://github.com/snaplet/seed)
  * Docs: [docs.snaplet.dev/seed](https://snaplet-seed.netlify.app/seed)


### Snapshot[#](https://supabase.com/blog/snaplet-is-now-open-source#snapshot)
Snapshot is for capturing, transforming, and restoring snapshots of your database. It's like an advanced version of pg_dump/pg_restore. It has a particularly neat feature called “subsetting”. Point it at a database table and it tell it how much data you need. To maintain referential integrity, subsetting traverses tables, selecting all the rows that are connected to the target table through foreign key relationships:
![Subset data](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-3%2Fsnaplet-subset.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
  * Repo: [github.com/snaplet/snapshot](https://github.com/snaplet/snapshot)
  * Docs: [docs.snaplet.dev/snapshot](https://snaplet-snapshot.netlify.app/snapshot)


## The future of Snaplet tech[#](https://supabase.com/blog/snaplet-is-now-open-source#the-future-of-snaplet-tech)
The Snaplet team who joined Supabase have been helping Peter to migrate these projects to open source. Over the next few weeks we'll move these into the Supabase GitHub org and pick up the ongoing maintenance.
We prefer to keep products decoupled (it's one of our [Principles](https://supabase.com/docs/guides/getting-started/architecture#everything-works-in-isolation)), so you'll always be able to use these tools independently from Supabase. We can also see a lot of value providing a deep integration, so we've already started adding their [Snaplet Seed](https://supabase.com/docs/guides/local-development/seeding-your-database#generating-seed-data) to our official docs. This is just a start, watch this space!
## Where's Peter now?[#](https://supabase.com/blog/snaplet-is-now-open-source#wheres-peter-now)
Peter is back at [RedwoodJS](https://redwoodjs.com/), which he co-founded before Snaplet. He's been working on React Server Components, coming soon to Redwood.
[Launch Week12](https://supabase.com/launch-week/12)
12-16 August
[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage
[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)[02 -pg_replicate](https://news.ycombinator.com/item?id=41209994)[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)[06 -vec2pg](https://supabase.com/blog/vec2pg)[07 -pg_graphql](https://supabase.com/blog/pg-graphql-1-5-7)[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)[09 -python-support](https://supabase.com/blog/python-support)[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsnaplet-is-now-open-source&text=Snaplet%20is%20now%20open%20source)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsnaplet-is-now-open-source&text=Snaplet%20is%20now%20open%20source)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsnaplet-is-now-open-source&t=Snaplet%20is%20now%20open%20source)
[Last postpg_graphql 1.5.7: pagination and multi-tenancy support15 August 2024](https://supabase.com/blog/pg-graphql-1-5-7)
[Next postSupabase Auth: Bring-your-own Auth0, Cognito, or Firebase14 August 2024](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)
[engineering](https://supabase.com/blog/tags/engineering)
On this page
  * [Open source products](https://supabase.com/blog/snaplet-is-now-open-source#open-source-products)
    * [Copycat](https://supabase.com/blog/snaplet-is-now-open-source#copycat)
    * [Snaplet Seed](https://supabase.com/blog/snaplet-is-now-open-source#snaplet-seed)
    * [Snapshot](https://supabase.com/blog/snaplet-is-now-open-source#snapshot)
  * [The future of Snaplet tech](https://supabase.com/blog/snaplet-is-now-open-source#the-future-of-snaplet-tech)
  * [Where's Peter now?](https://supabase.com/blog/snaplet-is-now-open-source#wheres-peter-now)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsnaplet-is-now-open-source&text=Snaplet%20is%20now%20open%20source)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsnaplet-is-now-open-source&text=Snaplet%20is%20now%20open%20source)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsnaplet-is-now-open-source&t=Snaplet%20is%20now%20open%20source)
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

