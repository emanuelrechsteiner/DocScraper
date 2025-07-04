---
url: https://supabase.com/blog/supabase-beta-may-2021
scraped_at: 2025-05-25T09:14:33.128262
title: Supabase Beta May 2021
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
# Supabase Beta May 2021
02 Jun 2021
•
4 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
![Supabase Beta May 2021](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Frelease-may-2021.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Apple & Twitter Logins, Supabase Grid, Go & Swift Libraries. Lots of great stuff to try out this month.
### Quick demo[#](https://supabase.com/blog/supabase-beta-may-2021#quick-demo)
Watch a full demo:
## Apple logins are now available[#](https://supabase.com/blog/supabase-beta-may-2021#apple-logins-are-now-available)
Did you know: if you ship an app to the App Store with any third-party logins, you're required to enable Apple logins as well? Now you can with Supabase Auth.
![Apple OAuth is now available in Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Fsupabase-apple-login.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Twitter logins are now available[#](https://supabase.com/blog/supabase-beta-may-2021#twitter-logins-are-now-available)
You can also use Twitter as an OAuth provider with Supabase Auth. Twitter has a very archaic OAuth implementation, so this one took awhile.
![Twitter OAuth is now available in Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Fsupabase-twitter-login.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## New storage policy editor[#](https://supabase.com/blog/supabase-beta-may-2021#new-storage-policy-editor)
We shipped a new Policy Editor for managing Row Level Security on your Storage. We provide some templates to simplify the process for new developers.
![New Policy Editor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Fstorage-policies.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Supabase Grid[#](https://supabase.com/blog/supabase-beta-may-2021#supabase-grid)
We are still working on Open Sourcing our Dashboard, and took another step closer by publicly releasing a new [Supabase Grid](https://github.com/supabase/grid). It's not ready to use outside of the Supabase ecosystem, but over time we hope to make it usable with any Postgres Database.
![This is an image of the new Supabase Grid](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Ftable-grid.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Japan (Tokyo) 🇯🇵 is now available as a region[#](https://supabase.com/blog/supabase-beta-may-2021#japan-tokyo--is-now-available-as-a-region)
There are a huge number of Supabase developers in Japan and China, and at their request we've launched Tokyo as a region.
![Tokyo is now availabel as a region](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Fjapan-region.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Return data as CSV[#](https://supabase.com/blog/supabase-beta-may-2021#return-data-as-csv)
You can now [retrieve your data](https://supabase.com/docs/reference/javascript/select#return-data-as-csv) as Comma Separated Values. Thanks to [@andreivreja](https://github.com/andreivreja) for the [awesome PR](https://github.com/supabase/postgrest-js/pull/187).
![Download data as a CSV](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Freturn-data-as-csv.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## New Go Libraries[#](https://supabase.com/blog/supabase-beta-may-2021#new-go-libraries)
The community started developing the Go libraries. [postgrest-go](https://github.com/supabase/postgrest-go) is completed, [@Yusuf_Papurcu](https://twitter.com/Yusuf_Papurcu) and [@muratmirgun](https://twitter.com/muratmirgun) are working on the remaining libraries.
![Supabase Go Libraries](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Fsupabase-go-support.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## New Swift Libraries[#](https://supabase.com/blog/supabase-beta-may-2021#new-swift-libraries)
The community started developing the Swift libraries too. [@satishbabariya](https://twitter.com/satishbabariya) is making huge progress on [`storage-swift`](https://github.com/supabase/storage-swift), [`gotrue-swift`](https://github.com/supabase/gotrue-swift), [`realtime-swift`](https://github.com/supabase/realtime-swift), and [`supabase-swift`](https://github.com/supabase/supabase-swift).
![Supabase Swift Libraries](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Fsupabase-swift-support.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Build in Public[#](https://supabase.com/blog/supabase-beta-may-2021#build-in-public)
We started a weekly 1-hour live stream where we build in public.
  * [Build in Public 001](https://www.youtube.com/watch?v=p561ogKZ63o): Building a "Next.js + Supabase" Tutorial
  * [Build in Public 002](https://twitter.com/p_phiri/status/1397815806990372865?s=20): `maybeSingle()` and "React + Supabase" Tutorial


## Community[#](https://supabase.com/blog/supabase-beta-may-2021#community)
  * `@p_phiri` made his first OSS contribution, and documented it on YouTube. [Twitter](https://twitter.com/p_phiri/status/1397815806990372865?s=20).
  * `@sonnylazuardi` built an awesome 3d globe using Supabase. [Twitter](https://twitter.com/sonnylazuardi/status/1397141285664792578?s=20).
  * `@yallurium` released Part 2 of "Going Full Stack with Flutter and Supabase". [Twitter](https://twitter.com/yallurium/status/1396850742724632582?s=20).
  * `@coderinblack` built an Audio Social Platform using Supabase. [Twitter](https://twitter.com/coderinblack/status/1396199050207121408).
  * `@adityathakurxd` built a Flutter + Supabase starter kit. [GitHub](https://github.com/adityathakurxd/supabase_flutter).
  * `@dshukertjr` built a geo-tagged video sharing app with Flutter + Supabase. [GitHub](https://github.com/dshukertjr/spot)
  * `@JonoYeong` created a 6-minute overview of Supabase. [YouTube](https://www.youtube.com/watch?v=1F240hR7nHU). [Twitter](https://twitter.com/JonoYeong/status/1398451556723294208).
  * Everyone who has produced Supabase content is now receiving their [swag](https://twitter.com/coderinblack/status/1397042488586559490?s=20). Send a link to your blog, app, or video to swag@supabase.io along with your address and we'll make sure you're included in the next drop.


**Supabase GitHub Star Growth**
![13223 stars on GitHub.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-may%2Fsupabase-stars-may-2021.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Source: [repository.surf/supabase](https://repository.surf/supabase)
If you want to keep up to date, make sure you [subscribe to our YouTube channel](https://www.youtube.com/c/supabase) or [follow us on Twitter](https://twitter.com/supabase).
## Coming Next[#](https://supabase.com/blog/supabase-beta-may-2021#coming-next)
We're planning another Launch Week at the end of July. We'll probably have a quiet month of shipping this month so that we can get everything prepared for July.
### Get started[#](https://supabase.com/blog/supabase-beta-may-2021#get-started)
  * Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
  * Make sure to [star us on GitHub](https://github.com/supabase/supabase)
  * Follow us [on Twitter](https://twitter.com/supabase)
  * Subscribe to our [YouTube channel](https://www.youtube.com/c/supabase)
  * Become a [sponsor](https://github.com/sponsors/supabase)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-may-2021&text=Supabase%20Beta%20May%202021)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-may-2021&text=Supabase%20Beta%20May%202021)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-may-2021&t=Supabase%20Beta%20May%202021)
[Last postProtecting reserved roles with PostgreSQL Hooks2 July 2021](https://supabase.com/blog/roles-postgres-hooks)
[Next postSupabase Beta June 20212 June 2021](https://supabase.com/blog/supabase-beta-june-2021)
[release-notes](https://supabase.com/blog/tags/release-notes)
On this page
  * [Apple logins are now available](https://supabase.com/blog/supabase-beta-may-2021#apple-logins-are-now-available)
  * [Twitter logins are now available](https://supabase.com/blog/supabase-beta-may-2021#twitter-logins-are-now-available)
  * [New storage policy editor](https://supabase.com/blog/supabase-beta-may-2021#new-storage-policy-editor)
  * [Supabase Grid](https://supabase.com/blog/supabase-beta-may-2021#supabase-grid)
  * [Japan (Tokyo) 🇯🇵 is now available as a region](https://supabase.com/blog/supabase-beta-may-2021#japan-tokyo-%F0%9F%87%AF%F0%9F%87%B5-is-now-available-as-a-region)
  * [Return data as CSV](https://supabase.com/blog/supabase-beta-may-2021#return-data-as-csv)
  * [New Go Libraries](https://supabase.com/blog/supabase-beta-may-2021#new-go-libraries)
  * [New Swift Libraries](https://supabase.com/blog/supabase-beta-may-2021#new-swift-libraries)
  * [Build in Public](https://supabase.com/blog/supabase-beta-may-2021#build-in-public)
  * [Community](https://supabase.com/blog/supabase-beta-may-2021#community)
  * [Coming Next](https://supabase.com/blog/supabase-beta-may-2021#coming-next)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-may-2021&text=Supabase%20Beta%20May%202021)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-may-2021&text=Supabase%20Beta%20May%202021)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-may-2021&t=Supabase%20Beta%20May%202021)
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

