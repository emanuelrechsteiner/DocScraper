---
url: https://supabase.com/blog/postgrest-11-prerelease
scraped_at: 2025-05-25T08:54:26.954004
title: PostgREST 11 pre-release
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
# PostgREST 11 pre-release
16 Dec 2022
•
5 minute read
[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)
![PostgREST 11 pre-release](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-community%2Fpostgrest.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
PostgREST 11 is not wrapped up yet, however a pre-release with the **[latest features and fixes](https://github.com/PostgREST/postgrest/releases/tag/v10.1.1.20221212)** is available on the Supabase CLI.
In this blog post we'll cover some of the improved querying capabilities: spreading related tables, related orders and anti-joins.
## Spreading related tables[#](https://supabase.com/blog/postgrest-11-prerelease#spreading-related-tables)
Very often the way we structure a database is not the way we want to present it to the frontend application. For example, let's assume we have a `films` and `technical_specs` tables and they form a one-to-one relationship.
Using PostgREST resource embedding, we can query them in one request like so
From HTTP:
`
1
GET /films?select=title,technical_specs(camera,laboratory,sound_mix)
`
or JavaScript:
`
1
const { data, error } = await supabase.from('films').select(`
2
  title,
3
  technical_specs (
4
   camera, laboratory, duration
5
  )
6
 `)
`
Response:
`
1
[
2
 {
3
  "title": "Pulp Fiction",
4
  "technical_specs": {
5
   "camera": "Arriflex 35-III",
6
   "laboratory": "DeLuxe, Hollywood (CA), USA (color)",
7
   "duration": "02:34:00"
8
  }
9
 },
10
 "..."
11
]
`
But we'd like to present a “flattened” result to the frontend, without the `technical_specs` object. For this we could create a new database view or function that shapes the json the way we want, but creating extra database objects is not always convenient.
Using the new “spread” operator(syntax borrowed from [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)), we can expand a related table columns and remove the nested object.
From HTTP:
`
1
GET /films?select=title,...technical_specs(camera,laboratory,duration)
`
or JavaScript:
`
1
const { data, error } = await supabase.from('films').select(`
2
  title,
3
  ...technical_specs (
4
   camera, laboratory, duration
5
  )
6
 `)
`
Response:
`
1
[
2
 {
3
  "title": "Pulp Fiction",
4
  "camera": "Arriflex 35-III",
5
  "laboratory": "DeLuxe, Hollywood (CA), USA (color)",
6
  "duration": "02:34:00"
7
 },
8
 "..."
9
]
`
This only works for one-to-one and many-to-one relationships for now but we're looking at ways to remove this restriction.
## Order by related tables[#](https://supabase.com/blog/postgrest-11-prerelease#order-by-related-tables)
It's also a common use case to order a table by a related table column. For example, suppose you'd like to order `films` based on the `technical_specs.duration` column.
You can now do it like so:
From HTTP:
`
1
GET /films?select=title,...technical_specs(duration)&order=technical_specs(duration).desc
`
or JavaScript:
`
1
const { data, error } = await supabase
2
 .from('films')
3
 .select(`
4
  title,
5
  ...technical_specs (
6
   duration
7
  )
8
 `)
9
  .order('technical_specs(duration)', { descending: true }))
`
Response:
`
1
[
2
 {
3
  "title": "Amra Ekta Cinema Banabo",
4
  "duration": "21:05:00"
5
 },
6
 {
7
  "title": "Resan",
8
  "duration": "14:33:00"
9
 },
10
 "..."
11
]
`
Similarly to spreading related tables, this only works for one-to-one and many-to-one relationships.
## Anti-Joins[#](https://supabase.com/blog/postgrest-11-prerelease#anti-joins)
To do the equivalent of a left anti-join, you can now filter the rows where the related table is `null`.
From HTTP:
`
1
GET /films?select=title,nominations()&nominations=is.null
`
or JavaScript:
`
1
const { data, error } = await supabase
2
 .from('films')
3
 .select(`
4
  title,
5
  nominations()
6
 `)
7
  .is('nominations', null))
`
Response:
`
1
[
2
 {
3
  "title": "Memories of Murder"
4
 },
5
 {
6
  "title": "Rush"
7
 },
8
 {
9
  "title": "Groundhog Day"
10
 },
11
 "..."
12
]
`
Note that `nominations` doesn't select any columns so they don't show on the resulting response.
The equivalent of an inner join can be done by filtering the rows where the related table is `not null`.
`
1
GET /films?select=title,nominations(rank,...competitions(name))&nominations=not.is.null
`
`
1
const { data, error } = await supabase
2
 .from('films')
3
 .select(
4
  `
5
  title,
6
  nominations(rank,...competitions(name))
7
 `
8
 )
9
 .not('nominations', 'is', null)
`
Response:
`
1
[
2
 {
3
  "title": "Pulp Fiction"
4
  "nominations": [
5
   {"rank": 1, "name": "Palme d'Or"},
6
   {"rank": 1, "name": "BAFTA Film Award"},
7
   {"..."}
8
  ]
9
 },
10
 "..."
11
]
`
This was already possible with the `!inner` modifier([introduced on PostgREST 9](https://supabase.com/blog/postgrest-9#resource-embedding-with-inner-joins)) but the `not null` filter is more flexible and can be used with an [or filter](https://supabase.com/docs/reference/javascript/or) to combine related tables' conditions.
## Try it out[#](https://supabase.com/blog/postgrest-11-prerelease#try-it-out)
This pre-release is not deployed to Supabase cloud but you can try it out locally with the [Supabase CLI](https://supabase.com/docs/reference/cli/introduction).
`
1
$ supabase start
`
Please try it and report any bugs, suggestions or ideas!
## More Launch Week 6[#](https://supabase.com/blog/postgrest-11-prerelease#more-launch-week-6)
  * [Day 1: New Supabase Docs, built with Next.js](https://supabase.com/blog/new-supabase-docs-built-with-nextjs)
  * [Day 2: Supabase Storage v2: Image resizing and Smart CDN](https://supabase.com/blog/storage-image-resizing-smart-cdn)
  * [Day 3: Multi-factor Authentication via Row Level Security Enforcement](https://supabase.com/blog/mfa-auth-via-rls)
  * [Day 4: Supabase Wrappers, a Postgres FDW framework written in Rust](https://supabase.com/blog/postgres-foreign-data-wrappers-rust)
  * [Day 5: Supabase Vault is now in Beta](https://supabase.com/blog/vault-now-in-beta)
  * [Community Day](https://supabase.com/blog/launch-week-6-community-day)
  * [Point in Time Recovery is now available](https://supabase.com/blog/postgres-point-in-time-recovery)
  * [Custom Domain Names are now available](https://supabase.com/blog/custom-domain-names)
  * [Wrap Up: everything we shipped](https://supabase.com/blog/launch-week-6-wrap-up)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&text=PostgREST%2011%20pre-release)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&text=PostgREST%2011%20pre-release)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&t=PostgREST%2011%20pre-release)
[Last postPoint in Time Recovery is now available for Pro projects16 December 2022](https://supabase.com/blog/postgres-point-in-time-recovery)
[Next postSupabase Vault is now in Beta16 December 2022](https://supabase.com/blog/vault-now-in-beta)
[postgres](https://supabase.com/blog/tags/postgres)[launch-week](https://supabase.com/blog/tags/launch-week)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [Spreading related tables](https://supabase.com/blog/postgrest-11-prerelease#spreading-related-tables)
  * [Order by related tables](https://supabase.com/blog/postgrest-11-prerelease#order-by-related-tables)
  * [Anti-Joins](https://supabase.com/blog/postgrest-11-prerelease#anti-joins)
  * [Try it out](https://supabase.com/blog/postgrest-11-prerelease#try-it-out)
  * [More Launch Week 6](https://supabase.com/blog/postgrest-11-prerelease#more-launch-week-6)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&text=PostgREST%2011%20pre-release)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&text=PostgREST%2011%20pre-release)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&t=PostgREST%2011%20pre-release)
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

