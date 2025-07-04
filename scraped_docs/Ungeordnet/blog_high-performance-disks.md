---
url: https://supabase.com/blog/high-performance-disks
scraped_at: 2025-05-25T09:28:58.469666
title: High Performance Disk
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
# High Performance Disk
05 Dec 2024
•
4 minute read
[![Paul Cioanca avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fpcnc.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CioancaEngineering](https://github.com/pcnc)
[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Jonny Summers-MuirProduct Design](https://github.com/mildtomato)
[![Greg Papas avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsayil.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Greg PapasProduct](https://github.com/sayil)
![High Performance Disk](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fhigh-performance-disks%2Fthumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
High Performance disks store up to 60 TB of data with 100x improved durability, and provision up to 5x more IOPS than the default disks we offer.
## A Two-Pronged Approach to Disk Scalability[#](https://supabase.com/blog/high-performance-disks#a-two-pronged-approach-to-disk-scalability)
We've been tackling disk scalability from two angles. On the software side, our implementation of [Oriole DB's index-organized tables](https://www.orioledb.com/blog/orioledb-beta7-benchmarks) significantly reduces disk I/O operations, improving performance without additional hardware resources.
On the infrastructure side we've added new disk options that allow for advanced scaling of your Postgres databases.
## Expanded Capacity[#](https://supabase.com/blog/high-performance-disks#expanded-capacity)
One of the most significant improvements is our increased storage capacity. We've moved beyond our previous 16 TB limit, now offering up to 60 TB of storage for your largest databases. But with greater capacity comes the need for enhanced performance - particularly in how quickly your database can read and write data. This makes IOPS (Input/Output Operations Per Second) especially important.
To address these needs, our new High Performance disks can handle up to 80,000 IOPS - a 5x increase from the 16,000 IOPS limit of our General Purpose disks.
## Understanding Performance: IOPS and Throughput[#](https://supabase.com/blog/high-performance-disks#understanding-performance-iops-and-throughput)
IOPS is a critical metric that measures how many read and write operations your database can perform each second. Think of it as the "speed limit" for your database's ability to access stored data. Higher IOPS means faster database operations, which translates to better application performance, especially for data-intensive workloads.
Throughput, measured in MiB/s (Mebibytes per second), is equally important as it determines how much total data can flow through your disk at once. While IOPS tells you how many individual read/write operations can happen per second, throughput determines the total volume of data that can be moved. With our General Purpose disks, you start with a baseline throughput of 125 MiB/s, which can be provisioned up to 1,000 MiB/s. Our High Performance disks automatically scale throughput with IOPS, providing better performance for data-intensive workloads.
Effective throughput and IOPS also depends on your compute instance size. You can read more about these interdependencies in our [compute and disk documentation](https://supabase.com/docs/guides/platform/compute-and-disk#compute-size).
## Durability: Keeping Your Data Safe[#](https://supabase.com/blog/high-performance-disks#durability-keeping-your-data-safe)
Another benefit of our High Performance disks is increased durability. Our new disks offer 99.999% durability, a 100x increase over our standard disk. This means that if you use High Performance Disk, you will almost never need to worry about disk failure — say goodbye to recovery from backups.
## Consolidated Disk and Compute User Interface[#](https://supabase.com/blog/high-performance-disks#consolidated-disk-and-compute-user-interface)
With these advanced options comes complexity—both in the number of options available, and how they interplay with compute settings. To address this we've redesigned our disk management interface to coexist and interoperate with our compute upgrade UI. When designing the new UI, we adhered to the following principles:
### Transparent Billing[#](https://supabase.com/blog/high-performance-disks#transparent-billing)
  * Real-time cost updates as you adjust your disk configuration


![Real-time cost updates as you adjust your disk configuration](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fhigh-performance-disks%2Fhigh-performance-disks-billing-1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
  * Clear breakdown of how each change affects your bill


![Clear breakdown of how each change affects your bill](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fhigh-performance-disks%2Fhigh-performance-disks-billing-2.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Updated Disk Size Insights[#](https://supabase.com/blog/high-performance-disks#updated-disk-size-insights)
The Disk Size Usage graph breaks down the space used by the Database, Write-Ahead Log, and the System, rather than simply showing "used space."
![Updated disk size insights](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fhigh-performance-disks%2Fhigh-performance-disks-insights.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Preventing Footguns[#](https://supabase.com/blog/high-performance-disks#preventing-footguns)
Effective IOPS is limited by both your compute add-on and disk configuration and it is technically possible to over provision the disk throughput and IOPS with the instance not being able to make full use of it. For example, to achieve maximum IOPS (80,000), you'll need a 16XL or larger compute instance. The dashboard warns you when it detects scenarios like these.
![Preventing footguns](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fhigh-performance-disks%2Fhigh-performance-disks-footgun.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Pricing[#](https://supabase.com/blog/high-performance-disks#pricing)
The pricing for High Performance Disk starts at $0.195 per GB, and you can provision IOPS at $0.119 per IOPS. The storage pricing for General Purpose disks remains unchanged, and you can provision IOPS at $0.024 per IOPS and 0.095$ per Mbps throughput.
For more details on pricing breakdown vs. General Purpose Disk, check out our [pricing page](https://supabase.com/pricing).
## Getting Started[#](https://supabase.com/blog/high-performance-disks#getting-started)
Ready to try out our new disk options? Visit [Compute and Disk](https://supabase.com/dashboard/project/_/settings/compute-and-disk) in the Supabase Dashboard.
We're excited to see what you'll build with these new capabilities. As always, we're committed to providing the tools you need to scale your applications effectively while maintaining the simplicity and developer experience you've come to expect from Supabase.
[Launch Week13](https://supabase.com/launch-week/13)
2-6 December 24
[Day 1 -Supabase AI Assistant v2](https://supabase.com/blog/supabase-ai-assistant-v2)[Day 2 -Supabase Functions: Background Tasks and WebSockets](https://supabase.com/blog/edge-functions-background-tasks-websockets)[Day 3 -Supabase Cron: Schedule Recurring Jobs in Postgres](https://supabase.com/blog/supabase-cron)[Day 4 -Supabase Queues](https://supabase.com/blog/supabase-queues)[Day 5 -database.build v2: Bring-Your-Own-LLM](https://supabase.com/blog/database-build-v2)

Build Stage
[01 -OrioleDB Public Alpha](https://supabase.com/blog/orioledb-launch)[02 -Supabase CLI v2: Config as Code](https://supabase.com/blog/cli-v2-config-as-code)[03 -High Performance Disks](https://supabase.com/blog/high-performance-disks)[04 -Restore to a New Project](https://supabase.com/blog/restore-to-a-new-project)[05 -Hack the Base! with Supabase](https://supabase.com/blog/hack-the-base)[Community Meetups](https://supabase.com/events?category=meetup)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhigh-performance-disks&text=High%20Performance%20Disk)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhigh-performance-disks&text=High%20Performance%20Disk)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fhigh-performance-disks&t=High%20Performance%20Disk)
[Last postSupabase Queues5 December 2024](https://supabase.com/blog/supabase-queues)
[Next postSupabase Cron4 December 2024](https://supabase.com/blog/supabase-cron)
[launch-week](https://supabase.com/blog/tags/launch-week)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [A Two-Pronged Approach to Disk Scalability](https://supabase.com/blog/high-performance-disks#a-two-pronged-approach-to-disk-scalability)
  * [Expanded Capacity](https://supabase.com/blog/high-performance-disks#expanded-capacity)
  * [Understanding Performance: IOPS and Throughput](https://supabase.com/blog/high-performance-disks#understanding-performance-iops-and-throughput)
  * [Durability: Keeping Your Data Safe](https://supabase.com/blog/high-performance-disks#durability-keeping-your-data-safe)
  * [Consolidated Disk and Compute User Interface](https://supabase.com/blog/high-performance-disks#consolidated-disk-and-compute-user-interface)
    * [Transparent Billing](https://supabase.com/blog/high-performance-disks#transparent-billing)
    * [Updated Disk Size Insights](https://supabase.com/blog/high-performance-disks#updated-disk-size-insights)
    * [Preventing Footguns](https://supabase.com/blog/high-performance-disks#preventing-footguns)
  * [Pricing](https://supabase.com/blog/high-performance-disks#pricing)
  * [Getting Started](https://supabase.com/blog/high-performance-disks#getting-started)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhigh-performance-disks&text=High%20Performance%20Disk)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhigh-performance-disks&text=High%20Performance%20Disk)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fhigh-performance-disks&t=High%20Performance%20Disk)
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

