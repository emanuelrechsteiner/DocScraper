---
url: https://supabase.com/docs/guides/database/extensions/wrappers/s3
scraped_at: 2025-05-25T09:12:30.285814
title: AWS S3 | Supabase Docs
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
  3. [Connecting to AWS S3](https://supabase.com/docs/guides/database/extensions/wrappers/s3)


AWS S3
[AWS S3](https://aws.amazon.com/s3/) is an object storage service offering industry-leading scalability, data availability, security, and performance. It is read-only and supports below file formats:
The S3 Wrapper allows you to read data of below formats from S3 within your Postgres database.
  1. CSV - with or without header line
  2. [JSON Lines](https://jsonlines.org/)
  3. [Parquet](https://parquet.apache.org/)


The S3 Wrapper also supports below compression algorithms:
  1. gzip
  2. bzip2
  3. xz
  4. zlib


**Note for CSV and JSONL files: currently all columns in S3 files must be defined in the foreign table and their types must be`text` type**.
**Note for Parquet files: the whole Parquet file will be loaded into local memory if it is compressed, so keep the file size as small as possible**.
## Preparation[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#preparation)
Before you can query S3, you need to enable the Wrappers extension and store your credentials in Postgres.
### Enable Wrappers[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#enable-wrappers)
Make sure the `wrappers` extension is installed on your database:
```

1
create extension ifnotexists wrappers withschema extensions;

```

### Enable the S3 Wrapper[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#enable-the-s3-wrapper)
Enable the `s3_wrapper` FDW:
```

1
2
3
create foreign data wrapper s3_wrapper handler s3_fdw_handler validator s3_fdw_validator;

```

### Store your credentials (optional)[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#store-your-credentials-optional)
By default, Postgres stores FDW credentials inside `pg_catalog.pg_foreign_server` in plain text. Anyone with access to this table will be able to view these credentials. Wrappers is designed to work with [Vault](https://supabase.com/docs/guides/database/vault), which provides an additional level of security for storing credentials. We recommend using Vault to store your credentials.
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
-- Save your AWS credentials in Vault and retrieve the created `s3_access_key_id` and `s3_secret_access_key`selectvault.create_secret('<access key id>','s3_access_key_id','AWS access key for Wrappers');selectvault.create_secret('<secret access key>''s3_secret_access_key','AWS secret access key for Wrappers');

```

### Connecting to S3[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#connecting-to-s3)
We need to provide Postgres with the credentials to connect to S3, and any additional options. We can do this using the `create server` command:
With VaultWithout Vault
```

1
2
3
4
5
6
7
createserver s3_server foreign data wrapper s3_wrapper options (  vault_access_key_id '<your s3_access_key_id from above>',  vault_secret_access_key '<your s3_secret_access_key from above>',  aws_region 'us-east-1' );

```

The full list of options are below:
  * `aws_access_key_id` (required) - Your access key
  * `aws_secret_access_key` (required) - Your secret key
  * `aws_region` (required) - The region of your bucket (if providing an endpoint URL with a region in it, make sure that they are the same)
  * `endpoint_url` (optional) - An optional URL to allow connection to S3-compliant providers (i.e. Wasabi, Cloudflare R2, Backblaze B2, DigitalOcean Spaces)
  * `path_style_url` (optional) - Whether to use [path-style URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#path-style-access) access. This is required by some S3-compliant providers. `true` or `false`, default is `false`.


#### Required S3 permissions[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#required-s3-permissions)
Below S3 permissions are needed:
  * s3:GetObject
  * s3:GetObjectAttributes


If the bucket is versioned, we also need:
  * s3:GetObjectVersion
  * s3:GetObjectVersionAttributes


### Connecting to S3-compliant Providers - Supabase Storage[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#connecting-to-s3-compliant-providers---supabase-storage)
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
createserver s3_server foreign data wrapper s3_wrapper options (  aws_access_key_id '<supabase_storage_access_key>',  aws_secret_access_key '<supabase_storage_secret_key>',  aws_region 'eu-central-1',endpoint_url'https://<project_ref>.supabase.co/storage/v1/s3',  path_style_url 'true' );

```

### Connecting to S3-compliant Providers - Wasabi[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#connecting-to-s3-compliant-providers---wasabi)
```

1
2
3
4
5
6
7
8
createserver s3_server foreign data wrapper s3_wrapper options (  aws_access_key_id '<your_wasabi_access_key>',  aws_secret_access_key '<your_wasabi_secret_key>',  aws_region 'eu-central-1',endpoint_url'https://s3.eu-central-1.wasabisys.com' );

```

### Create a schema[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#create-a-schema)
We recommend creating a schema to hold all the foreign tables:
```

1
createschemaifnotexists s3;

```

## Options[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#options)
The following options are available when creating S3 foreign tables:
  * `uri` - S3 URI, required. For example, `s3://bucket/s3_table.csv`
  * `format` - File format, required. `csv`, `jsonl`, or `parquet`
  * `has_header` - If the CSV file has header, optional. `true` or `false`, default is `false`
  * `compress` - Compression algorithm, optional. One of `gzip`, `bzip2`, `xz`, `zlib`, default is no compression


## Entities[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#entities)
### CSV Files[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#csv-files)
This is an object representing CSV files in S3.
Ref: [AWS S3 docs](https://aws.amazon.com/s3/)
#### Operations[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#operations)
Object| Select| Insert| Update| Delete| Truncate  
---|---|---|---|---|---  
CSV| ✅| ❌| ❌| ❌| ❌  
#### Usage[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#usage)
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
create foreign tables3.table_csv (nametext, sex text, age text, height text,weighttext)server s3_server options (  uri 's3://bucket/s3_table.csv',  format 'csv',  has_header 'true' );

```

#### Notes[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#notes)
  * All columns must be defined in the foreign table
  * All column types must be `text`
  * Optional header support via `has_header` option
  * Supports compression (gzip, bzip2, xz, zlib)


### JSON Lines Files[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#json-lines-files)
This is an object representing JSONL files in S3.
Ref: [JSONL docs](https://jsonlines.org/)
#### Operations[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#operations-1)
Object| Select| Insert| Update| Delete| Truncate  
---|---|---|---|---|---  
JSONL| ✅| ❌| ❌| ❌| ❌  
#### Usage[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#usage-1)
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
create foreign tables3.table_jsonl (nametext, sex text, age text, height text,weighttext)server s3_server options (  uri 's3://bucket/s3_table.jsonl',  format 'jsonl' );

```

#### Notes[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#notes-1)
  * All columns must be defined in the foreign table
  * All column types must be `text`
  * Each line must be a valid JSON object
  * Supports compression (gzip, bzip2, xz, zlib)


### Parquet Files[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#parquet-files)
This is an object representing Parquet files in S3.
Ref: [Parquet docs](https://parquet.apache.org/)
#### Operations[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#operations-2)
Object| Select| Insert| Update| Delete| Truncate  
---|---|---|---|---|---  
Parquet| ✅| ❌| ❌| ❌| ❌  
#### Usage[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#usage-2)
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
create foreign tables3.table_parquet ( id integer, bool_col boolean, bigint_col bigint, float_col real, date_string_col text, timestamp_col timestamp)server s3_server options (  uri 's3://bucket/s3_table.parquet',  format 'parquet' );

```

#### Notes[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#notes-2)
  * Not all columns need to be defined in foreign table
  * Column names must match between Parquet file and foreign table
  * Supports various Postgres data types (see Data Types section)
  * Compressed files are loaded entirely into memory
  * Supports compression (gzip, bzip2, xz, zlib)


## Query Pushdown Support[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#query-pushdown-support)
This FDW doesn't support query pushdown.
## Supported Data Types For Parquet File[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#supported-data-types-for-parquet-file)
The S3 Wrapper uses Parquet file data types from [arrow_array::types](https://docs.rs/arrow-array/41.0.0/arrow_array/types/index.html), below are their mappings to Postgres data types.
Postgres Type| Parquet Type  
---|---  
boolean| BooleanType  
char| Int8Type  
smallint| Int16Type  
real| Float32Type  
integer| Int32Type  
double precision| Float64Type  
bigint| Int64Type  
numeric| Float64Type  
text| ByteArrayType  
date| Date64Type  
timestamp| TimestampNanosecondType  
timestamptz| TimestampNanosecondType  
## Limitations[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#limitations)
This section describes important limitations and considerations when using this FDW:
  * Large result sets experience slower performance due to full data transfer requirement
  * Compressed files are loaded entirely into memory and have additional processing overhead
  * CSV and JSONL columns must be defined as `text` type only
  * All columns must be defined in foreign tables for CSV and JSONL
  * Column names must match exactly for Parquet files
  * No support for S3 Select or other S3-side filtering
  * Materialized views using these foreign tables may fail during logical backups


## Examples[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#examples)
### Basic Example[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#basic-example)
This will create some "foreign table" inside your Postgres database can read data from S3:
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
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
-- CSV file, no compressioncreate foreign tables3.table_csv (nametext, sex text, age text, height text,weighttext)server s3_server options (  uri 's3://bucket/s3_table.csv',  format 'csv',  has_header 'true' );-- JSON line file, no compressioncreate foreign tables3.table_jsonl (nametext, sex text, age text, height text,weighttext)server s3_server options (  uri 's3://bucket/s3_table.jsonl',  format 'jsonl' );-- GZIP compressed CSV filecreate foreign tables3.table_csv_gzip (nametext, sex text, age text, height text,weighttext)server s3_server options (  uri 's3://bucket/s3_table.csv.gz',  format 'csv',  has_header 'true',  compress 'gzip' );-- Parquet file, no compressioncreate foreign tables3.table_parquet ( id integer, bool_col boolean, bigint_col bigint, float_col real, date_string_col text, timestamp_col timestamp)server s3_server options (  uri 's3://bucket/s3_table.parquet',  format 'parquet' );-- GZIP compressed Parquet filecreate foreign tables3.table_parquet_gz ( id integer, bool_col boolean, bigint_col bigint, float_col real, date_string_col text, timestamp_col timestamp)server s3_server options (  uri 's3://bucket/s3_table.parquet.gz',  format 'parquet',  compress 'gzip' );

```

### Read from Supabase Storage[#](https://supabase.com/docs/guides/database/extensions/wrappers/s3#read-from-supabase-storage)
This example will read a CSV file stored on Supabase Storage. The access information can be found on [Supabase Storage settings page](https://supabase.com/dashboard/project/_/settings/storage).
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
createserver s3_server foreign data wrapper s3_wrapper options (  aws_access_key_id '<access key ID>',  aws_secret_access_key '<secret access key>',  aws_region '<region>',endpoint_url'https://<project_ref>.supabase.co/storage/v1/s3',  path_style_url 'true' );create foreign tables3.supabase_table_csv ( id text,nametext)server s3_server options (  uri 's3://mybucket/myfile.csv',  format 'csv',  has_header 'true' );

```

[Edit this page on GitHub ](https://github.com/supabase/wrappers/blob/docs_v0.4.6-1/docs/catalog/s3.md)
### Is this helpful?
No Yes
### On this page
[Preparation](https://supabase.com/docs/guides/database/extensions/wrappers/s3#preparation)[Enable Wrappers](https://supabase.com/docs/guides/database/extensions/wrappers/s3#enable-wrappers)[Enable the S3 Wrapper](https://supabase.com/docs/guides/database/extensions/wrappers/s3#enable-the-s3-wrapper)[Store your credentials (optional)](https://supabase.com/docs/guides/database/extensions/wrappers/s3#store-your-credentials-optional)[Connecting to S3](https://supabase.com/docs/guides/database/extensions/wrappers/s3#connecting-to-s3)[Connecting to S3-compliant Providers - Supabase Storage](https://supabase.com/docs/guides/database/extensions/wrappers/s3#connecting-to-s3-compliant-providers---supabase-storage)[Connecting to S3-compliant Providers - Wasabi](https://supabase.com/docs/guides/database/extensions/wrappers/s3#connecting-to-s3-compliant-providers---wasabi)[Create a schema](https://supabase.com/docs/guides/database/extensions/wrappers/s3#create-a-schema)[Options](https://supabase.com/docs/guides/database/extensions/wrappers/s3#options)[Entities](https://supabase.com/docs/guides/database/extensions/wrappers/s3#entities)[CSV Files](https://supabase.com/docs/guides/database/extensions/wrappers/s3#csv-files)[JSON Lines Files](https://supabase.com/docs/guides/database/extensions/wrappers/s3#json-lines-files)[Parquet Files](https://supabase.com/docs/guides/database/extensions/wrappers/s3#parquet-files)[Query Pushdown Support](https://supabase.com/docs/guides/database/extensions/wrappers/s3#query-pushdown-support)[Supported Data Types For Parquet File](https://supabase.com/docs/guides/database/extensions/wrappers/s3#supported-data-types-for-parquet-file)[Limitations](https://supabase.com/docs/guides/database/extensions/wrappers/s3#limitations)[Examples](https://supabase.com/docs/guides/database/extensions/wrappers/s3#examples)[Basic Example](https://supabase.com/docs/guides/database/extensions/wrappers/s3#basic-example)[Read from Supabase Storage](https://supabase.com/docs/guides/database/extensions/wrappers/s3#read-from-supabase-storage)
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



