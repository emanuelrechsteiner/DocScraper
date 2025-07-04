---
url: https://supabase.com/blog/supabase-studio-3-0
scraped_at: 2025-05-25T09:23:11.803837
title: Supabase Studio 3.0: AI SQL Editor, Schema Diagrams, and new Wrappers
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
# Supabase Studio 3.0: AI SQL Editor, Schema Diagrams, and new Wrappers
09 Aug 2023
•
8 minute read
[![Alaister Young avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Falaister.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Alaister YoungEngineering](https://github.com/alaister)
[![Greg Richardson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgregnr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Greg RichardsonEngineering](https://github.com/gregnr)
[![Joshen Lim avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjoshenlim.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Joshen LimEngineering](https://github.com/joshenlim)
![Supabase Studio 3.0: AI SQL Editor, Schema Diagrams, and new Wrappers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-3%2Fthumb-day3.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase Studio 3.0 is here, with some huge new features, including a brand new Supabase AI, integrated right into our SQL Editor. If you hate writing SQL, you'll love this update.
Here's the highlight reel:
  * [**Supabase AI in the SQL Editor**](https://supabase.com/blog/supabase-studio-3-0#supabase-ai-right-in-the-sql-editor): inline AI, always ready to help
  * [**Schema Visualizer**](https://supabase.com/blog/supabase-studio-3-0#schema-visualizer): — see all your table schemas visually.
  * [**Role Management**](https://supabase.com/blog/supabase-studio-3-0#role-management): — fine-grained access to table data
  * [**Shared SQL Snippets**](https://supabase.com/blog/supabase-studio-3-0#shared-sql-snippets): — share your snippets with the team
  * [**Database Migration UI**](https://supabase.com/blog/supabase-studio-3-0#database-migration-ui): — your database, with receipts
  * [**Wrappers UI**](https://supabase.com/blog/supabase-studio-3-0#wrappers-ui): — easily query foreign data


## Supabase AI, right in the SQL Editor[#](https://supabase.com/blog/supabase-studio-3-0#supabase-ai-right-in-the-sql-editor)
In Launch Week 7, [we added Supabase AI to the Studio](https://supabase.com/blog/supabase-studio-2.0). Through our ⌘K menu, you could ask Supabase AI to do all sorts of common tasks — create tables, views, and indexes, write database functions, write RLS policies, and more.
After this release, we had two key realizations:
  1. people love having computers write their SQL for them!
  2. many of you are using the SQL Editor as the heart (and engine!) of your projects.


Today, we're releasing a huge improvement to our SQL Editor. First up, we've added Supabase AI directly into the editor. It's always accessible, and ready to help. As before, you can give it a prompt (`create an orders table for me`) and it will return the SQL for you, but now it does so much more.
Supabase AI is aware of the SQL snippet in the editor and can modify it for you. You can ask it to change `customers` to `customer_orders`, for example. You can interact with the code the same way you would converse with ChatGPT until it's just right.
![Create a table](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-3%2Fcreate-orders.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Next, we've added a diff view for changes that Supabase AI makes to your SQL snippet. You can tell Supabase AI what you want changed, and visualize it as you would a Git diff. From this view, you can accept or reject the diffs, and keep asking Supabase AI to make changes until you're satisfied.
![Create a table diff](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-3%2Fcreate-orders-diff.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've wondered for a long time how to make it easier to teach developers how to use SQL. It's fortunate we didn't solve this problem too quickly, as it turns out that AI does a much better job than we could do ourselves.
With Supabase AI, you won't even need the whole weekend to scale to millions. Head over to the [SQL Editor](https://supabase.com/dashboard/project/_/sql) and give it a try!
In the coming months, we're looking to sprinkle Supabase AI through more parts of the Studio. With Postgres under the hood, there's so much we can do with SQL and a little bit of AI to help you move fast. Keep an eye out for the Supabase AI icon, you never know where it will pop up next.
![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fsupabase-ai-loading-animation.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Along with these huge AI features, we also added a bunch of new improvements elsewhere around the Studio. Several of these features have come either from requests from the community or are contributions by community members themselves.
📢 Many of the features and enhancements below came from user requests [Please keep them coming](https://github.com/orgs/supabase/discussions/categories/feature-requests)!
## Schema Visualizer[#](https://supabase.com/blog/supabase-studio-3-0#schema-visualizer)
![Schema Visualizer](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-3%2Fvisualizer.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
For a while now, many Supabase users have been using [Zernonia's](https://github.com/zernonia) [Supabase Schema visualization tool](https://supabase-schema.vercel.app/). While this was an amazing tool, many users wanted to see something like this directly integrated into the Studio.
We opened an [Issue for it on Github](https://github.com/supabase/supabase/issues/15585) and within a day or two the wheels were in motion. After a couple of weeks, the feature was polished up and merged. It's inspiring to see the power of open source at work. This feature wasn't trivial, and to see community members take it from feature request to production in just a couple of weeks is mind-blowing. Unquestionably, we have one of the best open source communities out there. Huge thanks to [kamilogorek](https://github.com/kamilogorek) and [adiologydev](https://github.com/adiologydev) for their work on this!
Special thanks as well to [Zernonia](https://twitter.com/zernonia) for providing the inspiration for this great new feature! OSS FTW.
## Role Management[#](https://supabase.com/blog/supabase-studio-3-0#role-management)
Postgres has built-in support for managing users and roles, and this release, we're happy to release a UI for it in the Studio. This is another extremely common feature request, fulfilled almost completely by a community member.
A few months back, we saw this [PR](https://github.com/supabase/supabase/pull/13745) come in out of the blue from [HTMHell](https://github.com/HTMHell). They built the entire thing with zero help or direction from our team. We were blown away. We had some changes to make on the backend to properly accommodate the UI, and now we're almost ready to get this out into the wild!
![Role management](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-3%2Frole-management.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Due to the security focus of this feature, we want to make sure we do a very thorough job of testing, so we're hoping to make this generally available in the next week or so.
Massive thanks to [HTMHell](https://github.com/HTMHell) (amazing handle btw) for the work on this!
## Shared SQL Snippets[#](https://supabase.com/blog/supabase-studio-3-0#shared-sql-snippets)
Speaking of commonly requested features, this one has to be in the all-time top 5. Your beautiful, hand-crafted SQL snippets used to be yours and yours alone. Now you can share them with team members and let them bask in your technical prowess.
![Share SQL Snippets](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-3%2Fshare-query.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You can create a set of project-wide snippets for doing common tasks, making it faster to collaborate and build. To share a snippet, just take a personal snippet that ~~Supabase AI~~ you wrote and share it with the project. It will show up in a new Project Snippets list that's visible to everyone on the team.
Teamwork makes the dream work!
## Database Migration UI[#](https://supabase.com/blog/supabase-studio-3-0#database-migration-ui)
We're releasing a new UI for working with database migrations right from the Studio. Database migrations give you a way to update your database using version-controlled SQL files. They describe changes that you want to make to your database, and also keep track of what changes have been made to your database over time.
As migrations get run against your project from the CLI, you can see information in the Studio about when the migration was run, by who and what changes were made. [See the documentation](https://supabase.com/docs/guides/deployment/database-migrations) to get started with migrations.
![Migrations UI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-3%2Fmigrations.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Wrappers UI[#](https://supabase.com/blog/supabase-studio-3-0#wrappers-ui)
During Launch Week 6, we [announced](https://supabase.com/blog/postgres-foreign-data-wrappers-rust) Supabase Wrappers — a framework for building foreign data wrappers with Postgres. Wrappers allow your Supabase project to act as a one-stop hub for your data.
When we released Wrappers, we had support for just two providers — Stripe and Firebase. We're now up to 6! This round, we're happy to release support for S3, ClickHouse, BigQuery, and Logflare! Wrappers add a mind-bending level of extensibility to Supabase projects. You can pull data straight into your projects as though they were normal Supabase tables — you can even query them with our client libraries. It's a whole new world of possibilities.
![Wrappers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-3%2Fwrappers.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Wrapping Up[#](https://supabase.com/blog/supabase-studio-3-0#wrapping-up)
We hope you get a lot of value out of these new features and enhancements. As we mentioned earlier, many of the features listed here came directly from [Feature Requests](https://github.com/orgs/supabase/discussions/categories/feature-requests) on GitHub. Thanks to everyone who has taken the time to submit these, and encourage submissions for anything else you'd like to see.
## More Launch Week 8[#](https://supabase.com/blog/supabase-studio-3-0#more-launch-week-8)
  * [Supabase Local Dev: migrations, branching, and observability](https://supabase.com/blog/supabase-local-dev)
  * [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
  * [Launch Week 8](https://supabase.com/launch-week)
  * [Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber)
  * [Why we'll stay remote](https://supabase.com/blog/why-supabase-remote)
  * [Postgres Language Server](https://github.com/supabase/postgres_lsp)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-3-0&text=Supabase%20Studio%203.0%3A%20AI%20SQL%20Editor%2C%20Schema%20Diagrams%2C%20and%20new%20Wrappers)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-3-0&text=Supabase%20Studio%203.0%3A%20AI%20SQL%20Editor%2C%20Schema%20Diagrams%2C%20and%20new%20Wrappers)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-3-0&t=Supabase%20Studio%203.0%3A%20AI%20SQL%20Editor%2C%20Schema%20Diagrams%2C%20and%20new%20Wrappers)
[Last postVercel Integration and Next.js App Router Support10 August 2023](https://supabase.com/blog/using-supabase-with-vercel)
[Next postSupabase Local Dev: migrations, branching, and observability8 August 2023](https://supabase.com/blog/supabase-local-dev)
[launch-week](https://supabase.com/blog/tags/launch-week)[studio](https://supabase.com/blog/tags/studio)[AI](https://supabase.com/blog/tags/AI)
On this page
  * [Supabase AI, right in the SQL Editor](https://supabase.com/blog/supabase-studio-3-0#supabase-ai-right-in-the-sql-editor)
  * [Schema Visualizer](https://supabase.com/blog/supabase-studio-3-0#schema-visualizer)
  * [Role Management](https://supabase.com/blog/supabase-studio-3-0#role-management)
  * [Shared SQL Snippets](https://supabase.com/blog/supabase-studio-3-0#shared-sql-snippets)
  * [Database Migration UI](https://supabase.com/blog/supabase-studio-3-0#database-migration-ui)
  * [Wrappers UI](https://supabase.com/blog/supabase-studio-3-0#wrappers-ui)
  * [Wrapping Up](https://supabase.com/blog/supabase-studio-3-0#wrapping-up)
  * [More Launch Week 8](https://supabase.com/blog/supabase-studio-3-0#more-launch-week-8)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-3-0&text=Supabase%20Studio%203.0%3A%20AI%20SQL%20Editor%2C%20Schema%20Diagrams%2C%20and%20new%20Wrappers)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-3-0&text=Supabase%20Studio%203.0%3A%20AI%20SQL%20Editor%2C%20Schema%20Diagrams%2C%20and%20new%20Wrappers)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-3-0&t=Supabase%20Studio%203.0%3A%20AI%20SQL%20Editor%2C%20Schema%20Diagrams%2C%20and%20new%20Wrappers)
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

