---
url: https://supabase.com/blog/supabase-auth-identity-linking-hooks
scraped_at: 2025-05-25T09:39:45.853569
title: Supabase Auth: Identity Linking, Hooks, and HaveIBeenPwned integration
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
# Supabase Auth: Identity Linking, Hooks, and HaveIBeenPwned integration
14 Dec 2023
•
7 minute read
[![Stojan Dimitrovski avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fhf.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Stojan DimitrovskiEngineering](https://github.com/hf)
[![Joel Lee avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fj0.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Joel LeeEngineering](https://github.com/j0)
[![Kang Ming Tay avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkangmingtay.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Kang Ming TayEngineering](https://github.com/kangmingtay)
![Supabase Auth: Identity Linking, Hooks, and HaveIBeenPwned integration](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-auth%2Fauth-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We're excited to announce four new features for Supabase Auth:
  1. Identity Linking
  2. Session Control
  3. Leaked Password Protection
  4. Auth Hooks with Postgres functions


## Identity Linking[#](https://supabase.com/blog/supabase-auth-identity-linking-hooks#identity-linking)
When a user signs in, an identity is created with the authentication method and sign-in provider. Historically, [Supabase Auth](https://supabase.com/docs/guides/auth) has been automatically linking identities to a user if the identity shares the same verified email as the user. This is convenient to de-duplicate user accounts. However, some developers also need the flexibility to link accounts that don’t share the same email.
Today we are launching Identity Linking, which developers can use to manually link two separate identities. We’ve added two new endpoints for developers to manage the identity linking process:
Once a user is signed in, use `linkIdentity()` to [link an OAuth identity](https://supabase.com/docs/reference/javascript/auth-linkidentity):
`
1
const { data, error } = await supabase.auth.linkIdentity({
2
 provider: 'google',
3
})
`
Use `unlinkIdentity()` to [unlink an identity](https://supabase.com/docs/reference/javascript/auth-unlinkidentity):
`
1
// retrieve all identities linked to a user
2
const {
3
 data: { identities },
4
} = await supabase.auth.getUserIdentities()
56
// find the google identity linked to the user
7
const googleIdentity = identities.find(({ provider }) => provider === 'google')
89
// unlink the google identity from the user
10
const { data, error } = await supabase.auth.unlinkIdentity(googleIdentity)
`
Currently, these methods support linking an OAuth identity. To link an email or phone identity to the user, you can use the [`updateUser()`](https://supabase.com/docs/reference/javascript/auth-updateuser)method.
Manual linking is disabled by default. You can enable it for your project in [the dashboard Auth settings](https://supabase.com/dashboard/project/_/settings/auth).
![How to enable manual linking](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-auth%2Faccount-linking-config--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
How to enable manual linking
See the [Identity Linking docs](https://supabase.com/docs/guides/auth/auth-identity-linking) for more information.
## Session Control[#](https://supabase.com/blog/supabase-auth-identity-linking-hooks#session-control)
Supabase Auth manages the full session lifecycle from the moment your user signs into your application. This involves the following steps:
  1. Creating the session for the user.
  2. Refreshing the session to keep it active.
  3. Revoking the session upon expiry or logout.


For developers who want finer control over their users’ sessions, we have exposed 3 new settings:
  * **Time-box user sessions** : Force users to sign in again after a time interval.
  * **Inactivity Timeout** : Force users to sign in again if they’re inactive for a time interval.
  * **Single session per user** : Restrict users to a single session. The most recently active session is kept, and all others are terminated.


These session control settings are available on the Pro Plan and above.
![How to enforce single session per user](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-auth%2Fsession-config--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
How to enforce single session per user
See the [Session Management docs](https://supabase.com/docs/guides/auth/sessions) for more information.
## Leaked Password Protection[#](https://supabase.com/blog/supabase-auth-identity-linking-hooks#leaked-password-protection)
Passwords can be inherently insecure due to common user behaviors like choosing guessable passwords or reusing them across different platforms.
Even though OAuth and magiclinks are more secure, we recognize passwords are here to stay. We want to make the potential pitfalls less user-prone. To accomplish that, we have integrated the [HaveIBeenPwned.org](https://haveibeenpwned.com/) _Pwned Passwords API_ in Supabase Auth to prevent users from using leaked passwords.
##### Go library
ℹ️ We have open-sourced a Go library for interacting with the [HaveIBeenPwned.org](http://HaveIBeenPwned.org) Pwned Passwords API that we use in our Auth server. Check out the [repository](https://github.com/supabase/hibp) and feel free to contribute!
As an additional step, we have added the ability to specify password requirements for your users. This can be configured from your project’s Auth settings in [the dashboard](https://supabase.com/dashboard/project/_/settings/auth):
![Adding password requirements](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-auth%2Fpasswords-config--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Adding password requirements
See the [password docs](https://supabase.com/docs/guides/auth/passwords) for more information.
## Auth Hooks[#](https://supabase.com/blog/supabase-auth-identity-linking-hooks#auth-hooks)
We’ve received a ton of feedback asking for ways to customize Auth, like:
  * Add custom claims to the access token JWT
  * Log the user out after multiple failed MFA verification attempts
  * Apply custom rules for password validation attempts


We aim to maintain a straightforward and seamless Supabase Auth experience. It should work effortlessly for most developers, requiring no customization. However, recognizing the diversity of apps, you can now extend standard Auth features through Auth Hooks.
Auth Hooks are simply Postgres functions that run synchronously at key points in the Auth lifecycle, to change the outcome of the action.
For example, to customize the JWT claims with Auth Hooks, you can create a Postgres function that accepts the JWT claims in the first argument and returns the JWT you wish to be used by Supabase Auth.
Suppose you’re creating a gamified application and you wish to attach the user’s level to the JWT as a custom claim:
`
1
create function custom_access_token_hook(event jsonb)
2
returns jsonb
3
language plpgsql
4
as $$
5
declare
6
 user_level jsonb;
7
begin
8
 -- fetch the current user's level
9
 select
10
  to_jsonb(level) into user_level
11
 from profiles
12
 where
13
  user_id = event->>'user_id'::uuid;
1415
 -- change the event.claims.level
16
 return jsonb_set(
17
		event,
18
		'{claims,level}',
19
		user_level);
2021
end;
22
$$
`
Once you’ve created the function in the database, you only need to register it with Supabase Auth:
![Auth Hooks](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-auth%2Fhooks--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Auth Hooks
Currently, you can register an Auth Hook for the following points in the flow:
  * **Custom access token:** called each time a new JWT is generated.
  * **MFA verification attempt** : called each time an MFA factor is verified, allowing finer control over detecting and blocking attempts.
  * **Password verification attempt** : called each time a password is used to sign-in a user, allowing finer control over the security of the user’s accounts.


And if writing PL/pgSQL functions is not your forte, you can always use [pg_net](https://supabase.com/docs/guides/database/extensions/pg_net) to send out requests to your backend APIs instead, or use [plv8](https://supabase.com/docs/guides/database/extensions/plv8) to manipulate JSON more easily by writing your function in JavaScript.
Auth Hooks is available today for self-hosting and will be rolled out to the platform next month. Reach out to us via [support](https://supabase.help) if you need access sooner!
That’s not all! Postgres functions aren’t the only way to write hooks.
Supabase is a founding contributor of [Standard Webhooks](https://www.standardwebhooks.com/), a set of open source tools and guidelines about sending and receiving webhooks easily, securely, and reliably. Naturally, Auth Hooks will be supporting webhooks in Q1 of 2024.
## One more thing…[#](https://supabase.com/blog/supabase-auth-identity-linking-hooks#one-more-thing)
If you’ve been following us from [the start](https://supabase.com/blog/supabase-auth), you will know that Supabase Auth started by forking [Netlify’s GoTrue server](https://github.com/netlify/gotrue). A lot has changed since then and we’ve diverged from the upstream repository. At this stage it makes sense to rename the project to something else (_cues drumroll_) — Auth.
This simply means that the repositories will be renamed from using `gotrue` to `auth`. But don’t worry! Docker images and libraries like `@supabase/gotrue-js` will continue to be published and you can use `@supabase/auth-js` interchangeably for the current v2 version for as long as it is supported. All of the classes and methods remain in place. No breaking changes here!
## Conclusion[#](https://supabase.com/blog/supabase-auth-identity-linking-hooks#conclusion)
Thanks for reading till the end! We hope you enjoyed the Supabase Auth updates for Launch Week X: Identity Linking, Session Control, Leaked Password Protection, and Auth Hooks with Postgres functions.
We are looking forward to seeing what you build with these new features, and, of course, your feedback to make them even better.
[Launch Week ![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/launch-week)
11-15 Dec
Main Stage
[Day 1 -Supabase Studio: introducing an **AI Assistant** , **Postgres roles** , and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)[ Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)[Day 3 -Introducing Supabase **Branching** , a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)[Day 4 -Supabase Auth: **Identity Linking** , **Session Control** , **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)[ Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)

Build Stage
[01 -Supabase Album](https://supabase.productions/)[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)[05 -pg_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-identity-linking-hooks&text=Supabase%20Auth%3A%20Identity%20Linking%2C%20Hooks%2C%20and%20HaveIBeenPwned%20integration)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-identity-linking-hooks&text=Supabase%20Auth%3A%20Identity%20Linking%2C%20Hooks%2C%20and%20HaveIBeenPwned%20integration)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-identity-linking-hooks&t=Supabase%20Auth%3A%20Identity%20Linking%2C%20Hooks%2C%20and%20HaveIBeenPwned%20integration)
[Last postFly Postgres, managed by Supabase15 December 2023](https://supabase.com/blog/postgres-on-fly-by-supabase)
[Next postSupabase Wrappers v0.2: Query Pushdown & Remote Subqueries14 December 2023](https://supabase.com/blog/supabase-wrappers-v02)
[launch-week](https://supabase.com/blog/tags/launch-week)[auth](https://supabase.com/blog/tags/auth)
On this page
  * [Identity Linking](https://supabase.com/blog/supabase-auth-identity-linking-hooks#identity-linking)
  * [Session Control](https://supabase.com/blog/supabase-auth-identity-linking-hooks#session-control)
  * [Leaked Password Protection](https://supabase.com/blog/supabase-auth-identity-linking-hooks#leaked-password-protection)
  * [Auth Hooks](https://supabase.com/blog/supabase-auth-identity-linking-hooks#auth-hooks)
  * [One more thing…](https://supabase.com/blog/supabase-auth-identity-linking-hooks#one-more-thing)
  * [Conclusion](https://supabase.com/blog/supabase-auth-identity-linking-hooks#conclusion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-identity-linking-hooks&text=Supabase%20Auth%3A%20Identity%20Linking%2C%20Hooks%2C%20and%20HaveIBeenPwned%20integration)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-identity-linking-hooks&text=Supabase%20Auth%3A%20Identity%20Linking%2C%20Hooks%2C%20and%20HaveIBeenPwned%20integration)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-identity-linking-hooks&t=Supabase%20Auth%3A%20Identity%20Linking%2C%20Hooks%2C%20and%20HaveIBeenPwned%20integration)
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

