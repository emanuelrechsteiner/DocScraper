---
url: https://supabase.com/blog/range-columns
scraped_at: 2025-05-25T08:43:12.519059
title: Simplifying Time-Based Queries with Range Columns
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
# Simplifying Time-Based Queries with Range Columns
11 Jul 2024
•
6 minute read
[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Tyler ShukertDevRel](https://twitter.com/dshukertjr)
![Simplifying Time-Based Queries with Range Columns](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Frange-columns%2Frange-columns-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Do you prefer audio-visual learning? Watch the video guide!](https://youtu.be/eG_9lZrrbEY?si=MtTQsKZrzMinU536)
When working on applications such as a reservation app or calendar app, you need to store the start time and end time of an event. You may also need to query events occurring in a specific time frame or ensure that certain events do not overlap. If you have a table with two separate columns `start_at` and `end_at` to hold the beginning and end of an event, it might be hard to perform advanced queries or add constraints to prevent overlaps. This article will show how range-type columns could provide helpful query functionalities and advanced constraints to avoid overlapping.
## The Problem with Traditional Date Columns[#](https://supabase.com/blog/range-columns#the-problem-with-traditional-date-columns)
Traditionally, when dealing with events or periods, developers often use two separate columns to represent the start and end of a range. For example:
`
1
create table reservations (
2
 id serial primary key,
3
 title text,
4
 start_at timestamptz,
5
 end_at timestamptz
6
);
`
While this approach works, it has a few drawbacks:
  1. **Querying Complexity** : Writing queries to find overlapping events or events within a specific period becomes complex and error-prone.
  2. **Data Integrity** : Ensuring that reservations do not overlap is difficult.


## Enter Range Types[#](https://supabase.com/blog/range-columns#enter-range-types)
Range types are data types in Postgres that hold the beginning and end of a range of a base type. The range of `int4` is `int4range`, the range of `timestamptz` is `tstzrange`, and the range of `date` is `daterange`. Each range has a start value, an end value, and either square brackets `[]` or parenthesis `()` surrounding them. A bracket means the end is inclusive, and a parenthesis means the end is exclusive. An `int4range` of `[2,5)` represents a range of integers from 2 including it to 5 excluding it, so 2, 3, and 4.
### Querying range columns[#](https://supabase.com/blog/range-columns#querying-range-columns)
Using these range values, we can create a reservation table like the following:
`
1
create table reservations (
2
 id serial primary key,
3
 title text,
4
 duration tstzrange
5
);
`
Using `tstzrange` instead of two `timestamptz` columns have a few advantages. First, it allows us to easily query reservations that overlap with a provided range using the `&&` operator. Look at the following select query:
`
1
select *
2
	from reservations
3
	where duration && '[2024-07-04 16:00, 2024-07-04 19:00)';
`
This query returns rows where the duration overlaps with `[2024-07-04 16:00, 2024-07-04 19:00)`. For example, a row with `[2024-07-04 18:00, 2024-07-04 21:00)` will be returned, but a row with `[2024-07-04 20:00, 2024-07-04 22:00)` will not be returned. The overlaps operator can be used when finding reservations or events in a given period.
Postgres provides more range-specific operators. The official Postgres documentation provides a complete list [of range operators](https://www.postgresql.org/docs/9.3/functions-range.html).
### Adding constraints on range columns[#](https://supabase.com/blog/range-columns#adding-constraints-on-range-columns)
When working on a reservations app, you might want to ensure there are no overlapping reservations. Range columns make it easy to add such constraints. The following SQL statement adds an exclude constraint that prevents new inserts/ updates from overlapping on any of the existing reservations.
`
1
alter table reservations
2
	add constraint exclude_duration exclude
3
	using gist (duration with &&)
`
With the above constraint, the second insert on the following SQL statements fails because the `duration` overlaps with the first insert.
`
1
-- Add a first reservation
2
insert into reservations (title, duration)
3
values ('Tyler Dinner', '[2024-07-04 18:00, 2024-07-04 21:00)');
45
-- The following insert fails because the duration overlaps with the above
6
insert into reservations (title, duration)
7
values ('Thor Dinner', '[2024-07-04 20:00, 2024-07-04 22:00)');
`
Now, the exclusion constraint prevents any reservations from overlapping, but in the real world, a single reservations table typically holds reservations for different restaurants and tables within a restaurant, and just because a single reservation was made at a restaurant, it does not mean the entire restaurant is booked. Postgres can create such constraints where an insert or an update is disallowed only if a specific other column matches and the range overlaps.
Let’s say we had a `table_id` column in our reservations table. This `table_id` could represent a single table in various restaurants this database holds.
`
1
create table reservations (
2
 id serial primary key,
3
 title text,
4
 table_id int4,
5
 duration tstzrange
6
);
`
With a `table_id` column in place, we can add a constraint to ensure that reservations on the same table do not overlap. The constraint requires the [btree_gist](https://www.postgresql.org/docs/current/btree-gist.html) extension.
`
1
-- Enable the btree_gist index required for the constraint.
2
create extension btree_gist
34
-- Add a constraint to prevent overlaps with the same table_id
5
alter table reservations
6
 add constraint exclude_duration
7
 exclude using gist (table_id WITH =, duration WITH &&);
`
With this simple constraint, no two reservations will overlap with each other with the same `table_id`. If we run the following inserts, the second insert will fail because it is trying to book the same table as the first insert while the duration overlaps.
`
1
-- Add a first reservation
2
insert into reservations (title, table_id, duration)
3
values ('Tyler Dinner', 1, '[2024-07-04 18:00, 2024-07-04 21:00)');
45
-- Insert fails, because table 1 is taken from 18:00 - 21:00
6
insert into reservations (title, table_id, duration)
7
values ('Thor Dinner', 1, '[2024-07-04 20:00, 2024-07-04 22:00)');
89
-- Insert succeeds because table 2 is not taken by anyone
10
insert into reservations (title, table_id, duration)
11
values ('Thor Dinner', 2, '[2024-07-04 20:00, 2024-07-04 22:00)');
`
And that is how to create an air-tight table that holds reservations.
## Conclusion[#](https://supabase.com/blog/range-columns#conclusion)
Postgres's range columns offer a solution for handling range data in applications like reservation systems. They simplify queries with specific operators such as `&&` and improve data integrity by enabling constraints to prevent overlaps. Range columns provide an alternative to traditional two-column approaches for representing periods. By leveraging these features, developers can create more sophisticated and reliable applications with less code.
## More Supabase[#](https://supabase.com/blog/range-columns#more-supabase)
  * [Watch the video guide for range columns](https://youtu.be/eG_9lZrrbEY?si=MtTQsKZrzMinU536)
  * [Check constraint video](https://youtu.be/hjrQb029LEE?si=wJ8ztryZP6K6EKmW)
  * [Self-host Maps on Supabase Storage with Protomaps](https://supabase.link/protomaps-storage-yt)
  * [Row Level Security guide](https://supabase.com/docs/guides/database/postgres/row-level-security)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frange-columns&text=Simplifying%20Time-Based%20Queries%20with%20Range%20Columns)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frange-columns&text=Simplifying%20Time-Based%20Queries%20with%20Range%20Columns)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Frange-columns&t=Simplifying%20Time-Based%20Queries%20with%20Range%20Columns)
[Last postSupabase Security Suite11 July 2024](https://supabase.com/blog/hardening-supabase)
[Next postPostgres Realtime location sharing with MapLibre4 July 2024](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre)
[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [The Problem with Traditional Date Columns](https://supabase.com/blog/range-columns#the-problem-with-traditional-date-columns)
  * [Enter Range Types](https://supabase.com/blog/range-columns#enter-range-types)
    * [Querying range columns](https://supabase.com/blog/range-columns#querying-range-columns)
    * [Adding constraints on range columns](https://supabase.com/blog/range-columns#adding-constraints-on-range-columns)
  * [Conclusion](https://supabase.com/blog/range-columns#conclusion)
  * [More Supabase](https://supabase.com/blog/range-columns#more-supabase)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frange-columns&text=Simplifying%20Time-Based%20Queries%20with%20Range%20Columns)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frange-columns&text=Simplifying%20Time-Based%20Queries%20with%20Range%20Columns)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Frange-columns&t=Simplifying%20Time-Based%20Queries%20with%20Range%20Columns)
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

