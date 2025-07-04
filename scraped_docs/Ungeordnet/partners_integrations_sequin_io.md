---
url: https://supabase.com/partners/integrations/sequin_io
scraped_at: 2025-05-25T09:25:45.802791
title: Sequin | Works With Supabase
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
![Sequin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fsequin_io%2Fsequin_logo.png&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Sequin
![Sequin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fsequin_io%2Fsequin-stream-1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Sequin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fsequin_io%2Fsequin-stream-2.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Sequin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fsequin_io%2Fsequin-stream-3.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Sequin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fsequin_io%2Fsequin-stream-4.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
Sequin sends your Supabase rows and changes anywhere you want. It’s designed to never miss an `insert`, `update`, or `delete` and provide exactly-once process for all changes.
You can receive changes via HTTP push (webhooks) or pull (think SQS). You can easily send changes to your application, another service (i.e. trigger.dev, resend, ingest), or trigger a Supabase edge function.
At some point, almost every Supabase app needs to trigger side effects. Think of sending a new user a welcome email or fanning out Jobs when an order arrives. Sequin aims to give you the tools to make that happen.
## Killer features
  * **Never miss a message:** Sequin persists messages until they are acknowledged (i.e. exactly once processing guarantees).
  * **SQL-based routing:** Filter and route messages using SQL `where` conditions
  * **Replays:** Rewind to any row on your table. Republish messages that match a SQL query.
  * **Backfills:** Queue up records from this moment forward or the entire table.
  * **Observability and debugging:** Sequin has a web console that adds the Supabase queue tooling you’ve been looking for.
  * **Skip the PL/pgsql:** Define business logic in the language of your choice and in your application.
  * **Transforms:** Transform message payloads with Lua functions.


## Documentation
This guide steps you through connecting Sequin to your Supabase database to send database changes anywhere.
### 1. Connect to Sequin with a direct connection
Sequin uses the Write Ahead Log (WAL) to capture changes from your Supabase database. Supabase's connection pooling does not support the WAL, so you need to connect to your Supabase database using a direct connection.
Here is how to set up a direct connection in Supabase:
  1. Login to Supabase and navigate to the database settings page (**Settings > Configurations > Database**).
  2. Disable the **Use connection pooling** option to show your direct connection credentials:
  3. In Sequin, enter the direct connection details in the **Database connection** page, including the **Host** , **Port** , **Database** , **User** , and **Password** for your Supabase database. Turn **SSL** on.


✓ Sequin will automatically detect that you're using a Supabase database and check that your connection is configured correctly.
### 2. Create a replication slot in Supabase
With your Supabase database connected to Sequin, you'll now create the replication slot that Sequin will use to detect changes in your database.
  1. In the Supabase SQL editor, run the following SQL command to create a replication slot:
`
1
select pg_create_logical_replication_slot('sequin_slot', 'pgoutput');
`


This creates a replication slot named `sequin_slot`.
  1. Next, you'll create a publication to indicate which tables will publish changes to the replication slot.
In the SQL editor, run the following SQL command to create a publication:
`
1
create publication sequin_pub for table table1, table2, table3;
`
If you want to publish changes from all the tables in your database, you can also use the `for all tables` option:
`
1
create publication sequin_pub for all tables;
`
  2. Back in the Sequin Console, enter the name of the replication slot (e.g. `sequin_slot`) and publication (e.g. `sequin_pub`) you just created. Then, name your database and click **Create Database**.
![Supabase connected to Sequin](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/sequin_io/sequin-stream-successful-database-connection.png)


✓ Sequin will now capture rows and changes from your Supabase database.
### 3. Add a consumer in Sequin
Sequin and Supabase are now working together. Every change in your database will be captured and can be sent to your application, another service, or trigger a Supabase edge function.
You’ll add a consumer in Sequin to define what changes you want to process and where you want to send them.
  1. In the Sequin Console, navigate to the Consumers page and click Create Consumer.
  2. Select your Supabase database and the table that contains the data you want to process in the consumer. Then, add filters to process just the rows and changes you need.
  3. Set your consumer as an HTTP push consumer or HTTP pull consumer, and then configure the endpoints and headers as needed. Then save your consumer.


✓ Make a change in your database, and see it appear in your consumer:
![Supabase change to Sequin consumer](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/sequin_io/sequin-stream-imgur.gif)
## Next steps
You’ve now walked through the basics of connecting to Sequin, creating a consumer, and capturing changes. Now, you can write the business logic for your application to react to the changes.
From here, you might want to:
  * [Move some Supabase webhooks](https://sequinstream.com/docs/guides/supabase#moving-supabase-webhooks-to-sequin) to Sequin.
  * Set up a Sequin consumer to [trigger a Supabase edge function](https://sequinstream.com/docs/guides/supabase#triggering-a-supabase-edge-function-with-sequin).
  * Use the [Sequin javascript SDK](https://github.com/sequinstream/sequin-js) to pull messages from a consumer.
  * Dig into Sequin’s [core concepts](https://sequinstream.com/docs/core-concepts) to tune your setup.


## Details
Watch an introductory video
![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
DeveloperSequin
Category[DevTools](https://supabase.com/partners/integrations#devtools)
Website[sequinstream.com](https://sequinstream.com)
Documentation[Learn](https://sequinstream.com/docs/introduction)
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

