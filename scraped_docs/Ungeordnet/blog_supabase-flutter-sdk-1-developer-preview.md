---
url: https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview
scraped_at: 2025-05-25T09:21:57.605174
title: Supabase Flutter SDK 1.0 Developer Preview
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
# Supabase Flutter SDK 1.0 Developer Preview
02 Aug 2022
•
6 minute read
[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Tyler ShukertDevRel](https://twitter.com/dshukertjr)
![Supabase Flutter SDK 1.0 Developer Preview](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-1%2Fsupabase-flutter-1.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today, we are releasing of Developer Preview version of v1.0 of [Supabase Flutter SDK](https://pub.dev/packages/supabase_flutter/versions/1.0.0-dev.1). Flutter has quickly become one of the most popular frameworks for developers to build cross-platform mobile apps. We can attest to that growth, our Flutter SDK is one of the most popular libraries and each day we see more Flutter devs choosing Supabase.
For this release, our main focus is developer experiences. We would love for you to try the SDK and provide your feedback so that we can continue to improve!
Before we dive into the actual updates, I would like to thank all the community contributors who have helped the library to be where it is today.
## Better developer experience[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#better-developer-experience)
Until now, there were some disputable implementations in the Flutter SDK. We've made several improvements:
### Automatically handling auth state persistence[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#automatically-handling-auth-state-persistence)
Previously, `supabase-flutter` required a class that extends `SupabaseAuthState` or `SupabaseAuthRequiredState` to persist auth state. With `supabase-flutter` 1.0, you no longer need to include these classes.
All you need to persist the auth state is initialize Supabase and everything else will be automatically taken care of. `SupabaseAuthState` and `SupabaseAuthRequiredState` have been removed from the code base.
`
1
// Before
2
await Supabase.initialize(
3
 url: 'SUPABASE_URL',
4
 anonKey: 'SUPABASE_ANON_KEY',
5
);
6
...
78
class AuthState<T extends StatefulWidget> extends SupabaseAuthState<T> {
9
 ...
10
}
1112
// After
13
await Supabase.initialize(
14
 url: 'SUPABASE_URL',
15
 anonKey: 'SUPABASE_ANON_KEY',
16
);
`
### Automatically handling deep links[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#automatically-handling-deep-links)
Deep link handling had similar issues previously, requiring you to implement `SupabaseAuthState` or `SupabaseAuthRequiredState` classes.
With the 1.0 update, you no longer need to use these classes, and deep links will be automatically handled. You can listen to `onAuthStateChange` to handle when a deep link is received to redirect users to a new screen.
`
1
// Before
2
void onReceivedAuthDeeplink(Uri uri) {
3
 Supabase.instance.log('onReceivedAuthDeeplink uri: $uri');
4
}
56
// After
7
await Supabase.instance.initialize(
8
 url: 'SUPABASE_URL',
9
 anonKey: 'SUPABASE_ANON_KEY',
10
);
`
### Throwing errors instead of returning them[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#throwing-errors-instead-of-returning-them)
When `supabase-dart` and `supabase-flutter` were created, we wanted to mirror the JavaScript library as much as possible. We soon realized that some syntax does not fit well when written in Dart. Throwing vs returning error is a good example of that. Since Dart does not have object destruction, the code becomes a bit tedious when errors are returned.
With `supabase-flutter` 1.0, we are throwing errors instead of returning them. This is consistent across all features from `auth`, `postgrest`, and `storage`.
`
1
// Before
2
final response = await Supabase.instance.from('messages').select().execute();
3
final data = response.data;
4
final error = response.error;
56
// After
7
try {
8
 final data = await Supabase.instance.from('messages').select();
9
} catch(error) {
10
 // Handle error here
11
}
`
### No more `.execute()` to get the data[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#no-more-execute-to-get-the-data)
We want this SDK to be as close as possible to the JavaScript SDK to provide consistent developer experience no matter what programming language you are using. Prior to the 1.0 update, whenever you called the `postgrest` endpoints, you had to call `.execute()` at the end of each query.
`.execute()` is now deprecated. You no longer needed it to query data from your Supabase database. This update, along with many many other improvements across the whole library, has been done by [Bruno D'Luka](https://github.com/bdlukaa), and I would love to give him a special shout out here!
`
1
// Before
2
final response = await Supabase.instance.from('messages').select().execute();
3
final data = response.data;
45
// After
6
final data = await Supabase.instance.from('messages').select();
`
## Desktop support for deeplinks[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#desktop-support-for-deeplinks)
Ever since `supabase-flutter` was born, it supported only iOS, Android and Web for deep linking. This was a limitation of the deep link library that we were using.
With the 1.0 launch, we are moving to use [app_links](https://pub.dev/packages/app_links), which will enable us to support MacOS and Windows applications as well! Linux support is being worked on - follow the repo to keep updated.
![Supabase Flutter desktop support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-1%2Fsupported-platforms-table.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Multiplayer support[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#multiplayer-support)
[Multiplayer](https://supabase.com/blog/supabase-realtime-with-multiplayer-features) is the next generation Supabase Realtime engine that was announced at the previous launch week.
We want our Flutter developers to experience this new multiplayer feature as well, so are working hard at bringing it to our Flutter SDK. It is not yet included in the developer preview of Supabase Flutter 1.0, but will be part of it when stable launch has been released.
## Supabase Auth UI for Flutter[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#supabase-auth-ui-for-flutter)
![Supabase Auth UI for Flutter](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-1%2Fsupabase-flutter-auth-ui.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Last but not least, we are bringing you another library, the Supabase Auth UI for Supabase! When released, this library will enable you to implement a basic authentication screen without building it yourself. You can just load the library and display a nice looking Auth UI. The library takes your theme settings automatically to match the look and feel of your application.
You can get started with it on [pub.dev](https://pub.dev/packages/supabase_auth_ui).
I would like to thank [Fatuma](https://twitter.com/XquisiteDreamer) for single-handedly working on bringing us an easier authentication experience.
`
1
// Email and password signin form
2
SupaEmailAuth(
3
 authAction: AuthAction.signIn,
4
 redirectUrl: '/home',
5
),
67
// Magic Link signin form
8
SupaMagicAuth(),
910
// Social Login Buttons
11
SupaSocialsAuth(
12
 socialProviders: [
13
 SocialProviders.apple,
14
 SocialProviders.google,
15
 ],
16
 colored: true,
17
),
`
## Final thoughts[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#final-thoughts)
These updates are just the tip of the iceberg for 1.0. There are been many bug fixes and features constantly being added to the Supabase Flutter SDK. This could not have been possible without the help from the open source community. Here, I would also like to give a shout out to two other developers who have been a major part of the journey of this SDK: [Vinzent](https://twitter.com/Vinzent03_) and [Daniel Mossaband](https://github.com/DanMossa). They have been a huge part of the Supabase Flutter SDK - not just for the 1.0 release, but throughout the lifetime of the library. For those of you who want to try out the new SDK, you can get the developer preview version from [supabase-flutter](https://pub.dev/packages/supabase_flutter/versions/1.0.0-dev.1) pub.dev page or can simply copy and paste the following into your pubspec.yaml file.
`
1
supabase_flutter: ^1.0.0-dev.1
`
If you have any feedbacks, please let us know in the issues of the [supabase-flutter](https://github.com/supabase-community/supabase-flutter/issues) repository.
## Flutter Resources[#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#flutter-resources)
  * [supabase-flutter 1.0 developer preview](https://pub.dev/packages/supabase_flutter)
  * [Flutter Tutorial: building a Flutter chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
  * [Flutter Tutorial - Part 2: Authentication and Authorization with RLS](https://supabase.com/blog/flutter-authentication-and-authorization-with-rls)
  * [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)
  * [Build a Flutter app with Very Good CLI and Supabase](https://verygood.ventures/blog/flutter-app-very-good-cli-supabase)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&text=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&text=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&t=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)
[Last postSupabase Beta July 20223 August 2022](https://supabase.com/blog/supabase-beta-update-july-2022)
[Next postImplementing "seen by" functionality with Postgres18 July 2022](https://supabase.com/blog/seen-by-in-postgresql)
[flutter](https://supabase.com/blog/tags/flutter)[mobile](https://supabase.com/blog/tags/mobile)
On this page
  * [Better developer experience](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#better-developer-experience)
    * [Automatically handling auth state persistence](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#automatically-handling-auth-state-persistence)
    * [Automatically handling deep links](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#automatically-handling-deep-links)
    * [Throwing errors instead of returning them](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#throwing-errors-instead-of-returning-them)
    * [No more `.execute()` to get the data](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#no-more-execute-to-get-the-data)
  * [Desktop support for deeplinks](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#desktop-support-for-deeplinks)
  * [Multiplayer support](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#multiplayer-support)
  * [Supabase Auth UI for Flutter](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#supabase-auth-ui-for-flutter)
  * [Final thoughts](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#final-thoughts)
  * [Flutter Resources](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#flutter-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&text=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&text=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&t=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)
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

