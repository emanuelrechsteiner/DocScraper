---
url: https://supabase.com/blog/pg-graphql-1-5-7
scraped_at: 2025-05-25T09:41:01.181189
title: pg_graphql 1.5.7: pagination and multi-tenancy support
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
# pg_graphql 1.5.7: pagination and multi-tenancy support
15 Aug 2024
•
4 minute read
[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Oliver RiceEngineering](https://github.com/olirice)
![pg_graphql 1.5.7: pagination and multi-tenancy support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fthumb_pg_graphql.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# What's new in pg_graphql 1.5.7[#](https://supabase.com/blog/pg-graphql-1-5-7#whats-new-in-pg_graphql-157)
Since our [last check-in on pg_graphql](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2) there have been a few quality of life improvements worth calling out. A quick roundup of the key differences includes:
  * Pagination via First/Offset
  * Schema based multi-tenancy
  * Filtering on array typed columns with `contains`, `containedBy` and `overlaps`


## First/Offset pagination[#](https://supabase.com/blog/pg-graphql-1-5-7#firstoffset-pagination)
Since the earliest days of pg_graphql, [keyset pagination](https://supabase.github.io/pg_graphql/api/#keyset-pagination) has been supported. Keyset pagination allows for paging forwards and backwards through a collection by specifying a number of records and the unique id of a record within the collection. For example:
`
1
{
2
 blogCollection(
3
  first: 2,
4
  after: "Y3Vyc29yMQ=="
5
 ) {
6
 ...
7
}
`
to retrieve the first 2 records after the record with unique id `Y3Vyc29yMQ==` .
Starting in version `1.5.0` there is support for `offset` based pagination, which is based on skipping `offset` number of records before returning the results.
`
1
{
2
 blogCollection(
3
  first: 2,
4
  offset: 5
5
 ) {
6
 ...
7
}
`
That is roughly equivalent to the SQL
`
1
select
2
  *
3
from
4
  blog
5
limit
6
  2
7
offset
8
  5
`
In general as offset values increase, the performance of the query will decrease. For that reason its important to use keyset pagination where possible.
## Performance schema based multi-tennancy[#](https://supabase.com/blog/pg-graphql-1-5-7#performance-schema-based-multi-tennancy)
pg_graphql caches the database schema on first query and rebuilds that cache any time the schema changes. The cache key is a combination of the postgres role and the database schema's version number. Initially, the structure of all schemas was loaded for all roles, and table/column visibility was filtered down within `pg_graphql`.
In multi-tenant environments with 1 schema per tenant, that meant every time a tenant updated their schema, all tenants had to rebuild the cache. When the number of tenants gets large, that burdens the database if its under heavy load.
Following version `1.5.2` each tenant's cache only loads the schemas that they have `usage` permission for, which greatly reduces the query time in multi-tenant environments and the size of the schema cache. At time of writing this solution powers a project with >2200 tenants.
## Filtering array column types[#](https://supabase.com/blog/pg-graphql-1-5-7#filtering-array-column-types)
From `1.5.6` pg_graphql has added `contains`, `containedBy`, `overlaps` filter operators for scalar array fields like `text[]` or `int[]`.
For example, given a table
`
1
create table blog (
2
 id int primary key,
3
 name text not null,
4
 tags text[] not null,
5
 created_at timestamp not null
6
);
`
the `tags` column with type `text[]` can be filtered on.
`
1
{
2
 blogCollection(filter: { tags: { contains: ["tech", "innovation"] } }) {
3
  edges {
4
   cursor
5
   node {
6
    name
7
    tags
8
    createdAt
9
   }
10
  }
11
 }
12
}
`
In this case, the result set is filtered to records where the `tags` column contains both `tech` and `innovation`.
## Roadmap[#](https://supabase.com/blog/pg-graphql-1-5-7#roadmap)
The headline features we aim to launch in coming releases of pg_graphql include support for:
  * Insert on conflict / Upsert
  * Nested inserts


If you want to get started with GraphQL today, check out the [Docs](https://supabase.com/docs/guides/graphql) or the [source code](https://github.com/supabase/pg_graphql/).
[Launch Week12](https://supabase.com/launch-week/12)
12-16 August
[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage
[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)[02 -pg_replicate](https://news.ycombinator.com/item?id=41209994)[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)[06 -vec2pg](https://supabase.com/blog/vec2pg)[07 -pg_graphql](https://supabase.com/blog/pg-graphql-1-5-7)[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)[09 -python-support](https://supabase.com/blog/python-support)[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&text=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&text=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&t=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)
[Last postIntroducing Log Drains15 August 2024](https://supabase.com/blog/log-drains)
[Next postSnaplet is now open source14 August 2024](https://supabase.com/blog/snaplet-is-now-open-source)
[launch-week](https://supabase.com/blog/tags/launch-week)[graphql](https://supabase.com/blog/tags/graphql)
On this page
  * [What's new in pg_graphql 1.5.7](https://supabase.com/blog/pg-graphql-1-5-7#whats-new-in-pg_graphql-157)
    * [First/Offset pagination](https://supabase.com/blog/pg-graphql-1-5-7#firstoffset-pagination)
    * [Performance schema based multi-tennancy](https://supabase.com/blog/pg-graphql-1-5-7#performance-schema-based-multi-tennancy)
    * [Filtering array column types](https://supabase.com/blog/pg-graphql-1-5-7#filtering-array-column-types)
    * [Roadmap](https://supabase.com/blog/pg-graphql-1-5-7#roadmap)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&text=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&text=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&t=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)
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

