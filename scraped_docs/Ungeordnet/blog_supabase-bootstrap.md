---
url: https://supabase.com/blog/supabase-bootstrap
scraped_at: 2025-05-25T08:54:33.714473
title: Supabase Bootstrap: the fastest way to launch a new project
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
# Supabase Bootstrap: the fastest way to launch a new project
15 Apr 2024
•
4 minute read
[![Qiao Han avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsweatybridge.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Qiao HanEngineering](https://github.com/sweatybridge)
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Supabase Bootstrap: the fastest way to launch a new project](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fbootstrap%2Fthumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase `bootstrap` is the fastest to spin up a new hosted Supabase project from existing starter templates:
`
1
npx supabase bootstrap
`
This brings a “shadcn”-like experience to Supabase, creating a project locally and launching a remote database ready for deployment.
## Getting started[#](https://supabase.com/blog/supabase-bootstrap#getting-started)
From any local directory, run `supabase bootstrap` and you will be prompted to choose a starter template. And the best thing is, you don't even need to install the CLI to get started! As long as you have `npm` or `bun` installed, you're ready to go!
  * CLI: `supabase bootstrap`
  * NPM: `npx supabase@latest bootstrap`
  * Bun: `bunx` `supabase@latest bootstrap`


![Bootstrap getting started](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fbootstrap%2Fgetting-started.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## How templates work[#](https://supabase.com/blog/supabase-bootstrap#how-templates-work)
The list of starter templates is published on GitHub as [samples.json](https://github.com/supabase-community/supabase-samples/blob/main/samples.json). Whenever we (and in the future the community) add a new starter, it will automatically become available to all Supabase users.
The template repository typically includes the full frontend code, following the file structure below:
  * A `supabase` directory with `config.toml` and `migrations` files (if any).
  * A `.env.example` file that defines a list of environment variables for CLI to populate project credentials. We currently support the same list of credentials as our [Vercel integration](https://vercel.com/integrations/supabase). If a `.env` file doesn't exist, the CLI will create it for you.


### Local development[#](https://supabase.com/blog/supabase-bootstrap#local-development)
After selecting a starter, the Supabase CLI downloads all files from the template repository to your chosen local directory.
##### GitHub rate limits
You may run into GitHub rate limit when downloading too frequently from template repository. This can be avoided by setting `GITHUB_TOKEN` environment variable locally to your GitHub personal access token.
This model is very similar to the popular [shadcn](https://ui.shadcn.com/) workflow. After files are creating in your local repo, you can modify them and check them into source control.
### Deploying to production[#](https://supabase.com/blog/supabase-bootstrap#deploying-to-production)
During the `supabase bootstrap` process, a new project will be created on the Supabase platform and linked to your local environment. This command will run you through the account creation flow if you don't already have one.
![Bootstrap getting started](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fbootstrap%2Fdeploying-to-production.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
##### Some patience required
Linking to your new hosted project may take a short while as it needs to spin up a new database in the cloud.
Once the linking is completed, you will be prompted to push any template migration files to your new hosted project. These migration files will setup your remote database with the necessary schemas to support the starter application.
![Bootstrap getting started](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fbootstrap%2Fdeploying-to-production-2.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
After pushing the migrations, your project credentials will be exported to a `.env` file for you to connect from any frontend or backend code. The default environment variables include:
  * `POSTGRES_URL`
  * `SUPABASE_URL`
  * `SUPABASE_ANON_KEY`
  * `SUPABASE_SERVICE_ROLE_KEY`


Other custom variables from `.env.example` file defined by your chosen template will also be merged to your local `.env` file.
##### Store credentials securely
It is important to store these credentials securely as anyone can connect to your remote database using the `POSTGRES_URL`.
## Start developing[#](https://supabase.com/blog/supabase-bootstrap#start-developing)
Finally, the CLI will suggest a `start` command to launch your application locally. Starting the local app will use credentials defined in `.env` file to connect to your new hosted project.
![Bootstrap getting started](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fbootstrap%2Fstart-developing.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Template library[#](https://supabase.com/blog/supabase-bootstrap#template-library)
And that's it, with a single command, you can get a new project up and running end to end.
Supabase Bootstrap makes it even easier to get started with Supabase, mobile app tools, and web development frameworks like Next.js, Expo React Native, Flutter, Swift iOS.
We have many many more templates coming soon, and we'll be opening it up to community contributions. Stay tuned!
## Get started[#](https://supabase.com/blog/supabase-bootstrap#get-started)
Visit the [Supabase CLI docs](https://supabase.com/docs/guides/cli/getting-started) to get started with `supabase bootstrap`.
[![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-black.svg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-white.svg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Week](https://supabase.com/ga-week)
15-19 April
[Day 1 -Supabase is officially launching into General Availability](https://supabase.com/ga)[Day 2 -Supabase Functions now supports AI models](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)[Day 3 -Supabase Auth now supports Anonymous sign-ins](https://supabase.com/blog/anonymous-sign-ins)[Day 4 -Supabase Storage: now supports the S3 protocol](https://supabase.com/blog/s3-compatible-storage)[Day 5 -Supabase Security Advisor & Performance Advisor](https://supabase.com/blog/security-performance-advisor)

Build Stage
[01 -PostgreSQL Index Advisor](https://github.com/supabase/index_advisor)[02 -Branching now Publicly Available](https://supabase.com/blog/branching-publicly-available)[03 -Oriole joins Supabase](https://supabase.com/blog/supabase-acquires-oriole)[04 -Supabase on AWS Marketplace](https://supabase.com/blog/supabase-aws-marketplace)[05 -Supabase Bootstrap](https://supabase.com/blog/supabase-bootstrap)[06 -Supabase Swift](https://supabase.com/blog/supabase-swift)[07 -Top 10 Launches from Supabase GA Week](https://supabase.com/blog/ga-week-summary)[Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon)[Community Meetups](https://supabase.com/ga-week#meetups)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-bootstrap&text=Supabase%20Bootstrap%3A%20the%20fastest%20way%20to%20launch%20a%20new%20project)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-bootstrap&text=Supabase%20Bootstrap%3A%20the%20fastest%20way%20to%20launch%20a%20new%20project)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-bootstrap&t=Supabase%20Bootstrap%3A%20the%20fastest%20way%20to%20launch%20a%20new%20project)
[Last postSupabase on the AWS Marketplace15 April 2024](https://supabase.com/blog/supabase-aws-marketplace)
[Next postSupabase Swift15 April 2024](https://supabase.com/blog/supabase-swift)
[launch-week](https://supabase.com/blog/tags/launch-week)[CLI](https://supabase.com/blog/tags/CLI)
On this page
  * [Getting started](https://supabase.com/blog/supabase-bootstrap#getting-started)
  * [How templates work](https://supabase.com/blog/supabase-bootstrap#how-templates-work)
    * [Local development](https://supabase.com/blog/supabase-bootstrap#local-development)
    * [Deploying to production](https://supabase.com/blog/supabase-bootstrap#deploying-to-production)
  * [Start developing](https://supabase.com/blog/supabase-bootstrap#start-developing)
  * [Template library](https://supabase.com/blog/supabase-bootstrap#template-library)
  * [Get started](https://supabase.com/blog/supabase-bootstrap#get-started)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-bootstrap&text=Supabase%20Bootstrap%3A%20the%20fastest%20way%20to%20launch%20a%20new%20project)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-bootstrap&text=Supabase%20Bootstrap%3A%20the%20fastest%20way%20to%20launch%20a%20new%20project)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-bootstrap&t=Supabase%20Bootstrap%3A%20the%20fastest%20way%20to%20launch%20a%20new%20project)
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

