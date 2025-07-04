---
url: https://supabase.com/docs/guides/database/extensions/pgrouting
scraped_at: 2025-05-25T09:02:17.482330
title: pgrouting: Geospatial Routing | Supabase Docs
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
[Database](https://supabase.com/docs/guides/database/overview)
  * [Overview](https://supabase.com/docs/guides/database/overview)
Fundamentals
  * [Connecting to your database](https://supabase.com/docs/guides/database/connecting-to-postgres)
  * [Importing data](https://supabase.com/docs/guides/database/import-data)
  * [Securing your data](https://supabase.com/docs/guides/database/secure-data)
Working with your database (basics)
  * [Managing tables, views, and data](https://supabase.com/docs/guides/database/tables)
  * [Working with arrays](https://supabase.com/docs/guides/database/arrays)
  * [Managing indexes](https://supabase.com/docs/guides/database/postgres/indexes)
  * [Querying joins and nested tables](https://supabase.com/docs/guides/database/joins-and-nesting)
  * [JSON and unstructured data](https://supabase.com/docs/guides/database/json)
Working with your database (intermediate)
  * [Implementing cascade deletes](https://supabase.com/docs/guides/database/postgres/cascade-deletes)
  * [Managing enums](https://supabase.com/docs/guides/database/postgres/enums)
  * [Managing database functions](https://supabase.com/docs/guides/database/functions)
  * [Managing database triggers](https://supabase.com/docs/guides/database/postgres/triggers)
  * [Managing database webhooks](https://supabase.com/docs/guides/database/webhooks)
  * [Using Full Text Search](https://supabase.com/docs/guides/database/full-text-search)
  * [Partitioning your tables](https://supabase.com/docs/guides/database/partitions)
  * [Managing connections](https://supabase.com/docs/guides/database/connection-management)
OrioleDB
  * [Overview](https://supabase.com/docs/guides/database/orioledb)
Access and security
  * [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
  * [Column Level Security](https://supabase.com/docs/guides/database/postgres/column-level-security)
  * [Hardening the Data API](https://supabase.com/docs/guides/database/hardening-data-api)
  * [Custom Claims & RBAC](https://supabase.com/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac)
  * [Managing Postgres Roles](https://supabase.com/docs/guides/database/postgres/roles)
  * [Using Custom Postgres Roles](https://supabase.com/docs/guides/storage/schema/custom-roles)
  * [Managing secrets with Vault](https://supabase.com/docs/guides/database/vault)
  * [Superuser Access and Unsupported Operations](https://supabase.com/docs/guides/database/postgres/roles-superuser)
Configuration, optimization, and testing
  * [Database configuration](https://supabase.com/docs/guides/database/postgres/configuration)
  * [Managing database replication](https://supabase.com/docs/guides/database/replication)
  * [Query optimization](https://supabase.com/docs/guides/database/query-optimization)
  * [Database Advisors](https://supabase.com/docs/guides/database/database-advisors)
  * [Testing your database](https://supabase.com/docs/guides/database/testing)
  * [Customizing Postgres config](https://supabase.com/docs/guides/database/custom-postgres-config)
Debugging
  * [Timeouts](https://supabase.com/docs/guides/database/postgres/timeouts)
  * [Debugging and monitoring](https://supabase.com/docs/guides/database/inspect)
  * [Debugging performance issues](https://supabase.com/docs/guides/database/debugging-performance)
  * [Supavisor](https://supabase.com/docs/guides/database/supavisor)
ORM Quickstarts
  * [Prisma](https://supabase.com/docs/guides/database/prisma)
  * [Drizzle](https://supabase.com/docs/guides/database/drizzle)
  * [Postgres.js](https://supabase.com/docs/guides/database/postgres-js)
GUI quickstarts
  * [pgAdmin](https://supabase.com/docs/guides/database/pgadmin)
  * [PSQL](https://supabase.com/docs/guides/database/psql)
  * [DBeaver](https://supabase.com/docs/guides/database/dbeaver)
  * [Metabase](https://supabase.com/docs/guides/database/metabase)
  * [Beekeeper Studio](https://supabase.com/docs/guides/database/beekeeper-studio)
Extensions
  * [Overview](https://supabase.com/docs/guides/database/extensions)
  * [HypoPG: Hypothetical indexes](https://supabase.com/docs/guides/database/extensions/hypopg)
  * [plv8: Javascript Language](https://supabase.com/docs/guides/database/extensions/plv8)
  * [http: RESTful Client](https://supabase.com/docs/guides/database/extensions/http)
  * [index_advisor: Query optimization](https://supabase.com/docs/guides/database/extensions/index_advisor)
  * [PGAudit: Postgres Auditing](https://supabase.com/docs/guides/database/extensions/pgaudit)
  * [pgjwt: JSON Web Tokens](https://supabase.com/docs/guides/database/extensions/pgjwt)
  * [PGroonga: Multilingual Full Text Search](https://supabase.com/docs/guides/database/extensions/pgroonga)
  * [pgRouting: Geospatial Routing](https://supabase.com/docs/guides/database/extensions/pgrouting)
  * [pg_cron: Schedule Recurring Jobs](https://supabase.com/docs/guides/database/extensions/pg_cron)
  * [pg_graphql: GraphQL Support](https://supabase.com/docs/guides/database/extensions/pg_graphql)
  * [pg_hashids: Short UIDs](https://supabase.com/docs/guides/database/extensions/pg_hashids)
  * [pg_jsonschema: JSON Schema Validation](https://supabase.com/docs/guides/database/extensions/pg_jsonschema)
  * [pg_net: Async Networking](https://supabase.com/docs/guides/database/extensions/pg_net)
  * [pg_plan_filter: Restrict Total Cost](https://supabase.com/docs/guides/database/extensions/pg_plan_filter)
  * [postgres_fdw: query data from an external Postgres server](https://supabase.com/docs/guides/database/extensions/postgres_fdw)
  * [pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)
  * [pg_stat_statements: SQL Planning and Execution Statistics](https://supabase.com/docs/guides/database/extensions/pg_stat_statements)
  * [pg_repack: Storage Optimization](https://supabase.com/docs/guides/database/extensions/pg_repack)
  * [PostGIS: Geo queries](https://supabase.com/docs/guides/database/extensions/postgis)
  * [pgmq: Queues](https://supabase.com/docs/guides/database/extensions/pgmq)
  * [pgsodium (pending deprecation): Encryption Features](https://supabase.com/docs/guides/database/extensions/pgsodium)
  * [pgTAP: Unit Testing](https://supabase.com/docs/guides/database/extensions/pgtap)
  * [plpgsql_check: PL/pgSQL Linter](https://supabase.com/docs/guides/database/extensions/plpgsql_check)
  * [timescaledb: Time-series data](https://supabase.com/docs/guides/database/extensions/timescaledb)
  * [uuid-ossp: Unique Identifiers](https://supabase.com/docs/guides/database/extensions/uuid-ossp)
  * [RUM: inverted index for full-text search](https://supabase.com/docs/guides/database/extensions/rum)
Foreign Data Wrappers
  * [Overview](https://supabase.com/docs/guides/database/extensions/wrappers/overview)
  * [Connecting to Auth0](https://supabase.com/docs/guides/database/extensions/wrappers/auth0)
  * [Connecting to Airtable](https://supabase.com/docs/guides/database/extensions/wrappers/airtable)
  * [Connecting to AWS Cognito](https://supabase.com/docs/guides/database/extensions/wrappers/cognito)
  * [Connecting to AWS S3](https://supabase.com/docs/guides/database/extensions/wrappers/s3)
  * [Connecting to BigQuery](https://supabase.com/docs/guides/database/extensions/wrappers/bigquery)
  * [Connecting to Clerk](https://supabase.com/docs/guides/database/extensions/wrappers/clerk)
  * [Connecting to ClickHouse](https://supabase.com/docs/guides/database/extensions/wrappers/clickhouse)
  * [Connecting to Firebase](https://supabase.com/docs/guides/database/extensions/wrappers/firebase)
  * [Connecting to Logflare](https://supabase.com/docs/guides/database/extensions/wrappers/logflare)
  * [Connecting to MSSQL](https://supabase.com/docs/guides/database/extensions/wrappers/mssql)
  * [Connecting to Notion](https://supabase.com/docs/guides/database/extensions/wrappers/notion)
  * [Connecting to Paddle](https://supabase.com/docs/guides/database/extensions/wrappers/paddle)
  * [Connecting to Redis](https://supabase.com/docs/guides/database/extensions/wrappers/redis)
  * [Connecting to Snowflake](https://supabase.com/docs/guides/database/extensions/wrappers/snowflake)
  * [Connecting to Stripe](https://supabase.com/docs/guides/database/extensions/wrappers/stripe)
Examples
  * [Drop All Tables in Schema](https://supabase.com/docs/guides/database/postgres/dropping-all-tables-in-schema)
  * [Select First Row per Group](https://supabase.com/docs/guides/database/postgres/first-row-in-group)
  * [Print PostgreSQL Version](https://supabase.com/docs/guides/database/postgres/which-version-of-postgres)
  * [Replicating from Supabase to External Postgres](https://supabase.com/docs/guides/database/postgres/setup-replication-external)


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
Database
  1. [Database](https://supabase.com/docs/guides/database/overview)
  2. Extensions
  3. [pgRouting: Geospatial Routing](https://supabase.com/docs/guides/database/extensions/pgrouting)


pgrouting: Geospatial Routing
[`pgRouting`](http://pgrouting.org) is Postgres and [PostGIS](http://postgis.net) extension adding geospatial routing functionality.
The core functionality of `pgRouting` is a set of path finding algorithms including:
  * All Pairs Shortest Path, Johnson’s Algorithm
  * All Pairs Shortest Path, Floyd-Warshall Algorithm
  * Shortest Path A*
  * Bi-directional Dijkstra Shortest Path
  * Bi-directional A* Shortest Path
  * Shortest Path Dijkstra
  * Driving Distance
  * K-Shortest Path, Multiple Alternative Paths
  * K-Dijkstra, One to Many Shortest Path
  * Traveling Sales Person
  * Turn Restriction Shortest Path (TRSP)


## Enable the extension[#](https://supabase.com/docs/guides/database/extensions/pgrouting#enable-the-extension)
DashboardSQL
  1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard.
  2. Click on **Extensions** in the sidebar.
  3. Search for `pgrouting` and enable the extension.


## Example[#](https://supabase.com/docs/guides/database/extensions/pgrouting#example)
As an example, we'll solve the [traveling salesperson problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) using the `pgRouting`'s `pgr_TSPeuclidean` function from some PostGIS coordinates.
A summary of the traveling salesperson problem is, given a set of city coordinates, solve for a path that goes through each city and minimizes the total distance traveled.
First we populate a table with some X, Y coordinates
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
createtablewi29 ( id bigint, x float, y float, geom geometry);insert into wi29 (id, x, y)values (1,20833.3333,17100.0000), (2,20900.0000,17066.6667), (3,21300.0000,13016.6667), (4,21600.0000,14150.0000), (5,21600.0000,14966.6667), (6,21600.0000,16500.0000), (7,22183.3333,13133.3333), (8,22583.3333,14300.0000), (9,22683.3333,12716.6667), (10,23616.6667,15866.6667), (11,23700.0000,15933.3333), (12,23883.3333,14533.3333), (13,24166.6667,13250.0000), (14,25149.1667,12365.8333), (15,26133.3333,14500.0000), (16,26150.0000,10550.0000), (17,26283.3333,12766.6667), (18,26433.3333,13433.3333), (19,26550.0000,13850.0000), (20,26733.3333,11683.3333), (21,27026.1111,13051.9444), (22,27096.1111,13415.8333), (23,27153.6111,13203.3333), (24,27166.6667,9833.3333), (25,27233.3333,10450.0000), (26,27233.3333,11783.3333), (27,27266.6667,10383.3333), (28,27433.3333,12400.0000), (29,27462.5000,12992.2222);

```

Next we use the `pgr_TSPeuclidean` function to find the best path.
```

1
2
3
4
select*from   pgr_TSPeuclidean($$select*from wi29$$)

```

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
seq | node |    cost    |   agg_cost   -----+------+------------------+------------------1 |  1 |        0 |        02 |  2 | 74.535614157127 | 74.5356141571273 |  6 | 900.617093380362 | 975.1527075374894 |  10 | 2113.77757765045 | 3088.930285187935 |  11 | 106.718669615254 | 3195.648954803196 |  12 | 1411.95293791574 | 4607.601892718937 |  13 | 1314.23824873744 | 5921.840141456378 |  14 | 1321.76283931305 | 7243.602980769429 |  17 | 1202.91366735569 | 8446.516648125110 |  18 | 683.333268292684 | 9129.8499164177911 |  15 | 1108.05137466134 | 10237.901291079112 |  19 | 772.082339448903 | 11009.98363052813 |  22 | 697.666150054665 | 11707.649780582714 |  23 | 220.141999627513 | 11927.791780210215 |  21 | 197.926372783442 | 12125.718152993716 |  29 | 440.456596290771 | 12566.174749284417 |  28 | 592.939989005405 | 13159.114738289818 |  26 | 648.288376333318 | 13807.403114623119 |  20 | 509.901951359278 | 14317.305065982420 |  25 | 1330.83095428717 | 15648.136020269621 |  27 | 74.535658878487 | 15722.671679148122 |  24 | 559.016994374947 | 16281.68867352323 |  16 | 1243.87392358622 | 17525.562597109224 |  9 | 4088.0585364911 | 21613.621133600425 |  7 | 650.85409697993 | 22264.475230580326 |  3 | 891.004385199336 | 23155.479615779627 |  4 | 1172.36699411442 | 24327.84660989428 |  8 | 994.708187806297 | 25322.554797700329 |  5 | 1188.01888359478 | 26510.573681295130 |  1 | 2266.91173136004 | 28777.4854126552

```

## Resources[#](https://supabase.com/docs/guides/database/extensions/pgrouting#resources)
  * Official [`pgRouting` documentation](https://docs.pgrouting.org/latest/en/index.html)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/database/extensions/pgrouting.mdx)
### Is this helpful?
No Yes
### On this page
[Enable the extension](https://supabase.com/docs/guides/database/extensions/pgrouting#enable-the-extension)[Example](https://supabase.com/docs/guides/database/extensions/pgrouting#example)[Resources](https://supabase.com/docs/guides/database/extensions/pgrouting#resources)
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



