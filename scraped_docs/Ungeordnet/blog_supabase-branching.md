---
url: https://supabase.com/blog/supabase-branching
scraped_at: 2025-05-25T08:38:54.130090
title: Supabase Branching
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
# Supabase Branching
13 Dec 2023
•
8 minute read
[![Qiao Han avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsweatybridge.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Qiao HanEngineering](https://github.com/sweatybridge)
[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Jonny Summers-MuirProduct Design](https://github.com/mildtomato)
![Supabase Branching](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Fbranching-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
A few months ago we mentioned that we were working on Branching with a (somewhat ambitious) early-access form.
Today we are rolling out access to early-access subscribers. Internally, we were hoping to make this public access for this Launch Week but, well, [_we did say this was hard_](https://supabase.com/blog/supabase-local-dev#supabase-branching-is-hard).
We're operating on a first-signed-up, first-served basis, rolling it out in batches to paid orgs who registered for early access.
## What's Branching?[#](https://supabase.com/blog/supabase-branching#whats-branching)
At some point during development, you will probably need to experiment with your Postgres database. Today that's possible on your local development machine using the Supabase CLI. When you run `supabase start` with the CLI to get the entire Supabase stack running locally. You can play around with ideas and run `supabase db reset` whenever you want to start again. When you want to capture your changes in a database migration, you can run `supabase db diff`.
Branching is a natural extension of this, but instead of experimenting with just a _local_ database you also get _remote_ database. You continue to use the workflow above, and then when you commit your changes to Git we'll run them on a Supabase Preview Branch.
![Each Git branch has a corresponding Supabase Preview.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Ffeat-branches-examples--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Each Git branch has a corresponding Supabase Preview.
Each Git branch has a corresponding Supabase Preview, which automatically updates whenever you push an update. The rest of the workflow should feel familiar: when you merge a Pull Request into your main Git branch, Supabase will run your database migrations inside your Production database.
Your project's Preview Branches are designed with safety in mind. They are isolated instances, each with a distinct set of API keys and passwords. Each instance contains every Supabase feature: a Postgres database, Auth, File Storage, Realtime, Edge Functions, and Data APIs.
![Every Supabase Preview is a dedicated instance, with a full suite of Supabase services.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Fisolated-instances--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Every Supabase Preview is a dedicated instance, with a full suite of Supabase services.
Even in relaxed developer environments, if one of your team accidentally leaks a key it won't affect your Production branch.
### Support for Vercel Previews[#](https://supabase.com/blog/supabase-branching#support-for-vercel-previews)
We've designed Supabase Branching to work perfectly with Vercel's [Preview](https://vercel.com/features/previews) deployments. This means that you get an _entire stack_ with Branching.
![Vercel will build your preview deployments, and your preview deployment can connect to the Supabase services on your Preview Branch.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Fvercel-support--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Vercel will build your preview deployments, and your preview deployment can connect to the Supabase services on your Preview Branch.
We've made several improvements to our [Vercel Integration](https://vercel.com/integrations/supabase) to make the Vercel experience seamless. For example, since we provide distinct, secure database credentials for every Supabase Preview Branch, we automatically populate the environment variables on Vercel with the connection secrets your app needs to connect to the Preview Branch.
![Vercel environment variables settings page, showing the Git branch based env vars.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Fvercel-env-var-settings--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Vercel environment variables settings page, showing the Git branch based env vars.
### Developing on the hosted Preview Branch[#](https://supabase.com/blog/supabase-branching#developing-on-the-hosted-preview-branch)
One of the most-loved features of Supabase is the dashboard. Even if we [beg](https://supabase.com/docs/guides/platform/maturity-model#in-production), it seems that developers simply want to use it for everything - even in production.
The cool thing about Branching is that every Supabase Preview can be managed from the Dashboard. You can make schema changes, access the SQL Editor, and use the [new AI Assistant](https://supabase.com/blog/studio-introducing-assistant). Once you're happy with your changes, you simply run `supabase db diff` on your local machine to pull the changes and you can commit them to Git.
Just note that we _still_ want you to develop locally! You should treat the Preview Branches [like cattle, not pets](https://devops.stackexchange.com/questions/653/what-is-the-definition-of-cattle-not-pets). Your Preview changes can be wiped at any time if one of your team pushes a destructive migration.
### Database migrations[#](https://supabase.com/blog/supabase-branching#database-migrations)
We've developed Branching to work with a Git provider, starting with GitHub.
Our [GitHub app](https://github.com/apps/supabase) observes changes within a connected GitHub repository. When you open a Pull Request, it launches a Preview Branch and runs the migrations in `./supabase/migrations`. If there are any errors they are logged to the [Check Run](https://docs.github.com/en/rest/checks/runs?apiVersion=2022-11-28) associated with that git commit. When all checks turn green, your new Preview Branch is ready to use.
When you push a new migration file to the Git branch, the app runs it incrementally in your Preview Branch. This allows you to verify schema changes easily on existing seed data.
Finally, when you merge that PR, the app runs the new migrations on your Production environment. If you have other PRs already open, make sure to update those migration files to a later timestamp than the ones in the Production branch following a [standard migration practice](https://supabase.com/docs/guides/cli/managing-environments).
### Data seeding[#](https://supabase.com/blog/supabase-branching#data-seeding)
You can seed your Preview branch in the same way that you [seed your local development environment](https://supabase.com/docs/guides/cli/seeding-your-database). Just add `./supabase/seed.sql` in your repo and the seed script will run when the Preview Branch is created.
Optionally, you can reset the database by running `supabase db reset --db-url <branch-connection-string />`. The branch connection string can be retrieved using your Personal Access Token with Supabase CLI's [branch management](https://supabase.com/docs/reference/cli/supabase-branches-get) commands.
We're investigating data masking techniques with a copy-on-write system so that you can emulate a production workload inside your Preview Branches. We plan for this to work with File Storage too.
##### Testing with product workloads today?
If you need to test with production workloads today, check out [Snaplet](https://www.snaplet.dev/) and [Postgres.ai](http://Postgres.ai). Both are great partners of Supabase.
## Future considerations[#](https://supabase.com/blog/supabase-branching#future-considerations)
That's already a lot for Branching v0. Branching will be a core part of the developer workflow in the future. These are the themes we'll explore next:
### Declarative config[#](https://supabase.com/blog/supabase-branching#declarative-config)
We're still working on “configuration in code”. For example, you might want to try a different Google Auth in your Preview Branch than the one you use in Product. This would be a lot easier if the code was declarative, inside the [config.toml](https://supabase.com/docs/guides/cli/config) file.
### Automatic dashboard commits[#](https://supabase.com/blog/supabase-branching#automatic-dashboard-commits)
In the current version, when you use the dashboard to create a change on a Preview Branch, you need to run `db diff` locally to pull that change into your Git repository. We plan to work on a feature to automatically capture your changes in a Git repo that you've connected.
### Extended seeding behavior[#](https://supabase.com/blog/supabase-branching#extended-seeding-behavior)
There are a multitude of different strategies for populating seed data. We've dabbled with AI to generate seed data, which was fun. We also like the approach of [postgresql-anonymizer](https://postgresql-anonymizer.readthedocs.io/en/stable/) and [Snaplet](https://docs.snaplet.dev/recipes/supabase), which specialize in cloning production data while anonymizing the data for safe development.
### Copy-on-write[#](https://supabase.com/blog/supabase-branching#copy-on-write)
We have something in development :). CoW means you can branch from database snapshot and then run tests on “production-like” workloads. This is the approach that [Postgres.ai](http://Postgres.ai) uses. As we mentioned above, we need to figure out an approach that also works with [File Storage](https://supabase.com/storage).
## Interested in using Branching?[#](https://supabase.com/blog/supabase-branching#interested-in-using-branching)
We'll be onboarding organizations in batches over the next few weeks, and working with these early users on Pricing.
**Update 17th January 2024** - Early access for Branching is now closed for the foreseeable future. We are now working hard towards releasing a public beta.
Check out the [Branching docs](https://supabase.com/docs/guides/platform/branching) and also if you have any feedback, [you can join the discussion](https://github.com/orgs/supabase/discussions/18937).
![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Fbranching-ui--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
New Branching UI in the Supabase dashboard
[Launch Week ![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/launch-week)
11-15 Dec
Main Stage
[Day 1 -Supabase Studio: introducing an **AI Assistant** , **Postgres roles** , and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)[ Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)[Day 3 -Introducing Supabase **Branching** , a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)[Day 4 -Supabase Auth: **Identity Linking** , **Session Control** , **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)[ Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)

Build Stage
[01 -Supabase Album](https://supabase.productions/)[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)[05 -pg_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-branching&text=Supabase%20Branching)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-branching&text=Supabase%20Branching)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-branching&t=Supabase%20Branching)
[Last postPostgREST 1213 December 2023](https://supabase.com/blog/postgrest-12)
[Next postSupavisor 1.0: a scalable connection pooler for Postgres13 December 2023](https://supabase.com/blog/supavisor-postgres-connection-pooler)
[launch-week](https://supabase.com/blog/tags/launch-week)[supavisor](https://supabase.com/blog/tags/supavisor)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [What's Branching?](https://supabase.com/blog/supabase-branching#whats-branching)
    * [Support for Vercel Previews](https://supabase.com/blog/supabase-branching#support-for-vercel-previews)
    * [Developing on the hosted Preview Branch](https://supabase.com/blog/supabase-branching#developing-on-the-hosted-preview-branch)
    * [Database migrations](https://supabase.com/blog/supabase-branching#database-migrations)
    * [Data seeding](https://supabase.com/blog/supabase-branching#data-seeding)
  * [Future considerations](https://supabase.com/blog/supabase-branching#future-considerations)
    * [Declarative config](https://supabase.com/blog/supabase-branching#declarative-config)
    * [Automatic dashboard commits](https://supabase.com/blog/supabase-branching#automatic-dashboard-commits)
    * [Extended seeding behavior](https://supabase.com/blog/supabase-branching#extended-seeding-behavior)
    * [Copy-on-write](https://supabase.com/blog/supabase-branching#copy-on-write)
  * [Interested in using Branching?](https://supabase.com/blog/supabase-branching#interested-in-using-branching)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-branching&text=Supabase%20Branching)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-branching&text=Supabase%20Branching)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-branching&t=Supabase%20Branching)
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
![Each Git branch has a corresponding Supabase Preview.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Ffeat-branches-examples--dark.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

