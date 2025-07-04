---
url: https://supabase.com/blog/restore-to-a-new-project
scraped_at: 2025-05-25T08:35:18.648053
title: Restore to a New Project
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
# Restore to a New Project
06 Dec 2024
•
3 minute read
[![Paul Caselton avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fcrispy1975.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CaseltonEngineering](https://github.com/crispy1975)
![Restore to a New Project](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Frestore-to-a-new-project%2Fthumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we’re adding [Restore to a New Project](https://supabase.com/docs/guides/platform/backups#restore-to-a-new-project).
You can use this new tool to copy data easily from an existing Supabase project to a new one. **Restore to a New Project** integrates seamlessly with daily physical backups and Point-in-Time Recovery (PITR) to provide flexible restoration options.
Restore to a New Project requires physical backups to be enabled. It is available to all customers on a paid plan.
## How it Works[#](https://supabase.com/blog/restore-to-a-new-project#how-it-works)
When physical backups are enabled, Supabase triggers daily backups of project data. You can use this backup to restore to a new Supabase project. The new project should match the original project attributes:
  * Size of compute instance.
  * Disk settings; volume type, size, IOPS, and throughput.
  * SSL enforcement configuration.
  * Network restrictions.
  * Cloud region.


After launching your restored project, the rest of the process is automated. The length of time for a new project to provision will depend on the size of the source dataset.
The new project will be available in the Supabase Dashboard as soon as the copy process has completed. This project will behave as any other Supabase project and is completely independent of the source.
### Point-in-Time Recovery[#](https://supabase.com/blog/restore-to-a-new-project#point-in-time-recovery)
In addition to daily backups it is possible to restore from a project with PITR enabled. This allows for very fine granularity when selecting the desired point to restore from. The process is very similar as with daily backup with the exception of being asked to select a specific time.
## Unlimited Cloning from a Source Project[#](https://supabase.com/blog/restore-to-a-new-project#unlimited-cloning-from-a-source-project)
To ensure maximum flexibility a source project can be _copied_ as many times as required, making the tool perfect for testing, development environments etc. However, please note that cloning from an already cloned project is not currently supported (this is in the works).
New projects created with this process, as with any new Supabase project, will incur the usual compute and disk costs. These costs are displayed ahead of time to ensure there are no surprises.
## Accessing Restore to a New Project[#](https://supabase.com/blog/restore-to-a-new-project#accessing-restore-to-a-new-project)
The Restore to a New Project feature can be found on the Supabase dashboard under [database backups](https://supabase.com/dashboard/project/_/database/backups/restore-to-new-project).
Please be aware that Restore to a New Project is currently in Public Alpha. You can reach out to [Supabase support](https://supabase.help) if you experience any issues.
[Launch Week13](https://supabase.com/launch-week/13)
2-6 December 24
[Day 1 -Supabase AI Assistant v2](https://supabase.com/blog/supabase-ai-assistant-v2)[Day 2 -Supabase Functions: Background Tasks and WebSockets](https://supabase.com/blog/edge-functions-background-tasks-websockets)[Day 3 -Supabase Cron: Schedule Recurring Jobs in Postgres](https://supabase.com/blog/supabase-cron)[Day 4 -Supabase Queues](https://supabase.com/blog/supabase-queues)[Day 5 -database.build v2: Bring-Your-Own-LLM](https://supabase.com/blog/database-build-v2)

Build Stage
[01 -OrioleDB Public Alpha](https://supabase.com/blog/orioledb-launch)[02 -Supabase CLI v2: Config as Code](https://supabase.com/blog/cli-v2-config-as-code)[03 -High Performance Disks](https://supabase.com/blog/high-performance-disks)[04 -Restore to a New Project](https://supabase.com/blog/restore-to-a-new-project)[05 -Hack the Base! with Supabase](https://supabase.com/blog/hack-the-base)[Community Meetups](https://supabase.com/events?category=meetup)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&text=Restore%20to%20a%20New%20Project)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&text=Restore%20to%20a%20New%20Project)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&t=Restore%20to%20a%20New%20Project)
[Last postdatabase.build v2: Bring-your-own-LLM6 December 2024](https://supabase.com/blog/database-build-v2)
[Next postHack the Base! with Supabase6 December 2024](https://supabase.com/blog/hack-the-base)
[cloning](https://supabase.com/blog/tags/cloning)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [How it Works](https://supabase.com/blog/restore-to-a-new-project#how-it-works)
    * [Point-in-Time Recovery](https://supabase.com/blog/restore-to-a-new-project#point-in-time-recovery)
  * [Unlimited Cloning from a Source Project](https://supabase.com/blog/restore-to-a-new-project#unlimited-cloning-from-a-source-project)
  * [Accessing Restore to a New Project](https://supabase.com/blog/restore-to-a-new-project#accessing-restore-to-a-new-project)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&text=Restore%20to%20a%20New%20Project)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&text=Restore%20to%20a%20New%20Project)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&t=Restore%20to%20a%20New%20Project)
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

