---
url: https://supabase.com/blog/launch-week-14-top-10
scraped_at: 2025-05-25T09:28:51.591365
title: Top 10 Launches of Launch Week 14
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
# Top 10 Launches of Launch Week 14
04 Apr 2025
•
4 minute read
[![Wen Bo Xie avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fw3b6x9.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Wen Bo XieProduct](https://twitter.com/wenboxie)
![Top 10 Launches of Launch Week 14](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fwrap-up%2Fthumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Here are the top 10 launches from the past week.
It was very hard to rank them, they’re all #1s in my book, so I may or may not have enlisted AI to rank them for me. Speaking of AI, make sure to check out #5 and #10.
## #1: Deploy Edge Functions from Dashboard[#](https://supabase.com/blog/launch-week-14-top-10#1-deploy-edge-functions-from-dashboard)
You can now create, test, edit, and deploy Edge Functions directly from the Supabase Dashboard without having to spin up the CLI and Docker. We’ve also included templates for common use cases like uploading files to Supabase Storage, OpenAI proxying, and Stripe WebHooks.
[Read more →](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)
## #2: Realtime Broadcast from Database Scales Database Changes[#](https://supabase.com/blog/launch-week-14-top-10#2-realtime-broadcast-from-database-scales-database-changes)
We’re extended Realtime Broadcast to enable sending messages from database triggers to give you better control over the database change payload while making sure that the workflow is secure and scalable.
[Read more →](https://supabase.com/blog/realtime-broadcast-from-database)
## #3: Route Data API Requests to the Nearest Read Replica[#](https://supabase.com/blog/launch-week-14-top-10#3-route-data-api-requests-to-the-nearest-read-replica)
You can now route your Data API (PostgREST) requests to the nearest Read Replica to minimize network latency. This is available today as the default for all load balancer endpoints.
[Read more →](https://supabase.com/blog/data-api-nearest-read-replica)
## #4: Introducing the Supabase UI Library[#](https://supabase.com/blog/launch-week-14-top-10#4-introducing-the-supabase-ui-library)
Building in a weekend becomes much easier with our official UI Library - a collection of ready-to-use components built on top of [shadcn/ui](https://ui.shadcn.com) and integrated with Supabase products like Auth, Storage, and Realtime.
[Read more →](https://supabase.com/blog/supabase-ui-library)
## #5: Official MCP Server[#](https://supabase.com/blog/launch-week-14-top-10#5-official-mcp-server)
We’re launching an official MCP server so you can connect your favorite AI tools, like Claude and Cursor, with Supabase and perform tasks such as creating projects, fetching project configuration, querying data using SQL queries, and so much more.
[Read more →](https://supabase.com/blog/mcp-server)
## #6: Declarative Schemas for Simpler Database Management[#](https://supabase.com/blog/launch-week-14-top-10#6-declarative-schemas-for-simpler-database-management)
We’re simplifying database management with declarative schemas - version-controlled, source of truth for your database structure in the form of `.sql` files. This reduces errors, maintains consistency across environments, and increases development velocity.
[Read more →](https://supabase.com/blog/declarative-schemas)
## #7: Bringing Clerk Auth to Supabase[#](https://supabase.com/blog/launch-week-14-top-10#7-bringing-clerk-auth-to-supabase)
We’ve been working with the Clerk team to make Clerk a Supabase Third-party Auth integration. This means that users can seamlessly connect Clerk and interact with Supabase and its Data API, Storage, Realtime and Edge Functions services without having to migrate auth providers.
[Read more →](https://supabase.com/blog/clerk-tpa-pricing)
## #8: Postgres Language Server[#](https://supabase.com/blog/launch-week-14-top-10#8-postgres-language-server)
Supabase contributors [psteinroe](https://x.com/psteinroe) and [juleswritescode](https://x.com/juleswritescode) have officially launched a Language Server Protocol (LSP) implementation for Postgres to make SQL tooling more reliable and easier to use. The initial release includes autocompletion, syntax error highlighting, type-checking, and a linter and it’s available today as a VSCode extension and npm package.
[Read more →](https://supabase.com/blog/postgres-language-server)
## #9: Dedicated Poolers[#](https://supabase.com/blog/launch-week-14-top-10#9-dedicated-poolers)
We’re launching a Postgres connection pooler that’s co-located with your database via pgBouncer for better performance and reliability. This is only available on paid plans and gives you three options to connect to your database: direct connections, shared pooler via Supavisor, and dedicated pooler via pgBouncer.
[Read more →](https://supabase.com/blog/dedicated-poolers)
## #10: We Invite AI Builders to Partner With Us[#](https://supabase.com/blog/launch-week-14-top-10#10-we-invite-ai-builders-to-partner-with-us)
Supabase has become the default backend for AI Builders like Lovable, Bolt, and Tempo, and with good reason. We are easy to integrate with, we have all the primitives to build full-stack apps, and we can scale when those apps take off.
We invite more AI Builders to come and integrate with us so their users can build in a weekend and scale to millions.
[Read more →](https://supabase.com/solutions/ai-builders)
## Hackathon Ends April 6[#](https://supabase.com/blog/launch-week-14-top-10#hackathon-ends-april-6)
Make sure you get your submissions in for the hackathon by April 6 at 11:59 PM PT. You can read the announcement [here](https://x.com/supabase/status/1905603458742505516).
[Launch Week 14](https://supabase.com/launch-week)
Mar 31 - Apr 04 '25
[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage
[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)[Community Meetups](https://supabase.com/events?category=meetup)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-14-top-10&text=Top%2010%20Launches%20of%20Launch%20Week%2014)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-14-top-10&text=Top%2010%20Launches%20of%20Launch%20Week%2014)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-14-top-10&t=Top%2010%20Launches%20of%20Launch%20Week%2014)
[Last postPostgreSQL Event Triggers without superuser access8 May 2025](https://supabase.com/blog/event-triggers-wo-superuser)
[Next postSupabase MCP Server4 April 2025](https://supabase.com/blog/mcp-server)
[launch-week](https://supabase.com/blog/tags/launch-week)
On this page
  * [#1: Deploy Edge Functions from Dashboard](https://supabase.com/blog/launch-week-14-top-10#1-deploy-edge-functions-from-dashboard)
  * [#2: Realtime Broadcast from Database Scales Database Changes](https://supabase.com/blog/launch-week-14-top-10#2-realtime-broadcast-from-database-scales-database-changes)
  * [#3: Route Data API Requests to the Nearest Read Replica](https://supabase.com/blog/launch-week-14-top-10#3-route-data-api-requests-to-the-nearest-read-replica)
  * [#4: Introducing the Supabase UI Library](https://supabase.com/blog/launch-week-14-top-10#4-introducing-the-supabase-ui-library)
  * [#5: Official MCP Server](https://supabase.com/blog/launch-week-14-top-10#5-official-mcp-server)
  * [#6: Declarative Schemas for Simpler Database Management](https://supabase.com/blog/launch-week-14-top-10#6-declarative-schemas-for-simpler-database-management)
  * [#7: Bringing Clerk Auth to Supabase](https://supabase.com/blog/launch-week-14-top-10#7-bringing-clerk-auth-to-supabase)
  * [#8: Postgres Language Server](https://supabase.com/blog/launch-week-14-top-10#8-postgres-language-server)
  * [#9: Dedicated Poolers](https://supabase.com/blog/launch-week-14-top-10#9-dedicated-poolers)
  * [#10: We Invite AI Builders to Partner With Us](https://supabase.com/blog/launch-week-14-top-10#10-we-invite-ai-builders-to-partner-with-us)
  * [Hackathon Ends April 6](https://supabase.com/blog/launch-week-14-top-10#hackathon-ends-april-6)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-14-top-10&text=Top%2010%20Launches%20of%20Launch%20Week%2014)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-14-top-10&text=Top%2010%20Launches%20of%20Launch%20Week%2014)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-14-top-10&t=Top%2010%20Launches%20of%20Launch%20Week%2014)
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

