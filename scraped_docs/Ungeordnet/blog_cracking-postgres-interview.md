---
url: https://supabase.com/blog/cracking-postgres-interview
scraped_at: 2025-05-25T08:56:47.274432
title: Cracking PostgreSQL Interview Questions
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
# Cracking PostgreSQL Interview Questions
27 Feb 2021
•
7 minute read
[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Ant WilsonCTO and Co-Founder](https://github.com/awalias)
![Cracking PostgreSQL Interview Questions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Felephants.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
There are plenty of resources out there for preparing for PostgreSQL interview questions. Most posts are for technical interviews with a focus on PostgreSQL, however many just cover the basics and the advanced resources often conflate transactional SQL with analytical SQL (WINDOW/RANK functions, aggregates etc.).
Here, we're going to focus on PostgreSQL interview questions that are aimed to understand the transactional side of PostgreSQL, and offer some areas that you may want to go a little deeper on in order to really impress your interviewer (and more importantly, become a kick-ass software engineer).
## 1. Modeling[#](https://supabase.com/blog/cracking-postgres-interview#1-modeling)
### Know how to model 1-M, M-M, 1-1 relationships. And know how to use foreign keys.[#](https://supabase.com/blog/cracking-postgres-interview#know-how-to-model-1-m-m-m-1-1-relationships-and-know-how-to-use-foreign-keys)
A review of [database normalization](https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-264j-database-internet-and-systems-integration-technologies-fall-2013/lecture-notes-exercises/MIT1_264JF13_lect_10.pdf) is a great place to start when thinking about how to correctly model relationships. However if you don't have the time to read through lecture notes, head over to [DBDesigner](https://app.dbdesigner.net/designer/schema/guest_template) and inspect their example schema. The table StudentCourses is a great example of how to model a Many-to-Many relationship, by using a join table. (side note: you can export these visual schemas to SQL using Ctrl+E). Modelling your data correctly is arguably the most important part of any software project, writing applications becomes a breeze if you can get the data layer right.
### Know how to use pg rich type system: [arrays](https://www.postgresql.org/docs/current/arrays.html), [domains](https://www.postgresql.org/docs/current/domains.html), [JSONB](https://www.postgresql.org/docs/13/datatype-json.html), [timestamptz](https://www.postgresql.org/docs/current/functions-datetime.html), [enums](https://www.postgresql.org/docs/13/datatype-enum.html)[#](https://supabase.com/blog/cracking-postgres-interview#know-how-to-use-pg-rich-type-system-arrays-domains-jsonb-timestamptz-enums)
Postgres has tons of useful types beyond the basics, knowing how to use them will show you can leverage the true power of Postgres. JSONB for example can be incredibly useful for storing non-structured data, which you can query using syntax like:
`
1
-- grades = {'geography': 'A', 'history': 'B', 'postgres': 'A++'}
2
select * from students where grades->>'geography' = 'A';
`
### Know about namespacing with SCHEMAs[#](https://supabase.com/blog/cracking-postgres-interview#know-about-namespacing-with-schemas)
In Supabase for example we keep system schemas such as `extensions` and `auth` in separate schemas so that we don't pollute the default `public` schema.
## 2. INDEXes[#](https://supabase.com/blog/cracking-postgres-interview#2-indexes)
### Know how speed up queries with indexes.[#](https://supabase.com/blog/cracking-postgres-interview#know-how-speed-up-queries-with-indexes)
The art of indexing in Postgres could fill an entire book. In some circumstances it can happen that a bad index is worse for performance than no index, so it's worth spending a little time to learn some of the common strategies.
An index can be simple, for example, if your students table is most frequently queried on surname alone, you create an index:
`
1
create index idx_students_surname on students (surname);
`
The default index type used here is `btree` (you could have specified this as `USING btree`), but there are other types of indexes, such as `BRIN`, `GiST`, `GIN`, `hash`, and more. Readers wanting to go deeper may also want to explore [Partial](https://www.postgresql.org/docs/current/indexes-partial.html) or [Multicolumn](https://www.postgresql.org/docs/13/indexes-multicolumn.html) Indexes.
### Know how to analyze with EXPLAIN ANALYZE[#](https://supabase.com/blog/cracking-postgres-interview#know-how-to-analyze-with-explain-analyze)
Running
`
1
EXPLAIN (ANALYZE) SELECT *
2
FROM students
3
WHERE surname = 'Krobb';
`
Before and after adding your index will show you the difference in approach the query planner took to finding your data. Note that using EXPLAIN alone will give us estimated plan costs. When used together with ANALYZE like: `EXPLAIN (ANALYZE)` you will receive both estimated and actual costs.
## 3. VIEWs[#](https://supabase.com/blog/cracking-postgres-interview#3-views)
### Know how to create different representations of data with [VIEWs](https://supabase.com/blog/postgresql-views).[#](https://supabase.com/blog/cracking-postgres-interview#know-how-to-create-different-representations-of-data-with-views)
We might create a VIEW `transcripts` which pulls out data from `students`, `courses`, and `grades`. It's useful for security, and logical abstractions. Check out our longer post on VIEWs here: [/blog/postgresql-views](https://supabase.com/blog/postgresql-views). Some purists may argue that you should always query VIEWs and never TABLEs.
### Know about Autoupdatable views.[#](https://supabase.com/blog/cracking-postgres-interview#know-about-autoupdatable-views)
If a VIEW is named as the target relation in an INSERT, UPDATE, or DELETE and only SELECTs from a single base relation, then the underlying subquery is automatically rewritten to update the underlying base relation instead.
### Limitations on VIEWs[#](https://supabase.com/blog/cracking-postgres-interview#limitations-on-views)
One example of a limitation is when a VIEW is not Autoupdatable. This happens when the VIEW does not SELECT from a single base relation. If the user does not specify an INSTEAD OF trigger that upgrades the underlying query, then an error will be thrown, since the executor cannot update a view as such.
## 4. ROLEs[#](https://supabase.com/blog/cracking-postgres-interview#4-roles)
### Know how to secure their database. Permissions at the table, column, row level.[#](https://supabase.com/blog/cracking-postgres-interview#know-how-to-secure-their-database-permissions-at-the-table-column-row-level)
All databases have different user types, your client for example doesn't usually need the ability to create and drop schemas, but your DB admin does. You should play around with [creating roles](https://www.postgresql.org/docs/current/database-roles.html), and [granting](https://www.postgresql.org/docs/current/role-membership.html) various permissions.
### Know about [ROLEs](https://www.postgresql.org/docs/13/sql-createrole.html), application ROLEs, the PUBLIC role, and [GRANTs](https://www.postgresql.org/docs/current/sql-grant.html)[#](https://supabase.com/blog/cracking-postgres-interview#know-about-roles-application-roles-the-public-role-and-grants)
In Postgres, the special “role” name PUBLIC can be used to grant a privilege to every role on the system. For example, if you want to grant insert access to all users on table students:
`
1
GRANT INSERT ON students TO PUBLIC;
`
### Know how to do RLS - Policies[#](https://supabase.com/blog/cracking-postgres-interview#know-how-to-do-rls---policies)
We use Row Level Security in Supabase as a way to grant/restrict access on a row level basis. For example if you're writing a Discord clone, perhaps only a given user should be able to write their own messages:
`
1
CREATE POLICY "Individuals can only write their own messages." ON messages FOR
2
  INSERT WITH CHECK ((select auth.uid()) = user_id);
34
-- auth.uid() is a function provided by Supabase which plucks the uid out
5
--  of the JWT sent along with an API request more on this here:
6
--  https://www.youtube.com/watch?v=0LvCOlELs5U
`
## 5. FUNCTIONs[#](https://supabase.com/blog/cracking-postgres-interview#5-functions)
### Know how to do business logic on SQL/[PLPGSQL](https://www.postgresql.org/docs/current/plpgsql-overview.html#PLPGSQL-ADVANTAGES)[#](https://supabase.com/blog/cracking-postgres-interview#know-how-to-do-business-logic-on-sqlplpgsql)
PL/pgSQL is a procedural programming language that can be used to write functions inside of your database. It can be useful for making [remote procedure calls](https://supabase.com/docs/reference/javascript/rpc) from an API. You can go as deep as you want here, since it's an entire programming language, but understanding the basics will really go a long way, and give you super powers when working with your data.
You can use FUNCTIONs in combination with TRIGGERs to do cool stuff like have auto-updating `updated_at` columns on your data:
`
1
-- a function that sets the updated_at value to now()
2
CREATE FUNCTION set_updated_at()
3
RETURNS TRIGGER AS $$
4
BEGIN
5
 new.updated_at = now();
6
 RETURN NEW;
7
END;
8
$$ LANGUAGE plpgsql;
910
-- a trigger that fires when students table is updated
11
CREATE TRIGGER handle_updated_at
12
 BEFORE UPDATE ON students
13
 FOR EACH ROW
14
 EXECUTE PROCEDURE set_updated_at();
`
### Thinks in SETs when doing logic[#](https://supabase.com/blog/cracking-postgres-interview#thinks-in-sets-when-doing-logic)
Whilst PL/pgSQL does have [loops](https://www.postgresql.org/docs/current/plpgsql-control-structures.html#PLPGSQL-CONTROL-STRUCTURES-LOOPS) and [cursors](https://www.postgresql.org/docs/current/plpgsql-cursors.html), there is usually a faster and more legible pure SQL based solution available using JOIN/UNION etc. So it's important to become well acquainted with thinking in these terms.
### Know how to use [CTEs](https://www.postgresqltutorial.com/postgresql-cte/)[#](https://supabase.com/blog/cracking-postgres-interview#know-how-to-use-ctes)
Common table expressions are temporary or intermediate result sets. They can make your queries more readable and even enable recursion. The typical form is:
`
1
with ten_strumpers as (
2
 select id, first_name
3
 from students
4
 where surname = 'Strumper'
5
 order by first_name
6
 limit 10
7
)
8
select id
9
from ten_strumpers
10
where first_name like "S%";
`
If you can reason about most of the topics in this post then you'll be in a very strong position to impress with your answers to PostgreSQL interview questions. As with all programming topics however, the real learning starts when you put these things into practice. At Supabase we offer a very very fast (the fastest?) way to spin up a PostgreSQL database and start querying it, and our browser based SQL editor is getting more powerful every day.
[Get started on Supabase for free here](https://supabase.com/dashboard)
Thanks Steve Chavez for providing all the good bits of this post :)
## More Postgres resources[#](https://supabase.com/blog/cracking-postgres-interview#more-postgres-resources)
  * [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
  * [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
  * [Postgres Views](https://supabase.com/blog/postgresql-views)
  * [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
  * [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
  * [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcracking-postgres-interview&text=Cracking%20PostgreSQL%20Interview%20Questions)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcracking-postgres-interview&text=Cracking%20PostgreSQL%20Interview%20Questions)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcracking-postgres-interview&t=Cracking%20PostgreSQL%20Interview%20Questions)
[Last postSupabase Beta February 20212 March 2021](https://supabase.com/blog/supabase-beta-february-2021)
[Next postRoboflow.com choose Supabase to power Paint.wtf leaderboard9 February 2021](https://supabase.com/blog/case-study-roboflow)
[sql](https://supabase.com/blog/tags/sql)[postgres](https://supabase.com/blog/tags/postgres)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [1. Modeling](https://supabase.com/blog/cracking-postgres-interview#1-modeling)
  * [2. INDEXes](https://supabase.com/blog/cracking-postgres-interview#2-indexes)
  * [3. VIEWs](https://supabase.com/blog/cracking-postgres-interview#3-views)
  * [4. ROLEs](https://supabase.com/blog/cracking-postgres-interview#4-roles)
  * [5. FUNCTIONs](https://supabase.com/blog/cracking-postgres-interview#5-functions)
  * [More Postgres resources](https://supabase.com/blog/cracking-postgres-interview#more-postgres-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcracking-postgres-interview&text=Cracking%20PostgreSQL%20Interview%20Questions)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcracking-postgres-interview&text=Cracking%20PostgreSQL%20Interview%20Questions)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcracking-postgres-interview&t=Cracking%20PostgreSQL%20Interview%20Questions)
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

