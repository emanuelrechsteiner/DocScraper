---
url: https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit
scraped_at: 2025-05-25T09:30:48.627821
title: Build a User Management App with SvelteKit | Supabase Docs
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
  3. [SvelteKit](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit)


Build a User Management App with SvelteKit
This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - allow users to sign up and log in.
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![Supabase User Management example](https://supabase.com/docs/img/user-management-demo.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/sveltekit-user-management).
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#set-up-the-database-schema)
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

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#building-the-app)
Let's start building the Svelte app from scratch.
### Initialize a Svelte app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#initialize-a-svelte-app)
We can use the [SvelteKit Skeleton Project](https://kit.svelte.dev/docs) to initialize an app called `supabase-sveltekit` (for this tutorial we will be using TypeScript):
```

1
2
3
npmcreatesvelte@latestsupabase-sveltekitcdsupabase-sveltekitnpminstall

```

Then install the Supabase client library: [supabase-js](https://github.com/supabase/supabase-js)
```

1
npminstall@supabase/supabase-js

```

And finally we want to save the environment variables in a `.env`. All we need are the `SUPABASE_URL` and the `SUPABASE_KEY` key that you copied [earlier](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#get-the-api-keys).
.env
```

1
2
PUBLIC_SUPABASE_URL="YOUR_SUPABASE_URL"PUBLIC_SUPABASE_ANON_KEY="YOUR_SUPABASE_KEY"

```

Optionally, add `src/styles.css` with the [CSS from the example](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/sveltekit-user-management/src/styles.css).
### Creating a Supabase client for SSR[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#creating-a-supabase-client-for-ssr)
The `ssr` package configures Supabase to use Cookies, which is required for server-side languages and frameworks.
Install the Supabase packages:
```

1
npminstall@supabase/ssr@supabase/supabase-js

```

Creating a Supabase client with the `ssr` package automatically configures it to use Cookies. This means your user's session is available throughout the entire SvelteKit stack - page, layout, server, hooks.
Add the code below to your `src/hooks.server.ts` to initialize the client on the server:
src/hooks.server.ts
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
// src/hooks.server.tsimport{PUBLIC_SUPABASE_URL,PUBLIC_SUPABASE_ANON_KEY}from'$env/static/public'import{createServerClient}from'@supabase/ssr'importtype{Handle}from'@sveltejs/kit'exportconsthandle:Handle=async({event,resolve})=>{event.locals.supabase=createServerClient(PUBLIC_SUPABASE_URL,PUBLIC_SUPABASE_ANON_KEY,{cookies:{getAll:()=>event.cookies.getAll(),/**    * SvelteKit's cookies API requires `path` to be explicitly set in    * the cookie options. Setting `path` to `/` replicates previous/    * standard behavior.    */setAll:(cookiesToSet)=>{cookiesToSet.forEach(({name,value,options})=>{event.cookies.set(name,value,{...options,path:'/'})})},},})/**  * Unlike `supabase.auth.getSession()`, which returns the session _without_  * validating the JWT, this function also calls `getUser()` to validate the  * JWT before returning the session.  */event.locals.safeGetSession=async()=>{const{data:{session},}=awaitevent.locals.supabase.auth.getSession()if (!session) {return{session:null,user:null}}const{data:{user},error,}=awaitevent.locals.supabase.auth.getUser()if (error) {// JWT validation has failedreturn{session:null,user:null}}return{session,user}}returnresolve(event,{filterSerializedResponseHeaders(name){returnname==='content-range'||name==='x-supabase-api-version'},})}

```

Note that `auth.getSession` reads the auth token and the unencoded session data from the local storage medium. It _doesn't_ send a request back to the Supabase Auth server unless the local session is expired.
You should **never** trust the unencoded session data if you're writing server code, since it could be tampered with by the sender. If you need verified, trustworthy user data, call `auth.getUser` instead, which always makes a request to the Auth server to fetch trusted data.
If you are using TypeScript the compiler might complain about `event.locals.supabase` and `event.locals.safeGetSession`, this can be fixed by updating your `src/app.d.ts` with the content below:
src/app.d.ts
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
// src/app.d.tsimport{SupabaseClient,Session}from'@supabase/supabase-js'declareglobal{namespaceApp{interfaceLocals{supabase:SupabaseClientsafeGetSession():Promise<{session:Session|null;user:User|null}>}interfacePageData{session:Session|nulluser:User|null}// interface Error {}// interface Platform {}}}

```

Create a new `src/routes/+layout.server.ts` file to handle the session on the server-side.
src/routes/+layout.server.ts
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
// src/routes/+layout.server.tsimporttype{LayoutServerLoad}from'./$types'exportconstload:LayoutServerLoad=async({locals:{safeGetSession},cookies})=>{const{session,user}=awaitsafeGetSession()return{session,user,cookies:cookies.getAll(),}}

```

Start your dev server (`npm run dev`) in order to generate the `./$types` files we are referencing in our project.
Create a new `src/routes/+layout.ts` file to handle the session and the `supabase` object on the client-side.
src/routes/+layout.ts
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
// src/routes/+layout.tsimport{createBrowserClient,createServerClient,isBrowser}from'@supabase/ssr'import{PUBLIC_SUPABASE_ANON_KEY,PUBLIC_SUPABASE_URL}from'$env/static/public'importtype{LayoutLoad}from'./$types'exportconstload:LayoutLoad=async({fetch,data,depends})=>{depends('supabase:auth')constsupabase=isBrowser()?createBrowserClient(PUBLIC_SUPABASE_URL,PUBLIC_SUPABASE_ANON_KEY,{global:{fetch,},}):createServerClient(PUBLIC_SUPABASE_URL,PUBLIC_SUPABASE_ANON_KEY,{global:{fetch,},cookies:{getAll(){returndata.cookies},},})/**  * It's fine to use `getSession` here, because on the client, `getSession` is  * safe, and on the server, it reads `session` from the `LayoutData`, which  * safely checked the session using `safeGetSession`.  */const{data:{session},}=awaitsupabase.auth.getSession()return{supabase,session}}

```

Update your `src/routes/+layout.svelte`:
src/routes/+layout.svelte
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
<!-- src/routes/+layout.svelte --><script lang="ts">import'../styles.css'import{invalidate}from'$app/navigation'import{onMount}from'svelte'exportletdatalet{supabase,session}=data$:({supabase,session}=data)onMount(()=>{const{data}=supabase.auth.onAuthStateChange((event,newSession)=>{if (newSession?.expires_at!==session?.expires_at) {invalidate('supabase:auth')}})return()=>data.subscription.unsubscribe()})</script><svelte:head><title>User Management</title></svelte:head><div class="container"style="padding: 50px 0 100px 0"><slot/></div>

```

## Set up a login page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#set-up-a-login-page)
Create a magic link login/signup page for your application:
src/routes/+page.svelte
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
<!-- src/routes/+page.svelte --><script lang="ts">import{enhance}from'$app/forms'importtype{ActionData,SubmitFunction}from'./$types.js'exportletform:ActionData;letloading=falseconsthandleSubmit:SubmitFunction=()=>{loading=truereturnasync({update})=>{update()loading=false}}</script><svelte:head><title>User Management</title></svelte:head><form class="row flex flex-center"method="POST"use:enhance={handleSubmit}><div class="col-6 form-widget"><h1 class="header">Supabase + SvelteKit</h1><p class="description">Sign in via magic link with your email below</p>{#ifform?.message!==undefined}<div class="success {form?.success?'':'fail'}">{form?.message}</div>{/if}<div><label for="email">Email address</label><inputid="email"name="email"class="inputField"type="email"placeholder="Your email"value={form?.email??''}/></div>{#ifform?.errors?.email}<span class="flex items-center text-sm error">{form?.errors?.email}</span>{/if}<div><button class="button primary block">{loading?'Loading':'Send magic link'}</button></div></div></form>

```

Create a `src/routes/+page.server.ts` file that will handle our magic link form when submitted.
src/routes/+page.server.ts
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
// src/routes/+page.server.tsimport{fail,redirect}from'@sveltejs/kit'importtype{Actions,PageServerLoad}from'./$types'exportconstload:PageServerLoad=async({url,locals:{safeGetSession}})=>{const{session}=awaitsafeGetSession()// if the user is already logged in return them to the account pageif (session) {redirect(303,'/account')}return{url:url.origin}}exportconstactions:Actions={default:async(event)=>{const{url,request,locals:{supabase},}=eventconstformData=awaitrequest.formData()constemail=formData.get('email')asstringconstvalidEmail=/^[\w-\.+]+@([\w-]+\.)+[\w-]{2,8}$/.test(email)if (!validEmail) {returnfail(400,{errors:{email:'Please enter a valid email address'},email})}const{error}=awaitsupabase.auth.signInWithOtp({email})if (error) {returnfail(400,{success:false,email,message:`There was an issue, Please contact support.`,})}return{success:true,message:'Please check your email for a magic link to log into the website.',}},}

```

### Email template[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#email-template)
Change the email template to support a server-side authentication flow.
Before we proceed, let's change the email template to support sending a token hash:
  * Go to the [Auth templates](https://supabase.com/dashboard/project/_/auth/templates) page in your dashboard.
  * Select `Confirm signup` template.
  * Change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email`.
  * Repeat the previous step for `Magic link` template.


Did you know? You could also customize emails sent out to new users, including the email's looks, content, and query parameters. Check out the [settings of your project](https://supabase.com/dashboard/project/_/auth/templates).
### Confirmation endpoint[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#confirmation-endpoint)
As we are working in a server-side rendering (SSR) environment, it is necessary to create a server endpoint responsible for exchanging the `token_hash` for a session.
In the following code snippet, we perform the following steps:
  * Retrieve the `token_hash` sent back from the Supabase Auth server using the `token_hash` query parameter.
  * Exchange this `token_hash` for a session, which we store in storage (in this case, cookies).
  * Finally, the user is redirected to the `account` page or the `error` page.


src/routes/auth/confirm/+server.ts
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
// src/routes/auth/confirm/+server.tsimporttype{EmailOtpType}from'@supabase/supabase-js'import{redirect}from'@sveltejs/kit'importtype{RequestHandler}from'./$types'exportconstGET:RequestHandler=async({url,locals:{supabase}})=>{consttoken_hash=url.searchParams.get('token_hash')consttype=url.searchParams.get('type')asEmailOtpType|nullconstnext=url.searchParams.get('next')??'/account'/**  * Clean up the redirect URL by deleting the Auth flow parameters.  *  * `next` is preserved for now, because it's needed in the error case.  */constredirectTo=newURL(url)redirectTo.pathname=nextredirectTo.searchParams.delete('token_hash')redirectTo.searchParams.delete('type')if (token_hash&&type) {const{error}=awaitsupabase.auth.verifyOtp({type,token_hash})if (!error) {redirectTo.searchParams.delete('next')redirect(303,redirectTo)}}redirectTo.pathname='/auth/error'redirect(303,redirectTo)}

```

### Authentication error page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#authentication-error-page)
If there is an error with confirming the token you will be redirect to this error page.
src/routes/auth/error/+page.svelte
```

1
<p>Login error</p>

```

### Account page[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#account-page)
After a user is signed in, they need to be able to edit their profile details and manage their account. Create a new `src/routes/account/+page.svelte` file with the content below.
src/routes/account/+page.svelte
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
<!-- src/routes/account/+page.svelte --><script lang="ts">import{enhance}from'$app/forms';importtype{SubmitFunction}from'@sveltejs/kit';exportletdataexportletformlet{session,supabase,profile}=data$:({session,supabase,profile}=data)letprofileForm:HTMLFormElementletloading=falseletfullName:string=profile?.full_name??''letusername:string=profile?.username??''letwebsite:string=profile?.website??''letavatarUrl:string=profile?.avatar_url??''consthandleSubmit:SubmitFunction=()=>{loading=truereturnasync()=>{loading=false}}consthandleSignOut:SubmitFunction=()=>{loading=truereturnasync({update})=>{loading=falseupdate()}}</script><div class="form-widget"><formclass="form-widget"method="post"action="?/update"use:enhance={handleSubmit}bind:this={profileForm}><div><label for="email">Email</label><input id="email"type="text"value={session.user.email}disabled/></div><div><label for="fullName">Full Name</label><input id="fullName"name="fullName"type="text"value={form?.fullName??fullName}/></div><div><label for="username">Username</label><input id="username"name="username"type="text"value={form?.username??username}/></div><div><label for="website">Website</label><input id="website"name="website"type="url"value={form?.website??website}/></div><div><inputtype="submit"class="button block primary"value={loading?'Loading...':'Update'}disabled={loading}/></div></form><form method="post"action="?/signout"use:enhance={handleSignOut}><div><button class="button block"disabled={loading}>Sign Out</button></div></form></div>

```

Now create the associated `src/routes/account/+page.server.ts` file that will handle loading our data from the server through the `load` function and handle all our form actions through the `actions` object.
###### src/routes/account/+page.server.ts
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
import{fail,redirect}from'@sveltejs/kit'importtype{Actions,PageServerLoad}from'./$types'exportconstload:PageServerLoad=async({locals:{supabase,safeGetSession}})=>{const{session}=awaitsafeGetSession()if (!session) {redirect(303,'/')}const{data:profile}=awaitsupabase.from('profiles').select(`username, full_name, website, avatar_url`).eq('id',session.user.id).single()return{session,profile}}exportconstactions:Actions={update:async({request,locals:{supabase,safeGetSession}})=>{constformData=awaitrequest.formData()constfullName=formData.get('fullName')asstringconstusername=formData.get('username')asstringconstwebsite=formData.get('website')asstringconstavatarUrl=formData.get('avatarUrl')asstringconst{session}=awaitsafeGetSession()const{error}=awaitsupabase.from('profiles').upsert({id:session?.user.id,full_name:fullName,username,website,avatar_url:avatarUrl,updated_at:newDate(),})if (error) {returnfail(500,{fullName,username,website,avatarUrl,})}return{fullName,username,website,avatarUrl,}},signout:async({locals:{supabase,safeGetSession}})=>{const{session}=awaitsafeGetSession()if (session) {awaitsupabase.auth.signOut()redirect(303,'/')}},}

```

### Launch![#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#launch)
Now that we have all the pages in place, run this in a terminal window:
```

1
npmrundev

```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.
![Supabase Svelte](https://supabase.com/docs/img/supabase-svelte-demo.png)
## Bonus: Profile photos[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#bonus-profile-photos)
Every Supabase project is configured with [Storage](https://supabase.com/docs/guides/storage) for managing large files like photos and videos.
### Create an upload widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#create-an-upload-widget)
Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component called `Avatar.svelte` in the `src/routes/account` directory:
src/routes/account/Avatar.svelte
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
<!-- src/routes/account/Avatar.svelte --><script lang="ts">importtype{SupabaseClient}from'@supabase/supabase-js'import{createEventDispatcher}from'svelte'exportletsize=10exportleturl:stringexportletsupabase:SupabaseClientletavatarUrl:string|null=nullletuploading=falseletfiles:FileListconstdispatch=createEventDispatcher()constdownloadImage=async(path:string)=>{try{const{data,error}=awaitsupabase.storage.from('avatars').download(path)if (error) {throwerror}consturl=URL.createObjectURL(data)avatarUrl=url}catch (error) {if (errorinstanceofError) {console.log('Error downloading image: ',error.message)}}}constuploadAvatar=async()=>{try{uploading=trueif (!files||files.length===0) {thrownewError('You must select an image to upload.')}constfile=files[0]constfileExt=file.name.split('.').pop()constfilePath=`${Math.random()}.${fileExt}`const{error}=awaitsupabase.storage.from('avatars').upload(filePath,file)if (error) {throwerror}url=filePathsetTimeout(()=>{dispatch('upload')},100)}catch (error) {if (errorinstanceofError) {alert(error.message)}}finally{uploading=false}}$:if(url)downloadImage(url)</script><div>{#ifavatarUrl}<imgsrc={avatarUrl}alt={avatarUrl?'Avatar':'No image'}class="avatar image"style="height: {size}em; width: {size}em;"/>{:else}<div class="avatar no-image"style="height: {size}em; width: {size}em;"/>{/if}<input type="hidden"name="avatarUrl"value={url}/><div style="width: {size}em;"><label class="button primary block"for="single">{uploading?'Uploading ...':'Upload'}</label><inputstyle="visibility: hidden; position:absolute;"type="file"id="single"accept="image/*"bind:fileson:change={uploadAvatar}disabled={uploading}/></div></div>

```

### Add the new widget[#](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#add-the-new-widget)
And then we can add the widget to the Account page:
src/routes/account/+page.svelte
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
<!-- src/routes/account/+page.svelte --><script lang="ts">// Import the new componentimportAvatarfrom'./Avatar.svelte'</script><div class="form-widget"><formclass="form-widget"method="post"action="?/update"use:enhance={handleSubmit}bind:this={profileForm}><!-- Add to body --><Avatar{supabase}bind:url={avatarUrl}size={10}on:upload={()=>{profileForm.requestSubmit();}}/><!-- Other form elements --></form></div>

```

At this stage you have a fully functional application!
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-sveltekit.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#get-the-api-keys)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#building-the-app)[Initialize a Svelte app](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#initialize-a-svelte-app)[Creating a Supabase client for SSR](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#creating-a-supabase-client-for-ssr)[Set up a login page](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#set-up-a-login-page)[Email template](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#email-template)[Confirmation endpoint](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#confirmation-endpoint)[Authentication error page](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#authentication-error-page)[Account page](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#account-page)[Launch!](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#launch)[Bonus: Profile photos](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#bonus-profile-photos)[Create an upload widget](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#create-an-upload-widget)[Add the new widget](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit#add-the-new-widget)
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



