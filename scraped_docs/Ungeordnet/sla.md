---
url: http://supabase.com/sla
scraped_at: 2025-05-25T09:28:21.559065
title: Service Level Agreement | Supabase
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
# Service Level Agreements[#](https://supabase.com/sla#service-level-agreements)
## Enterprise Platform Uptime SLA[#](https://supabase.com/sla#enterprise-platform-uptime-sla)
The following Service Level Agreement, which is incorporated into and forms part of the Subscription Agreement between Supabase, Inc. ("Supabase") and Customer (the "Agreement"), will apply to the Services for Enterprise Customers specified in an Order Form during the applicable Subscription Term:
### 1. Uptime Commitment[#](https://supabase.com/sla#1-uptime-commitment)
Supabase will provide Actual Availability for at least ninety-nine and nine tenths percent (99.9%) of the total time in each calendar month during the Subscription Term, as measured by Supabase (the **"Uptime Commitment"**).
### 2. Service Credits[#](https://supabase.com/sla#2-service-credits)
If the Uptime Commitment is not met during any particular calendar month during the Subscription Term, then Customer will be eligible for a service credit ("Service Credit"), provided that Customer reports to Supabase such failure to meet the Uptime Commitment and requests such Service Credit in accordance with this Exhibit. The amount of any Service Credit due hereunder shall be calculated as follows: X * Y, where X = the total fees due from Customer to Supabase for the affected Services for the relevant calendar month (regardless of when billed or payable), and Y = the Credit Percentage corresponding with the Actual Availability provided (as a percentage of total time) for the relevant calendar month, as set forth in the table below.
Actual Availability| Credit Percentage  
---|---  
Less than 99.9% but greater than or equal to 99.0%| 10%  
Less than 99.0% but greater than or equal to 98.0%| 15%  
Less than 98.0% but greater than or equal to 96.0%| 20%  
Less than 96.0%| 30%  
### 3. Credit Requests and Payment[#](https://supabase.com/sla#3-credit-requests-and-payment)
To request a Service Credit, Customer must send an email to Supabase at support@supabase.io within thirty (30) days of the end of the month in which the Uptime Commitment was not met. Customer must include either its account ID or registered email address, and the previously reported dates and times that there was no Service Availability. If Supabase confirms that Customer is eligible for a Service Credit, Supabase will issue a credit to Customer's account within thirty (30) days. Service Credits are not refunds, cannot be exchanged into a cash amount, and may only be used against future billing charges. Except as set forth in Section 4 below, the Service Credits shall be Customer's sole and exclusive remedy, and Supabase's sole and exclusive liability, for any failure by Supabase to meet the Uptime Commitment.
### 4. Definitions[#](https://supabase.com/sla#4-definitions)
All capitalized words used but not defined in this Service Level Agreement have the meaning set forth in the Agreement.
#### 4.1 Scheduled Availability[#](https://supabase.com/sla#41-scheduled-availability)
"Scheduled Availability" means the time, in minutes, that the applicable Services are generally accessible and available to Customer's Permitted Users.
#### 4.2 Unscheduled Downtime[#](https://supabase.com/sla#42-unscheduled-downtime)
"Unscheduled Downtime" means the time, in minutes, that the applicable Services are not generally accessible and available to Customer's Permitted Users, excluding inaccessibility or unavailability due to Customer's or Permitted Users' acts or omissions, force majeure events, scheduled maintenance disclosed with at least 24 hours' notice by email, hacking or virus attacks, reasonable emergency maintenance or other product specific exclusions listed under SLA Exclusions.
#### 4.3 Actual Availability[#](https://supabase.com/sla#43-actual-availability)
"Actual Availability" means Scheduled Availability less Unscheduled Downtime.
#### 4.4 Production[#](https://supabase.com/sla#44-production)
"Production" is defined as a system serving live customer-facing or business systems with existing deployed and functional features.
"Development", "Staging", "uat", "pre-production" or new feature implementation even if in a production environment, are not considered Production.
### SLA Exclusions[#](https://supabase.com/sla#sla-exclusions)
#### General Service Exclusions[#](https://supabase.com/sla#general-service-exclusions)
  * (i) Caused by factors outside of our reasonable control, including but not limited to any force majeure event or Internet access, ISP provider issues, and/or related problems beyond the demarcation point of Supabase. For the avoidance of doubt, this list is not exhaustive, and we will endeavor to inform you if the issue is beyond a factor that we can reasonably control.
  * (ii) That result from any voluntary actions or inactions from you.
  * (iii) That result from instance class CPU and memory resource limitations.
  * (iv) That result from you not following the basic operational guidelines described in our [Docs](https://supabase.com/docs) (e.g., overloading a database instance to the point it is inoperable, creating an excessively large number of tables that significantly increase the recovery time, etc.).
  * (vi) That result in a long recovery time due to insufficient IO capacity for your database workload.
  * (vii) That result from your equipment, software, or other technology.
  * (viii) Arising from our suspension and termination of your right to use Supabase in accordance with our Terms.


#### Database SLA Exclusions[#](https://supabase.com/sla#database-sla-exclusions)
  * (i) Unofficially supported Postgres extensions are excluded from our SLA.
  * (ii) Our SLA only applies to the 2 most recent major releases of Postgres that Supabase has officially supported. Older versions are excluded.


#### Auth SLA Exclusions[#](https://supabase.com/sla#auth-sla-exclusions)
  * (i) Inappropriately provisioned compute resources related to your project for the expected load on your database and Auth servers, especially in the case of verifying or storing password-based credentials in the sign-in, sign-up, password change, password reset, and other such flows and APIs.
  * (ii) Any accidental or intentional modifications, additions, or deletions of database objects (tables, views, triggers, roles, functions, indexes, constraints, permissions, grants, and similar) in the `auth` schema or foreign key relationships in any schema to non-primary key columns within the `auth` schema that may cause total or partial outage, including outages caused in the future but related to such modifications, additions, or deletions in the past when arising from schema migrations initiated by Supabase.
  * (iii) Total or partial outages caused by third-party services as configured by default or by choice, including and not limited to: OAuth, OpenID Connect, Security Assertion Markup Language servers and related APIs and protocols; Email (via SMTP or otherwise) and SMS sending servers and related APIs; CAPTCHA services and APIs; Password Strength Checking services such as HaveIBeenPwned.org; IP geo-location; and other such services.
  * (iv) Outages caused by overly permissive rate-limiting configurations.
  * (v) Outages caused by email sending issues when using the provisional (default) email sending configuration included with any Supabase project with the intention of getting started but not for production use.
  * (vi) Outages or issues caused by retracted versions of official Supabase libraries, frameworks, software packages (CLI, Docker image, executable, Infrastructure-as-Code plugins, etc.) or APIs, including urgent retractions due to identified security vulnerabilities.
  * (vii) Outages or issues caused by unofficial Supabase client libraries, frameworks, or API proxies, including security vulnerabilities, even when those libraries internally use official Supabase libraries.
  * (viii) Outages or issues that could have been resolved by upgrading to a higher minor or patch version of an official Supabase client library, framework, or software package (CLI, Docker image, executable, Infrastructure-as-Code plugin, etc.).


#### Storage SLA Exclusions[#](https://supabase.com/sla#storage-sla-exclusions)
  * (i) Inappropriately provisioned compute resources related to your project for the expected load on your database.
  * (ii) Low amounts of pgBouncer or Supervisor connection pool configuration, such as max_clients and pool_size, for high amounts of traffic.
  * (iii) Any accidental or intentional modifications, additions, or deletions of database objects (tables, views, triggers, roles, functions, indexes, constraints, permissions, grants, and similar) in the `storage` schema, or foreign key relationships in any schema to non-primary key columns within the `storage` schema, that may cause total or partial outage, including outages caused in the future but related to such modifications, additions, or deletions in the past when arising from schema migrations initiated by Supabase.
  * (iv) Outages or issues that could have been resolved by upgrading to a higher minor or patch version of an official Supabase client library, framework, or software package (CLI, Docker image, executable, Infrastructure-as-Code plugin, etc.).
  * (v) Outages caused by accidental deletions of objects or buckets via the Storage API by the user.


#### Management API SLA Exclusions[#](https://supabase.com/sla#management-api-sla-exclusions)
  * (i) Until the management API reaches General Availability (GA), we cannot provide an uptime commitment.
  * (ii) Personal access tokens getting lost or leaked due to improper maintenance or improper use of confidential information.
  * (iii) Violation of Supabase fair-use policy.


#### Realtime SLA Exclusions[#](https://supabase.com/sla#realtime-sla-exclusions)
  * (i) Inappropriately provisioned compute resources related to your project for the expected load on your database.
  * (ii) The Realtime service does not guarantee messaging deliverability. If you need at-least-once, exactly-once, or at-most-once guarantees, you will need to build this functionality on top of the realtime service.


#### Edge Functions[#](https://supabase.com/sla#edge-functions)
  * (i) **Uptime Commitment Exclusion:** Until Edge Functions reach General Availability (GA), we cannot provide an uptime commitment. Customers acknowledge that the service may experience downtime, interruptions, or performance issues, and no specific availability percentage is promised at this time.


## Support[#](https://supabase.com/sla#support)
Supabase provides Support Service Level Agreements for our Team and Enterprise customers.
### 1. Urgent[#](https://supabase.com/sla#1-urgent)
**Critical Issue**
Defect resulting in full or partial system outage or a condition that makes Supabase unusable or unavailable in production for all of Customer's Users.
### 2. High[#](https://supabase.com/sla#2-high)
**Significant Business Disruption**
Issue resulting in a situation meaning major functionality is impacted and significant performance degradation is experienced. Issue impacts significant proportion of user base and / or major Supabase functionality.
### 3. Normal[#](https://supabase.com/sla#3-normal)
**Minor Feature or Functional Issue / General Question**
Issue results in a component of Supabase not performing as expected or documented. An inquiry by a Customer representative regarding a general technical issue or general question.
### 4. Low[#](https://supabase.com/sla#4-low)
**Minor Issue / Feature Request**
An Information request about Supabase or feature request.
## Target initial response times[#](https://supabase.com/sla#target-initial-response-times)
Severity Level| Team| Enterprise Standard| Priority Plus  
---|---|---|---  
1. Urgent| 24 hours24/7 × 365| 1 hour24/7 × 365| 1 hour24/7 × 365  
2. High| 1 business dayMonday - Friday| 2 business hoursMonday - Friday| 2 hours24/7 × 365  
3. Normal| 1 business dayMonday - Friday| 1 business dayMonday - Friday| 12 hours24/7 x 365  
4. Low| 2 business daysMonday - Friday| 2 business daysMonday - Friday| 24 hours24/7 x 365  
Business hours are from 6am to 6pm (local time), except where otherwise stated.
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

