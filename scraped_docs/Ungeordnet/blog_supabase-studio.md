---
url: https://supabase.com/blog/supabase-studio
scraped_at: 2025-05-25T08:38:20.383329
title: Supabase Studio
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
# Supabase Studio
30 Nov 2021
•
4 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Supabase Studio](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fstudio%2Fopen-source-studio-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we're releasing [Supabase Studio](https://github.com/supabase/supabase/tree/master/studio). The same Dashboard that you're using on our Platform is now available for [Local Development](https://supabase.com/docs/guides/local-development) and [Self-Hosting](https://supabase.com/docs/guides/hosting/overview).
## Background[#](https://supabase.com/blog/supabase-studio#background)
Let's get the obvious question out of the way - why wasn't it already open source?
When Ant and I started Supabase the codebase was one large monorepo which contained everything from the dashboard to cloud infrastructure code to experimental code. This is our preferred development setup - we like to keep all code in one place so that we have a single source of truth and tightly coupled CI workflows.
The original Dashboard really wasn't much except a couple of buttons which allowed our Alpha users to start and stop a Supabase project - back then only a PostgreSQL connection string.
Then time went on, and we started gaining traction - a lot faster than expected. The nice thing about building for developers is that they are very vocal about the features they want to see next. And so we kept shipping - a SQL editor, a Table view, User management, auto-generated Docs, and everything else you can find on the Dashboard today.
We've been planning to make the Dashboard public for a long time now, starting with [Supabase UI](https://ui.supabase.com/), [`supabase/grid`](https://github.com/supabase/grid), and a standalone [PR](https://github.com/supabase/supabase/pull/2281) for Supabase Studio. But as feature requests kept rolling in it became a Sisyphean task to maintain separate code bases.
After the last Launch Week, we decided to prioritize the Studio.
## Approaches for managing shared codebases[#](https://supabase.com/blog/supabase-studio#approaches-for-managing-shared-codebases)
We investigated a few different approaches used in the open source world. There are three popular strategies that we found amongst OSS projects and some of our YC alum:
  * Maintain separate code bases. Pluck changes from one to another.
  * Keep two repos in sync using some mixture of git submodules or a tool like [copycat](https://github.com/atomix/copycat)
  * Use the same codebase, abstracting platform-specific code behind an API and feature flags.


Our frontend [team](https://github.com/orgs/supabase/teams/frontend/members) experimented with the first two approaches where they plucked (injected, merged, and wrangled) code for our Platform. Time-to-production become a lot slower, an unacceptable outcome at Supabase.
Eventually we decided to open source all the frontend code, a shared codebase for both the Platform and Self Hosting.
Special shout out
Sentry do a fantastic job of [ documenting their strategy ](https://develop.sentry.dev/sentry-vs-getsentry/) for managing a shared codebase and served as a great model for Supabase.
## Build in public[#](https://supabase.com/blog/supabase-studio#build-in-public)
For the past week, the dashboard you've been using on the Platform has been deployed from our [main repository](https://github.com/supabase/supabase/tree/master/studio).
This fits one of our core philosophies at Supabase: do less. Less code to manage means less bugs. Fewer codebases means faster shipping.
![Open Source Table Editor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fstudio%2Fopen-source-studio-table-editor.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
It also fits the development philosophy of every other part of Supabase: building in public, "warts and all".
This is a huge step forward for the community. Supabase users can now spot a bug, fix it in the open source repository, and have it shipped to both the Platform and Self-Hosted environments - all in a few hours.
## Technical details[#](https://supabase.com/blog/supabase-studio#technical-details)
Let's jump into some of the technical implementation for Supabase Studio.
### Tech stack[#](https://supabase.com/blog/supabase-studio#tech-stack)
Studio is a Javascript application with a few key pieces of technology:
  * [Next.js](https://nextjs.org/) - A frontend Javascript framework built with React.
  * [Tailwind](https://tailwindcss.com/) - A utility-first CSS framework.
  * [Supabase UI](https://ui.supabase.com/) - Our own component library.
  * [MobX](https://www.mobxjs.com/) - A state management library.
  * A host of other [useful libraries](https://github.com/supabase/supabase/blob/master/studio/package.json), including [Radix UI](https://www.radix-ui.com), [Lottiefiles](https://lottiefiles.com/), [react-grid-layout](https://github.com/react-grid-layout/react-grid-layout), and [zxcvbn](https://github.com/dropbox/zxcvbn).


### What's included[#](https://supabase.com/blog/supabase-studio#whats-included)
Studio is designed to work with existing deployments - either the local hosted, docker setup, or our CLI. It is not intended for managing the deployment and administration of projects - that's out of scope.
The features exposed on Studio for existing deployments are limited to those which manage your database:
  * Table & SQL editors. (Saved queries are unavailable for now)
  * Database management: Policies, roles, extensions, replication.
  * API documentation.


Over time we'll expose a lot more of the codebase in the self-hosted Dashboard, this was as much as we could do for this Launch Week!
## How to contribute?[#](https://supabase.com/blog/supabase-studio#how-to-contribute)
Check out the full instructions in our [Studio Readme](https://github.com/supabase/supabase/tree/master/studio).
### We are live and launched on Product Hunt[#](https://supabase.com/blog/supabase-studio#we-are-live-and-launched-on-product-hunt)
Our new open source Studio is also on Product Hunt right now. If you like what you see, please give it an upvote and a review.
[![Open Source Table Editor](https://supabase.com/_next/image?url=https%3A%2F%2Fapi.producthunt.com%2Fwidgets%2Fembed-image%2Fv1%2Ffeatured.svg%3Fpost_id%3D321226%26theme%3Dlight&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://www.producthunt.com/posts/open-source-postgresql-studio?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-open-source-postgresql-studio)
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio&text=Supabase%20Studio)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio&text=Supabase%20Studio)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio&t=Supabase%20Studio)
[Last postRealtime Postgres RLS now available on Supabase1 December 2021](https://supabase.com/blog/realtime-row-level-security-in-postgresql)
[Next postCommunity Day29 November 2021](https://supabase.com/blog/community-day-lw3)
[launch-week](https://supabase.com/blog/tags/launch-week)[frontend](https://supabase.com/blog/tags/frontend)[studio](https://supabase.com/blog/tags/studio)
On this page
  * [Background](https://supabase.com/blog/supabase-studio#background)
  * [Approaches for managing shared codebases](https://supabase.com/blog/supabase-studio#approaches-for-managing-shared-codebases)
  * [Build in public](https://supabase.com/blog/supabase-studio#build-in-public)
  * [Technical details](https://supabase.com/blog/supabase-studio#technical-details)
  * [How to contribute?](https://supabase.com/blog/supabase-studio#how-to-contribute)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio&text=Supabase%20Studio)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio&text=Supabase%20Studio)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio&t=Supabase%20Studio)
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

