---
url: https://supabase.com/blog/postgrest-9
scraped_at: 2025-05-25T09:04:11.299842
title: PostgREST 9
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
# PostgREST 9
27 Nov 2021
•
4 minute read
[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)
![PostgREST 9](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpostgrest-9%2Fwhats-new-in-postgrest-9-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
PostgREST turns your PostgreSQL database automatically into a RESTful API. Today, PostgREST 9 was [released](https://postgrest.org/en/v9.0/releases/v9.0.0.html). Let's take a look at some of the new features.
## Resource embedding with Inner Joins[#](https://supabase.com/blog/postgrest-9#resource-embedding-with-inner-joins)
PostgREST 9 brings a [much-requested feature](https://github.com/supabase/postgrest-js/issues/197): the ability to do `inner joins` when embedding a table.
Here's an example with `supabase-js`:
hideCopy
`
1
const { data, error } = await supabase
2
 .from('messages')
3
 .select('*, users!inner(*)')
4
 .eq('users.username', 'Jane')
`
With the new `!inner` keyword, you can now filter rows of the top-level table (`messages`) based on a filter (`eq`) of the embedded table (`users`). This works across all Supabase client libraries and you can use it with any of the available operators (`gt`, `in`, etc.)
[Read more](https://postgrest.org/en/v9.0/releases/v9.0.0.html#resource-embedding-with-top-level-filtering).
## Functions with unnamed parameters[#](https://supabase.com/blog/postgrest-9#functions-with-unnamed-parameters)
You can now make `POST` requests to functions with a single unnamed parameter. This is particularly useful for webhooks that send JSON payloads.
For example, imagine you were using Postmark as an email provider and you wanted to save email bounces using their [bounce webhook](https://postmarkapp.com/developer/webhooks/bounce-webhook). Previously this wouldn't be possible with PostgREST, as every function required a named parameter.
As of PostgREST 9, this is possible. Simply create a function inside your PostgreSQL database to receive the raw JSON:
hideCopy
`
1
create function store_bounces(json)
2
returns json
3
language sql
4
as $$
5
 insert into bounces (webhook_id, email)
6
 values (
7
  ($1->>'ID')::bigint,
8
  ($1->>'Email')::text
9
 );
1011
 select '{ "status": 200 }'::json;
12
$$;
`
And the webhook can send data directly to your database via an `rpc` call:
hideCopy
`
1
POST https://<PROJECT_REF>.supabase.co/rest/v1/rpc/store_bounces HTTP/1.1
2
Content-Type: application/json
34
{
5
 "RecordType": "Bounce",
6
 "MessageStream": "outbound",
7
 "ID": 4323372036854775807,
8
 "Type": "HardBounce",
9
 "MessageID": "883953f4-6105-42a2-a16a-77a8eac79483",
10
 "Description": "The server was unable to deliver your message (ex: unknown user, mailbox not found).",
11
 "Details": "Test bounce details",
12
 "Email": "john@example.com",
13
 "From": "sender@example.com",
14
 "BouncedAt": "2019-11-05T16:33:54.9070259Z"
15
}
`
[Read more](https://postgrest.org/en/v9.0/api.html#s-proc-single-unnamed).
## PostgreSQL 14 compatibility[#](https://supabase.com/blog/postgrest-9#postgresql-14-compatibility)
If you've ever done your own custom `auth` functions using PostgREST [HTTP Context](https://postgrest.org/en/v8.0/api.html#accessing-request-headers-cookies-and-jwt-claims), note that a breaking change was necessary for PostgreSQL 14 Compatibility. You'll need to update them:
`From`| `To`  
---|---  
`current_setting('request.jwt.claim.custom-claim', true)`| `current_setting('request.jwt.claims', true)::json->>'custom-claim'`  
`current_setting('request.header.custom-header', true)`| `current_setting('request.headers', true)::json->>'custom-header'`  
If you only use Supabase default `auth` functions(`auth.email()`, `auth.uid()`, `auth.role()`), then no action is required because we have updated the functions to handle these changes transparently.
[Read more](https://postgrest.org/en/v9.0/releases/v9.0.0.html#postgresql-14-compatibility).
## Release notes[#](https://supabase.com/blog/postgrest-9#release-notes)
There are a lot more improvements released in PostgREST 9, including [support for Partitioned Tables](https://postgrest.org/en/v9.0/releases/v9.0.0.html#partitioned-tables), [improved doc](https://postgrest.org/en/v9.0/releases/v9.0.0.html#documentation-improvements), and [bug fixes](https://postgrest.org/en/v9.0/releases/v9.0.0.html#bug-fixes).
You can see the full updates on the [PostgREST 9 release notes](https://postgrest.org/en/v9.0/releases/v9.0.0.html).
## More Postgres resources[#](https://supabase.com/blog/postgrest-9#more-postgres-resources)
  * [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
  * [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
  * [Postgres Views](https://supabase.com/blog/postgresql-views)
  * [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
  * [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
  * [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
  * [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-9&text=PostgREST%209)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-9&text=PostgREST%209)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-9&t=PostgREST%209)
[Last postNew in PostgreSQL 14: What every developer should know28 November 2021](https://supabase.com/blog/whats-new-in-postgres-14)
[Next postHow we launch at Supabase26 November 2021](https://supabase.com/blog/supabase-how-we-launch)
[launch-week](https://supabase.com/blog/tags/launch-week)[release-notes](https://supabase.com/blog/tags/release-notes)[tech](https://supabase.com/blog/tags/tech)[community](https://supabase.com/blog/tags/community)
On this page
  * [Resource embedding with Inner Joins](https://supabase.com/blog/postgrest-9#resource-embedding-with-inner-joins)
  * [Functions with unnamed parameters](https://supabase.com/blog/postgrest-9#functions-with-unnamed-parameters)
  * [PostgreSQL 14 compatibility](https://supabase.com/blog/postgrest-9#postgresql-14-compatibility)
  * [Release notes](https://supabase.com/blog/postgrest-9#release-notes)
  * [More Postgres resources](https://supabase.com/blog/postgrest-9#more-postgres-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-9&text=PostgREST%209)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-9&text=PostgREST%209)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-9&t=PostgREST%209)
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

