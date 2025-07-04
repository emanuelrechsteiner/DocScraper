---
url: https://supabase.com/blog/improved-dx
scraped_at: 2025-05-25T08:57:04.861742
title: Supabase.js 1.0
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
# Supabase.js 1.0
30 Oct 2020
•
4 minute read
[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)
**UPDATE 16/08/2022** : supabase-js v2 is out and focuses on “quality-of-life” improvements for developers. V2 includes Type support, new auth methods, realtime multiplayer sneak peek, and more: [**Read the blog post**](https://supabase.com/blog/supabase-js-v2)
### New Docs[#](https://supabase.com/blog/improved-dx#new-docs)
Before digging into the improvements, we're excited to point out our new [developer docs](https://supabase.com/docs/reference/javascript/installing). While they're still a work in progress, here are some things we think you'll like:
  * The [Reference Docs](https://supabase.com/docs/reference/javascript/installing) are auto-generated from our TypeScript definitions and then enriched with examples. This forces us to document our code and makes it easier to keep everything in sync.
  * We added placeholders for the other languages that the community is developing. They have already started with Python, C#, Dart, Rust, and Swift. Expect to see the docs filling up soon!
  * We've added sections for all of the open source tools we use, including [Postgres](https://supabase.com/docs/postgres/server/about), PostgREST[1](https://supabase.com/blog/improved-dx#user-content-fn-1), [GoTrue](https://supabase.com/docs/guides/auth/architecture#auth-service), and Realtime[2](https://supabase.com/blog/improved-dx#user-content-fn-2). We'll be filling these with lots of valuable information including self-hosting, benchmarks, and simple guides.


### Errors are returned, not thrown[#](https://supabase.com/blog/improved-dx#errors-are-returned-not-thrown)
We attribute this improvement to community feedback. This has significantly improved the developer experience.
Previously we would throw errors:
`
1
try {
2
 const { body } = supabase.from('todos').select('*')
3
} catch (error) {
4
 console.log(error)
5
}
`
And now we simply return them:
`
1
const { data, error } = supabase.from('todos').select('*')
2
if (error) console.log(error)\n
3
// else, carry on ..
`
After testing this for a while we're very happy with this pattern. Errors are handled next to the offending function. Of course you can always rethrow the error if that's your preference.
### We created `gotrue-js`[#](https://supabase.com/blog/improved-dx#we-created-gotrue-js)
Our goal for `supabase-js` is to tie together many sub-libraries. Each sub-library is a standalone implementation for a single external system. This is one of the ways we support existing open source tools.
To maintain this philosophy, we created [`gotrue-js`](https://github.com/supabase/gotrue-js), a library for Netlify's GoTrue auth server. This library includes a number of new additions, including third-party logins.
Previously:
`
1
const {
2
 body: { user },
3
} = await supabase.auth.signup('someone@email.com', 'password')
`
Now:
`
1
const { user, error } = await supabase.auth.signUp({
2
 email: 'someone@email.com',
3
 password: 'password',
4
})
`
### Enhancements and fixes[#](https://supabase.com/blog/improved-dx#enhancements-and-fixes)
  * Native TypeScript. All of our libraries are now natively built with TypeScript: [`supabase-js`](https://github.com/supabase/supabase-js), [`postgrest-js`](https://github.com/supabase/postgrest-js), [`gotrue-js`](https://github.com/supabase/gotrue-js), and [`realtime-js`](https://github.com/supabase/realtime-js).
  * Better realtime scalability: we only generate one socket connection per Supabase client. Previously we would create a connection for every subscription.
  * We've added support for OAuth providers.
  * 60% of minor bugs outstanding for `supabase-js` have been [solved](https://github.com/supabase/supabase-js/pull/50).
  * You can use `select()` instead of `select(*)`


### Breaking changes[#](https://supabase.com/blog/improved-dx#breaking-changes)
We've bumped the major version because there are a number of breaking changes. We've detailed these in the [release notes](https://github.com/supabase/supabase-js/releases/tag/v1.0.1), but here are a few to be aware of:
  * `signup()` is now `signUp()` and `email` / `password` is passed as an object
  * `logout()` is now `signOut()`
  * `login()` is now `signIn()`
  * `ova()` and `ovr()` are now just `ov()`
  * `body` is now `data`


Previously:
`
1
const { body } = supabase.from('todos').select('*')
`
Now:
`
1
const { data } = supabase.from('todos').select()
`
### Upgrading[#](https://supabase.com/blog/improved-dx#upgrading)
We have documented all of the changes in the [release notes](https://github.com/supabase/supabase-js/releases/tag/v1.0.1).
To summarise the steps:
  1. Install the new version: `npm install @supabase/supabase-js@latest`
  2. Update all your `body` constants to `data`
  3. Update all your `supabase.auth` functions with the new [Auth interface](https://supabase.com/docs/reference/javascript/auth-signup)


### Get started[#](https://supabase.com/blog/improved-dx#get-started)
  * Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
  * Make sure to [star us on GitHub](https://github.com/supabase/supabase)
  * Follow us [on Twitter](https://twitter.com/supabase)
  * Become a [sponsor](https://github.com/sponsors/supabase)


## Footnotes[#](https://supabase.com/blog/improved-dx#footnote-label)
  1. Removed link on June 14 2022 for search optimization: page currently does not exist [↩](https://supabase.com/blog/improved-dx#user-content-fnref-1)
  2. Removed link on June 14 2022 for search optimization: page currently does not exist [↩](https://supabase.com/blog/improved-dx#user-content-fnref-2)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&text=Supabase.js%201.0)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&text=Supabase.js%201.0)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&t=Supabase.js%201.0)
[Last postSupabase Alpha October 20202 November 2020](https://supabase.com/blog/supabase-alpha-october-2020)
[Next postSupabase Alpha September 20203 October 2020](https://supabase.com/blog/supabase-alpha-september-2020)
[supabase](https://supabase.com/blog/tags/supabase)
On this page
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&text=Supabase.js%201.0)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&text=Supabase.js%201.0)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&t=Supabase.js%201.0)
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

