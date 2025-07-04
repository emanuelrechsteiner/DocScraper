---
url: https://supabase.com/docs/guides/database/extensions/pg_net
scraped_at: 2025-05-25T09:50:12.574813
title: pg_net: Async Networking | Supabase Docs
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
  3. [pg_net: Async Networking](https://supabase.com/docs/guides/database/extensions/pg_net)


pg_net: Async Networking
The pg_net API is in beta. Functions signatures may change.
[pg_net](https://github.com/supabase/pg_net/) enables Postgres to make asynchronous HTTP/HTTPS requests in SQL. It differs from the [`http`](https://supabase.com/docs/guides/database/extensions/http) extension in that it is asynchronous by default. This makes it useful in blocking functions (like triggers).
It eliminates the need for servers to continuously poll for database changes and instead allows the database to proactively notify external resources about significant events.
## Enable the extension[#](https://supabase.com/docs/guides/database/extensions/pg_net#enable-the-extension)
DashboardSQL
```

1
2
3
4
5
6
7
-- Example: enable the "pg_net" extension.create extension pg_net;-- Note: The extension creates its own schema/namespace named "net" to avoid naming conflicts.-- Example: disable the "pg_net" extensiondrop extension ifexists pg_net;dropschema net;

```

Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension". To disable an extension, call `drop extension`.
Procedural languages are automatically installed within `pg_catalog`, so you don't need to specify a schema.
## `http_get`[#](https://supabase.com/docs/guides/database/extensions/pg_net#httpget)
Creates an HTTP GET request returning the request's ID. HTTP requests are not started until the transaction is committed.
### Signature [#](https://supabase.com/docs/guides/database/extensions/pg_net#get-signature)
This is a Postgres [SECURITY DEFINER](https://supabase.com/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function.
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
net.http_get(-- url for the requesturltext,-- key/value pairs to be url encoded and appended to the `url`  params jsonb default'{}'::jsonb,-- key/values to be included in request headers  headers jsonb default'{}'::jsonb,-- the maximum number of milliseconds the request may take before being canceled  timeout_milliseconds intdefault2000)-- request_id referencereturnsbigint  strict  volatile  parallel safelanguage plpgsql

```

### Usage [#](https://supabase.com/docs/guides/database/extensions/pg_net#get-usage)
```

1
2
3
4
5
6
7
selectnet.http_get('https://news.ycombinator.com')as request_id;request_id----------1(1row)

```

## `http_post`[#](https://supabase.com/docs/guides/database/extensions/pg_net#httppost)
Creates an HTTP POST request with a JSON body, returning the request's ID. HTTP requests are not started until the transaction is committed.
The body's character set encoding matches the database's `server_encoding` setting.
### Signature [#](https://supabase.com/docs/guides/database/extensions/pg_net#post-signature)
This is a Postgres [SECURITY DEFINER](https://supabase.com/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function
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
net.http_post(-- url for the requesturltext,-- body of the POST request  body jsonb default'{}'::jsonb,-- key/value pairs to be url encoded and appended to the `url`  params jsonb default'{}'::jsonb,-- key/values to be included in request headers  headers jsonb default'{"Content-Type": "application/json"}'::jsonb,-- the maximum number of milliseconds the request may take before being canceled  timeout_milliseconds intdefault2000)-- request_id referencereturnsbigint  volatile  parallel safelanguage plpgsql

```

### Usage [#](https://supabase.com/docs/guides/database/extensions/pg_net#post-usage)
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
selectnet.http_post(url:='https://httpbin.org/post',    body:='{"hello": "world"}'::jsonb  ) as request_id;request_id----------1(1row)

```

## `http_delete`[#](https://supabase.com/docs/guides/database/extensions/pg_net#httpdelete)
Creates an HTTP DELETE request, returning the request's ID. HTTP requests are not started until the transaction is committed.
### Signature [#](https://supabase.com/docs/guides/database/extensions/pg_net#post-signature)
This is a Postgres [SECURITY DEFINER](https://supabase.com/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function
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
net.http_delete(-- url for the requesturltext,-- key/value pairs to be url encoded and appended to the `url`  params jsonb default'{}'::jsonb,-- key/values to be included in request headers  headers jsonb default'{}'::jsonb,-- the maximum number of milliseconds the request may take before being canceled  timeout_milliseconds intdefault2000)-- request_id referencereturnsbigint  strict  volatile  parallel safelanguage plpgsqlsecurity definer

```

### Usage [#](https://supabase.com/docs/guides/database/extensions/pg_net#delete-usage)
```

1
2
3
4
5
6
7
selectnet.http_delete('https://dummy.restapiexample.com/api/v1/delete/2'  ) as request_id;----------1(1row)

```

## Analyzing responses[#](https://supabase.com/docs/guides/database/extensions/pg_net#analyzing-responses)
Waiting requests are stored in the `net.http_request_queue` table. Upon execution, they are deleted.
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
CREATE UNLOGGED TABLEnet.http_request_queue (    id bigintNOT NULLDEFAULT nextval('net.http_request_queue_id_seq'::regclass),    method textNOT NULL,urltextNOT NULL,    headers jsonb NOT NULL,    body byteaNULL,    timeout_milliseconds integerNOT NULL  )

```

Once a response is returned, by default, it is stored for 6 hours in the `net._http_response` table.
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
CREATE UNLOGGED TABLEnet._http_response (    id bigintNULL,    status_code integerNULL,    content_type textNULL,    headers jsonb NULL,    content textNULL,    timed_out booleanNULL,    error_msg textNULL,    created timestamp with time zoneNOT NULLDEFAULTnow()  )

```

The responses can be observed with the following query:
```

1
select*fromnet._http_response;

```

The data can also be observed in the `net` schema with the [Supabase Dashboard's SQL Editor](https://supabase.com/dashboard/project/_/editor)
## Debugging requests[#](https://supabase.com/docs/guides/database/extensions/pg_net#debugging-requests)
### Inspecting request data[#](https://supabase.com/docs/guides/database/extensions/pg_net#inspecting-request-data)
The [Postman Echo API](https://documenter.getpostman.com/view/5025623/SWTG5aqV) returns a response with the same body and content as the request. It can be used to inspect the data being sent.
Sending a post request to the echo API
```

1
2
3
4
5
selectnet.http_post(url :='https://postman-echo.com/post',    body :='{"key1": "value", "key2": 5}'::jsonb  ) as request_id;

```

Inspecting the echo API response content to ensure it contains the right body
```

1
2
3
4
5
6
select"content"fromnet._http_responsewhere id =<request_id>-- returns information about the request-- including the body sent: {"key": "value", "key": 5}

```

Alternatively, by wrapping a request in a [database function](https://supabase.com/docs/guides/database/functions), sent row data can be logged or returned for inspection and debugging.
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
create or replacefunctiondebugging_example (row_id int)returns jsonb as $$declare-- Store payload data  row_data_var jsonb;begin-- Retrieve row data and convert to JSONselect to_jsonb("<example_table>".*) into row_data_varfrom"<example_table>"where"<example_table>".id = row_id;-- Initiate HTTP POST request to URL  performnet.http_post(url :='https://postman-echo.com/post',-- Use row data as payload      body := row_data_var    ) as request_id;-- Optionally Log row data or other data for inspection in Supabase Dashboard's Postgres Logs  raise log'Logging an entire row as JSON (%)', row_data_var;-- return row data to inspectreturn row_data_var;-- Handle exceptions here if neededexceptionwhen others then    raise exception 'An error occurred: %', SQLERRM;end;$$ language plpgsql;-- calling functionselect debugging_example(<row_id>);

```

### Inspecting failed requests[#](https://supabase.com/docs/guides/database/extensions/pg_net#inspecting-failed-requests)
Finds all failed requests
```

1
2
3
4
5
select*fromnet._http_responsewhere"status_code">=400or"error_msg"is not nullorder by"created"desc;

```

## Configuration[#](https://supabase.com/docs/guides/database/extensions/pg_net#configuration)
##### Must be on pg_net v0.12.0 or above to reconfigure 
Supabase supports reconfiguring pg*net starting from v0.12.0+. For the latest release, initiate a Postgres upgrade in the [Infrastructure Settings](https://supabase.com/dashboard/project/*/settings/infrastructure).
The extension is configured to reliably execute up to 200 requests per second. The response messages are stored for only 6 hours to prevent needless buildup. The default behavior can be modified by rewriting config variables.
### Get current settings[#](https://supabase.com/docs/guides/database/extensions/pg_net#get-current-settings)
```

1
2
3
4
5
select"name","setting"from pg_settingswhere"name"like'pg_net%';

```

### Alter settings[#](https://supabase.com/docs/guides/database/extensions/pg_net#alter-settings)
Change variables:
```

1
2
alterrole"postgres"setpg_net.ttlto'24 hours';alterrole"postgres"setpg_net.batch_sizeto500;

```

Then reload the settings and restart the `pg_net` background worker with:
```

1
selectnet.worker_restart();

```

## Examples[#](https://supabase.com/docs/guides/database/extensions/pg_net#examples)
### Invoke a Supabase Edge Function[#](https://supabase.com/docs/guides/database/extensions/pg_net#invoke-a-supabase-edge-function)
Make a POST request to a Supabase Edge Function with auth header and JSON body payload:
```

1
2
3
4
5
6
selectnet.http_post(url:='https://project-ref.supabase.co/functions/v1/function-name',    headers:='{"Content-Type": "application/json", "Authorization": "Bearer <YOUR_ANON_KEY>"}'::jsonb,    body:='{"name": "pg_net"}'::jsonb  ) as request_id;

```

### Call an endpoint every minute with [pg_cron](https://supabase.com/docs/guides/database/extensions/pgcron)[#](https://supabase.com/docs/guides/database/extensions/pg_net#call-an-endpoint-every-minute-with-pgcron)
The pg_cron extension enables Postgres to become its own cron server. With it you can schedule regular calls with up to a minute precision to endpoints.
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
selectcron.schedule('cron-job-name','* * * * *', -- Executes every minute (cron syntax)	$$-- SQL queryselect"net"."http_post"(-- URL of Edge functionurl:='https://project-ref.supabase.co/functions/v1/function-name',      headers:='{"Authorization": "Bearer <YOUR_ANON_KEY>"}'::jsonb,      body:='{"name": "pg_net"}'::jsonb	  ) as"request_id";	$$);

```

### Execute pg_net in a trigger[#](https://supabase.com/docs/guides/database/extensions/pg_net#execute-pgnet-in-a-trigger)
Make a call to an external endpoint when a trigger event occurs.
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
-- function called by triggercreateorreplacefunction<function_name>()returns triggerlanguage plpgSQLas $$begin-- calls pg_net function net.http_post-- sends request to postman API  perform "net"."http_post"('https://postman-echo.com/post'::text,   jsonb_build_object('old_row', to_jsonb(old.*),'new_row', to_jsonb(new.*)   ),   headers:='{"Content-Type": "application/json"}'::jsonb  ) as request_id;return new;END $$;-- trigger for table updatecreate trigger <trigger_name>afterupdateon<table_name>for each rowexecutefunction<function_name>();

```

### Send multiple table rows in one request[#](https://supabase.com/docs/guides/database/extensions/pg_net#send-multiple-table-rows-in-one-request)
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
with"selected_table_rows"as (select-- Converts all the rows into a JSONB array    jsonb_agg(to_jsonb(<table_name>.*)) as JSON_payloadfrom<table_name>-- good practice to LIMIT the max amount of rows)selectnet.http_post(url :='https://postman-echo.com/post'::text,    body := JSON_payload  ) AS request_idFROM"selected_table_rows";

```

More examples can be seen on the [Extension's GitHub page](https://github.com/supabase/pg_net/)
## Limitations[#](https://supabase.com/docs/guides/database/extensions/pg_net#limitations)
  * To improve speed and performance, the requests and responses are stored in [unlogged tables](https://pgpedia.info/u/unlogged-table.html), which are not preserved during a crash or unclean shutdown.
  * By default, response data is saved for only 6 hours
  * Can only make POST requests with JSON data. No other data formats are supported
  * Intended to handle at most 200 requests per second. Increasing the rate can introduce instability
  * Does not have support for PATCH/PUT requests
  * Can only work with one database at a time. It defaults to the `postgres` database.


## Resources[#](https://supabase.com/docs/guides/database/extensions/pg_net#resources)
  * Source code: [github.com/supabase/pg_net](https://github.com/supabase/pg_net/)
  * Official Docs: [github.com/supabase/pg_net](https://github.com/supabase/pg_net/)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/database/extensions/pg_net.mdx)
### Is this helpful?
No Yes
### On this page
[Enable the extension](https://supabase.com/docs/guides/database/extensions/pg_net#enable-the-extension)[http_get](https://supabase.com/docs/guides/database/extensions/pg_net#httpget)[Signature ](https://supabase.com/docs/guides/database/extensions/pg_net#get-signature)[Usage ](https://supabase.com/docs/guides/database/extensions/pg_net#get-usage)[http_post](https://supabase.com/docs/guides/database/extensions/pg_net#httppost)[Signature ](https://supabase.com/docs/guides/database/extensions/pg_net#post-signature)[Usage ](https://supabase.com/docs/guides/database/extensions/pg_net#post-usage)[http_delete](https://supabase.com/docs/guides/database/extensions/pg_net#httpdelete)[Signature ](https://supabase.com/docs/guides/database/extensions/pg_net#post-signature)[Usage ](https://supabase.com/docs/guides/database/extensions/pg_net#delete-usage)[Analyzing responses](https://supabase.com/docs/guides/database/extensions/pg_net#analyzing-responses)[Debugging requests](https://supabase.com/docs/guides/database/extensions/pg_net#debugging-requests)[Inspecting request data](https://supabase.com/docs/guides/database/extensions/pg_net#inspecting-request-data)[Inspecting failed requests](https://supabase.com/docs/guides/database/extensions/pg_net#inspecting-failed-requests)[Configuration](https://supabase.com/docs/guides/database/extensions/pg_net#configuration)[Get current settings](https://supabase.com/docs/guides/database/extensions/pg_net#get-current-settings)[Alter settings](https://supabase.com/docs/guides/database/extensions/pg_net#alter-settings)[Examples](https://supabase.com/docs/guides/database/extensions/pg_net#examples)[Invoke a Supabase Edge Function](https://supabase.com/docs/guides/database/extensions/pg_net#invoke-a-supabase-edge-function)[Call an endpoint every minute with pg_cron](https://supabase.com/docs/guides/database/extensions/pg_net#https://supabase.com/docs/guides/database/extensions/pgcron)[Execute pg_net in a trigger](https://supabase.com/docs/guides/database/extensions/pg_net#execute-pgnet-in-a-trigger)[Send multiple table rows in one request](https://supabase.com/docs/guides/database/extensions/pg_net#send-multiple-table-rows-in-one-request)[Limitations](https://supabase.com/docs/guides/database/extensions/pg_net#limitations)[Resources](https://supabase.com/docs/guides/database/extensions/pg_net#resources)
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



