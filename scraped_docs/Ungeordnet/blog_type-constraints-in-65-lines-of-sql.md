---
url: https://supabase.com/blog/type-constraints-in-65-lines-of-sql
scraped_at: 2025-05-25T09:21:12.283623
title: Type Constraints in 65 lines of SQL
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
# Type Constraints in 65 lines of SQL
17 Feb 2023
•
10 minute read
[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Oliver RiceEngineering](https://github.com/olirice)
![Type Constraints in 65 lines of SQL](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-jan%2Fsemver-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
PostgreSQL has a rich and extensible type system. Beyond [enums](https://www.postgresql.org/docs/current/datatype-enum.html) and [composite](https://www.postgresql.org/docs/current/rowtypes.html) types, we can:
  * apply data validation rules
  * override comparison operators like `=` / `+` / `-`
  * create custom aggregations
  * define casting rules between types


With a little effort, a user-defined type can feel indistinguishable from a built-in. In this article we focus on validation and ergonomics while quickly touching on a few other concepts.
To illustrate, we’ll create an `semver` data type to represent [Semantic Versioning](https://semver.org) values. We’ll then add validation rules to make invalid states unrepresentable.
## SemVer[#](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#semver)
A (very) loose primer on SemVer:
SemVer is a specification for representing software versions that communicate information about backwards compatibility. The type is typically represented as a string with 5 components.
![image](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-jan%2Fsemver-spec.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Where `pre-release` and `metadata` are optional.
The intent of each component is outside the scope of this article but, as an example, incrementing the major version number notifies users that the release includes at least one backwards incompatible change.
For a concise representation of the full spec, [check out the grammar](https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions).
## SQL[#](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#sql)
For our purposes, we’ll assume that the SemVer type is a critical component of the application that needs to be queried flexibly and efficiently.
### Storing Components[#](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#storing-components)
To that end, we’ll store each component of the version as a separate field on a [composite type](https://www.postgresql.org/docs/current/rowtypes.html).
`
1
create type semver_components as (
2
  major int,
3
  minor int,
4
  patch int,
5
  pre_release text[],
6
  build_metadata text[]
7
);
`
We can create an instance of this type in SQL by casting a tuple as the `semver_components` type.
`
1
select
2
  (1, 2, 3, array['beta', '1'], array['meta'])::semver_components
3
-- returns: (1,2,3,{'beta','1'},{'meta'})
`
Unfortunately, our definition is far too permissive.
`
1
select
2
  (null, -500, null, array['?'], array[''])::semver_components
3
-- returns: (,-500,,{'?'},{''
`
Our data type has no problem accepting invalid components. To list a few of the SemVer rules we violated:
  * Major version must not be null
  * Minor version must be ≥ 0
  * Patch version must not be null
  * Pre-release elements must only include characters [A-z0-9]
  * Build metadata elements may not be empty strings


We need to add some validation rules to meet our “make invalid states unrepresentable” goal.
### Validation[#](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#validation)
[Domains](https://www.postgresql.org/docs/current/sql-createdomain.html) are Postgres’ solution for optionally layering constraints over a data type. Domains are to types what [check constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) are to tables. If you’re not familiar with check constraints, you can think of them as equivalent to zod/pydantic in javascript/python.
Let's codify some SemVer rules, layer them on the `semver_components` type, and give the new domain a friendly name.
`
1
create domain semver
2
  as semver_components
3
  check (
4
    -- major: non-null positive integer
5
    (value).major is not null and (value).major >= 0
6
    -- minor: non-null positive integer
7
    and (value).minor is not null and (value).minor >= 0
8
    -- patch: non-null positive integer
9
    and (value).patch is not null and (value).patch >= 0
10
    and semver_elements_match_regex(
11
      (value).pre_release,
12
      '^[A-z0-9]{1,255}$'
13
    )
14
    and semver_elements_match_regex(
15
      (value).build_metadata,
16
      '^[A-z0-9\.]{1,255}$'
17
    )
18
  );
`
which references a helper function:
`
1
create or replace function semver_elements_match_regex(
2
  parts text[],
3
  regex text
4
)
5
returns bool
6
language sql
7
as $$
8
  -- validates that *parts* nullable array of non-empty strings
9
  -- where each element of *parts* matches *regex*
10
  select
11
    $1 is null
12
    or (
13
      (
14
        select (
15
          bool_and(pr_arr.elem is not null)
16
          and bool_and(pr_arr.elem ~ $2)
17
        )
18
        from
19
          unnest($1) pr_arr(elem)
20
      )
21
      and array_length($1, 1) > 0
22
    )
23
$$;
`
Now, if we repeat our positive and negative test cases using the `semver` type (vs `semver_components`) we still accept valid states:
`
1
-- Success Case
2
select
3
  (1, 2, 3, array['beta', '1'], array['meta'])::semver,
4
-- returns: (1,2,3,{'beta','1'},{'meta'})
`
while invalid states are rejected with an error:
`
1
-- Failure Case
2
select
3
  (null, -500, null, array['?'], array[''])::semver
4
-- ERROR: value for domain semver violates check constraint "semver_check"
5
-- SQL state: 23514
`
### Testing[#](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#testing)
Our validation doesn’t have to be called manually. The `semver` domain can be used anywhere you’d use the `semver_components` type and the validations are automatically applied.
`
1
-- A table with a semver column
2
create table package_version(
3
  id bigserial primary key,
4
  package_name text not null,
5
  package_semver semver not null -- semver column
6
);
78
-- Insert some valid records
9
insert into package_version( package_name, package_semver )
10
values
11
  ('supabase-js', (2, 2, 3, null, null)),
12
  ('supabase-js', (2, 0, 0, array['rc', '1'], null)
13
);
1415
-- Attempt to insert an invalid record (major is null)
16
insert into package_version( package_name, package_semver )
17
values
18
  ('invalid-js', (null, 1, 0, array['asdf'], null));
19
-- ERROR: value for domain semver violates check constraint "semver_check"
`
Good stuff!
We’re 48 lines of SQL in and have solved for making invalid states unrepresentable. Now lets think about ergonomics.
### Displaying[#](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#displaying)
Now that our data type is well constrained, you might notice that selecting values from a `semver` typed column returns a tuple, rather than the SemVer string we’re used to seeing.
`
1
select
2
  *
3
from
4
  package_version
5
/*
6
id | package_name |  package_semver
7
-------------------------------------
8
 1 | supabase-js |     (2,2,3,,)
9
 2 | supabase-js | (2,0,0,"{rc,1}",)
10
*/
`
For example: `(2,0,0,"{rc,1}",)` vs `2.0.0-rc.1`
We could work around that problem with some [custom casts](https://www.postgresql.org/docs/current/sql-createcast.html), but I’d recommend keeping everything explicit with a function call.
`
1
create or replace function semver_to_text(semver)
2
  returns text
3
  immutable
4
  language sql
5
as $$
6
  select
7
    format('%s.%s.%s', $1.major, $1.minor, $1.patch)
8
    || case
9
      when $1.pre_release is null then ''
10
      else format('-%s', array_to_string($1.pre_release, '.'))
11
    end
12
    || case
13
      when $1.build_metadata is null then ''
14
      else format('+%s', array_to_string($1.build_metadata, '.'))
15
    end
16
$$;
`
Which allows us to query the `package_version` table and retrieve a string representation of the data.
`
1
select
2
  id,
3
  package_name,
4
  semver_to_text(package_semver) as ver -- cast as text
5
from
6
  package_version
7
/*
8
id | package_name |  ver
9
------------------------------
10
 1 | supabase-js |   2.2.3
11
 2 | supabase-js | 2.0.0-rc.1
12
*/
`
Or, better yet, use a [generated column](https://www.postgresql.org/docs/current/ddl-generated-columns.html)
`
1
create table package_version(
2
  id bigserial primary key,
3
  package_name text not null,
4
  package_semver semver not null,
5
 semver_text text generated always as (semver_to_text(package_semver)) stored
6
);
`
so the text representation is persisted along with the `semver` type and incurs no query/filter penalty.
### Other Tricks[#](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#other-tricks)
Postgres provides all the tools you could want to make your data types/domains work with SQL as seamlessly as builtins.
For example, you could:
  * add convenience functions to parse a [semver type from text](https://github.com/supabase/dbdev/blob/ca338584203d9b2eb7a4a378f5724674c15b9c25/supabase/migrations/20220117141507_semver.sql#L78)
  * [override the equality operator](https://github.com/supabase/dbdev/blob/ca338584203d9b2eb7a4a378f5724674c15b9c25/supabase/migrations/20220117141507_semver.sql#L37-L63) (`=`) to correctly reflect that versions differing only in build metadata are considered equal
  * [add a `max` function](https://github.com/supabase/dbdev/blob/ca338584203d9b2eb7a4a378f5724674c15b9c25/supabase/migrations/20220117141507_semver.sql#L122-L140) to efficiently query for the newest version of each package from within the database


to name a few.
Aligning the right parts of your business’ logic with the database can dramatically improve throughput, decrease IO, and simplify application code.
### Conclusion[#](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#conclusion)
Admittedly, building performant and ergonomic custom data types in Postgres involves a lot of ceremony.
That said, in cases where:
  * the type’s data integrity is critical
  * the type is well specified
  * the type’s spec does not change (or changes infrequently)


Teaching Postgres to have first class support for your custom type can be transformative for data integrity and performance.
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ftype-constraints-in-65-lines-of-sql&text=Type%20Constraints%20in%2065%20lines%20of%20SQL)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ftype-constraints-in-65-lines-of-sql&text=Type%20Constraints%20in%2065%20lines%20of%20SQL)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Ftype-constraints-in-65-lines-of-sql&t=Type%20Constraints%20in%2065%20lines%20of%20SQL)
[Last postGeo Queries with PostGIS in Ionic Angular1 March 2023](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular)
[Next postHappyTeams unlocks better performance and reduces cost with Supabase16 February 2023](https://supabase.com/blog/case-study-happyteams)
[postgres](https://supabase.com/blog/tags/postgres)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [SemVer](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#semver)
  * [SQL](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#sql)
    * [Storing Components](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#storing-components)
    * [Validation](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#validation)
    * [Testing](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#testing)
    * [Displaying](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#displaying)
    * [Other Tricks](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#other-tricks)
    * [Conclusion](https://supabase.com/blog/type-constraints-in-65-lines-of-sql#conclusion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ftype-constraints-in-65-lines-of-sql&text=Type%20Constraints%20in%2065%20lines%20of%20SQL)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ftype-constraints-in-65-lines-of-sql&text=Type%20Constraints%20in%2065%20lines%20of%20SQL)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Ftype-constraints-in-65-lines-of-sql&t=Type%20Constraints%20in%2065%20lines%20of%20SQL)
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

