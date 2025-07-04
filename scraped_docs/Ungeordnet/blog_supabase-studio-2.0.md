---
url: https://supabase.com/blog/supabase-studio-2.0
scraped_at: 2025-05-25T09:27:12.342310
title: Supabase Studio 2.0: help when you need it most
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
# Supabase Studio 2.0: help when you need it most
14 Apr 2023
•
8 minute read
[![Alaister Young avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Falaister.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Alaister YoungEngineering](https://github.com/alaister)
[![Joshen Lim avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjoshenlim.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Joshen LimEngineering](https://github.com/joshenlim)
[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Jonny Summers-MuirProduct Design](https://github.com/mildtomato)
[![Terry Sutton avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaltcod.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Terry SuttonEngineering](https://github.com/saltcod)
![Supabase Studio 2.0: help when you need it most](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-supabase-studio-2.0%2Fday-5-supabase-studio-2.0-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we're announcing Supabase Studio 2.0, packed with a ton of new stuff. We have features people have been asking for forever, and new capabilities that will change the way you work.
Here's the birds-eye-view:
  * [**Supabase AI**](https://supabase.com/blog/supabase-studio-2.0#supabase-ai--assisted-database-development): ChatGPT, right in the Studio
  * [**GraphiQL**](https://supabase.com/blog/supabase-studio-2.0#graphiql): Query your database with GraphQL
  * [**Cascade deletes**](https://supabase.com/blog/supabase-studio-2.0#cascade-deletes): Our #1 most requested feature from the community
  * [**Query Performance**](https://supabase.com/blog/supabase-studio-2.0#query-performance): Investigate slow running queries
  * [**Foreign key Selector**](https://supabase.com/blog/supabase-studio-2.0#foreign-key-selector): Look up a row in reference table
  * [**Postgres Roles**](https://supabase.com/blog/supabase-studio-2.0#postgres-roles): Manage your Postgres roles and privileges
  * [**Database Webhooks**](https://supabase.com/blog/supabase-studio-2.0#database-webhooks): Database triggers for Edge Functions
  * [**Table/View definitions**](https://supabase.com/blog/supabase-studio-2.0#tableview-definitions): View SQL definitions for tables and views
  * [**API Autodocs**](https://supabase.com/blog/supabase-studio-2.0#api-autodocs): View auto-generated docs right from the Table Editor
  * [**Support for many tables**](https://supabase.com/blog/supabase-studio-2.0#support-for-many-tables): Table Editor now supports 1000s of tables
  * [**JSON editing**](https://supabase.com/blog/supabase-studio-2.0#json-editing): Improved JSON editing
  * [**Nullable columns**](https://supabase.com/blog/supabase-studio-2.0#nullable-columns): Allow text/bool cells to be null or empty


## Supabase AI — assisted database development[#](https://supabase.com/blog/supabase-studio-2.0#supabase-ai--assisted-database-development)
One of our guiding principles at Supabase is to make SQL more accessible to developers. We don't want to just abstract it away with a custom implementation. By embracing SQL, developers learn important, transferable skills while they build on top of Supabase.
In the past few months, AI advancements have made this easy! Writing a complex SQL query is now as simple as asking ChatGPT, and we're leaning into this approach with our Studio. AI gives developers superpowers, and by providing relevant context, Supabase gives AI superpowers.
AI has already changed a lot about the way we work as developers. We can use ChatGPT to write code for us as fast as we can prompt it. We wanted to bring this power into the Studio with integrations that will help you work even faster than before.
Today you'll be able to do many common SQL operations with the help of AI. You can create tables, views and indexes, write functions and triggers, and more, right from the ⌘K menu.
Soon, we'll also let you opt-in to sending your table schemas to OpenAI to help fine tune queries to your project. All this should result in a dramatic boost in development speed. Maybe you'll only need half a weekend to scale to millions now!
As with every ⌘K menu, quick navigation is at the heart of things. You'll now be able to jump to any page in the Studio in a couple of keystrokes. You can also search the Docs directly from the menu.
We'll be actively working on our ⌘K menu in the coming months to make it faster and even more useful for you. Next, we're going to focus on better support for writing RLS policies. Stay tuned, and make sure to explore how we're integrating AI [behind the scenes](https://supabase.com/blog/tags/AI)!
Huge props for the amazing work done on the [⌘K package](https://cmdk.paco.me/) we've built on top of here.
Along with the new AI features, we also doubled-down on some of the critical missing pieces for a Postgres UI. Before we started to work on any of these, we combed through user feedback and tallied up the most submitted Feature Requests on GitHub.
📢 Many of the features and enhancements below came from user requests — [please keep them coming](https://github.com/orgs/supabase/discussions/categories/feature-requests)!
## GraphiQL[#](https://supabase.com/blog/supabase-studio-2.0#graphiql)
![Logs UI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw7-studio%2Fgraphiql.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
While GraphQL has been available in Supabase for just over a year, we haven't provided a visual tool for using it. You can now use the very popular GraphiQL directly from the Studio. GraphiQL is a browser tool for writing, validating, and testing GraphQL testing. Being able to use a fully integrated GraphQL IDE is a huge DX win.
## Cascade deletes[#](https://supabase.com/blog/supabase-studio-2.0#cascade-deletes)
Cascade deletes are a core feature of Postgres, but have not been available in the Studio UI until now. This has been the #1 feature request from the community for a long time. You can now choose what you want to happen when deleting a referenced row in another table, right from Table Editor side panel.
## Query Performance[#](https://supabase.com/blog/supabase-studio-2.0#query-performance)
![Logs UI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw7-studio%2Fquery-performance.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've just released a new Query Performance tool to help you identify slow queries. Using this tool, along with our new [guide](https://supabase.com/docs/guides/platform/performance#examining-query-performance) should help you speed things up. These tools can help you uncover where you might have inefficient queries or schemas, or where you might need indexes or even additional compute resources.
## Foreign key selector[#](https://supabase.com/blog/supabase-studio-2.0#foreign-key-selector)
You can now select a referencing row from another table, rather than having to pass a value manually. You can also quickly jump to the row being referenced in another table with the _View referencing_ record button from the grid itself.
## Postgres Roles[#](https://supabase.com/blog/supabase-studio-2.0#postgres-roles)
![Logs UI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw7-studio%2Froles.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The Roles page got a huge revision, making it easy for you to manage access control through users, groups, and permissions. It's now easy to see how many connections you're using and where they're coming from.
## Database Webhooks[#](https://supabase.com/blog/supabase-studio-2.0#database-webhooks)
![Logs UI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw7-studio%2Fwebhooks.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've wanted to improve the webhooks interface for a long time, and we've finally gotten to it. We now have full support for editing your webhooks, and you can now select an edge function to call instead of having to pass in a url. We're happy to roll this very common request out to the community.
## Table/View definitions[#](https://supabase.com/blog/supabase-studio-2.0#tableview-definitions)
![Logs UI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw7-studio%2Fdefinitions.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You can now see the SQL definitions for your tables and views, directly from the Table Editor. This is a great way to see how Supabase is translating your UI changes into SQL. This can be useful for creating migrations, getting help, or just for learning more about how Supabase and SQL works.
## API Autodocs[#](https://supabase.com/blog/supabase-studio-2.0#api-autodocs)
![Logs UI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw7-studio%2Fapi-autodocs.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You can now view the auto-generated API docs right from the Table Editor. Grab the SQL and `supabase-js` code for all of the CRUD operations, straight from the table. You can also quickly generate and download a Typescript types file for your table, right from the editor.
### Quality of life improvements[#](https://supabase.com/blog/supabase-studio-2.0#quality-of-life-improvements)
#### Support for many tables[#](https://supabase.com/blog/supabase-studio-2.0#support-for-many-tables)
Previously, the Table Editor would get slow and unresponsive when you had many tables. We've made a number of improvements to make it much faster and more responsive. Feel free to make all the tables you need!
#### JSON editing[#](https://supabase.com/blog/supabase-studio-2.0#json-editing)
You've always been able to use the JSON data type in your tables, but editing the data wasn't easy. We've improved the inline Table Editor, and also now allow you open json cells from the side panel for a more spacious editing experience. Next Launch Week we're hoping to decide if it's pronounced “Jason” or “Jay-sawn”. Stay tuned.
#### Nullable columns[#](https://supabase.com/blog/supabase-studio-2.0#nullable-columns)
Speaking of extremely common feature requests, we've gotten this one a lot in the past few months. You used to have to handle this manually, but now you can now allow text/boolean cells to be null or empty. Supabase, where productivity is more than just an empty (or null) promise.
## Wrapping Up[#](https://supabase.com/blog/supabase-studio-2.0#wrapping-up)
We hope you get a lot of value out of these new features and enhancements. As we mentioned earlier, many of the features listed here came directly from [Feature Requests](https://github.com/orgs/supabase/discussions/categories/feature-requests) on GitHub. Thanks to everyone who have taken the time to submit these, and encourage submissions for anything else you'd like to see.
### More Launch Week 7
[Designing with AI![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fai-images%2F00-ai-images-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/designing-with-ai-midjourney)
[Supavisor![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fsupavisor%2Fsupavisor-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://github.com/supabase/supavisor)
[Open Source Logging![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday1%2Fself-hosted-logs-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-logs-self-hosted)
[Self-hosted Deno Edge Functions![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday2%2Fself-hosted-edge-functions-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)
[Storage v3: Resumable Uploads with support for 50GB files![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday3%2Fstorage-v3-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/storage-v3-resumable-uploads)
[Supabase Auth: SSO, Mobile, and Server-side support![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday4%2Fsso-support-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-auth-sso-pkce)
[Community Highlight![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fcommunity%2Fcommunity-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/launch-week-7-community-highlights)
[Studio Updates![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fstudio%2Fstudio-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-studio-2.0)
[dbdev![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2Fdbdev-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/dbdev)
[Postgres TLE![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2FpgTLE-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/pg-tle)
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-2.0&text=Supabase%20Studio%202.0%3A%20help%20when%20you%20need%20it%20most)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-2.0&text=Supabase%20Studio%202.0%3A%20help%20when%20you%20need%20it%20most)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-2.0&t=Supabase%20Studio%202.0%3A%20help%20when%20you%20need%20it%20most)
[Last postTrusted Language Extensions for Postgres14 April 2023](https://supabase.com/blog/pg-tle)
[Next postSupabase Auth: SSO, Mobile, and Server-side support13 April 2023](https://supabase.com/blog/supabase-auth-sso-pkce)
[launch-week](https://supabase.com/blog/tags/launch-week)[studio](https://supabase.com/blog/tags/studio)
On this page
  * [Supabase AI — assisted database development](https://supabase.com/blog/supabase-studio-2.0#supabase-ai--assisted-database-development)
  * [GraphiQL](https://supabase.com/blog/supabase-studio-2.0#graphiql)
  * [Cascade deletes](https://supabase.com/blog/supabase-studio-2.0#cascade-deletes)
  * [Query Performance](https://supabase.com/blog/supabase-studio-2.0#query-performance)
  * [Foreign key selector](https://supabase.com/blog/supabase-studio-2.0#foreign-key-selector)
  * [Postgres Roles](https://supabase.com/blog/supabase-studio-2.0#postgres-roles)
  * [Database Webhooks](https://supabase.com/blog/supabase-studio-2.0#database-webhooks)
  * [Table/View definitions](https://supabase.com/blog/supabase-studio-2.0#tableview-definitions)
  * [API Autodocs](https://supabase.com/blog/supabase-studio-2.0#api-autodocs)
    * [Quality of life improvements](https://supabase.com/blog/supabase-studio-2.0#quality-of-life-improvements)
  * [Wrapping Up](https://supabase.com/blog/supabase-studio-2.0#wrapping-up)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-2.0&text=Supabase%20Studio%202.0%3A%20help%20when%20you%20need%20it%20most)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-2.0&text=Supabase%20Studio%202.0%3A%20help%20when%20you%20need%20it%20most)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-studio-2.0&t=Supabase%20Studio%202.0%3A%20help%20when%20you%20need%20it%20most)
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

