---
url: https://supabase.com/docs/guides/with-ionic-angular
scraped_at: 2025-05-25T09:37:47.416402
title: Build a User Management App with Ionic Angular | Supabase Docs
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
  3. [Ionic Angular](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular)


Build a User Management App with Ionic Angular
This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - allow users to sign up and log in.
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![Supabase User Management example](https://supabase.com/docs/img/ionic-demos/ionic-angular-account.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/mhartington/supabase-ionic-angular).
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#set-up-the-database-schema)
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

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#building-the-app)
Let's start building the Angular app from scratch.
### Initialize an Ionic Angular app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#initialize-an-ionic-angular-app)
We can use the [Ionic CLI](https://ionicframework.com/docs/cli) to initialize an app called `supabase-ionic-angular`:
```

1
2
3
npminstall-g@ionic/cliionicstartsupabase-ionic-angularblank--typeangularcdsupabase-ionic-angular

```

Then let's install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)
```

1
npminstall@supabase/supabase-js

```

And finally, we want to save the environment variables in the `src/environments/environment.ts` file. All we need are the API URL and the `anon` key that you copied [earlier](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#get-the-api-keys). These variables will be exposed on the browser, and that's completely fine since we have [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) enabled on our Database.
environment.ts
```

1
2
3
4
5
exportconstenvironment={production:false,supabaseUrl:'YOUR_SUPABASE_URL',supabaseKey:'YOUR_SUPABASE_KEY',}

```

Now that we have the API credentials in place, let's create a `SupabaseService` with `ionic g s supabase` to initialize the Supabase client and implement functions to communicate with the Supabase API.
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
74
75
76
77
78
79
80
import{Injectable}from'@angular/core'import{LoadingController,ToastController}from'@ionic/angular'import{AuthChangeEvent,createClient,Session,SupabaseClient}from'@supabase/supabase-js'import{environment}from'../environments/environment'exportinterfaceProfile{username:stringwebsite:stringavatar_url:string}@Injectable({providedIn:'root',})exportclassSupabaseService{privatesupabase:SupabaseClientconstructor(privateloadingCtrl:LoadingController,privatetoastCtrl:ToastController){this.supabase=createClient(environment.supabaseUrl,environment.supabaseKey)}getuser(){returnthis.supabase.auth.getUser().then(({data})=>data?.user)}getsession(){returnthis.supabase.auth.getSession().then(({data})=>data?.session)}getprofile(){returnthis.user.then((user)=>user?.id).then((id)=>this.supabase.from('profiles').select(`username, website, avatar_url`).eq('id',id).single()   )}authChanges(callback:(event:AuthChangeEvent,session:Session|null)=>void){returnthis.supabase.auth.onAuthStateChange(callback)}signIn(email:string){returnthis.supabase.auth.signInWithOtp({email})}signOut(){returnthis.supabase.auth.signOut()}asyncupdateProfile(profile:Profile){constuser=awaitthis.userconstupdate={...profile,id:user?.id,updated_at:newDate(),}returnthis.supabase.from('profiles').upsert(update)}downLoadImage(path:string){returnthis.supabase.storage.from('avatars').download(path)}uploadAvatar(filePath:string,file:File){returnthis.supabase.storage.from('avatars').upload(filePath,file)}asynccreateNotice(message:string){consttoast=awaitthis.toastCtrl.create({message,duration:5000})awaittoast.present()}createLoader(){returnthis.loadingCtrl.create()}}

```

### Set up a login route[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#set-up-a-login-route)
Let's set up a route to manage logins and signups. We'll use Magic Links so users can sign in with their email without using passwords. Create a `LoginPage` with the `ionic g page login` Ionic CLI command.
This guide will show the template inline, but the example app will have `templateUrl`s
src/app/login/login.page.ts
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
import{Component,OnInit}from'@angular/core'import{SupabaseService}from'../supabase.service'@Component({selector:'app-login',template:`  <ion-header>   <ion-toolbar>    <ion-title>Login</ion-title>   </ion-toolbar>  </ion-header>  <ion-content>   <div class="ion-padding">    <h1>Supabase + Ionic Angular</h1>    <p>Sign in via magic link with your email below</p>   </div>   <ion-list inset="true">    <form (ngSubmit)="handleLogin($event)">     <ion-item>      <ion-label position="stacked">Email</ion-label>      <ion-input [(ngModel)]="email" name="email" autocomplete type="email"></ion-input>     </ion-item>     <div class="ion-text-center">      <ion-button type="submit" fill="clear">Login</ion-button>     </div>    </form>   </ion-list>  </ion-content>`,styleUrls:['./login.page.scss'],})exportclassLoginPage{email=''constructor(privatereadonlysupabase:SupabaseService){}asynchandleLogin(event:any){event.preventDefault()constloader=awaitthis.supabase.createLoader()awaitloader.present()try{const{error}=awaitthis.supabase.signIn(this.email)if (error) {throwerror}awaitloader.dismiss()awaitthis.supabase.createNotice('Check your email for the login link!')}catch(error:any){awaitloader.dismiss()awaitthis.supabase.createNotice(error.error_description||error.message)}}}

```

### Account page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#account-page)
After a user is signed in, we can allow them to edit their profile details and manage their account. Create an `AccountComponent` with `ionic g page account` Ionic CLI command.
src/app/account.page.ts
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
import{Component,OnInit}from'@angular/core'import{Router}from'@angular/router'import{Profile,SupabaseService}from'../supabase.service'@Component({selector:'app-account',template:`  <ion-header>   <ion-toolbar>    <ion-title>Account</ion-title>   </ion-toolbar>  </ion-header>  <ion-content>   <form>    <ion-item>     <ion-label position="stacked">Email</ion-label>     <ion-input type="email" name="email" [(ngModel)]="email" readonly></ion-input>    </ion-item>    <ion-item>     <ion-label position="stacked">Name</ion-label>     <ion-input type="text" name="username" [(ngModel)]="profile.username"></ion-input>    </ion-item>    <ion-item>     <ion-label position="stacked">Website</ion-label>     <ion-input type="url" name="website" [(ngModel)]="profile.website"></ion-input>    </ion-item>    <div class="ion-text-center">     <ion-button fill="clear" (click)="updateProfile()">Update Profile</ion-button>    </div>   </form>   <div class="ion-text-center">    <ion-button fill="clear" (click)="signOut()">Log Out</ion-button>   </div>  </ion-content>`,styleUrls:['./account.page.scss'],})exportclassAccountPageimplementsOnInit{profile:Profile={username:'',avatar_url:'',website:'',}email=''constructor(privatereadonlysupabase:SupabaseService,privaterouter:Router){}ngOnInit(){this.getEmail()this.getProfile()}asyncgetEmail(){this.email=awaitthis.supabase.user.then((user)=>user?.email||'')}asyncgetProfile(){try{const{data:profile,error,status}=awaitthis.supabase.profileif (error&&status!==406) {throwerror}if (profile) {this.profile=profile}}catch(error:any){alert(error.message)}}asyncupdateProfile(avatar_url:string=''){constloader=awaitthis.supabase.createLoader()awaitloader.present()try{const{error}=awaitthis.supabase.updateProfile({...this.profile,avatar_url})if (error) {throwerror}awaitloader.dismiss()awaitthis.supabase.createNotice('Profile updated!')}catch(error:any){awaitloader.dismiss()awaitthis.supabase.createNotice(error.message)}}asyncsignOut(){console.log('testing?')awaitthis.supabase.signOut()this.router.navigate(['/'],{replaceUrl:true})}}

```

### Launch![#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#launch)
Now that we have all the components in place, let's update `AppComponent`:
src/app/app.component.ts
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
import{Component}from'@angular/core'import{Router}from'@angular/router'import{SupabaseService}from'./supabase.service'@Component({selector:'app-root',template:`  <ion-app>   <ion-router-outlet></ion-router-outlet>  </ion-app>`,styleUrls:['app.component.scss'],})exportclassAppComponent{constructor(privatesupabase:SupabaseService,privaterouter:Router){this.supabase.authChanges((_,session)=>{console.log(session)if (session?.user) {this.router.navigate(['/account'])}})}}

```

Then update the `AppRoutingModule`
src/app/app-routing.module.ts"
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
import{NgModule}from'@angular/core'import{PreloadAllModules,RouterModule,Routes}from'@angular/router'constroutes:Routes=[{path:'',loadChildren:()=>import('./login/login.module').then((m)=>m.LoginPageModule),},{path:'account',loadChildren:()=>import('./account/account.module').then((m)=>m.AccountPageModule),},]@NgModule({imports:[RouterModule.forRoot(routes,{preloadingStrategy:PreloadAllModules,}),],exports:[RouterModule],})exportclassAppRoutingModule{}

```

Once that's done, run this in a terminal window:
```

1
ionicserve

```

And the browser will automatically open to show the app.
![Supabase Angular](https://supabase.com/docs/img/ionic-demos/ionic-angular.png)
## Bonus: Profile photos[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#bonus-profile-photos)
Every Supabase project is configured with [Storage](https://supabase.com/docs/guides/storage) for managing large files like photos and videos.
### Create an upload widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#create-an-upload-widget)
Let's create an avatar for the user so that they can upload a profile photo.
First, install two packages in order to interact with the user's camera.
```

1
npminstall@ionic/pwa-elements@capacitor/camera

```

[Capacitor](https://capacitorjs.com) is a cross-platform native runtime from Ionic that enables web apps to be deployed through the app store and provides access to native device API.
Ionic PWA elements is a companion package that will polyfill certain browser APIs that provide no user interface with custom Ionic UI.
With those packages installed, we can update our `main.ts` to include an additional bootstrapping call for the Ionic PWA Elements.
src/main.ts
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
import{enableProdMode}from'@angular/core'import{platformBrowserDynamic}from'@angular/platform-browser-dynamic'import{AppModule}from'./app/app.module'import{environment}from'./environments/environment'import{defineCustomElements}from'@ionic/pwa-elements/loader'defineCustomElements(window)if (environment.production) {enableProdMode()}platformBrowserDynamic().bootstrapModule(AppModule).catch((err)=>console.log(err))

```

Then create an `AvatarComponent` with this Ionic CLI command:
```

1
ionicgcomponentavatar--module=/src/app/account/account.module.ts--create-module

```

src/app/avatar.component.ts
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
import{Component,EventEmitter,Input,OnInit,Output}from'@angular/core'import{DomSanitizer,SafeResourceUrl}from'@angular/platform-browser'import{SupabaseService}from'../supabase.service'import{Camera,CameraResultType}from'@capacitor/camera'import{addIcons}from'ionicons'import{person}from'ionicons/icons'@Component({selector:'app-avatar',template:`  <div class="avatar_wrapper" (click)="uploadAvatar()">   <img *ngIf="_avatarUrl; else noAvatar" [src]="_avatarUrl" />   <ng-template #noAvatar>    <ion-icon name="person" class="no-avatar"></ion-icon>   </ng-template>  </div>`,style:[`  :host {    display: block;    margin: auto;    min-height: 150px;  }   :host .avatar_wrapper {    margin: 16px auto 16px;    border-radius: 50%;    overflow: hidden;    height: 150px;    aspect-ratio: 1;    background: var(--ion-color-step-50);    border: thick solid var(--ion-color-step-200);  }   :host .avatar_wrapper:hover {    cursor: pointer;  }   :host .avatar_wrapper ion-icon.no-avatar {    width: 100%;    height: 115%;  }   :host img {    display: block;    object-fit: cover;    width: 100%;    height: 100%;  }`,],})exportclassAvatarComponent{_avatarUrl:SafeResourceUrl|undefineduploading=false@Input()setavatarUrl(url:string|undefined){if (url) {this.downloadImage(url)}}@Output() upload=newEventEmitter<string>()constructor(privatereadonlysupabase:SupabaseService,privatereadonlydom:DomSanitizer){addIcons({person})}asyncdownloadImage(path:string){try{const{data,error}=awaitthis.supabase.downLoadImage(path)if (error) {throwerror}this._avatarUrl=this.dom.bypassSecurityTrustResourceUrl(URL.createObjectURL(data!))}catch(error:any){console.error('Error downloading image: ',error.message)}}asyncuploadAvatar(){constloader=awaitthis.supabase.createLoader()try{constphoto=awaitCamera.getPhoto({resultType:CameraResultType.DataUrl,})constfile=awaitfetch(photo.dataUrl!).then((res)=>res.blob()).then((blob)=>newFile([blob],'my-file',{type:`image/${photo.format}`}))constfileName=`${Math.random()}-${newDate().getTime()}.${photo.format}`awaitloader.present()const{error}=awaitthis.supabase.uploadAvatar(fileName,file)if (error) {throwerror}this.upload.emit(fileName)}catch(error:any){this.supabase.createNotice(error.message)}finally{loader.dismiss()}}}

```

### Add the new widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#add-the-new-widget)
And then, we can add the widget on top of the `AccountComponent` HTML template:
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
template:`<ion-header> <ion-toolbar>  <ion-title>Account</ion-title> </ion-toolbar></ion-header><ion-content> <app-avatar  [avatarUrl]="this.profile?.avatar_url"  (upload)="updateProfile($event)" ></app-avatar><!-- input fields -->`

```

At this stage, you have a fully functional application!
## See also[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#see-also)
  * [Authentication in Ionic Angular with Supabase](https://supabase.com/blog/authentication-in-ionic-angular)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-ionic-angular.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#get-the-api-keys)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#building-the-app)[Initialize an Ionic Angular app](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#initialize-an-ionic-angular-app)[Set up a login route](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#set-up-a-login-route)[Account page](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#account-page)[Launch!](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#launch)[Bonus: Profile photos](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#bonus-profile-photos)[Create an upload widget](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#create-an-upload-widget)[Add the new widget](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#add-the-new-widget)[See also](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular#see-also)
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



