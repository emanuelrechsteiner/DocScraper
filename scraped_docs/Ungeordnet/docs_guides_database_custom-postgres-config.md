---
url: https://supabase.com/docs/guides/database/custom-postgres-config
scraped_at: 2025-05-25T08:54:48.039030
title: Customizing Postgres configs | Supabase Docs
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
  2. Configuration, optimization, and testing
  3. [Customizing Postgres config](https://supabase.com/docs/guides/database/custom-postgres-config)


Customizing Postgres configs
Each Supabase project is a pre-configured Postgres cluster. You can override some configuration settings to suit your needs. This is an advanced topic, and we don't recommend touching these settings unless it is necessary.
Customizing Postgres configurations provides _advanced_ control over your database, but inappropriate settings can lead to severe performance degradation or project instability.
### Viewing settings[#](https://supabase.com/docs/guides/database/custom-postgres-config#viewing-settings)
To list all Postgres settings and their descriptions, run:
```

1
select*from pg_settings;

```

## Configurable settings[#](https://supabase.com/docs/guides/database/custom-postgres-config#configurable-settings)
### User-context settings[#](https://supabase.com/docs/guides/database/custom-postgres-config#user-context-settings)
The [`pg_settings`](https://www.postgresql.org/docs/current/view-pg-settings.html) table's `context` column specifies the requirements for changing a setting. By default, those with a `user` context can be changed at the `role` or `database` level with [SQL](https://supabase.com/dashboard/project/_/sql/).
To list all user-context settings, run:
```

1
select*from pg_settings where context ='user';

```

As an example, the `statement_timeout` setting can be altered:
```

1
alterdatabase"postgres"set"statement_timeout"TO'60s';

```

To verify the change, execute:
```

1
show "statement_timeout";

```

### Superuser settings[#](https://supabase.com/docs/guides/database/custom-postgres-config#superuser-settings)
Some settings can only be modified by a superuser. Supabase pre-enables the [`supautils` extension](https://supabase.com/blog/roles-postgres-hooks#setting-up-the-supautils-extension), which allows the `postgres` role to retain certain superuser privileges. It enables modification of the below reserved configurations at the `role` level:
Setting| Description  
---|---  
`auto_explain.log_min_duration`| Logs query plans taking longer than this duration.  
`auto_explain.log_nested_statements`| Log nested statements' plans.  
`log_min_messages`| Minimum severity level of messages to log.  
`pg_net.ttl`| Sets how long the [pg_net extension](https://supabase.com/docs/guides/database/extensions/pg_net) saves responses  
`pg_net.batch_size`| Sets how many requests the [pg_net extension](https://supabase.com/docs/guides/database/extensions/pg_net) can make per second  
`pgaudit.*`| Configures the [PGAudit extension](https://supabase.com/docs/guides/database/extensions/pgaudit). The `log_parameter` is still restricted to protect secrets  
`pgrst.*`| [`PostgREST` settings](https://docs.postgrest.org/en/stable/references/configuration.html#db-aggregates-enabled)  
`plan_filter.*`| Configures the [pg_plan_filter extension](https://supabase.com/docs/guides/database/extensions/pg_plan_filter)  
`session_replication_role`| Sets the session's behavior for triggers and rewrite rules.  
`track_io_timing`| Collects timing statistics for database I/O activity.  
For example, to enable `log_nested_statements` for the `postgres` role, execute:
```

1
alterrole"postgres"set"auto_explain.log_nested_statements"to'on';

```

To view the change:
```

1
2
3
4
5
select rolname, rolconfigfrom pg_roleswhere rolname ='postgres';

```

### CLI configurable settings[#](https://supabase.com/docs/guides/database/custom-postgres-config#cli-configurable-settings)
While many Postgres parameters are configurable directly, some configurations can be changed with the Supabase CLI at the [`system`](https://www.postgresql.org/docs/current/config-setting.html#CONFIG-SETTING-SQL) level.
CLI changes permanently overwrite default settings, so `reset all` and `set to default` commands won't revert to the original values.
In order to overwrite the default settings, you must have `Owner` or `Administrator` privileges within your organizations.
#### CLI supported parameters[#](https://supabase.com/docs/guides/database/custom-postgres-config#cli-supported-parameters)
If a setting you need is not yet configurable, [share your use case with us](https://supabase.com/dashboard/support/new)! Let us know what setting you'd like to control, and we'll consider adding support in future updates.
The following parameters are available for overrides:
  1. [effective_cache_size](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-EFFECTIVE-CACHE-SIZE)
  2. [logical_decoding_work_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-LOGICAL-DECODING-WORK-MEM) (CLI only)
  3. [maintenance_work_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM)
  4. [max_connections](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-MAX-CONNECTIONS) (CLI only)
  5. [max_locks_per_transaction](https://www.postgresql.org/docs/current/runtime-config-locks.html#GUC-MAX-LOCKS-PER-TRANSACTION) (CLI only)
  6. [max_parallel_maintenance_workers](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-MAINTENANCE-WORKERS)
  7. [max_parallel_workers_per_gather](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER)
  8. [max_parallel_workers](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS)
  9. [max_replication_slots](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS) (CLI only)
  10. [max_slot_wal_keep_size](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE) (CLI only)
  11. [max_standby_archive_delay](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-STANDBY-ARCHIVE-DELAY) (CLI only)
  12. [max_standby_streaming_delay](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-STANDBY-STREAMING-DELAY) (CLI only)
  13. [max_wal_size](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-MAX-WAL-SIZE) (CLI only)
  14. [max_wal_senders](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS) (CLI only)
  15. [max_worker_processes](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES) (CLI only)
  16. [session_replication_role](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-SESSION-REPLICATION-ROLE)
  17. [shared_buffers](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-SHARED-BUFFERS) (CLI only)
  18. [statement_timeout](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-STATEMENT-TIMEOUT)
  19. [track_activity_query_size](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-ACTIVITY-QUERY-SIZE)
  20. [track_commit_timestamp](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-TRACK-COMMIT-TIMESTAMP)
  21. [wal_keep_size](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-KEEP-SIZE) (CLI only)
  22. [wal_sender_timeout](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) (CLI only)
  23. [work_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM)


#### Managing Postgres configuration with the CLI[#](https://supabase.com/docs/guides/database/custom-postgres-config#managing-postgres-configuration-with-the-cli)
To start:
  1. [Install](https://supabase.com/docs/guides/resources/supabase-cli) Supabase CLI 1.69.0+.
  2. [Log in](https://supabase.com/docs/guides/cli/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.


To update Postgres configurations, use the [`postgres config`](https://supabase.com/docs/reference/cli/supabase-postgres-config) command:
```

1
2
3
supabase--experimental\--project-ref <project-ref>\postgres-config update--configshared_buffers=250MB

```

By default, the CLI will merge any provided config overrides with any existing ones. The `--replace-existing-overrides` flag can be used to instead force all existing overrides to be replaced with the ones being provided:
```

1
2
3
4
supabase--experimental\--project-ref <project-ref>\postgres-config update--configmax_parallel_workers=3\--replace-existing-overrides

```

To delete specific configuration overrides, use the `postgres-config delete` command:
```

1
2
3
supabase--experimental\--project-ref <project-ref>\postgres-config delete--configshared_buffers,work_mem

```

By default, changing the configuration, whether by updating or deleting, causes the database and all associated read replicas to restart. You can use the `--no-restart` flag to prevent this behavior, and attempt to reload the updated configuration without a restart. Refer to the Postgres documentation to determine if a given parameter can be reloaded without a restart.
##### Read Replicas and Custom Config
Postgres requires several parameters to be synchronized between the Primary cluster and [Read Replicas](https://supabase.com/docs/guides/platform/read-replicas).
By default, Supabase ensures that this propagation is executed correctly. However, if the `--no-restart` behavior is used in conjunction with parameters that cannot be reloaded without a restart, the user is responsible for ensuring that both the primaries and the read replicas get restarted in a timely manner to ensure a stable running state. Leaving the configuration updated, but not utilized (via a restart) in such a case can result in read replica failure if the primary, or a read replica, restarts in isolation (e.g. due to an out-of-memory event, or hardware failure).
```

1
2
3
supabase--experimental\--project-ref <project-ref>\postgres-config delete--configshared_buffers--no-restart

```

### Resetting to default config[#](https://supabase.com/docs/guides/database/custom-postgres-config#resetting-to-default-config)
To reset a setting to its default value at the database level:
```

1
2
3
4
5
-- reset a single setting at the database levelalterdatabase"postgres"set"<setting_name>"todefault;-- reset all settings at the database levelalterdatabase"postgres"reset all;

```

For `role` level configurations, you can run:
```

1
alterrole"<role_name>"set"<setting_name>"todefault;

```

### Considerations[#](https://supabase.com/docs/guides/database/custom-postgres-config#considerations)
  1. Changes through the CLI might restart the database causing momentary disruption to existing database connections; in most cases this should not take more than a few seconds. However, you can use the --no-restart flag to bypass the restart and keep the connections intact. Keep in mind that this depends on the specific configuration changes you're making. if the change requires a restart, using the --no-restart flag will prevent the restart but you won't see those changes take effect until a restart is manually triggered. Additionally, some parameters are required to be the same on Primary and Read Replicas; not restarting in these cases can result in read replica failure if the Primary/Read Replicas restart in isolation.
  2. Custom Postgres Config will always override the default optimizations generated by Supabase. When changing compute add-ons, you should also review and update your custom Postgres Config to ensure they remain compatible and effective with the updated compute.
  3. Some parameters (e.g. `wal_keep_size`) can increase disk utilization, triggering disk expansion, which in turn can lead to [increases in your bill](https://supabase.com/docs/guides/platform/compute-add-ons#disk-io).

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/database/custom-postgres-config.mdx)
### Is this helpful?
No Yes
### On this page
[Viewing settings](https://supabase.com/docs/guides/database/custom-postgres-config#viewing-settings)[Configurable settings](https://supabase.com/docs/guides/database/custom-postgres-config#configurable-settings)[User-context settings](https://supabase.com/docs/guides/database/custom-postgres-config#user-context-settings)[Superuser settings](https://supabase.com/docs/guides/database/custom-postgres-config#superuser-settings)[CLI configurable settings](https://supabase.com/docs/guides/database/custom-postgres-config#cli-configurable-settings)[Resetting to default config](https://supabase.com/docs/guides/database/custom-postgres-config#resetting-to-default-config)[Considerations](https://supabase.com/docs/guides/database/custom-postgres-config#considerations)
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



