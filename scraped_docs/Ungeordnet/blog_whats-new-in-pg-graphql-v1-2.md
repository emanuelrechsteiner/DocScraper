---
url: https://supabase.com/blog/whats-new-in-pg-graphql-v1-2
scraped_at: 2025-05-25T08:54:16.474239
title: What's New in pg_graphql v1.2
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
# What's New in pg_graphql v1.2
21 Apr 2023
•
6 minute read
[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Oliver RiceEngineering](https://github.com/olirice)
![What's New in pg_graphql v1.2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fpggraphql%2Fog-pg-graphql.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
It's been 4 months since the [1.0.0 release of pg_graphql](https://supabase.com/blog/pg-graphql-v1). Since then, we’ve pushed several features to improve the APIs that `pg_graphql` produces.
In this article, we’ll walk through those features and show examples of each.
📢 These features are only available on projects with Postgres version `15.1.0.63` or higher. For help with upgrading, please review the [migrating and upgrading projects guide](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects).
### View Support[#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#view-support)
Prior to `v1.1`, `pg_graphql` would only reflect standard tables. Since then, views, materialized views, and foreign tables are now also reflected in the GraphQL schema.
For example:
`
1
create view "ProjectOwner" as
2
 select
3
  acc.id,
4
  acc.name
5
 from
6
  account as acc
7
  join role as r on r.id = acc.role_id
8
 where acc.role = 'project_owner';
`
Since all entities exposed by `pg_graphql` require primary keys, we must define that constraint for the view. We do that using a comment directive:
`
1
comment on view "ProjectOwner"
2
 is '@graphql({"primary_key_columns": ["id"]})';
`
Which yields the GraphQL type:
`
1
type ProjectOwner implements Node {
2
 nodeId: ID!
3
 id: UUID!
4
 name: String
5
}
`
With associated `Edge` and `Connection` types. That enables querying via:
`
1
{
2
 projectOwnerCollection(first: 2) {
3
  edges {
4
   node {
5
    nodeId
6
    name
7
   }
8
  }
9
 }
10
}
`
Additionally, simple views automatically support mutation events like inserts and updates. You might use these to migrate underlying tables while maintaining backwards compatibility with previous API versions.
## Filtering[#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#filtering)
Filtering in SQL is endlessly flexible. We’ve taken two incremental steps to bring more of that flexibility to the GraphQL interface.
### `is null` and `is not null`[#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#is-null-and-is-not-null)
Handling `null` values can be tricky in both SQL and GraphQL. However, there are similarities we can take advantage of. In `pg_graphql`, every scalar data type has its own filter type, such as `IntFilter` and `StringFilter`. Each of these filter types now includes an `is` argument, which allows you to filter based on whether a value is null or not null. You can do this by using `{is: NULL}` for `null` values and `{is: NOT_NULL}` for non-`null` values.
`
1
enum FilterIs {
2
  NULL
3
  NOT_NULL
4
}
56
type IntFilter {
7
  ...
8
  is: FilterIs
9
}
`
For example:
`
1
{
2
 blogCollection(filter: { name: {is: NULL}}) {
3
  ...
4
 }
5
}
`
to return all `blog`s where the `name` is `null`.
### **`like`**,**`ilike`**, and**`startsWith`**[#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#like-ilike-and-startswith)
Text filtering options in `pg_graphql` have historically been restricted to equality checks. The hesitation was due to concerns about exposing a default filter that is difficult to index. The combination of [citext](https://www.postgresql.org/docs/current/citext.html) and [PGroonga available on the platform](https://supabase.com/docs/guides/database/extensions/pgroonga) solves those scalability risks and enabled us to expand the `StringFilter` with options for `like` `ilike` and `startsWith`.
`
1
input StringFilter {
2
 eq: String
3
 ...
4
 startsWith: String
5
 like: String
6
 ilike: String
7
}
`
Note that `startsWith` filters should be preferred where appropriate because they can leverage simple B-Tree indexes to improve performance.
`
1
{
2
 generalLedgerCollection(filter: { identifierCode: { startsWith: "BX1:" } }) {
3
  edges {
4
   node {
5
    nodeId
6
    identifierCode
7
    amount
8
   }
9
  }
10
 }
11
}
`
### GraphQL directives `@skip` and `@include`[#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#graphql-directives-skip-and-include)
The GraphQL spec has evolved over time. Although the spec is clear, it is common for GraphQL servers to selectively omit some chunks of functionality. For example, some frameworks intentionally do not expose an introspection schema as a form of security through obscurity.
`pg_graphql` aims to be unopinionated and adhere exactly to the spec. The `@skip` and `@include` directives are part of the [GraphQL core specification](https://spec.graphql.org/October2021/#sec--skip) and are now functional.
The **`@skip`**directive in GraphQL is used to conditionally skip a field or fragment during query execution based on a Boolean variable. It can be used to make the query more efficient by reducing the amount of data retrieved from the server.
The **`@include`**directive is the mirror of**`@skip`**where a field or fragment is conditionally included depending on the value of a Boolean variable.
Here's an example of how the **`@skip`**directive can be used in a GraphQL query:
`
1
query getBooks($includeDetails: Boolean!) {
2
 booksCollection {
3
  edges {
4
   node {
5
    id
6
    title
7
    description @skip(if: $includeDetails)
8
   }
9
  }
10
 }
11
}
`
### User Defined Descriptions[#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#user-defined-descriptions)
Users can now use the [comment directive system to assign descriptions](https://supabase.github.io/pg_graphql/configuration/#description) to tables, views and columns.
`
1
create table public.book(
2
  id int primary key,
3
  title text not null
4
);
56
comment on table public.book
7
is e'@graphql({"description": "a library book"})';
89
comment on column public.book.title
10
is e'@graphql({"description": "the title of the book"})';
`
GraphQL IDEs, such as GraphiQL render those descriptions, allowing developers to provide clearer API documentation.
![description comment directive](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-04-19-pg_graphql-v1_2%2Fdescription_directive.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Roadmap[#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#roadmap)
The headline features we aim to launch in coming releases of `pg_graphql` include:
  1. Support for user-defined functions: [GitHub issue](https://github.com/supabase/pg_graphql/issues/222)
  2. Support for nested inserts: [GitHub issue](https://github.com/supabase/pg_graphql/issues/294)
  3. An alternative approach to computed relationships based on SQL functions returning **`SET OF`**rather than comment directives (compatible with PostgREST)


## More pg_graphql[#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#more-pg_graphql)
  * [Introducing pg_graphql: A GraphQL extension for PostgreSQL](https://supabase.com/blog/pg-graphql)
  * [GraphQL is now available in Supabase](https://supabase.com/blog/graphql-now-available)
  * [pg_graphql v1.0](https://supabase.com/blog/pg-graphql-v1)
  * [pg_graphql: Postgres functions now supported](https://supabase.com/blog/pg-graphql-postgres-functions)


### More Launch Week 7
[Designing with AI![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fai-images%2F00-ai-images-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/designing-with-ai-midjourney)
[Supavisor![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fsupavisor%2Fsupavisor-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://github.com/supabase/supavisor)
[Open Source Logging![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday1%2Fself-hosted-logs-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-logs-self-hosted)
[Self-hosted Deno Edge Functions![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday2%2Fself-hosted-edge-functions-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)
[Storage v3: Resumable Uploads with support for 50GB files![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday3%2Fstorage-v3-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/storage-v3-resumable-uploads)
[Supabase Auth: SSO, Mobile, and Server-side support![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday4%2Fsso-support-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-auth-sso-pkce)
[Community Highlight![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fcommunity%2Fcommunity-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/launch-week-7-community-highlights)
[Studio Updates![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fstudio%2Fstudio-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-studio-2.0)
[dbdev![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2Fdbdev-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/dbdev)
[Postgres TLE![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2FpgTLE-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/pg-tle)
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&text=What's%20New%20in%20pg_graphql%20v1.2)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&text=What's%20New%20in%20pg_graphql%20v1.2)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&t=What's%20New%20in%20pg_graphql%20v1.2)
[Last postLaunch Week 7 Hackathon Winners24 April 2023](https://supabase.com/blog/launch-week-7-hackathon-winners)
[Next postdbdev: PostgreSQL Package Manager14 April 2023](https://supabase.com/blog/dbdev)
[postgres](https://supabase.com/blog/tags/postgres)[graphql](https://supabase.com/blog/tags/graphql)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [View Support](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#view-support)


  * [Filtering](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#filtering)
    * [`is null` and `is not null`](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#is-null-and-is-not-null)
    * [**`like`**,**`ilike`**, and**`startsWith`**](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#like-ilike-and-startswith)
    * [GraphQL directives `@skip` and `@include`](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#graphql-directives-skip-and-include)
    * [User Defined Descriptions](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#user-defined-descriptions)
  * [Roadmap](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#roadmap)
  * [More pg_graphql](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#more-pg_graphql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&text=What's%20New%20in%20pg_graphql%20v1.2)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&text=What's%20New%20in%20pg_graphql%20v1.2)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&t=What's%20New%20in%20pg_graphql%20v1.2)
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

