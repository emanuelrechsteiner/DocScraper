---
url: http://supabase.com/docs/guides/getting-started/tutorials/with-angular
scraped_at: 2025-05-25T09:43:43.876615
title: Build a User Management App with Angular | Supabase Docs
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
  2. Web app demos
  3. [Angular](https://supabase.com/docs/guides/getting-started/tutorials/with-angular)


Build a User Management App with Angular
This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - allow users to sign up and log in.
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![Supabase User Management example](https://supabase.com/docs/img/user-management-demo.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/angular-user-management).
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#set-up-the-database-schema)
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

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#building-the-app)
Let's start building the Angular app from scratch.
### Initialize an Angular app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#initialize-an-angular-app)
We can use the [Angular CLI](https://angular.io/cli) to initialize an app called `supabase-angular`:
```

1
2
npxngnewsupabase-angular--routingfalse--stylecss--standalonefalsecdsupabase-angular

```

Then let's install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)
```

1
npminstall@supabase/supabase-js

```

And finally we want to save the environment variables in the `src/environments/environment.ts` file. All we need are the API URL and the `anon` key that you copied [earlier](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#get-the-api-keys). These variables will be exposed on the browser, and that's completely fine since we have [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) enabled on our Database.
src/environments/environment.ts
```

1
2
3
4
5
exportconstenvironment={production:false,supabaseUrl:'YOUR_SUPABASE_URL',supabaseKey:'YOUR_SUPABASE_KEY',}

```

Now that we have the API credentials in place, let's create a `SupabaseService` with `ng g s supabase` to initialize the Supabase client and implement functions to communicate with the Supabase API.
src/app/supabase.service.ts
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
import{Injectable}from'@angular/core'import{AuthChangeEvent,AuthSession,createClient,Session,SupabaseClient,User,}from'@supabase/supabase-js'import{environment}from'../environments/environment'exportinterfaceProfile{id?:stringusername:stringwebsite:stringavatar_url:string}@Injectable({providedIn:'root',})exportclassSupabaseService{privatesupabase:SupabaseClient_session:AuthSession|null=nullconstructor(){this.supabase=createClient(environment.supabaseUrl,environment.supabaseKey)}getsession(){this.supabase.auth.getSession().then(({data})=>{this._session=data.session})returnthis._session}profile(user:User){returnthis.supabase.from('profiles').select(`username, website, avatar_url`).eq('id',user.id).single()}authChanges(callback:(event:AuthChangeEvent,session:Session|null)=>void){returnthis.supabase.auth.onAuthStateChange(callback)}signIn(email:string){returnthis.supabase.auth.signInWithOtp({email})}signOut(){returnthis.supabase.auth.signOut()}updateProfile(profile:Profile){constupdate={...profile,updated_at:newDate(),}returnthis.supabase.from('profiles').upsert(update)}downLoadImage(path:string){returnthis.supabase.storage.from('avatars').download(path)}uploadAvatar(filePath:string,file:File){returnthis.supabase.storage.from('avatars').upload(filePath,file)}}

```

Optionally, update [src/styles.css](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/angular-user-management/src/styles.css) to style the app.
### Set up a login component[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#set-up-a-login-component)
Let's set up an Angular component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords. Create an `AuthComponent` with `ng g c auth` Angular CLI command.
src/app/auth/auth.component.tssrc/app/auth/auth.component.html
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
import{Component}from'@angular/core'import{FormBuilder}from'@angular/forms'import{SupabaseService}from'../supabase.service'@Component({selector:'app-auth',templateUrl:'./auth.component.html',styleUrls:['./auth.component.css'],})exportclassAuthComponent{loading=falsesignInForm=this.formBuilder.group({email:'',})constructor(privatereadonlysupabase:SupabaseService,privatereadonlyformBuilder:FormBuilder){}asynconSubmit():Promise<void>{try{this.loading=trueconstemail=this.signInForm.value.emailasstringconst{error}=awaitthis.supabase.signIn(email)if (error) throwerroralert('Check your email for the login link!')}catch (error) {if (errorinstanceofError) {alert(error.message)}}finally{this.signInForm.reset()this.loading=false}}}

```

### Account page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#account-page)
Users also need a way to edit their profile details and manage their accounts after signing in. Create an `AccountComponent` with the `ng g c account` Angular CLI command.
src/app/account/account.component.tssrc/app/account/account.component.html
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
import{Component,Input,OnInit}from'@angular/core'import{FormBuilder}from'@angular/forms'import{AuthSession}from'@supabase/supabase-js'import{Profile,SupabaseService}from'../supabase.service'@Component({selector:'app-account',templateUrl:'./account.component.html',styleUrls:['./account.component.css'],})exportclassAccountComponentimplementsOnInit{loading=falseprofile!:Profile@Input()session!:AuthSessionupdateProfileForm=this.formBuilder.group({username:'',website:'',avatar_url:'',})constructor(privatereadonlysupabase:SupabaseService,privateformBuilder:FormBuilder){}asyncngOnInit():Promise<void>{awaitthis.getProfile()const{username,website,avatar_url}=this.profilethis.updateProfileForm.patchValue({username,website,avatar_url,})}asyncgetProfile(){try{this.loading=trueconst{user}=this.sessionconst{data:profile,error,status}=awaitthis.supabase.profile(user)if (error&&status!==406) {throwerror}if (profile) {this.profile=profile}}catch (error) {if (errorinstanceofError) {alert(error.message)}}finally{this.loading=false}}asyncupdateProfile():Promise<void>{try{this.loading=trueconst{user}=this.sessionconstusername=this.updateProfileForm.value.usernameasstringconstwebsite=this.updateProfileForm.value.websiteasstringconstavatar_url=this.updateProfileForm.value.avatar_urlasstringconst{error}=awaitthis.supabase.updateProfile({id:user.id,username,website,avatar_url,})if (error) throwerror}catch (error) {if (errorinstanceofError) {alert(error.message)}}finally{this.loading=false}}asyncsignOut(){awaitthis.supabase.signOut()}}

```

### Launch![#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#launch)
Now that we have all the components in place, let's update `AppComponent`:
src/app/app.component.tssrc/app/app.component.html
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
import{Component,OnInit}from'@angular/core'import{SupabaseService}from'./supabase.service'@Component({selector:'app-root',templateUrl:'./app.component.html',styleUrls:['./app.component.css'],})exportclassAppComponentimplementsOnInit{title='angular-user-management'session=this.supabase.sessionconstructor(privatereadonlysupabase:SupabaseService){}ngOnInit(){this.supabase.authChanges((_,session)=> (this.session=session))}}

```

`app.module.ts` also needs to be modified to include the `ReactiveFormsModule` from the `@angular/forms` package.
src/app/app.module.ts
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
import{NgModule}from'@angular/core'import{BrowserModule}from'@angular/platform-browser'import{AppComponent}from'./app.component'import{AuthComponent}from'./auth/auth.component'import{AccountComponent}from'./account/account.component'import{ReactiveFormsModule}from'@angular/forms'import{AvatarComponent}from'./avatar/avatar.component'@NgModule({declarations:[AppComponent,AuthComponent,AccountComponent,AvatarComponent],imports:[BrowserModule,ReactiveFormsModule],providers:[],bootstrap:[AppComponent],})exportclassAppModule{}

```

Once that's done, run this in a terminal window:
```

1
npmrunstart

```

And then open the browser to [localhost:4200](http://localhost:4200) and you should see the completed app.
![Supabase Angular](https://supabase.com/docs/img/supabase-angular-demo.png)
## Bonus: Profile photos[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#bonus-profile-photos)
Every Supabase project is configured with [Storage](https://supabase.com/docs/guides/storage) for managing large files like photos and videos.
### Create an upload widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#create-an-upload-widget)
Let's create an avatar for the user so that they can upload a profile photo. Create an `AvatarComponent` with `ng g c avatar` Angular CLI command.
src/app/avatar/avatar.component.tssrc/app/avatar/avatar.component.html
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
import{Component,EventEmitter,Input,Output}from'@angular/core'import{SafeResourceUrl,DomSanitizer}from'@angular/platform-browser'import{SupabaseService}from'../supabase.service'@Component({selector:'app-avatar',templateUrl:'./avatar.component.html',styleUrls:['./avatar.component.css'],})exportclassAvatarComponent{_avatarUrl:SafeResourceUrl|undefineduploading=false@Input()setavatarUrl(url:string|null){if (url) {this.downloadImage(url)}}@Output() upload=newEventEmitter<string>()constructor(privatereadonlysupabase:SupabaseService,privatereadonlydom:DomSanitizer){}asyncdownloadImage(path:string){try{const{data}=awaitthis.supabase.downLoadImage(path)if (datainstanceofBlob) {this._avatarUrl=this.dom.bypassSecurityTrustResourceUrl(URL.createObjectURL(data))}}catch (error) {if (errorinstanceofError) {console.error('Error downloading image: ',error.message)}}}asyncuploadAvatar(event:any){try{this.uploading=trueif (!event.target.files||event.target.files.length===0) {thrownewError('You must select an image to upload.')}constfile=event.target.files[0]constfileExt=file.name.split('.').pop()constfilePath=`${Math.random()}.${fileExt}`awaitthis.supabase.uploadAvatar(filePath,file)this.upload.emit(filePath)}catch (error) {if (errorinstanceofError) {alert(error.message)}}finally{this.uploading=false}}}

```

### Add the new widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#add-the-new-widget)
And then we can add the widget on top of the `AccountComponent` HTML template:
src/app/account.component.html
```

1
2
3
4
<form [formGroup]="updateProfileForm"(ngSubmit)="updateProfile()"class="form-widget"><app-avatar [avatarUrl]="this.avatarUrl"(upload)="updateAvatar($event)"></app-avatar><!-- input fields --></form>

```

And add an `updateAvatar` function along with an `avatarUrl` getter to the `AccountComponent` typescript file:
src/app/account.component.ts
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
@Component({selector:'app-account',templateUrl:'./account.component.html',styleUrls:['./account.component.css'],})exportclassAccountComponentimplementsOnInit{// ...getavatarUrl(){returnthis.updateProfileForm.value.avatar_urlasstring}asyncupdateAvatar(event:string):Promise<void>{this.updateProfileForm.patchValue({avatar_url:event,})awaitthis.updateProfile()}// ...}

```

At this stage you have a fully functional application!
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-angular.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#get-the-api-keys)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#building-the-app)[Initialize an Angular app](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#initialize-an-angular-app)[Set up a login component](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#set-up-a-login-component)[Account page](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#account-page)[Launch!](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#launch)[Bonus: Profile photos](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#bonus-profile-photos)[Create an upload widget](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#create-an-upload-widget)[Add the new widget](https://supabase.com/docs/guides/getting-started/tutorials/with-angular#add-the-new-widget)
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



