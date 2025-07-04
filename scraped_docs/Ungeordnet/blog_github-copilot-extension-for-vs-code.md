---
url: https://supabase.com/blog/github-copilot-extension-for-vs-code
scraped_at: 2025-05-25T08:43:09.176763
title: Official Supabase extension for VS Code and GitHub Copilot
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
# Official Supabase extension for VS Code and GitHub Copilot
12 Aug 2024
•
3 minute read
[![Anas Araid avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fanas-araid.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Anas AraidGuest Author](https://github.com/anas-araid)
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Official Supabase extension for VS Code and GitHub Copilot](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-1%2Fgithub_copilot_extension-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we're launching a new [GitHub Copilot extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Supabase.vscode-supabase-extension) to make your development with Supabase and VS Code even more delightful, starting with a Copilot-guided experience for [database migrations](https://supabase.com/docs/guides/deployment/database-migrations).
![Database Migrations Demo](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-1%2Fcopilot_migration.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The foundation for this extension was created by [Anas Araid](https://github.com/anas-araid) during a previous [Launch Week Hackathon](https://twitter.com/anas_araid/status/1736641409094988033). Impressed with their work, we partnered with them to add a ["Chat Participant"](https://code.visualstudio.com/api/extension-guides/chat), an exciting [new feature recently launched](https://code.visualstudio.com/blogs/2024/06/24/extensions-are-all-you-need) by the GitHub and VS Code teams at Microsoft.
## Features[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#features)
The VS Code extension is quite feature rich:
### GitHub Copilot Chat Participant[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#github-copilot-chat-participant)
The extension provides a [Chat Participant](https://code.visualstudio.com/api/extension-guides/chat) for GitHub Copilot to help with your Supabase questions. Simply type `@supabase` in your Copilot Chat and the extension will include your database schema as context to Copilot.
![Copilot Chat integration demo](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-1%2Fcopilot_chat.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Copilot-guided database migrations[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#copilot-guided-database-migrations)
The extension provides a guided experience to create and apply [database migrations](https://supabase.com/docs/guides/deployment/database-migrations). Simply type `@supabase /migration <describe what you want to do>` in your Copilot Chat and the extension will generate a new SQL migration for you.
![Copilot guided database migrations demo](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-1%2Fcopilot_migration.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Inspect tables & views[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#inspect-tables--views)
Inspect your tables and views, including their columns, types, and data, directly from the editor:
![View tables and views](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-1%2Ftable_view.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### List database migrations[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#list-database-migrations)
See the migration history of your database:
![Migration History](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-1%2Fmigration_history.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Inspect database functions[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#inspect-database-functions)
Inspect your database functions and their SQL definitions:
![Database functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-1%2Fdatabase_functions.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### List Storage buckets[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#list-storage-buckets)
List the Storage buckets in your Supabase project.
![Storage buckets](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-1%2Fstorage-buckets.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## What's Next?[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#whats-next)
We're excited to continue adding more features that will make your development experience with Supabase even more delightful - and for this we need your help! If you have any feedback, feature requests, or bug reports, please [open an issue on GitHub](https://github.com/supabase-community/supabase-vscode-extension/issues).
The extension requires you to have the Supabase CLI installed and have your project running locally. In a future release, we will integrate the [Supabase Management API](https://supabase.com/docs/reference/api/introduction) into the extension to make connecting to your hosted Supabase projects as seamless as possible.
## Contributing to Supabase[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#contributing-to-supabase)
The entire Supabase stack is [fully open source](https://supabase.com/open-source), including [this extension](https://github.com/supabase-community/supabase-vscode-extension). In fact, this extension was originally created by [Anas Araid](https://github.com/anas-araid) during a [previous Launch Week Hackathon](https://twitter.com/anas_araid/status/1736641409094988033).
Your contributions, feedback, and engagement in the Supabase community are invaluable, and play a significant role in shaping our future. Thank you for your support!
## Resources[#](https://supabase.com/blog/github-copilot-extension-for-vs-code#resources)
  * [Install the extension](https://marketplace.visualstudio.com/items?itemName=Supabase.vscode-supabase-extension)
  * [Read the source code](https://github.com/supabase-community/supabase-vscode-extension)
  * [Submit a Feature Request](https://github.com/supabase-community/supabase-vscode-extension/issues)
  * [Get started with Supabase](https://database.new)


[Launch Week12](https://supabase.com/launch-week/12)
12-16 August
[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage
[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)[02 -pg_replicate](https://news.ycombinator.com/item?id=41209994)[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)[06 -vec2pg](https://supabase.com/blog/vec2pg)[07 -pg_graphql](https://supabase.com/blog/pg-graphql-1-5-7)[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)[09 -python-support](https://supabase.com/blog/python-support)[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgithub-copilot-extension-for-vs-code&text=Official%20Supabase%20extension%20for%20VS%20Code%20and%20GitHub%20Copilot)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgithub-copilot-extension-for-vs-code&text=Official%20Supabase%20extension%20for%20VS%20Code%20and%20GitHub%20Copilot)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fgithub-copilot-extension-for-vs-code&t=Official%20Supabase%20extension%20for%20VS%20Code%20and%20GitHub%20Copilot)
[Last postSupabase Realtime: Broadcast and Presence Authorization13 August 2024](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)
[Next postpostgres.new: In-browser Postgres with an AI interface12 August 2024](https://supabase.com/blog/postgres-new)
[launch-week](https://supabase.com/blog/tags/launch-week)
On this page
  * [Features](https://supabase.com/blog/github-copilot-extension-for-vs-code#features)
    * [GitHub Copilot Chat Participant](https://supabase.com/blog/github-copilot-extension-for-vs-code#github-copilot-chat-participant)
    * [Copilot-guided database migrations](https://supabase.com/blog/github-copilot-extension-for-vs-code#copilot-guided-database-migrations)
    * [Inspect tables & views](https://supabase.com/blog/github-copilot-extension-for-vs-code#inspect-tables--views)
    * [List database migrations](https://supabase.com/blog/github-copilot-extension-for-vs-code#list-database-migrations)
    * [Inspect database functions](https://supabase.com/blog/github-copilot-extension-for-vs-code#inspect-database-functions)
    * [List Storage buckets](https://supabase.com/blog/github-copilot-extension-for-vs-code#list-storage-buckets)
  * [What's Next?](https://supabase.com/blog/github-copilot-extension-for-vs-code#whats-next)
  * [Contributing to Supabase](https://supabase.com/blog/github-copilot-extension-for-vs-code#contributing-to-supabase)
  * [Resources](https://supabase.com/blog/github-copilot-extension-for-vs-code#resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgithub-copilot-extension-for-vs-code&text=Official%20Supabase%20extension%20for%20VS%20Code%20and%20GitHub%20Copilot)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgithub-copilot-extension-for-vs-code&text=Official%20Supabase%20extension%20for%20VS%20Code%20and%20GitHub%20Copilot)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fgithub-copilot-extension-for-vs-code&t=Official%20Supabase%20extension%20for%20VS%20Code%20and%20GitHub%20Copilot)
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

