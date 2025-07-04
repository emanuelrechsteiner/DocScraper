---
url: https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers
scraped_at: 2025-05-25T08:43:26.971932
title: Calendars in Postgres using Foreign Data Wrappers
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
# Calendars in Postgres using Foreign Data Wrappers
20 Dec 2024
•
6 minute read
[![Bo Lu avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fburmecia.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Bo LuEngineering](https://github.com/burmecia)
![Calendars in Postgres using Foreign Data Wrappers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2Fog-calcom.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we're releasing Foreign Data Wrappers for [Cal.com](https://cal.com) so that you can create event bookings directly from Postgres.
This is especially useful for signup forms where you create an event in your database and schedule an event simultaneously: now you can do all this in a single Postgres transaction.
## What's Cal.com?[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#whats-calcom)
[Cal.com](http://cal.com/) is an open-source scheduling platform that allows individuals and businesses to book and manage appointments. It is designed to work with a variety of use cases, from personal calendars to enterprise-grade scheduling systems. They have a great [developer toolkit](https://cal.com/platform).
## Creating event bookings with Postgres[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#creating-event-bookings-with-postgres)
[Cal.com](http://Cal.com) offers various scheduling features. One of the most common scenarios for developers is creating a new event in a calendar (for example, after someone has purchased a flight).
Let's use your Supabase database to create an event in [Cal.com](http://cal.com/), using Postgres Foreign Data Wrappers.
### Set up a Cal.com account[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-a-calcom-account)
  * Sign up on [Cal.com](http://Cal.com)
  * Visit [Settings -> Developer -> API keys](https://app.cal.com/settings/developer/api-keys) to create an API key


![create API key on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F01-cal-api-key.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Set up a Supabase account[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-a-supabase-account)
  * Sign up on [supabase.com](http://supabase.com)
  * Create a project or open an existing project
  * Go to [supabase.com/dashboard/project/_/database/extensions](https://supabase.com/dashboard/project/_/database/extensions) to enable `wrappers` extension


![enable wrappers extension](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F02-enable-wrapper-ext.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Create Wasm wrapper and a foreign server[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#create-wasm-wrapper-and-a-foreign-server)
Visit [Supabase SQL Editor](https://supabase.com/dashboard/project/_/sql/new), use below SQL to create the Wasm foreign data wrapper:
`
1
create foreign data wrapper wasm_wrapper
2
 handler wasm_fdw_handler
3
 validator wasm_fdw_validator;
`
And then create a foreign server for [Cal.com](http://Cal.com) connection with your API Key:
`
1
create server cal_server
2
 foreign data wrapper wasm_wrapper
3
 options (
4
  fdw_package_url 'https://github.com/supabase/wrappers/releases/download/wasm_cal_fdw_v0.1.0/cal_fdw.wasm',
5
  fdw_package_name 'supabase:cal-fdw',
6
  fdw_package_version '0.1.0',
7
  fdw_package_checksum '4afe4fac8c51f2caa1de8483b3817d2cec3a14cd8a65a3942c8b4ff6c430f08a',
8
  api_key '<your Cal.com API key>'
9
 );
`
Find the latest version and checksum in the docs: [fdw.dev/catalog/cal](https://fdw.dev/catalog/cal/)
### Set up foreign tables[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-foreign-tables)
Now let's setup the foreign tables. First of all, create a dedicate schema for the foreign tables:
`
1
create schema if not exists cal;
`
And then create a foreign table for [Event Types](https://app.cal.com/event-types):
`
1
create foreign table cal.event_types (
2
 attrs jsonb
3
)
4
 server cal_server
5
 options (
6
  object 'event-types'
7
 );
`
And another foreign table for [Bookings](https://app.cal.com/bookings/upcoming):
`
1
create foreign table cal.bookings (
2
 attrs jsonb
3
)
4
 server cal_server
5
 options (
6
  object 'bookings',
7
  rowid_column 'attrs'
8
 );
`
Note the `rowid_column` option which is required to insert data into `cal.bookings` table, we will see it later.
### Query Event Types and Bookings from Cal.com[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#query-event-types-and-bookings-from-calcom)
Great, now we are all set, it's time to query some juicy data from Cal.com! Let's start query from [Event Types](https://app.cal.com/event-types) first:
`
1
-- extract event types
2
select
3
 etg->'profile'->>'name' as profile,
4
 et->>'id' as id,
5
 et->>'title' as title
6
from cal.event_types t
7
 cross join json_array_elements((attrs->'eventTypeGroups')::json) etg
8
 cross join json_array_elements((etg->'eventTypes')::json) et;
`
![query event types from Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F03-query-event-types.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Note all the scheduling information returned from [Cal.com](http://Cal.com) API are stored in the JSON column `attrs` , from which we can extract any fields of that object. For example, we can extract `id`, `title`, `name` and etc., from [Bookings](https://app.cal.com/bookings/upcoming) object:
`
1
-- extract bookings
2
select
3
 bk->>'id' as id,
4
 bk->>'title' as title,
5
 bk->'responses'->>'name' as name,
6
 bk->>'startTime' as start_time
7
from cal.bookings t
8
 cross join json_array_elements((attrs->'bookings')::json) bk;
`
![query bookings from Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F04-query-booking.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Oops, it looks like we haven't booked any meetings with anybody yet. Now it's the fun part, let's make a booking on [Cal.com](http://Cal.com) from Supabase!
### Make a bookings on Cal.com from Supabase[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#make-a-bookings-on-calcom-from-supabase)
To make a booking directly from Postgres, all we need to do is to insert a record to `cal.bookings` foreign table, with the booking details in JSON format. For example,
`
1
-- make a 15 minutes meeting with Elon Musk
2
insert into cal.bookings(attrs)
3
values (
4
 '{
5
   "start": "2025-01-01T23:30:00.000Z",
6
   "eventTypeId": 1398027,
7
   "attendee": {
8
    "name": "Elon Musk",
9
    "email": "elon.musk@x.com",
10
    "timeZone": "America/New_York"
11
   }
12
 }'::jsonb
13
);
`
![make a bookings from postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F05-make-booking.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Here you can see we made a 15 minutes meeting booking with Elon, just to give him a happy new year greeting 😄. Note the `eventTypeId` , “1398027”, is our `15 Min Meeting` event type ID, you can find yours by querying the `cal.event_types` foreign table using above example SQL.
After inserting the booking record, we can verify it appears on our upcoming list in [Cal.com](http://Cal.com).
![verify bookings is on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F06-verify-on-cal.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
When we query `cal.bookings` again using the previous SQL, we can see our new booking record is in the results as well.
![verify bookings on Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F07-verify-on-supabase.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
That wraps up our tutorial! We've covered how to interact with [Cal.com](http://Cal.com) in Supabase using foreign wrapper and tables. For more information about available objects and fields, refer to the [Cal.com API v2 reference](https://cal.com/docs/api-reference/v2/introduction) and the [Wrappers Cal.com Wasm Wrapper documentation](https://fdw.dev/catalog/cal/).
## Built with Wrappers[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#built-with-wrappers)
The [Cal.com](http://Cal.com) FDW is built with [Wrappers](https://fdw.dev), a framework for Postgres Foreign Data Wrappers (FDW). Our latest release supports [Wasm (WebAssembly)](https://webassembly.org/) to simplify development for API-based services.
## Explore more[#](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#explore-more)
We've built a variety of wrappers available on [fdw.dev](https://fdw.dev/), ranging from popular tools like [Stripe](https://stripe.com/) and [Notion](https://www.notion.com/) to databases like [ClickHouse](https://clickhouse.com/) and [BigQuery](https://cloud.google.com/bigquery). Check out the [full catalog](https://fdw.dev/catalog/) and get started with Supabase today:
[database.new](https://database.new)
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&text=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&text=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&t=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)
[Last postAI Hackathon at Y Combinator20 December 2024](https://supabase.com/blog/ai-hackathon-at-y-combinator)
[Next postSupabase Launch Week 13 Hackathon Winners20 December 2024](https://supabase.com/blog/lw13-hackathon-winners)
[wasm](https://supabase.com/blog/tags/wasm)[wrappers](https://supabase.com/blog/tags/wrappers)[integration](https://supabase.com/blog/tags/integration)
On this page
  * [What's Cal.com?](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#whats-calcom)
  * [Creating event bookings with Postgres](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#creating-event-bookings-with-postgres)
    * [Set up a Cal.com account](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-a-calcom-account)
    * [Set up a Supabase account](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-a-supabase-account)
    * [Create Wasm wrapper and a foreign server](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#create-wasm-wrapper-and-a-foreign-server)
    * [Set up foreign tables](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#set-up-foreign-tables)
    * [Query Event Types and Bookings from Cal.com](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#query-event-types-and-bookings-from-calcom)
    * [Make a bookings on Cal.com from Supabase](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#make-a-bookings-on-calcom-from-supabase)
  * [Built with Wrappers](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#built-with-wrappers)
  * [Explore more](https://supabase.com/blog/calendars-in-postgres-using-foreign-data-wrappers#explore-more)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&text=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&text=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalendars-in-postgres-using-foreign-data-wrappers&t=Calendars%20in%20Postgres%20using%20Foreign%20Data%20Wrappers)
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
![enable wrappers extension](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F02-enable-wrapper-ext.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![create API key on Cal.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-20-cal-wrapper%2F01-cal-api-key.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

