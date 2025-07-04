---
url: https://supabase.com/docs/guides/getting-started/tutorials/with-react
scraped_at: 2025-05-25T09:31:20.862112
title: Build a User Management App with React | Supabase Docs
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
  3. [React](https://supabase.com/docs/guides/getting-started/tutorials/with-react)


Build a User Management App with React
This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - allow users to sign up and log in.
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![Supabase User Management example](https://supabase.com/docs/img/user-management-demo.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/react-user-management).
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#set-up-the-database-schema)
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

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#building-the-app)
Let's start building the React app from scratch.
### Initialize a React app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#initialize-a-react-app)
We can use [Vite](https://vitejs.dev/guide/) to initialize an app called `supabase-react`:
```

1
2
npmcreatevite@latestsupabase-react----templatereactcdsupabase-react

```

Then let's install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js).
```

1
npminstall@supabase/supabase-js

```

And finally we want to save the environment variables in a `.env.local` file. All we need are the API URL and the `anon` key that you copied [earlier](https://supabase.com/docs/guides/getting-started/tutorials/with-react#get-the-api-keys).
.env
```

1
2
VITE_SUPABASE_URL=YOUR_SUPABASE_URLVITE_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY

```

Now that we have the API credentials in place, let's create a helper file to initialize the Supabase client. These variables will be exposed on the browser, and that's completely fine since we have [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) enabled on our Database.
Create and edit `src/supabaseClient.js`:
src/supabaseClient.js
```

1
2
3
4
5
6
import{createClient}from'@supabase/supabase-js'constsupabaseUrl=import.meta.env.VITE_SUPABASE_URLconstsupabaseAnonKey=import.meta.env.VITE_SUPABASE_ANON_KEYexportconstsupabase=createClient(supabaseUrl,supabaseAnonKey)

```

### App styling (optional)[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#app-styling-optional)
An optional step is to update the CSS file `src/index.css` to make the app look nice. You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/react-user-management/src/index.css).
### Set up a login component[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#set-up-a-login-component)
Let's set up a React component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.
Create and edit `src/Auth.jsx`:
src/Auth.jsx
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
import{useState}from'react'import{supabase}from'./supabaseClient'exportdefaultfunctionAuth(){const[loading,setLoading]=useState(false)const[email,setEmail]=useState('')consthandleLogin=async(event)=>{event.preventDefault()setLoading(true)const{error}=awaitsupabase.auth.signInWithOtp({email})if (error) {alert(error.error_description||error.message)}else{alert('Check your email for the login link!')}setLoading(false)}return (<div className="row flex flex-center"><div className="col-6 form-widget"><h1 className="header">Supabase + React</h1><p className="description">Sign in via magic link with your email below</p><form className="form-widget"onSubmit={handleLogin}><div><inputclassName="inputField"type="email"placeholder="Your email"value={email}required={true}onChange={(e)=>setEmail(e.target.value)}/></div><div><button className={'button block'}disabled={loading}>{loading?<span>Loading</span>:<span>Send magic link</span>}</button></div></form></div></div> )}

```

### Account page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#account-page)
After a user is signed in we can allow them to edit their profile details and manage their account.
Let's create a new component for that called `src/Account.jsx`.
src/Account.jsx
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
import{useState,useEffect}from'react'import{supabase}from'./supabaseClient'exportdefaultfunctionAccount({session}){const[loading,setLoading]=useState(true)const[username,setUsername]=useState(null)const[website,setWebsite]=useState(null)const[avatar_url,setAvatarUrl]=useState(null)useEffect(()=>{letignore=falseasyncfunctiongetProfile(){setLoading(true)const{user}=sessionconst{data,error}=awaitsupabase.from('profiles').select(`username, website, avatar_url`).eq('id',user.id).single()if (!ignore) {if (error) {console.warn(error)}elseif (data) {setUsername(data.username)setWebsite(data.website)setAvatarUrl(data.avatar_url)}}setLoading(false)}getProfile()return()=>{ignore=true}},[session])asyncfunctionupdateProfile(event,avatarUrl){event.preventDefault()setLoading(true)const{user}=sessionconstupdates={id:user.id,username,website,avatar_url:avatarUrl,updated_at:newDate(),}const{error}=awaitsupabase.from('profiles').upsert(updates)if (error) {alert(error.message)}else{setAvatarUrl(avatarUrl)}setLoading(false)}return (<form onSubmit={updateProfile}className="form-widget"><div><label htmlFor="email">Email</label><input id="email"type="text"value={session.user.email}disabled/></div><div><label htmlFor="username">Name</label><inputid="username"type="text"requiredvalue={username||''}onChange={(e)=>setUsername(e.target.value)}/></div><div><label htmlFor="website">Website</label><inputid="website"type="url"value={website||''}onChange={(e)=>setWebsite(e.target.value)}/></div><div><button className="button block primary"type="submit"disabled={loading}>{loading?'Loading ...':'Update'}</button></div><div><button className="button block"type="button"onClick={()=>supabase.auth.signOut()}>     Sign Out</button></div></form> )}

```

### Launch![#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#launch)
Now that we have all the components in place, let's update `src/App.jsx`:
src/App.jsx
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
import'./App.css'import{useState,useEffect}from'react'import{supabase}from'./supabaseClient'importAuthfrom'./Auth'importAccountfrom'./Account'functionApp(){const[session,setSession]=useState(null)useEffect(()=>{supabase.auth.getSession().then(({data:{session}})=>{setSession(session)})supabase.auth.onAuthStateChange((_event,session)=>{setSession(session)})},[])return (<div className="container"style={{padding:'50px 0 100px 0'}}>{!session?<Auth />:<Account key={session.user.id}session={session}/>}</div> )}exportdefaultApp

```

Once that's done, run this in a terminal window:
```

1
npmrundev

```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.
![Supabase React](https://supabase.com/docs/img/supabase-react-demo.png)
## Bonus: Profile photos[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#bonus-profile-photos)
Every Supabase project is configured with [Storage](https://supabase.com/docs/guides/storage) for managing large files like photos and videos.
### Create an upload widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#create-an-upload-widget)
Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:
Create and edit `src/Avatar.jsx`:
src/Avatar.jsx
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
import{useEffect,useState}from'react'import{supabase}from'./supabaseClient'exportdefaultfunctionAvatar({url,size,onUpload}){const[avatarUrl,setAvatarUrl]=useState(null)const[uploading,setUploading]=useState(false)useEffect(()=>{if (url) downloadImage(url)},[url])asyncfunctiondownloadImage(path){try{const{data,error}=awaitsupabase.storage.from('avatars').download(path)if (error) {throwerror}consturl=URL.createObjectURL(data)setAvatarUrl(url)}catch (error) {console.log('Error downloading image: ',error.message)}}asyncfunctionuploadAvatar(event){try{setUploading(true)if (!event.target.files||event.target.files.length===0) {thrownewError('You must select an image to upload.')}constfile=event.target.files[0]constfileExt=file.name.split('.').pop()constfileName=`${Math.random()}.${fileExt}`constfilePath=`${fileName}`const{error:uploadError}=awaitsupabase.storage.from('avatars').upload(filePath,file)if (uploadError) {throwuploadError}onUpload(event,filePath)}catch (error) {alert(error.message)}finally{setUploading(false)}}return (<div>{avatarUrl?(<imgsrc={avatarUrl}alt="Avatar"className="avatar image"style={{height:size,width:size}}/>):(<div className="avatar no-image"style={{height:size,width:size}}/>)}<div style={{width:size}}><label className="button primary block"htmlFor="single">{uploading?'Uploading ...':'Upload'}</label><inputstyle={{visibility:'hidden',position:'absolute',}}type="file"id="single"accept="image/*"onChange={uploadAvatar}disabled={uploading}/></div></div> )}

```

### Add the new widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-react#add-the-new-widget)
And then we can add the widget to the Account page at `src/Account.jsx`:
src/Account.jsx
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
// Import the new componentimportAvatarfrom'./Avatar'// ...return (<form onSubmit={updateProfile}className="form-widget">{/* Add to the body */}<Avatarurl={avatar_url}size={150}onUpload={(event,url)=>{updateProfile(event,url)}}/>{/* ... */}</form>)

```

At this stage you have a fully functional application!
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-react.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-react#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-react#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-react#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-react#get-the-api-keys)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-react#building-the-app)[Initialize a React app](https://supabase.com/docs/guides/getting-started/tutorials/with-react#initialize-a-react-app)[App styling (optional)](https://supabase.com/docs/guides/getting-started/tutorials/with-react#app-styling-optional)[Set up a login component](https://supabase.com/docs/guides/getting-started/tutorials/with-react#set-up-a-login-component)[Account page](https://supabase.com/docs/guides/getting-started/tutorials/with-react#account-page)[Launch!](https://supabase.com/docs/guides/getting-started/tutorials/with-react#launch)[Bonus: Profile photos](https://supabase.com/docs/guides/getting-started/tutorials/with-react#bonus-profile-photos)[Create an upload widget](https://supabase.com/docs/guides/getting-started/tutorials/with-react#create-an-upload-widget)[Add the new widget](https://supabase.com/docs/guides/getting-started/tutorials/with-react#add-the-new-widget)
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



