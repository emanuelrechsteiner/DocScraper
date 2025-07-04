---
url: http://supabase.com/customers/replenysh
scraped_at: 2025-05-25T09:42:16.364461
title: Replenysh | Supabase Customer Stories
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
[Back](https://supabase.com/customers)
[Customer Stories](https://supabase.com/customers)
# Replenysh uses Supabase to implement OTP in less than 24 hours.
With Supabase, Replenysh gets a slick auth experience, reduces DevOps overhead, and continues to scale with Postgres.
![Replenysh uses Supabase to implement OTP in less than 24 hours. logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Freplenysh.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
About
Replenysh is a digital platform that connects global brands with local communities to recover materials and eliminate the concept of waste.
[https://replenysh.com/](https://replenysh.com/)
FoundedSouthern California
Ready to get started?
[Contact sales](https://supabase.com/contact/enterprise)
Replenysh connects brands who want to recover their products and packaging with communities looking to monetize used materials.
Learn how Replenysh uses Supabase to power the circular economy, redefining how brands interact with their customers & products.
## Material recovery offers brands a new way to connect to their customers[#](https://supabase.com/customers/replenysh#material-recovery-offers-brands-a-new-way-to-connect-to-their-customers)
At the end of a linear economy, products usually end up in landfills or the ocean. Every year, 8 million metric tons of plastics enter our ocean. This is on top of the estimated 150 million metric tons that currently circulate our marine environments. In the USA alone, every year, 139 million tons of waste is sent to landfills.
The problem is our current waste and recycling infrastructure can't support that demand. With less than 10% of material actually getting recycled, the vast majority just ends up in a landfill or as pollution.
Replenysh is building a solution to this problem by creating entirely new infrastructure to help brands get their materials back. They're building an ecosystem of tools to enable any community in the world to do the right thing.
Whenever material is dropped off at a host, brands have the opportunity to engage with that person, resulting in a win-win situation for the planet, the brands, and the individual who all want to make a positive impact. Anyone in the community can take their used products and materials to the hosts — with that material being tracked all the way back to the brands and manufacturers who will reuse it. Brands have the opportunity to engage with that person, resulting in a win-win situation for the planet, the brands, and the individual who all want to make a positive impact. This turns a traditional consumption model into an opportunity for brands and customers to participate in the circular economy.
Brands are adopting Replenysh to demonstrate their commitment to making a positive environmental impact, while seeking to engage with consumers in a new, authentic way. Replenysh provides the technology to communities that are helping build the future infrastructure where all materials are traceable and reused.
![Linear vs Circular economy](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Freplenysh%2Fcircular-economy.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Refactoring code leads to a better way forward[#](https://supabase.com/customers/replenysh#refactoring-code-leads-to-a-better-way-forward)
Historically the team created their own backend infrastructure, setting up APIs and Authentication to run their own OTP system with Twilio and passwords. Postgres is essential to their requirements because Replenysh use Row Level Security for authorization. Before adopting Supabase, the team used a Haskell server with a different Postgres instance deployed on Heroku.
The team decided to do a large refactor of their codebase and began investigating alternative hosting options to help speed up development time and reduce maintenance.
Firebase seemed appealing due to its ability to get started quickly, but the team didn't want to migrate away from a relational database. Specifically, Postgres and RLS fit their requirements.
When the team discovered Supabase on Hacker News they felt excitement. Supabase has a reputation for a smooth developer experience, providing Postgres and Row Level Security as a core feature.
As a bonus, Supabase provided more than just a database, reducing their DevOps overhead. After reading the [Supabase Auth documentation](https://supabase.com/docs/guides/auth/overview) the team determined they can have the functionality they need, like SMS OTP. When they saw [Mobbin are using Supabase at scale](https://supabase.com/case-studies-mobbin), they decided to migrate to Supabase.
## Globally recognized brands need quality at scale[#](https://supabase.com/customers/replenysh#globally-recognized-brands-need-quality-at-scale)
Less than a day after beginning development with Supabase, the team completed their SMS OTP implementation, and deployed their app to the app store a few weeks later.
![Replenysh-Mobile-App](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Freplenysh%2FReplenysh-Mobile-App.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Replenysh clients include brands with global recognition and millions of customers. With their reputation at stake, major brands have a high-quality threshold. If a global brand asks its customers to adopt a technology, the user experience must be high quality and reliable. Their customers' primary interaction point is mobile-first. This means a robust and smooth mobile Auth experience is non-negotiable. After switching to Supabase, when they demo, clients are instantly impressed with just how easy it is for users to log in with an SMS OTP and start participating in the circular economy. As a result, some of the world's largest retailers and beverage companies have recently joined Replenysh and the circular economy.
![Replenysh-large-screen-view](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Freplenysh%2FReplenysh-large-screen-view.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Supabase means faster development and reduced maintenance[#](https://supabase.com/customers/replenysh#supabase-means-faster-development-and-reduced-maintenance)
> We saw the Auth update for launch week we thought it was the perfect time to get going with Supabase.
> We implemented & pushed live phone (OTP) auth and had something ready to deploy to the app store in less than 24-hours!
> Supabase's developer experience lived up to its reputation. Our app is ready to launch with major brands to help them reach sustainability goals and connect with their customers in a meaningful way
> ![Clark Dinnison, Head of Product at Replenysh. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fclark-dinnison.jpeg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> Clark Dinnison, Head of Product at Replenysh.
## Supabase help Replenysh continue to scale[#](https://supabase.com/customers/replenysh#supabase-help-replenysh-continue-to-scale)
Supabase turbo-charged Replenysh's development time with a seamless end-user mobile login experience. They are ready to help major brands engage with their users through participation in the circular economy. With Supabase, the team knows they have a slick auth experience, reduced DevOps overhead, and can continue to scale with Postgres. You can test out the Supabase developer experience today by [starting a new project on the Free Plan!.](https://supabase.com/dashboard)
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

