---
url: https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1
scraped_at: 2025-05-25T09:11:10.427043
title: Edge Functions: Deploy from the Dashboard + Deno 2.1
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
# Edge Functions: Deploy from the Dashboard + Deno 2.1
01 Apr 2025
•
4 minute read
[![Saxon Fletcher avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaxonf.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Saxon FletcherProduct Design](https://github.com/saxonf)
[![Nyannyacha avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fnyannyacha.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)NyannyachaEngineering](https://github.com/nyannyacha)
[![Lakshan Perera avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Flaktek.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Lakshan PereraEngineering](https://github.com/laktek)
![Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fthumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Now you can create, test, edit, and deploy Edge Functions directly from the Supabase Dashboard. We're also releasing Deno 2.1 Preview today but more on that later.
## Creating Edge Functions from the Supabase Dashboard[#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#creating-edge-functions-from-the-supabase-dashboard)
To write an Edge Functions previously, you had to install the Supabase CLI, spin up Docker, and then set up your editor to use Deno. Those steps are no longer necessary. The Edge Functions editor in the Dashboard has built-in syntax highlighting and type-checking for Deno and Supabase-specific APIs.
![Create a Function from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fcreate-function.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The Edge Functions editor includes templates for common use cases, such as Stripe WebHooks, OpenAI proxying, uploading files to Supabase Storage, and sending emails.
![Function Templates](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Ffunction-templates.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Once a Function has been deployed you can make edits directly within the Dashboard, and if you get stuck you can summon an inline AI Assistant to explain, debug or write code.
![Edit Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fedit-function.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Downloading Edge Functions[#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#downloading-edge-functions)
You can download Edge Functions source code via Supabase CLI using `supabase functions download FUNCTION_NAME` or by clicking the Download button in the dashboard.
![Download Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fdownload-function.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The Dashboard's Edge Function editor currently does not support versioning or rollbacks. We recommend using it only for quick testing and prototypes. When you’re ready to go to production, store Edge Functions code in a source code repository (e.g. git) and deploy it using one of the [CI integrations](https://supabase.com/docs/guides/functions/cicd-workflow).
## Testing Edge Functions from the Supabase Dashboard[#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#testing-edge-functions-from-the-supabase-dashboard)
We are introducing a built-in tool for testing your Edge Functions from the Supabase Dashboard. You can execute your Edge Function with different request payloads, headers, and query parameters. The built-in tester returns the response status, headers, and body.
![Test Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Ftest-function.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
With the built-in editor and tester, you have a streamlined workflow for creating, testing, and refactoring your Edge Functions without leaving the Supabase Dashboard.
## Deploying Edge Functions no longer requires Docker[#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#deploying-edge-functions-no-longer-requires-docker)
By popular request, you can now deploy Edge Functions from the Supabase CLI with the `--use-api` flag, which will not use Docker. We will make this the default behavior in future releases (with a `--use-docker` flag as a fallback option.)
`
1
supabase functions deploy MY_FUNCTION --use-api
`
## New APIs for Deploying Edge Functions[#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#new-apis-for-deploying-edge-functions)
The ability to deploy without Docker in both the Edge Functions editor and Supabase CLI are made possible by new APIs we introduced to deploy and update Edge Functions. These APIs are publicly available for you to build custom integrations and workflows.
You can check [the Changelog announcement](https://github.com/orgs/supabase/discussions/33720) for more details and official references to these API endpoints.
## Deno 2.1 Preview[#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#deno-21-preview)
Last, but not least, we have added Deno 2.1 support for Supabase Edge Runtime. With Deno 2.1, you can use built-in Deno commands to scaffold a new project, manage dependencies, run tests, and lints.
Check [our guide on how to start using Deno 2.1](https://github.com/orgs/supabase/discussions/34054) tooling for your Edge Functions.
Note that the Supabase hosted platform is still using Deno 1.45. In the coming weeks, we will provide more details on deploying Deno 2.1 projects in the hosted platform.
## Conclusion[#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#conclusion)
These changes to Supabase Edge Functions make it easier and more accessible for all developers to build powerful functionality into their applications.
  * Read the [Edge Functions documentation](https://supabase.com/docs/guides/functions) to learn more
  * [Sign up for Supabase](https://supabase.com/dashboard/sign-up) and get started today


[Launch Week 14](https://supabase.com/launch-week)
Mar 31 - Apr 04 '25
[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage
[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)[Community Meetups](https://supabase.com/events?category=meetup)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&text=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&text=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&t=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)
[Last postKeeping Tabs on What's New in Supabase Studio2 April 2025](https://supabase.com/blog/tabs-dashboard-updates)
[Next postAutomatic Embeddings in Postgres1 April 2025](https://supabase.com/blog/automatic-embeddings)
[launch-week](https://supabase.com/blog/tags/launch-week)[functions](https://supabase.com/blog/tags/functions)
On this page
  * [Creating Edge Functions from the Supabase Dashboard](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#creating-edge-functions-from-the-supabase-dashboard)
  * [Downloading Edge Functions](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#downloading-edge-functions)
  * [Testing Edge Functions from the Supabase Dashboard](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#testing-edge-functions-from-the-supabase-dashboard)
  * [Deploying Edge Functions no longer requires Docker](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#deploying-edge-functions-no-longer-requires-docker)
  * [New APIs for Deploying Edge Functions](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#new-apis-for-deploying-edge-functions)
  * [Deno 2.1 Preview](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#deno-21-preview)
  * [Conclusion](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#conclusion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&text=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&text=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&t=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)
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
![Function Templates](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Ffunction-templates.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Create a Function from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fcreate-function.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Edit Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fedit-function.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

