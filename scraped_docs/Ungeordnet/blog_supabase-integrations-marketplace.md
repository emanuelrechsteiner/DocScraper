---
url: https://supabase.com/blog/supabase-integrations-marketplace
scraped_at: 2025-05-25T08:54:13.072314
title: Supabase Integrations Marketplace
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
# Supabase Integrations Marketplace
10 Aug 2023
•
5 minute read
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Supabase Integrations Marketplace](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fintegration-marketplace-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've been running our [Integrations Marketplace](https://supabase.com/partners) in “stealth mode” for about a year now. What started as a dog-fooding project has now transformed into a marketplace with [over 60 integrations](https://supabase.com/partners/integrations). (It's also an [open source template](https://vercel.com/templates/next.js/supabase-partner-gallery) that you can use yourself).
![Featured](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Ffeatured-integrations.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase Integrations allows Partners to extend the Supabase platform with useful tooling. Today we're adding [OAuth2.0 Applications](https://supabase.com/docs/guides/platform/oauth-apps/publish-an-oauth-app). For Supabase users, this makes it even easier to connect their favorite tools to their Supabase projects. Within minutes you can:
  * Add your favorite [Low Code](https://supabase.com/partners/integrations#low-code) tools on top of your Supabase database.
  * Integrate your favorite [DevTools](https://supabase.com/partners/integrations#devtools): including secrets managers and database management tools.
  * Add [caching](https://supabase.com/partners/integrations#caching%20/%20offline-first) to your Supabase database.
  * Not a fan of the Supabase admin dashboard? Try [one of these](https://supabase.com/partners/integrations#data%20platform).
  * Try out a different [SMS and email provider](https://supabase.com/partners/integrations#messaging).


## Featured Partners[#](https://supabase.com/blog/supabase-integrations-marketplace#featured-partners)
For the initial launch we've started with a few partners to help us build and test the OAuth functionality.
### Cloudflare[#](https://supabase.com/blog/supabase-integrations-marketplace#cloudflare)
![Cloudflare x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-cloudflare.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We worked with Cloudflare to build [support for databases](https://blog.cloudflare.com/announcing-database-integrations/) inside Cloudflare Workers. The Cloudflare integration makes it incredibly easy to connect to your Supabase database directly from the Cloudflare Dashboard.
Check out the [latest episode](https://cloudflare.tv/event/using-supabase-with-cloudflare-workers/dgM90RgD) on Cloudflare TV to see it in action.
### Resend[#](https://supabase.com/blog/supabase-integrations-marketplace#resend)
![Resend x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-resend.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Resend](https://resend.com) (YC [W23](https://www.ycombinator.com/companies/resend)) is building the modern email sending platform. If you're using Supabase for Auth, then you'll know already that we handle all your Auth emails. But did you know that the email configuration we provide you is only for testing purposes? When you're [going into production](https://supabase.com/docs/guides/platform/going-into-prod#restricted-access-levels-for-team-members), you need to integrate your own email provider. That's where Resend come in. They've built a one-click integration to add Resend as a custom SMTP provider for Supabase.
Read more on [Resend's blog](https://resend.com/blog/how-to-configure-supabase-to-send-emails-from-your-domain).
### Snaplet[#](https://supabase.com/blog/supabase-integrations-marketplace#snaplet)
![Snaplet x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-snaplet.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Snaplet is a tool for Typescript developers to copy your database, transform sensitive data, and share it with your team without worrying about PII. If you followed our [Tuesday launch](https://supabase.com/blog/supabase-local-dev#database-seeding) you'll be familiar with Snaplet - they are one of the best tools for [generating seed data](https://supabase.com/docs/guides/cli/seeding-your-database#generating-seed-data) for your local development environment. Now they are making it even easier, with their official OAuth App, to spin up production-like development environments for your team.
[Learn more on snaplet.dev](https://www.snaplet.dev/post/now-live-supabase-x-snaplet-integration).
### Trigger.dev[#](https://supabase.com/blog/supabase-integrations-marketplace#triggerdev)
![Trigger x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-triggerdev.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Trigger.dev](http://trigger.dev/) (YC [W23](https://www.ycombinator.com/companies/trigger-dev)) is the open source Background Jobs framework for Next.js. You can create long-running Jobs directly in your codebase with features like API integrations, webhooks, scheduling and delays. And today you can use their one-click integration to [trigger anything from a database change](https://trigger.dev/supabase) in Supabase.
Learn more about their integration at: [trigger.dev/supabase](http://trigger.dev/supabase)
### Vercel[#](https://supabase.com/blog/supabase-integrations-marketplace#vercel)
![Vercel x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-vercel.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One that requires no introduction - since so many of you use Vercel, we've dedicated an entire blog post to the upgraded Vercel integration.
Learn more about the Vercel integration [updates we're launching](https://supabase.com/blog/using-supabase-with-vercel) today.
### Windmill[#](https://supabase.com/blog/supabase-integrations-marketplace#windmill)
![Windmill x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-windmill.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Windmill](https://windmill.dev) (YC [S22](https://www.ycombinator.com/companies/windmill)) is an open source alternative to Retool and a modern Airflow. They provide a developer platform to quickly build production-grade complex workflows and integrations from minimal Python and Typescript scripts. Their one-click integration with Supabase makes it simple to launch new databases, process large quantities of data (maybe even convert them into [embeddings](https://supabase.com/vector)), and build internal dashboards.
Read the [official blog post on windmill.dev](https://www.windmill.dev/blog/2023/08/10/supabase-partnership).
## Building Supabase Integrations[#](https://supabase.com/blog/supabase-integrations-marketplace#building-supabase-integrations)
We've released full instructions in our [Build with Supabase](https://supabase.com/docs/guides/platform/oauth-apps/build-a-supabase-integration) documentation so that you can build your own Supabase OAuth application for your users. Simply visit your [Organization settings](https://supabase.com/dashboard/org/_/apps) and click “Add application” to get started:
The Integrations marketplace is open to everyone. After your submission is complete, you can share the integration with your own users - simply create a button to launch your new app. We've provided some [brand assets](https://supabase.com/brand-assets) so that developers can quickly identify the integration on your site.
## Building custom integrations[#](https://supabase.com/blog/supabase-integrations-marketplace#building-custom-integrations)
You don't actually need to build an OAuth Application to build an integration with Supabase. If you're building something for yourself or your team, the [Management API](https://supabase.com/docs/reference/api/introduction) is the way to go.
The [Trigger.dev](https://trigger.dev) team deserve a special shout out. While developing their Integration they also developed [supabase-management-js](https://github.com/supabase-community/supabase-management-js), a Typescript library for the [Supabase Management API](https://supabase.com/docs/reference/api/introduction). This makes it even easier to get started with the Supabase API.
It's useful beyond just integrations. Want to programmatically spin up databases? Easy:
`
1
import { SupabaseManagementAPI } from "supabase-management-js";
23
const client = new SupabaseManagementAPI({
4
	accessToken: "<access token>"
5
})
67
const newProject = await client.createProject({
8
	 name: 'staging',
9
		db_pass: 'XXX',
10
  organization_id: 'XXX'
11
		plan: 'free',
12
  region: 'us-east-1'
13
})
`
## Become a Partner[#](https://supabase.com/blog/supabase-integrations-marketplace#become-a-partner)
Supabase is a collaborative company. We love working with other communities (especially open source ones!), and we'd love to work with you. Get started today:
  * [Build an OAuth integration](https://supabase.com/docs/guides/platform/oauth-apps/build-a-supabase-integration)
  * [Learn more about our Management API](https://supabase.com/docs/reference/api/introduction)


![Partner with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fpartner-with-supabase.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## More Launch Week 8[#](https://supabase.com/blog/supabase-integrations-marketplace#more-launch-week-8)
  * [Supabase Local Dev: migrations, branching, and observability](https://supabase.com/blog/supabase-local-dev)
  * [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
  * [Launch Week 8](https://supabase.com/launch-week)
  * [Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber)
  * [Why we'll stay remote](https://supabase.com/blog/why-supabase-remote)
  * [Postgres Language Server](https://github.com/supabase/postgres_lsp)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&text=Supabase%20Integrations%20Marketplace)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&text=Supabase%20Integrations%20Marketplace)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&t=Supabase%20Integrations%20Marketplace)
[Last postSupavisor: Scaling Postgres to 1 Million Connections11 August 2023](https://supabase.com/blog/supavisor-1-million)
[Next postVercel Integration and Next.js App Router Support10 August 2023](https://supabase.com/blog/using-supabase-with-vercel)
[launch-week](https://supabase.com/blog/tags/launch-week)[integrations](https://supabase.com/blog/tags/integrations)
On this page
  * [Featured Partners](https://supabase.com/blog/supabase-integrations-marketplace#featured-partners)
    * [Cloudflare](https://supabase.com/blog/supabase-integrations-marketplace#cloudflare)
    * [Resend](https://supabase.com/blog/supabase-integrations-marketplace#resend)
    * [Snaplet](https://supabase.com/blog/supabase-integrations-marketplace#snaplet)
    * [Trigger.dev](https://supabase.com/blog/supabase-integrations-marketplace#triggerdev)
    * [Vercel](https://supabase.com/blog/supabase-integrations-marketplace#vercel)
    * [Windmill](https://supabase.com/blog/supabase-integrations-marketplace#windmill)
  * [Building Supabase Integrations](https://supabase.com/blog/supabase-integrations-marketplace#building-supabase-integrations)
  * [Building custom integrations](https://supabase.com/blog/supabase-integrations-marketplace#building-custom-integrations)
  * [Become a Partner](https://supabase.com/blog/supabase-integrations-marketplace#become-a-partner)
  * [More Launch Week 8](https://supabase.com/blog/supabase-integrations-marketplace#more-launch-week-8)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&text=Supabase%20Integrations%20Marketplace)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&text=Supabase%20Integrations%20Marketplace)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&t=Supabase%20Integrations%20Marketplace)
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

