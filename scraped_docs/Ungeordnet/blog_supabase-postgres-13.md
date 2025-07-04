---
url: https://supabase.com/blog/supabase-postgres-13
scraped_at: 2025-05-25T09:12:54.709147
title: Supabase is now on Postgres 13.3
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
# Supabase is now on Postgres 13.3
26 Jul 2021
•
5 minute read
[![Angelico de los Reyes avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdragarcia.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Angelico de los ReyesEngineering](https://github.com/dragarcia)
![Supabase is now on Postgres 13.3](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpg13%2Fpostgres-13-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
From today, new Supabase projects will be on a version of [Supabase Postgres](https://github.com/supabase/postgres) that runs on [Postgres 13.3](https://www.postgresql.org/about/news/postgresql-13-released-2077/). This won't be the only big change however in this version. Here are a few other things that have changed under the hood.
## PostgreSQL version 13.3[#](https://supabase.com/blog/supabase-postgres-13#postgresql-version-133)
We've jumped from PostgreSQL 12.0 to PostgreSQL [version 13.3](https://www.postgresql.org/docs/13/release-13-3.html), introducing significant performance improvements and some great new functionality. Some changes include:
  * native [UUID generation](https://www.postgresql.org/docs/13/functions-uuid.html) (!) using `gen_random_uuid`
  * a new JSONB [datetime](https://www.postgresql.org/docs/13/functions-json.html) function
  * vacuuming indexes in [parallel](https://www.postgresql.org/docs/13/sql-vacuum.html)
  * [incremental sorting](https://www.postgresql.org/docs/13/using-explain.html#USING-EXPLAIN-BASICS)
  * smaller [btree indexes](https://www.postgresql.org/docs/13/btree-implementation.html#BTREE-DEDUPLICATION)
  * improvements to [extended statistics](https://www.postgresql.org/docs/13/planner-stats.html#PLANNER-STATS-EXTENDED)


## Supabase Versioning[#](https://supabase.com/blog/supabase-postgres-13#supabase-versioning)
Our [Postgres repo](https://github.com/supabase/postgres) has jumped from `0.15.0` to `13.3.0`. From now on, both major and minor versions of Supabase Postgres will follow PostgreSQL. This makes it much easier to ascertain what version of PostgreSQL is installed. In the situation wherein there are no updates to PostgreSQL in between releases, the patch version will be bumped up.
## Large System Extensions (LSE) enabled for ARM instances[#](https://supabase.com/blog/supabase-postgres-13#large-system-extensions-lse-enabled-for-arm-instances)
_Disclaimer for self-hosting: This is not available for x86 instances. All instances on the Supabase platform have this enabled by default._
The recent wave of Graviton 2 instances from AWS introduces support for the Large System Extensions (LSE). This looks to greatly enhance application performance through atomics, and [improves locking and synchronization performance across large systems](https://github.com/aws/aws-graviton-getting-started#building-for-graviton-and-graviton2).
### Preliminary Benchmarks[#](https://supabase.com/blog/supabase-postgres-13#preliminary-benchmarks)
Below is a comparison between the ARM versions of Supabase Postgres `0.15.0` and `13.3.0`. Both are using `m6gd.8xlarge` instances and follow the PostgreSQL configuration [here](https://www.percona.com/blog/2021/01/22/postgresql-on-arm-based-aws-ec2-instances-is-it-any-good/). The following configuration of `pgbench` was used.
hideCopy
`
1
pgbench -i -s 150
`
Running the benchmark with 2, 4, 8, 16, 64, and 128 clients:
hideCopy
`
1
pgbench -P 5 -c {num_clients} -j {num_clients} -T 300 -M prepared postgres
`
![PostgreSQL 13.3 performance](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpg13%2Fpostgres-13-performance.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Ubuntu 20.04[#](https://supabase.com/blog/supabase-postgres-13#ubuntu-2004)
We have taken the opportunity to upgrade new projects from Ubuntu 18.04 to Ubuntu 20.04. A switch to Ubuntu 20.04 guarantees that the underlying OS of Supabase Postgres is supported by the Canonical team up until the year 2025 (2023 for Ubuntu 18.04).
## Built from source[#](https://supabase.com/blog/supabase-postgres-13#built-from-source)
Driven by the need to enable LSE, the underlying PostgreSQL in this version was built from the ground up instead of downloaded binaries. Supabase Postgres can now be easily upgraded whenever a new major or minor version of PostgreSQL is released. When PostgreSQL 14 comes out, expect Supabase Postgres 14 to quickly follow.
## New Extensions[#](https://supabase.com/blog/supabase-postgres-13#new-extensions)
### `pgRouting`[#](https://supabase.com/blog/supabase-postgres-13#pgrouting)
An extension of PostGIS, [`pgRouting`](https://pgrouting.org/) provides geospatial routing functionality.
More information can be found [here](https://docs.pgrouting.org/latest/en/index.html).
### `wal2json`[#](https://supabase.com/blog/supabase-postgres-13#wal2json)
Converts WAL output into clean and organized JSON objects.
More information can be found [here](https://github.com/eulerto/wal2json).
## Enhanced security[#](https://supabase.com/blog/supabase-postgres-13#enhanced-security)
To help combat brute force attacks, `fail2ban` has now been configured to protect direct connections to Postgres. This applies to both ports `5432` (PostgreSQL) and `6543` (PgBouncer).
IPs get banned for 10 minutes after three failed attempts, and we'll continue to fine-tune and improve the protections applied to the database servers based on evolving traffic patterns.
## PostgreSQL bundles[#](https://supabase.com/blog/supabase-postgres-13#postgresql-bundles)
`[Coming Soon]`
Last but not the least, we're diversifying the images of Supabase Postgres available in the AWS and Digital Ocean Marketplaces.
Instead of a single option, we'll soon offer four configurations of PostgreSQL. Each bundle offers functionality for common use-cases. For example, if you're using Postgres with Serverless functions, you might want to run the PgBouncer bundle. If you want an HTTP API with your Postgres offering you might want to run the PostgREST bundle.
`Name`| `PostgreSQL`| `PgBouncer`| `PostgREST`  
---|---|---|---  
Supabase Postgres| ✅| |   
Supabase Postgres: PgBouncer Bundle| ✅| ✅|   
Supabase Postgres: PostgREST Bundle| ✅| | ✅  
Supabase Postgres: Complete Bundle| ✅| ✅| ✅  
Each offering will be available for both the `x86` and `arm` architectures.
## Try PostgreSQL 13[#](https://supabase.com/blog/supabase-postgres-13#try-postgresql-13)
Try the new features of PostgreSQL 13.3 today by creating a [new project](https://supabase.com/dashboard/) on Supabase.
## More Postgres resources[#](https://supabase.com/blog/supabase-postgres-13#more-postgres-resources)
  * [Realtime Postgres RLS on Supabase](https://supabase.com//blog/realtime-row-level-security-in-postgresql)
  * [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
  * [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
  * [Postgres Views](https://supabase.com/blog/postgresql-views)
  * [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/postgres-audit)
  * [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
  * [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-postgres-13&text=Supabase%20is%20now%20on%20Postgres%2013.3)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-postgres-13&text=Supabase%20is%20now%20on%20Postgres%2013.3)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-postgres-13&t=Supabase%20is%20now%20on%20Postgres%2013.3)
[Last postSupabase Community Day26 July 2021](https://supabase.com/blog/supabase-community-day)
[Next postSupabase Launch Week II: The SQL22 July 2021](https://supabase.com/blog/supabase-launch-week-sql)
[launch-week](https://supabase.com/blog/tags/launch-week)[database](https://supabase.com/blog/tags/database)
On this page
  * [PostgreSQL version 13.3](https://supabase.com/blog/supabase-postgres-13#postgresql-version-133)
  * [Supabase Versioning](https://supabase.com/blog/supabase-postgres-13#supabase-versioning)
  * [Large System Extensions (LSE) enabled for ARM instances](https://supabase.com/blog/supabase-postgres-13#large-system-extensions-lse-enabled-for-arm-instances)
  * [Ubuntu 20.04](https://supabase.com/blog/supabase-postgres-13#ubuntu-2004)
  * [Built from source](https://supabase.com/blog/supabase-postgres-13#built-from-source)
  * [New Extensions](https://supabase.com/blog/supabase-postgres-13#new-extensions)
  * [Enhanced security](https://supabase.com/blog/supabase-postgres-13#enhanced-security)
  * [PostgreSQL bundles](https://supabase.com/blog/supabase-postgres-13#postgresql-bundles)
  * [Try PostgreSQL 13](https://supabase.com/blog/supabase-postgres-13#try-postgresql-13)
  * [More Postgres resources](https://supabase.com/blog/supabase-postgres-13#more-postgres-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-postgres-13&text=Supabase%20is%20now%20on%20Postgres%2013.3)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-postgres-13&text=Supabase%20is%20now%20on%20Postgres%2013.3)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-postgres-13&t=Supabase%20is%20now%20on%20Postgres%2013.3)
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

