---
url: https://supabase.com/blog/launch-week-x-best-launches
scraped_at: 2025-05-25T09:02:53.703398
title: Top 10 Launches of LWX
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
# Top 10 Launches of LWX
19 Dec 2023
•
6 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Top 10 Launches of LWX](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-best-launches%2Ftop-10-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
This launch week was unique. We had so much content that we decided to do a “main stage”, with five major features, and a “build stage” with additional content. It's a lot to digest, so here are 10 of my favorites.
## Top 10[#](https://supabase.com/blog/launch-week-x-best-launches#top-10)
### #1: We teamed up with Fly[#](https://supabase.com/blog/launch-week-x-best-launches#1-we-teamed-up-with-fly)
We're launching Fly Postgres, a managed Postgres offering by Supabase and [Fly.io](http://fly.io/). Fly's current Postgres offering is unmanaged, so we're working with them to bring the same delightful Postgres experience to Fly.
[Read more](https://supabase.com/blog/postgres-on-fly-by-supabase)
### #2: We launched Supabase Grafana[#](https://supabase.com/blog/launch-week-x-best-launches#2-we-launched-supabase-grafana)
We shipped an open source observability suite for your Supabase project, using Prometheus and Grafana. It collects around 200 metrics and can be deployed to any server.
[Read more](https://github.com/supabase/supabase-grafana)
### #3: pg_graphql now supports Postgres Functions[#](https://supabase.com/blog/launch-week-x-best-launches#3-pg_graphql-now-supports-postgres-functions)
Supabase GraphQL (pg_graphql) 1.4+ supports the most requested feature: Postgres functions a.k.a. User Defined Functions. Execute custom SQL logic within GraphQL queries to support complex server-side operations.
[Read more](https://supabase.com/blog/pg-graphql-postgres-functions)
### #4: Python libs are now stable[#](https://supabase.com/blog/launch-week-x-best-launches#4-python-libs-are-now-stable)
Supabase Python is now stable and ready to use in your Python applications. We've created a few guides and examples to show how easy it is to use Python libraries with existing frameworks like Flask.
[Read more](https://supabase.com/blog/client-libraries-v2)
### #5: Aggregate Functions in PostgREST[#](https://supabase.com/blog/launch-week-x-best-launches#5-aggregate-functions-in-postgrest)
Support for aggregate functions has been much requested feature that went through multiple iterations of design and review. PostgREST 12 was just released and it now supports `avg`, `count`, `max`, `min`, `sum`.
[Read more](https://supabase.com/blog/postgrest-12)
### #6: Supavisor 1.0[#](https://supabase.com/blog/launch-week-x-best-launches#6-supavisor-10)
Supavisor is a cloud-native connection pooler for Postgres, built with Elixir. We've migrated all projects on the platform from pgbouncer to Supavisor. Every new Supabase project launched now gets a Supavisor connection string to use for connection pooling.
[Read more](https://supabase.com/blog/supavisor-postgres-connection-pooler)
### #7: Edge Functions now support Node & NPM[#](https://supabase.com/blog/launch-week-x-best-launches#7-edge-functions-now-support-node--npm)
Edge Functions now natively supports npm modules and Node built-in APIs. You can directly import millions of popular, commonly used npm modules into your Edge Functions.
[Read more](https://supabase.com/blog/edge-functions-node-npm)
### #8: Leaked Password Protection with Have I Been Pwned[#](https://supabase.com/blog/launch-week-x-best-launches#8-leaked-password-protection-with-have-i-been-pwned)
we have integrated the [HaveIBeenPwned.org](https://haveibeenpwned.com/) _Pwned Passwords API_ in Supabase Auth to prevent users from using leaked passwords. This will prevent your users from using a password that has previously been leaked.
[Read more](https://supabase.com/blog/supabase-auth-identity-linking-hooks)
### #9: Supabase Branching[#](https://supabase.com/blog/launch-week-x-best-launches#9-supabase-branching)
Branching gives you a Postgres database for every Pull Request. You can run experimental changes on your branch database, and then merge your changes into production when you're happy with the changes. We're rolling out branching in batches.
[Read more](https://supabase.com/blog/supabase-branching)
### #10: Postgres Read Replicas[#](https://supabase.com/blog/launch-week-x-best-launches#10-postgres-read-replicas)
Read replicas continuously, well, _replicate_ data from a primary database. It contains a constantly-updated copy of the data in your Primary. These are great for distributing data closer to your users to reduce application latency, and for reducing the load on your Primary database.
[Read more](https://supabase.com/blog/introducing-read-replicas)
### Bonus: we dropped an Album[#](https://supabase.com/blog/launch-week-x-best-launches#bonus-we-dropped-an-album)
I made a [bet](https://twitter.com/kiwicopple/status/1664118998169014273) with Sam that we would make an album. Luckily Jon has a side hobby. Check out [supabase.productions](https://supabase.productions/).
## Cool things from the community[#](https://supabase.com/blog/launch-week-x-best-launches#cool-things-from-the-community)
I also wanted to highlight a few things that happened in the community over the past few weeks:
### Local AI Stack with Yoko from a16z[#](https://supabase.com/blog/launch-week-x-best-launches#local-ai-stack-with-yoko-from-a16z)
I caught up with [Yoko](https://twitter.com/stuffyokodraws) from Andreessen Horowitz to chat about the [Local AI stack](https://github.com/ykhli/local-ai-stack) that she developed with Supabase, Ollama, Langchain, and Next.js.
### **Finance integrations with OpenBB**[ #](https://supabase.com/blog/launch-week-x-best-launches#finance-integrations-with-openbb)
Didier explained the origins of [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal), the first financial terminal that is free and fully open source. He shared some details about the integration that he's building with Supabase.
### Offline sync with ElectricSQL[#](https://supabase.com/blog/launch-week-x-best-launches#offline-sync-with-electricsql)
Offline sync is one of the most requested features for Supabase. I caught up with the team at ElectricSQL to learn more about their [integration](https://supabase.com/partners/integrations/electricsql).
### Basejump is like “shadcn for Supabase”[#](https://supabase.com/blog/launch-week-x-best-launches#basejump-is-like-shadcn-for-supabase)
In the past few months, [Tiniscule](https://twitter.com/tiniscule) has been quietly upgrading the [Basejump](https://usebasejump.com/) starter kit for Supabase. I think of it a bit like [shadcn](https://ui.shadcn.com/) for Supabase - super easy to template out a secure, scalable enterprise app. Along the way, he's been developing periphery tooling like [test helpers](https://github.com/usebasejump/supabase-test-helpers), and pushing us to provide better primitives. One of our most common questions is “accounts and permissions?”. [Basejump](https://usebasejump.com) solves that and more.
![Basejumo](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-best-launches%2Fbasejump.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Mockup madness from tldraw[#](https://supabase.com/blog/launch-week-x-best-launches#mockup-madness-from-tldraw)
Oh, and the [tldraw](https://www.tldraw.com/) team have been on an [absolute tear this week](https://twitter.com/tldraw/status/1734624421623521719):
### In case you missed it …[#](https://supabase.com/blog/launch-week-x-best-launches#in-case-you-missed-it-)
  * [Supabase + OpenAI cookbook](https://github.com/openai/openai-cookbook/pull/913)
  * [Self-hosting Supabase on Linode](https://twitter.com/linode/status/1735068344410108170)
  * [k8s is coming](https://github.com/supabase-community/supabase-kubernetes/pull/48)
  * [Bun supports Supabase](https://twitter.com/bunjavascript/status/1734470860755566815)
  * [Svix Webhooks, from Postgres](https://www.svix.com/blog/use-svix-from-supabase/)
  * [Offline support with Powersync](https://www.powersync.com/blog/flutter-tutorial-building-an-offline-first-chat-app-with-supabase-and-powersync)
  * [Lowcode Supabase with Buildship](https://docs.buildship.com/supabase)
  * [Visual programming with Comnoco and Supabase](https://docs.comnoco.com/usecases/Supabase/)


### And finally…[#](https://supabase.com/blog/launch-week-x-best-launches#and-finally)
We wouldn't be anything [without Postgres](https://twitter.com/supabase/status/1735377750788042824?s=20).
![Postgres meme](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-best-launches%2Fpostgres-meme.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Launch Week ![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/launch-week)
11-15 Dec
Main Stage
[Day 1 -Supabase Studio: introducing an **AI Assistant** , **Postgres roles** , and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)[ Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)[Day 3 -Introducing Supabase **Branching** , a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)[Day 4 -Supabase Auth: **Identity Linking** , **Session Control** , **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)[ Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)

Build Stage
[01 -Supabase Album](https://supabase.productions/)[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)[05 -pg_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-x-best-launches&text=Top%2010%20Launches%20of%20LWX)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-x-best-launches&text=Top%2010%20Launches%20of%20LWX)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-x-best-launches&t=Top%2010%20Launches%20of%20LWX)
[Last postLaunch Week X Hackathon Winners4 January 2024](https://supabase.com/blog/launch-week-x-hackathon-winners)
[Next postSupabase Libraries V2: Python, Swift, Kotlin, Flutter, and Typescript15 December 2023](https://supabase.com/blog/client-libraries-v2)
[launch-week](https://supabase.com/blog/tags/launch-week)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [Top 10](https://supabase.com/blog/launch-week-x-best-launches#top-10)
    * [#1: We teamed up with Fly](https://supabase.com/blog/launch-week-x-best-launches#1-we-teamed-up-with-fly)
    * [#2: We launched Supabase Grafana](https://supabase.com/blog/launch-week-x-best-launches#2-we-launched-supabase-grafana)
    * [#3: pg_graphql now supports Postgres Functions](https://supabase.com/blog/launch-week-x-best-launches#3-pg_graphql-now-supports-postgres-functions)
    * [#4: Python libs are now stable](https://supabase.com/blog/launch-week-x-best-launches#4-python-libs-are-now-stable)
    * [#5: Aggregate Functions in PostgREST](https://supabase.com/blog/launch-week-x-best-launches#5-aggregate-functions-in-postgrest)
    * [#6: Supavisor 1.0](https://supabase.com/blog/launch-week-x-best-launches#6-supavisor-10)
    * [#7: Edge Functions now support Node & NPM](https://supabase.com/blog/launch-week-x-best-launches#7-edge-functions-now-support-node--npm)
    * [#8: Leaked Password Protection with Have I Been Pwned](https://supabase.com/blog/launch-week-x-best-launches#8-leaked-password-protection-with-have-i-been-pwned)
    * [#9: Supabase Branching](https://supabase.com/blog/launch-week-x-best-launches#9-supabase-branching)
    * [#10: Postgres Read Replicas](https://supabase.com/blog/launch-week-x-best-launches#10-postgres-read-replicas)
    * [Bonus: we dropped an Album](https://supabase.com/blog/launch-week-x-best-launches#bonus-we-dropped-an-album)
  * [Cool things from the community](https://supabase.com/blog/launch-week-x-best-launches#cool-things-from-the-community)
    * [Local AI Stack with Yoko from a16z](https://supabase.com/blog/launch-week-x-best-launches#local-ai-stack-with-yoko-from-a16z)
    * [**Finance integrations with OpenBB**](https://supabase.com/blog/launch-week-x-best-launches#finance-integrations-with-openbb)
    * [Offline sync with ElectricSQL](https://supabase.com/blog/launch-week-x-best-launches#offline-sync-with-electricsql)
    * [Basejump is like “shadcn for Supabase”](https://supabase.com/blog/launch-week-x-best-launches#basejump-is-like-shadcn-for-supabase)
    * [Mockup madness from tldraw](https://supabase.com/blog/launch-week-x-best-launches#mockup-madness-from-tldraw)
    * [In case you missed it …](https://supabase.com/blog/launch-week-x-best-launches#in-case-you-missed-it-)
    * [And finally…](https://supabase.com/blog/launch-week-x-best-launches#and-finally)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-x-best-launches&text=Top%2010%20Launches%20of%20LWX)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-x-best-launches&text=Top%2010%20Launches%20of%20LWX)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-x-best-launches&t=Top%2010%20Launches%20of%20LWX)
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

