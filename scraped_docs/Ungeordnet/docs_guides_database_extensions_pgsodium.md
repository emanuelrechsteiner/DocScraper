---
url: https://supabase.com/docs/guides/database/extensions/pgsodium
scraped_at: 2025-05-25T09:02:24.189189
title: pgsodium (pending deprecation): Encryption Features | Supabase Docs
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
  3. [pgsodium (pending deprecation): Encryption Features](https://supabase.com/docs/guides/database/extensions/pgsodium)


pgsodium (pending deprecation): Encryption Features
Supabase DOES NOT RECOMMEND any new usage of [`pgsodium`](https://github.com/michelp/pgsodium).
The [`pgsodium`](https://github.com/michelp/pgsodium) extension is expected to go through a deprecation cycle in the near future. We will reach out to owners of impacted projects to assist with migrations away from [`pgsodium`](https://github.com/michelp/pgsodium) once the deprecation process begins.
The [Vault extension](https://supabase.com/docs/guides/database/vault) won’t be impacted. Its internal implementation will shift away from pgsodium, but the interface and API will remain unchanged.
[`pgsodium`](https://github.com/michelp/pgsodium) is a Postgres extension which provides SQL access to [`libsodium`'s](https://doc.libsodium.org/) high-level cryptographic algorithms.
Supabase previously documented two features derived from pgsodium. Namely [Server Key Management](https://github.com/michelp/pgsodium#server-key-management) and [Transparent Column Encryption](https://github.com/michelp/pgsodium#transparent-column-encryption). At this time, we do not recommend using either on the Supabase platform due to their high level of operational complexity and misconfiguration risk.
Note that Supabase projects are encrypted at rest by default which likely is sufficient for your compliance needs e.g. SOC2 & HIPAA.
## Get the root encryption key for your Supabase project[#](https://supabase.com/docs/guides/database/extensions/pgsodium#get-the-root-encryption-key-for-your-supabase-project)
Encryption requires keys. Keeping the keys in the same database as the encrypted data would be unsafe. For more information about managing the `pgsodium` root encryption key on your Supabase project see **[encryption key location](https://supabase.com/docs/guides/database/vault#encryption-key-location)**. This key is required to decrypt values stored in [Supabase Vault](https://supabase.com/docs/guides/database/vault) and data encrypted with Transparent Column Encryption.
## Resources[#](https://supabase.com/docs/guides/database/extensions/pgsodium#resources)
  * [Supabase Vault](https://supabase.com/docs/guides/database/vault)
  * Read more about Supabase Vault in the [blog post](https://supabase.com/blog/vault-now-in-beta)
  * [Supabase Vault on GitHub](https://github.com/supabase/vault)


## Resources[#](https://supabase.com/docs/guides/database/extensions/pgsodium#resources)
  * Official [`pgsodium` documentation](https://github.com/michelp/pgsodium)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/database/extensions/pgsodium.mdx)
### Is this helpful?
No Yes
### On this page
[Get the root encryption key for your Supabase project](https://supabase.com/docs/guides/database/extensions/pgsodium#get-the-root-encryption-key-for-your-supabase-project)[Resources](https://supabase.com/docs/guides/database/extensions/pgsodium#resources)[Resources](https://supabase.com/docs/guides/database/extensions/pgsodium#resources)
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



