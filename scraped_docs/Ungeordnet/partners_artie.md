---
url: https://supabase.com/partners/artie
scraped_at: 2025-05-25T09:48:58.338479
title: Artie | Works With Supabase
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
![Artie](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fartie%2Fartie-logo.png&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Artie
![Artie](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fartie%2Fartie-og.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
Artie is a real-time database replication platform that leverages change data capture. We help companies replicate data from databases like Supabase to their data warehouse (Snowflake, BigQuery, Redshift) and ensure data consistency.
Artie is fully-managed and quick to set up. We take care of historical backfills, provide analytics, monitoring, schema change alerts and more - all out-of-the-box.
### Step #1 - Enable IPv4 Add On
Artie does not support IPv6. Please ensure that you have IPv4 enabled as an add on.
To do this:
  1. Go to your project settings in Supabase
  2. Click on Add Ons
  3. Enable IPv4


![Screenshot 1](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image1.png)
### Step #2 - Create an Artie account
Go to Artie's website and fill out the contact form (<https://www.artie.com/contact>). We will reach out shortly with an account activation link.
![Screenshot 2](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image2.png)
### Step #3 - Find your Supabase database credentials
You can find this under Settings > Database > Connection Parameters.
We will need the following:
  * Database Host (Uncheck Display connection pooler)
  * Database Port (Should be 5432)
  * Username
  * Password
  * Database


To create a service account, please run the following commands in Supabase.
`
1
CREATE USER artie_transfer WITH PASSWORD 'password';
23
-- Grant replication permissions
4
ALTER USER artie_transfer REPLICATION;
56
-- Grant read-only access to future tables
7
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO artie_transfer;
8
-- Grant access to existing tables
9
GRANT SELECT ON ALL TABLES IN SCHEMA public TO artie_transfer;
1011
CREATE PUBLICATION dbz_publication FOR ALL TABLES;
`
### Step #4 - Create a new deployment in Artie
Head over to Artie with the information you have gathered from Step #2 and create a new deployment.
![Screenshot 3](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image3.png)
  * Pick the tables you want to replicate
  * (Optional) You can also enable [history mode](https://www.artie.com/blogs/history-table) (which will create a SCD Type 4 table with `__history` suffix) and record every database change. Consider enabling history mode if you need audit logs or to replace existing daily snapshot processes.
  * Pick your destination. Destination setup instructions will appear on the right hand side of the screen.


Check out our [docs](https://artie.com/docs/start) if you need additional help.
## Product Screenshots
![Screenshot 4](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image4.png)
![Screenshot 5](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image5.png)
![Screenshot 6](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image6.png)
## Details
DeveloperArtie
Category[Data Platform](https://supabase.com/partners/integrations#data%20platform)
Website[artie.com](https://artie.com/)
Documentation[Learn](https://docs.artie.com/real-time-sources/postgresql)
Third-party integrations and docs are managed by Supabase partners.
# Get started with Artie and Supabase.
[ Add integration ](https://docs.artie.com/real-time-sources/postgresql/supabase)
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

