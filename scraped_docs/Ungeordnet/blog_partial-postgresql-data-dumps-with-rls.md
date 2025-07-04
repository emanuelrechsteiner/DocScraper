---
url: https://supabase.com/blog/partial-postgresql-data-dumps-with-rls
scraped_at: 2025-05-25T08:50:53.084587
title: Partial data dumps using Postgres Row Level Security
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
# Partial data dumps using Postgres Row Level Security
28 Jun 2022
•
6 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Partial data dumps using Postgres Row Level Security](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpartial-dumps%2Fog-partial-dumps-with-rls.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
When working with databases, it's common to create a `seed.sql` file which contains a subset of production data for testing.
During early development, it's fine to dump the entire database and restore it on your development machine. However, once you have production users this becomes a security issue - do you really want to dump your users' data onto your local machines?
There are many ways to solve this, but recently I stumbled upon a neat way to do it using PostgreSQL's Row Level Security (RLS).
The concept is simple:
  1. Create a database user with restricted access.
  2. Define some RLS rules for that user, limiting what data they can access.
  3. Run `pg_dump` as that user.


For this scenario, let's imagine that you have a table called `profiles` in your database:
hideCopy
`
1
create table profiles (
2
 id serial primary key,
3
 name text,
4
 email text
5
);
`
`id`| `name`| `email`  
---|---|---  
`1`| `Employee 1`| `employee1@supabase.com`  
`2`| `Employee 2`| `employee2@supabase.com`  
`3`| `Employee 3`| `employee3@supabase.com`  
`4`| `Jenny`| `jenny@example.com`  
`5`| `Joe`| `joe@example.com`  
In this case, if we ran a `pg_dump` we will save Jenny and Joe's personal data. We don't want that, so let's create a Postgres user called `exporter`, who can only dump the data we want.
### Step 1: Prepare a user[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-1-prepare-a-user)
Create a user to connect to the database. We'll call them `exporter` and grant them access to the public schema:
hideCopy
`
1
-- Create a new user with login privileges
2
create user exporter
3
 with password 'exporter_secure_password';
45
-- Allow this user to select the rows we need
6
grant usage on schema public to exporter;
7
grant select on profiles to exporter;
`
### Step 2: Create data access rules[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-2-create-data-access-rules)
Let's turn on RLS for this table and limit the data which `exporter` can access:
hideCopy
`
1
-- Turn on Row Level Security
2
alter table profiles
3
 enable row level security;
45
-- Only dump data for internal team members 1, 2, 3
6
create policy "Data dump rule" on profiles
7
 for select
8
 to exporter
9
 using (
10
  id in (1, 2, 3)
11
 );
`
### Step 3: Export the data[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-3-export-the-data)
Now we can use `pg_dump` to get only the data that we need.
Run the dump with the `exporter` user that we created above and use the `--enable-row-security` flag to ensure that the dump succeeds.
hideCopy
`
1
# Dump all the data into a "seed.sql" file
2
# which we can use to restore our local databases.
3
pg_dump \
4
-h db.host.supabase.co \
5
-U exporter \
6
-d postgres \
7
-n public \
8
--data-only \
9
--enable-row-security \
10
--table=profiles \
11
> seed.sql
`
hideCopy
`
1
-h db.host.supabase.co \
`
And that's it. You can follow this same pattern for any tables that you want to dump.
## Data access patterns[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#data-access-patterns)
RLS is a bit like appending a “where” clause to a `select`, so you can create all sorts of data access patterns. Let's see a few more which are useful for extracting seed data.
### Using email rules[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#using-email-rules)
Instead of using hardcoded numbers in our RLS policies, we could use email extensions to determine the users who we want to export:
hideCopy
`
1
-- Only dump data for supabase employees
2
create policy "Data dump rule" on profiles
3
 for select
4
 to exporter
5
 using (
6
  substring(email from '@(.*)$') = 'supabase.com'
7
 );
`
### Only recent data[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#only-recent-data)
If we have a table with a lot of data, like an `analytics` table, we might only care about the last 2 months of data.
hideCopy
`
1
-- A fake analytics table where we store actions a user takes
2
create table analytics (
3
 id serial primary key,
4
 ts timestamptz default now(),
5
 profile_id references profiles,
6
 event text
7
);
8
alter table profiles
9
 enable row level security;
1011
-- Here is an "age" rule so that we only dump the most recent analytics
12
create policy "Data dump rule" on logs
13
 for select
14
 to exporter
15
 using (
16
  profile_id in (1, 2, 3) and
17
  ts > now() - interval '2 MONTHS' -- here's the magic
18
 );
`
### Using flags[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#using-flags)
If you don't mind having some additional columns in you database, you can add flags to each row to determine whether it's safe to export.
hideCopy
`
1
create table profiles (
2
 id serial primary key,
3
 name text,
4
 email text,
5
 is_exportable boolean -- make this "TRUE" if you want to allow access
6
);
7
alter table profiles
8
 enable row level security;
910
-- Only dump data for internal team members 1, 2, 3
11
create policy "Data dump rule" on profiles
12
 for select
13
 to exporter
14
 using ( is_exportable = true );
`
## Conclusion[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#conclusion)
Using `seed` data isn't the only way to run development environments. It's also possible to run fully-masked copies of your database using tools like [Snaplet](https://docs.snaplet.dev/tutorials/supabase-clone-environments).
We're also bullish on copy-on-write strategies which allow users to "fork" a database at a point in time, a strategy used by [Database Lab Engine](https://postgres.ai/docs/database-lab). DLE uses the ZFS file system to achieve this, but it's within reach of the Postgres core once alternative storage strategies become easier to implement.
If you want to try out the steps we described in this article, fire up a full PostgreSQL database: [database.new](https://database.new)
## More Postgres resources[#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#more-postgres-resources)
  * [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
  * [Postgres Views](https://supabase.com/blog/postgresql-views)
  * [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
  * [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
  * [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
  * [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&text=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&text=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&t=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)
[Last postVisualizing Supabase Data using Metabase29 June 2022](https://supabase.com/blog/visualizing-supabase-data-using-metabase)
[Next postPython data loading with Supabase17 June 2022](https://supabase.com/blog/loading-data-supabase-python)
[postgresql](https://supabase.com/blog/tags/postgresql)[data](https://supabase.com/blog/tags/data)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [Step 1: Prepare a user](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-1-prepare-a-user)
  * [Step 2: Create data access rules](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-2-create-data-access-rules)
  * [Step 3: Export the data](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-3-export-the-data)


  * [Data access patterns](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#data-access-patterns)
    * [Using email rules](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#using-email-rules)
    * [Only recent data](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#only-recent-data)
    * [Using flags](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#using-flags)
  * [Conclusion](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#conclusion)
  * [More Postgres resources](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#more-postgres-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&text=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&text=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&t=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)
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

