---
url: https://supabase.com/blog/flutter-multi-factor-authentication
scraped_at: 2025-05-25T09:19:20.436749
title: Securing your Flutter apps with Multi-Factor Authentication
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
# Securing your Flutter apps with Multi-Factor Authentication
04 May 2023
•
50 minute read
[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Tyler ShukertDevRel](https://twitter.com/dshukertjr)
![Securing your Flutter apps with Multi-Factor Authentication](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fflutter-mfa-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Multi-factor authentication or MFA is an essential part of security for any kind of app.
We will take a look at an example app where a user has to sign in via MFA in order to view the contents of the app to demonstrate how easy it is to get started with MFA on Flutter.
## What is Multi-Factor Authentication?[#](https://supabase.com/blog/flutter-multi-factor-authentication#what-is-multi-factor-authentication)
Multi-factor authentication (MFA), sometimes called two-factor authentication (2FA), is an additional security layer on top of traditional login methods such as email and password login.
There are several forms of MFA, such as with an SMS or through using an authenticator app such as Google Authenticator. It is considered a best practice to use MFA whenever possible because it protects users against weak passwords or compromised social accounts.
## Why Multi-Factor Authentication matters for Flutter apps[#](https://supabase.com/blog/flutter-multi-factor-authentication#why-multi-factor-authentication-matters-for-flutter-apps)
In the context of Flutter apps, MFA is important because it helps protect sensitive user data and prevent unauthorized access to user accounts. By requiring users to provide an additional factor, MFA adds an extra layer of security that makes it harder for attackers to gain access to user accounts.
Given how Flutter is widely used MFA might be a requirement rather than a nice-to-have. Implementing MFA in a Flutter app can improve overall security and give users peace of mind knowing that their data is better protected.
## Building the App[#](https://supabase.com/blog/flutter-multi-factor-authentication#building-the-app)
![Multi-factor Authentication with Flutter](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fmfa.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We are building a simple app where users register with an email and password. After completing the registration process, the users will be asked to set up MFA using an authenticator app. Once verifying the identity via the authenticator app, the user can go to the home page where they can view the main content.
Login works similarly, where after an email and password login, they are asked to enter the verification code to complete the login process.
The app will have the following directory structure, where `auth` contains any basic auth-related pages, `mfa` contains enrolling and verifying the MFA, and we have some additional pages for us to see that MFA is working correctly.
You can find the complete code created in this article [here](https://github.com/supabase/supabase/tree/master/examples/auth/flutter-mfa).
![Directory Structure of the app](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fdirectory.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Step 1: Setup the scenes[#](https://supabase.com/blog/flutter-multi-factor-authentication#step-1-setup-the-scenes)
Let’s start with the `flutter create` command.
`
1
flutter create mfa_app
`
Also, if you do not have a Supabase project yet, create one by heading to [database.new](https://dstabase.new). Within a few minutes, you will have a new Supabase project.
### Step 2: Add the dependencies[#](https://supabase.com/blog/flutter-multi-factor-authentication#step-2-add-the-dependencies)
Install the [supabase_flutter](https://pub.dev/packages/supabase_flutter) package by running the following command in your terminal.
`
1
dart pub add supabase_flutter
`
Then update your `lib/main.dart` file to initialize Supabase in the main function. You should be able to find your Supabase URL and AnonKey from the `settings -> api` section of your dashboard. We will also extract the `SupabaseClient` for easy access to our Supabase instance.
`
1
import 'package:flutter/material.dart';
2
import 'package:supabase_flutter/supabase_flutter.dart';
34
void main() async {
5
 await Supabase.initialize(
6
  url: 'SUPABASE_URL',
7
  anonKey: 'SUPABASE_ANONKEY',
8
 );
9
 runApp(const MyApp());
10
}
1112
/// Extract SupabaseClient instance in a handy variable
13
final supabase = Supabase.instance.client;
`
Also, add [go_router](https://pub.dev/packages/go_router) to handle our routing and redirects.
`
1
dart pub add go_router
`
We will set up the routes towards the end when we have created all the pages we need. With this, we are ready to jump into creating the app.
Also, if we want to support iOS and Android, we need to set up deep links so that a session can be obtained upon clicking on the confirmation link sent to the user’s email address.
We will configure it so that we can open the app by redirecting to `mfa-app://callback` .
For iOS, open `ios/Runner/info.plist` file and add the following deep link configuration.
`
1
<!-- ... other tags -->
2
 <plist>
3
 <dict>
4
  <!-- ... other tags -->
56
		<!-- Deep Links -->
7
		<key>FlutterDeepLinkingEnabled</key>
8
		<true/>
9
  <key>CFBundleURLTypes</key>
10
  <array>
11
   <dict>
12
    <key>CFBundleTypeRole</key>
13
    <string>Editor</string>
14
    <key>CFBundleURLSchemes</key>
15
    <array>
16
     <string>mfa-app</string>
17
    </array>
18
   </dict>
19
  </array>
20
		<!-- Deep Links -->
2122
  <!-- ... other tags -->
23
 </dict>
24
 </plist>
`
For Android, open `android/app/src/main/AndroidManifest.xml` file and add the following deep link configuration.
`
1
<manifest ...>
2
  <!-- ... other tags -->
3
  <application ...>
4
   <activity ...>
5
    <!-- ... other tags -->
67
    <!-- Deep Links -->
8
				<meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
9
    <intent-filter>
10
     <action android:name="android.intent.action.VIEW" />
11
     <category android:name="android.intent.category.DEFAULT" />
12
     <category android:name="android.intent.category.BROWSABLE" />
13
     <data
14
      android:scheme="mfa-app"
15
      android:host="callback" />
16
    </intent-filter>
17
    <!-- END Deep Links -->
1819
   </activity>
20
  </application>
21
 </manifest>
`
After, we will add the deep link as one of the redirect URLs in our Supabase dashboard.
Go to `Authentication > URL Configuration` and add `mfa-app://callback/*` as a redirect URL. Make sure you don’t add any extra slashes or anything because if you do, deep linking will not work properly.
![Supabase Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fsupabase-dashboard.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Lastly, we will add the `flutter_svg` package. This package will later be used to display a QR code to scan with their authentication app.
`
1
dart pub add flutter_svg
`
That is all the dependencies that we need. Let’s dive into coding!
### Step 3: Create the signup flow[#](https://supabase.com/blog/flutter-multi-factor-authentication#step-3-create-the-signup-flow)
![Register flow](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fregister.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Let’s first create a signup flow. Again, the user will register with the app using email and password, and after confirming their email address, they will enroll in MFA using an authenticator app.
The register page contains a form with an email and password field for the user to create a new account. We are just calling the [.signUp()](https://supabase.com/docs/reference/dart/auth-signup) method with it. As you can see in the code below at `emailRedirectTo` option of the `.signUp()`method, upon clicking on the confirmation link sent to the user, they will be taken to MFA enrollment page, which we will implement later.
Create a `lib/pages/auth/signup_page.dart` file and add the following. There will be some errors, but that is because we haven’t created some of the files yet. The errors will go away as we move on, so ignore them for now.
`
1
import 'package:flutter/material.dart';
2
import 'package:go_router/go_router.dart';
3
import 'package:mfa_app/main.dart';
4
import 'package:mfa_app/pages/auth/login_page.dart';
5
import 'package:mfa_app/pages/mfa/enroll_page.dart';
6
import 'package:supabase_flutter/supabase_flutter.dart';
78
class RegisterPage extends StatefulWidget {
9
 static const route = '/auth/register';
1011
 const RegisterPage({super.key});
1213
 @override
14
 State<RegisterPage> createState() => _RegisterPageState();
15
}
1617
class _RegisterPageState extends State<RegisterPage> {
18
 final _emailController = TextEditingController();
19
 final _passwordController = TextEditingController();
2021
 bool _isLoading = false;
2223
 @override
24
 void dispose() {
25
  _emailController.dispose();
26
  _passwordController.dispose();
27
  super.dispose();
28
 }
2930
 @override
31
 Widget build(BuildContext context) {
32
  return Scaffold(
33
   appBar: AppBar(title: const Text('Register')),
34
   body: ListView(
35
    padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
36
    children: [
37
     TextFormField(
38
      controller: _emailController,
39
      decoration: const InputDecoration(
40
       label: Text('Email'),
41
      ),
42
     ),
43
     const SizedBox(height: 16),
44
     TextFormField(
45
      controller: _passwordController,
46
      decoration: const InputDecoration(
47
       label: Text('Password'),
48
      ),
49
      obscureText: true,
50
     ),
51
     const SizedBox(height: 16),
52
     ElevatedButton(
53
      onPressed: () async {
54
       try {
55
        setState(() {
56
         _isLoading = true;
57
        });
58
        final email = _emailController.text.trim();
59
        final password = _passwordController.text.trim();
60
        await supabase.auth.signUp(
61
         email: email,
62
         password: password,
63
         emailRedirectTo:
64
           'mfa-app://callback${MFAEnrollPage.route}', // redirect the user to setup MFA page after email confirmation
65
        );
66
        if (mounted) {
67
         ScaffoldMessenger.of(context).showSnackBar(
68
           const SnackBar(content: Text('Check your inbox.')));
69
        }
70
       } on AuthException catch (error) {
71
        ScaffoldMessenger.of(context)
72
          .showSnackBar(SnackBar(content: Text(error.message)));
73
       } catch (error) {
74
        ScaffoldMessenger.of(context).showSnackBar(
75
          const SnackBar(content: Text('Unexpected error occurred')));
76
       }
77
       if (mounted) {
78
        setState(() {
79
         _isLoading = false;
80
        });
81
       }
82
      },
83
      child: _isLoading
84
        ? const SizedBox(
85
          height: 24,
86
          width: 24,
87
          child: Center(
88
            child: CircularProgressIndicator(color: Colors.white)),
89
         )
90
        : const Text('Register'),
91
     ),
92
     const SizedBox(height: 16),
93
     TextButton(
94
      onPressed: () => context.push(LoginPage.route),
95
      child: const Text('I already have an account'),
96
     )
97
    ],
98
   ),
99
  );
100
 }
101
}
`
We can then create the enrollment page for MFA. This page is taking care of the following.
  * Retrieve the enrollment secret from the server via `supabase.auth.mfa.enroll()` method.
  * Displaying the secret and its QR code representation and prompts the user to add the app to their authenticator app
  * Verifies the user with a TOTP


The QR code and the secret will be displayed automatically when the page loads. When the user enters the correct 6-digit TOTP, they will be automatically redirected to the home page.
Create `lib/pages/mfa/enroll_page.dart` file and add the following.
`
1
import 'package:flutter/material.dart';
2
import 'package:flutter/services.dart';
3
import 'package:flutter_svg/flutter_svg.dart';
4
import 'package:go_router/go_router.dart';
5
import 'package:mfa_app/main.dart';
6
import 'package:mfa_app/pages/auth/register_page.dart';
7
import 'package:mfa_app/pages/home_page.dart';
8
import 'package:supabase_flutter/supabase_flutter.dart';
910
class MFAEnrollPage extends StatefulWidget {
11
 static const route = '/mfa/enroll';
12
 const MFAEnrollPage({super.key});
1314
 @override
15
 State<MFAEnrollPage> createState() => _MFAEnrollPageState();
16
}
1718
class _MFAEnrollPageState extends State<MFAEnrollPage> {
19
 final _enrollFuture = supabase.auth.mfa.enroll();
2021
 @override
22
 Widget build(BuildContext context) {
23
  return Scaffold(
24
   appBar: AppBar(
25
    title: const Text('Setup MFA'),
26
    actions: [
27
     TextButton(
28
      onPressed: () {
29
       supabase.auth.signOut();
30
       context.go(RegisterPage.route);
31
      },
32
      child: Text(
33
       'Logout',
34
       style: TextStyle(color: Theme.of(context).colorScheme.onPrimary),
35
      ),
36
     ),
37
    ],
38
   ),
39
   body: FutureBuilder(
40
    future: _enrollFuture,
41
    builder: (context, snapshot) {
42
     if (snapshot.hasError) {
43
      return Center(child: Text(snapshot.error.toString()));
44
     }
45
     if (!snapshot.hasData) {
46
      return const Center(child: CircularProgressIndicator());
47
     }
4849
     final response = snapshot.data!;
50
     final qrCodeUrl = response.totp.qrCode;
51
     final secret = response.totp.secret;
52
     final factorId = response.id;
5354
     return ListView(
55
      padding: const EdgeInsets.symmetric(
56
       horizontal: 20,
57
       vertical: 24,
58
      ),
59
      children: [
60
       const Text(
61
        'Open your authentication app and add this app via QR code or by pasting the code below.',
62
        style: TextStyle(
63
         fontWeight: FontWeight.bold,
64
        ),
65
       ),
66
       const SizedBox(height: 16),
67
       SvgPicture.string(
68
        qrCodeUrl,
69
        width: 150,
70
        height: 150,
71
       ),
72
       const SizedBox(height: 16),
73
       Row(
74
        children: [
75
         Expanded(
76
          child: Text(
77
           secret,
78
           style: const TextStyle(
79
            fontWeight: FontWeight.bold,
80
            fontSize: 18,
81
           ),
82
          ),
83
         ),
84
         IconButton(
85
          onPressed: () {
86
           Clipboard.setData(ClipboardData(text: secret));
87
           ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
88
             content: Text('Copied to your clip board')));
89
          },
90
          icon: const Icon(Icons.copy),
91
         ),
92
        ],
93
       ),
94
       const SizedBox(height: 16),
95
       const Text('Enter the code shown in your authentication app.'),
96
       const SizedBox(height: 16),
97
       TextFormField(
98
        decoration: const InputDecoration(
99
         hintText: '000000',
100
        ),
101
        style: const TextStyle(fontSize: 24),
102
        textAlign: TextAlign.center,
103
        keyboardType: TextInputType.number,
104
        onChanged: (value) async {
105
         if (value.length != 6) return;
106107
         // kick off the verification process once 6 characters are entered
108
         try {
109
          final challenge =
110
            await supabase.auth.mfa.challenge(factorId: factorId);
111
          await supabase.auth.mfa.verify(
112
           factorId: factorId,
113
           challengeId: challenge.id,
114
           code: value,
115
          );
116
          await supabase.auth.refreshSession();
117
          if (mounted) {
118
           context.go(HomePage.route);
119
          }
120
         } on AuthException catch (error) {
121
          ScaffoldMessenger.of(context)
122
            .showSnackBar(SnackBar(content: Text(error.message)));
123
         } catch (error) {
124
          ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
125
            content: Text('Unexpected error occurred')));
126
         }
127
        },
128
       ),
129
      ],
130
     );
131
    },
132
   ),
133
  );
134
 }
135
}
`
### Step 4: Creating the login flow[#](https://supabase.com/blog/flutter-multi-factor-authentication#step-4-creating-the-login-flow)
![Login flow](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Flogin.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Now that we have created a registration flow, we can get to the login flow for returning existing users. Again, the login page has nothing fancy going. We are just collecting the user’s email and password, and calling the good old [.signInWithPassword()](https://supabase.com/docs/reference/dart/auth-signinwithpassword) method. Upon signing in, the user will be taken to a verify page where the user will then enter their verification code from their authenticator app.
Create `lib/pages/auth/login_page.dart` and add the following.
`
1
import 'package:flutter/material.dart';
2
import 'package:go_router/go_router.dart';
3
import 'package:mfa_app/main.dart';
4
import 'package:mfa_app/pages/mfa/verify_page.dart';
5
import 'package:supabase_flutter/supabase_flutter.dart';
67
class LoginPage extends StatefulWidget {
8
 static const route = '/auth/login';
910
 const LoginPage({super.key});
1112
 @override
13
 State<LoginPage> createState() => _LoginPageState();
14
}
1516
class _LoginPageState extends State<LoginPage> {
17
 final _emailController = TextEditingController();
18
 final _passwordController = TextEditingController();
1920
 @override
21
 void dispose() {
22
  _emailController.dispose();
23
  _passwordController.dispose();
24
  super.dispose();
25
 }
2627
 @override
28
 Widget build(BuildContext context) {
29
  return Scaffold(
30
   appBar: AppBar(title: const Text('Login')),
31
   body: ListView(
32
    padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
33
    children: [
34
     TextFormField(
35
      controller: _emailController,
36
      decoration: const InputDecoration(
37
       label: Text('Email'),
38
      ),
39
     ),
40
     const SizedBox(height: 16),
41
     TextFormField(
42
      controller: _passwordController,
43
      decoration: const InputDecoration(
44
       label: Text('Password'),
45
      ),
46
      obscureText: true,
47
     ),
48
     const SizedBox(height: 16),
49
     ElevatedButton(
50
      onPressed: () async {
51
       try {
52
        final email = _emailController.text.trim();
53
        final password = _passwordController.text.trim();
54
        await supabase.auth.signInWithPassword(
55
         email: email,
56
         password: password,
57
        );
58
        if (mounted) {
59
         context.go(MFAVerifyPage.route);
60
        }
61
       } on AuthException catch (error) {
62
        ScaffoldMessenger.of(context)
63
          .showSnackBar(SnackBar(content: Text(error.message)));
64
       } catch (error) {
65
        ScaffoldMessenger.of(context).showSnackBar(
66
          const SnackBar(content: Text('Unexpected error occurred')));
67
       }
68
      },
69
      child: const Text('Login'),
70
     ),
71
    ],
72
   ),
73
  );
74
 }
75
}
`
Once a returning user logs in, they are taken to the verification page where they are asked to enter the TOTP from their authenticator app.
This verification page has the same text field as the enrollment page, and upon entering the code, they are taken to the home page.
Create a `lib/pages/mfa/verify_page.dart` file and add the following.
`
1
import 'package:flutter/material.dart';
2
import 'package:go_router/go_router.dart';
3
import 'package:mfa_app/main.dart';
4
import 'package:mfa_app/pages/auth/register_page.dart';
5
import 'package:mfa_app/pages/home_page.dart';
6
import 'package:supabase_flutter/supabase_flutter.dart';
78
class MFAVerifyPage extends StatefulWidget {
9
 static const route = '/mfa/verify';
10
 const MFAVerifyPage({super.key});
1112
 @override
13
 State<MFAVerifyPage> createState() => _MFAVerifyPageState();
14
}
1516
class _MFAVerifyPageState extends State<MFAVerifyPage> {
17
 @override
18
 Widget build(BuildContext context) {
19
  return Scaffold(
20
   appBar: AppBar(
21
    title: const Text('Verify MFA'),
22
    actions: [
23
     TextButton(
24
      onPressed: () {
25
       supabase.auth.signOut();
26
       context.go(RegisterPage.route);
27
      },
28
      child: Text(
29
       'Logout',
30
       style: TextStyle(color: Theme.of(context).colorScheme.onPrimary),
31
      ),
32
     ),
33
    ],
34
   ),
35
   body: ListView(
36
    padding: const EdgeInsets.symmetric(
37
     horizontal: 20,
38
     vertical: 24,
39
    ),
40
    children: [
41
     Text(
42
      'Verification Required',
43
      style: Theme.of(context).textTheme.titleLarge,
44
     ),
45
     const SizedBox(height: 16),
46
     const Text('Enter the code shown in your authentication app.'),
47
     const SizedBox(height: 16),
48
     TextFormField(
49
      decoration: const InputDecoration(
50
       hintText: '000000',
51
      ),
52
      style: const TextStyle(fontSize: 24),
53
      textAlign: TextAlign.center,
54
      keyboardType: TextInputType.number,
55
      onChanged: (value) async {
56
       if (value.length != 6) return;
5758
       // kick off the verification process once 6 characters are entered
59
       try {
60
        final factorsResponse = await supabase.auth.mfa.listFactors();
61
        final factor = factorsResponse.totp.first;
62
        final factorId = factor.id;
6364
        final challenge =
65
          await supabase.auth.mfa.challenge(factorId: factorId);
66
        await supabase.auth.mfa.verify(
67
         factorId: factorId,
68
         challengeId: challenge.id,
69
         code: value,
70
        );
71
        await supabase.auth.refreshSession();
72
        if (mounted) {
73
         context.go(HomePage.route);
74
        }
75
       } on AuthException catch (error) {
76
        ScaffoldMessenger.of(context)
77
          .showSnackBar(SnackBar(content: Text(error.message)));
78
       } catch (error) {
79
        ScaffoldMessenger.of(context).showSnackBar(
80
          const SnackBar(content: Text('Unexpected error occurred')));
81
       }
82
      },
83
     ),
84
    ],
85
   ),
86
  );
87
 }
88
}
`
### Step 5: Add a home page with secure contents[#](https://supabase.com/blog/flutter-multi-factor-authentication#step-5-add-a-home-page-with-secure-contents)
![Home Page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-mfa%2Fhome.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The home page is where the “secure” contents are displayed. We will create a dummy table with some dummy secure contents for demonstration purposes.
First, we create dummy content. Run the following SQL to create the table and add some content.
`
1
-- Dummy table that contains "secure" information
2
create table
3
 if not exists public.private_posts (
4
  id int generated by default as identity primary key,
5
  content text not null
6
 );
78
-- Dmmy "secure" data
9
insert into
10
 public.private_posts (content)
11
values
12
 ('Flutter is awesome!'),
13
 ('Supabase is awesome!'),
14
 ('Postgres is awesome!');
`
Now, we can add some [row security policy](https://supabase.com/docs/guides/auth/row-level-security) to lock those data down so that only users who have signed in using MFA can view them.
Run the following SQL to secure our data from malicious users.
`
1
-- Enable RLS for private_posts table
2
alter table
3
 public.private_posts enable row level security;
45
-- Create a policy that only allows read if they user has signed in via MFA
6
create policy "Users can view private_posts if they have signed in via MFA" on public.private_posts for
7
select
8
 to authenticated using ((select auth.jwt() - >> 'aal') = 'aal2');
`
`aal` here stands for [Authenticator Assurance Level](https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/), and it will be `aal1` for users who have only signed in with 1 sign-in method, and `aal2` for users who have completed the MFA flow. Checking the `aal` inside RLS policy ensures that the data cannot be viewed by users unless they complete the entire MFA flow.
The nice thing about RLS is that it gives us the flexibility to control how users can interact with the data. In this particular example, we are mandating MFA to view the data, but you could easily create layered permissions where for example a user can view the data with 1 factor, but can edit the data when signed in with MFA. You can see more examples in our official MFA guide [here](https://supabase.com/docs/guides/auth/auth-mfa).
Now that we have the secure data in our Supabase instance, all we need to do is to display them in the HomePage. We can simply query the table and display it using a `FutureBuilder`.
Create a `lib/pages/home_page.dart` file and add the following.
`
1
import 'package:flutter/material.dart';
2
import 'package:go_router/go_router.dart';
3
import 'package:mfa_app/main.dart';
4
import 'package:mfa_app/pages/auth/register_page.dart';
5
import 'package:mfa_app/pages/list_mfa_page.dart';
67
class HomePage extends StatelessWidget {
8
 static const route = '/';
910
 const HomePage({super.key});
1112
 @override
13
 Widget build(BuildContext context) {
14
  final privatePostsFuture = supabase.from('private_posts').select();
1516
  return Scaffold(
17
   appBar: AppBar(
18
    title: const Text('Home'),
19
    actions: [
20
     PopupMenuButton(
21
      itemBuilder: (context) {
22
       return [
23
        PopupMenuItem(
24
         child: const Text('Unenroll MFA'),
25
         onTap: () {
26
          context.push(ListMFAPage.route);
27
         },
28
        ),
29
        PopupMenuItem(
30
         child: const Text('Logout'),
31
         onTap: () {
32
          supabase.auth.signOut();
33
          context.go(RegisterPage.route);
34
         },
35
        ),
36
       ];
37
      },
38
     )
39
    ],
40
   ),
41
   body: FutureBuilder<List<Map<String, dynamic>>>(
42
    future: privatePostsFuture,
43
    builder: (context, snapshot) {
44
     if (snapshot.hasError) {
45
      return Center(child: Text(snapshot.error.toString()));
46
     }
47
     if (!snapshot.hasData) {
48
      return const Center(child: CircularProgressIndicator());
49
     }
5051
     // Display the secure private content upon retrieval
52
     final data = snapshot.data!;
53
     return ListView.builder(
54
      itemCount: data.length,
55
      itemBuilder: (context, index) {
56
       return ListTile(title: Text(data[index]['content']));
57
      },
58
     );
59
    },
60
   ),
61
  );
62
 }
63
}
`
Because we have set the RLS policy, any user without going through the MFA flow will not see anything on this page.
One final page to add here is the **unenrollment** page. On this page, users can remove any factors that they have added. Once a user removes the factor, the user’s account will no longer be associated with the authenticator app, and they would have to go through the enrollment steps again.
Create `lib/pages/list_mfa_page.dart` file and add the following.
`
1
import 'package:flutter/material.dart';
2
import 'package:go_router/go_router.dart';
3
import 'package:mfa_app/main.dart';
4
import 'package:mfa_app/pages/auth/register_page.dart';
56
/// A page that lists the currently signed in user's MFA methods.
7
///
8
/// The user can unenroll the factors.
9
class ListMFAPage extends StatelessWidget {
10
 static const route = '/list-mfa';
11
 ListMFAPage({super.key});
1213
 final _factorListFuture = supabase.auth.mfa.listFactors();
1415
 @override
16
 Widget build(BuildContext context) {
17
  return Scaffold(
18
   appBar: AppBar(title: const Text('List of MFA Factors')),
19
   body: FutureBuilder(
20
    future: _factorListFuture,
21
    builder: (context, snapshot) {
22
     if (snapshot.hasError) {
23
      return Center(child: Text(snapshot.error.toString()));
24
     }
25
     if (!snapshot.hasData) {
26
      return const Center(child: CircularProgressIndicator());
27
     }
2829
     final response = snapshot.data!;
30
     final factors = response.all;
31
     return ListView.builder(
32
      itemCount: factors.length,
33
      itemBuilder: (context, index) {
34
       final factor = factors[index];
35
       return ListTile(
36
        title: Text(factor.friendlyName ?? factor.factorType.name),
37
        subtitle: Text(factor.status.name),
38
        trailing: IconButton(
39
         onPressed: () {
40
          showDialog(
41
            context: context,
42
            builder: (context) {
43
             return AlertDialog(
44
              title: const Text(
45
               'Are you sure you want to delete this factor? You will be signed out of the app upon removing the factor.',
46
              ),
47
              actions: [
48
               TextButton(
49
                onPressed: () {
50
                 context.pop();
51
                },
52
                child: const Text('cancel'),
53
               ),
54
               TextButton(
55
                onPressed: () async {
56
                 await supabase.auth.mfa.unenroll(factor.id);
57
                 await supabase.auth.signOut();
58
                 if (context.mounted) {
59
                  context.go(RegisterPage.route);
60
                 }
61
                },
62
                child: const Text('delete'),
63
               ),
64
              ],
65
             );
66
            });
67
         },
68
         icon: const Icon(Icons.delete_outline),
69
        ),
70
       );
71
      },
72
     );
73
    },
74
   ),
75
  );
76
 }
77
}
`
### Step 6: Putting the pieces together with go_router[#](https://supabase.com/blog/flutter-multi-factor-authentication#step-6-putting-the-pieces-together-with-go_router)
Now that we have all the pages, it’s time to put it all together with the help of [go_router](https://pub.dev/packages/go_router).
go_router, as you may know, is a routing package for Flutter, and its redirect feature is particularly helpful for implementing the complex requirement this app had. Particularly, we wanted to make sure that a user who has not yet set up MFA is redirected to the MFA setup page, and only users who have signed in land on the home page.
Another helpful feature of go_router comes when using deep links, and it automatically redirects the users to the correct path of the deep link. Because of this, we can ensure that user lands on the MFA setup page upon confirming their email address.
We will add the router in our `lib/main.dart` file. Your `main.dart` file should now look like this.
`
1
import 'package:flutter/material.dart';
2
import 'package:go_router/go_router.dart';
3
import 'package:mfa_app/pages/auth/login_page.dart';
4
import 'package:mfa_app/pages/auth/register_page.dart';
5
import 'package:mfa_app/pages/home_page.dart';
6
import 'package:mfa_app/pages/list_mfa_page.dart';
7
import 'package:mfa_app/pages/mfa/verify_page.dart';
8
import 'package:supabase_flutter/supabase_flutter.dart';
9
import 'package:mfa_app/pages/mfa/enroll_page.dart';
1011
void main() async {
12
 await Supabase.initialize(
13
  url: 'YOUR_SUPABASE_URL',
14
  anonKey: 'YOUR_ANON_KEY',
15
 );
16
 runApp(const MyApp());
17
}
1819
/// Extract SupabaseClient instance in a handy variable
20
final supabase = Supabase.instance.client;
2122
final _router = GoRouter(
23
 routes: [
24
  GoRoute(
25
   path: HomePage.route,
26
   builder: (context, state) => const HomePage(),
27
  ),
28
  GoRoute(
29
   path: ListMFAPage.route,
30
   builder: (context, state) => ListMFAPage(),
31
  ),
32
  GoRoute(
33
   path: LoginPage.route,
34
   builder: (context, state) => const LoginPage(),
35
  ),
36
  GoRoute(
37
   path: RegisterPage.route,
38
   builder: (context, state) => const RegisterPage(),
39
  ),
40
  GoRoute(
41
   path: MFAEnrollPage.route,
42
   builder: (context, state) => const MFAEnrollPage(),
43
  ),
44
  GoRoute(
45
   path: MFAVerifyPage.route,
46
   builder: (context, state) => const MFAVerifyPage(),
47
  ),
48
 ],
49
 redirect: (context, state) async {
50
  // Any users can visit the /auth route
51
  if (state.location.contains('/auth') == true) {
52
   return null;
53
  }
5455
  final session = supabase.auth.currentSession;
56
  // A user without a session should be redirected to the register page
57
  if (session == null) {
58
   return RegisterPage.route;
59
  }
6061
  final assuranceLevelData =
62
    supabase.auth.mfa.getAuthenticatorAssuranceLevel();
6364
  // The user has not setup MFA yet, so send them to enroll MFA page.
65
  if (assuranceLevelData.currentLevel == AuthenticatorAssuranceLevels.aal1) {
66
   await supabase.auth.refreshSession();
67
   final nextLevel =
68
     supabase.auth.mfa.getAuthenticatorAssuranceLevel().nextLevel;
69
   if (nextLevel == AuthenticatorAssuranceLevels.aal2) {
70
    // The user has already setup MFA, but haven't login via MFA
71
    // Redirect them to the verify page
72
    return MFAVerifyPage.route;
73
   } else {
74
    // The user has not yet setup MFA
75
    // Redirect them to the enrollment page
76
    return MFAEnrollPage.route;
77
   }
78
  }
7980
  // The user has signed invia MFA, and is allowed to view any page.
81
  return null;
82
 },
83
);
8485
class MyApp extends StatelessWidget {
86
 const MyApp({super.key});
8788
 // This widget is the root of your application.
89
 @override
90
 Widget build(BuildContext context) {
91
  return MaterialApp.router(
92
   title: 'MFA App',
93
   debugShowCheckedModeBanner: false,
94
   theme: ThemeData.light().copyWith(
95
    inputDecorationTheme: const InputDecorationTheme(
96
     border: OutlineInputBorder(),
97
    ),
98
   ),
99
   routerConfig: _router,
100
  );
101
 }
102
}
`
## Conclusions and future iterations[#](https://supabase.com/blog/flutter-multi-factor-authentication#conclusions-and-future-iterations)
We looked at how to incorporate Multi-Factor Authentication into a Flutter app with a complete enrollment and verification flow for new and existing users. We saw how we are able to control how the users can interact with the data using their MFA status.
Another common use case is to make MFA optional and allow the user to opt-in whenever they are ready. Optionally enrolling in MFA will require some tweaks in the code, but might be a fun one to try out.
## More Flutter content[#](https://supabase.com/blog/flutter-multi-factor-authentication#more-flutter-content)
  * [Flutter Tutorial: building a Flutter chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
  * [Flutter Authentication and Authorization with RLS](https://supabase.com/blog/flutter-authentication-and-authorization-with-rls)
  * [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)
  * [Write backend code using Dart Edge](https://supabase.com/docs/guides/functions/dart-edge)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&text=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&text=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&t=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)
[Last postSupabase Beta April 20239 May 2023](https://supabase.com/blog/supabase-beta-update-april-2023)
[Next postNext steps for Postgres pluggable storage1 May 2023](https://supabase.com/blog/postgres-pluggable-strorage)
[flutter](https://supabase.com/blog/tags/flutter)[auth](https://supabase.com/blog/tags/auth)
On this page
  * [What is Multi-Factor Authentication?](https://supabase.com/blog/flutter-multi-factor-authentication#what-is-multi-factor-authentication)
  * [Why Multi-Factor Authentication matters for Flutter apps](https://supabase.com/blog/flutter-multi-factor-authentication#why-multi-factor-authentication-matters-for-flutter-apps)
  * [Building the App](https://supabase.com/blog/flutter-multi-factor-authentication#building-the-app)
  * [Conclusions and future iterations](https://supabase.com/blog/flutter-multi-factor-authentication#conclusions-and-future-iterations)
  * [More Flutter content](https://supabase.com/blog/flutter-multi-factor-authentication#more-flutter-content)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&text=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&text=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-multi-factor-authentication&t=Securing%20your%20Flutter%20apps%20with%20Multi-Factor%20Authentication)
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

