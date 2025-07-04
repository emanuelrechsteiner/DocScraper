---
url: https://supabase.com/blog/pg-paper-dump
scraped_at: 2025-05-25T08:40:18.218667
title: Announcing Data Preservation Service
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
# Announcing Data Preservation Service
01 Apr 2024
•
3 minute read
[![Long Hoang avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Floong.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Long HoangGrowth](https://github.com/loong)
![Announcing Data Preservation Service](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-04-01-pg-paper-dump%2Fpg-paper-dump-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We live in a world where data is as critical as air and water, powering everything from global enterprises to personal projects. At Supabase, we create products that are not just cutting-edge but also secure, reliable, and now, timeless.
Today, we are excited to introduce a groundbreaking service that bridges the digital divide with the most enduring medium known to humankind: paper. Meet [pg_paper_dump](https://github.com/supabase-community/pg_paper_dump), Supabase’s answer to the ultimate data preservation conundrum.
## Why Paper?[#](https://supabase.com/blog/pg-paper-dump#why-paper)
In the digital era, the threat landscape is constantly evolving, with new vulnerabilities emerging at a pace that's hard to keep up with. While digital backups are the norm, they are susceptible to cyber-attacks, hardware failures, and obsolescence.
This vulnerability led us to think outside the digital box and into a realm that is impervious to hacking, immune to electromagnetic pulses, and resistant to time itself: physical paper.
![Historical Paper Backup on Papyrus](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-04-01-pg-paper-dump%2Fhistorical-paper-backup.webp&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Historical data backup on Papyrus that inspired `pg_paper_dump`.
## How does `pg_paper_dump` work?[#](https://supabase.com/blog/pg-paper-dump#how-does-pg_paper_dump-work)
### Backup Process[#](https://supabase.com/blog/pg-paper-dump#backup-process)
  1. **Select Your Data:** Choose the databases you wish to back up with `pg_paper_dump`.
  2. **Encode and Print:** Our system encodes your data with Comic Sans and prints it onto durable paper.
  3. **Secure Storage:** We store your paper backups in a location of your choice or utilize our secure Arctic Vault for maximum security.


### Restoration Process[#](https://supabase.com/blog/pg-paper-dump#restoration-process)
  1. **Select your recovery point:** Thanks to point-in-time recovery, we can restore your data up until any specific page.
  2. **Restore:** Our Mechanical Turks are trained to decode data encoded in Comic Sans and will input your data with reasonable human-accuracy into your destination database.


### Scaling data preservation with containers[#](https://supabase.com/blog/pg-paper-dump#scaling-data-preservation-with-containers)
Our Analog Engineering team has developed a container orchestration protocol to coordinate the backup and restore process of large databases.
![Scaling analog data preservation with container orchetration](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-04-01-pg-paper-dump%2Fpaper-container.jpeg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Who is pg_paper_dump for?[#](https://supabase.com/blog/pg-paper-dump#who-is-pg_paper_dump-for)
  * Companies that use fax machines.
  * Future SOC 4 compliant companies.
  * [Vogons](https://en.m.wikipedia.org/wiki/Vogon).


## Features and Benefits[#](https://supabase.com/blog/pg-paper-dump#features-and-benefits)
  * **Security:** Provides a level of security that is fundamentally beyond the reach of digital vulnerabilities.
  * **Eco-conscious:** Our materials are selected for minimal environmental impact without compromising on durability or legibility.
  * **Simplicity of Restoration:** When the time comes, restoring your data is as simple as taking the printed codes and typing them back into Supabase’s SQL editor.


## Availability[#](https://supabase.com/blog/pg-paper-dump#availability)
[Sign up](https://forms.supabase.com/pg-paper-dump) for our open beta to get access to `pg_paper_dump` now or try it out our self-hosted solution.
As all of our products, we have open-sourced the code and made it available to the public to be used without any restrictions [here](https://github.com/supabase-community/pg_paper_dump).
## The Future is Here[#](https://supabase.com/blog/pg-paper-dump#the-future-is-here)
We are offering a bridge between these worlds, providing a backup solution that stands the test of time. Join us in redefining data security and making history, one sheet at a time.
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-paper-dump&text=Announcing%20Data%20Preservation%20Service)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-paper-dump&text=Announcing%20Data%20Preservation%20Service)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-paper-dump&t=Announcing%20Data%20Preservation%20Service)
[Last postPostgres Roles and Privileges11 April 2024](https://supabase.com/blog/postgres-roles-and-privileges)
[Next postImplementing semantic image search with Amazon Titan and Supabase Vector26 March 2024](https://supabase.com/blog/semantic-image-search-amazon-bedrock)
[announcements](https://supabase.com/blog/tags/announcements)
On this page
  * [Why Paper?](https://supabase.com/blog/pg-paper-dump#why-paper)
  * [How does `pg_paper_dump` work?](https://supabase.com/blog/pg-paper-dump#how-does-pg_paper_dump-work)
    * [Backup Process](https://supabase.com/blog/pg-paper-dump#backup-process)
    * [Restoration Process](https://supabase.com/blog/pg-paper-dump#restoration-process)
    * [Scaling data preservation with containers](https://supabase.com/blog/pg-paper-dump#scaling-data-preservation-with-containers)
  * [Who is pg_paper_dump for?](https://supabase.com/blog/pg-paper-dump#who-is-pg_paper_dump-for)
  * [Features and Benefits](https://supabase.com/blog/pg-paper-dump#features-and-benefits)
  * [Availability](https://supabase.com/blog/pg-paper-dump#availability)
  * [The Future is Here](https://supabase.com/blog/pg-paper-dump#the-future-is-here)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-paper-dump&text=Announcing%20Data%20Preservation%20Service)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-paper-dump&text=Announcing%20Data%20Preservation%20Service)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-paper-dump&t=Announcing%20Data%20Preservation%20Service)
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

