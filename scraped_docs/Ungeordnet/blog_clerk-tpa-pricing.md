---
url: https://supabase.com/blog/clerk-tpa-pricing
scraped_at: 2025-05-25T09:30:33.267144
title: Supabase Auth: Bring Your Own Clerk
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
# Supabase Auth: Bring Your Own Clerk
31 Mar 2025
•
3 minute read
[![Stojan Dimitrovski avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fhf.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Stojan DimitrovskiEngineering](https://github.com/hf)
![Supabase Auth: Bring Your Own Clerk](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-clerk-tpa-pricing%2Fclerk-tpa-pricing-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we're expanding our official Third-party Auth integrations to include [Clerk](https://clerk.com).
[Third-party Auth](https://supabase.com/docs/guides/auth/third-party/overview) allows you to use external Auth providers with the Supabase as a drop-in replacement for Supabase Auth. This modular design is [intentional](https://supabase.com/docs/guides/getting-started/architecture#product-principles), allowing you to pick and choose features of Supabase. Our platform makes it easy to get started with Postgres and _any_ of your favorite tools.
![Clerk TPA diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-clerk-tpa-pricing%2Fclerk-tpa-diagram.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
It was [already possible](https://supabase.com/partners/integrations/clerk) to use Clerk with Supabase, however the previous method was a bit of a hack that required sharing your project's secret and JWT templates from Clerk. We've worked with the Clerk team on the new implementation. Now you can enjoy better security and the same developer experience you've come to expect from Supabase.
To get started with Clerk and Supabase, visit Clerk's [Connect with Supabase](https://dashboard.clerk.com/setup/supabase) page.
Register your Clerk domain [in the Supabase Dashboard](https://supabase.com/dashboard/project/_/auth/third-party) or in the CLI:
`
1
[auth.third_party.clerk]
2
enabled = true
3
domain = "example.clerk.accounts.dev"
`
In your JavaScript app all you need to do is write the following code:
`
1
import { createClient } from '@supabase/supabase-js'
23
const SUPABASE_URL = 'https://<supabase-project>.supabase.co'
4
const SUPABASE_ANON_KEY = '<SUPABASE_ANON_KEY>'
56
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
7
 accessToken: () => {
8
  return Clerk.session?.getToken()
9
 },
10
})
`
[Read the docs](https://supabase.com/docs/guides/auth/third-party/clerk) to set up Flutter and Swift (iOS) applications, and to learn how to use Postgres Row-level Security (RLS) Policies.
## Third-Party Auth is now a lot cheaper[#](https://supabase.com/blog/clerk-tpa-pricing#third-party-auth-is-now-a-lot-cheaper)
One more thing: today we're making Third-party Auth cheaper so that it has pricing parity with Supabase Auth.
You can have up to 50,000 MAU on the Free plan, or 100,000 MAU on the Pro plan and $0.00325 per MAU above that number.
| Free Plan| Pro Plan  
---|---|---  
Previously| 50 MAUs included| 50,000 MAUs included  
Now| 50,000 MAUs included| 100,000 MAUs included  
## Get started today[#](https://supabase.com/blog/clerk-tpa-pricing#get-started-today)
Supabase Auth makes it easy to implement authentication and authorization in your app. We provide client SDKs and API endpoints to help you create and manage users.
  * [Read the documentation](https://supabase.com/docs/guides/auth/third-party/overview) for Third-party Auth
  * [Learn how to use Clerk with Supabase](https://supabase.com/docs/guides/auth/third-party/clerk)
  * [Sign up for Supabase](https://supabase.com/dashboard/sign-up) and get started today


[Launch Week 14](https://supabase.com/launch-week)
Mar 31 - Apr 04 '25
[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage
[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)[Community Meetups](https://supabase.com/events?category=meetup)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&text=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&text=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&t=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)
[Last postIntroducing the Supabase UI Library31 March 2025](https://supabase.com/blog/supabase-ui-library)
[Next postPostgres Language Server: Initial Release29 March 2025](https://supabase.com/blog/postgres-language-server)
[launch-week](https://supabase.com/blog/tags/launch-week)[auth](https://supabase.com/blog/tags/auth)
On this page
  * [Third-Party Auth is now a lot cheaper](https://supabase.com/blog/clerk-tpa-pricing#third-party-auth-is-now-a-lot-cheaper)
  * [Get started today](https://supabase.com/blog/clerk-tpa-pricing#get-started-today)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&text=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&text=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&t=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)
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

