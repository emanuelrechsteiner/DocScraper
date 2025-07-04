---
url: https://supabase.com/blog/supabase-enterprise
scraped_at: 2025-05-25T08:55:26.826234
title: Introducing Supabase Enterprise
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
# Introducing Supabase Enterprise
30 Mar 2022
•
10 minute read
[![Rory Wilding avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Froryw10.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Rory WildingHead of Growth](https://github.com/roryw10)
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Introducing Supabase Enterprise](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fenterprise-day%2Fenterprise-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
As our platform continues its rapid adoption within the developer community, we're seeing a growing segment of users building business-critical applications that require enterprise-grade resilience.
![wells-fargo logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fwells-fargo.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![under-armour logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Funder-armour.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![audi-logo logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Faudi-logo.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![capitalone logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fcapitalone.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![coinbase logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fcoinbase.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![facebook logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Ffacebook.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![github logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fgithub.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![google logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fgoogle.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![gsk logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fgsk.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![hewlett-packard logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fhewlett-packard.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![hubspot logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fhubspot.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![ibm logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fibm.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![instagram logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Finstagram.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![linkedin logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Flinkedin.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![microsoft logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fmicrosoft.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![netflix logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fnetflix.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![notion logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fnotion.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![red-hat logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fred-hat.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![robinhood logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Frobinhood.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![salesforce logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fsalesforce.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![santander logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fsantander.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![shopify logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fshopify.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![squarespace logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Fsquarespace.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![twitter logo](https://supabase.com/_next/image?url=%2Fimages%2Fcompany%2Fcompanies-using-supabase%2Ftwitter.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Enterprise features for everybody[#](https://supabase.com/blog/supabase-enterprise#enterprise-features-for-everybody)
Some features are too good to limit to large customers, so today we're introducing a few enterprise features into the Pro Plan.
### Spend caps[#](https://supabase.com/blog/supabase-enterprise#spend-caps)
To simplify pricing, we've merged the “Pro” and “Pay as you go” plans and introduced monthly spend caps to avoid nasty billing surprises. These changes are to keep Supabase pricing [predictable, transparent, and developer friendly](https://supabase.com/blog/pricing).
When you upgrade to the Pro Plan, spend caps are turned on by default, limiting your per-project costs to $25 per month. We're also retaining our soft limits while we manage the transition to granular spend-caps, so your service will continue to run even if your usage exceeds $25 (we'll contact you directly when you go over the limit). Right now there is a global project spend-cap, and in the future you'll have full control with configurable spend-caps on a “per-feature” basis.
### Database Add-ons[#](https://supabase.com/blog/supabase-enterprise#database-add-ons)
Today we're releasing self-serve Database Add-ons.
What do you do when your project hits production and your userbase is sky-rocketing? Many developers have been asking to scale their projects on-demand. Database Add-ons give everyone this control.
Today, Database Add-ons are available for a small set of customers. We will progressively release this for everyone by the end of next week (Friday 8th April).
### New Log Explorer[#](https://supabase.com/blog/supabase-enterprise#new-log-explorer)
Today we're releasing a brand new [Log Explorer](https://supabase.com/docs/guides/platform/logs) in the Supabase Dashboard. As big advocates of SQL, we've done what any good Postgres fanatics would do - we're giving you the ability to query your logs using SQL. And if you're new to SQL, we have plenty of templates included. This is just one of the exciting features we are releasing through our [Logflare acquisition](https://supabase.com/blog/supabase-acquires-logflare). Log history is available to every Supabase project [1](https://supabase.com/blog/supabase-enterprise#user-content-fn-1):
  * Free Plan: 1 day of log history
  * Pro Plan: 7 days of log history
  * Enterprise Plan: 90 days of log history


### Elixir Livebooks[#](https://supabase.com/blog/supabase-enterprise#elixir-livebooks)
Today we're releasing [Elixir Livebooks for Monitoring](https://github.com/supabase/livebooks), starting with built-in monitoring for PgBouncer, a Postgres connection pooler.
![PGBoucner](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fenterprise-day%2Fpg-bouncer.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
While our default PgBouncer settings work for 98% of our customers, sometimes they require customization for unique load patterns. For example, Supabase is popular with web3 projects where traffic can be very unpredictable - especially when you partner with Snoop Dogg. When [sound.xyz](http://sound.xyz) dropped [an NFT with Snoop](https://www.sound.xyz/snoopdogg/death-row-mix-vol-1), we customized their pooler to handle significant load. Their database handled over 9,000 simultaneously connections from Vercel's serverless API.
> In our MVP, we started with a serverless stack to simplify DevOps. Supabase made it dead simple to get PgBouncer and Postgres running so we could focus on the product.
> As we started hitting scale, they've been crucial to supporting our drops. When Snoop Dogg debuted on Sound, Supabase was able to help us provision our data store to handle the load.
> As we rearchitect our backend stack towards scaled microservices, we can be confident that managing Postgres won't be a bottleneck.
> Supabase takes out the mental effort from our back-end infrastructure so we can focus on our customers needs.
> ![Vignesh - CTO @ sound.xyz avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fvignesh-sound.jpeg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> Vignesh - CTO @ sound.xyz
If you want to monitor your own PgBouncer connections you can easily [spin up a Livebook](https://github.com/supabase/livebooks) on a free [Fly.io](http://fly.io) instance.
## Enterprise Features[#](https://supabase.com/blog/supabase-enterprise#enterprise-features)
With the release of our new Enterprise Plan, we're announcing a tonne of new features for Enterprise customers.
### Point-in-Time Recovery[#](https://supabase.com/blog/supabase-enterprise#point-in-time-recovery)
Disaster Recovery is a critical process for any company, even for the most fault-tolerant products. What happens when you accidentally delete that database column because of a clumsy `where` clause? Even with Supabase's daily backups, a day's worth of data can be lost if disaster strikes at the most inopportune time.
Every Enterprise project on the Supabase platform has access to Point-in-Time Recovery (PITR), allowing projects to recover from a snapshot mere seconds after a disaster. Supabase PITR is powered by [WAL-G](https://github.com/wal-g/wal-g), an open source archival and restoration tool.
### Prometheus Endpoints[#](https://supabase.com/blog/supabase-enterprise#prometheus-endpoints)
![Prometheus](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fenterprise-day%2Fprometheus.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
If you run critical infrastructure you likely use Prometheus to monitor your metrics. We've now exposed a Prometheus compatible endpoint for our Enterprise customers. This allows them to scrape Supabase metrics into their own metrics infrastructure for real-time monitoring and alerting. This makes monitoring Supabase as easy as building with Supabase.
If you want access to the Prometheus Endpoint, [contact the Supabase Enterprise team](https://supabase.com/contact/enterprise) today and we'll get you setup.
### SLAs & Enterprise Support[#](https://supabase.com/blog/supabase-enterprise#slas--enterprise-support)
For our enterprise customers we know that service level agreements and support response times are also critical features. We continue to treat support as an important priority for all plans, though enterprise users require confidence that our response times meet their business needs. We now offer faster response times for Enterprise customers, alongside Priority and Priority Plus support packages for those who need more comprehensive support. You can find further details around our SLAs & support [in our documentation](https://supabase.com/docs/company/sla).
### Enterprise Pricing[#](https://supabase.com/blog/supabase-enterprise#enterprise-pricing)
![enterprise-pricing](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fenterprise-day%2Fenterprise-pricing.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
If you need more information on our Enterprise plan, Pricing, SLAs, Support packages, or want to learn more about how Supabase can meet your scaling needs just [contact us](https://supabase.com/contact/enterprise).
## Coming soon[#](https://supabase.com/blog/supabase-enterprise#coming-soon)
We have a lot more Enterprise features under development, available to early-access customers:
### SOC2[#](https://supabase.com/blog/supabase-enterprise#soc2)
Supabase is now SOC2 Type 1 compliant, as announced during Launch Week 5. You can read all about the process we went through to get there in this [blog post](https://supabase.com/blog/supabase-soc2). Getting the Type 1 certification is just the start, and we will be working on getting certified for SOC2 Type 2 and HIPAA next.
### Log ingestion[#](https://supabase.com/blog/supabase-enterprise#log-ingestion)
Supabase is now ingesting over 4 billion log events every week, just from the Postgres instances we host on the platform. Soon you'll be able to ingest logs and analytics from anywhere directly into your Supabase project.
### Foreign Data Wrappers[#](https://supabase.com/blog/supabase-enterprise#foreign-data-wrappers)
Ingesting your logs is one thing, but what about querying them directly from your PostgreSQL database? What if you can figure out how many API requests one of your users made last month? Or how many gigabytes of video a user streamed from [Supabase Storage](https://supabase.com/storage)? Watch this space!
### Materialized Views[#](https://supabase.com/blog/supabase-enterprise#materialized-views)
Querying huge datasets can be time-consuming, especially when you are aggregating billions of rows of historical logs. Supabase will make this simple with auto-updating views, saved to disk for increased performance. These views update periodically at a cadence that you decide. You'll even be able to fetch these views with your [Supabase API](https://supabase.com/docs/guides/database/api)!
## Next steps[#](https://supabase.com/blog/supabase-enterprise#next-steps)
Get started today with all of our Enterprise Features on [supabase.com/dashboard](https://supabase.com/dashboard), or [contact the Supabase Enterprise team](https://supabase.com/contact/enterprise) if you want to access our Enterprise features.
## Footnotes[#](https://supabase.com/blog/supabase-enterprise#footnote-label)
  1. Updated on May 31 2022 for accuracy: Changed to accurately reflect the log periods we advertise on our [pricing page](https://supabase.com/pricing). [↩](https://supabase.com/blog/supabase-enterprise#user-content-fnref-1)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-enterprise&text=Introducing%20Supabase%20Enterprise)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-enterprise&text=Introducing%20Supabase%20Enterprise)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-enterprise&t=Introducing%20Supabase%20Enterprise)
[Last postEdge Functions are now available in Supabase31 March 2022](https://supabase.com/blog/supabase-edge-functions)
[Next postGraphQL is now available in Supabase29 March 2022](https://supabase.com/blog/graphql-now-available)
[launch-week](https://supabase.com/blog/tags/launch-week)[enterprise](https://supabase.com/blog/tags/enterprise)
On this page
  * [Enterprise features for everybody](https://supabase.com/blog/supabase-enterprise#enterprise-features-for-everybody)
    * [Spend caps](https://supabase.com/blog/supabase-enterprise#spend-caps)
    * [Database Add-ons](https://supabase.com/blog/supabase-enterprise#database-add-ons)
    * [New Log Explorer](https://supabase.com/blog/supabase-enterprise#new-log-explorer)
    * [Elixir Livebooks](https://supabase.com/blog/supabase-enterprise#elixir-livebooks)
  * [Enterprise Features](https://supabase.com/blog/supabase-enterprise#enterprise-features)
    * [Point-in-Time Recovery](https://supabase.com/blog/supabase-enterprise#point-in-time-recovery)
    * [Prometheus Endpoints](https://supabase.com/blog/supabase-enterprise#prometheus-endpoints)
    * [SLAs & Enterprise Support](https://supabase.com/blog/supabase-enterprise#slas--enterprise-support)
    * [Enterprise Pricing](https://supabase.com/blog/supabase-enterprise#enterprise-pricing)
  * [Coming soon](https://supabase.com/blog/supabase-enterprise#coming-soon)
    * [SOC2](https://supabase.com/blog/supabase-enterprise#soc2)
    * [Log ingestion](https://supabase.com/blog/supabase-enterprise#log-ingestion)
    * [Foreign Data Wrappers](https://supabase.com/blog/supabase-enterprise#foreign-data-wrappers)
    * [Materialized Views](https://supabase.com/blog/supabase-enterprise#materialized-views)
  * [Next steps](https://supabase.com/blog/supabase-enterprise#next-steps)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-enterprise&text=Introducing%20Supabase%20Enterprise)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-enterprise&text=Introducing%20Supabase%20Enterprise)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-enterprise&t=Introducing%20Supabase%20Enterprise)
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

