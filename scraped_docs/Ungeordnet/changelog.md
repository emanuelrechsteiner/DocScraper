---
url: https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2
scraped_at: 2025-05-25T09:13:53.330321
title: Changelog
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
# Changelog
New updates and product improvements
### [Projects on XL and larger compute add-ons can now create up to 5 Read Replicas. ](https://github.com/orgs/supabase/discussions/29434)
Sep 22, 2024
The initial launch of [Read Replicas](https://supabase.com/docs/guides/platform/read-replicas) allowed for up to two Read Replicas per project.
The limit for projects on XL compute add-ons and larger has now been raised to 5 Read Replicas per project.
Projects on compute add-ons smaller than XL are still allowed up to 2 Read Replicas per project.
### [Supabase Auth: Changes to default email provider ](https://github.com/orgs/supabase/discussions/29370)
Sep 18, 2024
As our user base has grown, we are taking steps to make sure we are able to continue to provide a safe, secure, robust free plan experience. To ensure that email-based auth continues to work for all users on Supabase, we're making changes if you're using the [default email provider](https://supabase.com/docs/guides/auth/auth-smtp#auth-smtp). This allows us to continue to offer our default provider in a more sustainable and resilient manner.
For maximum flexibility and control over your auth emails, we suggest one of the following:
  * Use a [custom SMTP provider](https://supabase.com/docs/guides/auth/auth-smtp#how-to-set-up-smtp) instead
  * Send emails through your own email provider using the [email send hook](https://supabase.com/docs/guides/auth/auth-hooks/send-email-hook)


If you still want to use the default email provider, these are the changes being planned:
  * **Email template customization will be allowed and customized email templates will not be reverted to default.**
  * **26th September** : If you do not have a custom SMTP server set up, emails can only be sent to email addresses in your project's organization. So for example, if your organization has the following members: person-a@example.com, person-b@example.com and person-c@example.com , this means that email messages from Auth will only be sent to these addresses.


These measures are taken to prevent abuse to our shared SMTP service. In the future, we may consider increasing the email rate limits once we see a drop in abuse.
## Frequently asked questions[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#frequently-asked-questions)
### Why such a short notice?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#why-such-a-short-notice)
Supabase uses a third-party email sending provider that has mandated we reduce email abuse significantly or they will be forced to block all email sending. A [tragedy of the commons](https://en.wikipedia.org/wiki/Tragedy_of_the_commons).
### Can't Supabase switch to a different email sending partner?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#cant-supabase-switch-to-a-different-email-sending-partner)
Yes, but we would run into the same issues. All email sending services are required to monitor abuse and force their customers to follow the same rules.
### Can't Supabase send emails on their own, without a third party?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#cant-supabase-send-emails-on-their-own-without-a-third-party)
Not really. You can't just send email on the web today without investing a lot of money and time (unblocking port 25, keeping IP addresses out of spam lists, etc.). This is not our core competency and do not have plans to start doing this today.
### How long does it take to set up a custom SMTP provider?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-long-does-it-take-to-set-up-a-custom-smtp-provider)
Fortunately this is very easy. You can use any email sending service for this, really popular ones include:
  * [Resend](https://resend.com/)
  * [AWS SES](https://aws.amazon.com/ses/)
  * [Postmark](https://postmarkapp.com/)
  * [SendGrid](https://sendgrid.com/)
  * [Zepto Mail](https://www.zoho.com/zeptomail/)
  * [Brevo](https://www.brevo.com)


All you need to do is create an account, verify your sending domain and finally input the SMTP username and password in the [Auth settings page](https://supabase.com/dashboard/project/_/settings/auth).
### What if I turn off email confirmations, can I use it then?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#what-if-i-turn-off-email-confirmations-can-i-use-it-then)
_Currently this behavior is not supported and we'll be rolling out a fix for it during the first week of October._
Confirming email addresses is where most of the email message activity for a project originates. Turning it off can be a viable option for some projects that are still in the early testing, development or experimental phase.
Be aware that even if you turn off email confirmations the forgot password or reset password flows in your app continue to function. They also send messages, and starting 26th September those messages will be delivered only to the members of the Supabase organization that owns the project. All other end-users will get a message similar to "Email address not authorized." Effectively, the forgot password / reset password flow will be broken for your project.
### What if I want just username + password authentication and using `<username>@<fakedomain>` instead?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#what-if-i-want-just-username--password-authentication-and-using-usernamefakedomain-instead)
Please don't do this. Part of the reason why we were forced to lock down these changes is bounced emails, probably from use cases like this.
Official username + password support is going to be made available in the coming year, and until then:
  * Use a real domain, that you control
  * Send emails to that domain, so set up a receiving server


But the best thing to do is:
  * Set up a [Send Email Auth Hook](https://supabase.com/docs/guides/auth/auth-hooks/send-email-hook) that does nothing. You don't even need to use a server or an Edge Function. Just define a Postgres function that just does nothing.


### I'm using the admin API to generate links, and not really sending using Supabase's default provider. Do I need to do anything?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#im-using-the-admin-api-to-generate-links-and-not-really-sending-using-supabases-default-provider-do-i-need-to-do-anything)
_All projects using generate link via the admin API without custom SMTP have been patched to allow the behavior. We still strongly urge those customers to set up custom SMTP regardless._
Just because you're mostly using the admin API to generate links to send in custom email messages, doesn't mean that the Auth server is not configured to use Supabase's shared SMTP service. Your Auth API can be called from your frontend at any time, especially in edge cases such as to handle forgot password or other similar flows, which you may not be handling via the admin API.
Therefore we urge all customers that do use the admin API to set up a custom SMTP sending service regardless.
If you are not interested in setting this up, you can instruct the Auth server to ignore all emails (pretend it's sending them) by configuring a [Send Email Auth Hook](https://supabase.com/docs/guides/auth/auth-hooks/send-email-hook) as a Postgres function that does nothing.
### How can I disable the warning banner?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-can-i-disable-the-warning-banner)
You can disable the warning banner by setting up a [custom SMTP provider](https://supabase.com/docs/guides/auth/auth-smtp#how-to-set-up-smtp) , or, if your project doesn't use email at all, by disabling the [email provider](https://supabase.com/dashboard/project/xguihxuzqibwxjnimxev/auth/providers).
## Updates[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#updates)
### [20th September 2024](https://github.com/orgs/supabase/discussions/29370#discussioncomment-10702421)[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#20th-september-2024)
**Email template customization will be allowed and customized email templates will not be reverted to default.**
Team has decided that restricting email template customization is not viable and a big breaking change. We may need to do go back to this in the future if abuse continues and our other measures like allowing projects to only send messages to authorized email addresses do not improve the situation. We continue to urge all customers regardless of plan that use the default SMTP service for live applications to move to a custom SMTP provider as soon as able.
  * ~~**20th September** : [Email template customization](https://supabase.com/dashboard/project/_/auth/templates) will no longer be possible without setting up a custom SMTP provider. Email templates already customized can still be customized until 24th September.~~
  * ~~**24th September** : Projects without a custom SMTP provider will have their custom email templates returned back to the default ones from Supabase. This means that any auth emails sent out from your project will use the default email template.~~


### [Supabase Auth: Asymmetric Keys support in 2025 ](https://github.com/orgs/supabase/discussions/29289)
Sep 13, 2024
> Update (19th December 2024): Asymmetric Keys will not be released in Q4 2024 because it needs further development work. We will finalize the timeline and announce the updated timeline in Q1 2025.
> Update (2nd October 2024): We have decided to push back the launch from 7th October 2024 to Q4 2024 to roll this out meticulously; we want to perform exhaustive security checks and spend more time dogfooding internally.
# Asymmetric key changelog[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#asymmetric-key-changelog)
# Introduction[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#introduction)
We are introducing asymmetric key cryptography to Supabase Auth in **Q4 2024~~on 7th October 2024~~**. This will be provided as an additional option to the JWT secret currently shown in the JWT settings page.
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F5ce813d3-7d10-41b7-9fc6-5eb2cb4896bf&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Why are we doing this?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#why-are-we-doing-this)
Supabase Auth has always been using a symmetric secret (known as the JWT secret) for signing and verifying JWTs. While this is simple and convenient (since the same secret is used for both signing and verifying), it presents the following problems:
  1. **Extra network request required to verify the user’s JWT with the symmetric secret.** Currently, one needs to make a request to Supabase Auth in order to verify the user’s JWT or copy the JWT secret into their environment. While the latter suggestion improves performance, it can result in security implications if the secret is accidentally leaked, which requires all your keys to be rolled.
  2. **Difficult to roll with zero downtime.** Since the symmetric secret cannot be shared publicly, developers need to wrangle with rolling the secret across their environments while ensuring that the new secret is used.


# Benefits of using asymmetric keys[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#benefits-of-using-asymmetric-keys)
Asymmetric keys rely on public / private key cryptography, which means that the private key is only used for signing, while the public key is only used for verifying. This solves the above problems in the following way:
  * Usage of asymmetric key cryptography rather than a shared symmetric secret for signing and verifying JWTs. Since asymmetric keys don’t use a shared secret, there is less risk of the secret being leaked.
  * Faster JWT verification times since there’s no need to make a network call to Supabase Auth via `getUser()` . The public key can be used for verifying the JWT. Note that adding the symmetric secret to your server-side environment to verify the JWT also has the same effect but is potentially less secure since there is an increased risk of the secret being leaked if it is used in multiple applications.
  * Zero-downtime key rotation. Public keys can be exposed in a JSON Web Key Set (JWKs) format, which allows any one of them to be used for verification. When the asymmetric key is rotated, we can still keep the previously used public key in the JWKs endpoint to verify existing JWTs. New JWTs will be signed by the new asymmetric key.


These will include the following changes:
  * A public JWKs endpoint for retrieving the public JWK to verify JWTs. This will be exposed through the `https://<project_ref>.supabase.co/auth/v1/.well-known/jwks.json` endpoint. The symmetric secret will not be exposed through this endpoint for security reasons.
  * A new method called `getClaims()` , which handles verifying the JWT and returning the claims in it.
  * Ability to download the public keys in different formats through the dashboard (e.g. PEM, JWKs).


## Migration to Asymmetric JWTs[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#migration-to-asymmetric-jwts)
New projects that are created after **1st May 2025** will be created with an RSA asymmetric key by default. Existing projects can choose to start using asymmetric keys by doing the following:
  1. Ensure that you are using the [new API keys](https://github.com/orgs/supabase/discussions/29260).
  2. Update all your clients to use at least supabase-js version x.x.x (the version number will be updated closer to the release date). In this version, we are introducing a new method called `getClaims` which handles verifying both symmetric and asymmetric JWTs: 
     * Example successful response payload for `getClaims()`
`
1
{
2
 "data": {
3
	 "iss": "https://projectref.supabase.co",
4
	 "sub": "565dafb5-fd66-4274-9c37-f0ff720f5637",
5
	 "aud": "authenticated",
6
	 "exp": 1824717902,
7
	 "iat": 1724717902,
8
	 "email": "foo@example.com",
9
	 "phone": "",
10
	 "app_metadata": {
11
	  "provider": "email",
12
	  "providers": ["email"]
13
	 },
14
	 "user_metadata": {
15
	  ...
16
	 },
17
	 "role": "authenticated",
18
	 "aal": "aal1",
19
	 "amr": [
20
	  {
21
	   "method": "oauth",
22
	   "timestamp": 1724717902
23
	  }
24
	 ],
25
	 "session_id": "479c1cbf-bd52-42d4-894f-1519f39b3241",
26
	 "is_anonymous": false
27
 },
28
 "error": null
29
}
`
     * Using `getClaims()` to verify the JWT
`
1
import { createClient } from 'supabase/supabase-js'
23
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)
45
// previously, using getUser() requires making an 
6
// additional network request to Supabase Auth to verify the JWT
7
// 
8
// const { data, error } = await supabase.auth.getUser()
910
// getClaims() will always return the JWT payload if the JWT is verified
11
// If it's an asymmetric JWT, getClaims() will verify using the JWKs endpoint.
12
// If it's a symmetric JWT, getClaims() calls getUser() to verify the JWT. 
13
const { data, error } = await supabase.auth.getClaims(jwks)
`
  3. Create an asymmetric key through the dashboard. At this point the symmetric JWT moves to a `Previously Used` state. Existing JWTs signed with the symmetric JWT continue to be valid, but new JWTs are signed via the asymmetric JWT. Note: The UI mockup below is subjected to change and is just meant to illustrate the different possible states of a signing key.


![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fafe92146-84f9-471d-b51d-bd0050824af7&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
  1. After the JWT expiry period, you can safely revoke the “Previously Used” symmetric JWT, since new JWTs will now be signed with the asymmetric key.


# Frequently Asked Questions[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#frequently-asked-questions)
  * What do I need to do before I can start using asymmetric keys in Supabase Auth? 
    * See migration section above for the detailed steps
  * Can I create a symmetric key after I create an asymmetric key? 
    * Yes. You will still be able to create a new symmetric key under the [JWT settings](https://supabase.com/dashboard/project/_/settings/api) page in the dashboard. New projects will be created with an asymmetric key by default on **1st May 2025**.
  * Will the private asymmetric key be exposed? 
    * No. Only the public keys will be exposed in various formats (e.g. PEM, JWKs) since those are needed for verification.
  * Will I be able to bring my own private key? 
    * Yes, you can bring your own private key as long as it complies with the key types allowed.
  * What key types can I use to create asymmetric JWTs? 
    * By default, asymmetric keys will be created with RS256 by default. You can optionally choose to use ECC or Ed25519. ECC keys are more performant, but not as widely supported as RS256. You can also fallback to HS256 (symmetric keys).


### [Upcoming changes to Supabase API Keys (release date TBC) ](https://github.com/orgs/supabase/discussions/29260)
Sep 12, 2024
> Update (19th December 2024): Changes to Supabase API Keys will not be released in Q4 2024 because it needs further development work. We will finalize the timeline and announce the updated timeline in Q1 2025.
# Introduction[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#introduction)
We’re changing the way [API keys](https://supabase.com/docs/guides/api/api-keys) work in Supabase to improve your project’s security and developer experience and plan to roll out these changes **Q4 2024**. Rest assured that the current API keys in your existing projects will continue to work for another year until **1st October 2025** during the transition.
We’ll contact you when we launch the new API keys, and when we do, no immediate action is required. However, we strongly recommend that you migrate your project’s existing API keys for the new set when they are introduced. Updating to use the new API keys is a quick and painless process and can be as simple as a change in environment variable and take just a few minutes.
# Timeline[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#timeline)
> **Update (2nd October 2024):** We have decided to push back the launch from 7th October 2024 to Q4 2024 to roll this out meticulously; we want to perform exhaustive security checks and spend more time dogfooding internally.
**Key Dates**| **Description**| **User Action Needed**  
---|---|---  
**Q4 2024~~7th October 2024~~**|  Introduction of new API keys.New projects will automatically generate **both** new API keys and legacy API keys to help ease the transition.Existing projects can continue to use the legacy API keys and can opt in to use the new API keys by manually generating them.| No immediate action needed. We strongly recommend that you migrate to use the new API keys.  
**TBC**|  We will start sending you monthly reminders to migrate off legacy API keys and start using the new keys.New projects will be created with only new API keys.Projects restored from **1st May 2025** will no longer be restored with the legacy API keys.| You are highly encouraged to migrate off to use the new API keys before this date since paused projects that are restored risk being broken as they won’t have the legacy keys.  
**TBC**|  Legacy API keys will be deleted and removed from the Docs / Dashboard.| You have to migrate to use the new API keys by this point or your app will break.  
# Why are we doing this?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#why-are-we-doing-this)
Currently there is a tight coupling between API keys and the JWT secret which presents a few challenges:
  1. **Difficult to revoke the`service_role` or `anon` key.** Imagine if someone in your Supabase organization leaves the team, and you want to roll your project’s JWT secret to revoke their access? Or you accidentally commit the `service_role` key into your version control system and need to roll it?
If either of these keys gets leaked, the developer’s only option is to roll the JWT secret by generating a new one. When the JWT secret is rolled, all authenticated users would be logged out, clients using the older anon and service keys would break. Realistically, there is no way to roll the JWT secret without downtime.
  2. **Sub-optimal developer experience to create an API key with a custom role.** Developer needs to sign a JWT with a long expiry time and their custom role using the secret.


The introduction of new API keys solves the above problems by allowing the developer to:
  * roll individual API keys
  * roll the API keys without logging out their users
  * create custom API keys easily


### **API Key changes**[ #](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#api-key-changes)
These are the planned changes for the API keys:
  * `anon` key will be renamed to `publishable` key and the `service_role` key will be renamed to `secret` key. `publishable` api keys are meant to be used along with Supabase Auth users and `secret` api keys are for use from the server side and bypasses all row level security policies. We chose to use `publishable` and `secret` to align with stripe’s terminology and preferred it to terms like `public` and `private` since those could be confused with public / private key cryptography when we introduce asymmetric JWTs to Supabase Auth.
  * New API keys will look like regular strings instead of JWTs:
**Legacy API Keys**| **Equivalent New API Keys**  
---|---  
`anon` key: `eyJhbGciOiJIUzI1...FDsBGn0iqSmL28Zeg8f0`| `publishable` key: `sb_publishable_123abc`  
`service_role` key: `eyJhbGciOiJIUzI1...SEVEyZQNhffCoSj4P5A`| `secret` key: `sb_secret_123abc`  
  * With the new API keys, it will be possible to revoke individual API keys and without revoking the JWT secret. Once the legacy API key is revoked, it won’t be possible to restore them.
  * New projects will be created with both new and legacy API keys until **1st May 2025.** New projects created after this date will only be created with new API keys.
  * Projects that are restored after **1st May 2025** will not be restored with legacy API keys.
  * Legacy API keys will no longer work for all projects after **1st October 2025.**


# Migration to the new API keys[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#migration-to-the-new-api-keys)
  1. If you want to use the new API keys, all you need to do is to swap out your keys for the new ones:

**Legacy API Keys**| **Equivalent New API Keys**  
---|---  
`anon` key| `publishable` key  
`service_role` key| `secret` key  
  1. Update your `.env` file to contain the new API key


`
1
# the legacy anon key
2
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...w6PYobnC7Ep7EnDd9DG25qBFDsBGn0iqSmL28Zeg8f0 
34
# the new publishable key
5
SUPABASE_PUBLISHABLE_KEY=sb_publishable_123abc
`
  1. Instantiate the supabase client with the new API Keys.


`
1
import { createClient } from 'supabase/supabase-js' 
23
const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)
`
  1. After all your clients have been instantiated with the new API keys, you can revoke the legacy keys from the dashboard.


# Frequently Asked Questions[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#frequently-asked-questions)
  * What is the timeline for the migration? 
    * See "Timeline" section above
  * My app is deployed through Vercel / Netlify, how do I use the new API keys? 
    * If you’re using Vercel or Netlify, changing the keys in your environment will only be reflected when you trigger a new deployment.
  * I only connect to the database via the connection string — do I need to worry about this at all? 
    * No, unless you use the supabase client libraries to make queries to the database.
  * How do we do custom claims? 
    * Currently, users have to manually create a new key with their custom claims using the JWT secret provided.
    * There will be support for creating new API keys with custom properties in the dashboard and management API.
  * What benefit do we get from migrating to use the new API keys? 
    * You can revoke an individual key in the event of a compromise
    * You can revoke keys without logging out existing users
    * You don’t have to deal with minting a new JWT using the JWT secret if you want to add custom claims to an API key.
  * What is the interaction between the `apikey` header, the `Authorization` header and the underlying Postgres role used? 
    * The new API keys are just regular strings instead of JWTs.
    * By default, secret API keys assume the `service_role`. When creating the new secret API keys, you can override this behavior and assign a custom `role`. Downstream services like postgREST and storage assume this role when they are called with this API key.
    * By default, publishable API keys default to the `anon` role. When a user JWT is passed in via the `Authorization` header, the role claim in the JWT is used instead. You cannot map publishable keys to custom roles when creating the key, like you will be able to do with secret API keys.


![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fce8698f8-c279-456b-8be2-1a81790ac2c1&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### [Dashboard Weekly Updates [02/09/24 - 09/09/24] ](https://github.com/orgs/supabase/discussions/29239)
Sep 12, 2024
## Schema Visualizer nodes are now persisted[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#schema-visualizer-nodes-are-now-persisted)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F55e18a2a-096a-4e88-b0d1-48ca0856a9a8&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
This was yet another request that we've commonly heard from everyone and we're taking a first step to making this happen 😄 Position of the nodes will now be stored within local storage so that you won't have to re-position them each time you land on this page. We've also added a button to help arrange the nodes automatically if that might be preferred!
Note that if you add new tables to the schema however, the node positions will be defaulted to a certain position that may overlap with other nodes - we're definitely looking into how we can make that better so that new nodes can be easily identified (and then shifted around to your liking 🙂)
PR: <https://github.com/supabase/supabase/pull/29136>
Link: <https://supabase.com/dashboard/project/_/schemas>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[General](https://supabase.com/dashboard)
  * Minor improvements to layouts and buttons to ensure their visibility on smaller screens ([PR](https://github.com/supabase/supabase/commit/3fa447d57d36c1de9d323f8de37820cbfbf4ce0d))
  * Fix project status filter on home page to only show active projects if only the active checkbox is checked ([PR](https://github.com/supabase/supabase/pull/29223))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Fix client crash when creating an empty table with no columns ([PR](https://github.com/supabase/supabase/pull/29062))
  * Fix handling of of large JSON / text fields in the side panel text editor ([PR](https://github.com/supabase/supabase/pull/28766))


[SQL Editor](https://github.com/supabase/supabase/pull/29173)
  * Add client side validation for query size (max 1MB) ([PR](https://github.com/supabase/supabase/pull/29173))
  * Couple of fixes around adding a new folder with the same name as an existing one ([PR](https://github.com/supabase/supabase/pull/29204))


[Database](https://supabase.com/dashboard/project/_/database/tables)
  * Update Stripe Wrapper with more tables ([PR](https://github.com/supabase/supabase/pull/29141))
  * Remove docs button for database extensions that have no documentation yet ([PR](https://github.com/supabase/supabase/pull/29203))


### [Edge Functions are now Deno 1.45 compatible ](https://github.com/orgs/supabase/discussions/29189)
Sep 10, 2024
Supabase [Edge Runtime version 1.57](https://github.com/supabase/edge-runtime/releases/tag/v1.57.0) is compatible with Deno 1.45.
Supabase's hosted platform was upgraded to use this release when serving Edge Functions starting last week.
If you're using Supabase CLI for local development [latest stable release 1.192.5](https://github.com/supabase/cli/releases/tag/v1.192.5), it adds compatibility for Deno 1.45.
## How do I find which version of Edge Runtime I'm running?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-do-i-find-which-version-of-edge-runtime-im-running)
### Supabase CLI (local)[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supabase-cli-local)
When you run supabase functions serve, it should show the current version of Edge Runtime used (and its Deno compatibility)
`
1
> supabase functions serve
23
Setting up Edge Functions runtime...
4
Serving functions on http://127.0.0.1:54321/functions/v1/<function-name>
5
Using supabase-edge-runtime-1.58.2 (compatible with Deno v1.45.2)
`
### Hosted Platform[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#hosted-platform)
You can check the served_by field in log events to see which Edge Runtime version was used to serve your function.
![Screenshot 2024-06-18 at 7 44 47 PM](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F5358%2F7dbfe2f2-6f8b-4ae8-b19c-7d01ef5c8adc&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We try our best to maintain backward compatibility in these upgrades. If you're experiencing any issues, please feel free to make a [support request](https://supabase.help)
### [Dashboard Weekly Updates [26/08/24 - 02/09/24] ](https://github.com/orgs/supabase/discussions/29030)
Sep 2, 2024
## Upgrade your organization directly from our pricing page[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#upgrade-your-organization-directly-from-our-pricing-page)
<https://github.com/user-attachments/assets/2262d816-0c69-4c58-a6e2-1ce4868122f2>
Users who are logged in will now be able to select and upgrade their organization from the pricing page itself when clicking on the Upgrade to Pro / Team plan buttons. This is mainly to help streamline this process so that users can upgrade their existing organizations, and prevent confusions where users end up creating new paid organizations instead.
PR: <https://github.com/supabase/supabase/pull/28942>
Link: <https://supabase.com/pricing>
## UI improvements around credit card billing information[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#ui-improvements-around-credit-card-billing-information)
![Screenshot 2024-08-29 at 12 45 11](https://github.com/user-attachments/assets/0af61d92-b063-4a7a-b622-7165cbe7f1ab)
The selected payment method on the [billing page](https://supabase.com/dashboard/org/_/billing) is easily missed as you'll need to scroll down before finding it. In particular with outstanding invoices, it may not be obvious that the wrong card (or even expired card) might have been selected as the default. As such we now will
  * Indicate which cards are about to expire (within the current month)
  * Indicate which cards have expired
  * Show the selected payment method, along with a quick link to change it on the invoices page


PR: <https://github.com/supabase/supabase/pull/28971>
Link: <https://supabase.com/dashboard/org/_/billing>
## Set payment method as default when adding a new payment method[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#set-payment-method-as-default-when-adding-a-new-payment-method)
![Screenshot 2024-08-27 at 17 59 50](https://github.com/user-attachments/assets/c1c1517b-d28e-4878-9560-6375dd1ea826)
When adding a new payment method, we have now added a checkbox to set the card as default which is toggled on by default. This should resolve a UX issue whereby customers needed to explicitly set the card as default in a separate manual step after adding it.
PR: <https://github.com/supabase/supabase/pull/28921>
Link: <https://supabase.com/dashboard/org/_/billing>
## Choose which schemas to share with OpenAI[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#choose-which-schemas-to-share-with-openai)
![AI assistant schema](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F68056238-937d-4285-bbe4-d973fa4e09e3&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
This mainly applies to wherever the Supabase AI assistant is present in the dashboard (SQL Editor + RLS policies). You can now choose which schemas to share with OpenAI as opposed to sending information from all schemas in hopes to improve the output quality of the assistant by only sharing relevant information for your prompts to the assistant.
Do keep in mind that you'll need to [opt in to sending anonymous data to OpenAI](https://supabase.com/dashboard/org/_/general) prior to doing this 🙂 You may also verify exactly what data is being sent [here](https://supabase.com/dashboard/org/_/general) as well under "Important information regarding opting in"!
PR: <https://github.com/supabase/supabase/pull/28594>
Link: <https://supabase.com/dashboard/project/_/sql/new>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[General](https://supabase.com/dashboard)
  * Show which is the last sign in method used on login page ([PR](https://github.com/supabase/supabase/pull/28631))
  * Added 3 new regions to spin up projects from: Ohio, Stockholm, Paris, and Zurich ([PR](https://github.com/supabase/supabase/pull/28806))
  * Commands added for cmd+k to search and open snippets in the SQL Editor ([PR](https://github.com/supabase/supabase/pull/28573))
  * Support pasting image (via Cmd/Ctrl + v) in the feedback widget ([PR](https://github.com/supabase/supabase/pull/28475))
  * Use expanding text area for RLS AI assistant for multi line prompts ([PR](https://github.com/supabase/supabase/pull/28444))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Save last selected schema, no longer defaults to public schema ([PR](https://github.com/supabase/supabase/pull/28662))
  * Set the correct schema in the schema selector when opening a table via URL directly ([PR](https://github.com/supabase/supabase/pull/28560))
  * Support exporting table data as SQL seed file ([PR](https://github.com/supabase/supabase/pull/28670))
  * Couple of fixes for bugs around composite foreign keys ([PR](https://github.com/supabase/supabase/pull/28585))
  * Improve display of estimated row count for the table if the table has > 50k rows, to emphasize that it's an estimated count ([PR](https://github.com/supabase/supabase/pull/28549))
  * Spreadsheet import now checks column types from imported spreadsheet ([PR](https://github.com/supabase/supabase/pull/17072))


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Fix folder name editing where clicking on the input field toggles the folder ([PR](https://github.com/supabase/supabase/pull/28913))
  * Support opening cell value via right click into a side panel for a more detailed view ([PR](https://github.com/supabase/supabase/pull/28547))


[Auth](https://supabase.com/dashboard/project/_/auth/policies)
  * "With check" checkbox is toggled on by default for commands that involve a with check expression ([PR](https://github.com/supabase/supabase/pull/28670))


[Storage](https://supabase.com/dashboard/project/_/storage/buckets)
  * Support searching and sorting buckets ([PR](https://github.com/supabase/supabase/pull/28416))


[Logs Explorer](https://supabase.com/dashboard/project/_/logs/explorer)
  * Support copying cell content via context menu ([PR](https://github.com/supabase/supabase/pull/28439))


### [Dashboard Weekly Updates [26/08/24 - 30/08/24] ](https://github.com/orgs/supabase/discussions/29004)
Aug 30, 2024
![screenshot-2024-08-30-at-13 18 28](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F29aec90a-a524-40f3-827c-f469414aa6cd&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The SQL Editor got an upgrade this week, finally letting you organize snippets into folders!
  * Favourites and Shared snippets are in folders now
  * Organize Private snippets in folders as you like
  * Share snippets with your team as you could before


Link: <https://supabase.com/dashboard/project/_/sql/new> PR: <https://github.com/supabase/supabase/pull/27881>
### Other bug fixes and improvements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-bug-fixes-and-improvements)
**Project compute size badge**
  * See project compute details and upgrade right from the home screen ([PR](https://github.com/supabase/supabase/pull/23234))


**SQL Editor**
  * Update the SQL Editor AI Assistant model to the latest from OpenAI ([PR](https://github.com/supabase/supabase/pull/28818))


### [Moving to hourly usage-based billing for databases, based on disk consumption ](https://github.com/orgs/supabase/discussions/28849)
Aug 23, 2024
**tldr:**
  * **No changes for Free Plan users**
  * **Billing for paid plan organizations will be based on provisioned disk rather than used database space:**
    * Each project starts with 8 GB disk provisioned by default.
    * The first 8 GB of provisioned disk per project is free, then $0.125 per additional GB.
    * Charges are prorated down to the hour, which is advantageous for short-lived projects and branches.
    * Provisioned disk from Read Replicas will also be included in billing.
    * Enables upcoming features for enhanced control over disk and Postgres parameters.


**Timeline**
This change will be rolled out to new customers on **August 26th, 2024** and will be gradually rolled out to existing customers shortly after.
**Changes**
We are adjusting our pricing to offer more flexibility and self-serve for developers wanting to tune their disk and Postgres configuration. For example:
  * Some developers want disks with higher throughput
  * Some developers want to store more than 1GB of WAL (for tools like Airbyte/PeerDB, or adding more read replicas)


To make this available we will start billing for provisioned disk size (rather than database space used). Previously, costs associated with WAL files were not directly billed but also users could not control change `max_wal_size` (default is 1GB).
There is no action needed on your end. You will automatically be transitioned to the new billing model throughout the next couple of weeks. In case there is any change in your monthly bill, we will reach out to you proactively with additional information and give you a grace period to decrease your usage.
For customers on the Free Plan, there will be no changes; the total database space remains capped at 500MB. These adjustments only apply to customers on paid plans. The database disk will continue to autoscale when nearing capacity for paid plan customers.
| **Before**| **After (August 26th, 2024)**  
---|---|---  
**Price**|  $0.125 / GB| $0.000171 / GB-Hr  
Change| We take the average database space used for all projects, independent of how many days/hours you store the files and sum it up.| We will you based on the provisioned disk usage every hour. First 8GB per project are free. Read replicas will also incur disk costs.  
Invoice Item| Your invoices display 'Total Database size'.| Your invoices will display 'Disk Size GB-Hrs'.  
### Example 1: Pro plan org, active for whole month[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#example-1-pro-plan-org-active-for-whole-month)
In this scenario, an Organization is on the Pro Plan with 3 active projects.
**Usage**
Project| # Days Active| Average Database Space Used| Provisioned Disk| After: Provisioned Disk Size GB-Hrs  
---|---|---|---|---  
Project A| 30| 25 GB| 40.5 GB| 29,160 (720 hours * 40.5 GB)  
Project B| 30| 10 GB| 27 GB| 19,440 (720 hours * 27 GB)  
Project C| 30| 5 GB| 8 GB| 5,760 (720 hours * 8 GB)  
| | | |   
**Total**| | **40 GB**| | **54,360 GB-Hrs**  
**Billing**
| **Before**| **After**  
---|---|---  
Total Usage| 40 GB| 54,360 GB-Hrs  
Usage Discount (Pro Plan)| (8 GB)| (17,280 GB-Hrs - first 8 GB per project included)  
_**Billable Usage**_| **32 GB**| **37,080 GB-Hrs**  
| |   
Price| $0.125 / GB| $0.000171 / GB-Hr  
 _**Total Cost**_|  _**$4.00**_|  _**$6.43**_  
### Example 2: Pro plan org, active for part of the month[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#example-2-pro-plan-org-active-for-part-of-the-month)
In this scenario, an Organization is on the Pro Plan with 3 active projects.
**Usage**
Project| # Days Active| Average Database Space Used| Provisioned Disk| After: Provisioned Disk Size GB-Hrs  
---|---|---|---|---  
Project A| 30| 9 GB| 12 GB| 8,640 (720 hours * 12 GB)  
Project B| 15| 9 GB| 12 GB| 4,320 (360 hours * 12 GB)  
Project C| 2| 9 GB| 12 GB| 576 (48 hours * 12 GB)  
| | | |   
**Total**| |  27 GB| | 13,536 GB-Hrs  
**Billing**
| **Before**| **After**  
---|---|---  
Total Usage| 27 GB| 13,536 GB-Hrs  
Usage Discount (Pro Plan)| (8 GB)| (9,024 - first 8 GB per project included)  
_**Billable Usage**_| **19 GB**| **4,512 GB-Hrs**  
| |   
Price| $0.125 / GB| $0.000171 / GB-Hr  
 _**Total Cost**_|  _**$2.38**_| **$0.77**  
### Where do I see my disk size?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#where-do-i-see-my-disk-size)
You can see your project’s disk size in your [database settings](https://supabase.com/dashboard/project/_/settings/database) (Project Settings > Database).
![Screenshot 2024-07-25 at 09 36 09](https://github.com/user-attachments/assets/f0429333-d65f-4172-bc6c-53569d1ea0a3)
### How can I resize my disk down?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-can-i-resize-my-disk-down)
Your disk size is based on your database space usage. As a first step, you need to identify current database space usage and reduce it. To see your current database space usage, head over to the built-in [“Database” project report](https://supabase.com/dashboard/project/_/reports/database). Once you have reduced your database space and want to reduce your provisioned disk, you can upgrade your Postgres version through your [project settings](https://supabase.com/dashboard/project/_/settings/infrastructure) to automatically rightsize your disk. For further information around disk management and reducing database space, please refer to our [docs](https://supabase.com/docs/guides/platform/database-size#disk-management).
### Is this going to affect my monthly bill?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#is-this-going-to-affect-my-monthly-bill)
If your current disk size is >8GB, this is likely going to impact you. Note that this will be gradually rolled out and you will be notified about the concrete impact on your organization and given a 3-month grace period, which gives you time to right-size your disk and minimize the impact of this change.
### [Threshold for transitioning projects to physical backups lowered to 15GB ](https://github.com/orgs/supabase/discussions/28738)
Aug 19, 2024
Further to [earlier](https://github.com/orgs/supabase/discussions/18654) [discussions](https://github.com/orgs/supabase/discussions/20122), the threshold for transitioning large databases to use physical backups for their daily backups is being lowered to 15GB in the next few days.
Physical backups are more performant, have lower impact on the db, and avoid holding locks for long periods of time. Restores continue to work as expected, but backups taken using this method can no longer be downloaded from the dashboard.
Over the next few months, we'll be introducing functionality to restore to a separate, new database, allowing for the perusal of the backed up data without disruption to the original project.
Please refer to [supabase.com/docs/guides/platform/backups#daily-backups-process](https://supabase.com/docs/guides/platform/backups#daily-backups-process) for additional details.
### [Improved invoices and more timely usage data ](https://github.com/orgs/supabase/discussions/28480)
Aug 8, 2024
Currently, usage data on the invoice breakdown and [organization usage page](https://supabase.com/dashboard/org/_/usage) has a 24-hour delay. Starting from **August 26th** , the usage data will have no more of 1 hour delay for new customers. Afterwards, the changes will be rolled out to existing customer gradually. We're also working on additional improvements to provide better usage insights.
![Screenshot 2024-07-31 at 21 06 58](https://github.com/user-attachments/assets/5365a59b-d49c-42de-a5cd-a2cd7f301b8a)
Additionally, we are revamping invoices to provide more detailed breakdowns of usage for enhanced transparency. Due to our new proration of project add-ons and storage down to the hour, you may notice slight variances in your monthly bill. For the majority of line items, you’ll see the project reference and usage on the invoice, which should make it clearer which project allocated the usage/costs.
A few examples:
Compute Hours is broken down per project and the compute credits ($10) is displayed as discount for the compute line item.
![Screenshot 2024-08-08 at 20 34 47](https://github.com/user-attachments/assets/135a896c-c427-4ce9-8e22-aa96003376b6)
Egress is broken down to each project and displays included quota (250GB) and over-age pricing ($0.09/GB)
![Screenshot 2024-08-08 at 20 34 57](https://github.com/user-attachments/assets/bb0afcf5-4b7f-43bf-a33f-052052b86091)
Realtime Messages line item shows package-based pricing with $2.50 per million.
![Screenshot 2024-08-08 at 20 35 26](https://github.com/user-attachments/assets/64699237-8638-4c4d-b40c-b06003ff5b1f)
### [Moving to hourly usage-based billing for IPv4, Custom Domain and Point-in-time recovery ](https://github.com/orgs/supabase/discussions/28438)
Aug 7, 2024
# Moving to hourly usage-based billing for IPv4, Custom Domain and Point-in-time recovery[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#moving-to-hourly-usage-based-billing-for-ipv4-custom-domain-and-point-in-time-recovery)
We’re moving to billing all project add-ons usage-based and prorated down to the hour at the end of your billing cycle. We're not altering the monthly prices.
## Timeline[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#timeline)
This change will be rolled out to new customers on **August 26th, 2024** and will be gradually rolled out to existing customers shortly after.
## Changes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#changes)
| Before| After (August 26th, 2024)  
---|---|---  
Custom Domain| $10 / month| $0.0137 / hour  
IPv4| $4 / month / database| $0.0055 / hour / database  
Point-in-time Recovery - 7 Days| $100 / month| $0.137 / hour  
Point-in-time Recovery - 14 Days| $200 / month| $0.274 / hour  
Point-in-time Recovery - 28 Days| $400 / month| $0.55 / hour  
Change| Project add-ons are paid upfront. Every time you change an add-on, you immediately pay for remaining time or get credits for unused time. Each change triggers an additional invoice.| We bill you at the end of your billing cycle for the hours you’ve used the project add-ons. No in-between charges, credit prorations or additional invoices.  
Invoice Item| Your invoices display '_Add-on Name_ '.| Your invoices will display '_Add-on Name_ Hours'.  
## Details[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#details)
We're updating how we bill project add-ons (IPv4, Point-in-time recovery, Custom Domain) without changing their monthly prices. This change will be rolled out on August 26th, 2024 for new customers and shortly after for existing customers.
Previously, when you added a project add-on, like IPv4 or PITR, you were immediately invoiced and charged for the remaining billing cycle period. At the start of a new cycle, you paid upfront for the entire month. If you removed an add-on mid-cycle, you received a credit for unused time.
Starting August 26th, you will be billed retrospectively for these add-ons, similar to Compute Hours. There are no more upfront charges, prorated invoices, or credits. You simply pay for the exact hours you use the project add-ons.
Plans (Pro/Team/Enterprise) are still charged upfront and there are no changes to how they are billed.
### [Moving to hourly billing for Storage Size ](https://github.com/orgs/supabase/discussions/28339)
Aug 2, 2024
# Hourly Billing for Storage[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#hourly-billing-for-storage)
We’re moving to more granular billing periods. We're not altering the prices or storage quotas. Every customer will benefit from this change, especially short-lived projects and customers using [Branching](https://supabase.com/docs/guides/platform/branching).
### **Timeline**[ #](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#timeline)
This change will be rolled out to new customers on **August 26th, 2024** and will be gradually rolled out to existing customers shortly after.
### **Changes**[ #](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#changes)
The price will move to "GB per hour" instead of "Total storage GB":
| Before| After (August 26th, 2024)  
---|---|---  
Price| $0.021 / GB| $0.00002919 / GB / hour  
Change| We take the average storage size for all projects, independent of how many days/hours you store the files.| We bill you only for the exact GBs used each hour.  
Invoice Item| Your invoices display 'Total storage size'.| Your invoices will display 'Storage Size GB-Hrs'.  
Let's step through 2 scenarios to explain how this change will benefit developers:
# **Example 1: Pro Plan Org, active for the full month**[ #](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#example-1-pro-plan-org-active-for-the-full-month)
In this scenario, an Organization is on the Pro Plan with 3 active projects.
#### **Usage**[ #](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#usage)
The projects are running for the entire month:
| Storage| # Days Active| Active Hours (After)  
---|---|---|---  
Project A| 200 GB| 30| 144,000 (720 hours * 200 GB)  
Project B| 1,500 GB| 30| 1,080,000 (720 hours * 1,500 GB)  
Project C| 2,500 GB| 30| 1,800,000 (720 hours * 2,500 GB)  
-| -| -| -  
Total| 4,200 GB| | 3,024,000 hours  
#### **Billing**[ #](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#billing)
After the billing changes on August 26th there would be **no change in pricing:**
| Before| After  
---|---|---  
Total Usage| 4,200 GB| 3,024,000 hours  
Usage Discount (Pro Plan)| (100 GB)| (74,400 hours)  
Billable Usage| 4,100 GB| 2,949,600 hours  
-| -| -  
Price| $0.021 / GB| $0.00002919 / GB / hour  
Total Cost| $86.10| $86.10  
# **Example 2: Pro Plan Org, active for part of the month**[ #](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#example-2-pro-plan-org-active-for-part-of-the-month)
In this scenario, an Organization is on the Pro Plan with 3 active projects.
**Usage**
In this scenario, some of the projects are only active for a few days in the month:
| Storage| # Days Active| After: GB Hours  
---|---|---|---  
Project A| 200 GB| 2| 9,600 (48 hours * 200 GB)  
Project B| 1,500 GB| 15| 540,000 (360 hours * 1,500 GB)  
Project C| 2,500 GB| 30| 1,800,000 (720 hours * 2,500 GB)  
-| -| -| -  
Total| 4,200 GB| | 2,349,600 hours  
**Billing**
Currently we charge you for the full 4,200 GB, even though Project A and B weren’t active for the entire month. After August 26th, this scenario will be **22.87% cheaper:**
| Before| After  
---|---|---  
Total Usage| 4,200 GB| 2,349,600 hours  
Usage Discount (Pro Plan)| (100 GB)| (74,400 hours)  
Billable Usage| 4,100 GB| 2,275,200 hours  
-| -| -  
Price| $0.021 / GB| $0.00002919 / GB / hour  
Total Cost| $86.10| $66.41  
# Feedback[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#feedback)
This change should be universally beneficial, but if there is anything that we have missed just let us know and we will make sure we consider it before rolling out this change.
### [Wrappers Wasm FDW is on Public Alpha ](https://github.com/orgs/supabase/discussions/28267)
Jul 30, 2024
[WebAssembly Foreign Data Wrapper (Wasm FDW)](https://supabase.github.io/wrappers/#webassemblywasm-foreign-data-wrapper) is now on public alpha from Wrappers version >= 0.4.1. This release also contains two new Wasm FDWs: [Snowflake](https://supabase.github.io/wrappers/snowflake/) and [Paddle](https://supabase.github.io/wrappers/paddle/).
### What is Wasm FDW?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#what-is-wasm-fdw)
In previous versions of Wrappers, all the foreign data wrappers need to be built into `wrappers` extension. The develop/test/release cycle is time consuming and fully on Supabase teams. To speed up this process and give more flexibility to community, we're adding Wasm to the Wrappers framework. With this new feature, users can build their own FDW using Wasm and use it instantly on Supabase platform.
Another benefit is because of the improved modularity, each FDW can be updated and loaded individually. New FDWs release will be quicker than before. Also, `wrappers` extension size won't be bloated as more FDWs added in.
### What are the changes?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#what-are-the-changes)
There is no changes from end-users' perspective, all existing native FDWs are still same. The Wasm FDW only brings a new way of developing and distributing FDW.
### How to use it?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-to-use-it)
Visit `Database -> Platform -> Wrappers` on Supabase Studio, enable `Wrappers` and choose `Snowflake` or `Paddle`, then create foreign tables.
Visit [Snowflake Wasm FDW docs](https://supabase.github.io/wrappers/snowflake/) or [Paddle Wasm FDW docs](https://supabase.github.io/wrappers/paddle/) for more details.
### How to develop my own Wasm FDW?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-to-develop-my-own-wasm-fdw)
To build your own Wasm FDW, visit [the example project](https://github.com/supabase-community/wasm-fdw-example) to get started.
### [Developer Updates - June 2024 ](https://github.com/orgs/supabase/discussions/28154)
Jul 24, 2024
We have several updates and new features to share with you this month. Dive in to see what’s new from Supabase.
# Edge Runtime Inspector Feature (CLI)[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#edge-runtime-inspector-feature-cli)
![Edge Runtime Inspector Feature \(CLI\)](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjune%25202024%2Fedge_runtime_inspector.jpg%3Ft%3D2024-07-16T12%253A20%253A04.791Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve introduced the Edge Runtime Inspector, a powerful new feature in the CLI that helps you inspect and debug edge functions more efficiently. [Pull Request](https://supabase.link/pr-2308)
# View and Abort Running Queries (Supabase Studio)[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#view-and-abort-running-queries-supabase-studio)
![View and abort queries in Supabase Studio](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjune%25202024%2Fsupa_studio_view_query.png%3Ft%3D2024-07-16T12%253A20%253A19.171Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You can now view and abort queries currently running on your database (primary or replica) in the Supabase Studio SQL Editor. This feature gives you greater control and flexibility in managing your queries. [Pull Request](https://supabase.link/pr-26887)
# Logging Integration With The ELK Stack[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#logging-integration-with-the-elk-stack)
The Logflare to Elastic filebeat backend has been merged. This integration enables log drains to ELK stacks, providing more robust logging and monitoring capabilities. [Documentation](https://supabase.link/elastic-doc)
# Interpreting Supabase Grafana I/O Charts[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#interpreting-supabase-grafana-io-charts)
![Interpreting Supabase Grafana I/O Charts](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjune%25202024%2Fgrafana.png%3Ft%3D2024-07-16T12%253A20%253A42.350Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)We have published a guide on how to use the Supabase I/O charts to identify when you may need to scale your database, optimize your queries, or spin up a read replica. [Github Discussion](https://supabase.link/gh-discussion-27003)
# Breaking Change to Supabase Platform Access Control[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#breaking-change-to-supabase-platform-access-control)
On July 26, 2024, Supabase will be making breaking changes to our platform’s access control system. **Developer** and **Read-Only** roles will no longer have write access to an organization’s GitHub and Vercel integrations. These changes **will not** affect existing integrations that are in place. [Github Discussion](https://supabase.link/gh-discussion-27993)
# Change to Retention of Paused Free Tier Projects[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#change-to-retention-of-paused-free-tier-projects)
Starting June 24, 2024, paused Free Tier projects are restorable for 90 days. There is a grace period where all paused projects will continue to be restorable until September 22, 2024. [Github Discussion](https://supabase.link/gh-discussion-27497)
# Billing Improvements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#billing-improvements)
![Billing Improvements](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjune%25202024%2Fbilling.png%3Ft%3D2024-07-16T12%253A20%253A52.830Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve made significant improvements to our billing system to help you better understand compute pricing. These changes aim to prevent unexpected charges and provide clarity on “Compute Hours.” [Github Discussion](https://supabase.link/gh-discussion-27498)
# Quick product announcements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#quick-product-announcements)
[Edge Functions] We’ve implemented some key updates to Edge Functions, including adding Deno 1.43 support [[Github Discussion](https://supabase.link/gh-discussion-27349)]
# New Engineering and Troubleshooting Guides[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#new-engineering-and-troubleshooting-guides)
![Troubleshooting Guides](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjune%25202024%2Ftroubleshooting_guides.jpg%3Ft%3D2024-07-16T12%253A21%253A48.891Z830Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
  * [How Postgres chooses which index to use](https://supabase.link/gh-discussion-26959)
  * [Using SQLAlchemy with Supabase](https://supabase.link/gh-discussion-27071)
  * [Supabase & Your Network: IPv4 and IPv6 compatibility](https://supabase.link/gh-discussion-27034)
  * [Understanding the Usage Summary on the Dashboard](https://supabase.link/gh-discussion-27479)
  * [Supavisor and Connection Terminology Explained](https://supabase.link/gh-discussion-27388)
  * [Prisma Error Management](https://supabase.link/gh-discussion-27395)
  * [How to change max database connections](https://supabase.link/gh-discussion-27197)
  * [Inspecting edge function environment variables](https://supabase.link/gh-discussion-27139)


# Made with Supabase[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#made-with-supabase)
  * Dribble - Flutter NBA name guess game available for iOS and Android [[Website](https://supabase.link/made-with-supa-dribble)]
  * EvalHub - an open-source platform for researchers to discover AI evaluation metrics [[Website](https://supabase.link/made-with-supa-evalhub)]
  * SVGPS - Removes the burden of working with a cluster of SVG files by converting your icons into a single JSON file [[Website](https://supabase.link/made-with-supa-svgps)]
  * CleanCoffee - Lean coffee discussion utility where you can create boards and share with friends [[Website](https://supabase.link/made-with-supa-clean-coffee)]
  * Rewritebar - Improve your writing in any macOS application with AI assistance. Quickly correct grammar mistakes, change writing styles or translate text [[Website](https://supabase.link/made-with-supa-rewritebar)]


# Community highlights[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#community-highlights)
  * Building a Basic Social Network with Remix and Supabase [[YouTube](https://supabase.link/yt-community-social-remix)]
  * Next Level Supabase Techniques For Your Production App! [[YouTube](https://supabase.link/yt-community-next-level-supa)]
  * Building a Local-First React Native App with PowerSync and Supabase [[YouTube](https://supabase.link/yt-community-local-first-react)]
  * Build a Fullstack Job Portal App with Next.js 14, Tailwind, Supabase, Stripe, Clerk [[YouTube](https://supabase.link/yt-community-full-stack-job-portal)]
  * Generate Vector Tiles with PostGIS [[Blog](https://supabase.link/tile-blog)] [[YouTube](https://supabase.link/yt-postgis-tile)]


### [DigiCert no longer being used as the CA for Supabase HTTP APIs ](https://github.com/orgs/supabase/discussions/28118)
Jul 22, 2024
Supabase HTTP APIs are [no longer using DigiCert](https://developers.cloudflare.com/ssl/reference/migration-guides/digicert-update/) as the root CA. This should have **no** impact on the vast majority of environments, as the other CAs in use are essentially universally trusted.
If your client environment only trusts certificates signed by DigiCert, you could be impacted. We're currently using Cloudflare to serve our HTTP APIs, and recommend ensuring that any client environment that only trusts a specific subset of CAs trusts [all of the CAs](https://developers.cloudflare.com/ssl/reference/certificate-authorities/) Cloudflare uses.
### [Edge Functions: Deploy More Functions at No Extra Cost ](https://github.com/orgs/supabase/discussions/28062)
Jul 18, 2024
In an effort to simplify pricing, we are going to remove usage-based billing for the number of Edge Functions in your projects. Instead, we are going for a bigger quota across all plans at no extra costs. We picked the limits to ensure all customers are benefiting from this change.
Free Plan customers can now create 25 instead of 10 functions without the need to upgrade to a paid Plan.
| Free Plan| Pro Plan| Team Plan|  Enterprise Plan  
---|---|---|---|---  
Before| 10 included| 100 included, then $10 per additional 100| 100 included, then $10 per additional 100| Custom  
After| 25 included| 500 included| 1000 included| Unlimited  
This change is effective immediately and in case you were previously exceeding the number of included functions on a paid Plan, you will no longer be charged for it.
### [Supabase Platform Access Control: Organization Permissions Breaking Changes on July 26, 2024 ](https://github.com/orgs/supabase/discussions/27993)
Jul 15, 2024
 _These breaking changes are rolling out on**July 26, 2024** and affects all organizations that have members assigned either the **Developer** or **Read-Only** roles._
All Supabase organizations invite users and assign them to one of the following roles as part of membership to an organization:
  * **Owner**
  * **Administrator**
  * **Developer**
  * **Read-Only** (available only on Team and Enterprise plans).


Depending on the role, members are authorized to access a specific set of the organization's resources, such as permission to create a new project or change the billing email.
We recently re-evaluated the access that the **Developer** and **Read-Only** roles have and decided to implement changes to restrict them on a couple of resources to improve your organizations' security.
On July 26, 2024, we will turn off certain access that the **Developer** and **Read-Only** roles currently have to your organization's resources. The following table is to illustrate the breaking changes that will be going into effect:
Resource| Action| Developer| Read-Only  
---|---|---|---  
**Integrations**[1](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-content-fn-1)| | |   
Authorize GitHub| -| ✅ → ❌| ✅ → ❌  
Add GitHub Repositories| -| ✅ → ❌| ✅ → ❌  
GitHub Connections| Delete| ✅ → ❌| ❌[2](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-content-fn-2)  
Vercel Connections| Update| ✅ → ❌| ❌[2](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-content-fn-2)  
| Delete| ✅ → ❌| ❌[2](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-content-fn-2)  
You can learn more about our Platform Access Control here: <https://supabase.com/docs/guides/platform/access-control>.
If you have any questions or concerns please [contact support](https://supabase.help).
## Footnotes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#footnote-label)
  1. Existing integrations will continue to work. [↩](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-content-fnref-1)
  2. Role's permission to the resource and action will remain the same. [↩](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-content-fnref-2) [↩2](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-content-fnref-2-2) [↩3](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-content-fnref-2-3)


### [Dashboard Weekly Updates [08/07/24 - 15/07/24] ](https://github.com/orgs/supabase/discussions/27988)
Jul 15, 2024
### Option to use a dedicated `api` schema for your project[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#option-to-use-a-dedicated-api-schema-for-your-project)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2F93b68ad0-2c9c-43c2-9411-d800a1473bda&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
By default, the `public` schema is used to generate API routes for your database. In some cases, it's better to use a custom schema - this is important if you use tools that generate tables in the `public` schema to prevent accidental exposure of your data.
The dashboard supports this workflow through 2 options: either at the project creation step under "Security Options", or in the project's API settings after your project has been created. More information about this workflow in our documentation [here](https://supabase.com/docs/guides/database/hardening-data-api)!
Link: <https://supabase.com/dashboard/project/_/settings/api>
PR: <https://github.com/supabase/supabase/pull/27918>
### Other bug fixes and improvements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-bug-fixes-and-improvements)
[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Text area under AI assistant is now expandable for better UX with multi-line prompts ([PR](https://github.com/supabase/supabase/pull/27930))


[Database](https://supabase.com/dashboard/project/_/database/functions)
  * Added placeholder for function body editor section to hint the syntax if language selected is plpgsql ([PR](https://github.com/supabase/supabase/pull/27922))


[Logs Explorer](https://supabase.com/dashboard/project/_/logs/explorer)
  * Fixed logs explorer placeholder query for local set up ([PR](https://github.com/supabase/supabase/pull/27861/files))


### [Postgres 13 Deprecation Notice ](https://github.com/orgs/supabase/discussions/27946)
Jul 12, 2024
Supabase support for Postgres 13 is being deprecated as of 15th July 2024, and support for it will be fully removed on 15th November 2024.
All Postgres 13 projects should be upgraded to Postgres 15 before 15th November, 2024.
Any projects still on Postgres 13 after the 15th of November 2024 will be automatically upgraded to Postgres 15. If any Postgres extensions or functions are in use that cause the [upgrade process](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects#pgupgrade) [to](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects#extensions) [fail](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects#objects-dependent-on-postgres-extensions), a backup will be taken instead, and the project will be paused.
Postgres 15 comes with numerous features, bug fixes and performance improvements. Check out the announcement blog posts to find out what each version introduces.
  * [Postgres 14 Launch](https://supabase.com/blog/whats-new-in-postgres-14)
  * [Postgres 15 Launch](https://supabase.com/blog/new-in-postgres-15)


## Deprecation Timeline[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#deprecation-timeline)
  * **15th July** : All users are notified via email about Postgres 13 Deprecation. Users can self-serve upgrade to Postgres 15 [from our dashboard](https://supabase.com/dashboard/project/_/settings/infrastructure).
  * **30th September** : Users are reminded of impending deprecation via email.
  * **30th October** : Users are sent a final email reminder.
  * **15th November** : Any remaining projects on PG13 start getting migrated to PG15 (or paused, if there are upgrade issues).


### [Dashboard Weekly Updates [01/07/24 - 08/07/24] ](https://github.com/orgs/supabase/discussions/27876)
Jul 9, 2024
## Option to disable Data API when creating projects[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#option-to-disable-data-api-when-creating-projects)
![Screenshot 2024-06-24 at 6 58 14 PM](https://github.com/supabase/supabase/assets/8291514/41d89f56-4926-4db4-b603-6995f64ee312)
You can now opt to disable the Data API when creating a new project under a section called "Advanced Options", such that you will only be able to connect to your database via connection string. Note that this setting can be subsequently updated again in the project's [API settings](https://supabase.com/dashboard/project/_/settings/api) if and when you want to connect your project via the client libraries.
PR: <https://github.com/supabase/supabase/pull/26809>
Link: <https://supabase.com/dashboard/new/_>
## Authorization for Realtime is now available![#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#authorization-for-realtime-is-now-available)
![Screenshot 2024-07-09 at 18 24 03](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2Fb0df9271-8317-4659-826a-738072a2abc4&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You can now control client access to Realtime Broadcast and Presence by adding Row Level Security policies to the `realtime.messages` table! Read more about through our documentation [here](https://supabase.com/docs/guides/realtime/authorization)!
PR: <https://github.com/supabase/supabase/pull/27362>
Link: <https://supabase.com/dashboard/project/_/realtime/inspector>\
## Optimizations for table editor row count query[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#optimizations-for-table-editor-row-count-query)
![image](https://github.com/supabase/supabase/assets/19742402/69a9fe36-f739-4e59-9769-040bbd3635cf)
Previously, the Table Editor on the dashboard would run a `select count(*) from table` query to retrieve the number of rows in the table and display it in the editor (this also supports the pagination logic as well). However, understandably this query can be resource intensive and expensive if the table in question is particularly large. As such, we've chucked some optimizations around this logic to only retrieve the exact row count if the table has less than 50k rows, otherwise we'll retrieve an estimate of the row count instead. You'll still be able to get the exact row count but on demand instead.
PR: <https://github.com/supabase/supabase/pull/27612>
Link: <https://supabase.com/dashboard/project/_/editor>
## Support showing all entity types in the database/tables page[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#support-showing-all-entity-types-in-the-databasetables-page)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2Fa248fdff-9699-4dc0-a0f5-3fc752b76856&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
PR: <https://github.com/supabase/supabase/pull/27749>
Link: <https://supabase.com/dashboard/project/_/database/tables>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[General](https://supabase.com/dashboard/project/_)
  * More granular project statuses for pausing and restoration ([PR](https://github.com/supabase/supabase/pull/27213))
  * Support filtering projects by status (either active or paused) ([PR](https://github.com/supabase/supabase/pull/27818))


[Account](https://supabase.com/dashboard/account/me)
  * Added instructions on how to change your email for your account ([PR](https://github.com/supabase/supabase/pull/27093))


[Storage](https://supabase.com/dashboard/project/_/storage/buckets)
  * Fix uploading a folder to the storage explorer causes all files to be uploaded in a flat list with the folder name prefixed to the file name ([PR](https://github.com/supabase/supabase/pull/27744))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Optimized table editor select query when cutting off column values ([PR](https://github.com/supabase/supabase/pull/27553))


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Added labels and grid to SQL editor charts ([PR](https://github.com/supabase/supabase/pull/27787))


### [Dashboard Weekly Updates [17/06/24 - 24/06/24] ](https://github.com/orgs/supabase/discussions/27498)
Jun 24, 2024
### Greater clarity on costs when creating new projects[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#greater-clarity-on-costs-when-creating-new-projects)
![Screenshot 2024-06-14 at 17 06 16](https://github.com/supabase/supabase/assets/14073399/b3af35df-9a6c-46bd-a29c-0b0d76e1b420)
One of our bigger papercuts in terms of billing is customers not understand compute pricing and that they cannot launch unlimited projects for $25 in total per month. Customers also get confused with "Compute Hours" on their bill. The changes aim to alleviate any "surprise" compute charges and serves as kaizen improvement.
Changes involved are only applicable to paid plan organizations, as it's irrelevant for free plan organizations.
PR: <https://github.com/supabase/supabase/pull/27268>
Link: <https://supabase.com/dashboard/new/_>
### Address Table Editor "resorting" of rows when rows are updated and no active sorts applied[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#address-table-editor-resorting-of-rows-when-rows-are-updated-and-no-active-sorts-applied)
If you've tried updating a table via the Table Editor without an active sort in place, you'd have noticed that the rows seem to re-sort themselves, specifically the row that you were updating. While this is because rows are returned in an unspecified order without a sort clause from the select query, it certainly must've been a confusing UX. We've alleviated this problem by setting a default sort by clause when reading the table via the Table Editor, which will get overriden once you've set a sort via the UI.
PR: <https://github.com/supabase/supabase/pull/27097>
Link: <https://supabase.com/dashboard/project/_/editor>
### Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[General](https://supabase.com/dashboard/project/_)
  * Greater granularity in project statuses, specifically for when project is restoring, when restoring failed and when pausing failed ([PR](https://github.com/supabase/supabase/pull/27213))


[Database](https://supabase.com/dashboard/project/_/database/tables)
  * Table searching is now case in-sensitive ([PR](https://github.com/supabase/supabase/pull/27337))
  * Add duplicate table CTA (Similar to the Table Editor) ([PR](https://github.com/supabase/supabase/pull/27359))


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Auto limit fix for when SQL query has "fetch first n rows only" ([PR](https://github.com/supabase/supabase/pull/27179))
  * Preserve whitespace in results ([PR](https://github.com/supabase/supabase/pull/27324))


[Query Performance](https://supabase.com/dashboard/project/_/database/query-performance)
  * Support index advisor for queries from Postgrest ([PR](https://github.com/supabase/supabase/pull/27364))


[Org Billing](https://supabase.com/dashboard/org/_/billing#taxId)
  * Users can now only manage a single tax ID instead of multiple ([PR](https://github.com/supabase/supabase/pull/27246))


### [Paused Free Plan projects are restorable for 90 days ](https://github.com/orgs/supabase/discussions/27497)
Jun 24, 2024
 _This only impacts projects on the Free Plan because projects in any of the paid plans cannot be paused._
Beginning June 24, 2024, we're updating some project pause/restore behavior:
  * paused Free projects are restorable for 90 days following their pause date
  * any Free projects paused before June 24 will be able to restore at any point before September 22, 2024 so they have a full 90 days from when this announcement is made
  * once a project is no longer restorable, the "restore" option is replaced with an option to download the latest logical backup, taken right before the project is paused, and all Storage objects


This change is being made to enable us to maintain high development velocity on the platform. Previously, paused projects could be restored indefinitely. That creates the need for the platform to remain fully backwards compatible with outdated versions of Postgres and associated extensions. The update allows us to provide a reasonable pause/restore window while gaining the ability to evolve the platform.
### [Edge Functions are now Deno 1.43 compatible ](https://github.com/orgs/supabase/discussions/27349)
Jun 18, 2024
Supabase [Edge Runtime version 1.54 ](https://github.com/supabase/edge-runtime/releases/tag/v1.54.0) is compatible with Deno 1.43.
Supabase's hosted platform was upgraded to use this release when serving Edge Functions starting today.
If you're using Supabase CLI for local development [latest stable release 1.176.10](https://github.com/supabase/cli/releases/tag/v1.176.10), it adds compatibility for Deno 1.43.
### How do I find which version of Edge Runtime I'm running?[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-do-i-find-which-version-of-edge-runtime-im-running)
### Supabase CLI (local)[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supabase-cli-local)
When you run `supabase functions serve`, it should show the current version of Edge Runtime used (and its Deno compatibility)
`
1
> supabase functions serve
23
Setting up Edge Functions runtime...
4
Serving functions on http://127.0.0.1:54321/functions/v1/<function-name>
5
Using supabase-edge-runtime-1.54.2 (compatible with Deno v1.43.0)
`
### Hosted Platform[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#hosted-platform)
You can check the `served_by` field in log events to see which Edge Runtime version was used to serve your function . ![Screenshot 2024-06-18 at 7 44 47 PM](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F5358%2F7dbfe2f2-6f8b-4ae8-b19c-7d01ef5c8adc&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We try our best to maintain backward compatibility in these upgrades. If you're experiencing any issues, please feel free to make a [support request](https://supabase.help)
### [Developer Updates - May 2024 ](https://github.com/orgs/supabase/discussions/27338)
Jun 18, 2024
Supabase underwent Consolidation Month™ to focus on initiatives that improve the stability, scalability, and security of our products. We also have exciting product announcements that we can’t wait to share. Let’s dive in!
## Consolidation Month™[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#consolidation-month)
We kicked off Consolidation Month (no it’s not actually trademarked) during the month of May. During this time, every product team within Supabase addressed outstanding performance and stability issues of existing features. Here’s a small subset of initiatives and product announcements as part of Consolidation Month:
## Auth Launches @supabase/ssr for Better SSR Framework Support[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#auth-launches-supabasessr-for-better-ssr-framework-support)
![Auth Launches @supabase/ssr](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmay2024%2Fauth_launcher_better_SSR.jpg%3Ft%3D2024-06-18T02%253A13%253A54.164Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The newly released @supabase/ssr package improves cookie management, developer experience, and handling of edge cases in various SSR and CSR contexts. We’ve added extensive testing to prevent issues that users experienced with the @supabase/auth-helpers package.
[Announcement](https://supabase.link/auth-ssr-email)
## pgvector v0.7.0 Release Features Significant Performance Improvements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#pgvector-v070-release-features-significant-performance-improvements)
![pgvector v0.7.0 Release](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmay2024%2Fpgvector_v070.jpg%3Ft%3D2024-06-18T02%253A16%253A29.754Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
pgvector v0.7.0 introduced float16 vectors that further improve HNSW build times by 30% while reducing shared memory and disk space by 50% when both index and underlying table use 16-bit float. The latest version also adds sparse and bit vectors as well as L1, Hamming, and Jaccard distance functions.
[Announcement](https://supabase.link/pgvector-v070-github)
## Edge Functions Improves Memory Handling[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#edge-functions-improves-memory-handling)
![Functions Memory Handling](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmay2024%2Fedge_functions_improvements.jpg%3Ft%3D2024-06-18T02%253A18%253A05.014Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The Edge Functions team has significantly reduced the error rate for functions encountering memory issues by implementing better safeguards. This has greatly minimized errors with the 502 status code. Additionally, status codes and limits are now documented separately.
[Status Codes](https://supabase.link/functions-codes-github) | [Limits](https://supabase.link/functions-limits-github)
## Dashboard Supports Bigger Workloads as Projects Grow[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#dashboard-supports-bigger-workloads-as-projects-grow)
![Dashboard Supports Bigger Workloads](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmay2024%2Fdashboard_workloads.jpg%3Ft%3D2024-06-18T02%253A19%253A39.432Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The Supabase Dashboard is now better equipped to handle your projects, regardless of their size. We have implemented sensible defaults for the amount of data rendered and returned in the Table and SQL Editors to prevent browser performance issues while maintaining a snappy user experience.
[Announcement](https://supabase.link/dashboard-workloads-email)
## Realtime Standardizes Error Codes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#realtime-standardizes-error-codes)
![Realtime Error Codes](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmay2024%2Frealtime_standardized_error_codes.jpg%3Ft%3D2024-06-18T02%253A21%253A16.200Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Realtime now emits standardized error codes, providing descriptions of their meanings and suggested actions. This enhancement improves your error-handling code and helps to narrow down whether the issue lies with the database, Realtime service, or client error.
[Realtime Error Codes](https://supabase.link/realtime-codes-github)
## RLS AI Assistant v2[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#rls-ai-assistant-v2)
![RLS AI Assistant v2](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmay2024%2FRLS_AI_Assistant.jpg%3Ft%3D2024-06-18T02%253A30%253A33.913Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve improved the prompt and output of our RLS AI Assistant by including best practices found in our RLS docs and upgrading to OpenAI’s newest GPT-4o. We’ve also introduced numerous test scenarios to make sure you’re getting the right security and performance recommendations by comparing parsed SQL with the help of pg_query.
[Pull Request](https://supabase.link/rls-ai-v2-email)
## Quick product announcements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#quick-product-announcements)
  * [Functions] JSR modules are supported in Edge Functions & Edge Runtime [[Announcement](https://supabase.link/functions-jsr-email)]
  * [Functions] Debug Edge Functions with Chrome DevTools [[Docs](https://supabase.link/functions-devtools-email)]
  * [Functions] Use HonoJS web Framework with Edge Functions [[Docs](https://supabase.link/functions-hono-email)]
  * [Analytics] Log Drains is in Private Alpha [[Announcement](https://supabase.link/log-drains-email)]
  * [Realtime] Realtime Authorization Early Access [[Announcement](https://supabase.link/realtime-authz-email)]
  * [Docs] SQL to PostgREST API Translator [[Docs](https://supabase.link/sql-to-rest-email)]
  * [Client libs] Supabase JavaScript SDK Sentry Integration now supports Sentry SDK v8 [[Commit](https://supabase.link/sentry-v8-email)]


## Made with Supabase[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#made-with-supabase)
  * GroupUp - organize social gatherings to hang out with friends [[Website](https://supabase.link/groupup-email)]
  * HabitKit - track habits, view daily progress, and stay motivated as you work towards your goals [[Website](https://supabase.link/habitkit-email)]
  * Meteron AI - LLM and generative AI metering, load-balancing and storage [[Website](https://supabase.link/meteron-email)]
  * EQMonitor - An app that displays and notifies earthquake information in Japan [[Website](https://supabase.link/eqmonitor-email)]
  * GitAuto - AI software engineer that writes, reads, and creates pull requests [[Website](https://supabase.link/gitauto-email)]
  * GenPPT - Free AI powerpoint presentation generator to help you create beautiful slides in minutes [[Website](https://supabase.link/genppt-email)]


## Community highlights[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#community-highlights)
  * Make your queries 43,240x faster [[Video](https://supabase.link/faster-queries-email)]
  * Exploring Support Tooling at Supabase: A Dive into SLA Buddy [[Article](https://supabase.link/sla-buddy-email)]
  * FlutterFlow SuperApp Complex Template : Developing Feed with Supabase [[Video](https://supabase.link/flutterflow-superapp-email)]
  * How We Use Supabase in Betashares Direct [[Video](https://supabase.link/betashares-direct-email)]
  * AI Assistant to Chat with Supabase Database [[Video](https://supabase.link/ai-chat-db-email)]
  * How to use wrappers in Supabase [[Video](https://supabase.link/wrappers-comm-email)]
  * Build Realtime Apps with Next.js and Supabase [[Video](https://supabase.link/realtime-next-supa-email)]
  * SvelteKit & Supabase Project Build [[Video](https://supabase.link/sveltekit-supa-email)]
  * Next.js 14 x Supabase — Build a Team component using shadcn [[Article](https://supabase.link/nextjs-supa-shadcn)]
  * Create a Real Time Chat App with Supabase and Angular [[Article](https://supabase.link/realtime-angular-email)]

_This discussion was created from the release[Developer Updates - May 2024](https://github.com/supabase/supabase/releases/tag/v1.24.05)._
### [Dashboard Weekly Updates [03/06/24 - 10/06/24] ](https://github.com/orgs/supabase/discussions/27166)
Jun 11, 2024
You might be wondering what we've been up to the past few weeks when we'd usually have some cadence in our weekly updates with our GitHub discussion updates - the team at Supabase had decided to commit to a month of consolidation by putting our efforts into each of the following pillars: Alerting, Testing, and Scaling. Let's jump right in to see what this means for the Dashboard! 💪🏻
### 🚨 Alerts: Enabling proactive resolution to issues that users run into[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#alerts-enabling-proactive-resolution-to-issues-that-users-run-into)
We want to find out about bugs before you do. In an effort to lower the time between deploying a bug and fixing it, we’ve set up some alerts that will enable us to be more proactively catch bugs, in particular for show-stopping problems (e.g that awful “A client side exception has occurred” screen)!
  * **Added alerts for critical points of failures ([PR](https://github.com/supabase/supabase/pull/27029))** This includes any errors that will completely prevent you from using the Supabase dashboard.
  * **Added alerts for full page client crash events with a custom error boundary ([PR](https://github.com/supabase/supabase/pull/25946))** Having a custom error boundary also allows us to potentially provide contextual hints/resolutions to the problem faced, such as what we did in this [PR](https://github.com/supabase/supabase/pull/26580).


### 🛠️ Testing: Identifying and covering critical points of failure[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#️testing-identifying-and-covering-critical-points-of-failure)
We believe in ensuring that minimally our critical paths are covered by tests as opposed to ensuring our dashboard has 100% test coverage. Anything that might completely block our users from doing what they need to do should be caught as much as possible before reaching production.
  * **Moved to Vitest + Integrating packages to make writing tests easier ([PR](https://github.com/supabase/supabase/pull/26303))** We’ve revamped our current test set up to use Vitest instead of Jest and have integrated [Mock Service Workers](https://mswjs.io/) (MSW) and [next-router-mock](https://www.npmjs.com/package/next-router-mock). These are all to support writing better tests easier, and also to reduce the amount of configuration we need to set up the tests.
  * **Expanded on Playwright for E2E tests ([PR](https://github.com/supabase/supabase/pull/26799))** We previously had a couple of Playwright tests written over in our [tests repository](https://github.com/supabase/tests) that we’ve decided to shift over to our main repository. We’re also in the midst of writing more tests and making them public


### 📈 Scaling: Supporting bigger workloads as the project grows[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#scaling-supporting-bigger-workloads-as-the-project-grows)
The dashboard should be able to keep up with your projects, no matter how big they grow - and even if unable to, it should never block you, or leave you feeling confused. This effort involved several solutions: gracefully failing if unable to handle large workloads, better observability, or even just better error handling to allow our users to self-service most errors. We were able to get improvements out for several common issues. Check out each individual PR for more information 😄
  * **Rendering large column data within the Table Editor ([PR](https://github.com/supabase/supabase/pull/26792))** We’re now limiting rendering each text/JSON based column data in the table editor at a max of 10kB when initially viewing the table, which should alleviate browser performance issues when rendering tables with large row data. You may load the entire column data on demand instead.
  * **Handling large results within the SQL editor ([PR](https://github.com/supabase/supabase/pull/26857))** A limit parameter will now be added as a suffix to select queries that are run in the SQL editor, which should prevent the browser performance from degrading when trying to query too much data. The limit parameter can be optionally removed if your intention might be to pull data in greater quantity.
  * **View ongoing queries in the SQL editor and support terminating them ([PR](https://github.com/supabase/supabase/pull/26887))** This came in response to a user who accidentally ran a large query through the SQL editor which ended up in the API request timing out, giving the impression that the query stopped running when in fact it was still running on the database in the background. This should help surface such problems and give the tooling required to abort erroneous queries.
  * **Contextual errors when something goes wrong ([PR](https://github.com/supabase/supabase/pull/23135))** While the attached PR was more of a POC, this is the direction we want to move towards to by providing contextual information and suggest possible resolutions whenever users run into an error


Of course consolidation is not a one time event, but an ongoing effort that our team is committing to in parallel to shipping new and exciting features. We hope that as our users, you will all be able to benefit from this with less blockers to keep you from building cool stuff 🙂
As always, if you have any feedback for us - we're just a message away through the feedback widget to the top right corner of the dashboard! We're always listening 👂🏻 (as in reading 👀).
### [@supabase/ssr updates and roadmap towards v1.0.0 ](https://github.com/orgs/supabase/discussions/27037)
Jun 5, 2024
[Go here for latest update](https://github.com/orgs/supabase/discussions/27037#discussioncomment-9862922)
Hey everyone,
I'm Stojan a member of the Supabase Auth team, bringing some updates about what's next with [`@supabase/ssr`](https://www.npmjs.com/package/@supabase/ssr). This is the [recommended package](https://supabase.com/docs/guides/auth/server-side#supabasessr) that helps you use the [Supabase JavaScript client](https://supabase.com/docs/reference/javascript/introduction) with SSR frameworks such as NextJS, Remix, SvelteKit and others.
We've been quite busy recently gathering feedback, reviewing common complaints and bugs with the package, and using it in the popular SSR frameworks. We've identified a few areas needing improvement and we've already started implementing them.
The package is still on major version 0, indicating its beta status. We plan to move it to major version 1 in the coming months making it the preferred way of using the Supabase JavaScript library in your favorite SSR framework.
First, we'll extract `@supabase/ssr`'s code from the [auth-helpers](https://github.com/supabase/auth-helpers) repository into [its own](https://github.com/supabase/ssr). We’re doing this because:
  * `@supabase/auth-helpers-x` (like for [NextJS](https://www.npmjs.com/package/@supabase/auth-helpers-nextjs)) is no longer supported by the team, as we expect people to move to `@supabase/ssr`.
  * It's no longer about "auth-helpers," but rather about how you can most effectively and ergonomically use the Supabase Client in various SSR and CSR contexts.
  * A standalone repo makes it easier for the community to contribute and for us to track issues.


We're going to release a fairly ground-up [reimplementation](https://github.com/supabase/ssr/pull/1) of the package. This should come as version 0.4.0 around mid-June. We've received a lot of signal in the past months from developers and the community about possible improvements for developer ergonomics and better handling for edge cases.
The reason for this change is because `@supabase/ssr` is really just a thin layer for cookie management on top of `@supabase/supabase-js`. We've identified some improvements that reduce odd and difficult-to-diagnose behavior. The new implementation will boast over 90% test coverage, including testing for issues that we’ve seen commonly reported so far.
As part of the new implementation, we are changing the API. The old API will be deprecated when we reach v1.0.0. This is to ensure the best possible experience for both developers and users. For most use cases and happy paths, the deprecated API will continue working during the phase-out, but we encourage switching as soon as possible. Once we release v1.0.0, major version 0 will no longer be maintained.
The change in the API is quite simple, so here’s an example of how it will look like. Instead of defining three cookie access methods `get`, `set` and `remove` like so:
`
1
createServerClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
2
	cookies: {
3
		get: async (name) => {
4
			// ...
5
		},
6
		set: async(name, value, options) => {
7
			// ...
8
		},
9
		remove: async(name) => {
10
			// ...
11
		}
12
	}
13
})
`
You would need to define two — `getAll` and `setAll` cookie access methods like so:
`
1
createServerClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
2
	cookies: {
3
		getAll: async() => {
4
			// return all cookies you have access to
5
		},
6
		setAll: async(cookiesToSet: { name: string; value: string; options: CookieOptions; }[]) => {
7
			// set the cookies exactly as they appear in the cookiesToSet array
8
		}
9
	}
10
})
`
Note that for `createBrowserClient` nothing needs to be done in most cases, it automatically works with the [`document.cookie` API](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie).
The change should be trivial for most SSR frameworks, and we'll be sure to update the guides to instruct you on how to change your code into this new way of accessing cookies.
Thanks for all your feedback! Feel free to ask any questions below!
### [Log Drains Private Alpha ](https://github.com/orgs/supabase/discussions/26650)
May 22, 2024
Log drains is currently private alpha, and is available for Teams and Enterprise customers. We are still firming up the [pricing and documentation](https://github.com/supabase/supabase/pull/26370), however it will likely involve a flat fee and variable egress usage. This will be announced separately through official channels.
We will be supporting **Datadog** as our initial provider.
The following destinations are in the works:
  1. Elastic/Filebeat
  2. Syslog


We are currently onboarding interested customers manually, so please fill out this form to get started: <https://forms.supabase.com/logdrains>.
### [Updated deployment instructions for supabase-grafana monitoring application ](https://github.com/orgs/supabase/discussions/26421)
May 17, 2024
We've released a fix to the deployment instructions for the [supabase-grafana monitoring application](https://github.com/supabase/supabase-grafana/blob/main/README.md#using-flyio).
If you're ingesting the [metrics endpoint](https://supabase.com/docs/guides/platform/metrics) into your pre-existing managed infrastructure without using the supabase-grafana app, this change does not affect you. If you're running the supabase-grafana app using the docker-compose mechanism, you are also not affected.
Fly applications launched off the repository between December 10, 2023, and May 16, 2024 are impacted, and will experience:
  * Fly application being shut down after periods of inactivity of a few minutes (default Fly.io behaviour)
  * Historical data will not be persisted after such a shutdown


The fix to the deployment instructions ensures that a persistent volume is created to store the data on, which prevents loss in case of a machine shutdown or restart. Additionally, autoshutdown behaviour is disabled, in order to prevent the app from being paused due to inactivity.
In order to fix an existing, already deployed Fly application, you can edit its [configuration](https://fly.io/docs/reference/configuration/) to disable `auto_stop_machines`, and create a persistent volume, and mount it at `/data` (similar to [the updated deployment instructions](https://github.com/supabase/supabase-grafana/blob/main/fly.toml#L8-L10)). Please note that as the newly created persistent volume will be empty to start, any existing metrics data will not be preserved as part of this change. If doing so is necessary, you can initially mount it at a separate path, copy the data over, and finally mount it at `/data`.
If you need further help, please reach out to Support via <https://supabase.help>
### [Dashboard Weekly Updates [06/05/24 - 13/05/24] ](https://github.com/orgs/supabase/discussions/26327)
May 15, 2024
## Conversational AI assistant in the SQL Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#conversational-ai-assistant-in-the-sql-editor)
![](https://github.com/supabase/supabase/assets/19742402/e808cf41-d9d4-4501-847b-7c0ccfcb8cb3)
This was previously behind a feature flag but we're now making this available by default, which will replace the existing single prompt UI that you saw previously at the top of the SQL editor. Once again, thank you all so much for the feedback that you've left us - we really appreciate them and they definitely do help in guiding us towards the ideal dashboard experience for everyone. 🙂🙏
We're also aware that the feature preview functionality is missing in the local set up - rest assured we're looking into it and hope to get a fix out soon for everyone!
PR: <https://github.com/supabase/supabase/pull/23142>
Link: <https://supabase.com/dashboard/project/_/sql>
## A step towards slightly more contextual error messages[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#a-step-towards-slightly-more-contextual-error-messages)
![](https://github.com/supabase/supabase/assets/19742402/f3876b34-a6d3-452a-97ec-5ae931cc8971)
A topic that came up in one of our discussions internally was regarding self-serviceability, and we realised that our error messages could do a much better job than just informing users what the error is about - especially when their errors from Postgres directly and the messages could be slightly cryptic for those not familiar with Postgres (yet 😉). The PR linked here is just a small idea and example for what we plan to do with error messages in the future, by giving users more context about the errors like possible solutions and links to relevant documentation. Hopefully this will make using the dashboard slightly more easier 🙂
PR: <https://github.com/supabase/supabase/pull/23135>
Link: <https://supabase.com/dashboard/project/_/editor>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[Branching](https://supabase.com/dashboard/project/_/branches)
  * Disable branch reset while branch is initializing ([PR](https://github.com/supabase/supabase/pull/23703))


[Database](https://supabase.com/dashboard/project/_/database/tables)
  * Allow searching for schema and tables when creating indexes ([PR](https://github.com/supabase/supabase/pull/25821))
  * Allow SQL language for writing database functions ([PR](https://github.com/supabase/supabase/pull/25986))


### [Developer Updates - April 2024 ](https://github.com/orgs/supabase/discussions/25860)
May 8, 2024
Here’s everything we shipped during our [GA week](https://supabase.link/ga-week-gh):
## Day 1 - Supabase is officially launching into General Availability (GA)[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#day-1---supabase-is-officially-launching-into-general-availability-ga)
![Day 1 - Supabase is officially launching into General Availability \(GA\)](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fapril2024%2Fday-1-ga-update.png%3Ft%3D2024-05-07T23%253A53%253A29.231Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase has moved to General Availability (GA) with over 1 million databases under management and over 2,500 databases launched daily. We’ve been production ready for years and now we are fully confident that we can help every customer become successful, from weekend projects to enterprise initiatives at organizations like Mozilla, 1Password, and PwC.
[Full announcement](https://supabase.link/ga-gh) | [Video announcement](https://supabase.link/ga-yt) | [X space](https://supabase.link/ga-x-space)
## Day 2 - Supabase Functions now supports AI models[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#day-2---supabase-functions-now-supports-ai-models)
![Day 2 - Supabase Functions now supports AI models](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fapril2024%2Fday-2-functions-ai.png%3Ft%3D2024-05-08T00%253A09%253A34.531Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase Functions has added a native API that makes it easy to run AI models within your functions while removing nasty cold starts. You can use the `gte-small` embedding model to generate text embeddings or bring your own Ollama server to tap into many more embedding models and Large Language Models (LLMs) like Llama3 and Mistral. Soon we’ll provide hosted Ollama servers so you won’t have to manage them yourselves for a more seamless experience.
[Blog post](https://supabase.link/ai-gh) | [Video announcement](https://supabase.link/ai-yt) | [X space](https://supabase.link/ai-x-space)
## Day 3 - Supabase Auth now supports Anonymous sign-ins[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#day-3---supabase-auth-now-supports-anonymous-sign-ins)
![Day 3 - Supabase Auth now supports Anonymous sign-ins](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fapril2024%2Fday-3-auth-anon.png%3Ft%3D2024-05-08T00%253A21%253A26.274Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase Auth heard your requests and went to work building anonymous sign-ins which enable you to create temporary users that have yet to sign up for your application. This lowers the friction for visitors to use your application while making it easy to convert them to permanent users once they’re hooked.
[Blog post](https://supabase.link/anon-auth-gh) | [Video announcement](https://supabase.link/anon-auth-yt) | [X space](https://supabase.link/anon-auth-x-space)
## Day 4 - Supabase Storage now supports the S3 protocol[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#day-4---supabase-storage-now-supports-the-s3-protocol)
![Day 4 - Supabase Storage now supports the S3 protocol](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fapril2024%2Fday-4-storage-s3.png%3Ft%3D2024-05-08T00%253A25%253A39.319Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase Storage already has standard and resumable uploads and now supports the industry standard S3 protocol enabling multipart upload and compatibility with a myriad of tools such as AWS CLI, Clickhouse, and Airbyte for a wide array of use cases.
[Blog post](https://supabase.link/storage-s3-gh) | [Video announcement](https://supabase.link/s3-storage-yt) | [X space](https://supabase.link/s3-storage-x-space)
## Day 5 - Supabase Security & Performance Advisor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#day-5---supabase-security--performance-advisor)
![Day 5 - Supabase Security & Performance Advisor](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fapril2024%2Fday-5-sec-perf-advisor.png%3Ft%3D2024-05-08T00%253A28%253A36.290Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase has managed over 1 million databases over the last four years and has seen all manner of use cases with common pitfalls that we’re helping our customers address with our Security, Performance, and Index Advisors. These Advisors will help to surface and fix insecure database configurations and recommend database and query optimizations to keep your database secure and performant for your mission critical workloads.
[Blog post](https://supabase.link/sec-perf-advisor-gh) | [Video announcement](https://supabase.link/sec-perf-advisor-yt) | [X space](https://supabase.link/sec-perf-advisor-x-space)
## GA Week Hackathon Winners[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#ga-week-hackathon-winners)
![GA Week Hackathon Winners](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fapril2024%2Fga-week-hackathon-winners.png%3Ft%3D2024-05-08T00%253A31%253A02.054Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We are delighted that so many high quality projects were submitted but in the end there could only be one Best Overall Project. The decision wasn’t easy but the Supabase panel of judges chose [vdbs](https://supabase.link/hackathon-vdbs) (vision database SQL) for the honorific. Congratulations 👏 to [@xavimonp](https://supabase.link/xavimonp) who will receive the prize of Apple AirPods.
[Full list of winners](https://supabase.link/ga-hackathon-winners-gh) | [All the submissions](https://supabase.link/made-with-supabase)
## One more thing from GA Week[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#one-more-thing-from-ga-week)
Just kidding, there’s always more than one. Here’s more awesome things we shipped:
  * [Supabase on the AWS Marketplace](https://supabase.link/sb-aws-marketplace-gh)
  * [Database branching is now Publicly Available](https://supabase.link/branching-pub-avail-gh)
  * [Supabase Bootstrap: the fastest way to launch a new project](https://supabase.link/sb-bootstrap-gh)
  * [Supabase Swift officially supported](https://supabase.link/sb-swift-gh)
  * [Oriole, table storage extension for Postgres, joins Supabase](https://supabase.link/sb-oriole-gh)
  * [Fly Postgres, a managed offering from Supabase, is available to everyone for testing](https://supabase.link/sb-managed-fly-gh)
  * [Supabase GA Week meetups in 27 cities around the world](https://supabase.link/ga-27-meetups-gh)
  * [Join our upcoming Meetup in SF at the a16z office with friends from Ollama and Fly.io](https://supabase.link/sf-ga-meetup)


## Community Highlights[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#community-highlights)
  * Changing Databases 5 Times in 48 Hours Boosted Our Launch to 35,000 Views [[Article](https://supabase.link/comm-highlight-changing-databases-5-times-in-48-hours-boosted-our-launch-to-35000-views)]
  * Crazy new Supabase feature: Understand and learn about anonymous users [[Video](https://supabase.link/comm-highlight-crazy-new-sb-feature-anon-users)]
  * Support unstructured data in Postgres with JSON columns [[Video](https://supabase.link/comm-highlight-pg-unstructured-data-json)]
  * Build an AI-powered blogging platform (Next.js, Langchain & CopilotKit) [[Article](https://supabase.link/comm-highlight-ai-blogging-platform)]
  * How to Secure Your Supabase Database and Storage [[Blog post](https://supabase.link/comm-highlight-secure-sp-db-storage)]
  * Self-host Protomaps PMTiles on Supabase Storage [[Video](https://supabase.link/comm-highlight-protomaps-pmtiles-storage)]
  * Supabase Realtime - How to deal with multiplayers in Next.js [[Blog post](https://supabase.link/comm-highlight-realtime-multiplayer-nextjs)]
  * The Hard Parts of Building an Application, Made Easy with Supabase [[Article](https://supabase.link/comm-highlight-hard-parts-made-easy-sb)]

_This discussion was created from the release[Developer Updates - April 2024](https://github.com/supabase/supabase/releases/tag/v1.24.04)._
### [JSR modules are supported in Edge Functions & Edge Runtime ](https://github.com/orgs/supabase/discussions/25842)
May 7, 2024
You can now use [JSR packages](https://jsr.io/docs/introduction) in your Edge Functions. JSR is a modern package registry for JavaScript and TypeScript created by the Deno team. With JSR support, you can use the latest versions of popular Deno packages like Oak.
How to use:
`
1
import { Application } from "jsr:@oak/oak/application";
2
import { Router } from "jsr:@oak/oak/router";
`
For local development, you will need to update Supabase CLI for the version [v1.166.1](https://github.com/supabase/cli/releases/tag/v1.166.1) or above.
Edge Functions also supports [using NPM ](https://supabase.com/blog/edge-functions-node-npm) and deno.land/x packages. If you are already using them, no changes are needed.
### [Dashboard Weekly Updates [22/04/24 - 29/04/24] ](https://github.com/orgs/supabase/discussions/23433)
Apr 30, 2024
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
We've been focusing on improving existing features on the dashboard and fixing some issues over the past week, so while we've got nothing shiny to shout out about, here's still a list of things that we've shipped! 🙂 As always, feel free to let us know if there's something that you guys _really_ want to see in the dashboard - we'll see how we can make it happen 😉
[General](https://supabase.com/dashboard)
  * Feedback widget will not clear its contents when closing until explicitly cleared or submitted [[PR](https://github.com/supabase/supabase/pull/23298)]


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Reinstate link button for foreign keys in table editor side panel [[PR](https://github.com/supabase/supabase/pull/23186)]
  * Fix creating foreign key on new column after changing column's name [[PR](https://github.com/supabase/supabase/pull/23204)]


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Set column width of results to be relative to column content length [[PR](https://github.com/supabase/supabase/pull/23235)]


[Authentication](https://supabase.com/dashboard/project/_/auth/policies)
  * Added Create policy CTA under each table for convenience [[PR](https://github.com/supabase/supabase/pull/23140)]


[Storage](https://supabase.com/dashboard/project/_/storage/buckets)
  * Added file size validation against project's upload limit when uploading files in dashboard [[PR](https://github.com/supabase/supabase/pull/23190)]


[Database](https://supabase.com/dashboard/project/_/database/query-performance)
  * Query performance: Fix searching via role and query [[PR](https://github.com/supabase/supabase/pull/23212)]
  * Query performance: Add db inspect docs link for visibility to aid in helping identify potential Postgres issues [[PR](https://github.com/supabase/supabase/pull/23268)]
  * Enumerated types: clean up form field when reopening create enumerated type panel [[PR](https://github.com/supabase/supabase/pull/23182)]
  * Tables: Add ellipses to table descriptions to prevent odd wrapping for long descriptions [[PR](https://github.com/supabase/supabase/pull/23240)]


### [Dashboard Weekly Updates [15/04/24 - 22/04/24] ](https://github.com/orgs/supabase/discussions/23139)
Apr 22, 2024
Supabase [GA Week](https://supabase.com/ga-week) just wrapped up but the shipping doesn't! This just summarises what have been shipped over the last week - and more 😉
## Auth support for anonymous sign-ins[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#auth-support-for-anonymous-sign-ins)
![allow-anon-sign-ins](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2F545870b8-7b3d-4e68-b861-e26414756910&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase Auth now supports anonymous sign-ins, which can be used to create temporary users who haven’t signed up for your application yet! This lowers the friction for new users to try out your product since they don’t have to provide any signup credentials.
Read more about this [here](https://supabase.com/blog/anonymous-sign-ins)
PR: <https://github.com/supabase/supabase/issues/21813>
Link: <https://supabase.com/dashboard/project/_/settings/auth>
## Storage support for S3 protocol[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#storage-support-for-s3-protocol)
![Screenshot 2024-04-22 at 16 27 25](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2Ff2ecd4a8-d046-41ad-b354-f2c877900050&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase Storage is now officially an S3-Compatible Storage Provider, and now you can use any S3 client to interact with your buckets and files: upload with TUS, serve them with REST, and manage them with the S3 protocol.
Read more about this [here](https://supabase.com/blog/s3-compatible-storage)
PR: <https://github.com/supabase/supabase/issues/22620>
Link: <http://supabase.com/dashboard/project/_/settings/storage>
## 3 new advisors to your database[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#3-new-advisors-to-your-database)
![Screenshot 2024-04-22 at 16 09 05](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2F26b95ef5-2485-4100-aa10-143a00c63224&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've added a Security Advisor, a Performance Advisor and a bonus Index Advisor as tools that can help improve your database, more specifically:
  * Security Advisor: for detecting insecure database configuration
  * Performance Advisor: for suggesting database optimizations
  * Index Advisor: for suggesting indexes on slow-running queries


Read more about them [here](https://supabase.com/blog/security-performance-advisor)!
PR: <https://github.com/supabase/supabase/issues/22842>
Link: <http://supabase.com/dashboard/project/_/database/security-advisor>
## 4 new database foreign data wrappers[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#4-new-database-foreign-data-wrappers)
![Screenshot 2024-04-22 at 15 56 43](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2F6de00079-928f-4a5d-b24c-615e5c8dbb7c&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've added support for data wrappers with Auth0, Cognito, Microsoft SQL Server, and Redis! Connect to these external data sources and query them directly from your database.
PR: <https://github.com/supabase/supabase/pull/22289>
Link: <https://supabase.com/dashboard/project/_/database/wrappers>
## Updating of some projects pages to more appropriate sections[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#updating-of-some-projects-pages-to-more-appropriate-sections)
![Screenshot 2024-04-22 at 16 03 56](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2Fb65e9949-c879-4279-988c-4b5bf0845ee6&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've renamed and shifted a couple of pages within a project to sections which we believe are more appropriate and relevant. These include:
  * Column Priveleges: Shifted from Auth section to [Database section](http://supabase.com/dashboard/project/_/database/column-privileges)
  * Database Replications: Renamed to Publications within the [Database section](https://supabase.com/dashboard/project/_/database/publications)
  * Query Performance Reports: Shifted from Reports section to [Database section](http://supabase.com/dashboard/project/_/database/query-performance)


We've also added more appropriate sections within the Database section in hopes to make things easier to find!
PR: <https://github.com/supabase/supabase/issues/22835>
Link: [https://supabase.com/dashboard/project/_](https://supabase.com/project/_)
## An option to submit a request to delete your account[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#an-option-to-submit-a-request-to-delete-your-account)
![Screenshot 2024-04-22 at 16 09 51](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2F237d6639-5ce1-4145-8065-e86044a10161&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
If comes the day that you'd no longer want to use Supabase anymore (hopefully not!) and want to be removed from our systems entirely, feel free to submit a request to delete your account through the account preferences page.
PR: <https://github.com/supabase/supabase/pull/22486>
Link: [[https://supabase.com/dashboard/account/me](](https://supabase.com/dashboard/account/me%5D\()<https://supabase.com/dashboard/account/me>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[General](https://supabase.com/dashboard/project/_)
  * Added project connection instructions for Vite [[PR](https://github.com/supabase/supabase/pull/22606)]


### [Platform Updates: March 2024 ](https://github.com/orgs/supabase/discussions/22525)
Apr 6, 2024
## Join us for a Special Announcement April 15-19[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#join-us-for-a-special-announcement-april-15-19)
![Special Announcement April 15-19](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmarch2024%2Fsupabase-special-announcement-april-15-19-2024.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’re making a Special Announcement on April 15th with a few more surprises throughout the week. [Claim your ticket](https://supabase.link/velZ07m) today so you don’t miss out and enter for a chance to win a set of AirPods Max.
[Claim your ticket](https://supabase.link/velZ07m)
## Increased Supavisor connection pooler limits[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#increased-supavisor-connection-pooler-limits)
![Increased Supavisor connection pooler limits](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmarch2024%2Fsupavisor-increased-connection-limits.jpg%3Ft%3D2024-04-05T21%253A48%253A02.612Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve increased the Supavisor client connection limits, the number of concurrent clients that can connect to your project’s pooler, for projects on Small, Medium, Large, and XL compute instances while pricing remains unchanged.
[Announcement](https://supabase.link/8z8fX0f)
## Conversational AI assistant now available in SQL Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#conversational-ai-assistant-now-available-in-sql-editor)
![Conversational AI assistant in SQL Editor](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmarch2024%2Fsql-editor-conversational-ai-assistant.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Introducing a conversational AI assistant in the SQL Editor to help you write and iterate on your queries. This is currently under a feature preview and can be enabled with instructions [here](https://supabase.link/Os3jpYP).
[Announcement](https://supabase.link/Os3jpYP)
## Supavisor pooler port 6543 is transaction-mode only[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supavisor-pooler-port-6543-is-transaction-mode-only)
![Supavisor pooler port 6543 is transaction-mode only](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmarch2024%2Fsupavisor-port-6543-transaction-only.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’re simplifying Supavisor connection pooler ports and modes so that port 6543 is only transaction mode and port 5432 continues to be only session mode. If you have pool mode set to session we recommend you switch to pooler port 5432 and set the mode to transaction.
[Pull request](https://supabase.link/ba5H5oU)
## Migration to v2 platform architecture[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#migration-to-v2-platform-architecture)
![v2 platform architecture migration](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmarch2024%2Fsupabase-v2-arch-migration.png%3Ft%3D2024-04-05T22%253A03%253A00.953Z&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You may have noticed improved performance from your database over the last couple of weeks. We made some architectural changes to free up resources for your Postgres instance by removing Storage, Realtime, and Pgbouncer from your instance and each are replaced with an equivalent multi-tenant solution, including our new Supavisor connection pooler.
[Announcement](https://supabase.link/XnxfO42)
## Implementing semantic image search with Amazon Bedrock and Supabase Vector[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#implementing-semantic-image-search-with-amazon-bedrock-and-supabase-vector)
![Semantic image search with Amazon Bedrock and Supabase Vector](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fmarch2024%2Fsemantic-image-search-amazon-bedrock-supabase-vector.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
In this post we'll be creating a Python project to implement semantic image search featuring Amazon Bedrock and Amazon Titan’s multimodal model to embed images and Supabase Vecs client library for managing embeddings in your Supabase database with the pgvector extension.
[Blog post](https://supabase.link/iOSqfPh)
## Quick Product Announcements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#quick-product-announcements)
  * [Postgres Tooling] vector (pgvector) upgraded to v0.6.2 enables faster HNSW index builds using more parallel workers [[Commit](https://supabase.link/5dUCCE7)]
  * [Postgres Tooling] pg_cron upgraded to v1.6.2 enables sub-minute schedules [[Pull request](https://supabase.link/RdeP5J9)]


## Made With Supabase[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#made-with-supabase)
  * location-tRacer - Supabase Realtime live location sharing app [[GitHub](https://supabase.link/bSgEEHP)]
  * Talk to your docs - An example agent providing help on your GitHub documentation [[GitHub](https://supabase.link/biIjh38)]
  * Feedbase - Open-source solution for collecting feedback & communicating updates [[GitHub](https://supabase.link/lCWRfaI)]
  * Wacky Wordcraft - Create wacky stories with some help from AI [[Twitter](https://supabase.link/rvNLNpX)]
  * Capgo - Instant updates for Capacitor apps. Ship updates, fixes, changes, and features within minutes [[Website](https://supabase.link/f3z1RmC)]


## Community Highlights[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#community-highlights)
  * Building an Investor List App with Novu and Supabase [[Blog post](https://supabase.link/dKChOdc)]
  * 3 reasons you should use Postgres Functions and Transactions [[Video](https://supabase.link/PzxbAq7)]
  * Add image support to Flutter web application with Supabase Storage [[Video](https://supabase.link/psNjG7E)]
  * How to set up a secure Supabase project [[Blog post](https://supabase.link/vCkI7Fc)]
  * Dynamic Role and Permission Management in Supabase: Enhancing Security and Flexibility [[Blog post](https://supabase.link/Z17JqH7)]
  * Simulate Supabase Postgres RLS (Row Level Security) [[Blog post](https://supabase.link/ro8pdrf)]
  * Monitor Supabase databases and Edge Functions [[Blog post](https://supabase.link/n1Z3hUo)]

_This discussion was created from the release[Platform Updates: March 2024](https://github.com/supabase/supabase/releases/tag/v0.24.03)._
### [Realtime Broadcast and Presence Authorization ](https://github.com/orgs/supabase/discussions/22484)
Apr 4, 2024
## Update[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#update)
Discussion has been updated with solution chosen.
Realtime Authorization for Broadcast and Presence is now available in Public Beta.
See the [official documentation](https://supabase.com/docs/guides/realtime/authorization).
## Overview[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#overview)
This post explains how authorization works for Realtime Broadcast and Realtime Presence.
This allows you (the developer) to control access to Realtime Channels. We use Postgres Row Level Security to manage access. Developers create Policies which allow or deny access for your users.
## Usage[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#usage)
### Creating Realtime Policies[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#creating-realtime-policies)
Using Studio’s SQL editor you can set RLS rules against the table `realtime.messages` which will define the rules for your users.
`
1
CREATE POLICY "presence sync and broadcast listen to authenticated users"
2
ON realtime.messages FOR SELECT
3
TO authenticated
4
USING ( true );
56
CREATE POLICY "presence track and broadcast send to authenticated users"
7
ON realtime.messages FOR INSERT
8
TO authenticated
9
WITH CHECK ( true );
`
Since you are using RLS policies you can do more complex examples.
In a scenario where you have a schema with a table for rooms and one that creates an association between rooms and users.
![Example schema to be used in RLS policies](https://github.com/supabase/supabase/assets/1697301/93cac144-a35e-42cd-8f92-c890a8c3f8e4)
We'll use this example schema to be showcase RLS policies limiting Realtime functionality
We can build more complex RLS rules using this information:
`
1
-- Set permission for authenticated users to only listen for Broadcast messages
2
CREATE POLICY "authenticated can listen to broadcast only on their topics"
3
ON realtime.messages FOR SELECT
4
TO authenticated
5
USING ( 
6
	exists(
7
   select 1
8
   from public.rooms r join public.rooms_users ru on r.id = ru.room_id
9
   where ru.user_id = auth.uid()
10
    and r.name = realtime.topic()
11
    and realtime.messages.extension = 'broadcast'
12
 )
13
);
14
-- Set permission for authenticated users to only write for Broadcast messages
15
CREATE POLICY "authenticated can write to broadcast only on their topics"
16
ON realtime.messages FOR INSERT
17
TO authenticated
18
WITH CHECK ( 
19
	exists(
20
	 select 1
21
  from public.rooms r join public.rooms_users ru on r.id = ru.room_id
22
  where ru.user_id = auth.uid()
23
   and r.name = realtime.topic()
24
   and realtime.messages.extension = 'broadcast'
25
 )
26
)
`
### Testing Authorization[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#testing-authorization)
Now to test it we can use a quick deno script by creating a `index.ts`
`
1
// Run with deno run --allow-net --allow-env --allow-read --allow-ffi index.ts
2
import { createClient } from "npm:@supabase/supabase-js@2.38.5";
3
const url = "https://<project_ref>.supabase.com";
4
const apikey = "<api_key>";
56
const client = createClient(url, apikey);
78
const channel = client.channel("channel_1", {
9
 config: { broadcast: { self: true }, private: true},
10
});
11
channel
12
 .on("broadcast", { event: "test" }, (payload) => console.log(payload))
13
 .on("presence", { event: "join" }, (payload) => console.log(payload))
14
 .on("presence", { event: "leave" }, (payload) => console.log(payload))
15
 .subscribe((status: string, err: any) => {
16
  if (status === "SUBSCRIBED") {
17
   console.log("Connected!");
18
  } else {
19
   console.error(err);
20
  }
21
 });
`
This will return an error with the message `You do not have permissions to read from this Topic`
But if we change our code to pass along an authenticated user, then we will be able to connect and receive / send messages.
`
1
import { createClient } from "npm:@supabase/supabase-js@2.38.5";
2
const url = "https://<project_ref>.supabase.co";
3
const apikey = "<api_key>";
45
const client = createClient(url, apikey);
67
await client.auth.signInWithPassword({
8
 email: "<email>",
9
 password: "<password>",
10
});
1112
client.realtime.setAuth(
13
 (await client.auth.getSession()).data.session.access_token
14
);
15
const channel = client.channel("channel_1", {
16
 config: { broadcast: { self: true }, private: true },
17
});
18
channel
19
 .on("broadcast", { event: "test" }, (payload) => console.log(payload))
20
 .on("presence", { event: "join" }, (payload) => console.log(payload))
21
 .on("presence", { event: "leave" }, (payload) => console.log(payload))
22
 .subscribe((status: string, err: any) => {
23
  if (status === "SUBSCRIBED") {
24
   console.log("Connected!");
25
  } else {
26
   console.error(err);
27
  }
28
 });
`
Do not forget that RLS policies can use other tables in them so this will give you all the flexibility you need to better fit your use case but be aware of the performance impact of heavy RLS queries or non-indexed fields.
### Migrating from Public Channels[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#migrating-from-public-channels)
On connect, you need to send in the configuration that the channel will be `private: true`
### Client library[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#client-library)
We’re working on the `next` version actively so we can provide a good developer experience.
Please check the latest `next` version at <https://www.npmjs.com/package/@supabase/realtime-js?activeTab=versions>
This library as changed the configuration settings to add `private: true` on channel connect to determine if the user will be connecting an RLS checked channel.
## How it works[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-it-works)
### Connection context[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#connection-context)
When you connect with Realtime we set a connection configuration with your JWT, Topic and Headers using the following query:
`
1
SELECT
2
	set_config('role', $1, true),
3
	set_config('realtime.topic', $2, true),
4
	set_config('request.jwt', $4, true),
5
	set_config('request.jwt.claims', $6, true),
6
	set_config('request.headers', $7, true)
`
This query is only run when you _connect_ to a topic.
We’re also providing a new function to easily fetch the `realtime.topic` configuration with
`
1
SELECT realtime.topic();
23
-- Usage example
4
CREATE POLICY "authenticated users can only write to topic named foo"
5
ON realtime.messages FOR INSERT
6
TO authenticated
7
WITH CHECK ( realtime.topic() = 'foo' );
`
### Applying RLS Policies[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#applying-rls-policies)
To achieve RLS checks on your Realtime connection we created a new table in the `realtime` schema to which you will be able to write RLS rules against it to control your topics extensions.
![87d33215-313f-42c6-b775-f2e8671206e5](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F1697301%2F0c3e3033-6bfb-4053-a947-fc48526af578&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You won’t see any entries recorded in this table as we rollback the changes made to test out RLS policies to avoid creating clutter in your database.
### [Increased Supavisor Client Connection Limits Across Paid Plans ](https://github.com/orgs/supabase/discussions/22457)
Apr 4, 2024
Supavisor, Supabase's multi-tenant connection pooler deployed to regional clusters, became production ready back in December 2023. You can read the announcement [here](https://supabase.com/blog/supavisor-postgres-connection-pooler).
Since then, we've migrated Supabase projects from PgBouncer, single tenant connection pooler deployed to the project's instance, to Supavisor.
However, we kept the previous client connection limits from PgBouncer during the transition across all compute instances.
Today, we're happy to announce that we've increased this limit for compute instances `Small`, `Medium`, `Large`, and `XL` so your projects can take advantage of additional client connections while pricing remains unchanged. These new limits have already been applied to all existing projects and any new projects spun up.
Here's a quick breakdown:
Compute Size| Previous Client Limits| New Client Limits  
---|---|---  
Small| 200| 400  
Medium| 200| 600  
Large| 300| 800  
XL| 700| 1,000  
For a more complete breakdown of your compute instance resources head over to the [Compute Add-ons](https://supabase.com/docs/guides/platform/compute-add-ons) page.
### [Dashboard Weekly Updates [18/03/24 - 25/03/24] ](https://github.com/orgs/supabase/discussions/22222)
Mar 26, 2024
## Update to the UI for RLS policies[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#update-to-the-ui-for-rls-policies)
![image](https://github.com/supabase/supabase/assets/19742402/3484a220-3485-452c-9755-49f4511078b2)
We've been looking into improving the UX for the RLS policy UI after going through feedback of the community's struggles with RLS in general, and this is the next step that we're taking to streamline the UX.
What we're calling as a "hybrid" editor (for now), you'll be able to see the corresponding SQL query for creating or updating your RLS policies while you're editing the policy via the input fields. And if you'd like even greater control, there's always the "Open in SQL Editor" button as an escape hatch where you can edit the SQL query in its entirety.
Templates are now right beside the editor as well, so you no longer have to click back and forth between templates and the editor.
We've always seen the dashboard as more than just a database adminstration tool, but also potentially an educational platform for developers to pick up the SQL language as they build out their database, and we hope that the changes here will help make that even easier.
PR: <https://github.com/supabase/supabase/pull/21806>
Link: <https://supabase.com/dashboard/project/_/auth/policies>
## Connection pooler on port 6543 is set to transaction mode permanently[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#connection-pooler-on-port-6543-is-set-to-transaction-mode-permanently)
![Screenshot 2024-03-25 at 19 28 35](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2Ffee3bef7-411a-4956-a580-0119e3eb3676&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Previously, connection pooler's port 6543 can be set to either transaction or session mode under your project's database settings. This change makes it easier to distinguish between pooler modes and ports by only enabling transaction mode on port 6543 while maintaining session mode on port 5432.
If your using port 6543 and your project's pooler mode is transaction then you won't be able to set the mode to session. You can use port 5432 for session mode.
If your using port 6543 and your project's pooler mode is session then we strongly advise that you use port 5432 for session mode and change the mode to transaction. Once this setting is saved you won't be able to set session mode on port 6543.
PR: <https://github.com/supabase/supabase/pull/22150>
Link: <https://supabase.com/dashboard/project/_/settings/database#connection-pooler>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[[General](https://supabase.com/dashboard/project/_)]
  * Home page connect modal fix broken link under pooler mode to Database Settings [[PR](https://github.com/supabase/supabase/pull/22105)]
  * Fix toast messages to handle really long messages, and support closing them in such scenarios [[PR](https://github.com/supabase/supabase/pull/22122)]


[[Auth](https://supabase.com/dashboard/project/_/auth)]
  * Fix applying table privileges to incorrect table if there any more than 1 table with the same name in different schemas [[PR](https://github.com/supabase/supabase/pull/22121)]


[[Table Editor](https://supabase.com/dashboard/project/_/editor)]
  * Prevent updating RLS via GUI for tables under protected schemas [[PR](https://github.com/supabase/supabase/pull/22119)]
  * Support updating column "is unique" when editing table in side panel [[PR](https://github.com/supabase/supabase/pull/22121)]
  * Fix support NULL values when importing data via CSV text [[PR](https://github.com/supabase/supabase/pull/22146)]
  * Ensure that table and column names are trimmed for whitespaces when saving [[PR](https://github.com/supabase/supabase/pull/22170)]


[[Storage Explorer](https://supabase.com/dashboard/project/_/buckets)]
  * Fix delete bucket modal styling when bucket name is long [[PR](https://github.com/supabase/supabase/pull/22109)]
  * Fix deleting parent folder not deleting child folders despite child folders being empty [[PR](https://github.com/supabase/supabase/pull/22125)]


[[Database Pages](https://supabase.com/dashboard/project/_/database/tables)]
  * Fix inability to manage foreign keys [[PR](https://github.com/supabase/supabase/pull/22104)]
  * Validate enumerated types to ensure names do not conflict with native PG data type names [[PR](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2)]
  * Validate enumerated types to ensure names do not conflict with native PG data type names [[PR](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2)]
  * Fix Stripe foreign data wrapper to support selecting a rowid_column, addresses the issue of not being able to update stripe foreign tables [[PR](https://github.com/supabase/supabase/pull/22127)]


### [Migration to v2 platform architecture ](https://github.com/orgs/supabase/discussions/22135)
Mar 20, 2024
In our previous platform architecture, our [Storage](https://supabase.com/storage), [Realtime](https://supabase.com/realtime), and connection pooler ([PgBouncer](https://www.pgbouncer.org/)) services were bundled together, with a single instance of each service per project.
For our v2 architecture, we’ve “unbundled” these services, moving to a multi-tenant model, where a single instance of each service serves many projects:
![](https://github.com/supabase/supabase/assets/1154867/66d6d8d3-291a-4657-856d-e2dfc75305d6)
This frees up as much resources as possible for your Postgres databases, while enabling us to offer more resource intensive features for these services, and opens the door to capabilities such as zero-downtime scaling.
With Supavisor [replacing PgBouncer](https://github.com/orgs/supabase/discussions/17817), along with some other key optimizations, the final pieces of our v2 architecture are now ready.
## Paid plan rollout (completed)[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#paid-plan-rollout-completed)
We’ve already fully rolled out our v2 architecture to paid plan projects. You now have more resources available, for the same price that you’ve been paying.
## Free plan gradual rollout (20 March 2024 onwards)[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#free-plan-gradual-rollout-20-march-2024-onwards)
  * **20 March 2024:** Newly created or unpaused projects will use v2 architecture
  * **28 March 2024:** Existing projects will start being migrated to v2 architecture


This will be a gradual rollout - we will email you at least one week before your project is scheduled to be migrated.
### Your action for projects scheduled to be migrated[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#your-action-for-projects-scheduled-to-be-migrated)
For newly created or unpaused projects on the Free Plan, no action is required.
For existing projects on the Free Plan, up to a few minutes of downtime is expected for the migration. For each of your projects, we’ll identify the 30-minute maintenance window where your project had the least database queries over the previous 10 weeks.
You have two choices:
  * **Automatic Migration:** If you don't take any action, we plan to do the migration automatically during that maintenance window with the least historical activity.
  * **Manual Migration:** Any time before that, you can go to [Project Settings > General](https://supabase.com/dashboard/project/_/settings/general) to see whether/when the maintenance window is scheduled (timings will also be included in the email). There, you may choose to manually restart the project yourself, at a time that is convenient for you. Your project will be restarted on v2 architecture.


### [Dashboard Weekly Updates [04/03/24 - 11/03/24] ](https://github.com/orgs/supabase/discussions/21974)
Mar 12, 2024
## Conversational AI assistant now available as part of the SQL Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#conversational-ai-assistant-now-available-as-part-of-the-sql-editor)
![Screenshot 2024-03-12 at 23 57 10](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2Fe808cf41-d9d4-4501-847b-7c0ccfcb8cb3&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
As part of our ongoing efforts to introduce the AI assistant across the dashboard, we're bringing the AI assistant to the SQL Editor next! Some of you might have already been using the AI assistant in the SQL Editor through the green bar at the top of the editor - we're sprucing it up by extending it further to a conversational UX. Go back and forth with the assistant and apply the code snippets that you deem to be the most appropriate!
This is currently under a feature preview - you may enable this feature by clicking on the user icon while in a project at the bottom of the side navigation bar and selecting "Feature previews". From there just enable the preview under "SQL Editor Conversational Assistant". And as always, we're incredibly open to any feedback for this, so give us a shout right [here](https://github.com/orgs/supabase/discussions/21967)!
PR: <https://github.com/supabase/supabase/pull/21388>
Link: <https://supabase.com/dashboard/project/_/sql/new>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Fix creating a table will automatically trim for whitespaces ([PR](https://github.com/supabase/supabase/pull/21861))


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Fix snippet names not truncating ([PR](https://github.com/supabase/supabase/pull/21777))


[Auth Policies](https://supabase.com/dashboard/project/_/auth/policies)
  * Fix error message not surfacing in new RLS UI from feature preview ([PR](https://github.com/supabase/supabase/pull/21961))


[Database Functions](https://supabase.com/dashboard/project/_/database/functions)
  * Fix light mode styling for code editor ([PR](https://github.com/supabase/supabase/pull/21820))


### [Platform Updates: February 2024 ](https://github.com/orgs/supabase/discussions/21823)
Mar 6, 2024
## Matryoshka Embeddings: Faster OpenAI Vector Search Using Adaptive Retrieval[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#matryoshka-embeddings-faster-openai-vector-search-using-adaptive-retrieval)
![Matryoshka Embeddings](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Frender%2Fimage%2Fpublic%2Fimages%2Fmarketing-emails%2Ffebruary2024%2Fmatryoshka-embeddings-thumb.png%3Fheight%3D1000%26resize%3Dfill&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Learn about how OpenAI’s newest text embeddings models, text-embedding-3-small and text-embedding-3-large, are able to truncate their dimensions with only a slight loss in accuracy.
[Blog post](https://supabase.com/blog/matryoshka-embeddings)
## Easily Connect to Supabase Projects From Frameworks and ORMs of Your Choice[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#easily-connect-to-supabase-projects-from-frameworks-and-orms-of-your-choice)
![Connect to Supabase Projects From Frameworks and ORMs](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Frender%2Fimage%2Fpublic%2Fimages%2Fmarketing-emails%2Ffebruary2024%2Fconnect-ui-frameworks-orms3.png%3Fheight%3D400%26resize%3Dcontain&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Connect to Supabase from any framework or ORM with our new “Connect” panel in Studio. This displays simple setup snippets that you can copy and paste into your application. We’ve started with a selection of popular frameworks and ORMs and you can request more by [feature request](https://github.com/orgs/supabase/discussions/categories/feature-requests?discussions_q=category%3A%22Feature+Requests%22+) or [pull request](https://github.com/supabase/supabase/pulls).
[Pull request](https://github.com/supabase/supabase/pull/20328)
## PostgREST Aggregate Functions[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#postgrest-aggregate-functions)
![PostgREST Aggregate Functions](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Frender%2Fimage%2Fpublic%2Fimages%2Fmarketing-emails%2Ffebruary2024%2Fpostgrest-v12-aggregate-functions3.png%3Fheight%3D500&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
PostgREST v12 has been released, and with it, comes the release of the highly requested aggregate functions, `avg()`, `count()`, `sum()`, `min()`, and `max()`, that is used to summarize data by performing calculations across groups of rows.
[Blog post](https://supabase.com/blog/postgrest-aggregate-functions)
## Terraform Provider to Manage Resources on Supabase Platform[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#terraform-provider-to-manage-resources-on-supabase-platform)
![Terraform Provider](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Frender%2Fimage%2Fpublic%2Fimages%2Fmarketing-emails%2Ffebruary2024%2Fsupabase-terraform.png%3Fheight%3D400&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve created an official Supabase Provider for Terraform to version-control your project settings in Git. You can use this provider in CI/CD pipelines to automatically provision projects and branches and keep configuration in code.
[Learn more](https://supabase.com/docs/guides/platform/terraform)
## Support for Composite Foreign Keys in Table Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#support-for-composite-foreign-keys-in-table-editor)
![Composite Foreign Keys](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Frender%2Fimage%2Fpublic%2Fimages%2Fmarketing-emails%2Ffebruary2024%2Fcomposite-foreign-keys5.png%3Fresize%3Dcontain&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've shifted the management of foreign keys into the Table Editor’s side panel so you can easily see all foreign keys pertaining to a table as well as referencing columns to composite foreign keys.
[Pull request](https://github.com/supabase/supabase/pull/21078)
## Build a Content Recommendation App With Flutter and OpenAI[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#build-a-content-recommendation-app-with-flutter-and-openai)
![Content Recommendation App With Flutter and OpenAI](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Frender%2Fimage%2Fpublic%2Fimages%2Fmarketing-emails%2Ffebruary2024%2Fsupabase-flutter-openai.webp%3Fheight%3D400&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Learn about how we built a movie listing app that recommends another movie based on the movie that a user is currently viewing built with Supabase, Flutter, and OpenAI.
[Blog post](https://supabase.com/blog/content-recommendation-with-flutter)
## Load Testing Supabase[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#load-testing-supabase)
![Load Testing Supabase](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Frender%2Fimage%2Fpublic%2Fimages%2Fmarketing-emails%2Ffebruary2024%2Fload-testing-supabase.png%3Fheight%3D800&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Performance testing evaluates a system's compliance with its performance requirements. It reveals your app’s ability to handle user load, unexpected spikes, or recover from stressful workloads. In this blog post you will learn about how we automated our performance testing.
[Blog post](https://supabase.com/blog/automating-performance-tests)
## More Studio Updates[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#more-studio-updates)
  * Collapsible main sidebar navigation [[PR](https://github.com/supabase/supabase/pull/21550)]
  * Create charts from SQL Editor [[PR](https://github.com/supabase/supabase/pull/21638)]
  * Resizable main tabs in Table Editor and SQL Editor [[PR](https://github.com/supabase/supabase/pull/21548)]
  * View user metadata from the dashboard [[PR](https://github.com/supabase/supabase/pull/21239)]
  * Bulk delete SQL Editor snippets [[PR](https://github.com/supabase/supabase/pull/20927)]
  * Query Performance updates [[PR](https://github.com/supabase/supabase/pull/20907)]
  * Choose a compute option when creating a project (Paid organizations only) [[PR](https://github.com/supabase/supabase/pull/21292)]
  * Logs Explorer facelift [[PR](https://github.com/supabase/supabase/pull/21055)]


## Quick Product Announcements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#quick-product-announcements)
  * [Auth] Require AAL2 to enroll additional factors for MFA enrollment [[PR](https://github.com/supabase/gotrue/pull/1439)]
  * [Storage] Increased maximum file upload size to 50GB for paid plans [[PR](https://github.com/supabase/supabase/pull/21220)]


## Made With Supabase[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#made-with-supabase)
  * Inkvestigations is a webgame using LLM technology (currently GPT) to create interactive mystery games [[GitHub](https://github.com/bromberry-games/Inkvestigations)]
  * MathPuzzles- a multiplayer game to outsmart your friends [[GitHub](https://github.com/beerose/supabase-realtime-math-game)]
  * Create a recipe app with Nowa [[Article](https://medium.com/@nowa.dev/create-a-recipe-app-with-nowa-supabase-e26c00358325)]
  * Open-source AI wearable device that captures what you say and hear [[GitHub](https://github.com/adamcohenhillel/ADeus)]
  * Brick yourself - turn yourself into a mini-figure [[Website](https://brick-yourself.vercel.app)]


## Community Highlights[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#community-highlights)
  * SupaVlog: Vlog Application Starter Kit Built with Supabase, Stream, Hookdeck, and Next.js [[Article](https://hookdeck.com/blog/supavlog-vlog-start-kit-supabase-stream-hookdeck-nextjs)]
  * Chat with Supabase PostgreSQL using AI [[Article](https://medium.com/@sheldonniu/chat-with-supabase-postgresql-using-ai-3c4d1cf1086a)]
  * How to implement Google sign-in on Flutter with Supabase on iOS, Android and the Web [[Video](https://www.youtube.com/watch?v=utMg6fVmX0U)]
  * They're Making Supabase Better... [[Video](https://www.youtube.com/watch?v=nk4LTSy7XtA)]
  * How to send welcome emails with Supabase edge functions and database triggers [[Article](https://bejamas.io/blog/send-emails-supabase-edge-functions-database-triggers)]
  * How to Create Email Signup and Login Screens in React Native (Expo), ExpressJS, and Supabase [[Article](https://medium.com/@programming-advice/taking-a-step-back-how-to-create-email-signup-and-login-screens-in-react-native-expo-4443569a7aa8)]
  * Integrating Supabase with Flutterflow [[Video](https://www.youtube.com/watch?v=fqq69JCN4CY)]
  * Join the [#SupaBuilders movement](https://twitter.com/thorwebdev/status/1760918914702430665) and never get your project paused again!

_This discussion was created from the release[Platform Updates: February 2024](https://github.com/supabase/supabase/releases/tag/v0.24.02)._
### [Dashboard Weekly Updates [26/02/24 - 04/03/24] ](https://github.com/orgs/supabase/discussions/21732)
Mar 4, 2024
## Templates added to new RLS assistant[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#templates-added-to-new-rls-assistant)
![](https://github.com/supabase/supabase/assets/19742402/28d51a21-d90c-4657-8078-b43133a30070)
If you're not aware yet, we previously created a new RLS UI that comes integrated with the Supabase Assistant to (hopefully) help everyone write RLS policies easier and faster. This is currently still a feature preview which you can enable by clicking on your user profile at the bottom of the side navigation bar. We're continuously trying to see how we can improve this to make it a much better UX than the current existing RLS policy user flow.
The first gap that we're trying to address is the ease of referencing existing templates that just work out of the box from the current RLS policy flow - those proved to be really useful when trying to understand the syntax of writing policies, and so we added that in to the new RLS UI. Not just that but we also added more complex templates that work better in the new UI than the current one!
The next item that we're looking into is to see what minimal guard rails we can add to make writing RLS policies even less intimidating since the new UI expects only SQL input. One of the aims of the dashboard is to guide our users to not be afraid of SQL no matter the level of proficiency and we hope that we'll be able to cook up the ideal UX that will allow everyone to write SQL with confidence.
PR: <https://github.com/supabase/supabase/pull/21447>
Link: <https://supabase.com/dashboard/project/_/auth/policies>
## Collapsible navigation bar[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#collapsible-navigation-bar)
<https://github.com/supabase/supabase/assets/8291514/070cb030-d249-404d-82cd-3ba92d9309f3>
We received many feedback that the icons alone in the navigation bar are not too intuitive in understanding what page they're navigating too. So finally, we're adding some textual cues that show up on hover to the navigation bar in hopes to make navigating around the dashboard easier!
PR: <https://github.com/supabase/supabase/pull/21550>
Link: <https://supabase.com/dashboard/project/_>
## Make charts in the SQL editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#make-charts-in-the-sql-editor)
![](https://github.com/supabase/supabase/assets/37541088/8a5e6767-d001-4d7a-b2ea-07e1cdd3b13c)
For the users who leverage on SQL to analyze data, this should be useful for you! You can now plot your data points through the SQL editor after running your query. Choose which columns to be your axes and you're good to go. As always - feel free to drop any feedback for us on this! We're keen to see how else we can make this feature better and stronger 😄
PR: <https://github.com/supabase/supabase/pull/21638>
Link: <https://supabase.com/dashboard/project/_/sql/new>
## Foreign Key Management re-introduced into the Column side panel editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#foreign-key-management-re-introduced-into-the-column-side-panel-editor)
![Screenshot 2024-03-04 at 17 59 15](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2F8c75d58b-cbda-44ab-b825-3dc0569e0847&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We previously made an update in the Table Editor to shift the management of foreign keys to the table editor as an effort to properly support composite foreign keys. This understandably caused the UX to suffer as we received many feedback around creating simple 1:1 foreign key relations much more troublesome. We've thus re-introduced being able to manage your foreign keys while editing a column! Thank you so much for everyone's feedback around this - it's something that we genuinely appreciate our community for! 🙏
PR: <https://github.com/supabase/supabase/pull/21683>
Link: <https://supabase.com/dashboard/project/_/editor>
## Toggle intellisense for the SQL editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#toggle-intellisense-for-the-sql-editor)
![Screenshot 2024-03-04 at 17 51 13](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2F6a95e870-e77a-4031-b553-66fd6789aebe&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Intellisense for the SQL editor was always enabled by default for everyone, but we're now making this a toggleable feature - this is more specifically useful for large projects with many tables as we've noticed the amount of data we try to load into intellisense causes the SQL editor to slow down noticeable (likely due to browser memory issues).
PR: <https://github.com/supabase/supabase/pull/21643>
Link: <https://supabase.com/dashboard/project/_/sql/new>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[Schema Visualizer](https://supabase.com/dashboard/project/_/database/schemas)
  * Added legends to the schema visualizer and align icons properly [[PR](https://github.com/supabase/supabase/pull/21575)]


### [Dashboard Weekly Updates [19/02/24 - 26/02/24] ](https://github.com/orgs/supabase/discussions/21563)
Feb 26, 2024
## Paid organizations can now launch projects on bigger compute immediately[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#paid-organizations-can-now-launch-projects-on-bigger-compute-immediately)
![Screenshot 2024-02-26 at 22 01 03](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2Fafbd2c94-828f-46c1-ae69-1c4d8c695ae9&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Paid plan users can now immediately launch projects on larger compute sizes. Previously, paid organizations had to launch projects on the default "Micro" instance and then separately upgrade their instance. You can always up and downgrade your instance in hindsight. Feel free to leave any feedback in our discussions [here](https://github.com/orgs/supabase/discussions/21386)!
PR: <https://github.com/supabase/supabase/pull/21292>
Link: <https://supabase.com/dashboard/new/_>
## Update on Table Editor search input[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#update-on-table-editor-search-input)
![Screenshot 2024-02-23 at 7 59 21 PM](https://github.com/supabase/supabase/assets/8291514/5e1bd973-bcc0-439f-b96f-5d49df37f44f)
As mentioned in last week's changelog (and also as always 😉) we see everyone's feedback regarding the changes to the table editor search input and have enacted a slight change to make the search action more prominent and easier to click on! Again, thank you to everyone for sounding your thoughts, we genuinely appreciate them as it helps us guide the dashboard's DX to be optimal - keep em coming!
Separetely - we're also aware of the feedback regarding our change in the way you manage your foreign keys as announced in the [changelog discussion](https://github.com/orgs/supabase/discussions/21219) 2 weeks ago - fret not! We're actively looking into that as well 🙂
PR: <https://github.com/supabase/supabase/pull/21486>
Link: <https://supabase.com/dashboard/project/_/editor>
## Resizeable inner sidebars for Table Editor and SQL Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#resizeable-inner-sidebars-for-table-editor-and-sql-editor)
<https://github.com/supabase/supabase/assets/8291514/1f3d04ef-df86-4398-b7b3-42a9effe950d>
For those who might have tables or SQL queries with long names, this should help alleviate some issues with the names truncating. Hopefully it'll be easier to find your tables / SQL queries! 😊
PR: <https://github.com/supabase/supabase/pull/21548>
Link: <https://supabase.com/dashboard/project/_/editor>
## Connecting to your project - added Expo React Native guides[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#connecting-to-your-project---added-expo-react-native-guides)
Last week we [announced](https://github.com/orgs/supabase/discussions/21366) a quicker way to get your project's connection parameters on the project's home page and we're heartened to already see some community contributions to add more content for different frameworks! Shoutout to @Hallidayo for the help on this - we're always keeping an eye out for more of such contributions 😄
PR: <https://github.com/supabase/supabase/pull/21350>
Link: <https://supabase.com/dashboard/project/_>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[Home](https://supabase.com/dashboard/projects)
  * Sort projects alphabetically and add search functionality for projects ([PR](https://github.com/supabase/supabase/pull/21392))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Fix missing role impersonation functionality when opening a view ([PR](https://github.com/supabase/supabase/pull/21401))
  * Fix a11y on table menu items ([PR](https://github.com/supabase/supabase/pull/21482))
  * Fix inability to update primary key of a table after renaming the table ([PR](https://github.com/supabase/supabase/pull/21285))


[SQL Editor](https://supabase.com/dashboard/project/_/sql)
  * Fix error highlighting wrong line if running a selected portion of the query ([PR](https://github.com/supabase/supabase/pull/21288))


### [Paid organizations can now launch projects on bigger compute immediately ](https://github.com/orgs/supabase/discussions/21386)
Feb 20, 2024
Paid plan users can now immediately launch projects on larger compute sizes. Previously, paid organizations had to launch projects on the default "Micro" instance and then separately upgrade their instance. You can always up- and downgrade your instance in hindsight.
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F14073399%2Fd61d7a58-8b8e-4d9c-93e8-cd005d695cfe&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F14073399%2F07a26ec0-2b89-45cf-8179-3eb00e45d305&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### [Dashboard Weekly Updates [12/02/24 - 19/02/24] ](https://github.com/orgs/supabase/discussions/21366)
Feb 19, 2024
## A quicker way to get your project's connection parameters[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#a-quicker-way-to-get-your-projects-connection-parameters)
![Screenshot 2024-02-19 at 19 20 39](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsupabase%2Fsupabase%2Fassets%2F19742402%2Ffcbc6de7-299d-4187-86d7-6d1fe220c9c9&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We've made retrieving your project's connection parameters more easily accessible by adding a "Connect" button to each projects' homepage. This will show you some quick instructions on how to either connect to your database directly, or connect to your project via some app frameworks and ORMs. Hopefully this will help both new and familiar developers on Supabase to get to building quicker without having to jump around the dashboard to find these information.
PR: <https://github.com/supabase/supabase/pull/20328>
Link: <https://supabase.com/dashboard/project/_>
## Table Editor side menu revamp[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#table-editor-side-menu-revamp)
![screenshot-2023-12-22-at-13 06 32](https://github.com/supabase/supabase/assets/105593/04678fb0-00bb-4ff0-8189-b77caccf84da)
We're in the midst of revising the UX around the table editor to ensure that controls aren't sprawled across the page despite us building more and more features - and this is just the first step of more to come. Icons for tables and views have been tweaked to be more minimal, each table has an indicator to whether RLS has been enabled or not, and the search bar has been made a tad sleeker. As an assurance, we definitely hear everyone's feedback about the changes here in particular with the search bar being less visible and are actively looking to improve the experience here! 🙏
PR: <https://github.com/supabase/supabase/pull/19977>
Link: <https://supabase.com/dashboard/project/_/editor>
## Table Editor header simplification[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#table-editor-header-simplification)
Similar to the above, we've updated the layout a little for the Table Editor itself, briefly the changes include
  * Support for enabling RLS from the Table Editor
  * Showing an indication of how many policies the table has
  * Shifting refresh + data/definition toggle to the footer of the grid


All these are tiny steps to allowing us to build more functionality into the Table Editor without turning it into a control panel!
PR: <https://github.com/supabase/supabase/pull/18366>
Link: <https://supabase.com/dashboard/project/_/editor>
## View auth user details[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#view-auth-user-details)
![](https://github.com/supabase/supabase/assets/105593/9dbf06b1-43e6-4858-9cbb-3a91ff5f461d)
We've had some feedback from users that they'd want a convenient way to check on their project's users from the UI rather than having to go through the Table Editor or SQL Editor to query the `auth.users` table, and so we've gone ahead to ship this one.
PR: <https://github.com/supabase/supabase/pull/21239>
Link: <https://supabase.com/dashboard/project/_/auth/users>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Fix definition view showing empty result if formatting the definition throws an error ([PR](https://github.com/supabase/supabase/pull/21255))


[SQL Editor](https://supabase.com/dashboard/project/_/sql)
  * Refocus to code editor after closing destructive query warning modal ([PR](https://github.com/supabase/supabase/pull/20759))


[Authentication](https://supabase.com/dashboard/project/_/auth/policies)
  * Fix policies under tables from "protected" schemas not showing RLS disabled/enabled state ([PR](https://github.com/supabase/supabase/pull/21217)) 
    * Also show "protected" schemas notice when viewing policies of tables under those schemas
  * Clicking "Toggle feature preview" from the new RLS creation UI will show a confirmation dialog if changes were made before closing the panel ([PR](https://github.com/supabase/supabase/pull/21251))


[Storage](https://supabase.com/dashboard/project/_/storage/buckets)
  * Renaming a file will just highlight the name of the file without the extension, similar to MacOS ([PR](https://github.com/supabase/supabase/pull/21231))


### [Dashboard Weekly Updates [05/02/24 - 12/02/24] ](https://github.com/orgs/supabase/discussions/21219)
Feb 13, 2024
## SQL editor bulk deletes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#sql-editor-bulk-deletes)
<https://github.com/supabase/supabase/assets/19742402/f50eabbf-9c30-4828-8f5f-0efeef67a025>
We hear you! This has been a very popular request by everyone and we're happy to make the first step to improving the UX around your SQL snippets. You can now delete your queries in bulk - gone are the days of rows full with Untitled queries 😄 Fret not, we're also aware that everyone is also requesting for better organization of snippets (specifically folders) - we're actively figuring out how best to bring that UX into the dashboard for everyone so be sure to watch this space 😉
PR: <https://github.com/supabase/supabase/pull/20927>
Link: <https://supabase.com/dashboard/project/_/sql/new>
## Query performance updates[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#query-performance-updates)
![](https://github.com/supabase/supabase/assets/37541088/4d13c4bb-a747-4790-b969-9fb162fabc9a)
Unoptimized queries are a major cause of poor database performance - which is why the query performance report was initially built. We're equipping this page with better tooling, allowing users to:
  1. Search by query or role
  2. Sort results by latency
  3. Expand results to view the full query that was run


As always, if there's anything more we can do for you, feel free to give us a shout in the feedback widget up top 🙂
PR: <https://github.com/supabase/supabase/pull/20907>
Link: <https://supabase.com/dashboard/project/_/reports/query-performance>
## Logs Explorer face lift[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#logs-explorer-face-lift)
![](https://github.com/supabase/supabase/assets/37541088/2b92056f-1278-4132-8688-2bd52898177b)
In an effort to make our UI more consistent + coherent across all products, we've revamped the Logs Explorer to look just like the SQL Editor in hopes that there's less UI for users to learn, and users can just stay focused on doing what they want to do.
PR: <https://github.com/supabase/supabase/pull/21055>
Link: <https://supabase.com/dashboard/project/_/logs/explorer>
## Support for composite foreign keys in table editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#support-for-composite-foreign-keys-in-table-editor)
![](https://github.com/supabase/supabase/assets/19742402/12f8efb0-8190-4680-82d7-0f19c3c8d7b2)
The previous UI for managing foreign keys in the table editor had functional limitations as it assumed single column relations for foreign keys (overly simplified). We've thus shifted the management of foreign keys into the table side panel editor instead. You can manage all foreign keys across all columns on the table in one place, rather than going into each column individually to do so.
PR: <https://github.com/supabase/supabase/pull/21078>
Link: <https://supabase.com/dashboard/project/_/editor>
## Other improvements and bug fixes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-improvements-and-bug-fixes)
### Table Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#table-editor)
  * Fixed duplicating a table not saving it's description ([PR](https://github.com/supabase/supabase/pull/21215))
  * Fixed viewing a reference row in the table editor from the grid not updating the selected schema if referenced row is in another schema ([PR](https://github.com/supabase/supabase/pull/21212))
  * Fixed errors from adding data via spreadsheet/CSV text not surfacing as toasts ([PR](https://github.com/supabase/supabase/pull/21137))


### SQL Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#sql-editor)
  * Fixed long errors getting cut off / not horizontally scrollable ([PR](https://github.com/supabase/supabase/pull/21213))
  * Fixed deleting a query that's not saved throws an error ([PR](https://github.com/supabase/supabase/pull/21082))


### Logs Explorer[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#logs-explorer)
  * Inserting a source will insert the value after the `FROM` command ([PR](https://github.com/supabase/supabase/pull/21114))


### Database[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#database)
  * Fixed enumerated types side panel input fields not resetting after saving ([PR](https://github.com/supabase/supabase/pull/21107))
  * Fixed roles side panel input fields not resetting after saving ([PR](https://github.com/supabase/supabase/pull/20840))


### Misc[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#misc)
  * Support page is now mobile responsive ([PR](https://github.com/supabase/supabase/pull/20999))


### [Platform Updates: January 2024 ](https://github.com/orgs/supabase/discussions/21042)
Feb 6, 2024
## Supavisor replaces PgBouncer for database connection pooling[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supavisor-replaces-pgbouncer-for-database-connection-pooling)
![Supavisor](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjanuary2024%2Fsupavisor-banner.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’re deprecating PgBouncer and migrating all projects to our Supavisor connection pooler. Go grab the pooler connection string in your project’s [Database Settings](https://supabase.com/dashboard/project/_/settings/database).
[Learn more](https://github.com/orgs/supabase/discussions/17817)
## Direct database connection resolve only to IPv6[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#direct-database-connection-resolve-only-to-ipv6)
![IPv4 to IPv6 Transition](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjanuary2024%2Fipv6-banner.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[ACTION REQUIRED] AWS is deprecating IPv4, so we’ve migrating your project to IPv6. If your network supports IPv6 and/or you’re using PostgREST then you don’t need to make any changes. Otherwise, you need to update any connections to Supavisor’s connection pooler. We’ve also made IPv4 addresses available to purchase (passing on the cost from AWS).
[Learn more](https://github.com/orgs/supabase/discussions/17817)
## Supabase Studio's latest enhancements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supabase-studios-latest-enhancements)
![Studio - 7 Updates](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjanuary2024%2Fstudio-updates-7.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Improved text editing in Table Editor, with Markdown previews[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#improved-text-editing-in-table-editor-with-markdown-previews)
![Studio Improved Text Editing With Markdown Previews](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjanuary2024%2Fimproved-text-editing-markdown-previews.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve made it much better for you to edit text in the Table Editor, including Markdown previews so you can preview your changes with ease. [[PR]](https://github.com/supabase/supabase/pull/20727)
### Preview HTML email templates right from the dashboard[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#preview-html-email-templates-right-from-the-dashboard)
![Studio HTML email templates](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjanuary2024%2Fhtml-email-template-preview.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve added the ability to preview your HTML email templates right from the dashboard. [[PR]](https://github.com/supabase/supabase/pull/20681)
### Preview SQL snippets for better discoverability[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#preview-sql-snippets-for-better-discoverability)
![Studio SQL Editor query previews](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjanuary2024%2Fquery-preview-sql-editor.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve added previews to your saved query snippets so you can find the one you’re looking for much faster. [[PR]](https://github.com/supabase/supabase/pull/20694)
### More Studio updates[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#more-studio-updates)
  * [Network Restrictions support IPv6 addresses](https://github.com/supabase/supabase/pull/20548)
  * [Improved database settings](https://github.com/supabase/supabase/pull/20575)
  * [New Notification Center with resource exhaustion notifications](https://github.com/supabase/supabase/pull/19162)
  * [More detailed billing breakdown](https://github.com/supabase/supabase/pull/20498)


## Quick product announcements[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#quick-product-announcements)
  * [AI] Added a guide on how to integrate Amazon Bedrock SDK with Supabase Vecs, our vector client for Postgres. [[Guide]](https://supabase.github.io/vecs/0.4/integrations_amazon_bedrock)
  * [Auth] Improved guide on implementing Server-Side Auth for Next.js. [[Guide]](https://supabase.com/docs/guides/auth/server-side/nextjs)
  * [Auth] Fixed the cookie chunking issue in `@supabase/ssr` - shout out to [SyntheticGoop](https://github.com/SyntheticGoop) from Mobbin. [[PR]](https://github.com/supabase/auth-helpers/pull/726)
  * [Auth] Fixed a bug in using a custom cookie name in `@supabase/ssr`. [[PR]](https://github.com/supabase/auth-helpers/pull/730)
  * [Edge Functions] Created a guide on custom routing. [[Guide]](https://supabase.com/docs/guides/functions/routing)
  * [Edge Functions] Created a guide on how to deploy via CI/CD pipelines on GitHub, GitLab, and Bitbucket. [[Guide]](https://supabase.com/docs/guides/functions/cicd-workflow)
  * [Edge Functions] Edge Runtime now supports Deno 1.39.2. [[Learn more]](https://deno.com/blog/v1.39)
  * [Edge Functions] Updated quickstart guide. [[Video]](https://www.youtube.com/watch?v=5OWH9c4u68M)


## Blog Central[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#blog-central)
### How pg_graphql Works[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#how-pg_graphql-works)
![How pg_graphql Works](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjanuary2024%2Fpggraphql-thumb.webp&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Learn about how we built the GraphQL Postgres extension, written in the Rust programming language, that powers our GraphQL data API.
[Learn more](https://supabase.com/blog/how-pg-graphql-works)
### Getting started with Ruby on Rails and Postgres on Supabase[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#getting-started-with-ruby-on-rails-and-postgres-on-supabase)
![Ruby on Rails and Postgres on Supabase](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjanuary2024%2Frails.webp&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Learn about how you can spin up a Rails app, integrate a Supabase database, and deploy it to Fly.io.
[Learn more](https://supabase.com/blog/ruby-on-rails-postgres)
### Other awesome blog posts[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#other-awesome-blog-posts)
  * [Brace yourself, IPv6 is coming](https://supabase.com/blog/ipv6)
  * [pgvector 0.6.0: 30x faster with parallel index builds](https://supabase.com/blog/pgvector-fast-builds)
  * [What is SAML? A practical guide to the authentication protocol](https://supabase.com/blog/what-is-saml-authentication)
  * [NoSQL Postgres: Add MongoDB compatibility to your Supabase projects with FerretDB](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio)
  * [Elixir clustering using Postgres](https://supabase.com/blog/elixir-clustering-using-postgres)
  * [Using React Query with Next.js App Router and Supabase Cache Helpers](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers)
  * [Create a Figma Clone app with Flutter and Supabase Realtime](https://supabase.com/blog/flutter-figma-clone)
  * [Getting started with Laravel and Postgres](https://supabase.com/blog/laravel-postgres)


### [March Beta 2021 ](https://github.com/supabase/supabase/releases/tag/0.21.03)
Apr 6, 2021
Launch week, Storage, Supabase CLI, Connection Pooling, Supabase UI, and Pricing. Here's what we released last month.
This is also available as a [blog post](https://supabase.io/blog/2021/04/06/supabase-beta-march-2021) and a [video demo](https://youtu.be/TtLxxaYE1rA).
## Supabase Storage[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supabase-storage)
Need to store images, audio, and video clips? Well now you can do it on [Supabase Storage](https://supabase.io/blog/2021/03/30/supabase-storage). It's backed by S3 and our new [OSS storage API](https://github.com/supabase/storage-api) written in Fastify and Typescript. Read the [full blog post](https://supabase.io/blog/2021/03/30/supabase-storage).
![ph-1](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F113680011-ff098c80-96f2-11eb-8cba-e19630ca02aa.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Connection Pooling[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#connection-pooling)
The Supabase API already handles Connection Pooling, but if you're connecting to your database directly (for example, with Prisma) we now [bundle PgBouncer](https://supabase.io/blog/2021/04/02/supabase-pgbouncer). Read the [full blog post](https://supabase.io/blog/2021/04/02/supabase-pgbouncer).
![pgbouncer-thumb](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F113680055-09c42180-96f3-11eb-93e4-3869a40d4b91.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## React UI Component Library[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#react-ui-component-library)
We open sourced our internal UI component library, so that anyone can use and contribute to the Supabase aesthetic. It lives at [ui.supabase.io](https://ui.supabase.io/) . It was also the #1 Product of the Day [on Product Hunt](https://www.producthunt.com/posts/supabase-ui).
![supabase-ui](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F113680095-16e11080-96f3-11eb-960a-b569e034e444.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## CLI[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#cli)
Now you can run Supabase locally in the terminal with `supabase start`. We have done some preliminary work on [diff-based schema migrations](https://supabase.io/blog/2021/03/31/supabase-cli#migrations), and added some new tooling for self-hosting Supabase with Docker. [Blog post here](https://supabase.io/new/blog/2021/03/31/supabase-cli).
![supabase-cli](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F113680121-1cd6f180-96f3-11eb-8aa4-930347d83eb0.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## OAuth Scopes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#oauth-scopes)
Thanks to a comunity contribution ([@_mateomorris](https://twitter.com/_mateomorris) and [@Beamanator](https://twitter.com/Beamanator)), Supabase Auth now includes OAuth scopes. These allow you to request elevated access during login. For example, you may want to request access to a list of Repositories when users log in with GitHub. Check out the [Documentation](https://supabase.io/docs/reference/javascript/auth-signup#sign-up-with-scopes).
![oauth-scopes](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F113680272-3ed07400-96f3-11eb-8703-09b47d849b4b.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Kaizen[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#kaizen)
  * You can now manage your PostgREST configuration inside the Dashboard.
  * Our website has been redesigned. Check out our new [Homepage](https://supabase.io/) and [Blog](https://supabase.io/blog), and our new [Database](https://supabase.io/database), [Auth](https://supabase.io/auth), and [Storage](https://supabase.io/storage) product pages.
  * We refactored some of our Filter methods to make them even easier to use. Check out the [Full Text Search](https://supabase.io/docs/reference/javascript/textsearch) refactor.
  * We have added several new sections to our Docs including: [Local Dev](https://supabase.io/docs/guides/local-development), [Self Hosting](https://supabase.io/docs/guides/self-hosting), and [Postgres Reference](https://supabase.io/docs/reference/postgres/getting-started) docs (all still under development).


### [February Beta 2021 ](https://github.com/supabase/supabase/releases/tag/v0.21.02)
Mar 1, 2021
Supabase is an open source Firebase alternative. We've now been building for one year. Here's what we released last month.
This is also available as a [blog post](https://supabase.io/blog/2021/03/02/supabase-beta-february-2021) and a [video demo](https://youtu.be/h-ses99G45g).
### Dashboard Sidebars[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#dashboard-sidebars)
We've improved the UX of our Dashboard with sidebars in every section, including the Table view, the Auth section, and the SQL Editor.
![Our dashboard has sidebars](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F109592536-5fcd0480-7b4a-11eb-9251-3f56b58660ca.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### SQL Autocomplete[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#sql-autocomplete)
Writing SQL just got 10x easier. We added autocomplete to the SQL editor, including table & column suggestions.
![autocomplete](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F109593221-87709c80-7b4b-11eb-8dc3-65c94cc64787.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Auth Redirects[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#auth-redirects)
Redirect your users to specific route within your site on [`signIn()`](https://supabase.io/docs/client/auth-signin#sign-in-with-redirect) and [`signUp()`](https://supabase.io/docs/client/auth-signup#sign-up-with-redirect).
![Redirect your users after sign up](https://user-images.githubusercontent.com/10214025/109592772-c8b47c80-7b4a-11eb-81cb-2b241293923a.png)
### Learning Resources[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#learning-resources)
We've released a new [Resources](https://supabase.io/docs/resources) section in our docs, as well as two new Auth modules: [GoTrue Overview](https://supabase.io/docs/learn/auth-deep-dive/auth-gotrue) and [Google OAuth](https://supabase.io/docs/learn/auth-deep-dive/auth-google-oauth).
![Our dashboard has sidebars](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F109592814-dc5fe300-7b4a-11eb-8fbf-c6d5782991f8.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### New Region[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#new-region)
Launch your database in South Africa.
![Launch your database in South Africa](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F109592834-e7b30e80-7b4a-11eb-96d5-fbafdb023528.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Kaizen[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#kaizen)
  * We filled up our [Examples](https://supabase.io/docs/guides/examples) page with a lot of new content.
  * We released a [Docker Compose](https://github.com/supabase/supabase/blob/master/docker/docker-compose.yml) file for running Supabase locally. This will be used in our upcoming CLI.
  * We have a couple of pending RFCs which you may want to participate in: 
    * [Planning our CLI and Local Development](https://github.com/supabase/cli/pull/2)
    * [Connection Pooling on Supabase](https://github.com/supabase/postgres/blob/rfc/connection_pooling/rfcs/0001-connection-pooling.md)


### [January Beta 2021 ](https://github.com/supabase/supabase/releases/tag/v0.21.01)
Feb 2, 2021
New year, new features. We've been busy at Supabase during January and our community has been even busier. Here's a few things you'll find interesting.
This is also available as a [blog post](https://supabase.io/blog/2021/03/02/supabase-beta-february-2021) and a [video demo](https://www.youtube.com/watch?v=DlybOLANG4s).
## Count functionality[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#count-functionality)
Anyone who has worked with Firebase long enough has become frustrated over the [lack](https://stackoverflow.com/questions/49979714/how-to-get-count-of-documents-in-a-collection) of `count` functionality. This isn't a problem with PostgreSQL! Our libraries now have support for PostgREST's [exact](https://postgrest.org/en/v7.0.0/api.html?highlight=count#exact-count), [planned](https://postgrest.org/en/v7.0.0/api.html?highlight=count#planned-count), and [estimated](https://postgrest.org/en/v7.0.0/api.html?highlight=count#estimated-count) counts. A massive thanks to [@dshukertjr](https://github.com/supabase/postgrest-js/issues/94#event-4210564301) for this adding support to our client library.
![Supabase now supports count functionality](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F106548150-78e19600-6549-11eb-8956-e3151677098c.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## New Auth Providers[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#new-auth-providers)
We enabled 2 new Auth providers - Facebook and Azure. Thanks to [@Levet](https://github.com/supabase/gotrue/pull/54) for the Azure plugin, and once again to [Netlify's amazing work](https://github.com/netlify/gotrue/issues/107) with GoTrue to implement Facebook.
![Supabase now supports Azure and Facebook Oauth providers](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F106548272-a7f80780-6549-11eb-98c7-930d105351ea.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Auth Audit Trail[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#auth-audit-trail)
We have exposed the audit trail directly in the dashboard, as well as the GoTrue logs. Great for security and debugging.
![Supabase exposes the Auth Audit trail on the dashboard](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F106548291-afb7ac00-6549-11eb-823a-74ec8b539aac.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Auth UI widget[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#auth-ui-widget)
In case our Auth endpoints aren't easy enough already, we've built a React [Auth Widget](http://ui.supabase.com/?path=/story/auth-auth--default) for you to drop into your app and to get up-and-running in minutes.
![Supabase has released a React Auth widget](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F106548318-bf36f500-6549-11eb-8286-487ec177b91a.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## New `auth.email()` function[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#new-authemail-function)
We added a helper function for extracting the logged in user's email address.
![Supabase added an email function for using with Policies](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F106548346-ceb63e00-6549-11eb-89a1-ff134b6bd243.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## New Regions[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#new-regions)
Launch your database in London or Sydney!
![Launch your database in London or Sydney](https://user-images.githubusercontent.com/10214025/106548384-d970d300-6549-11eb-8e12-a66b68033bf5.png)
## Copy rows as Markdown[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#copy-rows-as-markdown)
You can now copy SQL results as Markdown - super useful for adding to blogs and issues.
![Copy query results as markdown](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F106548425-eb527600-6549-11eb-8227-513c18bfa4a1.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## React server components[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#react-server-components)
If you're excited by React Server components then check out the Supabase + Server Components experimental repo. <https://github.com/supabase/next-server-components>
![Use supabase with React Server components](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F106548523-1ccb4180-654a-11eb-9149-c27b3d085909.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Learn[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#learn)
We know that Auth can be a bit daunting when you're just starting out, so we have created some intro videos to get you up to speed in no time:
  * [Supabase Auth Deep Dive Part 1: JWTs](https://youtu.be/v3Exg5YpJvE)
  * [Supabase Auth Deep Dive Part 2: Restrict Table Access](https://youtu.be/qY_iQ10IUhs)
  * [Supabase Auth Deep Dive Part 3: User Based Access Policies](https://youtu.be/0LvCOlELs5U)


## Kaizen[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#kaizen)
  * Performance: We migrated all of our subdomains to Route53, implementing custom Let's Encrypt certs for your APIs. As a result, our read benchmarks are measuring up 12% faster.
  * Performance: We upgrade your databases to the new [GP3](https://aws.amazon.com/about-aws/whats-new/2020/12/introducing-new-amazon-ebs-general-purpose-volumes-gp3/) storage for faster and more consistent throughput.


### [December Beta 2020 ](https://github.com/supabase/supabase/releases/tag/v0.0.12)
Jan 3, 2021
After 10 hectic months of building, Supabase is now in Beta.
This is also available as a [blog post](https://supabase.io/blog/2021/01/02/supabase-beta-december-2020) and a [video demo](https://youtu.be/ofSm4BJkZ1g).
### Supabase is now in Beta[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supabase-is-now-in-beta)
We spent months working on Performance, Security, and Reliability. Read more on our [Beta Page](https://supabase.io/beta).
![This image shows our Beta Page](https://user-images.githubusercontent.com/10214025/103484765-464e5b80-4e2c-11eb-89c6-8e88fe8105e1.png)
### Improve your docs inline[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#improve-your-docs-inline)
Add comments and descriptions to your Tables directly from our auto-generated docs.
![update-docs](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F103484975-df31a680-4e2d-11eb-8569-f8248a02b880.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Table View now has realtime changes[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#table-view-now-has-realtime-changes)
Any updates that happen to your database are reflected in the Table View immediately.
![realtime-updates](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F103484944-8eba4900-4e2d-11eb-867b-c56cfcd207ef.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Table Pagination[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#table-pagination)
Our table view now has pagination - better for working with large data sets.
![table-pagination](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F103484937-7d713c80-4e2d-11eb-9ddc-a0c2e871b864.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Supabase raised a Seed Round[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supabase-raised-a-seed-round)
We raised $6M from Y Combinator, Mozilla, and Coatue. You can read more on [TechCrunch](https://techcrunch.com/2020/12/15/supabase-raises-6m-for-its-open-source-firebase-alternative).
### Kaizen[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#kaizen)
  * Supabase is now 26% faster in regions which support Graviton (1460 reqs/s up from 1167 reqs/s)
  * We launched a new region in Sao Paulo.
  * Postgres Array Support. You can now edit Native Postgres array items in the grid editor or the side panel.
  * We added better support for your custom Database Types.
  * Fixed some buggy keyboard commands. We're continuously improving key commands in the Table editor.


### [Alpha November 2020 ](https://github.com/supabase/supabase/releases/tag/v0.0.11)
Dec 1, 2020
We've been building for 9 months now, are we're getting even closer to Beta.
This is also available as a [blog post](https://supabase.io/blog/2020/12/01/supabase-alpha-november-2020) and a [video demo](https://youtu.be/unC_de7iytA).
### Add users[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#add-users)
You can now add users manually from your dashboard.
![This image shows how to invite a new user directly from the dashboard.](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F100694951-1e9e4a80-33cb-11eb-9db6-7ae6ae6c252c.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### User admin[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#user-admin)
You can also perform admin functions on existing users - send password reset emails, magic links, and delete users.
![This image shows how to delete a user directly from the dashboard](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F100694970-2a8a0c80-33cb-11eb-8fbf-cfa1d90dca06.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Even more powerful SQL Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#even-more-powerful-sql-editor)
Last month we [announced](https://supabase.com/blog/supabase-alpha-october-2020) an improved SQL Editor, and this month we've taken it even further. The SQL Editor is now a full Monaco editor, like you'd find in VS Code. Build your database directly from the browser.
![This image shows our improved SQL Editor](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F100695002-3b3a8280-33cb-11eb-962a-818f62f7b0ae.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Status page[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#status-page)
We added a [Status Page](https://status.supabase.io/) which tracks the uptime and latency of the Supabase platform.
![This image shows our new status page](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F100695019-468dae00-33cb-11eb-8967-1bf7381c418b.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Kaizen[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#kaizen)
  * We completed a security audit by DigitalXRAID.
  * Email confirmations now enabled by default for signups.
  * Updated [Benchmarking Suite](https://github.com/supabase/benchmarks/) to include more realistic workloads, on various different servers (results published soon).
  * You can now set/edit/remove Foreign Keys via the table editor.


### [Alpha October 2020 ](https://github.com/supabase/supabase/releases/tag/v0.0.10)
Nov 3, 2020
We're now 8 months into building Supabase. We're focused on performance, stability, and reliability but that hasn't prevented us from shipping some great features.
This is also available as a [blog post](https://supabase.io/blog/2020/11/02/supabase-alpha-october-2020) and a [video demo](https://www.youtube.com/watch?v=1gNDMMsUPI0).
### Supabase.js 1.0[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#supabasejs-10)
In the lead-up to our Beta launch, we've [released](https://supabase.io/blog/2020/10/30/improved-dx) `supabase-js` version 1.0 and it comes with some major Developer Experience improvements. We received a lot of feedback from the community and we've incorporated it into our client libraries for our 1.0 release.
Check out the [blog post](https://supabase.io/blog/2020/10/30/improved-dx) to learn more.
### More powerful SQL Editor[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#more-powerful-sql-editor)
Although it was only intended to be a temporary feature, the SQL Editor has become one of the most useful features of Supabase. This month we decided to make give it some attention, adding Tabs and making it full-screen. This is the first of many updates, we've got some exciting things planned for the SQL Editor.
![This image shows a SQL Editor with tabs. Originally our SQL editor was very basic, but we're moving towards something very powerful.](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F97948387-62e9fb00-1dcb-11eb-9b29-4258dd0e6ea9.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Keyboard shortcuts for Power Users[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#keyboard-shortcuts-for-power-users)
For the heavy table editor users, we've gone ahead and added a bunch of key commands and keyboard shortcuts so you can zip around and manipulate your tables faster than ever.
![This image shows some of the keyboard shortcuts we introduced on the table editor.](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F97948660-32569100-1dcc-11eb-95b4-233324c6e6ad.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Magic Links[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#magic-links)
One of the most requested Auth features was the ability to send magic links that your users can use to log in. You can use this with new or existing users, and alongside passwords or stand alone.
![This image shows a template where developers can edit the magic links email which is sent to their users on sign up.](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F97948557-e9064180-1dcb-11eb-981b-271d73837626.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Kaizen[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#kaizen)
  * We have new and improved [docs](https://supabase.io/docs/client/supabase-client).
  * We converted [realtime-js](https://github.com/supabase/realtime-js/) to TypeScript.
  * Dashboard Performance: we heavily optimised our dashboard routes.
  * With the help of the community, we [closed a lot of issues](https://github.com/orgs/supabase/projects/5) during Hacktoberfest.
  * We have started [benchmarking](https://github.com/supabase/benchmarks) all the open source tools we use. We'll publish the results this month.


### [Alpha September 2020 ](https://github.com/supabase/supabase/releases/tag/0.0.9)
Oct 7, 2020
This is also available as a [blog post](https://supabase.io/blog/2020/10/03/supabase-alpha-september-2020).
### Third-party logins[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#third-party-logins)
We've released OAuth logins! You can now enable third-party logins on your app for Bitbucket, GitHub, GitLab, or Google.
![This is a picture of the supabase dashboard with OAuth logins](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F95417260-2c08fc80-0967-11eb-827a-f52262d4612b.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Clone tables[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#clone-tables)
You can duplicate your tables, just like you would inside a spreadsheet.
![duplicate-tables](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F95417283-3fb46300-0967-11eb-8b0b-1a2e9da7cecd.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Enable and disable extensions[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#enable-and-disable-extensions)
Extensions are easier to use. You can enable Postgres extensions with the click of a button.
![toggle-extensions](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F95417437-a3d72700-0967-11eb-9445-afbb39d9898e.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Save your favorite queries[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#save-your-favorite-queries)
The SQL editor now stores your query history in your browser. You can also save your favorite queries to run later!
![favourites](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F95417377-80ac7780-0967-11eb-99dd-fb36abab6a62.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### GitHub Discussions[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#github-discussions)
Supabase was given access to [GitHub Discussions](https://github.com/supabase/supabase/discussions)! This is the place for you to ask questions or show off what you've built with Supabase.
![This is a screenshot of our GitHub Discussions, a new feature by GitHub](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F95417467-b3567000-0967-11eb-84ed-ad10a85cb98c.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Kaizen[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#kaizen)
  * Our dashboard now uses [Next.js automatic static optimization](https://nextjs.org/docs/advanced-features/automatic-static-optimization) - so it should be noticeably more responsive.
  * We created an Isomorphic [`gotrue-js`](https://github.com/supabase/gotrue-js/) TypeScript library for interacting with Netlify's [GoTrue server](https://github.com/netlify/gotrue). This will soon be bundled into `supabase-js`
  * We migrated our [`postgrest-js`](https://github.com/supabase/postgrest-js/) library to TypeScript, and it will soon be bundled into `supabase-js`


### [Alpha August 2020 ](https://github.com/supabase/supabase/releases/tag/0.0.8)
Sep 6, 2020
This is also available as a [blog post](https://supabase.io/blog/2020/09/03/supabase-alpha-august-2020).
We're 6 months into building our hosted database platform and we've made some major improvements to our auth system and table view.
## Easily create tables[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#easily-create-tables)
Set up tables and columns directly from the table view.
![Create tables from the dashboard](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F92347178-bf99a400-f101-11ea-8ac8-10462d608d80.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Invite your team[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#invite-your-team)
You can now invite team members to your organisation.
![Invite team members to Supabase](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F92347197-cb856600-f101-11ea-95f6-f3aa90373336.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Auth: Email Confirmations[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#auth-email-confirmations)
You can now enable Email Confirmations for new users. This can be toggled on or off and the template for this email can be edited via the dashboard.
![Email templates](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F92347203-d8a25500-f101-11ea-9ed9-49054665c6a6.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Typescript support[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#typescript-support)
The biggest communty contribution to date, [@thorwebdev](https://twitter.com/thorwebdev) added Typescript support to Supabase. He even [live streamed the process](https://twitter.com/thorwebdev/status/1292722189788016641).
![This gif shows how TypeScript makes it even easier to use Supabase, through VSCode's intellisense](https://supabase.com/_next/image?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F10214025%2F92347208-e22bbd00-f101-11ea-935a-a0414183bdd0.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Kaizen[#](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0yM1QwNzowMzozNVrOAG46dg==&restPage=2#kaizen)
We have a number of small improvements:
  * supabase-js now has [UMD support](https://github.com/supabase/supabase/pull/156)
  * We significantly [improved our docs](https://supabase.io/docs). Try out the new search!
  * All of our awesome sponsors are now listed [on our OSS page](https://supabase.io/oss).


[ Previous](https://supabase.com/changelog)[Next ](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wMi0wNlQwNDoyNToxM1rOAF5ftw==&restPage=3)
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

