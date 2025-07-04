---
url: https://supabase.com/docs/guides/platform/project-transfer
scraped_at: 2025-05-25T08:40:04.330176
title: Project Transfers | Supabase Docs
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
  2. Project & Account Management
  3. [Transfer Project](https://supabase.com/docs/guides/platform/project-transfer)


Project Transfers
You can freely transfer projects between different organizations. Head to your [projects' general settings](https://supabase.com/dashboard/project/_/settings/general) to initiate a project transfer.
![Project Transfer: General Settings](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fproject-transfer-overview--light.png&w=3840&q=75)
![Project Transfer: Confirmation Modal](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fproject-transfer-modal--light.png&w=3840&q=75)
Source organization - the organization the project currently belongs to Target organization - the organization you want to move the project to
## Pre-Requirements[#](https://supabase.com/docs/guides/platform/project-transfer#pre-requirements)
  * You need to be the owner of the source organization.
  * You need to be at least a member of the target organization you want to move the project to.
  * Projects with support tier add-ons cannot be transferred at this point. [Open a support ticket](https://supabase.com/dashboard/support/new?category=billing&subject=Transfer%20project).


## Usage-billing and project add-ons[#](https://supabase.com/docs/guides/platform/project-transfer#usage-billing-and-project-add-ons)
For usage metrics such as disk size, egress or image transformations and project add-ons such as [Compute Add-On](https://supabase.com/docs/guides/platform/compute-add-ons), [Point-In-Time-Recovery](https://supabase.com/docs/guides/platform/backups#point-in-time-recovery), [IPv4](https://supabase.com/docs/guides/platform/ipv4-address), [Log Drains](https://supabase.com/docs/guides/platform/log-drains), [Advanced MFA](https://supabase.com/docs/guides/auth/auth-mfa/phone) or a [Custom Domain](https://supabase.com/docs/guides/platform/custom-domains), the source organization will still be charged for the usage up until the transfer. The charges will be added to the invoice when the billing cycle resets.
The target organization will be charged at the end of the billing cycle for usage after the project transfer.
## Things to watch out for[#](https://supabase.com/docs/guides/platform/project-transfer#things-to-watch-out-for)
  * Transferring a project might come with a short 1-2 minute downtime if you're moving a project from a paid to a Free Plan.
  * You could lose access to certain project features depending on the plan of the target organization, i.e. moving a project from a Pro Plan to a Free Plan.
  * When moving your project to a Free Plan, we also ensure you’re not exceeding your two free project limit. In these cases, it is best to upgrade your target organization to Pro Plan first.
  * You could have less rights on the project depending on your role in the target organization, i.e. you were an Owner in the previous organization and only have a Read-Only role in the target organization.


## Transfer to a different region[#](https://supabase.com/docs/guides/platform/project-transfer#transfer-to-a-different-region)
Note that project transfers are only transferring your projects across an organization and cannot be used to transfer between different regions. To move your project to a different region, see [migrating your project](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects#migrate-your-project).
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/platform/project-transfer.mdx)
### Is this helpful?
No Yes
### On this page
[Pre-Requirements](https://supabase.com/docs/guides/platform/project-transfer#pre-requirements)[Usage-billing and project add-ons](https://supabase.com/docs/guides/platform/project-transfer#usage-billing-and-project-add-ons)[Things to watch out for](https://supabase.com/docs/guides/platform/project-transfer#things-to-watch-out-for)[Transfer to a different region](https://supabase.com/docs/guides/platform/project-transfer#transfer-to-a-different-region)
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


![Project Transfer: Confirmation Modal](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fproject-transfer-modal--light.png&w=1920&q=75)
![Project Transfer: General Settings](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fproject-transfer-overview--light.png&w=1920&q=75)

