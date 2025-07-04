---
url: https://supabase.com/blog/postgresql-views
scraped_at: 2025-05-25T08:42:49.517352
title: Postgres Views
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
# Postgres Views
18 Nov 2020
•
7 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
A quick summary of Postgres views, materialized views, and why you should use them.
### What is a View?[#](https://supabase.com/blog/postgresql-views#what-is-a-view)
A [view](https://www.postgresql.org/docs/12/sql-createview.html) is a convenient shortcut to a query. Creating a view does not involve new tables or data. When run, an underlying query is executed, returning its results to the user.
#### Basic Example[#](https://supabase.com/blog/postgresql-views#basic-example)
Say we have the following tables from a database of a university:
**students**
id| name| type  
---|---|---  
1| Arun| undergraduate  
2| Zack| graduate  
3| Joy| graduate  
**courses**
id| title| code  
---|---|---  
1| Introduction to Postgres| PG101  
2| Authentication Theories| AUTH205  
3| Fundamentals of Supabase| SUP412  
**grades**
id| student_id| course_id| result  
---|---|---|---  
1| 1| 1| B+  
2| 1| 3| A+  
3| 2| 2| A  
4| 3| 1| A-  
5| 3| 2| A  
6| 3| 3| B-  
Creating a view consisting of all the three tables will look like this:
`
1
create view transcripts as
2
 select
3
  students.name,
4
  students.type,
5
  courses.title,
6
  courses.code,
7
  grades.result
8
 from
9
  grades
10
  left join students on grades.student_id = students.id
11
  left join courses on grades.course_id = courses.id;
`
Once done, we can now access the underlying query with:
`
1
select * from transcripts;
`
For additional parameters or options, refer [here](https://www.postgresql.org/docs/12/sql-createview.html#:~:text=parameters).
### Why should we use Views?[#](https://supabase.com/blog/postgresql-views#why-should-we-use-views)
Views provide the several benefits:
  * Simplicity
  * Consistency
  * Logical Organization
  * Security


#### Simplicity[#](https://supabase.com/blog/postgresql-views#simplicity)
As a query becomes complex it becomes a hassle to call it. Especially when we run it at regularly. In the example above, instead of repeatedly running:
`
1
select
2
 students.name,
3
 students.type,
4
 courses.title,
5
 courses.code,
6
 grades.result
7
from
8
 grades
9
 left join students on grades.student_id = students.id
10
 left join courses on grades.course_id = courses.id;
`
We can run this instead:
`
1
select * from transcripts;
`
Additionally, a view behaves like a typical table. We can safely use it in table `JOIN`s or even create new views using existing views.
#### Consistency[#](https://supabase.com/blog/postgresql-views#consistency)
Views ensure that the likelihood of mistakes decreases when repeatedly executing a query. In our example above, we may decide that we want to exclude the course _Introduction to Postgres_. The query would become:
`
1
select
2
 students.name,
3
 students.type,
4
 courses.title,
5
 courses.code,
6
 grades.result
7
from
8
 grades
9
 left join students on grades.student_id = students.id
10
 left join courses on grades.course_id = courses.id
11
where courses.code != 'PG101';
`
Without a view, we would need to go into every dependent query to add the new rule. This would increase in the likelihood of errors and inconsistencies, as well as introducing a lot of effort for a developer. With views, we can alter just the underlying query in the view **transcripts**. The change will be applied to all applications using this view.
#### Logical Organization[#](https://supabase.com/blog/postgresql-views#logical-organization)
With views, we can give our query a name. This is extremely useful for teams working with the same database. Instead of guessing what a query is supposed to do, a well-named view can easily explain it. For example, by looking at the name of the view **transcripts** , we can infer that the underlying query might involve the **students** , **courses** , and **grades** tables.
#### Security[#](https://supabase.com/blog/postgresql-views#security)
Views can restrict the amount and type of data presented to a user. Instead of allowing a user direct access to a set of tables, we provide them a view instead. We can prevent them from reading sensitive columns by excluding them from the underlying query.
### What is a Materialized View?[#](https://supabase.com/blog/postgresql-views#what-is-a-materialized-view)
A [materialized view](https://www.postgresql.org/docs/12/rules-materializedviews.html) is a form of view but with the added feature of physically storing the results. In subsequent reads of a materialized view, the time taken to return its results would be much faster than a conventional view. This is because the data is readily available for a materialized view while the conventional view executes the underlying query each time it is called.
#### Basic Example[#](https://supabase.com/blog/postgresql-views#basic-example-1)
Using our example above, a materialized view can be created like this:
`
1
create materialized view transcripts as
2
 select
3
  students.name,
4
  students.type,
5
  courses.title,
6
  courses.code,
7
  grades.result
8
 from
9
  grades
10
  left join students on grades.student_id = students.id
11
  left join courses on grades.course_id = courses.id;
`
Reading from the materialized view is the same as a conventional view:
`
1
select * from transcripts;
`
For additional parameters or options, refer [here](https://www.postgresql.org/docs/12/sql-creatematerializedview.html#:~:text=parameters).
#### Refreshing[#](https://supabase.com/blog/postgresql-views#refreshing)
Unfortunately, there is a trade-off - data in materialized views are not always up to date. We need to refresh it regularly to prevent the data from becoming too stale. To do so:
`
1
refresh materialized view transcripts;
`
It's up to you how regularly refresh your materialized views, and it's probably different for each view depending on its use-case.
### Materialized views vs Conventional views[#](https://supabase.com/blog/postgresql-views#materialized-views-vs-conventional-views)
Materialized views are useful when execution times for queries or views become unbearable or exceed the service level agreements of a business. These could likely occur in views or queries involving multiple tables and millions of rows. When using such a view, however, there should be tolerance towards data being outdated. Some use-cases for materialized views are internal dashboards and analytics.
Creating a materialized view is not a solution to inefficient queries. You should always seek to optimize a slow running query even if you are implementing a materialized view.
### Conclusion[#](https://supabase.com/blog/postgresql-views#conclusion)
Postgres views and materialized views are a great way to organize and view results from commonly used queries. Although similar to one another, each has its purpose. Views simplify the process of running queries. Materialized views are usually faster at returning results, with the trade-off of having stale data.
## More Postgres resources[#](https://supabase.com/blog/postgresql-views#more-postgres-resources)
  * [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
  * [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
  * [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
  * [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
  * [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
  * [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-views&text=Postgres%20Views)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-views&text=Postgres%20Views)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-views&t=Postgres%20Views)
[Last postSupabase Alpha November 20201 December 2020](https://supabase.com/blog/supabase-alpha-november-2020)
[Next postSupabase Alpha October 20202 November 2020](https://supabase.com/blog/supabase-alpha-october-2020)
[postgres](https://supabase.com/blog/tags/postgres)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [More Postgres resources](https://supabase.com/blog/postgresql-views#more-postgres-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-views&text=Postgres%20Views)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-views&text=Postgres%20Views)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-views&t=Postgres%20Views)
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

