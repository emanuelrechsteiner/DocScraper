---
url: https://supabase.com/blog/beta-november-2021-launch-week-recap
scraped_at: 2025-05-25T09:14:15.092758
title: Supabase Beta November 2021: Launch Week Recap
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
# Supabase Beta November 2021: Launch Week Recap
15 Dec 2021
•
4 minute read
[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Ant WilsonCTO and Co-Founder](https://github.com/awalias)
![Supabase Beta November 2021: Launch Week Recap](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Frelease-nov-2021-cover.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We wrapped up November with Supabase's third Launch Week. It also happens to be 12 months since we moved from alpha to beta.
Here's all the awesome stuff that got shipped during Launch Week...
## Supabase Studio[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#supabase-studio)
We [open sourced the Dashboard](https://supabase.com/blog/supabase-studio) - it's now included in Self-Hosting, and the community are now able to contribute, which is going to help us move even faster! Expect many more updates to the dashboard over the coming weeks and months! [Read the code for yourself.](https://github.com/supabase/supabase/tree/master/studio)
![Supabase Studio](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Fstudio.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## We acquired Logflare[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#we-acquired-logflare)
We were early Logflare users, and found it to be one of the most impressive products we'd ever used. So impressive in fact, that we wanted to offer it's capabilities to our entire user base. You'll now find fully searchable Supabase API and database logs within the dashboard, and we're also in the process of open sourcing the codebase. [Read more about the acquisition](https://supabase.com/blog/supabase-acquires-logflare).
![We acquired Logflare](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Flogflare.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Realtime Row Level Security[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#realtime-row-level-security)
[Security rules now work for Realtime](https://supabase.com/blog/realtime-row-level-security-in-postgresql). All of your row level security policies now work with the realtime API, so you can limit streams and subscriptions on a per user basis (or any configuration you want!).
![Realtime Row Level Security](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Frealtime.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## GraphQL is coming to Supabase[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#graphql-is-coming-to-supabase)
We heard you! And built a Postgres extension for [querying your database with GraphQL](https://supabase.com/blog/pg-graphql). This means that each GraphQL request is resolved by a single SQL statement and hits the theoretical minimum achievable network IO overhead of any GraphQL to SQL resolver.
![GraphQL is coming to Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Fgraphql.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Supabase now runs on PostgreSQL 14[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#supabase-now-runs-on-postgresql-14)
One of the most exciting things to happen in databases this year was the release of PG 14. Which is now the default database used on our hosted platform. Read more here about [why we're so excited about it](https://supabase.com/blog/whats-new-in-postgres-14).
![Supabase now runs on PostgreSQL 14](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Fpg14.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## PostgREST 9.0[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#postgrest-90)
PostgREST is the tool we use to introspect your schema and make your database available over a RESTful API. We also sponsor and help maintain this amazing open source project. Version 9.0 was just released and has also been rolled out to all new and existing Supabase projects on our hosted platform. [Check out the blog post](https://supabase.com/blog/postgrest-9) by Steve Chavez, the maintainer of PostgREST.
![PostgREST 9.0 ](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Fpostgrest9.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Building a SaaS?[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#building-a-saas)
We have [a course for that](https://egghead.io/courses/build-a-saas-product-with-next-js-supabase-and-stripe-61f2bc20). You'll learn how to combine Next.js, Stripe, and Supabase to launch your business in no time at all. It's honestly mind blowing how quickly you can get products out the door with this stack. Oh and it's free.
![Building a SaaS? ](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Fcourse.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## New Storage CDN[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#new-storage-cdn)
Serving your files in no time - Get eye wateringly fast load times for your media files. [Read all about the benefits](https://supabase.com/blog/launch-week-three-friday-five-more-things#supabase-cdn).
![New Storage CDN](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Ftoo_damn_high.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## How we Launch[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#how-we-launch)
We "open sourced" our launch methodology - Learn about how we plan, execute, and retrospect launch weeks internally. [Read the post](https://supabase.com/blog/supabase-how-we-launch). supabase monthly growth
![How we Launch](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Fsupabase-universe.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Community[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#community)
### Highlights[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#highlights)
  * Community Day [blog](https://supabase.com/blog/community-day#new-tutorials-and-integration-guides)
  * The SupaSquad has been busy [blog](https://supabase.com/blog/community-day#supasquad-updates)
  * 10 startups on what they're building with Supabase [video](https://www.youtube.com/watch?v=QAm1x7KaLq4&list=PL5S4mPUpp4OuzQN-a_FY3OZQuYo4NmXvb&t=3s)
  * New official integration guides [blog](https://supabase.com/blog/community-day#new-tutorials-and-integration-guides)
  * Add Supabase in Teta [video](https://www.youtube.com/watch?v=lt-Vebxk-Mk)
  * Auth flow with Remix and Supabase [video](https://www.youtube.com/watch?v=-KiH8feOHSc)
  * Discovering Supabase [video](https://www.youtube.com/watch?v=WToGeMIdoSY)
  * Next.js with Magic Links [blog](https://dev.to/dailydevtips1/authenticating-nextjs-with-supabase-auth-magic-links-363e)
  * Next.js + Auth0 + Supabase [blog](https://auth0.com/blog/using-nextjs-and-auth0-with-supabase/)


### TikTok[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#tiktok)
Supabase is [now on TikTok](https://www.tiktok.com/@supabase.com) - Watch us ship to some questionable beats.
![GitHub](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Ftiktok.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### GitHub[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#github)
We hit 25K stars!! [github.com/supabase/supabase](http://github.com/supabase/supabase)
![GitHub](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-nov%2Fstars.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Get started[#](https://supabase.com/blog/beta-november-2021-launch-week-recap#get-started)
  * Start using Supabase today: **[supabase.com/dashboard](https://supabase.com/dashboard/)**
  * Make sure to **[star us on GitHub](https://github.com/supabase/supabase)**
  * Follow us **[on Twitter](https://twitter.com/supabase)**
  * Subscribe to our **[YouTube channel](https://www.youtube.com/c/supabase)**
  * Become a **[sponsor](https://github.com/sponsors/supabase)**


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-november-2021-launch-week-recap&text=Supabase%20Beta%20November%202021%3A%20Launch%20Week%20Recap)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-november-2021-launch-week-recap&text=Supabase%20Beta%20November%202021%3A%20Launch%20Week%20Recap)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-november-2021-launch-week-recap&t=Supabase%20Beta%20November%202021%3A%20Launch%20Week%20Recap)
[Last postHoliday Hackdays Winners 202117 December 2021](https://supabase.com/blog/holiday-hackdays-winners-2021)
[Next postFive more things3 December 2021](https://supabase.com/blog/launch-week-three-friday-five-more-things)
[release-notes](https://supabase.com/blog/tags/release-notes)
On this page
  * [Supabase Studio](https://supabase.com/blog/beta-november-2021-launch-week-recap#supabase-studio)
  * [We acquired Logflare](https://supabase.com/blog/beta-november-2021-launch-week-recap#we-acquired-logflare)
  * [Realtime Row Level Security](https://supabase.com/blog/beta-november-2021-launch-week-recap#realtime-row-level-security)
  * [GraphQL is coming to Supabase](https://supabase.com/blog/beta-november-2021-launch-week-recap#graphql-is-coming-to-supabase)
  * [Supabase now runs on PostgreSQL 14](https://supabase.com/blog/beta-november-2021-launch-week-recap#supabase-now-runs-on-postgresql-14)
  * [PostgREST 9.0](https://supabase.com/blog/beta-november-2021-launch-week-recap#postgrest-90)
  * [Building a SaaS?](https://supabase.com/blog/beta-november-2021-launch-week-recap#building-a-saas)
  * [New Storage CDN](https://supabase.com/blog/beta-november-2021-launch-week-recap#new-storage-cdn)
  * [How we Launch](https://supabase.com/blog/beta-november-2021-launch-week-recap#how-we-launch)
  * [Community](https://supabase.com/blog/beta-november-2021-launch-week-recap#community)
    * [Highlights](https://supabase.com/blog/beta-november-2021-launch-week-recap#highlights)
    * [TikTok](https://supabase.com/blog/beta-november-2021-launch-week-recap#tiktok)
    * [GitHub](https://supabase.com/blog/beta-november-2021-launch-week-recap#github)
  * [Get started](https://supabase.com/blog/beta-november-2021-launch-week-recap#get-started)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-november-2021-launch-week-recap&text=Supabase%20Beta%20November%202021%3A%20Launch%20Week%20Recap)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-november-2021-launch-week-recap&text=Supabase%20Beta%20November%202021%3A%20Launch%20Week%20Recap)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-november-2021-launch-week-recap&t=Supabase%20Beta%20November%202021%3A%20Launch%20Week%20Recap)
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

