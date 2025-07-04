---
url: https://supabase.com/blog/postgresql-templates
scraped_at: 2025-05-25T08:53:15.619311
title: What are PostgreSQL Templates?
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
# What are PostgreSQL Templates?
09 Jul 2020
•
4 minute read
[![Angelico de los Reyes avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdragarcia.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Angelico de los ReyesEngineering](https://github.com/dragarcia)
Whenever you create a new database in Postgres, you are actually [basing it off an already present database](https://www.postgresql.org/docs/current/manage-ag-templatedbs.html) in your cluster.
This database, `template1`, and another, called `template0`, are standard system databases that exist in every newly created database cluster. Don't believe me? Why not quickly [spin up a database](https://supabase.com/docs/postgres/server/about) and see it for yourself with this query:
`
1
select * from pg_database;
`
In this post, we'll explore these template databases and see how we can make full use of their potential. We'll even look into creating a template database of our own.
## template1[#](https://supabase.com/blog/postgresql-templates#template1)
By default, running:
`
1
CREATE DATABASE new_db_name;
`
simply copies everything from the database `template1`. We can modify this template database in any way: add a table, insert some data, create new extensions, or install procedural languages. Any of these actions would be propagated to subsequently created databases.
This, however, is **not** advisable. Removing any one of these modifications would need you to manually uninstall or drop these changes from `template1`. You do have the option to drop and recreate the entire `template1` database altogether. This unfortunately comes at the risk of committing a mistake along the way, effectively breaking `CREATE DATABASE`. It would be better to leave `template1` alone and create a template database of your own.
## Custom Template Databases[#](https://supabase.com/blog/postgresql-templates#custom-template-databases)
To set an existing database as a template database:
`
1
ALTER DATABASE template_db_name WITH is_template TRUE;
`
Doing this allows any user or role with the `CREATEDB` privilege to utilize it as a template. If not, only superusers or owners of the database would be allowed to do so.
To create a new database with this template:
`
1
CREATE DATABASE new_db_name TEMPLATE template_db_name;
`
### Advantages[#](https://supabase.com/blog/postgresql-templates#advantages)
  * With this, you can now have customized templates without the need to worry about polluting `template1`.
  * You can safely drop the entire custom template database without the risk of breaking `CREATE DATABASE`.
  * If you wish, you can create multiple template databases for various use cases.


### Limitations[#](https://supabase.com/blog/postgresql-templates#limitations)
  * To properly create a database from a custom template database, there should be no other connections present. `CREATE DATABASE` immediately fails if any connections exist at the start of the query.
  * As such, if you are looking to replicate a database while maintaining your connections (eg. a production database), it would be more ideal to use the Postgres utility [pg_dump](https://www.postgresql.org/docs/12/app-pgdump.html).


## template0[#](https://supabase.com/blog/postgresql-templates#template0)
`template0` contains the same data as `template1`. We could think of this template database as a fallback if anything irreversible happens to `template1`. As such, this template database should never be modified in any way as soon as the database cluster has been initialized. To create a database with `template0` as the template database:
`
1
CREATE DATABASE new_db_name TEMPLATE template0;
`
### Applications[#](https://supabase.com/blog/postgresql-templates#applications)
  * If anything goes wrong with `template1`, It can be dropped and recreated with `template0` as the template database.
  * We can also create a clean database that does not contain any modifications present in `template1`. This would be useful when restoring from pg_dump. Any conflicts brought about by modifications not present in the dump are eliminated.
  * `template0` can be used to specify new encodings. As pointed out in this [article](https://hashrocket.com/blog/posts/exploring-the-default-postgres-template-databases#:~:text=we%20can't%20edit%20the%20locale%20or%20encoding%20of%20a%20database%20copied%20from%20template1), creating a new database with `template1` and new encodings would result in an error.


`
1
-- Will succeed
2
CREATE DATABASE new_db_name TEMPLATE template0 ENCODING 'SQL_ASCII';
34
-- Will return an error
5
CREATE DATABASE new_db_name ENCODING 'SQL_ASCII';
`
## Conclusion[#](https://supabase.com/blog/postgresql-templates#conclusion)
To quickly sum things up, we found out that new databases are, by default, created from a template database called `template1`. `template1` can be modified in any way we please and the changes would be present in any database created afterward. We can also create custom template databases and base new databases from them instead. If things go awry, `template0` is always there to help.
## More Postgres resources[#](https://supabase.com/blog/postgresql-templates#more-postgres-resources)
  * [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
  * [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
  * [Postgres Views](https://supabase.com/blog/postgresql-views)
  * [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
  * [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
  * [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-templates&text=What%20are%20PostgreSQL%20Templates%3F)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-templates&text=What%20are%20PostgreSQL%20Templates%3F)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-templates&t=What%20are%20PostgreSQL%20Templates%3F)
[Last postAlpha Launch Postmortem10 July 2020](https://supabase.com/blog/alpha-launch-postmortem)
[Next postPhysical vs Logical Backups in PostgreSQL7 July 2020](https://supabase.com/blog/postgresql-physical-logical-backups)
[postgres](https://supabase.com/blog/tags/postgres)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [template1](https://supabase.com/blog/postgresql-templates#template1)
  * [Custom Template Databases](https://supabase.com/blog/postgresql-templates#custom-template-databases)
  * [template0](https://supabase.com/blog/postgresql-templates#template0)
  * [Conclusion](https://supabase.com/blog/postgresql-templates#conclusion)
  * [More Postgres resources](https://supabase.com/blog/postgresql-templates#more-postgres-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-templates&text=What%20are%20PostgreSQL%20Templates%3F)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-templates&text=What%20are%20PostgreSQL%20Templates%3F)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-templates&t=What%20are%20PostgreSQL%20Templates%3F)
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

