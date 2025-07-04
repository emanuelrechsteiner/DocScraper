---
url: https://supabase.com/blog/supabase-auth-passwordless-sms-login
scraped_at: 2025-05-25T08:52:52.603054
title: Supabase Auth v2: Phone Auth now available
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
# Supabase Auth v2: Phone Auth now available
28 Jul 2021
•
4 minute read
[![Kang Ming Tay avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkangmingtay.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Kang Ming TayEngineering](https://github.com/kangmingtay)
![Supabase Auth v2: Phone Auth now available](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fauth-v2%2Fsupabase-auth-v2-cover.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Since launching Supabase Auth [last summer](https://news.ycombinator.com/item?id=24072051) it's proven to be a key part of the Supabase Stack. We receive a constant stream of feature requests and community PRs resulting in a long list of external providers including GitHub, Discord, Azure, Apple and more.
Supabase Auth is similar to Auth0 and Firebase Auth with one major difference - the user data lives in your own database, reducing lock-in, and making the auth system more extensible. You can write native PostgreSQL Row Level Security policies to determine which data your users should (or should not) have access to. It can even be used in conjunction with other Supabase features, such as [Storage](https://supabase.com/storage), to control access for specific files and buckets.
Today we're announcing some major new features for our [fork](https://github.com/supabase/gotrue) of Netlify's [GoTrue](https://github.com/netlify/gotrue) Auth server.
## Phone Auth is here![#](https://supabase.com/blog/supabase-auth-passwordless-sms-login#phone-auth-is-here)
Your users can now log in using their mobile with SMS-based OTPs (one-time password).
### Passwordless SMS login[#](https://supabase.com/blog/supabase-auth-passwordless-sms-login#passwordless-sms-login)
Users can log in using a passwordless SMS based OTP with `supabase-js`, or directly with the Auth API.
![Passwordless SMS login](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fauth-v2%2Fpasswordless-login.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
After logging in, the user will receive a six-digit One Time Password. The OTP can be easily verified.
![Use SMS and password to login](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fauth-v2%2Fverify-otp.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### SMS login with passwords[#](https://supabase.com/blog/supabase-auth-passwordless-sms-login#sms-login-with-passwords)
Phone Auth can be used in conjunction with a password. Using this flow, your users can subsequently log in with either an OTP or a phone + password combo.
![SMS login with passwords](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fauth-v2%2Fphone-and-password-login.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Choose an SMS Provider[#](https://supabase.com/blog/supabase-auth-passwordless-sms-login#choose-an-sms-provider)
Supabase Auth supports [Twilio](https://www.twilio.com/) as an SMS provider, with more options coming soon. Simply plug your Twilio credentials into your Auth Settings in the Supabase Dashboard to get started.
Check out the [documentation](https://supabase.com/docs/guides/auth/phone-login/twilio) to get started with Mobile OTPs, or watch the [Youtube guide](https://youtu.be/akScoPO01bc).
### Multi-Factor Auth coming soon[#](https://supabase.com/blog/supabase-auth-passwordless-sms-login#multi-factor-auth-coming-soon)
Phone Auth is available today on all new and existing Supabase projects. We've also laid the groundwork for mobile Multi-Factor Auth and will be offering that as an option soon.
## Even more OAuth providers[#](https://supabase.com/blog/supabase-auth-passwordless-sms-login#even-more-oauth-providers)
The community has contributed tons of OAuth providers, and today we're announcing two more.
Shoutout to [@ph1p](https://github.com/ph1p) who contributed [Twitch](https://supabase.com/docs/guides/auth/auth-twitch) as our latest OAuth provider! The Supabase team added [Discord](https://supabase.com/docs/guides/auth/social-login/auth-discord) last month, bringing the total OAuth Providers to ten.
![All Supabase OAuth providers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fauth-v2%2Fsupabase-oauth-providers.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You can request more providers on our [Auth repo](https://github.com/supabase/gotrue) and Pull Requests are, of course, always welcome.
## Generate Confirmation Links[#](https://supabase.com/blog/supabase-auth-passwordless-sms-login#generate-confirmation-links)
To make life easy for developers, the Supabase hosted platform manages all Auth-related emails, including confirmation, recovery, invite, and passwordless "magic-link" emails. The templates are customizable and we even offer the ability to bring your own SMTP provider.
Some of our power users require a little more flexibility however. We've had a lot of requests to dynamically generate email content, especially for sending internationalized emails. To handle situations like these, today we're adding the ability to generate confirmation, invite, recovery, and magic links via an API endpoint.
We've exposed this functionality in `supabase-js`, and it can be invoked with the use of your `service_role` admin key (which means you should only be calling this function from a backend and not from the client itself).
![Generate Confirmation Links](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fauth-v2%2Fgenerate-links.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## What's next?[#](https://supabase.com/blog/supabase-auth-passwordless-sms-login#whats-next)
The next major item on the list is MFA (Multi-Factor Authentication) - which includes TOTP ([Time-Based One Time Password](https://en.wikipedia.org/wiki/Time-based_One-Time_Password)).
Find out how Mobbin is using Supabase Auth to [manage 200,000 users](https://supabase.com/blog/mobbin-supabase-200000-users).
Anything else you want to see or can help implement in Auth? Reach out on [Discord](https://discord.supabase.com/) and give Auth a try by [creating a project](https://supabase.com/dashboard/) on Supabase!
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-passwordless-sms-login&text=Supabase%20Auth%20v2%3A%20Phone%20Auth%20now%20available)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-passwordless-sms-login&text=Supabase%20Auth%20v2%3A%20Phone%20Auth%20now%20available)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-passwordless-sms-login&t=Supabase%20Auth%20v2%3A%20Phone%20Auth%20now%20available)
[Last postMobbin uses Supabase to authenticate 200,000 users28 July 2021](https://supabase.com/blog/mobbin-supabase-200000-users)
[Next postSpot: a video sharing app built with Flutter27 July 2021](https://supabase.com/blog/spot-flutter-with-postgres)
[launch-week](https://supabase.com/blog/tags/launch-week)[auth](https://supabase.com/blog/tags/auth)
On this page
  * [Phone Auth is here!](https://supabase.com/blog/supabase-auth-passwordless-sms-login#phone-auth-is-here)
    * [Passwordless SMS login](https://supabase.com/blog/supabase-auth-passwordless-sms-login#passwordless-sms-login)
    * [SMS login with passwords](https://supabase.com/blog/supabase-auth-passwordless-sms-login#sms-login-with-passwords)
    * [Choose an SMS Provider](https://supabase.com/blog/supabase-auth-passwordless-sms-login#choose-an-sms-provider)
    * [Multi-Factor Auth coming soon](https://supabase.com/blog/supabase-auth-passwordless-sms-login#multi-factor-auth-coming-soon)
  * [Even more OAuth providers](https://supabase.com/blog/supabase-auth-passwordless-sms-login#even-more-oauth-providers)
  * [Generate Confirmation Links](https://supabase.com/blog/supabase-auth-passwordless-sms-login#generate-confirmation-links)
  * [What's next?](https://supabase.com/blog/supabase-auth-passwordless-sms-login#whats-next)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-passwordless-sms-login&text=Supabase%20Auth%20v2%3A%20Phone%20Auth%20now%20available)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-passwordless-sms-login&text=Supabase%20Auth%20v2%3A%20Phone%20Auth%20now%20available)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-passwordless-sms-login&t=Supabase%20Auth%20v2%3A%20Phone%20Auth%20now%20available)
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

