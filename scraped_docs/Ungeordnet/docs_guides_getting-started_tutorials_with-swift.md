---
url: http://supabase.com/docs/guides/getting-started/tutorials/with-swift
scraped_at: 2025-05-25T09:48:41.034112
title: Build a User Management App with Swift and SwiftUI | Supabase Docs
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
  3. [Swift](https://supabase.com/docs/guides/getting-started/tutorials/with-swift)


Build a User Management App with Swift and SwiftUI
This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - allow users to sign up and log in.
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![Supabase User Management example](https://supabase.com/docs/img/supabase-swift-demo.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/swift-user-management).
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#set-up-the-database-schema)
Now we are going to set up the database schema. We can use the "User Management Starter" quickstart in the SQL Editor, or you can just copy/paste the SQL from below and run it yourself.
DashboardSQL
When working locally you can run the following command to create a new migration file:
```

1
supabasemigrationnewuser_management_starter

```

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
-- Create a table for public profilescreatetableprofiles ( id uuid referencesauth.usersnot nullprimary key, updated_at timestamp with time zone, username textunique, full_name text, avatar_url text, website text,constraint username_length check (char_length(username) >=3));-- Set up Row Level Security (RLS)-- See https://supabase.com/docs/guides/database/postgres/row-level-security for more details.altertable profilesenablerowlevelsecurity;createpolicy"Public profiles are viewable by everyone."on profilesforselectusing (true);createpolicy"Users can insert their own profile."on profilesforinsertwithcheck ((selectauth.uid()) = id);createpolicy"Users can update own profile."on profilesforupdateusing ((selectauth.uid()) = id);-- This trigger automatically creates a profile entry when a new user signs up via Supabase Auth.-- See https://supabase.com/docs/guides/auth/managing-user-data#using-triggers for more details.createfunctionpublic.handle_new_user()returns triggerset search_path =''as $$begininsert intopublic.profiles (id, full_name, avatar_url)values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');return new;end;$$ language plpgsql security definer;createtriggeron_auth_user_createdafterinsertonauth.usersfor each rowexecuteprocedurepublic.handle_new_user();-- Set up Storage!insert intostorage.buckets (id, name)values ('avatars', 'avatars');-- Set up access controls for storage.-- See https://supabase.com/docs/guides/storage/security/access-control#policy-examples for more details.createpolicy"Avatar images are publicly accessible."onstorage.objectsforselectusing (bucket_id ='avatars');createpolicy"Anyone can upload an avatar."onstorage.objectsforinsertwithcheck (bucket_id ='avatars');createpolicy"Anyone can update their own avatar."onstorage.objectsforupdateusing ((selectauth.uid()) =owner) withcheck (bucket_id ='avatars');

```

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#building-the-app)
Let's start building the SwiftUI app from scratch.
### Create a SwiftUI app in Xcode[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#create-a-swiftui-app-in-xcode)
Open Xcode and create a new SwiftUI project.
Add the [supabase-swift](https://github.com/supabase/supabase-swift) dependency.
Add the `https://github.com/supabase/supabase-swift` package to your app. For instructions, see the [Apple tutorial on adding package dependencies](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app).
Create a helper file to initialize the Supabase client. You need the API URL and the `anon` key that you copied [earlier](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#get-the-api-keys). These variables will be exposed on the application, and that's completely fine since you have [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) enabled on your database.
Supabase.swift
```

1
2
3
4
5
6
7
importFoundationimportSupabaselet supabase =SupabaseClient( supabaseURL: URL(string:"YOUR_SUPABASE_URL")!, supabaseKey:"YOUR_SUPABASE_ANON_KEY")

```

### Set up a login view[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#set-up-a-login-view)
Set up a SwiftUI view to manage logins and sign ups. Users should be able to sign in using a magic link.
AuthView.swift
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
importSwiftUIimportSupabasestructAuthView:View {@Statevar email =""@Statevar isLoading =false@Statevar result: Result<Void, Error>?var body: some View {Form{Section{TextField("Email", text: $email)     .textContentType(.emailAddress)     .textInputAutocapitalization(.never)     .autocorrectionDisabled()}Section{Button("Sign in"){signInButtonTapped()}if isLoading {ProgressView()}}iflet result {Section{switch result {case .success:Text("Check your inbox.")case .failure(let error):Text(error.localizedDescription).foregroundStyle(.red)}}}}  .onOpenURL(perform:{ url in   Task {do {tryawait supabase.auth.session(from: url)}catch{self.result= .failure(error)}}})}funcsignInButtonTapped(){Task{   isLoading =truedefer{ isLoading =false}do {tryawait supabase.auth.signInWithOTP(      email: email,      redirectTo: URL(string:"io.supabase.user-management://login-callback"))    result = .success(())}catch{    result = .failure(error)}}}}

```

The example uses a custom `redirectTo` URL. For this to work, add a custom redirect URL to Supabase and a custom URL scheme to your SwiftUI application. Follow the guide on [implementing deep link handling](https://supabase.com/docs/guides/auth/native-mobile-deep-linking?platform=swift).
### Account view[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#account-view)
After a user is signed in, you can allow them to edit their profile details and manage their account.
Create a new view for that called `ProfileView.swift`.
ProfileView.swift
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
importSwiftUIstructProfileView:View {@Statevar username =""@Statevar fullName =""@Statevar website =""@Statevar isLoading =falsevar body: some View {NavigationStack{Form{Section{TextField("Username", text: $username)      .textContentType(.username)      .textInputAutocapitalization(.never)TextField("Full name", text: $fullName)      .textContentType(.name)TextField("Website", text: $website)      .textContentType(.URL)      .textInputAutocapitalization(.never)}Section{Button("Update profile"){updateProfileButtonTapped()}     .bold()if isLoading {ProgressView()}}}   .navigationTitle("Profile")   .toolbar(content:{    ToolbarItem(placement: .topBarLeading){     Button("Sign out", role: .destructive){      Task {try?await supabase.auth.signOut()}}}})}  .task{awaitgetInitialProfile()}}funcgetInitialProfile()async{do {let currentUser =tryawait supabase.auth.session.userlet profile: Profile =tryawait supabase    .from("profiles")    .select()    .eq("id", value: currentUser.id)    .single()    .execute()    .valueself.username= profile.username??""self.fullName= profile.fullName??""self.website= profile.website??""}catch{debugPrint(error)}}funcupdateProfileButtonTapped(){Task{   isLoading =truedefer{ isLoading =false}do {let currentUser =tryawait supabase.auth.session.usertryawait supabase     .from("profiles")     .update(      UpdateProfileParams(       username: username,       fullName: fullName,       website: website))     .eq("id", value: currentUser.id)     .execute()}catch{debugPrint(error)}}}}

```

### Models[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#models)
In `ProfileView.swift`, you used 2 model types for deserializing the response and serializing the request to Supabase. Add those in a new `Models.swift` file.
Models.swift
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
structProfile:Decodable {let username: String?let fullName: String?let website: String?enumCodingKeys:String, CodingKey {caseusernamecasefullName="full_name"casewebsite}}structUpdateProfileParams:Encodable {let username: Stringlet fullName: Stringlet website: StringenumCodingKeys:String, CodingKey {caseusernamecasefullName="full_name"casewebsite}}

```

### Launch![#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#launch)
Now that you've created all the views, add an entry point for the application. This will verify if the user has a valid session and route them to the authenticated or non-authenticated state.
Add a new `AppView.swift` file.
AppView.swift
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
importSwiftUIstructAppView:View {@Statevar isAuthenticated =falsevar body: some View {Group{if isAuthenticated {ProfileView()}else{AuthView()}}  .task{forawait state in supabase.auth.authStateChanges {if[.initialSession, .signedIn, .signedOut].contains(state.event){     isAuthenticated = state.session!=nil}}}}}

```

Update the entry point to the newly created `AppView`. Run in Xcode to launch your application in the simulator.
## Bonus: Profile photos[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#bonus-profile-photos)
Every Supabase project is configured with [Storage](https://supabase.com/docs/guides/storage) for managing large files like photos and videos.
### Add `PhotosPicker`[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#add-photospicker)
Let's add support for the user to pick an image from the library and upload it. Start by creating a new type to hold the picked avatar image:
AvatarImage.swift
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
importSwiftUIstructAvatarImage:Transferable, Equatable{let image: Imagelet data: Datastaticvar transferRepresentation: some TransferRepresentation {DataRepresentation(importedContentType: .image){ data inguardlet image =AvatarImage(data: data)else{throw TransferError.importFailed}return image}}}extensionAvatarImage{init?(data: Data){guardlet uiImage =UIImage(data: data)else{returnnil}let image =Image(uiImage: uiImage)self.init(image: image, data: data)}}enumTransferError:Error{caseimportFailed}

```

#### Add `PhotosPicker` to profile page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#add-photospicker-to-profile-page)
ProfileView.swift
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
importPhotosUIimportStorageimportSupabaseimportSwiftUIstructProfileView:View {@Statevar username =""@Statevar fullName =""@Statevar website =""@Statevar isLoading =false@Statevar imageSelection: PhotosPickerItem?@Statevar avatarImage: AvatarImage?var body: some View {NavigationStack{Form{Section{HStack{Group{iflet avatarImage {        avatarImage.image.resizable()}else{        Color.clear}}      .scaledToFit()      .frame(width:80, height:80)Spacer()PhotosPicker(selection: $imageSelection, matching: .images){Image(systemName:"pencil.circle.fill")        .symbolRenderingMode(.multicolor)        .font(.system(size:30))        .foregroundColor(.accentColor)}}}Section{TextField("Username", text: $username)      .textContentType(.username)      .textInputAutocapitalization(.never)TextField("Full name", text: $fullName)      .textContentType(.name)TextField("Website", text: $website)      .textContentType(.URL)      .textInputAutocapitalization(.never)}Section{Button("Update profile"){updateProfileButtonTapped()}     .bold()if isLoading {ProgressView()}}}   .navigationTitle("Profile")   .toolbar(content:{    ToolbarItem {     Button("Sign out", role: .destructive){      Task {try?await supabase.auth.signOut()}}}})   .onChange(of: imageSelection){_, newValue inguardlet newValue else{return}loadTransferable(from: newValue)}}  .task{awaitgetInitialProfile()}}funcgetInitialProfile()async{do {let currentUser =tryawait supabase.auth.session.userlet profile: Profile =tryawait supabase    .from("profiles")    .select()    .eq("id", value: currentUser.id)    .single()    .execute()    .value   username = profile.username??""   fullName = profile.fullName??""   website = profile.website??""iflet avatarURL = profile.avatarURL, !avatarURL.isEmpty{tryawaitdownloadImage(path: avatarURL)}}catch{debugPrint(error)}}funcupdateProfileButtonTapped(){Task{   isLoading =truedefer{ isLoading =false}do {let imageURL =tryawaituploadImage()let currentUser =tryawait supabase.auth.session.userlet updatedProfile =Profile(     username: username,     fullName: fullName,     website: website,     avatarURL: imageURL)tryawait supabase     .from("profiles")     .update(updatedProfile)     .eq("id", value: currentUser.id)     .execute()}catch{debugPrint(error)}}}privatefuncloadTransferable(fromimageSelection: PhotosPickerItem){Task{do {    avatarImage =tryawait imageSelection.loadTransferable(type: AvatarImage.self)}catch{debugPrint(error)}}}privatefuncdownloadImage(path: String)asyncthrows{let data =tryawait supabase.storage.from("avatars").download(path: path)  avatarImage =AvatarImage(data: data)}privatefuncuploadImage()asyncthrows->String?{guardlet data = avatarImage?.data else{returnnil}let filePath ="\(UUID().uuidString).jpeg"tryawait supabase.storage   .from("avatars")   .upload(    filePath,    data: data,    options: FileOptions(contentType:"image/jpeg"))return filePath}}

```

Finally, update your Models.
Models.swift
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
structProfile:Codable {let username: String?let fullName: String?let website: String?let avatarURL: String?enumCodingKeys:String, CodingKey {caseusernamecasefullName="full_name"casewebsitecaseavatarURL="avatar_url"}}

```

You no longer need the `UpdateProfileParams` struct, as you can now reuse the `Profile` struct for both request and response calls.
At this stage you have a fully functional application!
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-swift.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#get-the-api-keys)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#building-the-app)[Create a SwiftUI app in Xcode](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#create-a-swiftui-app-in-xcode)[Set up a login view](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#set-up-a-login-view)[Account view](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#account-view)[Models](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#models)[Launch!](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#launch)[Bonus: Profile photos](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#bonus-profile-photos)[Add PhotosPicker](https://supabase.com/docs/guides/getting-started/tutorials/with-swift#add-photospicker)
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



