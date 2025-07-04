---
url: https://supabase.com/blog/community-day-lw3
scraped_at: 2025-05-25T09:15:53.215749
title: Community Day
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
# Community Day
29 Nov 2021
•
6 minute read
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Community Day](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fcommunity-day%2Fsupabase-oss.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase combines existing open-source tools with our own open-source contributions to provide a delightful experience for developers. As part of this goal we hope to build a community of communities, bringing together developers from many different tools, as well as new developers looking to get involved with open source.
To kick off launch week we want to showcase some of the communities that make up the Supabase community, highlight some of their updates, and celebrate everyone who contributes their time to the Supabase mission.
So let's get cracking, we've got a lot to cover. 🚀
## Open Source Spotlight: Kong API Gateway[#](https://supabase.com/blog/community-day-lw3#open-source-spotlight-kong-api-gateway)
Supabase provides a whole bunch of features that are made up of a [collection of open-source tools](https://supabase.com/docs/guides/getting-started/architecture). To orchestrate these different services and functionalities we use the [Kong API Gateway](https://github.com/Kong/kong).
As a user of our hosted offering you don't really need to know all this, but we love showcasing the amazing open-source tools that we work with, and so we've invited [Vik Gamov](https://twitter.com/gAmUssA) to give you a little intro to [Kong](https://github.com/Kong/kong):
## PostgreSQL 14 updates[#](https://supabase.com/blog/community-day-lw3#postgresql-14-updates)
![Postgres-14](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fwhats-new-in-postgres-14%2Fwhats-new-in-postgres-14-og.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Every web developer knows the importance of choosing a suitable database for building modern apps. Even though NoSQL, NewSQL, and other types of databases have received a great deal of buzz in the last few years, relational database management systems (or RDBMS) are still relevant for several critical business use cases and will likely do so in the foreseeable future. Among the many open-source relational databases available, [PostgreSQL](https://supabase.com/docs/guides/database) is a popular choice among developers. It was named [DBMS of the year in 2020](https://db-engines.com/en/blog_post/85) by DBEngines, and with every release of PostgreSQL new features are available making it easy for developers and administrators to run their apps.
[Gurjeet](https://twitter.com/0xGurjeet), one of our Postgres engineers, has written up a [blogpost](https://supabase.com/blog/whats-new-in-postgres-14) with the most important updates the every dev should know.
## PostgREST 9 updates[#](https://supabase.com/blog/community-day-lw3#postgrest-9-updates)
![PostgREST-9](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fcommunity-day%2Fpostgrest-9-og.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've had a lot of feedback on our Postgres APIs, and we've been hard at work with the [PostgREST team](https://github.com/orgs/PostgREST/people) to improve an already-incredible product.
Some new features include
  * Inner Joins
  * Functions with unnamed parameters
  * PostgreSQL 14 compatibility


From tomorrow, every Supabase project will be on PostgREST 9 (including existing projects).
Read about some of the new features in PostgREST 9 [here](https://supabase.com/blog/postgrest-9).
## New community partner: GitGuardian[#](https://supabase.com/blog/community-day-lw3#new-community-partner-gitguardian)
![gitguardian-supabase-partnership.jpeg](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fcommunity-day%2Fgitguardian-supabase-partnership.jpeg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[As you (hopefully) know](https://supabase.com/docs/learn/auth-deep-dive/auth-deep-dive-jwts#jwts-in-supabase), keeping your service role key secret is a crucial part of securing your database. But we also know that it can be difficult to make sure it stays secret as your team grows and you don't accidentally leak it. To help you with this, [we've partnered with GitGuardian](https://blog.gitguardian.com/the-detector-of-the-month-november-2021/).
GitGuardian helps developers keep 250+ types of secrets out of source code. Their automated secrets detection and remediation solution secures every step of the development life cycle, helping you monitor your code for sensitive data. Read [their blog post](https://blog.gitguardian.com/the-detector-of-the-month-november-2021/) to learn more.
## Auth updates[#](https://supabase.com/blog/community-day-lw3#auth-updates)
![new-oauth-providers.jpg](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fcommunity-day%2Fnew-oauth-providers.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The beauty of building in the open is that the community can get involved in adding new OAuth providers, which is exactly what [@TheHarryET](https://twitter.com/TheHarryET) and [MonsterDeveloper](https://github.com/MonsterDeveloper) have been doing. Thanks to them you can now provide sign-in with [Slack](https://supabase.com/docs/guides/auth/social-login/auth-slack) as well as [Spotify](https://supabase.com/docs/guides/auth/social-login/auth-spotify) to your users, as well as use [MessageBird](https://supabase.com/docs/guides/auth/phone-login/messagebird) for phone auth as an alternative to the existing [Twilio](https://supabase.com/docs/guides/auth/phone-login/twilio) integration.
## SupaSquad updates[#](https://supabase.com/blog/community-day-lw3#supasquad-updates)
The [SupaSquad](https://supabase.com/supasquad) is an official Supabase advocate program where community members help build and manage the Supabase community.
Among many other awesome things, the SupaSquad has been absolutely on fire building [client libraries](https://supabase.com/docs/reference/javascript/installing) for all flavors of backends and environments.
![client-libs.jpg](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fcommunity-day%2Fclient-libs.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Python client library updates[#](https://supabase.com/blog/community-day-lw3#python-client-library-updates)
  * New maintainers [`@Dreinon`](https://github.com/dreinon), [`@anand2312`](https://github.com/anand2312), and [`@leynier`](https://github.com/leynier). 💚
  * `gotrue-py` rewritten and now at feature parity with `gotrue-js`.
  * `postgrest-py` now support synchronous operations as well instead of just asynchronous operations in the past. Also at feature parity with `postgrest-js`.
  * `supabase-py` is now `supabase` (e.g. you do `pip3 install supabase` instead of `pip3 install supabase-py`).
  * Storage is working for the Python client library but it's yet to be extracted out as a standalone lib.


## New tutorials and integration guides[#](https://supabase.com/blog/community-day-lw3#new-tutorials-and-integration-guides)
Our own [Jon Meyers](https://twitter.com/_dijonmusters) and the broader community have been busy creating awesome tutorials and integration guides to help everyone build even more amazing things with Supabase:
  * Jon has added official guides for working with [Auth0](https://supabase.com/partners/integrations/auth0) and [Vercel](https://supabase.com/partners/integrations/vercel),
  * [Jonny Summers-Muir](https://twitter.com/JSummersMuir) has been busy paving the way for [Prisma](https://supabase.com/partners/integrations/prisma), and
  * [Aman Mittal](https://github.com/amandeepmittal) has hooked us up with a guide for [Draftbit](https://supabase.com/partners/integrations/draftbit)!


And below are some of the community one's we've come across recently. If you've created one yourself, please notify us by tagging us in a Tweet!
  * [Supabase & Sveltekit - Build Twitter in 75 minutes](https://youtu.be/mPQyckogDYc)
  * [Supabase Auth With Next.Js 12 Middleware](https://jitsu.com/blog/supabase-nextjs-middleware#what-were-going-to-build)
  * [Vue 3 & Supabase | Workout Tracker App](https://www.youtube.com/watch?v=3tF0fGkd4ho)
  * [Use Supabase Auth with Vue.js 3](https://vueschool.io/articles/vuejs-tutorials/use-supabase-auth-with-vue-js-3/)
  * [Dynamic Jamstack with Stencil and Supabase](https://ionicframework.com/blog/dynamic-jamstack-with-stencil-and-supabase)


## Developer stories[#](https://supabase.com/blog/community-day-lw3#developer-stories)
Anytime we scroll through [madewithsupabase.com](https://www.madewithsupabase.com/) we're absolutely blown away by the awesome things y'all are building with Supabase.
So we reached out to some of our users, requesting a short video to learn more and we were overwhelmed with your gracious submissions. We've started a user stories playlist and we are so excited to see many more of these stories in the future. 💚
And with that, we officially declare Launch Week as open 🥳 Check back [here](https://supabase.com/blog) every day this week to see what new things we are shipping. We can't wait to share them with you 🚀
## Want even more Supabase in your life?[#](https://supabase.com/blog/community-day-lw3#want-even-more-supabase-in-your-life)
![tiktok.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fcommunity-day%2Ftiktok.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've got some stellar swag drops and behind the scenes footage for you on our new [TikTok page](https://www.tiktok.com/@supabase.com). Make sure to follow us there as we'll be giving away some swag randomly to 10 peeps who follow us during launch week!
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcommunity-day-lw3&text=Community%20Day)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcommunity-day-lw3&text=Community%20Day)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcommunity-day-lw3&t=Community%20Day)
[Last postSupabase Studio30 November 2021](https://supabase.com/blog/supabase-studio)
[Next postNew in PostgreSQL 14: What every developer should know28 November 2021](https://supabase.com/blog/whats-new-in-postgres-14)
[launch-week](https://supabase.com/blog/tags/launch-week)[community](https://supabase.com/blog/tags/community)
On this page
  * [Open Source Spotlight: Kong API Gateway](https://supabase.com/blog/community-day-lw3#open-source-spotlight-kong-api-gateway)
  * [PostgreSQL 14 updates](https://supabase.com/blog/community-day-lw3#postgresql-14-updates)
  * [PostgREST 9 updates](https://supabase.com/blog/community-day-lw3#postgrest-9-updates)
  * [New community partner: GitGuardian](https://supabase.com/blog/community-day-lw3#new-community-partner-gitguardian)
  * [Auth updates](https://supabase.com/blog/community-day-lw3#auth-updates)
  * [SupaSquad updates](https://supabase.com/blog/community-day-lw3#supasquad-updates)
  * [New tutorials and integration guides](https://supabase.com/blog/community-day-lw3#new-tutorials-and-integration-guides)
  * [Developer stories](https://supabase.com/blog/community-day-lw3#developer-stories)
  * [Want even more Supabase in your life?](https://supabase.com/blog/community-day-lw3#want-even-more-supabase-in-your-life)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcommunity-day-lw3&text=Community%20Day)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcommunity-day-lw3&text=Community%20Day)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcommunity-day-lw3&t=Community%20Day)
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

