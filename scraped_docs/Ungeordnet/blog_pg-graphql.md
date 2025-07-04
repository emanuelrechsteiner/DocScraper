---
url: https://supabase.com/blog/pg-graphql
scraped_at: 2025-05-25T09:04:18.134319
title: pg_graphql: A GraphQL extension for PostgreSQL
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
# pg_graphql: A GraphQL extension for PostgreSQL
03 Dec 2021
•
7 minute read
[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Oliver RiceEngineering](https://github.com/olirice)
![pg_graphql: A GraphQL extension for PostgreSQL](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Ffive-more-things%2Fsupabase-pg-graphql-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
🆕 `pg_graphql` is now generally available and has undergone significant enhancements since this announcement. Here is what is new:
  * [pg_graphql v1.0](https://supabase.com/blog/pg-graphql-v1)
  * [New Features in pg_graphql v1.2](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)


Today we're open sourcing [`pg_graphql`](https://github.com/supabase/pg_graphql), a native PostgreSQL extension adding GraphQL support. The extension keeps schema generation, query parsing, and resolvers all neatly contained on your database server requiring no external services.
`pg_graphql` inspects an existing PostgreSQL schema and reflects a GraphQL schema with resolvers that are:
  * performant
  * always up-to-date
  * compliant with best practices
  * serverless
  * open source


Interested? You're [3 commands away](https://supabase.github.io/pg_graphql/quickstart/) from a live [GraphiQL](https://graphql-dotnet.github.io/docs/getting-started/graphiql/) demo.
## Motivation[#](https://supabase.com/blog/pg-graphql#motivation)
The Supabase stack is centered around PostgreSQL as the single source of truth. All data, configuration, and security are housed in the database so any GraphQL solution needed to be equivalently SQL-centric.
With that in mind, we took a look at the landscape and considered two excellent technologies, [Graphile](https://www.graphile.org/postgraphile/), and [Hasura](https://hasura.io/).
Requirements| Graphile| Hasura  
---|---|---  
Open Source| ✅| ✅  
Reflected GraphQL Schema| ✅| ✅  
Reflected Resolvers| ✅| ✅  
Always up-to-date| ✅| ✅  
Performant| ✅| ✅  
We found both options to be largely viable for the core feature set.
Which left us with one final hang-up: we host free-tier projects on VMs with 1 GB of memory. After tallying the resources reserved for PostgreSQL, PostgREST, Kong, GoTrue, and a handful of smaller services, we were left with a total memory budget of ... 0 MB 😬. Unsurprisingly, our pathological memory target disqualified any option that required launching another process in those VMs.
For that reason, we decided to invest in a lightweight alternative that runs in the database, and can be exposed over HTTP using the existing [PostgREST](https://supabase.com/docs/guides/database/api) deployments' [RPC functionality.](https://postgrest.org/en/v8.0/api.html#stored-procedures)
By our most conservative estimate, that reduces the platform's memory requirements by 525 TB/hours every month, saving 💰 and 🌳.
## Design[#](https://supabase.com/blog/pg-graphql#design)
As a native PostgreSQL extension, `pg_graphl` is written in a combination of C and SQL. Each GraphQL query is parsed, validated, and transpiled to SQL, all within the database.
Each GraphQL request is resolved by a single SQL statement. That SQL statement aggregates requested data as a JSON document to return to the caller. This approach results in blazing fast response times, avoids the [N+1 query problem](https://medium.com/the-marcy-lab-school/what-is-the-n-1-problem-in-graphql-dd4921cb3c1a), and hits the theoretical minimum achievable network IO overhead of any GraphQL to SQL resolver. No special permissions are required for the PostgreSQL role executing queries, so `pg_graphql` is fully compatible with your existing [row level security policies](https://supabase.com/docs/guides/auth/row-level-security).
Embedding the GraphQL server directly in the database allows us to leverage PostgreSQL's built-in solutions for common challenges:
Caching → `PREPARE STATEMENT`
Errors → `RAISE EXCEPTION`
Bad Data → `ROLLBACK`
Authorization → `CREATE POLICY`
Similarly, `pg_graphql` benefits from PostgreSQL's strong [ACID](https://database.guide/what-is-acid-in-databases/) guarantees and can expose them through its API.
Ever wanted to execute multiple operations in a single transaction? Each request is managed in a single transaction so with a multi-operation GraphQL request and `pg_graphql`, that behavior falls out for free!
### Schema Reflection[#](https://supabase.com/blog/pg-graphql#schema-reflection)
As a limited example of how the reflection engine works, here's how it converts a single table into a full GraphQL schema.
hideCopy
`
1
# schema.sql
2
create table account (
3
 id serial primary key,
4
 email varchar(255) not null,
5
 created_at timestamp not null,
6
 updated_at timestamp not null
7
);
`
Translates into
hideCopy
`
1
# schema.graphql
2
scalar Cursor
3
scalar DateTime
4
scalar JSON
5
scalar UUID
6
scalar BigInt
78
type PageInfo {
9
 hasNextPage: Boolean!
10
 hasPreviousPage: Boolean!
11
 startCursor: String!
12
 endCursor: String!
13
}
1415
type Query {
16
 account(nodeId: ID!): Account
17
 allAccounts(after: Cursor, before: Cursor, first: Int, last: Int): AccountConnection
18
}
1920
type Account {
21
 nodeId: ID!
22
 id: String!
23
 email: String!
24
 createdAt: DateTime!
25
 updatedAt: DateTime!
26
}
2728
type AccountEdge {
29
 cursor: String!
30
 node: Account
31
}
3233
type AccountConnection {
34
 totalCount: Int!
35
 pageInfo: PageInfo!
36
 edges: [AccountEdge]
37
}
`
Where `Query` type's `account` field selects a single account by its globally unique `ID` and `allAccounts` enables pagination via the [relay connections specification](https://relay.dev/graphql/connections.htm). Under the SQL hood, iterating through pages is handled using keyset pagination giving consistent retrieval times on every page.
For a more complete examples with relationships, enums, and more exotic types check out the [API doc](https://supabase.github.io/pg_graphql/api).
### API[#](https://supabase.com/blog/pg-graphql#api)
`pg_graphql`'s public API is a single SQL function that returns JSON.
hideCopy
`
1
gql.resolve(
2
  stmt text, -- the graphql query/mutation
3
  variables jsonb default '{}'::jsonb, -- key value pairs
4
)
5
  returns jsonb
`
For example, a GraphQL query selecting the `id` field for a collection of type `Book` would look like this:
hideCopy
`
1
gqldb= select gql.resolve($$
23
query {
4
 allBooks {
5
  edges {
6
   node {
7
    id
8
   }
9
  }
10
 }
11
}
1213
$$);
1415
       resolve
16
----------------------------------------------------------------------
17
{"data": {"allBooks": {"edges": [{"node": {"id": 1}}]}}, "errors": []}
`
We're opting to expose the function over HTTP through PostgREST but you could also connect to the PostgreSQL database and call the function directly from your server code in any programming language.
## Performance[#](https://supabase.com/blog/pg-graphql#performance)
When it comes to APIs, performance counts. Here are some figures from [Apache Bench](https://www.tutorialspoint.com/apache_bench/apache_bench_quick_guide.htm) showing 2,205 requests/second on a 4 core machine with 16 GB of memory.
hideCopy
`
1
Concurrency Level:   8
2
Time taken for tests:  3.628 seconds
3
Complete requests:   8000
4
Failed requests:    0
5
Total transferred:   1768000 bytes
6
Total body sent:    1928000
7
HTML transferred:    368000 bytes
8
Requests per second:  2205.21 [#/sec] (mean)
9
Time per request:    3.628 [ms] (mean)
10
Time per request:    0.453 [ms] (mean, across all concurrent requests)
11
Transfer rate:     475.93 [Kbytes/sec] received
`
Full steps to reproduce this output are available in [the docs](https://supabase.github.io/pg_graphql).
## Open Source[#](https://supabase.com/blog/pg-graphql#open-source)
`pg_graphql` is [open source software](https://github.com/supabase/pg_graphql/). As always, Issues and PRs are welcome.
[Try `pg_graphql`](https://supabase.github.io/pg_graphql/quickstart/) today to see a live [GraphiQL](https://graphql-dotnet.github.io/docs/getting-started/graphiql/) demo.
## More pg_graphql[#](https://supabase.com/blog/pg-graphql#more-pg_graphql)
  * [pg_graphql v1.0](https://supabase.com/blog/pg-graphql-v1)
  * [New Features in pg_graphql v1.2](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)
  * [pg_graphql: Postgres functions now supported](https://supabase.com/blog/pg-graphql-postgres-functions)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&text=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&text=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&t=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)
[Last postFive more things3 December 2021](https://supabase.com/blog/launch-week-three-friday-five-more-things)
[Next postKicking off the Holiday Hackdays3 December 2021](https://supabase.com/blog/supabase-holiday-hackdays-hackathon)
[launch-week](https://supabase.com/blog/tags/launch-week)[community](https://supabase.com/blog/tags/community)[graphql](https://supabase.com/blog/tags/graphql)
On this page
  * [Motivation](https://supabase.com/blog/pg-graphql#motivation)
  * [Design](https://supabase.com/blog/pg-graphql#design)
    * [Schema Reflection](https://supabase.com/blog/pg-graphql#schema-reflection)
    * [API](https://supabase.com/blog/pg-graphql#api)
  * [Performance](https://supabase.com/blog/pg-graphql#performance)
  * [Open Source](https://supabase.com/blog/pg-graphql#open-source)
  * [More pg_graphql](https://supabase.com/blog/pg-graphql#more-pg_graphql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&text=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&text=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&t=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)
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

