---
url: https://supabase.com/docs/guides/getting-started/tutorials/with-refine
scraped_at: 2025-05-25T09:38:56.986462
title: Build a User Management App with refine | Supabase Docs
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
  3. [refine](https://supabase.com/docs/guides/getting-started/tutorials/with-refine)


Build a User Management App with refine
This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - allow users to sign up and log in.
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![Supabase User Management example](https://supabase.com/docs/img/user-management-demo.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/refine-user-management).
## About refine[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#about-refine)
[refine](https://github.com/refinedev/refine) is a React-based framework used to rapidly build data-heavy applications like admin panels, dashboards, storefronts and any type of CRUD apps. It separates app concerns into individual layers, each backed by a React context and respective provider object. For example, the auth layer represents a context served by a specific set of [`authProvider`](https://refine.dev/docs/tutorial/understanding-authprovider/index/) methods that carry out authentication and authorization actions such as logging in, logging out, getting roles data, etc. Similarly, the data layer offers another level of abstraction that is equipped with [`dataProvider`](https://refine.dev/docs/tutorial/understanding-dataprovider/index/) methods to handle CRUD operations at appropriate backend API endpoints.
refine provides hassle-free integration with Supabase backend with its supplementary [`@refinedev/supabase`](https://github.com/refinedev/refine/tree/master/packages/supabase) package. It generates `authProvider` and `dataProvider` methods at project initialization, so we don't need to expend much effort to define them ourselves. We just need to choose Supabase as our backend service while creating the app with `create refine-app`.
It is possible to customize the `authProvider` for Supabase and as we'll see below, it can be tweaked from `src/authProvider.ts` file. In contrast, the Supabase `dataProvider` is part of `node_modules` and therefore is not subject to modification.
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#set-up-the-database-schema)
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

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#building-the-app)
Let's start building the refine app from scratch.
### Initialize a refine app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#initialize-a-refine-app)
We can use [create refine-app](https://refine.dev/docs/tutorial/getting-started/headless/create-project/#launch-the-refine-cli-setup) command to initialize an app. Run the following in the terminal:
```

1
npmcreaterefine-app@latest----presetrefine-supabase

```

In the above command, we are using the `refine-supabase` preset which chooses the Supabase supplementary package for our app. We are not using any UI framework, so we'll have a headless UI with plain React and CSS styling.
The `refine-supabase` preset installs the `@refinedev/supabase` package which out-of-the-box includes the Supabase dependency: [supabase-js](https://github.com/supabase/supabase-js).
We also need to install `@refinedev/react-hook-form` and `react-hook-form` packages that allow us to use [React Hook Form](https://react-hook-form.com) inside refine apps. Run:
```

1
npminstall@refinedev/react-hook-formreact-hook-form

```

With the app initialized and packages installed, at this point before we begin discussing refine concepts, let's try running the app:
```

1
2
cdapp-namenpmrundev

```

We should have a running instance of the app with a Welcome page at `http://localhost:5173`.
Let's move ahead to understand the generated code now.
### Refine `supabaseClient`[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#refine-supabaseclient)
The `create refine-app` generated a Supabase client for us in the `src/utility/supabaseClient.ts` file. It has two constants: `SUPABASE_URL` and `SUPABASE_KEY`. We want to replace them as `supabaseUrl` and `supabaseAnonKey` respectively and assign them our own Supabase server's values.
We'll update it with environment variables managed by Vite:
src/utility/supabaseClient.ts
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
import{createClient}from'@refinedev/supabase'constsupabaseUrl=import.meta.env.VITE_SUPABASE_URLconstsupabaseAnonKey=import.meta.env.VITE_SUPABASE_ANON_KEYexportconstsupabaseClient=createClient(supabaseUrl,supabaseAnonKey,{db:{schema:'public',},auth:{persistSession:true,},})

```

And then, we want to save the environment variables in a `.env.local` file. All you need are the API URL and the `anon` key that you copied [earlier](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#get-the-api-keys).
```

1
2
VITE_SUPABASE_URL=YOUR_SUPABASE_URLVITE_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY

```

The `supabaseClient` will be used in fetch calls to Supabase endpoints from our app. As we'll see below, the client is instrumental in implementing authentication using Refine's auth provider methods and CRUD actions with appropriate data provider methods.
One optional step is to update the CSS file `src/App.css` to make the app look nice. You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/refine-user-management/src/App.css).
In order for us to add login and user profile pages in this App, we have to tweak the `<Refine />` component inside `App.tsx`.
### The `<Refine />` component[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#the-refine--component)
The `App.tsx` file initially looks like this:
src/App.tsx
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
import{Refine,WelcomePage}from'@refinedev/core'import{RefineKbar,RefineKbarProvider}from'@refinedev/kbar'importrouterBindings,{DocumentTitleHandler,UnsavedChangesNotifier,}from'@refinedev/react-router-v6'import{dataProvider,liveProvider}from'@refinedev/supabase'import{BrowserRouter,Route,Routes}from'react-router-dom'import'./App.css'importauthProviderfrom'./authProvider'import{supabaseClient}from'./utility'functionApp(){return (<BrowserRouter><RefineKbarProvider><RefinedataProvider={dataProvider(supabaseClient)}liveProvider={liveProvider(supabaseClient)}authProvider={authProvider}routerProvider={routerBindings}options={{syncWithLocation:true,warnWhenUnsavedChanges:true,}}><Routes><Route indexelement={<WelcomePage />}/></Routes><RefineKbar /><UnsavedChangesNotifier /><DocumentTitleHandler /></Refine></RefineKbarProvider></BrowserRouter> )}exportdefaultApp

```

We'd like to focus on the [`<Refine />`](https://refine.dev/docs/api-reference/core/components/refine-config/) component, which comes with several props passed to it. Notice the `dataProvider` prop. It uses a `dataProvider()` function with `supabaseClient` passed as argument to generate the data provider object. The `authProvider` object also uses `supabaseClient` in implementing its methods. You can look it up in `src/authProvider.ts` file.
## Customize `authProvider`[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#customize-authprovider)
If you examine the `authProvider` object you can notice that it has a `login` method that implements a OAuth and Email / Password strategy for authentication. We'll, however, remove them and use Magic Links to allow users sign in with their email without using passwords.
We want to use `supabaseClient` auth's `signInWithOtp` method inside `authProvider.login` method:
###### src/authProvider.ts
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
login:async({email})=>{try{const{error}=awaitsupabaseClient.auth.signInWithOtp({email});if (!error) {alert("Check your email for the login link!");return{success:true,};};throwerror;}catch(e:any){alert(e.message);return{success:false,e,};}},

```

We also want to remove `register`, `updatePassword`, `forgotPassword` and `getPermissions` properties, which are optional type members and also not necessary for our app. The final `authProvider` object looks like this:
src/authProvider.ts
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
import{AuthBindings}from'@refinedev/core'import{supabaseClient}from'./utility'constauthProvider:AuthBindings={login:async({email})=>{try{const{error}=awaitsupabaseClient.auth.signInWithOtp({email})if (!error) {alert('Check your email for the login link!')return{success:true,}}throwerror}catch(e:any){alert(e.message)return{success:false,e,}}},logout:async()=>{const{error}=awaitsupabaseClient.auth.signOut()if (error) {return{success:false,error,}}return{success:true,redirectTo:'/',}},onError:async(error)=>{console.error(error)return{error}},check:async()=>{try{const{data}=awaitsupabaseClient.auth.getSession()const{session}=dataif (!session) {return{authenticated:false,error:{message:'Check failed',name:'Session not found',},logout:true,redirectTo:'/login',}}}catch(error:any){return{authenticated:false,error:error||{message:'Check failed',name:'Not authenticated',},logout:true,redirectTo:'/login',}}return{authenticated:true,}},getIdentity:async()=>{const{data}=awaitsupabaseClient.auth.getUser()if (data?.user) {return{...data.user,name:data.user.email,}}returnnull},}exportdefaultauthProvider

```

### Set up a login component[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#set-up-a-login-component)
We have chosen to use the headless refine core package that comes with no supported UI framework. So, let's set up a plain React component to manage logins and sign ups.
Create and edit `src/components/auth.tsx`:
src/components/auth.tsx
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
import{useState}from'react'import{useLogin}from'@refinedev/core'exportdefaultfunctionAuth(){const[email,setEmail]=useState('')const{isLoading,mutate:login}=useLogin()consthandleLogin=async(event:{preventDefault:()=>void})=>{event.preventDefault()login({email})}return (<divclassName="row flex flex-center container"><divclassName="col-6 form-widget"><h1className="header">Supabase+refine</h1><pclassName="description">Signinviamagiclinkwithyouremailbelow</p><formclassName="form-widget"onSubmit={handleLogin}><div><inputclassName="inputField"type="email"placeholder="Your email"value={email}required={true}onChange={(e) => setEmail(e.target.value)}/></div><div><buttonclassName={'button block'}disabled={isLoading}>{isLoading ? <span>Loading</span> : <span>Sendmagiclink</span>}</button></div></form></div></div> )}

```

Notice we are using the [`useLogin()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useLogin/) refine auth hook to grab the `mutate: login` method to use inside `handleLogin()` function and `isLoading` state for our form submission. The `useLogin()` hook conveniently offers us access to `authProvider.login` method for authenticating the user with OTP.
### Account page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#account-page)
After a user is signed in we can allow them to edit their profile details and manage their account.
Let's create a new component for that in `src/components/account.tsx`.
src/components/account.tsx
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
import{BaseKey,useGetIdentity,useLogout}from'@refinedev/core'import{useForm}from'@refinedev/react-hook-form'interfaceIUserIdentity{id?:BaseKeyusername:stringname:string}exportinterfaceIProfile{id?:stringusername?:stringwebsite?:stringavatar_url?:string}exportdefaultfunctionAccount(){const{data:userIdentity}=useGetIdentity<IUserIdentity>()const{mutate:logOut}=useLogout()const{refineCore:{formLoading,queryResult,onFinish},register,control,handleSubmit,}=useForm<IProfile>({refineCoreProps:{resource:'profiles',action:'edit',id:userIdentity?.id,redirect:false,onMutationError:(data)=>alert(data?.message),},})return (<div className="container"style={{padding:'50px 0 100px 0'}}><form onSubmit={handleSubmit(onFinish)}className="form-widget"><div><label htmlFor="email">Email</label><input id="email"name="email"type="text"value={userIdentity?.name}disabled/></div><div><label htmlFor="username">Name</label><input id="username"type="text"{...register('username')}/></div><div><label htmlFor="website">Website</label><input id="website"type="url"{...register('website')}/></div><div><button className="button block primary"type="submit"disabled={formLoading}>{formLoading?'Loading ...':'Update'}</button></div><div><button className="button block"type="button"onClick={()=>logOut()}>      Sign Out</button></div></form></div> )}

```

Notice above that, we are using three refine hooks, namely the [`useGetIdentity()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useGetIdentity/), [`useLogOut()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useLogout/) and [`useForm()`](https://refine.dev/docs/packages/documentation/react-hook-form/useForm/) hooks.
`useGetIdentity()` is a auth hook that gets the identity of the authenticated user. It grabs the current user by invoking the `authProvider.getIdentity` method under the hood.
`useLogOut()` is also an auth hook. It calls the `authProvider.logout` method to end the session.
`useForm()`, in contrast, is a data hook that exposes a series of useful objects that serve the edit form. For example, we are grabbing the `onFinish` function to submit the form with the `handleSubmit` event handler. We are also using `formLoading` property to present state changes of the submitted form.
The `useForm()` hook is a higher-level hook built on top of Refine's `useForm()` core hook. It fully supports form state management, field validation and submission using React Hook Form. Behind the scenes, it invokes the `dataProvider.getOne` method to get the user profile data from our Supabase `/profiles` endpoint and also invokes `dataProvider.update` method when `onFinish()` is called.
### Launch![#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#launch)
Now that we have all the components in place, let's define the routes for the pages in which they should be rendered.
Add the routes for `/login` with the `<Auth />` component and the routes for `index` path with the `<Account />` component. So, the final `App.tsx`:
src/App.tsx
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
import{Authenticated,Refine}from'@refinedev/core'import{RefineKbar,RefineKbarProvider}from'@refinedev/kbar'importrouterBindings,{CatchAllNavigate,DocumentTitleHandler,UnsavedChangesNotifier,}from'@refinedev/react-router-v6'import{dataProvider,liveProvider}from'@refinedev/supabase'import{BrowserRouter,Outlet,Route,Routes}from'react-router-dom'import'./App.css'importauthProviderfrom'./authProvider'import{supabaseClient}from'./utility'importAccountfrom'./components/account'importAuthfrom'./components/auth'functionApp(){return (<BrowserRouter><RefineKbarProvider><RefinedataProvider={dataProvider(supabaseClient)}liveProvider={liveProvider(supabaseClient)}authProvider={authProvider}routerProvider={routerBindings}options={{syncWithLocation:true,warnWhenUnsavedChanges:true,}}><Routes><Routeelement={<Authenticated fallback={<CatchAllNavigate to="/login"/>}><Outlet /></Authenticated>}><Route indexelement={<Account />}/></Route><Route element={<Authenticated fallback={<Outlet />}/>}><Route path="/login"element={<Auth />}/></Route></Routes><RefineKbar /><UnsavedChangesNotifier /><DocumentTitleHandler /></Refine></RefineKbarProvider></BrowserRouter> )}exportdefaultApp

```

Let's test the App by running the server again:
```

1
npmrundev

```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.
![Supabase refine](https://supabase.com/docs/img/supabase-refine-demo.png)
## Bonus: Profile photos[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#bonus-profile-photos)
Every Supabase project is configured with [Storage](https://supabase.com/docs/guides/storage) for managing large files like photos and videos.
### Create an upload widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#create-an-upload-widget)
Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:
Create and edit `src/components/avatar.tsx`:
src/components/avatar.tsx
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
import{useEffect,useState}from'react'import{supabaseClient}from'../utility/supabaseClient'typeTAvatarProps={url?:stringsize:numberonUpload:(filePath:string)=>void}exportdefaultfunctionAvatar({url,size,onUpload}:TAvatarProps){const[avatarUrl,setAvatarUrl]=useState('')const[uploading,setUploading]=useState(false)useEffect(()=>{if (url) downloadImage(url)},[url])asyncfunctiondownloadImage(path:string){try{const{data,error}=awaitsupabaseClient.storage.from('avatars').download(path)if (error) {throwerror}consturl=URL.createObjectURL(data)setAvatarUrl(url)}catch(error:any){console.log('Error downloading image: ',error?.message)}}asyncfunctionuploadAvatar(event:React.ChangeEvent<HTMLInputElement>){try{setUploading(true)if (!event.target.files||event.target.files.length===0) {thrownewError('You must select an image to upload.')}constfile=event.target.files[0]constfileExt=file.name.split('.').pop()constfileName=`${Math.random()}.${fileExt}`constfilePath=`${fileName}`const{error:uploadError}=awaitsupabaseClient.storage.from('avatars').upload(filePath,file)if (uploadError) {throwuploadError}onUpload(filePath)}catch(error:any){alert(error.message)}finally{setUploading(false)}}return (<div>{avatarUrl?(<imgsrc={avatarUrl}alt="Avatar"className="avatar image"style={{height:size,width:size}}/>):(<div className="avatar no-image"style={{height:size,width:size}}/>)}<div style={{width:size}}><label className="button primary block"htmlFor="single">{uploading?'Uploading ...':'Upload'}</label><inputstyle={{visibility:'hidden',position:'absolute',}}type="file"id="single"name="avatar_url"accept="image/*"onChange={uploadAvatar}disabled={uploading}/></div></div> )}

```

### Add the new widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#add-the-new-widget)
And then we can add the widget to the Account page at `src/components/account.tsx`:
src/components/account.tsx
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
// Import the new componentsimport{Controller}from'react-hook-form'importAvatarfrom'./avatar'// ...return (<div className="container"style={{padding:'50px 0 100px 0'}}><form onSubmit={handleSubmit}className="form-widget"><Controllercontrol={control}name="avatar_url"render={({field})=>{return (<Avatarurl={field.value}size={150}onUpload={(filePath)=>{onFinish({...queryResult?.data?.data,avatar_url:filePath,onMutationError:(data:{message:string})=>alert(data?.message),})field.onChange({target:{value:filePath,},})}}/>     )}}/>{/* ... */}</form></div>)

```

At this stage, you have a fully functional application!
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-refine.mdx)
### Is this helpful?
No Yes
### On this page
[About refine](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#about-refine)[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#get-the-api-keys)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#building-the-app)[Initialize a refine app](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#initialize-a-refine-app)[Refine supabaseClient](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#refine-supabaseclient)[The <Refine /> component](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#the-refine--component)[Customize authProvider](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#customize-authprovider)[Set up a login component](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#set-up-a-login-component)[Account page](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#account-page)[Launch!](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#launch)[Bonus: Profile photos](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#bonus-profile-photos)[Create an upload widget](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#create-an-upload-widget)[Add the new widget](https://supabase.com/docs/guides/getting-started/tutorials/with-refine#add-the-new-widget)
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



