---
url: https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas
scraped_at: 2025-05-25T09:16:59.431018
title: Manage Read Replica usage | Supabase Docs
---

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Main menu
[Platform](https://supabase.com/docs/guides/platform)
Add-ons
  * [Custom Domains](https://supabase.com/docs/guides/platform/custom-domains)
  * [Database Backups](https://supabase.com/docs/guides/platform/backups)
  * [IPv4 Address](https://supabase.com/docs/guides/platform/ipv4-address)
  * [Read Replicas](https://supabase.com/docs/guides/platform/read-replicas)
Upgrades & Migrations
  * [Upgrading](https://supabase.com/docs/guides/platform/upgrading)
  * [Migrating within Supabase](https://supabase.com/docs/guides/platform/migrating-within-supabase)
  * [Migrating to Supabase](https://supabase.com/docs/guides/platform/migrating-to-supabase)
Project & Account Management
  * [Access Control](https://supabase.com/docs/guides/platform/access-control)
  * [Multi-factor Authentication](https://supabase.com/docs/guides/platform/multi-factor-authentication)
  * [Transfer Project](https://supabase.com/docs/guides/platform/project-transfer)
  * [Single Sign-On](https://supabase.com/docs/guides/platform/sso)
Platform Configuration
  * [Regions](https://supabase.com/docs/guides/platform/regions)
  * [Compute and Disk](https://supabase.com/docs/guides/platform/compute-and-disk)
  * [Database Size](https://supabase.com/docs/guides/platform/database-size)
  * [HIPAA Projects](https://supabase.com/docs/guides/platform/hipaa-projects)
  * [Network Restrictions](https://supabase.com/docs/guides/platform/network-restrictions)
  * [Performance Tuning](https://supabase.com/docs/guides/platform/performance)
  * [SSL Enforcement](https://supabase.com/docs/guides/platform/ssl-enforcement)
  * [Default Platform Permissions](https://supabase.com/docs/guides/platform/permissions)
Billing
  * [About billing on Supabase](https://supabase.com/docs/guides/platform/billing-on-supabase)
  * [Get set up for billing](https://supabase.com/docs/guides/platform/get-set-up-for-billing)
  * [Manage your subscription](https://supabase.com/docs/guides/platform/manage-your-subscription)
  * [Manage your usage](https://supabase.com/docs/guides/platform/manage-your-usage)
  * [Compute](https://supabase.com/docs/guides/platform/manage-your-usage/compute)
  * [Egress](https://supabase.com/docs/guides/platform/manage-your-usage/egress)
  * [Disk Size](https://supabase.com/docs/guides/platform/manage-your-usage/disk-size)
  * [Disk Throughput](https://supabase.com/docs/guides/platform/manage-your-usage/disk-throughput)
  * [Disk IOPS](https://supabase.com/docs/guides/platform/manage-your-usage/disk-iops)
  * [Monthly Active Users](https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users)
  * [Monthly Active Third-Party Users](https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users-third-party)
  * [Monthly Active SSO Users](https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users-sso)
  * [Storage Size](https://supabase.com/docs/guides/platform/manage-your-usage/storage-size)
  * [Storage Image Transformations](https://supabase.com/docs/guides/platform/manage-your-usage/storage-image-transformations)
  * [Edge Function Invocations](https://supabase.com/docs/guides/platform/manage-your-usage/edge-function-invocations)
  * [Realtime Messages](https://supabase.com/docs/guides/platform/manage-your-usage/realtime-messages)
  * [Realtime Peak Connections](https://supabase.com/docs/guides/platform/manage-your-usage/realtime-peak-connections)
  * [Custom Domains](https://supabase.com/docs/guides/platform/manage-your-usage/custom-domains)
  * [Point-in-Time Recovery](https://supabase.com/docs/guides/platform/manage-your-usage/point-in-time-recovery)
  * [IPv4](https://supabase.com/docs/guides/platform/manage-your-usage/ipv4)
  * [MFA Phone](https://supabase.com/docs/guides/platform/manage-your-usage/advanced-mfa-phone)
  * [Read Replicas](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas)
  * [Branching](https://supabase.com/docs/guides/platform/manage-your-usage/branching)
  * [Log Drains](https://supabase.com/docs/guides/platform/manage-your-usage/log-drains)
  * [Your monthly invoice](https://supabase.com/docs/guides/platform/your-monthly-invoice)
  * [Control your costs](https://supabase.com/docs/guides/platform/cost-control)
  * [Credits](https://supabase.com/docs/guides/platform/credits)
  * [Billing FAQ](https://supabase.com/docs/guides/platform/billing-faq)


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Platform
  1. [Platform](https://supabase.com/docs/guides/platform)
  2. More
  3. [Manage your usage](https://supabase.com/docs/guides/platform/manage-your-usage)
  4. [Read Replicas](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas)


Manage Read Replica usage
## What you are charged for[#](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#what-you-are-charged-for)
Each [Read Replica](https://supabase.com/docs/guides/platform/read-replicas) is a dedicated database. You are charged for its resources: [Compute](https://supabase.com/docs/guides/platform/compute-and-disk#compute), [Disk Size](https://supabase.com/docs/guides/platform/database-size#disk-size), provisioned [Disk IOPS](https://supabase.com/docs/guides/platform/compute-and-disk#provisioned-disk-throughput-and-iops), provisioned [Disk Throughput](https://supabase.com/docs/guides/platform/compute-and-disk#provisioned-disk-throughput-and-iops), and [IPv4](https://supabase.com/docs/guides/platform/ipv4-address).
## How charges are calculated[#](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#how-charges-are-calculated)
Read Replica charges are the total of the charges listed below.
**Compute** Compute is charged by the hour, meaning you are charged for the exact number of hours that a Read Replica is running and, therefore, incurring Compute usage. If a Read Replica runs for part of an hour, you are still charged for the full hour.
Read Replicas run on the same Compute size as the primary database.
**Disk Size** Refer to [Manage Disk Size usage](https://supabase.com/docs/guides/platform/manage-your-usage/disk-size) for details on how charges are calculated. The disk size of a Read Replica is 1.25x the size of the primary disk to account for WAL archives. With a Read Replica you go beyond your subscription plan's quota for Disk Size.
**Provisioned Disk IOPS (optional)** Read Replicas inherit any additional provisioned Disk IOPS from the primary database. Refer to [Manage Disk IOPS usage](https://supabase.com/docs/guides/platform/manage-your-usage/disk-iops) for details on how charges are calculated.
**Provisioned Disk Throughput (optional)** Read Replicas inherit any additional provisioned Disk Throughput from the primary database. Refer to [Manage Disk Throughput usage](https://supabase.com/docs/guides/platform/manage-your-usage/disk-throughput) for details on how charges are calculated.
**IPv4 (optional)** If the primary database has a configured IPv4 address, its Read Replicas are also assigned one, with charges for each. Refer to [Manage IPv4 usage](https://supabase.com/docs/guides/platform/manage-your-usage/ipv4) for details on how charges are calculated.
### Usage on your invoice[#](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#usage-on-your-invoice)
Compute incurred by Read Replicas is shown as "Replica Compute Hours" on your invoice. Disk Size, Disk IOPS, Disk Throughput and IPv4 are not shown separately for Read Replicas and are rolled up into the project.
## Billing examples[#](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#billing-examples)
### No additional resources configured[#](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#no-additional-resources-configured)
The project has one Read Replica and no IPv4 and no additional Disk IOPS and Disk Throughput configured.
Line Item| Units| Costs  
---|---|---  
Pro Plan| 1| $25  
| |   
Compute Hours Small Project 1| 744 hours| $15  
Disk Size Project 1| 8 GB| $0  
| |   
Compute Hours Small Replica| 744 hours| $15  
Disk Size Replica| 10 GB| $1.25  
| |   
**Subtotal**| | **$56.25**  
Compute Credits| | -$10  
**Total**| | **$46.25**  
### Additional resources configured[#](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#additional-resources-configured)
The project has two Read Replicas and IPv4 and additional Disk IOPS and Disk Throughput configured.
Line Item| Units| Costs  
---|---|---  
Pro Plan| 1| $25  
| |   
Compute Hours Large Project 1| 744 hours| $110  
Disk Size Project 1| 8 GB| $0  
Disk IOPS Project 1| 3600| $14.40  
Disk Throughput Project 1| 200 MB/s| $7.13  
IPv4 Hours Project 1| 744 hours| $4  
| |   
Compute Hours Large Replica 1| 744 hours| $110  
Disk Size Replica 1| 10 GB| $1.25  
Disk IOPS Replica 1| 3600| $14.40  
Disk Throughput Replica 1| 200 MB/s| $7.13  
IPv4 Hours Replica 1| 744 hours| $4  
| |   
Compute Hours Large Replica 2| 744 hours| $110  
Disk Size Replica 2| 10 GB| $1.25  
Disk IOPS Replica 2| 3600| $14.40  
Disk Throughput Replica 2| 200 MB/s| $7.13  
IPv4 Hours Replica 2| 744 hours| $4  
| |   
**Subtotal**| | **$434.09**  
Compute Credits| | -$10  
**Total**| | **$424.09**  
## FAQ[#](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#faq)
### Do Compute Credits apply to Read Replica Compute?[#](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#do-compute-credits-apply-to-read-replica-compute)
No, Compute Credits do not apply to Read Replica Compute.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/platform/manage-your-usage/read-replicas.mdx)
### Is this helpful?
No Yes
### On this page
[What you are charged for](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#what-you-are-charged-for)[How charges are calculated](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#how-charges-are-calculated)[Usage on your invoice](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#usage-on-your-invoice)[Billing examples](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#billing-examples)[No additional resources configured](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#no-additional-resources-configured)[Additional resources configured](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#additional-resources-configured)[FAQ](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#faq)[Do Compute Credits apply to Read Replica Compute?](https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas#do-compute-credits-apply-to-read-replica-compute)
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings



