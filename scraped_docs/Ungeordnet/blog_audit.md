---
url: https://supabase.com/blog/audit
scraped_at: 2025-05-25T09:32:01.853436
title: Postgres Auditing in 150 lines of SQL
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
# Postgres Auditing in 150 lines of SQL
08 Mar 2022
•
13 minute read
[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Oliver RiceEngineering](https://github.com/olirice)
![Postgres Auditing in 150 lines of SQL](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupa-audit%2Fpostgres_auditing_in_150_lines_of_SQL.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Data auditing is a system that tracks changes to tables' contents over time. PostgreSQL has a robust set of features which we can leverage to create a generic auditing solution in 150 lines of SQL.
Auditing is particularly useful for historical analysis. To demonstrate, imagine you have a `users` table that tracks when a user is online. You might add a `status` column which can have one of two values: `online` and `offline`. How would you track how long a user is online for throughout an entire month? An auditing system would track every change with timestamps, and so you can measure the difference between each timestamp and sum them up for the entire month.
The goals of our auditing solution are:
  * low maintenance
  * easy to use
  * fast to query


To demonstrate what we're working towards, the following example shows what we'll have at the end of the blog post:
`
1
-- create a table
2
create table public.members (
3
 id int primary key,
4
 name text not null
5
);
67
-- Enable auditing on the new table
8
select audit.enable_tracking('public.members');
`
Produce some records to audit
`
1
-- create a new record
2
insert into public.members
3
 (id, name)
4
values
5
 (1, 'foo');
67
-- edit the record
8
update public.members
9
set name = 'bar'
10
where id = 1;
1112
-- delete the record
13
delete from public.members;
`
Review the audit log
`
1
select * from audit.record_history;
`
`
1
id | record_id | old_record_id | op | ts | table_oid | table_schema | table_name | record | old_record 
2
----+--------------------------------------+--------------------------------------+--------+-------------------------------------+-----------+--------------+------------+--------------------------+--------------------------
3
2 | 1ecd5ff0-1b6b-5bc2-ad80-1cb19769c081 | | INSERT | Mon Feb 28 18:13:52.698511 2022 PST | 16452 | public | members | {"id": 1, "name": "foo"} |
4
3 | 1ecd5ff0-1b6b-5bc2-ad80-1cb19769c081 | 1ecd5ff0-1b6b-5bc2-ad80-1cb19769c081 | UPDATE | Mon Feb 28 18:13:52.698511 2022 PST | 16452 | public | members | {"id": 1, "name": "bar"} | {"id": 1, "name": "foo"}
5
4 | | 1ecd5ff0-1b6b-5bc2-ad80-1cb19769c081 | DELETE | Mon Feb 28 18:13:52.698511 2022 PST | 16452 | public | members | | {"id": 1, "name": "bar"}
6
(3 rows)
`
Notice that our `record_id` and `old_record_id` stayed constant as we updated the row so we can easily query for a single row's history over time!
## Lets get building[#](https://supabase.com/blog/postgres-audit#lets-get-building)
### Namespace[#](https://supabase.com/blog/postgres-audit#namespace)
To quote a tenet from [the zen of python](https://www.python.org/dev/peps/pep-0020/):
> Namespaces are one honking great idea -- let's do more of those!
So first things first, we'll create a separate schema named `audit` to house our auditing entities.
`
1
create schema if not exists audit;
`
### Storage[#](https://supabase.com/blog/postgres-audit#storage)
Next, we need a table to track inserts, updates and deletes.
Classically, an audit table's schema mirrors the table being audited and appends some metadata columns like the commit's timestamp. That solution has a few maintenance challenges:
  * enabling auditing on a table requires a database migration
  * when the source table's schema changes, the audit table's schema must also change


So instead, we'll lean on PostgreSQL's schema-less [`JSONB` data type](https://www.postgresql.org/docs/current/datatype-json.html) to store each record's data in a single column. That approach has the added benefit of allowing us to store multiple tables' audit history in a single audit table.
`
1
create table audit.record_version (
2
 id bigserial primary key,
3
 -- auditing metadata
4
 record_id uuid, -- identifies a new record by it's table + primary key
5
 old_record_id uuid, -- ^
6
 op varchar(8) not null, -- INSERT/UPDATE/DELETE/TRUNCATE
7
 ts timestamptz not null default now(),
8
 -- table identifiers
9
 table_oid oid not null, -- pg internal id for a table
10
 table_schema name not null, -- audited table's schema name e.g. 'public'
11
 table_name name not null, -- audited table's table name e.g. 'account'
12
 -- record data
13
 record jsonb, -- contents of the new record
14
 old_record jsonb -- previous record contents (for UPDATE/DELETE)
15
);
`
Postgres version compatibility
The table above uses PostgreSQL's built-in [uuid functionality](https://www.postgresql.org/docs/14/functions-uuid.html), which is available from version 14. For backwards compatibility you can use the uuid-ossp extension.
`create extension if not exists "uuid-ossp";`
### Query Patterns[#](https://supabase.com/blog/postgres-audit#query-patterns)
An audit log doesn't do us much good if its too slow to query! There are 2 query patterns we think are table stakes (😉) for an audit system:
**Changes to a Table in a Time Range**
For time slices, we need an index on the `ts` column. Since the table is append-only and the `ts` column is populated by insertion date, our values for `ts` are naturally in ascending order.
PostgreSQL's builtin [BRIN index](https://www.postgresql.org/docs/current/brin-intro.html) can leverage that correlation between value and physical location to produce an index that, at scale, is many hundreds of times smaller than the default (BTREE index) with faster lookup times.
`
1
-- index ts for time range filtering
2
create index record_version_ts
3
 on audit.record_version
4
 using brin(ts);
`
For table filtering, we've included a `table_oid` column which tracks PostgreSQL's internal numeric table identifier. We can add an index to this column instead of the `table_schema` and `table_name` columns, minimizing the index size and offering better performance.
`
1
-- index table_oid for table filtering
2
create index record_version_table_oid
3
 on audit.record_version
4
 using btree(table_oid);
`
**Changes to a Record Over Time**
One of the downsides to storing each row's data as `jsonb` is that filtering based on a column's value becomes very inefficient. If we want to look up a row's history quickly, we need to extract and index a unique identifier for each row.
For the globally unique identifier, we'll use the following structure
`
1
[table_oid, primary_key_value_1, primary_key_value_2, ...]
`
and hash that array as a UUID v5 to get an efficiently indexable UUID type to identify the row that is robust to data changes.
We'll use one utility function to lookup a record's primary key column names:
`
1
create or replace function audit.primary_key_columns(entity_oid oid)
2
  returns text[]
3
  stable
4
  security definer
5
  language sql
6
as $$
7
  -- Looks up the names of a table's primary key columns
8
  select
9
    coalesce(
10
      array_agg(pa.attname::text order by pa.attnum),
11
      array[]::text[]
12
    ) column_names
13
  from
14
    pg_index pi
15
    join pg_attribute pa
16
      on pi.indrelid = pa.attrelid
17
      and pa.attnum = any(pi.indkey)
18
  where
19
    indrelid = $1
20
    and indisprimary
21
$$;
`
and another to consume the `table_oid` and primary key, converting the result into the record's UUID.
`
1
create or replace function audit.to_record_id(
2
		entity_oid oid,
3
		pkey_cols text[],
4
		rec jsonb
5
)
6
  returns uuid
7
  stable
8
  language sql
9
as $$
10
  select
11
    case
12
      when rec is null then null
13
						-- if no primary key exists, use a random uuid
14
      when pkey_cols = array[]::text[] then gen_random_uuid()
15
      else (
16
        select
17
          uuid_generate_v5(
18
            'fd62bc3d-8d6e-43c2-919c-802ba3762271',
19
            (
20
													jsonb_build_array(to_jsonb($1))
21
													|| jsonb_agg($3 ->> key_)
22
												)::text
23
          )
24
        from
25
          unnest($2) x(key_)
26
      )
27
    end
28
$$;
`
Finally, we index the `record_id` and `old_record_id` columns that contain these unique identifiers for fast querying.
`
1
-- index record_id for fast searching
2
create index record_version_record_id on audit.record_version (record_id)
3
where record_id is not null;
45
-- index old_record_id for fast searching
6
create index record_version_old_record_id on audit.record_version (record_id)
7
where old_record_id is not null;
`
### Enrollment[#](https://supabase.com/blog/postgres-audit#enrollment)
Okay, so we have a home for our audit data that we're confident it can be queried efficiently. Now how do we populate it?
We need the audit table to populate without end-users making any changes to their transactions. So we'll set up a [trigger](https://www.postgresql.org/docs/current/sql-createtrigger.html) to fire when the data changes. In this case, we'll fire the trigger once for every inserted/updated/deleted row.
`
1
create or replace function audit.insert_update_delete_trigger()
2
  returns trigger
3
  security definer
4
  language plpgsql
5
as $$
6
declare
7
  pkey_cols text[] = audit.primary_key_columns(TG_RELID);
8
  record_jsonb jsonb = to_jsonb(new);
9
  record_id uuid = audit.to_record_id(TG_RELID, pkey_cols, record_jsonb);
10
  old_record_jsonb jsonb = to_jsonb(old);
11
  old_record_id uuid = audit.to_record_id(TG_RELID, pkey_cols, old_record_jsonb);
12
begin
1314
  insert into audit.record_version(
15
    record_id,
16
    old_record_id,
17
    op,
18
    table_oid,
19
    table_schema,
20
    table_name,
21
    record,
22
    old_record
23
  )
24
  select
25
    record_id,
26
    old_record_id,
27
    TG_OP,
28
    TG_RELID,
29
    TG_TABLE_SCHEMA,
30
    TG_TABLE_NAME,
31
    record_jsonb,
32
    old_record_jsonb;
3334
  return coalesce(new, old);
35
end;
36
$$;
`
## Public API[#](https://supabase.com/blog/postgres-audit#public-api)
Finally, we'll wrap up the trigger creation and removal process behind a clean, idempotent, user facing API.
The API we'll expose for enabling auditing on a table is
`
1
select audit.enable_tracking('<schema>.<table>'::regclass);
`
and for disabling tracking
`
1
select audit.disable_tracking('<schema>.<table>'::regclass);
`
Under the hood, those functions register our auditing trigger against the requested table.
`
1
create or replace function audit.enable_tracking(regclass)
2
  returns void
3
  volatile
4
  security definer
5
  language plpgsql
6
as $$
7
declare
8
  statement_row text = format('
9
    create trigger audit_i_u_d
10
      before insert or update or delete
11
      on %I
12
      for each row
13
      execute procedure audit.insert_update_delete_trigger();',
14
    $1
15
  );
1617
  pkey_cols text[] = audit.primary_key_columns($1);
18
begin
19
  if pkey_cols = array[]::text[] then
20
    raise exception 'Table % can not be audited because it has no primary key', $1;
21
  end if;
2223
  if not exists(select 1 from pg_trigger where tgrelid = $1 and tgname = 'audit_i_u_d') then
24
    execute statement_row;
25
  end if;
26
end;
27
$$;
2829
create or replace function audit.disable_tracking(regclass)
30
  returns void
31
  volatile
32
  security definer
33
  language plpgsql
34
as $$
35
declare
36
  statement_row text = format(
37
    'drop trigger if exists audit_i_u_d on %I;',
38
    $1
39
  );
40
begin
41
  execute statement_row;
42
end;
43
$$;
`
And we're done with 2 lines of code to spare!
### Performance[#](https://supabase.com/blog/postgres-audit#performance)
Auditing tables always reduces throughput of inserts, updates, and deletes. In cases where throughput is less than 1000 writes per second the overhead is typically negligible. For tables with a higher write frequency, consider logging changes outside of SQL with a tool like [pgAudit](https://www.pgaudit.org/).
### Do I really expect you to copy/paste all that?[#](https://supabase.com/blog/postgres-audit#do-i-really-expect-you-to-copypaste-all-that)
Nope, for a turnkey solution to auditing in PostgreSQL, we've packaged this script into an extension with some extra goodies like `TRUNCATE` support. Check it out at <https://github.com/supabase/supa_audit>.
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&text=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&text=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&t=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)
[Last postSupabase Launch Week 425 March 2022](https://supabase.com/blog/supabase-launch-week-four)
[Next postSupabase Beta January 202222 February 2022](https://supabase.com/blog/supabase-beta-january-2022)
[postgres](https://supabase.com/blog/tags/postgres)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [Lets get building](https://supabase.com/blog/postgres-audit#lets-get-building)
    * [Namespace](https://supabase.com/blog/postgres-audit#namespace)
    * [Storage](https://supabase.com/blog/postgres-audit#storage)
    * [Query Patterns](https://supabase.com/blog/postgres-audit#query-patterns)
    * [Enrollment](https://supabase.com/blog/postgres-audit#enrollment)
  * [Public API](https://supabase.com/blog/postgres-audit#public-api)
    * [Performance](https://supabase.com/blog/postgres-audit#performance)
    * [Do I really expect you to copy/paste all that?](https://supabase.com/blog/postgres-audit#do-i-really-expect-you-to-copypaste-all-that)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&text=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&text=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&t=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)
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

