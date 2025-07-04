---
url: https://supabase.com/docs/guides/database/extensions/wrappers/cognito
scraped_at: 2025-05-25T09:32:27.791325
title: AWS Cognito | Supabase Docs
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
  2. Foreign Data Wrappers
  3. [Connecting to AWS Cognito](https://supabase.com/docs/guides/database/extensions/wrappers/cognito)


AWS Cognito
[AWS Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) is an identity platform for web and mobile apps.
The Cognito wrapper allows you to read data from your Cognito Userpool within your Postgres database.
## Preparation[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#preparation)
Before you can query AWS Cognito, you need to enable the Wrappers extension and store your credentials in Postgres.
### Enable Wrappers[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#enable-wrappers)
Make sure the `wrappers` extension is installed on your database:
```

1
create extension ifnotexists wrappers withschema extensions;

```

### Enable the Cognito Wrapper[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#enable-the-cognito-wrapper)
Enable the `cognito_wrapper` FDW:
```

1
2
3
create foreign data wrapper cognito_wrapper handler cognito_fdw_handler validator cognito_fdw_validator;

```

### Store your credentials (optional)[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#store-your-credentials-optional)
By default, Postgres stores FDW credentials inside `pg_catalog.pg_foreign_server` in plain text. Anyone with access to this table will be able to view these credentials. Wrappers are designed to work with [Vault](https://supabase.com/docs/guides/database/vault), which provides an additional level of security for storing credentials. We recommend using Vault to store your credentials.
```

1
2
3
4
5
6
-- Save your Cognito secret access key in Vault and retrieve the created `key_id`selectvault.create_secret('<secret access key>','cognito','Cognito secret key for Wrappers');

```

### Connecting to Cognito[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#connecting-to-cognito)
We need to provide Postgres with the credentials to connect to Cognito, and any additional options. We can do this using the `create server` command:
With VaultWithout Vault
```

1
2
3
4
5
6
7
8
createserver cognito_server foreign data wrapper cognito_wrapper options (  aws_access_key_id '<your_access_key>',  api_key_id '<your_secret_key_id_in_vault>',  region '<your_aws_region>',  user_pool_id '<your_user_pool_id>' );

```

### Create a schema[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#create-a-schema)
We recommend creating a schema to hold all the foreign tables:
```

1
createschemaifnotexists cognito;

```

## Entities[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#entities)
We can use SQL [import foreign schema](https://www.postgresql.org/docs/current/sql-importforeignschema.html) to import foreign table definitions from Cognito.
For example, using below SQL can automatically create foreign table in the `cognito` schema.
```

1
import foreign schema cognito fromserver cognito_server into cognito;

```

The foreign table will be created as below:
### Users[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#users)
This is an object representing Cognito User Records.
Ref: [AWS Cognito User Records](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)
#### Operations[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#operations)
Object| Select| Insert| Update| Delete| Truncate  
---|---|---|---|---|---  
Users| ✅| ❌| ❌| ❌| ❌  
#### Usage[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#usage)
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
create foreign tablecognito.users ( username text, email text,statustext,enabledboolean, created_at timestamp, updated_at timestamp, attributes jsonb)server cognito_serveroptions (object'users');

```

#### Notes[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#notes)
  * Only the columns listed above are accepted in the foreign table
  * The `attributes` column contains additional user attributes in JSON format


## Query Pushdown Support[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#query-pushdown-support)
This FDW doesn't support query pushdown.
## Limitations[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#limitations)
This section describes important limitations and considerations when using this FDW:
  * No query pushdown support, all filtering must be done locally
  * Large result sets may experience slower performance due to full data transfer requirement
  * Only supports User Pool objects from Cognito API
  * No support for Identity Pool operations
  * Materialized views using these foreign tables may fail during logical backups


## Examples[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#examples)
### Basic example[#](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#basic-example)
This will create a "foreign table" inside your Postgres database called `cognito_table`:
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
create foreign tablecognito.users ( username text, email text,statustext,enabledboolean, created_at timestamp, updated_at timestamp, attributes jsonb)server cognito_serveroptions (object'users');

```

You can now fetch your Cognito data from within your Postgres database:
```

1
select*fromcognito.users;

```

[Edit this page on GitHub ](https://github.com/supabase/wrappers/blob/docs_v0.4.6-1/docs/catalog/cognito.md)
### Is this helpful?
No Yes
### On this page
[Preparation](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#preparation)[Enable Wrappers](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#enable-wrappers)[Enable the Cognito Wrapper](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#enable-the-cognito-wrapper)[Store your credentials (optional)](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#store-your-credentials-optional)[Connecting to Cognito](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#connecting-to-cognito)[Create a schema](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#create-a-schema)[Entities](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#entities)[Users](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#users)[Query Pushdown Support](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#query-pushdown-support)[Limitations](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#limitations)[Examples](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#examples)[Basic example](https://supabase.com/docs/guides/database/extensions/wrappers/cognito#basic-example)
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



