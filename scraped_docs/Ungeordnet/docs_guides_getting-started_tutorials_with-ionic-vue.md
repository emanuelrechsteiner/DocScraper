---
url: https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue
scraped_at: 2025-05-25T08:42:53.257475
title: Build a User Management App with Ionic Vue | Supabase Docs
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
  3. [Ionic Vue](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue)


Build a User Management App with Ionic Vue
This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - allow users to sign up and log in.
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![Supabase User Management example](https://supabase.com/docs/img/ionic-demos/ionic-angular-account.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/mhartington/supabase-ionic-vue).
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#set-up-the-database-schema)
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

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#building-the-app)
Let's start building the Vue app from scratch.
### Initialize an Ionic Vue app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#initialize-an-ionic-vue-app)
We can use the [Ionic CLI](https://ionicframework.com/docs/cli) to initialize an app called `supabase-ionic-vue`:
```

1
2
3
npminstall-g@ionic/cliionicstartsupabase-ionic-vueblank--typevuecdsupabase-ionic-vue

```

Then let's install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)
```

1
npminstall@supabase/supabase-js

```

And finally we want to save the environment variables in a `.env`.
All we need are the API URL and the `anon` key that you copied [earlier](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#get-the-api-keys).
.env
```

1
2
VITE_SUPABASE_URL=YOUR_SUPABASE_URLVITE_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY

```

Now that we have the API credentials in place, let's create a helper file to initialize the Supabase client. These variables will be exposed on the browser, and that's completely fine since we have [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) enabled on our Database.
src/supabase.ts
```

1
2
3
4
5
6
import{createClient}from'@supabase/supabase-js';constsupabaseUrl=import.meta.env.VITE_SUPABASE_URLasstring;constsupabaseAnonKey=import.meta.env.VITE_SUPABASE_ANON_KEYasstring;exportconstsupabase=createClient(supabaseUrl,supabaseAnonKey);

```

### Set up a login route[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#set-up-a-login-route)
Let's set up a Vue component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.
/src/views/Login.vue
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
<template><ion-page><ion-header><ion-toolbar><ion-title>Login</ion-title></ion-toolbar></ion-header><ion-content><div class="ion-padding"><h1>Supabase + Ionic Vue</h1><p>Sign in via magic link with your email below</p></div><ion-list inset="true"><form @submit.prevent="handleLogin"><ion-item><ion-label position="stacked">Email</ion-label><ion-input v-model="email"name="email"autocompletetype="email"></ion-input></ion-item><div class="ion-text-center"><ion-button type="submit"fill="clear">Login</ion-button></div></form></ion-list><p>{{ email }}</p></ion-content></ion-page></template><script lang="ts">import{supabase}from'../supabase'import{IonContent,IonHeader,IonPage,IonTitle,IonToolbar,IonList,IonItem,IonLabel,IonInput,IonButton,toastController,loadingController,}from'@ionic/vue'import{defineComponent,ref}from'vue'exportdefaultdefineComponent({name:'LoginPage',components:{IonContent,IonHeader,IonPage,IonTitle,IonToolbar,IonList,IonItem,IonLabel,IonInput,IonButton,},setup(){constemail=ref('')consthandleLogin=async()=>{constloader=awaitloadingController.create({})consttoast=awaittoastController.create({duration:5000})try{awaitloader.present()const{error}=awaitsupabase.auth.signInWithOtp({email:email.value})if (error) throwerrortoast.message='Check your email for the login link!'awaittoast.present()}catch(error:any){toast.message=error.error_description||error.messageawaittoast.present()}finally{awaitloader.dismiss()}}return{handleLogin,email}},})</script>

```

### Account page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#account-page)
After a user is signed in we can allow them to edit their profile details and manage their account.
Let's create a new component for that called `Account.vue`.
src/views/Account.vue
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
174
175
176
177
<template><ion-page><ion-header><ion-toolbar><ion-title>Account</ion-title></ion-toolbar></ion-header><ion-content><form @submit.prevent="updateProfile"><ion-item><ion-label><p>Email</p><p>{{ user?.email }}</p></ion-label></ion-item><ion-item><ion-label position="stacked">Name</ion-label><ion-input type="text"v-model="profile.username"/></ion-item><ion-item><ion-label position="stacked">Website</ion-label><ion-input type="url"v-model="profile.website"/></ion-item><div class="ion-text-center"><ion-button type="submit"fill="clear">Update Profile</ion-button></div></form><div class="ion-text-center"><ion-button fill="clear"@click="signOut">Log Out</ion-button></div></ion-content></ion-page></template><script lang="ts">import{IonPage,IonHeader,IonToolbar,IonTitle,IonContent,IonItem,IonLabel,IonInput,IonButton,toastController,loadingController,}from'@ionic/vue'import{defineComponent,onMounted,ref}from'vue'import{useRouter}from'vue-router'import{supabase}from'@/supabase'importtype{User}from'@supabase/supabase-js'exportdefaultdefineComponent({name:'AccountPage',components:{IonPage,IonHeader,IonToolbar,IonTitle,IonContent,IonItem,IonLabel,IonInput,IonButton,},setup(){constrouter=useRouter()constuser=ref<User|null>(null)constprofile=ref({username:'',website:'',avatar_url:'',})constgetProfile=async()=>{constloader=awaitloadingController.create()consttoast=awaittoastController.create({duration:5000})awaitloader.present()try{const{data,error,status}=awaitsupabase.from('profiles').select('username, website, avatar_url').eq('id',user.value?.id).single()if (error&&status!==406) throwerrorif (data) {profile.value={username:data.username,website:data.website,avatar_url:data.avatar_url,}}}catch(error:any){toast.message=error.messageawaittoast.present()}finally{awaitloader.dismiss()}}constupdateProfile=async()=>{constloader=awaitloadingController.create()consttoast=awaittoastController.create({duration:5000})awaitloader.present()try{constupdates={id:user.value?.id,...profile.value,updated_at:newDate(),}const{error}=awaitsupabase.from('profiles').upsert(updates,{returning:'minimal',})if (error) throwerror}catch(error:any){toast.message=error.messageawaittoast.present()}finally{awaitloader.dismiss()}}constsignOut=async()=>{constloader=awaitloadingController.create()consttoast=awaittoastController.create({duration:5000})awaitloader.present()try{const{error}=awaitsupabase.auth.signOut()if (error) throwerrorrouter.push('/')}catch(error:any){toast.message=error.messageawaittoast.present()}finally{awaitloader.dismiss()}}onMounted(async()=>{constloader=awaitloadingController.create()awaitloader.present()const{data}=awaitsupabase.auth.getSession()user.value=data.session?.user??nullif (!user.value) {router.push('/')}else{awaitgetProfile()}awaitloader.dismiss()})return{user,profile,updateProfile,signOut,}},})</script>

```

### Launch![#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#launch)
Now that we have all the components in place, let's update `App.vue` and our routes:
src/router.index.tssrc/App.vue
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
import{createRouter,createWebHistory}from'@ionic/vue-router'import{RouteRecordRaw}from'vue-router'importLoginPagefrom'../views/Login.vue'importAccountPagefrom'../views/Account.vue'constroutes:Array<RouteRecordRaw>=[{path:'/',name:'Login',component:LoginPage,},{path:'/account',name:'Account',component:AccountPage,},]constrouter=createRouter({history:createWebHistory(import.meta.env.BASE_URL),routes,})exportdefaultrouter

```

Once that's done, run this in a terminal window:
```

1
ionicserve

```

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.
![Supabase Ionic Vue](https://supabase.com/docs/img/ionic-demos/ionic-vue.png)
## Bonus: Profile photos[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#bonus-profile-photos)
Every Supabase project is configured with [Storage](https://supabase.com/docs/guides/storage) for managing large files like photos and videos.
### Create an upload widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#create-an-upload-widget)
First install two packages in order to interact with the user's camera.
```

1
npminstall@ionic/pwa-elements@capacitor/camera

```

[Capacitor](https://capacitorjs.com) is a cross-platform native runtime from Ionic that enables web apps to be deployed through the app store and provides access to native device API.
Ionic PWA elements is a companion package that will polyfill certain browser APIs that provide no user interface with custom Ionic UI.
With those packages installed we can update our `main.ts` to include an additional bootstrapping call for the Ionic PWA Elements.
src/main.tsx
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
import{createApp}from'vue'importAppfrom'./App.vue'importrouterfrom'./router'import{IonicVue}from'@ionic/vue'/* Core CSS required for Ionic components to work properly */import'@ionic/vue/css/ionic.bundle.css'/* Theme variables */import'./theme/variables.css'import{defineCustomElements}from'@ionic/pwa-elements/loader'defineCustomElements(window)constapp=createApp(App).use(IonicVue).use(router)router.isReady().then(()=>{app.mount('#app')})

```

Then create an `AvatarComponent`.
src/components/Avatar.vue
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
<template><div class="avatar"><div class="avatar_wrapper"@click="uploadAvatar"><img v-if="avatarUrl":src="avatarUrl"/><ion-icon v-elsename="person"class="no-avatar"></ion-icon></div></div></template><script lang="ts">import{ref,toRefs,watch,defineComponent}from'vue'import{supabase}from'../supabase'import{Camera,CameraResultType}from'@capacitor/camera'import{IonIcon}from'@ionic/vue'import{person}from'ionicons/icons'exportdefaultdefineComponent({name:'AppAvatar',props:{path:String},emits:['upload','update:path'],components:{IonIcon},setup(prop,{emit}){const{path}=toRefs(prop)constavatarUrl=ref('')constdownloadImage=async()=>{try{const{data,error}=awaitsupabase.storage.from('avatars').download(path.value)if (error) throwerroravatarUrl.value=URL.createObjectURL(data!)}catch(error:any){console.error('Error downloading image: ',error.message)}}constuploadAvatar=async()=>{try{constphoto=awaitCamera.getPhoto({resultType:CameraResultType.DataUrl,})if (photo.dataUrl) {constfile=awaitfetch(photo.dataUrl).then((res)=>res.blob()).then((blob)=>newFile([blob],'my-file',{type:`image/${photo.format}`}))constfileName=`${Math.random()}-${newDate().getTime()}.${photo.format}`const{error:uploadError}=awaitsupabase.storage.from('avatars').upload(fileName,file)if (uploadError) {throwuploadError}emit('update:path',fileName)emit('upload')}}catch (error) {console.log(error)}}watch(path,()=>{if (path.value) downloadImage()})return{avatarUrl,uploadAvatar,person}},})</script><style>.avatar{display: block;margin: auto;min-height:150px;}.avatar.avatar_wrapper{margin:16px auto 16px;border-radius:50%;overflow: hidden;height:150px;aspect-ratio:1;background:var(--ion-color-step-50);border: thick solid var(--ion-color-step-200);}.avatar.avatar_wrapper:hover{cursor: pointer;}.avatar.avatar_wrapperion-icon.no-avatar{width:100%;height:115%;}.avatarimg{display: block;object-fit: cover;width:100%;height:100%;}</style>

```

### Add the new widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#add-the-new-widget)
And then we can add the widget to the Account page:
src/views/Account.vue
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
<template><ion-page><ion-header><ion-toolbar><ion-title>Account</ion-title></ion-toolbar></ion-header><ion-content><avatarv-model:path="profile.avatar_url"@upload="updateProfile"></avatar>...</template><script lang="ts">importAvatarfrom'../components/Avatar.vue';exportdefaultdefineComponent({name:'AccountPage',components:{Avatar,....}</script>

```

At this stage you have a fully functional application!
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-ionic-vue.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#get-the-api-keys)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#building-the-app)[Initialize an Ionic Vue app](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#initialize-an-ionic-vue-app)[Set up a login route](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#set-up-a-login-route)[Account page](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#account-page)[Launch!](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#launch)[Bonus: Profile photos](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#bonus-profile-photos)[Create an upload widget](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#create-an-upload-widget)[Add the new widget](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue#add-the-new-widget)
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



