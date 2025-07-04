---
url: https://supabase.com/blog/supabase-reports-and-metrics
scraped_at: 2025-05-25T09:45:20.094507
title: Supabase Reports and Metrics
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
# Supabase Reports and Metrics
29 Jul 2021
•
6 minute read
[![Div Arora avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdarora.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Div AroraEngineering](https://github.com/darora)
![Supabase Reports and Metrics](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-4-reports-and-metrics%2Freports-and-metrics-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase offers a supercharged Postgres instance, along with a set of complementary services, making it easy to build mobile and web applications. Today, we're exposing a full set of metrics in your projects, so that you can build better (and faster) products for your users.
## Reports page[#](https://supabase.com/blog/supabase-reports-and-metrics#reports-page)
We've added a new "Reports" section to the Dashboard. You can view one month of data, including API requests across all of Supabase's core pillars: Database, Auth and Storage. We've included two instance health metrics, CPU usage and Memory usage, with a lot more on the way.
![Supabase reports screen](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-4-reports-and-metrics%2Freports-and-metrics-reports-screen.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
All charts are built with [Recharts](https://recharts.org/en-US), an MIT-licensed React chart library chosen for its ease of use. We'll add customizable charts in the future, so we'd love to hear which libraries you'd like to see in Supabase.
We support one configurable report per project, accessible and editable by all team members. In the next few weeks, we'll expand to unlimited reports, with longer date range options, new layout configurations, report templates, stacked charts and private/public visibility across your project's members.
## New project home page[#](https://supabase.com/blog/supabase-reports-and-metrics#new-project-home-page)
Every project has a new home page with a weekly overview of important metrics. We've included usage bars for Database storage, number of Auth users, and Storage space.
And we're just getting warmed up. Over the next few months you'll see more project information, notifications, and highlights to monitor your project health at a glance.
![Supabase new dashboard app homescreen](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-4-reports-and-metrics%2Freports-and-metrics-homepage.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Observability metrics[#](https://supabase.com/blog/supabase-reports-and-metrics#observability-metrics)
Backend as a Service? Infrastructure as a Service? We don't care about the label, but we do care about giving developers the relevant observability metrics. Supabase gives you a full Postgres cluster for every project, and now we give you the tools to diagnose and manage important infrastructure anomalies.
All databases are now launched with `pg_stat_statements` enabled, so you can expect some useful query statistics in the future too.
![Supabase observability metrics](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-4-reports-and-metrics%2Freports-and-metrics-observability-screen.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Building a metrics pipeline[#](https://supabase.com/blog/supabase-reports-and-metrics#building-a-metrics-pipeline)
"If you can't measure it, you can't improve it."
### Full control, full responsibility[#](https://supabase.com/blog/supabase-reports-and-metrics#full-control-full-responsibility)
When developers build services and applications on top of Supabase, relying on the platform's reliability and performance. Product observability is critical, as it allows developers to make decisions on where to spend their optimization dollars, and to get ahead of possible issues before they become showstoppers.
At Supabase, each project is provisioned with a Postgres cluster, and a suite of associated services that add, ahem, supa-powers to the database.
![Supabase architecture](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-4-reports-and-metrics%2Freports-infra.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Our users get liberal access to each of these services - you can use PostgREST for a RESTful API, Realtime to listen to changes in your Postgres instance, or even just open a raw connection to the database. While this makes for an extremely flexible offering, it presents a diverse cast of [foot-guns](https://en.wiktionary.org/wiki/footgun). Want to mess with Realtime? Why not bulk-insert millions of records on tables you've configured it to watch? Feel like taking out your entire database? Just connect to it and run a wildly inefficient query!
We're continuously rolling out protections to mitigate failure scenarios and to minimize the blast radius. However, given the power and flexibility exposed via our services and the diverse workloads they support, our users remain best positioned to make the call on what's reasonable for their project. As such, we're also working on exposing as much data as possible to them.
### Gathering relevant metrics[#](https://supabase.com/blog/supabase-reports-and-metrics#gathering-relevant-metrics)
Given the setup described above, there are two major categories of metrics that we care about. There are metrics pertinent to the services mentioned ("Project Metrics") that get spun up for each project (e.g. the number of active connections to the db), and there are metrics for the underlying infrastructure (e.g. system health). Most of the time, our users shouldn't have to care about the latter, though the nature of leaky abstractions dictates that sometimes they become relevant to Project Metrics as well.
In order to build a comprehensive view of the project's health, each service needs to be instrumented along with its underlying infrastructure. We're looking at hundreds of thousands of targets at our current scale (likely approaching millions in the near future) each of them presenting hundreds of metrics of interest (every minute!).
To buy ourselves some headroom, we built a federated approach: we run instances of our monitoring systems in each geographical region we operate in. This provides a natural dimension for sharding, while reducing the latency for everyone. We run [Prometheus](https://prometheus.io/) out of inertia, soon to be [VictoriaMetrics](https://victoriametrics.com/). The monitoring instances scrape data from a number of exporters that are bundled into each of our projects. A small subset of the metrics collected gets aggregated to a centralized VictoriaMetrics instance for easier cohort analysis.
![Supabase Prometheus](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-4-reports-and-metrics%2Fprometheus.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Available sources and metrics[#](https://supabase.com/blog/supabase-reports-and-metrics#available-sources-and-metrics)
To start with, we're focusing on metrics a few of the most pertinent metrics:
  * Database metrics: CPU and RAM usage
  * API Requests: Ingress, Egress, `GET`, `POST`, `PATCH`, `PUT`, `OPTIONS`, and all requests.
  * Storage Requests: Ingress, Egress, `GET`, `POST`, `PATCH`, `PUT`, `OPTIONS`, and all requests.
  * Auth Requests: Ingress, Egress, `GET`, `POST`, `PATCH`, `PUT`, `OPTIONS`, and all requests.


## What's next?[#](https://supabase.com/blog/supabase-reports-and-metrics#whats-next)
Where to begin?
  * Multiple reports per project: we've started with just one report per project, but in the next few weeks we'll allow you to create as many as you want.
  * More metrics: we're just getting started. 
    * Number of active connections to your database.
    * Various detailed stats from `pg_stat_statements`, `pg_stat_bgwriter`, `pg_stat_database`, `pg_stat_database_conflicts`.
    * System level metrics like CPU, memory and disk utilization.
  * Granularity: project statistics will come down to hourly.
  * Longer time periods: view historical data going back several months.
  * Interactive widgets: view-only reports are fine, but we wouldn't be a Postgres company if we didn't allow you to write your own SQL queries.


Any other metrics you want to see in your projects? Reach out on our [Discord channel](https://discord.supabase.com/) and give Supabase a try by [creating a project](https://supabase.com/dashboard/).
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-reports-and-metrics&text=Supabase%20Reports%20and%20Metrics)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-reports-and-metrics&text=Supabase%20Reports%20and%20Metrics)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-reports-and-metrics&t=Supabase%20Reports%20and%20Metrics)
[Last postSupabase Swag Store30 July 2021](https://supabase.com/blog/supabase-swag-store)
[Next postMobbin uses Supabase to authenticate 200,000 users28 July 2021](https://supabase.com/blog/mobbin-supabase-200000-users)
[launch-week](https://supabase.com/blog/tags/launch-week)[reports](https://supabase.com/blog/tags/reports)[database](https://supabase.com/blog/tags/database)
On this page
  * [Reports page](https://supabase.com/blog/supabase-reports-and-metrics#reports-page)
  * [New project home page](https://supabase.com/blog/supabase-reports-and-metrics#new-project-home-page)
  * [Observability metrics](https://supabase.com/blog/supabase-reports-and-metrics#observability-metrics)
  * [Building a metrics pipeline](https://supabase.com/blog/supabase-reports-and-metrics#building-a-metrics-pipeline)
    * [Full control, full responsibility](https://supabase.com/blog/supabase-reports-and-metrics#full-control-full-responsibility)
    * [Gathering relevant metrics](https://supabase.com/blog/supabase-reports-and-metrics#gathering-relevant-metrics)
    * [Available sources and metrics](https://supabase.com/blog/supabase-reports-and-metrics#available-sources-and-metrics)
  * [What's next?](https://supabase.com/blog/supabase-reports-and-metrics#whats-next)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-reports-and-metrics&text=Supabase%20Reports%20and%20Metrics)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-reports-and-metrics&text=Supabase%20Reports%20and%20Metrics)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-reports-and-metrics&t=Supabase%20Reports%20and%20Metrics)
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

