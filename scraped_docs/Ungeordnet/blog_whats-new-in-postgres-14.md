---
url: https://supabase.com/blog/whats-new-in-postgres-14
scraped_at: 2025-05-25T09:49:52.868601
title: New in PostgreSQL 14: What every developer should know
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
# New in PostgreSQL 14: What every developer should know
28 Nov 2021
•
8 minute read
[![Gurjeet Singh avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgurjeet.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Gurjeet SinghEngineering](https://github.com/gurjeet)
![New in PostgreSQL 14: What every developer should know](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fwhats-new-in-postgres-14%2Fwhats-new-in-postgres-14-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Every web developer knows the importance of choosing a suitable database for building modern apps. Even though NoSQL, NewSQL, and other types of databases have received a great deal of buzz in the last few years, relational database management systems (or RDBMS) are still relevant for several critical business use cases and will likely do so in the foreseeable future. Among the many open-source relational databases available, [PostgreSQL](https://supabase.com/docs/guides/database/introduction) is a popular choice among developers. It was named [DBMS of the year in 2020](https://db-engines.com/en/blog_post/85) by DBEngines, and with every release of PostgreSQL new features are available making it easy for developers and administrators to run their apps.
This blog will highlight some key features of the newly available PostgreSQL 14, which every developer can benefit from. So, let's dive right in.
## Complex data type support[#](https://supabase.com/blog/whats-new-in-postgres-14#complex-data-type-support)
### JSON subscripting[#](https://supabase.com/blog/whats-new-in-postgres-14#json-subscripting)
PostgreSQL continues to add innovations for complex data types, making JSON data more accessible. In postgreSQL 14, developers can use subscripts to iterate through JSON key pairs and fetch corresponding values. For example, using this capability, nested JSON fields can be quickly traversed to retrieve values to reconstruct application objects.
hideCopy
`
1
select (
2
 '{ "PostgreSQL": { "release": 14 }}'::jsonb
3
)['PostgreSQL']['release'];
45
 jsonb
6
-------
7
 14
`
### Working with disjointed data ranges[#](https://supabase.com/blog/whats-new-in-postgres-14#working-with-disjointed-data-ranges)
In the real world, data ranges are pretty common. For example, if you have sensor readings going into a PostgreSQL database, you may want to define a range for low, medium, and high metrics. Before version 14, you could set data ranges for integers, numerics, timestamps, and other data types. However, these ranges had to be contiguous, and it required multiple insert records across the different ranges. In PostgreSQL 14, a single insert statement can be used to map data across multiple noncontiguous ranges. Let's check it out with an example.
First, create an enum data type to capture low, medium, and high sensor reading levels.
hideCopy
`
1
create type valid_levels as enum (
2
 'low', 'medium', 'high'
3
);
`
To store sensor reading metric data, create a table consisting of the sensor description, the level and the range of timestamps when the sensor was at that level.
hideCopy
`
1
create table sensor_range (
2
 reading_id serial primary key,
3
 metric_desc varchar(100),
4
 metric_level valid_levels,
5
 metric_ts tsmultirange
6
);
`
Now, insert some data into the table. Note that, the insert statement below provides two time ranges that are not contiguous.
hideCopy
`
1
insert into sensor_range
2
 (metric_desc, metric_level, metric_ts)
3
values
4
 (
5
  'Temperature',
6
  'high',
7
  '{[2021-11-01 6:00, 2021-11-01 10:00],[2021-11-05 14:00, 2021-11-05 20:00]}'
8
 );
910
insert into sensor_range
11
 (metric_desc, metric_level, metric_ts)
12
values
13
 (
14
  'Temperature',
15
  'low',
16
  '{[2021-11-01 10:00, 2021-11-01 12:00],[2021-11-05 21:00, 2021-11-05 22:00]}'
17
 );
`
Query the data in the table to see the inserted data rows
hideCopy
`
1
select *
2
from sensor_range;
`
`
1
| `reading_id` | `metric_desc` | `metric_level` | `metric_ts`                                 |
2
|--------------|---------------|----------------|-----------------------------------------------------------------------------|
3
| 1      | Temperature  | high      | {[2021-11-01 6:00, 2021-11-01 10:00],[2021-11-05 14:00, 2021-11-05 20:00]} |
4
| 2      | Temperature  | low      | {[2021-11-01 10:00, 2021-11-01 12:00],[2021-11-05 21:00, 2021-11-05 22:00]} |
`
## Improved performance and monitoring[#](https://supabase.com/blog/whats-new-in-postgres-14#improved-performance-and-monitoring)
### Query pipelining[#](https://supabase.com/blog/whats-new-in-postgres-14#query-pipelining)
If you're a developer accessing PostgreSQL using a high-level programming language, the database driver you're using is likely based on a C library called libpq. For example, suppose your application performs several write operations within a short period, or your network has a higher latency. In that case, you may want to fire off several queries over the same network connection simultaneously, so you don't have to wait for a reply after each query. Under the hood, libpq can send multiple queries to PostgreSQL while maintaining a queue of queries that are waiting for results. This queue consumes additional memory on both the client and server. Developers can now take advantage of PostgreSQL 14's client-side query pipeline mode using clients built on top of the latest libpq library to accelerate app performance.
Aside from query pipelining, the latest PostgreSQL 14 release brings several other enhancements to query parallelism, including improved performance of parallel sequential scans, parallel query execution capabilities for Foreign Data Wrappers, and the ability to run parallel queries when refreshing materialized views. With this, your PostgreSQL server can now do more work for you at a lower cost.
### Monitoring and troubleshooting queries[#](https://supabase.com/blog/whats-new-in-postgres-14#monitoring-and-troubleshooting-queries)
Ask any database troubleshooting expert, and they will tell you that without a way to correlate data across different database components, investigating and monitoring query-related issues can quickly become a nightmare. When it comes to PostgreSQL, the SQL statement’s query_id can be used for this purpose, allowing database experts an easy way to identify workload patterns quickly, detect rogue run-away or slow queries, and common query-related issues. Before PostgreSQL 14, this information was only available using the pg_stat_statements [extension](https://supabase.com/docs/guides/database/extensions), which shows aggregate statistics about queries that have finished executing, but now this information is additionally available for live running queries with pg_stat_activity, in the EXPLAIN VERBOSE statement, and log files. An example of using query_id IN EXPLAIN (VERBOSE) statement
Start by altering the system to enable the query_id
hideCopy
`
1
alter system set compute_query_id = 'on';
`
Restart the PostgreSQL database for the alter system statement to take effect.
Run the following query that selects schema and table names from the catalog tables
hideCopy
`
1
explain (verbose, costs off)
2
select schemaname, tablename
3
from pg_tables, pg_sleep(5)
4
where schemaname <> 'pg_catalog';
`
View the result of the EXPLAIN statement
![View the result of the EXPLAIN statement](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fwhats-new-in-postgres-14%2Fexplain-statement.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Notice that the query identifier is in the output: `Query Identifier: 4856400161806292488`
## Enhanced security[#](https://supabase.com/blog/whats-new-in-postgres-14#enhanced-security)
Security remains top of mind for every organization, and PostgreSQL 14 brings some critical enhancements in this area.
Have you ever wanted to [manage database user access](https://supabase.com/docs/guides/auth/managing-user-data) so that only specific individuals have read-only access? For example, consider a situation where you would like to host some sample data online for a demo and not allow demo users to modify or delete data. With the latest PostgreSQL version 14, you can easily set that up using a single GRANT statement.
hideCopy
`
1
grant pg_read_all_data to bobfries;
`
From an authentication perspective, if you're still managing passwords in the database without [third-party login providers](https://supabase.com/docs/guides/auth#third-party-logins), you may want to read this. Since version 10, PostgreSQL supports several different hashing mechanisms such as MD5 and SCRAM-SHA-256 to store user passwords on disk. However, to keep up with the [latest security weaknesses around MD5](https://en.wikipedia.org/wiki/MD5#Security) and meet regulatory compliance requirements, PostgreSQL 14 has made SCRAM-SHA-256 the default password management mechanism. So, if you are using old PostgreSQL client software, you may want to update it, to be able to connect to the newer versions of the database server.
## It's only the tip of the iceberg[#](https://supabase.com/blog/whats-new-in-postgres-14#its-only-the-tip-of-the-iceberg)
Indeed, there's a lot more to explore in the latest PostgreSQL, and we've barely scratched the surface of what PostgreSQL 14 has to offer. There's no better way to experience some of these features than by trying them out for yourself. You can check out these new features within your Supabase project without having to perform a local installation.
Explore the [Supabase dashboard now](https://supabase.com/dashboard) and get started with your new project.
## More Postgres resources[#](https://supabase.com/blog/whats-new-in-postgres-14#more-postgres-resources)
  * [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
  * [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
  * [Postgres Views](https://supabase.com/blog/postgresql-views)
  * [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
  * [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
  * [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
  * [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-postgres-14&text=New%20in%20PostgreSQL%2014%3A%20What%20every%20developer%20should%20know)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-postgres-14&text=New%20in%20PostgreSQL%2014%3A%20What%20every%20developer%20should%20know)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-postgres-14&t=New%20in%20PostgreSQL%2014%3A%20What%20every%20developer%20should%20know)
[Last postCommunity Day29 November 2021](https://supabase.com/blog/community-day-lw3)
[Next postPostgREST 927 November 2021](https://supabase.com/blog/postgrest-9)
[tech](https://supabase.com/blog/tags/tech)
On this page
  * [Complex data type support](https://supabase.com/blog/whats-new-in-postgres-14#complex-data-type-support)
    * [JSON subscripting](https://supabase.com/blog/whats-new-in-postgres-14#json-subscripting)
    * [Working with disjointed data ranges](https://supabase.com/blog/whats-new-in-postgres-14#working-with-disjointed-data-ranges)
  * [Improved performance and monitoring](https://supabase.com/blog/whats-new-in-postgres-14#improved-performance-and-monitoring)
    * [Query pipelining](https://supabase.com/blog/whats-new-in-postgres-14#query-pipelining)
    * [Monitoring and troubleshooting queries](https://supabase.com/blog/whats-new-in-postgres-14#monitoring-and-troubleshooting-queries)
  * [Enhanced security](https://supabase.com/blog/whats-new-in-postgres-14#enhanced-security)
  * [It's only the tip of the iceberg](https://supabase.com/blog/whats-new-in-postgres-14#its-only-the-tip-of-the-iceberg)
  * [More Postgres resources](https://supabase.com/blog/whats-new-in-postgres-14#more-postgres-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-postgres-14&text=New%20in%20PostgreSQL%2014%3A%20What%20every%20developer%20should%20know)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-postgres-14&text=New%20in%20PostgreSQL%2014%3A%20What%20every%20developer%20should%20know)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-postgres-14&t=New%20in%20PostgreSQL%2014%3A%20What%20every%20developer%20should%20know)
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

