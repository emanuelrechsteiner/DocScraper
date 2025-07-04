---
url: https://supabase.com/blog/postgres-bloat
scraped_at: 2025-05-25T09:08:37.204628
title: Postgres Bloat Minimization
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
# Postgres Bloat Minimization
26 Apr 2024
•
7 minute read
[![Pavel Borisov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F63344111%3Fv%3D4&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Pavel BorisovPostgres Engineer](https://github.com/pashkinelfe)
![Postgres Bloat Minimization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpostgres-bloat.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### How data of Postgres tables stored[#](https://supabase.com/blog/postgres-bloat#how-data-of-postgres-tables-stored)
By default, all table data in Postgres are physically stored using the “heap” method. So every database is a set of 1Gb files (”segments”) and each file is logically split into 8Kb pages. Actual table rows are put into any page with enough free space.
When the row data is updated, a new version of a whole row is constructed and written (to any free space). The old one remains because, at the time of the update, the transaction is not completed and can be rolled back in the future. When the transaction is completed we’ll have two or several versions of the same row in the table. Cleaning old ones is by an asynchronous process called vacuum (and autovacuum).
### How does the vacuum work?[#](https://supabase.com/blog/postgres-bloat#how-does-the-vacuum-work)
Vacuum goes through all table files looking for row versions that were updated or deleted by already completed transactions and frees the space on the pages.
Then it updates the table’s free-space-map to reflect that some page has a certain amount of free space for row inserts.
It also updates the visibility map for a page. It marks that all remaining rows are visible. So index scans can skip visibility checks, which is not so for the modified page before vacuuming. This significantly increases the speed of queries using indexes.
In many cases vacuum runs automatically, cleans everything, and requires little care. But in some scenarios, we need to go deeper and tune the autovacuum parameters or run the vacuum manually.
### Cleaning relation files[#](https://supabase.com/blog/postgres-bloat#cleaning-relation-files)
Vacuum marks space in a relation file as free to use for future row inserts or updates. And it’s not a problem unless we insert many rows, delete many rows at once, and then don’t make any inserts or updates. Space remains reserved in a file but we don’t use it.
In this case, we could free actual filesystem space by running more aggressive mode:
`
1
VACUUM FULL mytable;
`
It will rebuild the table from live rows and they will be placed compactly so that filesystem space will be freed. The downside is that it needs an exclusive lock and you won’t be able to modify the table while `VACUUM FULL` does it's work. It’s wise to execute that process when the database is least accessed e.g. at night.
An alternative way that doesn’t need full locks is using pg_repack extension:
`
1
pg_repack --table mytable test
`
pg_repack operates similarly to VACUUM FULL for database `test` and table `mytable`.
### Table bloating and autovaccuum[#](https://supabase.com/blog/postgres-bloat#table-bloating-and-autovaccuum)
To see database bloat via the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) run:
`
1
$ supabase inspect db bloat
`
or:
`
1
-- number of dead rows
2
SELECT
3
	n_dead_tup
4
FROM
5
	pg_stat_user_tables
6
WHERE
7
	relname = ‘mytable’;
89
-- number of live rows
10
SELECT
11
	count(*)
12
FROM
13
	mytable;
`
If the numbers differ by more than 2x, chances are that the autovacuum didn’t start or hasn’t completed for a table. There could be several legitimate reasons for this.
You can see information for the last successful autovacuum by running:
`
1
$ supabase inspect db vacuum-stats
`
or:
`
1
SELECT
2
	last_vacuum,
3
	last_autovacuum
4
FROM
5
	pg_stat_user_tables
6
WHERE
7
	relname = ‘mytable’;
`
Let’s turn on autovacuum logging so that all autovacuum events land in the log:
`
1
ALTER TABLE mytable SET log_autovacuum_min_duration to 0;
`
There are two ways we can encounter this situation:
  * autovacuum hasn’t started
  * autovacuum did start, (possibly multiple times) but never succeeded


### Autovacuum hasn’t started for a table[#](https://supabase.com/blog/postgres-bloat#autovacuum-hasnt-started-for-a-table)
Autovacuum starts based on several configuration parameters like timeout and pattern of access to a particular table. Maybe it’s even legitimate that it hasn’t started.
  * `autovacuum_vacuum_threshold` - number of rows updated or deleted in a table to invoke autovacuum
  * `autovacuum_vacuum_insert_threshold` - number of rows inserted into a table to invoke autovacuum
  * `autovacuum_vacuum_scale_factor` - a fraction of table modified by updates or deletes to invoke autovacuum
  * `autovacuum_vacuum_insert_scale_factor` - a fraction of table modified by inserts to invoke autovacuum


With all these parameters set, the autovacuum will start if the number of rows updated or deleted exceeds:
`
1
autovacuum_vacuum_scale_factor * size_of_table + autovacuum_vacuum_threshold
`
The same logic applies for inserts. Default scale factors are 20% of a table, which could be too high for big tables. If we want autovacuum to occur on large tables more frequently and take less time each run, decrease the default values for these tables e.g.:
`
1
ALTER TABLE mytable SET autovacuum_vacuum_scale_factor to 0.05;
`
  * `autovacuum_naptime` (default 1 min) - Each 1-minute autovacuum daemon will see the state of all tables in the database and decide whether to start autovacuum for a table. Most often this parameter does not need to be modified.


To see global vacuum settings for your cluster let’s run:
`
1
SELECT * from pg_settings where category like 'Autovacuum';
`
To see current settings for a table (that overrides global settings) run:
`
1
SELECT relname, reloptions FROM pg_class WHERE relname='mytable';
`
### Autovacuum started but couldn’t succeed[#](https://supabase.com/blog/postgres-bloat#autovacuum-started-but-couldnt-succeed)
The most common reason autovacuum doesn’t succeed is long-running open transactions that access old row versions. In that case, Postgres recognizes that the row versions are still needed so any row versions created after that point can’t be marked as dead. One common cause for this problem is interactive sessions that were left open on accident. When tuples can’t be marked as dead, the database begins to bloat.
To see all open transactions run:
`
1
SELECT xact_start, state FROM pg_stat_activity;
`
To close transactions found to be idling:
`
1
SELECT pg_cancel_backend(pid) FROM pg_stat_activity WHERE xact_start = '<value from previous query>';
`
For automatically closing idle transactions in a session:
`
1
SET idle_in_transaction_session_timeout TO '10000s';
`
The same parameter could be set per role or database as needed.
Another, less likely, possibility is that autovacuum can’t succeed due to locks. If some of your processes take the `SHARE UPDATE EXCLUSIVE` lock e.g. `ALTER TABLE` clause, this lock will prevent vacuum from processing a table. Lock conflicts in your ordinary transactions could cause `SHARE UPDATE EXCLUSIVE` to be taken for a long time. A good recipe when this happens is to cancel all the open transactions and run VACUUM for a table manually (or wait until the next autovacuum comes for it).
`
1
SELECT pg_cancel_backend(pid) FROM pg_stat_activity WHERE state = 'active';
2
VACUUM mytable;
`
### Other vacuum optimizations[#](https://supabase.com/blog/postgres-bloat#other-vacuum-optimizations)
There could be too few autovacuum workers or each worker could operate slowly due to the low setting of `autovacuum_work_mem`.
  * `autovacuum_max_workers` (default 3) - Number of parallel workers doing autovacuum for tables. When you have enough cores, increasing the default value is worthwhile. Note that this will decrease the number of possible backends or regular parallel workers running at a time.
  * `autovacuum_work_mem` (default equal to `maintenance_work_mem` or 64Mb) - work memory that is used per autovacuum worker. If you see in your logs that autovacuum for some tables starts but takes a long time, that time may be decreased by increasing this value. This parameter can only be modified in the config file.


### Conclusion[#](https://supabase.com/blog/postgres-bloat#conclusion)
Vacuum and autovacuum are efficient ways to maintain the tables without bloat. They have several parameters that allow efficient tuning. Some insight into what database does can help prevent the cases where autovacuum becomes problematic and bloat increases i.e.:
  * Long open transactions
  * Stuck locks
  * Insufficient resources allocated to vacuuming
  * Space not freed on a filesystem level after massive table modifications


For more information about bloat and vacuuming, here are some direct references to resources:
[Full official documentation for vacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-BASICS)
[Per-table vacuum parameters](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS)
[Global autovacuum parameters (most of them need modifying postgresql.conf, but could be overridden by per-table parameters)](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html)
[Supabase CLI reference](https://supabase.com/docs/reference/cli/global-flags)
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-bloat&text=Postgres%20Bloat%20Minimization)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-bloat&text=Postgres%20Bloat%20Minimization)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-bloat&t=Postgres%20Bloat%20Minimization)
[Last postOpen Source Hackathon 2024 winners30 April 2024](https://supabase.com/blog/supabase-oss-hackathon-winners)
[Next postExploring Support Tooling at Supabase: A Dive into SLA Buddy25 April 2024](https://supabase.com/blog/exploring-support-tooling)
[supabase-engineering](https://supabase.com/blog/tags/supabase-engineering)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [How data of Postgres tables stored](https://supabase.com/blog/postgres-bloat#how-data-of-postgres-tables-stored)
  * [How does the vacuum work?](https://supabase.com/blog/postgres-bloat#how-does-the-vacuum-work)
  * [Cleaning relation files](https://supabase.com/blog/postgres-bloat#cleaning-relation-files)
  * [Table bloating and autovaccuum](https://supabase.com/blog/postgres-bloat#table-bloating-and-autovaccuum)
  * [Autovacuum hasn’t started for a table](https://supabase.com/blog/postgres-bloat#autovacuum-hasnt-started-for-a-table)
  * [Autovacuum started but couldn’t succeed](https://supabase.com/blog/postgres-bloat#autovacuum-started-but-couldnt-succeed)
  * [Other vacuum optimizations](https://supabase.com/blog/postgres-bloat#other-vacuum-optimizations)
  * [Conclusion](https://supabase.com/blog/postgres-bloat#conclusion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-bloat&text=Postgres%20Bloat%20Minimization)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-bloat&text=Postgres%20Bloat%20Minimization)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-bloat&t=Postgres%20Bloat%20Minimization)
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

