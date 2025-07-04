---
url: https://supabase.com/blog/supabase-swift
scraped_at: 2025-05-25T09:19:41.300312
title: Supabase Swift
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
# Supabase Swift
15 Apr 2024
•
2 minute read
[![Guilherme Souza avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgrdsdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Guilherme SouzaEngineering](https://github.com/grdsdev)
![Supabase Swift](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-11%2Fswift%2Fthumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We are excited to announce that Supabase Swift libraries are now officially supported by Supabase.
This makes it simple to interact with Supabase from applications on Apple's platforms, including iOS, macOS, watchOS, tvOS, and visionOS:
`
1
let url = URL(string: "...")!
2
let anonKey = "public-anon-key"
3
let client = SupabaseClient(supabaseURL: url, supabaseKey: anonKey)
45
struct Country: Decodable {
6
 let id: Int
7
 let name: String
8
}
910
let countries: [Country] = try await supabase.from("countries")
11
 .select()
12
 .execute()
13
 .value
`
## New features[#](https://supabase.com/blog/supabase-swift#new-features)
This release includes the following new features:
  * WhatsApp OTP: <https://github.com/supabase/supabase-swift/pull/287>
  * Captcha support: <https://github.com/supabase/supabase-swift/pull/276>
  * SSO: <https://github.com/supabase/supabase-swift/pull/289>
  * Simplified Storage uploads: <https://github.com/supabase/supabase-swift/pull/290>
  * Anonymous sign-ins: <https://github.com/supabase-community/supabase-swift/releases/tag/v2.6.0>
  * Simplified OAuth: <https://github.com/supabase/supabase-swift/pull/299>


## What does official support mean?[#](https://supabase.com/blog/supabase-swift#what-does-official-support-mean)
Swift developers can now integrate Supabase services seamlessly with official support. This means:
  * **Direct assistance from the Supabase team** : Get timely and effective help directly from the developers who build and maintain your tools.
  * **Continuously updated libraries** : Stay up-to-date with the latest features and optimizations that are fully tested and endorsed by Supabase.
  * **Community and collaboration** : Engage with a broader community of Swift developers using Supabase, share knowledge, and contribute to the library's growth.


## Contributors[#](https://supabase.com/blog/supabase-swift#contributors)
We want to give a shout out to the community members who have contributed to the development of the Supabase Swift libraries:
[grdsdev](https://github.com/grdsdev), [satishbabariya](https://github.com/satishbabariya), [AngCosmin](https://github.com/AngCosmin), [thecoolwinter](https://github.com/thecoolwinter), [maail](https://github.com/maail), [gentilijuanmanuel](https://github.com/gentilijuanmanuel), [mbarnach](https://github.com/mbarnach), [mdloucks](https://github.com/mdloucks), [mpross512](https://github.com/mpross512), [SaurabhJamadagni](https://github.com/SaurabhJamadagni), [theolampert](https://github.com/theolampert), [tyirenkyi](https://github.com/tyirenkyi), [tmn](https://github.com/tmn), [multimokia](https://github.com/multimokia), [zunda-pixel](https://github.com/zunda-pixel), [iamlouislab](https://github.com/iamlouislab), [jxhug](https://github.com/jxhug), [james-william-r](https://github.com/james-william-r), [jknlsn](https://github.com/jknlsn), [jknlsn](https://github.com/glowcap), [Colgates](https://github.com/Colgates), [ChristophePRAT](https://github.com/ChristophePRAT), [brianmichel](https://github.com/brianmichel), [junjielu](https://github.com/junjielu).
## Getting started[#](https://supabase.com/blog/supabase-swift#getting-started)
We've released a [new guide](https://supabase.com/docs/guides/getting-started/tutorials/with-swift) to help you get started with the key features available in Supabase Swift.
Or you can jump into our deep dive to use iOS Swift with Postgres & Supabase Auth:
[![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-black.svg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-white.svg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Week](https://supabase.com/ga-week)
15-19 April
[Day 1 -Supabase is officially launching into General Availability](https://supabase.com/ga)[Day 2 -Supabase Functions now supports AI models](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)[Day 3 -Supabase Auth now supports Anonymous sign-ins](https://supabase.com/blog/anonymous-sign-ins)[Day 4 -Supabase Storage: now supports the S3 protocol](https://supabase.com/blog/s3-compatible-storage)[Day 5 -Supabase Security Advisor & Performance Advisor](https://supabase.com/blog/security-performance-advisor)

Build Stage
[01 -PostgreSQL Index Advisor](https://github.com/supabase/index_advisor)[02 -Branching now Publicly Available](https://supabase.com/blog/branching-publicly-available)[03 -Oriole joins Supabase](https://supabase.com/blog/supabase-acquires-oriole)[04 -Supabase on AWS Marketplace](https://supabase.com/blog/supabase-aws-marketplace)[05 -Supabase Bootstrap](https://supabase.com/blog/supabase-bootstrap)[06 -Supabase Swift](https://supabase.com/blog/supabase-swift)[07 -Top 10 Launches from Supabase GA Week](https://supabase.com/blog/ga-week-summary)[Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon)[Community Meetups](https://supabase.com/ga-week#meetups)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&text=Supabase%20Swift)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&text=Supabase%20Swift)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&t=Supabase%20Swift)
[Last postSupabase Bootstrap: the fastest way to launch a new project15 April 2024](https://supabase.com/blog/supabase-bootstrap)
[Next postSupabase Open Source Hackathon 202412 April 2024](https://supabase.com/blog/supabase-oss-hackathon)
[launch-week](https://supabase.com/blog/tags/launch-week)[database](https://supabase.com/blog/tags/database)
On this page
  * [New features](https://supabase.com/blog/supabase-swift#new-features)
  * [What does official support mean?](https://supabase.com/blog/supabase-swift#what-does-official-support-mean)
  * [Contributors](https://supabase.com/blog/supabase-swift#contributors)
  * [Getting started](https://supabase.com/blog/supabase-swift#getting-started)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&text=Supabase%20Swift)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&text=Supabase%20Swift)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&t=Supabase%20Swift)
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

