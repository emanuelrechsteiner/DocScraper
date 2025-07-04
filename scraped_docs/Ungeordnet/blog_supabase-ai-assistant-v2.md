---
url: https://supabase.com/blog/supabase-ai-assistant-v2
scraped_at: 2025-05-25T09:48:44.648472
title: Supabase AI Assistant v2
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
# Supabase AI Assistant v2
02 Dec 2024
•
4 minute read
[![Saxon Fletcher avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaxonf.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Saxon FletcherProduct Design](https://github.com/saxonf)
[![Joshen Lim avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjoshenlim.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Joshen LimEngineering](https://github.com/joshenlim)
![Supabase AI Assistant v2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fthumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we are releasing Supabase Assistant v2 in the Dashboard - a global assistant with several new abilities:
  1. Postgres schema design
  2. Data queries and charting
  3. Error debugging
  4. Postgres RLS Policies: create and edit
  5. Postgres Functions: create and edit
  6. Postgres Triggers: create and edit
  7. SQL to `supabase-js` conversion


## A new, unified approach to AI[#](https://supabase.com/blog/supabase-ai-assistant-v2#a-new-unified-approach-to-ai)
Our new Assistant is more extensible, using a flexible system of components, tools, and APIs. You can provide context manually (e.g. an RLS Policy) or automatically based on whichever page you're visiting in the Dashboard (e.g. the specific table you're working on).
The result is a single panel that's persistent across the entire Dashboard. It sits alongside your workspace and can be called upon when needed (`cmd+i`!). It automatically retrieves context for your prompt and can be provided with extra context similar to other AI tools like Cursor and GitHub Copilot.
## New abilities in Supabase Assistant v2[#](https://supabase.com/blog/supabase-ai-assistant-v2#new-abilities-in-supabase-assistant-v2)
Let's take a look at new abilities in this release.
### Schema design[#](https://supabase.com/blog/supabase-ai-assistant-v2#schema-design)
If you are creating something new, the Assistant can guide or inspire you. It will show you how to structure your database and generate all the SQL queries to set it up.
![Design new database schemas](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fdesign.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Writing SQL[#](https://supabase.com/blog/supabase-ai-assistant-v2#writing-sql)
Like our previous Assistant, the new Assistant will help you write queries based on your schema. This version has better contextual understanding and can provide more accurate suggestions.
### Debug your queries[#](https://supabase.com/blog/supabase-ai-assistant-v2#debug-your-queries)
Writing SQL can be tough. You can use the new Assistant to debug database errors directly through the SQL Editor or within the Assistant panel.
![Debug your queries with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fdebug.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Discover data insights[#](https://supabase.com/blog/supabase-ai-assistant-v2#discover-data-insights)
The new Assistant can run queries directly. This can be a useful (and fun) way to query your data through natural language. Basic select queries run automatically, and results are displayed within the conversation in tabular form or chart form. The chart axis are picked intuitively by the Assistant. No data is sent to the underlying LLM, only your schema structure. This is a helpful tool for folks who are not comfortable with SQL but are still interested in analyzing data insights.
![Query data with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fquery.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### SQL to REST[#](https://supabase.com/blog/supabase-ai-assistant-v2#sql-to-rest)
Once your database is set up, you probably want to connect to it directly or with one of our client libraries. If you're using our `supabase-js` library, we've added a helpful tool to convert an SQL query to supabase-js client code. Simply ask the Assistant to convert a query, and it will respond with either a complete snippet for you to copy or a combination of function + RPC call. This is powered by the [sql-to-rest](https://supabase.com/docs/guides/api/sql-to-rest) tool.
![Convert SQL to supabase-js code](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fjs.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### RLS Policies: Protect your database[#](https://supabase.com/blog/supabase-ai-assistant-v2#rls-policies-protect-your-database)
Use the Assistant to suggest, create or modify RLS Policies. Simply explain the desired behavior and the Assistant will generate a new Policy using the context of your database schema and existing policies. To edit an existing policy, click “edit with Assistant” within your Policy list. The Assistant will be provided the appropriate context for you to start prompting.
![Create and edit RLS Policies with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fpolicy.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Postgres Functions and Triggers[#](https://supabase.com/blog/supabase-ai-assistant-v2#postgres-functions-and-triggers)
Suggest, create or update functions and triggers in a similar way to policies. Just describe what you want or select “Edit with Assistant” from your Function or Trigger list.
![Create and edit functions and triggers with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Ffunctions.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Feedback[#](https://supabase.com/blog/supabase-ai-assistant-v2#feedback)
This release gives us a foundation to build off and incorporate into other parts of your database journey. Where are you struggling the most when using Postgres? How might the Assistant help you? Send us your thoughts, ideas, concerns via the feedback form in the Dashboard.
## How to access[#](https://supabase.com/blog/supabase-ai-assistant-v2#how-to-access)
Supabase Assistant v2 is available today. Go to a Project and hit `cmd + i`, or alternatively click the Assistant icon in the top right toolbar.
[Launch Week13](https://supabase.com/launch-week/13)
2-6 December 24
[Day 1 -Supabase AI Assistant v2](https://supabase.com/blog/supabase-ai-assistant-v2)[Day 2 -Supabase Functions: Background Tasks and WebSockets](https://supabase.com/blog/edge-functions-background-tasks-websockets)[Day 3 -Supabase Cron: Schedule Recurring Jobs in Postgres](https://supabase.com/blog/supabase-cron)[Day 4 -Supabase Queues](https://supabase.com/blog/supabase-queues)[Day 5 -database.build v2: Bring-Your-Own-LLM](https://supabase.com/blog/database-build-v2)

Build Stage
[01 -OrioleDB Public Alpha](https://supabase.com/blog/orioledb-launch)[02 -Supabase CLI v2: Config as Code](https://supabase.com/blog/cli-v2-config-as-code)[03 -High Performance Disks](https://supabase.com/blog/high-performance-disks)[04 -Restore to a New Project](https://supabase.com/blog/restore-to-a-new-project)[05 -Hack the Base! with Supabase](https://supabase.com/blog/hack-the-base)[Community Meetups](https://supabase.com/events?category=meetup)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&text=Supabase%20AI%20Assistant%20v2)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&text=Supabase%20AI%20Assistant%20v2)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&t=Supabase%20AI%20Assistant%20v2)
[Last postSupabase Edge Functions: Introducing Background Tasks, Ephemeral Storage, and WebSockets3 December 2024](https://supabase.com/blog/edge-functions-background-tasks-websockets)
[Next postOrioleDB Public Alpha1 December 2024](https://supabase.com/blog/orioledb-launch)
[AI](https://supabase.com/blog/tags/AI)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [A new, unified approach to AI](https://supabase.com/blog/supabase-ai-assistant-v2#a-new-unified-approach-to-ai)
  * [New abilities in Supabase Assistant v2](https://supabase.com/blog/supabase-ai-assistant-v2#new-abilities-in-supabase-assistant-v2)
    * [Schema design](https://supabase.com/blog/supabase-ai-assistant-v2#schema-design)
    * [Writing SQL](https://supabase.com/blog/supabase-ai-assistant-v2#writing-sql)
    * [Debug your queries](https://supabase.com/blog/supabase-ai-assistant-v2#debug-your-queries)
    * [Discover data insights](https://supabase.com/blog/supabase-ai-assistant-v2#discover-data-insights)
    * [SQL to REST](https://supabase.com/blog/supabase-ai-assistant-v2#sql-to-rest)
    * [RLS Policies: Protect your database](https://supabase.com/blog/supabase-ai-assistant-v2#rls-policies-protect-your-database)
    * [Postgres Functions and Triggers](https://supabase.com/blog/supabase-ai-assistant-v2#postgres-functions-and-triggers)
  * [Feedback](https://supabase.com/blog/supabase-ai-assistant-v2#feedback)
  * [How to access](https://supabase.com/blog/supabase-ai-assistant-v2#how-to-access)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&text=Supabase%20AI%20Assistant%20v2)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&text=Supabase%20AI%20Assistant%20v2)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&t=Supabase%20AI%20Assistant%20v2)
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

