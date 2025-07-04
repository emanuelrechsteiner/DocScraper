---
url: https://supabase.com/docs/guides/getting-started/tutorials/with-flutter
scraped_at: 2025-05-25T08:43:40.577878
title: Build a User Management App with Flutter | Supabase Docs
---

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Main menu
[Start with Supabase](https://supabase.com/docs/guides/getting-started)
  * [Features](https://supabase.com/docs/guides/getting-started/features)
  * [Architecture](https://supabase.com/docs/guides/getting-started/architecture)
Framework Quickstarts
  * [Next.js](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
  * [React](https://supabase.com/docs/guides/getting-started/quickstarts/reactjs)
  * [Nuxt](https://supabase.com/docs/guides/getting-started/quickstarts/nuxtjs)
  * [Vue](https://supabase.com/docs/guides/getting-started/quickstarts/vue)
  * [Hono](https://supabase.com/docs/guides/getting-started/quickstarts/hono)
  * [Flutter](https://supabase.com/docs/guides/getting-started/quickstarts/flutter)
  * [iOS SwiftUI](https://supabase.com/docs/guides/getting-started/quickstarts/ios-swiftui)
  * [Android Kotlin](https://supabase.com/docs/guides/getting-started/quickstarts/kotlin)
  * [SvelteKit](https://supabase.com/docs/guides/getting-started/quickstarts/sveltekit)
  * [Laravel PHP](https://supabase.com/docs/guides/getting-started/quickstarts/laravel)
  * [Ruby on Rails](https://supabase.com/docs/guides/getting-started/quickstarts/ruby-on-rails)
  * [SolidJS](https://supabase.com/docs/guides/getting-started/quickstarts/solidjs)
  * [RedwoodJS](https://supabase.com/docs/guides/getting-started/quickstarts/redwoodjs)
  * [refine](https://supabase.com/docs/guides/getting-started/quickstarts/refine)
Web app demos
  * [Next.js](https://supabase.com/docs/guides/getting-started/tutorials/with-nextjs)
  * [React](https://supabase.com/docs/guides/getting-started/tutorials/with-react)
  * [Vue 3](https://supabase.com/docs/guides/getting-started/tutorials/with-vue-3)
  * [Nuxt 3](https://supabase.com/docs/guides/getting-started/tutorials/with-nuxt-3)
  * [Angular](https://supabase.com/docs/guides/getting-started/tutorials/with-angular)
  * [RedwoodJS](https://supabase.com/docs/guides/getting-started/tutorials/with-redwoodjs)
  * [SolidJS](https://supabase.com/docs/guides/getting-started/tutorials/with-solidjs)
  * [Svelte](https://supabase.com/docs/guides/getting-started/tutorials/with-svelte)
  * [SvelteKit](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit)
  * [refine](https://supabase.com/docs/guides/getting-started/tutorials/with-refine)
Mobile tutorials
  * [Flutter](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter)
  * [Expo React Native](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native)
  * [Android Kotlin](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin)
  * [Ionic React](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-react)
  * [Ionic Vue](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue)
  * [Ionic Angular](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular)
  * [Swift](https://supabase.com/docs/guides/getting-started/tutorials/with-swift)
AI Tools
  * [Prompts](https://supabase.com/docs/guides/getting-started/ai-prompts)
  * [Model context protocol (MCP)](https://supabase.com/docs/guides/getting-started/mcp)


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Getting Started
  1. [Start with Supabase](https://supabase.com/docs/guides/getting-started)
  2. Mobile tutorials
  3. [Flutter](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter)


Build a User Management App with Flutter
This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - allow users to sign up and log in.
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![Supabase User Management example](https://supabase.com/docs/img/supabase-flutter-demo.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/flutter-user-management).
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#set-up-the-database-schema)
Now we are going to set up the database schema. We can use the "User Management Starter" quickstart in the SQL Editor, or you can just copy/paste the SQL from below and run it yourself.
DashboardSQL
  1. Go to the [SQL Editor](https://supabase.com/dashboard/project/_/sql) page in the Dashboard.
  2. Click **User Management Starter**.
  3. Click **Run**.


You can pull the database schema down to your local project by running the `db pull` command. Read the [local development docs](https://supabase.com/docs/guides/cli/local-development#link-your-project) for detailed instructions.
```

1
2
3
supabaselink--project-ref<project-id># You can get <project-id> from your project's dashboard URL: https://supabase.com/dashboard/project/<project-id>supabasedbpull

```

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#building-the-app)
Let's start building the Flutter app from scratch.
### Initialize a Flutter app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#initialize-a-flutter-app)
We can use [`flutter create`](https://flutter.dev/docs/get-started/test-drive) to initialize an app called `supabase_quickstart`:
```

1
fluttercreatesupabase_quickstart

```

Then let's install the only additional dependency: [`supabase_flutter`](https://pub.dev/packages/supabase_flutter)
Copy and paste the following line in your pubspec.yaml to install the package:
```

1
supabase_flutter:^2.0.0

```

Run `flutter pub get` to install the dependencies.
### Setup deep links[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#setup-deep-links)
Now that we have the dependencies installed let's setup deep links. Setting up deep links is required to bring back the user to the app when they click on the magic link to sign in. We can setup deep links with just a minor tweak on our Flutter application.
We have to use `io.supabase.flutterquickstart` as the scheme. In this example, we will use `login-callback` as the host for our deep link, but you can change it to whatever you would like.
First, add `io.supabase.flutterquickstart://login-callback/` as a new [redirect URL](https://supabase.com/dashboard/project/_/auth/url-configuration) in the Dashboard.
![Supabase console deep link setting](https://supabase.com/docs/img/deeplink-setting.png)
That is it on Supabase's end and the rest are platform specific settings:
iOSAndroidWeb
Edit the `ios/Runner/Info.plist` file.
Add `CFBundleURLTypes` to enable deep linking:
ios/Runner/Info.plist"
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
<!-- ... other tags --><plist><dict><!-- ... other tags --><!-- Add this array for Deep Links --><key>CFBundleURLTypes</key><array><dict><key>CFBundleTypeRole</key><string>Editor</string><key>CFBundleURLSchemes</key><array><string>io.supabase.flutterquickstart</string></array></dict></array><!-- ... other tags --></dict></plist>

```

### Main function[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#main-function)
Now that we have deep links ready let's initialize the Supabase client inside our `main` function with the API credentials that you copied [earlier](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#get-the-api-keys). These variables will be exposed on the app, and that's completely fine since we have [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) enabled on our Database.
lib/main.dart
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
import'package:flutter/material.dart';import'package:supabase_flutter/supabase_flutter.dart';Future<void> main() async {awaitSupabase.initialize(  url:'YOUR_SUPABASE_URL',  anonKey:'YOUR_SUPABASE_ANON_KEY', );runApp(constMyApp());}final supabase =Supabase.instance.client;classMyAppextendsStatelessWidget {constMyApp({super.key});@overrideWidgetbuild(BuildContext context) {returnconstMaterialApp(title:'Supabase Flutter'); }}extensionContextExtensiononBuildContext {voidshowSnackBar(String message, {bool isError =false}) {ScaffoldMessenger.of(this).showSnackBar(SnackBar(    content:Text(message),    backgroundColor: isError?Theme.of(this).colorScheme.error:Theme.of(this).snackBarTheme.backgroundColor,   ),  ); }}

```

Notice that we have a `showSnackBar` extension method that we will use to show snack bars in the app. You could define this method in a separate file and import it where needed, but for simplicity, we will define it here.
### Set up a login page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#set-up-a-login-page)
Let's create a Flutter widget to manage logins and sign ups. We will use Magic Links, so users can sign in with their email without using passwords.
Notice that this page sets up a listener on the user's auth state using `onAuthStateChange`. A new event will fire when the user comes back to the app by clicking their magic link, which this page can catch and redirect the user accordingly.
lib/pages/login_page.dart
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
import'dart:async';import'package:flutter/foundation.dart';import'package:flutter/material.dart';import'package:supabase_flutter/supabase_flutter.dart';import'package:supabase_quickstart/main.dart';import'package:supabase_quickstart/pages/account_page.dart';classLoginPageextendsStatefulWidget {constLoginPage({super.key});@overrideState<LoginPage> createState() =>_LoginPageState();}class_LoginPageStateextendsState<LoginPage> {bool _isLoading =false;bool _redirecting =false;latefinalTextEditingController _emailController =TextEditingController();latefinalStreamSubscription<AuthState> _authStateSubscription;Future<void> _signIn() async {try {setState(() {    _isLoading =true;   });await supabase.auth.signInWithOtp(    email: _emailController.text.trim(),    emailRedirectTo:      kIsWeb ?null:'io.supabase.flutterquickstart://login-callback/',   );if (mounted) {    context.showSnackBar('Check your email for a login link!');    _emailController.clear();   }  } onAuthExceptioncatch (error) {if (mounted) context.showSnackBar(error.message, isError:true);  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  } finally {if (mounted) {setState(() {     _isLoading =false;    });   }  } }@overridevoidinitState() {  _authStateSubscription = supabase.auth.onAuthStateChange.listen(   (data) {if (_redirecting) return;final session = data.session;if (session !=null) {     _redirecting =true;Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (context) =>constAccountPage()),     );    }   },   onError: (error) {if (error isAuthException) {     context.showSnackBar(error.message, isError:true);    } else {     context.showSnackBar('Unexpected error occurred', isError:true);    }   },  );super.initState(); }@overridevoiddispose() {  _emailController.dispose();  _authStateSubscription.cancel();super.dispose(); }@overrideWidgetbuild(BuildContext context) {returnScaffold(   appBar:AppBar(title:constText('Sign In')),   body:ListView(    padding:constEdgeInsets.symmetric(vertical:18, horizontal:12),    children: [constText('Sign in via the magic link with your email below'),constSizedBox(height:18),TextFormField(      controller: _emailController,      decoration:constInputDecoration(labelText:'Email'),     ),constSizedBox(height:18),ElevatedButton(      onPressed: _isLoading ?null: _signIn,      child:Text(_isLoading ?'Sending...':'Send Magic Link'),     ),    ],   ),  ); }}

```

### Set up account page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#set-up-account-page)
After a user is signed in we can allow them to edit their profile details and manage their account. Let's create a new widget called `account_page.dart` for that.
lib/pages/account_page.dart"
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
import'package:flutter/material.dart';import'package:supabase_flutter/supabase_flutter.dart';import'package:supabase_quickstart/main.dart';import'package:supabase_quickstart/pages/login_page.dart';classAccountPageextendsStatefulWidget {constAccountPage({super.key});@overrideState<AccountPage> createState() =>_AccountPageState();}class_AccountPageStateextendsState<AccountPage> {final _usernameController =TextEditingController();final _websiteController =TextEditingController();String? _avatarUrl;var _loading =true;/// Called once a user id is received within `onAuthenticated()`Future<void> _getProfile() async {setState(() {   _loading =true;  });try {final userId = supabase.auth.currentSession!.user.id;final data =await supabase.from('profiles').select().eq('id', userId).single();   _usernameController.text = (data['username'] ??'') asString;   _websiteController.text = (data['website'] ??'') asString;   _avatarUrl = (data['avatar_url'] ??'') asString;  } onPostgrestExceptioncatch (error) {if (mounted) context.showSnackBar(error.message, isError:true);  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  } finally {if (mounted) {setState(() {     _loading =false;    });   }  } }/// Called when user taps `Update` buttonFuture<void> _updateProfile() async {setState(() {   _loading =true;  });final userName = _usernameController.text.trim();final website = _websiteController.text.trim();final user = supabase.auth.currentUser;final updates = {'id': user!.id,'username': userName,'website': website,'updated_at':DateTime.now().toIso8601String(),  };try {await supabase.from('profiles').upsert(updates);if (mounted) context.showSnackBar('Successfully updated profile!');  } onPostgrestExceptioncatch (error) {if (mounted) context.showSnackBar(error.message, isError:true);  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  } finally {if (mounted) {setState(() {     _loading =false;    });   }  } }Future<void> _signOut() async {try {await supabase.auth.signOut();  } onAuthExceptioncatch (error) {if (mounted) context.showSnackBar(error.message, isError:true);  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  } finally {if (mounted) {Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) =>constLoginPage()),    );   }  } }@overridevoidinitState() {super.initState();_getProfile(); }@overridevoiddispose() {  _usernameController.dispose();  _websiteController.dispose();super.dispose(); }@overrideWidgetbuild(BuildContext context) {returnScaffold(   appBar:AppBar(title:constText('Profile')),   body:ListView(    padding:constEdgeInsets.symmetric(vertical:18, horizontal:12),    children: [TextFormField(      controller: _usernameController,      decoration:constInputDecoration(labelText:'User Name'),     ),constSizedBox(height:18),TextFormField(      controller: _websiteController,      decoration:constInputDecoration(labelText:'Website'),     ),constSizedBox(height:18),ElevatedButton(      onPressed: _loading ?null: _updateProfile,      child:Text(_loading ?'Saving...':'Update'),     ),constSizedBox(height:18),TextButton(onPressed: _signOut, child:constText('Sign Out')),    ],   ),  ); }}

```

### Launch![#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#launch)
Now that we have all the components in place, let's update `lib/main.dart`. The `home` of the `MaterialApp`, meaning the initial page shown to the user, will be the `LoginPage` if the user is not authenticated, and the `AccountPage` if the user is authenticated. We also included some theming to make the app look a bit nicer.
lib/main.dart
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
import'package:flutter/material.dart';import'package:supabase_flutter/supabase_flutter.dart';import'package:supabase_quickstart/pages/account_page.dart';import'package:supabase_quickstart/pages/login_page.dart';Future<void> main() async {awaitSupabase.initialize(  url:'YOUR_SUPABASE_URL',  anonKey:'YOUR_SUPABASE_ANON_KEY', );runApp(constMyApp());}final supabase =Supabase.instance.client;classMyAppextendsStatelessWidget {constMyApp({super.key});@overrideWidgetbuild(BuildContext context) {returnMaterialApp(   title:'Supabase Flutter',   theme:ThemeData.dark().copyWith(    primaryColor:Colors.green,    textButtonTheme:TextButtonThemeData(     style:TextButton.styleFrom(      foregroundColor:Colors.green,     ),    ),    elevatedButtonTheme:ElevatedButtonThemeData(     style:ElevatedButton.styleFrom(      foregroundColor:Colors.white,      backgroundColor:Colors.green,     ),    ),   ),   home: supabase.auth.currentSession ==null?constLoginPage():constAccountPage(),  ); }}extensionContextExtensiononBuildContext {voidshowSnackBar(String message, {bool isError =false}) {ScaffoldMessenger.of(this).showSnackBar(SnackBar(    content:Text(message),    backgroundColor: isError?Theme.of(this).colorScheme.error:Theme.of(this).snackBarTheme.backgroundColor,   ),  ); }}

```

Once that's done, run this in a terminal window to launch on Android or iOS:
```

1
flutterrun

```

Or for web, run the following command to launch it on `localhost:3000`
```

1
flutterrun-dweb-server--web-hostnamelocalhost--web-port3000

```

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.
![Supabase User Management example](https://supabase.com/docs/img/supabase-flutter-account-page.png)
## Bonus: Profile photos[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#bonus-profile-photos)
Every Supabase project is configured with [Storage](https://supabase.com/docs/guides/storage) for managing large files like photos and videos.
### Making sure we have a public bucket[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#making-sure-we-have-a-public-bucket)
We will be storing the image as a publicly sharable image. Make sure your `avatars` bucket is set to public, and if it is not, change the publicity by clicking the dot menu that appears when you hover over the bucket name. You should see an orange `Public` badge next to your bucket name if your bucket is set to public.
### Adding image uploading feature to account page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#adding-image-uploading-feature-to-account-page)
We will use [`image_picker`](https://pub.dev/packages/image_picker) plugin to select an image from the device.
Add the following line in your pubspec.yaml file to install `image_picker`:
```

1
image_picker:^1.0.5

```

Using [`image_picker`](https://pub.dev/packages/image_picker) requires some additional preparation depending on the platform. Follow the instruction on README.md of [`image_picker`](https://pub.dev/packages/image_picker) on how to set it up for the platform you are using.
Once you are done with all of the above, it is time to dive into coding.
### Create an upload widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#create-an-upload-widget)
Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:
lib/components/avatar.dart
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
import'package:flutter/material.dart';import'package:image_picker/image_picker.dart';import'package:supabase_flutter/supabase_flutter.dart';import'package:supabase_quickstart/main.dart';classAvatarextendsStatefulWidget {constAvatar({super.key,requiredthis.imageUrl,requiredthis.onUpload, });finalString? imageUrl;finalvoidFunction(String) onUpload;@overrideState<Avatar> createState() =>_AvatarState();}class_AvatarStateextendsState<Avatar> {bool _isLoading =false;@overrideWidgetbuild(BuildContext context) {returnColumn(   children: [if (widget.imageUrl ==null|| widget.imageUrl!.isEmpty)Container(      width:150,      height:150,      color:Colors.grey,      child:constCenter(       child:Text('No Image'),      ),     )elseImage.network(      widget.imageUrl!,      width:150,      height:150,      fit:BoxFit.cover,     ),ElevatedButton(     onPressed: _isLoading ?null: _upload,     child:constText('Upload'),    ),   ],  ); }Future<void> _upload() async {final picker =ImagePicker();final imageFile =await picker.pickImage(   source:ImageSource.gallery,   maxWidth:300,   maxHeight:300,  );if (imageFile ==null) {return;  }setState(() => _isLoading =true);try {final bytes =await imageFile.readAsBytes();final fileExt = imageFile.path.split('.').last;final fileName ='${DateTime.now().toIso8601String()}.$fileExt';final filePath = fileName;await supabase.storage.from('avatars').uploadBinary(      filePath,      bytes,      fileOptions:FileOptions(contentType: imageFile.mimeType),     );final imageUrlResponse =await supabase.storage.from('avatars').createSignedUrl(filePath,60*60*24*365*10);   widget.onUpload(imageUrlResponse);  } onStorageExceptioncatch (error) {if (mounted) {    context.showSnackBar(error.message, isError:true);   }  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  }setState(() => _isLoading =false); }}

```

### Add the new widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#add-the-new-widget)
And then we can add the widget to the Account page as well as some logic to update the `avatar_url` whenever the user uploads a new avatar.
lib/pages/account_page.dart
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
import'package:flutter/material.dart';import'package:supabase_flutter/supabase_flutter.dart';import'package:supabase_quickstart/components/avatar.dart';import'package:supabase_quickstart/main.dart';import'package:supabase_quickstart/pages/login_page.dart';classAccountPageextendsStatefulWidget {constAccountPage({super.key});@overrideState<AccountPage> createState() =>_AccountPageState();}class_AccountPageStateextendsState<AccountPage> {final _usernameController =TextEditingController();final _websiteController =TextEditingController();String? _avatarUrl;var _loading =true;/// Called once a user id is received within `onAuthenticated()`Future<void> _getProfile() async {setState(() {   _loading =true;  });try {final userId = supabase.auth.currentSession!.user.id;final data =await supabase.from('profiles').select().eq('id', userId).single();   _usernameController.text = (data['username'] ??'') asString;   _websiteController.text = (data['website'] ??'') asString;   _avatarUrl = (data['avatar_url'] ??'') asString;  } onPostgrestExceptioncatch (error) {if (mounted) context.showSnackBar(error.message, isError:true);  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  } finally {if (mounted) {setState(() {     _loading =false;    });   }  } }/// Called when user taps `Update` buttonFuture<void> _updateProfile() async {setState(() {   _loading =true;  });final userName = _usernameController.text.trim();final website = _websiteController.text.trim();final user = supabase.auth.currentUser;final updates = {'id': user!.id,'username': userName,'website': website,'updated_at':DateTime.now().toIso8601String(),  };try {await supabase.from('profiles').upsert(updates);if (mounted) context.showSnackBar('Successfully updated profile!');  } onPostgrestExceptioncatch (error) {if (mounted) context.showSnackBar(error.message, isError:true);  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  } finally {if (mounted) {setState(() {     _loading =false;    });   }  } }Future<void> _signOut() async {try {await supabase.auth.signOut();  } onAuthExceptioncatch (error) {if (mounted) context.showSnackBar(error.message, isError:true);  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  } finally {if (mounted) {Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) =>constLoginPage()),    );   }  } }/// Called when image has been uploaded to Supabase storage from within Avatar widgetFuture<void> _onUpload(String imageUrl) async {try {final userId = supabase.auth.currentUser!.id;await supabase.from('profiles').upsert({'id': userId,'avatar_url': imageUrl,   });if (mounted) {constSnackBar(     content:Text('Updated your profile image!'),    );   }  } onPostgrestExceptioncatch (error) {if (mounted) context.showSnackBar(error.message, isError:true);  } catch (error) {if (mounted) {    context.showSnackBar('Unexpected error occurred', isError:true);   }  }if (!mounted) {return;  }setState(() {   _avatarUrl = imageUrl;  }); }@overridevoidinitState() {super.initState();_getProfile(); }@overridevoiddispose() {  _usernameController.dispose();  _websiteController.dispose();super.dispose(); }@overrideWidgetbuild(BuildContext context) {returnScaffold(   appBar:AppBar(title:constText('Profile')),   body:ListView(    padding:constEdgeInsets.symmetric(vertical:18, horizontal:12),    children: [Avatar(      imageUrl: _avatarUrl,      onUpload: _onUpload,     ),constSizedBox(height:18),TextFormField(      controller: _usernameController,      decoration:constInputDecoration(labelText:'User Name'),     ),constSizedBox(height:18),TextFormField(      controller: _websiteController,      decoration:constInputDecoration(labelText:'Website'),     ),constSizedBox(height:18),ElevatedButton(      onPressed: _loading ?null: _updateProfile,      child:Text(_loading ?'Saving...':'Update'),     ),constSizedBox(height:18),TextButton(onPressed: _signOut, child:constText('Sign Out')),    ],   ),  ); }}

```

Congratulations, you've built a fully functional user management app using Flutter and Supabase!
## See also[#](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#see-also)
  * [Flutter Tutorial: building a Flutter chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
  * [Flutter Tutorial - Part 2: Authentication and Authorization with RLS](https://supabase.com/blog/flutter-authentication-and-authorization-with-rls)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-flutter.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2Fr7ysVtZ5Row%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#get-the-api-keys)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#building-the-app)[Initialize a Flutter app](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#initialize-a-flutter-app)[Setup deep links](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#setup-deep-links)[Main function](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#main-function)[Set up a login page](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#set-up-a-login-page)[Set up account page](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#set-up-account-page)[Launch!](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#launch)[Bonus: Profile photos](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#bonus-profile-photos)[Making sure we have a public bucket](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#making-sure-we-have-a-public-bucket)[Adding image uploading feature to account page](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#adding-image-uploading-feature-to-account-page)[Create an upload widget](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#create-an-upload-widget)[Add the new widget](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#add-the-new-widget)[See also](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter#see-also)
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings



