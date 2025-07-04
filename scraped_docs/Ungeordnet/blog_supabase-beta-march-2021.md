---
url: https://supabase.com/blog/supabase-beta-march-2021
scraped_at: 2025-05-25T08:51:03.468268
title: Supabase Beta March 2021
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
# Supabase Beta March 2021
06 Apr 2021
•
4 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Supabase Beta March 2021](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmarch-2021%2Frelease-mar-2021.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Launch week, Storage, Supabase CLI, Connection Pooling, Supabase UI, and Pricing. Here's what we released last month.
### Quick demo[#](https://supabase.com/blog/supabase-beta-march-2021#quick-demo)
Watch a full demo:
## Supabase Storage[#](https://supabase.com/blog/supabase-beta-march-2021#supabase-storage)
Need to store images, audio, and video clips? Well now you can do it on [Supabase Storage](https://supabase.com/blog/supabase-storage). It's backed by S3 and our new [OSS storage API](https://github.com/supabase/storage-api) written in Fastify and Typescript. Read the [full blog post](https://supabase.com/blog/supabase-storage).
![Supabase Storage](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fstorage%2Fph-1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Connection Pooling[#](https://supabase.com/blog/supabase-beta-march-2021#connection-pooling)
The Supabase API already handles Connection Pooling, but if you're connecting to your database directly (for example, with Prisma) we now [bundle PgBouncer](https://supabase.com/blog/supabase-pgbouncer). Read the [full blog post](https://supabase.com/blog/supabase-pgbouncer).
![Connection Pooling](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fbouncer%2Fpgbouncer-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## React UI Component Library[#](https://supabase.com/blog/supabase-beta-march-2021#react-ui-component-library)
We open sourced our internal UI component library, so that anyone can use and contribute to the Supabase aesthetic. It lives at [ui.supabase.com](https://ui.supabase.com/) . It was also the #1 Product of the Day [on Product Hunt](https://www.producthunt.com/posts/supabase-ui).
![React UI Library](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmarch-2021%2Fsupabase-ui.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## CLI[#](https://supabase.com/blog/supabase-beta-march-2021#cli)
Now you can run Supabase locally in the terminal with `supabase start`. We have done some preliminary work on [diff-based schema migrations](https://supabase.com/blog/supabase-cli#migrations), and added some new tooling for self-hosting Supabase with Docker. [Blog post here](https://supabase.com/blog/supabase-cli).
![Supabase CLI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmarch-2021%2Fsupabase-cli.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Pricing[#](https://supabase.com/blog/supabase-beta-march-2021#pricing)
Our most frequently asked question by far is "ok supabase is sweet, but how much is it going to cost?". TL;DR there's **Free Plan** up to 500mb + 10k auth users, a **Pro** **Plan** at $25/month for 8GB + 100k auth users, and anything additional is charged on a usage basis.
See [Pricing Page](https://supabase.com/pricing) for full details and also our blog on why [pricing is hard](https://supabase.com/blog/pricing).
![Supabase Pricing](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmarch-2021%2Fsupabase-pricing.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## NFT Platform[#](https://supabase.com/blog/supabase-beta-march-2021#nft-platform)
Well... not really, but it made for a great [April Fools joke](https://supabase.com/blog/supabase-nft-marketplace).
![Supabase NFT marketplace BuyMeth.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnft%2Fnft-1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Supabase Dot Com[#](https://supabase.com/blog/supabase-beta-march-2021#supabase-dot-com)
We are now dot com! We'll be porting across over the next few weeks. Read the origin story behind the name [here](https://supabase.com/blog/supabase-dot-com).
![Supabase Dot Com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupabase-dot-com-og.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## OAuth Scopes[#](https://supabase.com/blog/supabase-beta-march-2021#oauth-scopes)
Thanks to a comunity contribution ([@_mateomorris](https://twitter.com/_mateomorris) and [@Beamanator](https://twitter.com/Beamanator)), Supabase Auth now includes OAuth scopes. These allow you to request elevated access during login. For example, you may want to request access to a list of Repositories when users log in with GitHub. Check out the [Documentation](https://supabase.com/docs/reference/javascript/auth-signup#sign-up-with-scopes).
![Oauth Scope](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmarch-2021%2Foauth-scopes.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Kaizen[#](https://supabase.com/blog/supabase-beta-march-2021#kaizen)
  * You can now manage your PostgREST configuration inside the Dashboard.
  * Our website has been redesigned. Check out our new [Homepage](https://supabase.com/) and [Blog](https://supabase.com/blog), and our new [Database](https://supabase.com/database), [Auth](https://supabase.com/auth), and [Storage](https://supabase.com/storage) product pages.
  * We refactored some of our Filter methods to make them even easier to use. Check out the [Full Text Search](https://supabase.com/docs/reference/javascript/textsearch) refactor.
  * We have added several new sections to our Docs including: [Local Dev](https://supabase.com/docs/guides/local-development), [Self Hosting](https://supabase.com/docs/guides/self-hosting), and [Postgres Reference](https://supabase.com/docs/reference/postgres/getting-started) docs (all still under development).


## Community[#](https://supabase.com/blog/supabase-beta-march-2021#community)
  * How to use Supabase inside Replit [[Video](https://www.youtube.com/watch?v=lQ5iIxaYduI)]
  * [Connecting Draftbit to Supabase](https://docs.draftbit.com/docs/supabase) by [@amanhimself](https://twitter.com/amanhimself)
  * [Creating Users in Next-js](https://t.co/IKcn3mgqW0?amp=1) by [@indigitalcolor](https://twitter.com/indigitalcolor)
  * [A Backend for IndieHackers](https://drew.tech/supabase-a-backend-for-indiehackers) by [@dbredvick](https://twitter.com/DBredvick)
  * The Firebase Alternative by [Simon Grimm](https://www.youtube.com/user/saimon1924) [[Video](https://www.youtube.com/watch?v=F6VyIXFQVtQ)]
  * Ionic Integration by [Simon Grimm](https://www.youtube.com/user/saimon1924) [[Video](https://www.youtube.com/watch?v=pl9XfIWutKE)]
  * Flutter Integration by [Aditya Thakur](https://www.youtube.com/channel/UChCAJNpMwoEUYCsE_eSyU4w) by [[Video](https://www.youtube.com/watch?v=fqfHEZvQPlY)]
  * Svelte Integration by [Khaerunnisa Isnaeni](https://www.youtube.com/channel/UCqNDj6eQeTLHuEwgEHWOGjw) [[Video](https://www.youtube.com/watch?v=odPYzJJyEJI)]
  * An [example app](https://github.com/supabase/supabase/tree/master/examples/user-management) for adding User Profiles to your Next.js app


![Supabase Stars march 2021](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmarch-2021%2Fsupabase-stars-march-2021.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Source: [repository.surf/supabase](https://repository.surf/supabase)
If you want to keep up to date, make sure you [subscribe to our YouTube channel](https://www.youtube.com/c/supabase) or [follow us on Twitter](https://twitter.com/supabase).
## Coming Next[#](https://supabase.com/blog/supabase-beta-march-2021#coming-next)
Lets say for each new sign up, you want to trigger a slack alert, send them an email after 24 hours.
For this we are working on our own [Workflow engine](https://supabase.com/blog/supabase-workflows), it will eventually have a Zapier-like interface inside the dashboard. For now it's a state-machine interpreter (fully compatible with Amazon States Language) written in Elixir, [open source](https://github.com/supabase/workflows), and ready for community contributions.
![Workflows](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fworkflows%2Fworkflows-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Get started[#](https://supabase.com/blog/supabase-beta-march-2021#get-started)
  * Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
  * Make sure to [star us on GitHub](https://github.com/supabase/supabase)
  * Follow us [on Twitter](https://twitter.com/supabase)
  * Subscribe to our [YouTube channel](https://www.youtube.com/c/supabase)
  * Become a [sponsor](https://github.com/sponsors/supabase)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-march-2021&text=Supabase%20Beta%20March%202021)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-march-2021&text=Supabase%20Beta%20March%202021)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-march-2021&t=Supabase%20Beta%20March%202021)
[Last postSupabase Beta April 20215 May 2021](https://supabase.com/blog/supabase-beta-april-2021)
[Next postSupabase Dot Com2 April 2021](https://supabase.com/blog/supabase-dot-com)
[release-notes](https://supabase.com/blog/tags/release-notes)
On this page
  * [Supabase Storage](https://supabase.com/blog/supabase-beta-march-2021#supabase-storage)
  * [Connection Pooling](https://supabase.com/blog/supabase-beta-march-2021#connection-pooling)
  * [React UI Component Library](https://supabase.com/blog/supabase-beta-march-2021#react-ui-component-library)
  * [CLI](https://supabase.com/blog/supabase-beta-march-2021#cli)
  * [Pricing](https://supabase.com/blog/supabase-beta-march-2021#pricing)
  * [NFT Platform](https://supabase.com/blog/supabase-beta-march-2021#nft-platform)
  * [Supabase Dot Com](https://supabase.com/blog/supabase-beta-march-2021#supabase-dot-com)
  * [OAuth Scopes](https://supabase.com/blog/supabase-beta-march-2021#oauth-scopes)
  * [Kaizen](https://supabase.com/blog/supabase-beta-march-2021#kaizen)
  * [Community](https://supabase.com/blog/supabase-beta-march-2021#community)
  * [Coming Next](https://supabase.com/blog/supabase-beta-march-2021#coming-next)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-march-2021&text=Supabase%20Beta%20March%202021)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-march-2021&text=Supabase%20Beta%20March%202021)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-march-2021&t=Supabase%20Beta%20March%202021)
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

