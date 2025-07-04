---
url: https://supabase.com/blog/postgres-as-a-cron-server
scraped_at: 2025-05-25T09:26:32.946577
title: Postgres as a CRON Server
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
# Postgres as a CRON Server
05 Mar 2021
•
8 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Postgres as a CRON Server](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupabase-postgres-cron.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
A Supabase user asked recently if they can trigger a webhook periodically. We haven't yet released Functions yet, so we checked whether it's possible with Postgres.
It is. Here's how.
### What's cron?[#](https://supabase.com/blog/postgres-as-a-cron-server#whats-cron)
A "cron job" is a script[1](https://supabase.com/blog/postgres-as-a-cron-server#user-content-fn-1) that runs periodically at fixed times, dates, or intervals. Traditionally you'd set it up on a Linux server. An example might be an hourly script that downloads emails to your computer.
These days, cron jobs are set up on a remote servers and in the cloud to run internet-related tasks. Like checking an endpoint every hour, or scraping a website every day.
### Postgres + cron[#](https://supabase.com/blog/postgres-as-a-cron-server#postgres--cron)
Postgres has "extensions" which allow you to, well, extend the database with "non-core" features. Extensions essentially turn Postgres into an application server.
The team at [Citus](https://github.com/citusdata) created [`pg_cron`](https://github.com/citusdata/pg_cron) to run periodic jobs within your Postgres database.
#### Enabling the extension[#](https://supabase.com/blog/postgres-as-a-cron-server#enabling-the-extension)
If you're using a cloud-hosted Postgres database, make sure that `pg_cron` is installed first. The easiest way to do this is to run this command:
`
1
select name, comment, default_version, installed_version
2
from pg_available_extensions
3
where name = 'pg_cron';
`
If it returns a result then the extension is supported and you can turn it on by running:
`
1
create extension if not exists pg_cron;
`
If you're using Supabase you can also enable it in the Dashboard.
![This image shows that pg_cron is enabled in the Supabase Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupabase-extensions.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
#### Granting access to the extension[#](https://supabase.com/blog/postgres-as-a-cron-server#granting-access-to-the-extension)
If you're planning to use a `non-superuser` role to schedule jobs, ensure that they are granted access to the `cron` schema and its underlying objects beforehand.
`
1
grant usage on schema cron to {{DB user}};
2
grant all privileges on all tables in schema cron to {{DB user}};
`
Failure to do so would result in jobs by these roles to not run at all.
### Postgres + webhooks[#](https://supabase.com/blog/postgres-as-a-cron-server#postgres--webhooks)
The Supabase customer wanted to call external endpoints every day. How would we do this? Another extension of course. This time we're going to use [pgsql-http](https://github.com/pramsey/pgsql-http) by [@pramsey](https://github.com/pramsey). Using the same technique, we can enable the extension (if it exists in your cloud provider).
`
1
create extension if not exists http;
`
This extension can now be used for [sending](https://github.com/pramsey/pgsql-http#functions) `GET`, `POST`, `PATCH`, and `DELETE` requests.
For example, this function would get all the people in Star Wars (using the [Star Wars API](https://swapi.dev)):
`
1
select content::json->'results'
2
from http_get('https://swapi.dev/api/people');
`
### Postgres + cron + webhooks[#](https://supabase.com/blog/postgres-as-a-cron-server#postgres--cron--webhooks)
Now the fun stuff. For this example we're going to call [webhook.site](https://webhook.site) every minute with the payload `{ "hello": "world" }`.
Here's the code (with comments `--like this`).
`
1
select
2
 cron.schedule(
3
  'webhook-every-minute', -- name of the cron job
4
  '* * * * *', -- every minute
5
  $$
6
  select status
7
  from
8
   http_post(
9
    'https://webhook.site/223c8a43-725b-4cbd-b1fe-d0da73353a6b', -- webhook URL, replace the ID(223c8..) with your own
10
    '{"hello": "world"}', -- payload
11
    'application/json'
12
   )
13
  $$
14
 );
`
Now when we see that the payload is sent every minute, exactly on the minute.
![This image shows the website that receives our webhook every minute.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fwebsite-hook.jpeg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
And that's it! We've built a cron webhook. Breaking down the code example above we have 2 key parts:
#### POSTing data[#](https://supabase.com/blog/postgres-as-a-cron-server#posting-data)
This is the part that sends the data to the website:
`
1
select status
2
from
3
 http_post(
4
  'https://webhook.site/223c8a43-725b-4cbd-b1fe-d0da73353a6b', -- webhook URL
5
  '{"hello": "world"}', -- payload
6
  'application/json'
7
 );
`
#### Scheduling the job[#](https://supabase.com/blog/postgres-as-a-cron-server#scheduling-the-job)
The HTTP function is wrapped with the CRON scheduler:
`
1
select
2
 cron.schedule(
3
  'cron-name', -- name of the cron job
4
  '* * * * *', -- every minute
5
  $$
6
   -- Put your code between two dollar signs so that you can create full statements.
7
   -- Alternatively, you can write you code in a Postgres Function and call it here.
8
  $$
9
 );
`
The second parameter uses cron syntax:
`
1
 ┌───────────── min (0 - 59)
2
 │ ┌────────────── hour (0 - 23)
3
 │ │ ┌─────────────── day of month (1 - 31)
4
 │ │ │ ┌──────────────── month (1 - 12)
5
 │ │ │ │ ┌───────────────── day of week (0 - 6) (0 to 6 are Sunday to
6
 │ │ │ │ │         Saturday, or use names; 7 is also Sunday)
7
 * * * * *
`
If you're unfamiliar with the cron syntax, useful shortcuts can be found on [crontab.guru](https://crontab.guru/)
`
1
* * * * *    # every minute
2
*/5 * * * *   # every 5th minute
3
0 * * * *    # every hour
4
0 0 * * *    # every day
`
#### Managing your cron jobs[#](https://supabase.com/blog/postgres-as-a-cron-server#managing-your-cron-jobs)
To see a list of all your cron jobs, run:
`
1
select * from cron.job;
`
And if you need to see the results of each cron iterations, you can find them in `cron.job_run_details`:
`
1
select * from cron.job_run_details;
`
To stop a running cron job, you can run:
`
1
select cron.unschedule('webhook-every-minute'); -- pass the name of the cron job
`
### What can I do with this?[#](https://supabase.com/blog/postgres-as-a-cron-server#what-can-i-do-with-this)
There are plenty use-cases for this. For example:
  * **Sending welcome emails.** If you use an email provider with an HTTP API, then you batch emails to that service. Write a function that `selects` all your signups yesterday, then sends them to your favorite transactional email service. Schedule it every day to run at midnight.
  * **Aggregating data.** If you're providing analytical data, you might want to aggregate it into time periods for faster querying (which serves a similar purpose as a [Materialized View](https://supabase.com/blog/postgresql-views#materialized-views-vs-conventional-views)).
  * **Deleting old data.** Need to free up space? Run a scheduled job to delete data you no longer need.


See a detailed list in the [`pg_cron` README](https://github.com/citusdata/pg_cron#example-use-cases).
## Addendum[#](https://supabase.com/blog/postgres-as-a-cron-server#addendum)
### Postgres background workers[#](https://supabase.com/blog/postgres-as-a-cron-server#postgres-background-workers)
You might have noticed [this](https://github.com/pramsey/pgsql-http#why-this-is-a-bad-idea) notice the warning at the bottom of the `http` readme:
> "What happens if the web page takes a long time to return?" Your SQL call will just wait there until it does. Make sure your web service fails fast.
Luckily pg_cron implements [Background Workers](https://paquier.xyz/postgresql-2/postgres-9-3-feature-highlight-custom-background-workers/):
> Care is taken that these extra processes do not interfere with other postmaster tasks: only one such process is started on each ServerLoop iteration. This means a large number of them could be waiting to be started up and postmaster is still able to quickly service external connection requests.
This means that even if your endpoint takes a long time to return, it's not going to be blocking your core Postgres functions. Either way, you should probably only call endpoints that will return a response quickly, or set the http extension to fail fast (`http.timeout_msec = 300`).
If you're familiar with `C`, you could also help `@pramsey` to implement async functions: <https://github.com/pramsey/pgsql-http/issues/105>
### Should I use Postgres as a cron server?[#](https://supabase.com/blog/postgres-as-a-cron-server#should-i-use-postgres-as-a-cron-server)
There are plenty of ways to run cron jobs these days. You can trigger them from your local machine. You can install them on a VPS. You can schedule Serverless functions. You can use a paid service. You can use GitHub Actions.
Is Postgres the best place to put your cron jobs? `¯\_(ツ)_/¯`. Postgres databases are free on Supabase and since it takes only one minute to [get started](https://supabase.com/dashboard/), why not make your next cron server a Postgres database?
## More Postgres resources[#](https://supabase.com/blog/postgres-as-a-cron-server#more-postgres-resources)
  * [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
  * [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
  * [Postgres Views](https://supabase.com/blog/postgresql-views)
  * [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
  * [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
  * [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
  * [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)


## Footnotes[#](https://supabase.com/blog/postgres-as-a-cron-server#footnote-label)
  1. Not necessarily a script. The cron is really a scheduler which triggers a job (of some sort, usually a bash script). [↩](https://supabase.com/blog/postgres-as-a-cron-server#user-content-fnref-1)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-as-a-cron-server&text=Postgres%20as%20a%20CRON%20Server)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-as-a-cron-server&text=Postgres%20as%20a%20CRON%20Server)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-as-a-cron-server&t=Postgres%20as%20a%20CRON%20Server)
[Last postToad, a link shortener with simple APIs for low-coders8 March 2021](https://supabase.com/blog/toad-a-link-shortener-with-simple-apis-for-low-coders)
[Next postSupabase Beta February 20212 March 2021](https://supabase.com/blog/supabase-beta-february-2021)
[postgres](https://supabase.com/blog/tags/postgres)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [Addendum](https://supabase.com/blog/postgres-as-a-cron-server#addendum)
  * [More Postgres resources](https://supabase.com/blog/postgres-as-a-cron-server#more-postgres-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-as-a-cron-server&text=Postgres%20as%20a%20CRON%20Server)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-as-a-cron-server&text=Postgres%20as%20a%20CRON%20Server)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-as-a-cron-server&t=Postgres%20as%20a%20CRON%20Server)
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

