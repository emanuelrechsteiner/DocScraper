---
url: https://supabase.com/blog/flutter-authentication
scraped_at: 2025-05-25T09:03:15.856546
title: Getting started with Flutter authentication
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
# Getting started with Flutter authentication
18 Jul 2023
•
14 minute read
[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Tyler ShukertDevRel](https://twitter.com/dshukertjr)
![Getting started with Flutter authentication](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fflutter-authentication.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Flutter is Google’s open-source framework to develop cross-platform applications. In this article, we will take a look at how we can implement authentication using Google sign-in to secure our application using the [Supabase SDK for Flutter](https://supabase.com/docs/reference/dart/introduction).
We will also dive into the deep ends of Open ID Connect sign-in to better understand how third-party sign-ins are being performed. You can check out the code of the sample in this article [here](https://github.com/supabase/supabase/tree/master/examples/auth/flutter-native-google-auth).
## Prerequisites[#](https://supabase.com/blog/flutter-authentication#prerequisites)
This article assumes you are comfortable with writing a basic application in Flutter. No knowledge of Supabase is required.
We will use the following tools
  * [Flutter](https://docs.flutter.dev/get-started/install) - we used v3.10.5 for this article
  * Supabase - create your account [here](https://database.new/) if you do not have one
  * IDE of your choosing


## What is Open ID Connect?[#](https://supabase.com/blog/flutter-authentication#what-is-open-id-connect)
We will implement third-party login with Google utilizing the Open ID Connect functionality of Supabase Auth. Open ID Connect, or OIDC is a protocol built on top of OAuth 2.0 that allows third-party applications to request the users to provide some personal information, such as name or profile image, in the form of an identity token along with an access token. This identity token can then be verified and decoded by the application to obtain that personal information.
Supabase auth provides `signInWithIdToken` method where we can sign in a user using their ID token obtained from third-party auth providers such as Google. Upon signing a user with the `signInWithIdToken` method, Supabase automatically populates the content of the ID token in the Supabase user metadata for easy access to the information. We will be utilizing this feature in this example to display the user profile upon the user signing in.
In today’s example, our app will make a request to Google, obtain the identity token, and we will use it to sign the user in as well as obtain basic user information.
## What we will build[#](https://supabase.com/blog/flutter-authentication#what-we-will-build)
We will build a simple app with a login screen and a home screen. The user is first presented with the login screen, and only after they sign in, can they proceed to the home screen. The login screen presents a login button that will kick off a third-party authentication flow to complete the sign-in. The profile screen displays user information such as the profile image or their full name.
![Flutter Google sign in](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fflutter-google-sign-in.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Setup the Flutter project[#](https://supabase.com/blog/flutter-authentication#setup-the-flutter-project)
Let’s start by creating a fresh Flutter project.
`
1
flutter create myauthapp
`
then we can install the dependencies. Change the working directory to the newly created app directory and run the following command to install our dependencies.
`
1
flutter pub add supabase_flutter google_sign_in
`
The [supabase_flutter](https://pub.dev/packages/supabase_flutter) package is used to interact with a Supabase instance. The [google_sign_in](https://pub.dev/packages/google_sign_in) package is used to implement social sign-in with Google.
We are done installing our dependencies. Let’s set up [authentication](https://supabase.com/docs/guides/auth) now.
## Configure Google sign-in on Supabase Auth[#](https://supabase.com/blog/flutter-authentication#configure-google-sign-in-on-supabase-auth)
We will obtain client IDs for iOS, Android, and web from the Google Cloud console, and register them to our Supabase project. The web client ID will be used by the auth server of Supabase to verify the ID token provided by the Google sign-in package.
First, create your Google Cloud project [here](https://cloud.google.com/) if you do not have one yet. Within your Google Cloud project, follow the [Get an OAuth client ID for the iOS](https://developers.google.com/identity/sign-in/ios/start-integrating#get_an_oauth_client_id) guide, [Configure a Google API Console project for Android](https://developers.google.com/identity/sign-in/android/start-integrating#configure_a_project) guide, and [Get your backend server's OAuth 2.0 client ID](https://developers.google.com/identity/sign-in/android/start-integrating#configure_a_project) to obtain client IDs for iOS, Android, and web respectively.
Once you have the client IDs, let’s add them to our Supabase dashboard. If you don’t have a Supabase project created yet, you can create one at [database.new](https://database.new) for free. The name is just an internal name, so we can call it “Auth” for now. The database password won't be used in this example and can be reconfigured later, so press the `Generate a password` button and let Supabase generate a secure random password. The region should be anywhere close to where you live, or where your users live in an actual production app. Lastly, for the pricing plan choose the Free Plan that allows you to connect with all major social OAuth providers and supports up to 50,000 monthly active users.
![Supabase project creation](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fsupabase-project-creation.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Your project should be ready in a minute or two. Once your project is ready, open `authentication -> Providers -> Google` to set up Google auth. Toggle the `Enable Sign in with Google` switch first. Then add the web client ID you obtained in your Google Cloud console to `Authorized Client IDs` field. No need to add the Android or iOS client IDs here.
Turn on the `Skip nonce checks` option. This would allow us to use the Google sign in package on iOS, which is not compatible with providing a method to access or specify a nonce.
![Supabase auth Google auth provider](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fsupabase-google-provider.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We also need some iOS specific settings. Open `ios/Runner/Info.plist` file and add the `CFBundleURLTypes` like the following. You need to provide the reverse client ID of the iOS client ID you registered earlier.
`
1
<key>CFBundleURLTypes</key>
2
<array>
3
 <dict>
4
  <key>CFBundleTypeRole</key>
5
  <string>Editor</string>
6
  <key>CFBundleURLSchemes</key>
7
  <array>
8
   <!-- TODO Replace this value: -->
9
   <!-- Copied from GoogleService-Info.plist key REVERSED_CLIENT_ID -->
10
   <string>com.googleusercontent.apps.my-ios</string>
11
  </array>
12
 </dict>
13
</array>
`
That is it for setting up our [Supabase auth to prepare for Google sign-in](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=flutter).
Finally, we can initialize Supabase in our Flutter application with the credentials of our Supabase instance. Update your `main.dart` file and add `Supabase.initialize()` in the `main` function like the following. Note that you will see some errors since the home screen is set to the `LoginScreen`, which we will create later.
`
1
import 'package:flutter/material.dart';
2
import 'package:myauthapp/screens/login_screen.dart';
3
import 'package:supabase_flutter/supabase_flutter.dart';
45
void main() async {
6
 /// TODO: update Supabase credentials with your own
7
 await Supabase.initialize(
8
  url: 'YOUR_SUPABASE_URL',
9
  anonKey: 'YOUR_ANON_KEY',
10
 );
11
 runApp(const MyApp());
12
}
1314
final supabase = Supabase.instance.client;
1516
class MyApp extends StatelessWidget {
17
 const MyApp({super.key});
1819
 @override
20
 Widget build(BuildContext context) {
21
  return MaterialApp(
22
   debugShowCheckedModeBanner: false,
23
   title: 'Flutter Auth',
24
   theme: ThemeData(
25
    colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
26
    useMaterial3: true,
27
   ),
28
   home: const LoginScreen(),
29
  );
30
 }
31
}
`
You can find your Supabase URL and Anon key in `Settings -> API` from your [Supabase dashboard](https://supabase.com/dashboard/project/_/settings/api).
![Supabase credentials](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fsupabase-credentials.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Create the Login Screen[#](https://supabase.com/blog/flutter-authentication#create-the-login-screen)
We will have two screens for this app, `LoginScreen` and `ProfileScreen`. `LoginScreen` presents a single sign-in button for the user to perform Google sign-in. Create a `lib/screens/login_screen.dart` file add add the following.
`
1
import 'package:flutter/material.dart';
2
import 'package:google_sign_in/google_sign_in.dart';
3
import 'package:myauthapp/main.dart';
4
import 'package:myauthapp/screens/profile_screen.dart';
5
import 'package:supabase_flutter/supabase_flutter.dart';
67
class LoginScreen extends StatefulWidget {
8
 const LoginScreen({super.key});
910
 @override
11
 State<LoginScreen> createState() => _LoginScreenState();
12
}
1314
class _LoginScreenState extends State<LoginScreen> {
15
 @override
16
 void initState() {
17
  _setupAuthListener();
18
  super.initState();
19
 }
2021
 void _setupAuthListener() {
22
  supabase.auth.onAuthStateChange.listen((data) {
23
   final event = data.event;
24
   if (event == AuthChangeEvent.signedIn) {
25
    Navigator.of(context).pushReplacement(
26
     MaterialPageRoute(
27
      builder: (context) => const ProfileScreen(),
28
     ),
29
    );
30
   }
31
  });
32
 }
3334
 Future<AuthResponse> _googleSignIn() async {
35
  /// TODO: update the Web client ID with your own.
36
  ///
37
  /// Web Client ID that you registered with Google Cloud.
38
  const webClientId = 'my-web.apps.googleusercontent.com';
3940
  /// TODO: update the iOS client ID with your own.
41
  ///
42
  /// iOS Client ID that you registered with Google Cloud.
43
  const iosClientId = 'my-ios.apps.googleusercontent.com';
4445
  // Google sign in on Android will work without providing the Android
46
  // Client ID registered on Google Cloud.
4748
  final GoogleSignIn googleSignIn = GoogleSignIn(
49
   clientId: iosClientId,
50
   serverClientId: webClientId,
51
  );
52
  final googleUser = await googleSignIn.signIn();
53
  final googleAuth = await googleUser!.authentication;
54
  final accessToken = googleAuth.accessToken;
55
  final idToken = googleAuth.idToken;
5657
  if (accessToken == null) {
58
   throw 'No Access Token found.';
59
  }
60
  if (idToken == null) {
61
   throw 'No ID Token found.';
62
  }
6364
  return supabase.auth.signInWithIdToken(
65
   provider: OAuthProvider.google,
66
   idToken: idToken,
67
   accessToken: accessToken,
68
  );
69
 }
7071
 @override
72
 Widget build(BuildContext context) {
73
  return Scaffold(
74
   appBar: AppBar(
75
    title: const Text('Login'),
76
   ),
77
   body: Center(
78
    child: ElevatedButton(
79
     onPressed: _googleSignIn,
80
     child: const Text('Google login'),
81
    ),
82
   ),
83
  );
84
 }
85
}
`
In terms of UI, this page is very simple, it just has a basic `Scaffold` with an `AppBar`, and has a button right in the middle of the body. Upon pressing the button, Google sign in flow starts. The user is presented with a Google authentication screen where they will complete the consent to allow our application to sign the user in using a Google account, as well as allow us to view some personal information.
![Google sign in](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fgoogle-sign-in.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Within the `onPressed` callback of the button, we are calling the `_googleSignIn` method. This method calls the Google sign-in package to perform the sign-in flow. Once the user completes the sign-in flow, we obtain an access token and an ID token. We will pass these tokens to Supabase auth to then obtain a Supabase session.
## Create the Profile Screen[#](https://supabase.com/blog/flutter-authentication#create-the-profile-screen)
The `ProfileScreen` will be just a simple UI presenting some of the information we obtained in the `LoginPage`. We can access the user data with `supabase.auth.currentUser`, where Supabase has saved the personal information in a property called `userMetadata`. In this example, we are displaying the `avatar_url` and `full_name` to display a basic profile page. Create a `lib/screens/profile_screen.dart` file and add the following.
`
1
import 'package:flutter/material.dart';
2
import 'package:myauthapp/main.dart';
3
import 'package:myauthapp/screens/login_screen.dart';
45
class ProfileScreen extends StatelessWidget {
6
 const ProfileScreen({super.key});
78
 @override
9
 Widget build(BuildContext context) {
10
  final user = supabase.auth.currentUser;
11
  final profileImageUrl = user?.userMetadata?['avatar_url'];
12
  final fullName = user?.userMetadata?['full_name'];
13
  return Scaffold(
14
   appBar: AppBar(
15
    title: const Text('Profile'),
16
    actions: [
17
     TextButton(
18
      onPressed: () async {
19
       await supabase.auth.signOut();
20
       if (context.mounted) {
21
        Navigator.of(context).pushReplacement(
22
         MaterialPageRoute(builder: (context) => const LoginScreen()),
23
        );
24
       }
25
      },
26
      child: const Text('Sign out'),
27
     )
28
    ],
29
   ),
30
   body: Center(
31
    child: Column(
32
     mainAxisSize: MainAxisSize.min,
33
     children: [
34
      if (profileImageUrl != null)
35
       ClipOval(
36
        child: Image.network(
37
         profileImageUrl,
38
         width: 100,
39
         height: 100,
40
         fit: BoxFit.cover,
41
        ),
42
       ),
43
      const SizedBox(height: 16),
44
      Text(
45
       fullName ?? '',
46
       style: Theme.of(context).textTheme.headlineMedium,
47
      ),
48
      const SizedBox(height: 32),
49
     ],
50
    ),
51
   ),
52
  );
53
 }
54
}
`
And with that, we now have a basic working personalized application that utilizes Google sign-in.
![Flutter Google sign in app](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-authentication%2Fflutter-google-sign-in.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Conclusion[#](https://supabase.com/blog/flutter-authentication#conclusion)
In this post, we learned how to implement authentication in a Flutter application using Google sign-in and the Supabase SDK for Flutter. We also delved into the Open ID Connect functionality, which allows third-party sign-ins and the retrieval of personal information through identity tokens.
You can also check out the [Flutter reference documents](https://supabase.com/docs/reference/dart/installing) to see how you can use `supabase-flutter` to implement a Postgres database, Storage, Realtime, and more.
## More Flutter and Supabase resources[#](https://supabase.com/blog/flutter-authentication#more-flutter-and-supabase-resources)
  * [supabase_flutter package](https://pub.dev/packages/supabase_flutter)
  * [Build a chat application using Flutter and Supabase](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
  * [Securing your Flutter apps with Multi-Factor Authentication](https://supabase.com/blog/flutter-multi-factor-authentication)
  * [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&text=Getting%20started%20with%20Flutter%20authentication)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&text=Getting%20started%20with%20Flutter%20authentication)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&t=Getting%20started%20with%20Flutter%20authentication)
[Last postSupabase Launch Week 8 Hackathon25 July 2023](https://supabase.com/blog/supabase-lw8-hackathon)
[Next postpgvector 0.4.0 performance13 July 2023](https://supabase.com/blog/pgvector-performance)
[flutter](https://supabase.com/blog/tags/flutter)[auth](https://supabase.com/blog/tags/auth)
On this page
  * [Prerequisites](https://supabase.com/blog/flutter-authentication#prerequisites)
  * [What is Open ID Connect?](https://supabase.com/blog/flutter-authentication#what-is-open-id-connect)
  * [What we will build](https://supabase.com/blog/flutter-authentication#what-we-will-build)
  * [Setup the Flutter project](https://supabase.com/blog/flutter-authentication#setup-the-flutter-project)
  * [Configure Google sign-in on Supabase Auth](https://supabase.com/blog/flutter-authentication#configure-google-sign-in-on-supabase-auth)
  * [Create the Login Screen](https://supabase.com/blog/flutter-authentication#create-the-login-screen)
  * [Create the Profile Screen](https://supabase.com/blog/flutter-authentication#create-the-profile-screen)
  * [Conclusion](https://supabase.com/blog/flutter-authentication#conclusion)
  * [More Flutter and Supabase resources](https://supabase.com/blog/flutter-authentication#more-flutter-and-supabase-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&text=Getting%20started%20with%20Flutter%20authentication)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&text=Getting%20started%20with%20Flutter%20authentication)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authentication&t=Getting%20started%20with%20Flutter%20authentication)
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

