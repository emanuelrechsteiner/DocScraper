---
url: https://supabase.com/partners/integrations/cloudflare-workers
scraped_at: 2025-05-25T09:11:35.066930
title: CloudFlare Workers | Works With Supabase
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
[Back](https://supabase.com/partners/integrations)
![CloudFlare Workers](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fcloudflare-integration%2Fcloudflare_workers_logo.png%3Ft%3D2023-07-21T11%253A07%253A47.005Z&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# CloudFlare Workers
## Overview
Using Supabase in Cloudflare Workers has always been a great way to interact with your data from the edge. Supabase-js communicates with your Supabase Postgres instance via HTTP using PostgREST, so you never need to worry about running out of database connections.
In this guide we'll walk you through a new addition to the Cloudflare Workers dashboard - the ability to authenticate directly with your Supabase account, and automatically inject your Supabase environment variables into your Worker code.
## How To Enable Supabase Integration in Cloudflare Workers
Start by heading to the [Cloudflare Dashboard](https://dash.cloudflare.com), go to the Workers & Pages tab and hit 'Create Application' followed by 'Create Worker'.
![Cloudflare Dashboard 2](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/2.png)
Deploy the Hello World example Worker. Once it's deployed hit 'Configure Worker'.
![Cloudflare Dashboard 3](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/3.png)
On the configuration page select the Settings tab, followed by the Integrations option.
You should now see the database integration options. On the Supabase card, click 'Add Integration'
![Cloudflare Dashboard 4](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/4.png)
After reviewing and accepting the terms, you will be shown the option to connect and a Supabase popup should appear.
Follow the flow by selecting your Supabase Org and the Project you wish to connect to. If you don't have any projects yet, head over to the [Supabase Dashboard](https://supabase.com/dashboard) to create one.
![Cloudflare Dashboard 5](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/5.png)
Once it's connected you will be given the option to select which Supabase Key you want to pull into the Worker context.
The `Anon` key here is one that always adhires to the Database's RLS policies (read more on [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security)).
The `Service Role` is typically ok to use in backend contexts, such as Cloudflare Workers, but note that this key **bypasses your Row Level Security policies** , and has the ablity to read, write, and delete any data in your database.
![Cloudflare Dashboard 6](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/6.png)
Once this is done the `SUPABASE_KEY` and `SUPABASE_URL` environment variables will now be available from your Cloudflare Worker code.
![Cloudflare Dashboard 7](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cloudflare-integration/documentation/7.png)
You can now install the supabase-js client in your Worker:
`npm install @supabase/supabase-js`
Then you can initiate the Supabase client, and start querying your data:
`
1
import { createClient } from '@supabase/supabase-js'
23
export default {
4
 async fetch(request, env) {
5
  const supabase = createClient(env.SUPABASE_URL, env.SUPABASE_KEY)
6
  const { data, error } = await supabase.from('countries').select('*')
7
  if (error) throw error
8
  return new Response(JSON.stringify(data), {
9
   headers: {
10
    'Content-Type': 'application/json',
11
   },
12
  })
13
 },
14
}
`
The snippet above assumes you already have a `countries` table. Run the following in the [SQL Editor in the Supabase Dashboard](https://supabase.com/dashboard/project/_/sql) if you wish to install this demo schema:
`
1
create table countries (
2
 id serial primary key,
3
 name varchar(255) not null
4
);
56
insert into countries
7
 (name)
8
values
9
 ('Oceania');
1011
insert into countries
12
 (name)
13
values
14
 ('Genovia');
1516
insert into countries
17
 (name)
18
values
19
 ('Wakanda');
2021
insert into countries
22
 (name)
23
values
24
 ('Lilliput');
`
Remember that you don't need to use supabase-js to connect to your Supabase database, you can connect "directly" to the underlying Postgres database using the connection string (every Supabase database comes pre-installed with a [connection pooler](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pool)), or you can try Cloudflare's new [TCP socket method of connecting to Postgres](https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/) directly from Cloudflare Workers.
  * [Cloudflare Integration Docs](https://developers.cloudflare.com/workers/learning/integrations/databases/#supabase).
  * [Cloudflare Dashboard](https://dash.cloudflare.com/).
  * [Cloudflare Integration Announcement](https://blog.cloudflare.com/announcing-database-integrations/).


## Details
DeveloperCloudFlare
Category[DevTools](https://supabase.com/partners/integrations#devtools)
Website[workers.cloudflare.com](https://workers.cloudflare.com/)
Documentation[Learn](https://workers.cloudflare.com/)
Third-party integrations and docs are managed by Supabase partners.
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

