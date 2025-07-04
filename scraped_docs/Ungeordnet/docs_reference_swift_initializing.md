---
url: https://supabase.com/docs/reference/swift/initializing
scraped_at: 2025-05-25T09:14:37.106173
title: Swift API Reference | Supabase Docs
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
swift
v2.0
  * [Introduction](https://supabase.com/docs/reference/swift/introduction)
  * [Installing](https://supabase.com/docs/reference/swift/installing)
  * [Initializing](https://supabase.com/docs/reference/swift/initializing)
  * Database
    * [Fetch data](https://supabase.com/docs/reference/swift/select)
    * [Insert data](https://supabase.com/docs/reference/swift/insert)
    * [Update data](https://supabase.com/docs/reference/swift/update)
    * [Upsert data](https://supabase.com/docs/reference/swift/upsert)
    * [Delete data](https://supabase.com/docs/reference/swift/delete)
    * [Call a Postgres function](https://supabase.com/docs/reference/swift/rpc)
    * Using filters
    * Using modifiers
  * Auth
    * [Overview](https://supabase.com/docs/reference/swift/auth-api)
    * [Create a new user](https://supabase.com/docs/reference/swift/auth-signup)
    * [Listen to auth events](https://supabase.com/docs/reference/swift/auth-onauthstatechange)
    * [Create an anonymous user](https://supabase.com/docs/reference/swift/auth-signinanonymously)
    * [Sign in a user](https://supabase.com/docs/reference/swift/auth-signinwithpassword)
    * [Sign in with ID Token](https://supabase.com/docs/reference/swift/auth-signinwithidtoken)
    * [Sign in a user through OTP](https://supabase.com/docs/reference/swift/auth-signinwithotp)
    * [Sign in a user through OAuth](https://supabase.com/docs/reference/swift/auth-signinwithoauth)
    * [Sign in a user through SSO](https://supabase.com/docs/reference/swift/auth-signinwithsso)
    * [Sign out a user](https://supabase.com/docs/reference/swift/auth-signout)
    * [Verify and log in through OTP](https://supabase.com/docs/reference/swift/auth-verifyotp)
    * [Retrieve a session](https://supabase.com/docs/reference/swift/auth-getsession)
    * [Retrieve a new session](https://supabase.com/docs/reference/swift/auth-refreshsession)
    * [Retrieve a user](https://supabase.com/docs/reference/swift/auth-getuser)
    * [Update a user](https://supabase.com/docs/reference/swift/auth-updateuser)
    * [Retrieve identities linked to a user](https://supabase.com/docs/reference/swift/auth-getuseridentities)
    * [Link an identity to a user](https://supabase.com/docs/reference/swift/auth-linkidentity)
    * [Unlink an identity from a user](https://supabase.com/docs/reference/swift/auth-unlinkidentity)
    * [Send a password reauthentication nonce](https://supabase.com/docs/reference/swift/auth-reauthentication)
    * [Resend an OTP](https://supabase.com/docs/reference/swift/auth-resend)
    * [Set the session data](https://supabase.com/docs/reference/swift/auth-setsession)
    * [Exchange an auth code for a session](https://supabase.com/docs/reference/swift/auth-exchangecodeforsession)
    * Auth MFA
    * Auth Admin
  * Edge Functions
    * [Invokes a Supabase Edge Function.](https://supabase.com/docs/reference/swift/functions-invoke)
  * Realtime
    * [Subscribe to channel](https://supabase.com/docs/reference/swift/subscribe)
    * [Unsubscribe from a channel](https://supabase.com/docs/reference/swift/removechannel)
    * [Unsubscribe from all channels](https://supabase.com/docs/reference/swift/removeallchannels)
    * [Retrieve all channels](https://supabase.com/docs/reference/swift/getchannels)
  * Storage
    * [Create a bucket](https://supabase.com/docs/reference/swift/storage-createbucket)
    * [Retrieve a bucket](https://supabase.com/docs/reference/swift/storage-getbucket)
    * [List all buckets](https://supabase.com/docs/reference/swift/storage-listbuckets)
    * [Update a bucket](https://supabase.com/docs/reference/swift/storage-updatebucket)
    * [Delete a bucket](https://supabase.com/docs/reference/swift/storage-deletebucket)
    * [Empty a bucket](https://supabase.com/docs/reference/swift/storage-emptybucket)
    * [Upload a file](https://supabase.com/docs/reference/swift/storage-from-upload)
    * [Download a file](https://supabase.com/docs/reference/swift/storage-from-download)
    * [List all files in a bucket](https://supabase.com/docs/reference/swift/storage-from-list)
    * [Replace an existing file](https://supabase.com/docs/reference/swift/storage-from-update)
    * [Move an existing file](https://supabase.com/docs/reference/swift/storage-from-move)
    * [Copy an existing file](https://supabase.com/docs/reference/swift/storage-from-copy)
    * [Delete files in a bucket](https://supabase.com/docs/reference/swift/storage-from-remove)
    * [Create a signed URL](https://supabase.com/docs/reference/swift/storage-from-createsignedurl)
    * [Create signed URLs](https://supabase.com/docs/reference/swift/storage-from-createsignedurls)
    * [Retrieve public URL](https://supabase.com/docs/reference/swift/storage-from-getpublicurl)


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
Swift Reference v2.0
# swift Client Library
supabase-swift[View on GitHub](https://github.com/supabase/supabase-swift)
This reference documents every object and method available in Supabase's Swift library, [supabase-swift](https://github.com/supabase/supabase-swift). You can use supabase-swift to interact with your Postgres database, listen to database changes, invoke Deno Edge Functions, build login and user management functionality, and manage large files.
## Installing
### Install using Swift Package Manager[#](https://supabase.com/docs/reference/swift/initializing#install-using-swift-package-manager)
You can install Supabase package using Swift Package Manager.
The package exposes multiple libraries, you can choose between adding all of them using Supabase, or some of:
  * `Auth`
  * `Realtime`
  * `Postgrest`
  * `Functions`
  * `Storage`


Package.swift
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
letpackage=Package(...  dependencies: [...    .package(      url:"https://github.com/supabase/supabase-swift.git",      from:"2.0.0"),  ],  targets: [    .target(      name:"YourTargetName",      dependencies: [        .product(          name:"Supabase", // Auth, Realtime, Postgrest, Functions, or Storage          package:"supabase-swift"),      ])  ])

```

## Initializing
You can initialize Supabase with the `SupabaseClient` by passing your `Project URL` and `Project Key`. You can find these under your `Project Settings` → `API Settings` The Supabase client is your entrypoint to the rest of the Supabase functionality and is the easiest way to interact with everything we offer within the Supabase ecosystem.
Initialize ClientInitialize Client with custom optionsInitialize Client with LoggingWith custom schemas
```

1
2
3
importSupabaselet client =SupabaseClient(supabaseURL: URL(string:"https://xyzcompany.supabase.co")!, supabaseKey:"public-anon-key")

```

## Fetch data
  * By default, Supabase projects will return a maximum of 1,000 rows. This setting can be changed in Project API Settings. It's recommended that you keep it low to limit the payload size of accidental or malicious requests. You can use `range()` queries to paginate through your data.
  * `select()` can be combined with [Modifiers](https://supabase.com/docs/reference/swift/using-modifiers)
  * `select()` can be combined with [Filters](https://supabase.com/docs/reference/swift/using-filters)
  * If using the Supabase hosted platform `apikey` is technically a reserved keyword, since the API gateway will pluck it out for authentication. [It should be avoided as a column name](https://github.com/supabase/supabase/issues/5465).
  * The recommended solution for getting data is to use the value property which will return a decoded model. Create a `Codable` to easily decode your database responses.


Getting your dataSelecting specific columnsQuery foreign tablesQuery foreign tables through a join tableQuery the same foreign table multiple timesFiltering through foreign tablesQuerying foreign table with countQuerying with count optionQuerying JSON dataQuerying foreign table with inner joinSwitching schemas per query
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
structInstrument:Decodable {let id: Intlet name: String}let instruments: [Instrument]=tryawait supabase .from("instruments") .select() .execute() .value

```

Data source
Response
## Insert data
Create a recordCreate a record and return itBulk create
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
structInstrument:Encodable {let id: Intlet name: String}let instrument =Instrument(id:1, name:"ukelele")tryawait supabase .from("instruments") .insert(instrument) .execute()

```

Data source
Response
## Update data
  * `update()` should always be combined with [Filters](https://supabase.com/docs/reference/swift/using-filters) to target the item(s) you wish to update.


Updating your dataUpdate a record and return itUpdating JSON data
```

1
2
3
4
5
tryawait supabase .from("instruments") .update(["name":"piano"]) .eq("id", value:1) .execute()

```

Data source
Response
## Upsert data
  * Primary keys must be included in `values` to use upsert.


Upsert your dataBulk Upsert your dataUpserting into tables with constraints
```

1
2
3
4
5
6
7
8
structInstrument:Encodable {let id: Intlet name: String}tryawait supabase .from("instruments") .upsert(Instrument(id:1, name:"piano")) .execute()

```

Data source
Response
## Delete data
  * `delete()` should always be combined with [filters](https://supabase.com/docs/reference/swift/using-filters) to target the item(s) you wish to delete.
  * If you use `delete()` with filters and you have [RLS](https://supabase.com/docs/learn/auth-deep-dive/auth-row-level-security) enabled, only rows visible through `SELECT` policies are deleted. Note that by default no rows are visible, so you need at least one `SELECT`/`ALL` policy that makes the rows visible.


Delete records
```

1
2
3
4
5
tryawait supabase .from("instruments") .delete() .eq("id", value:1) .execute()

```

Data source
Response
## Call a Postgres function
You can call Postgres functions as _Remote Procedure Calls_ , logic in your database that you can execute from anywhere. Functions are useful when the logic rarely changes—like for password resets and updates.
```

1
2
3
create or replacefunctionhello_world()returnstextas $$select'Hello world';$$ languagesql;

```

Call a Postgres function without argumentsCall a Postgres function with argumentsBulk processingCall a Postgres function with filters
```

1
2
3
4
let value: String=tryawait supabase .rpc("hello_world") .execute() .value

```

Data source
Response
## Using filters
Filters allow you to only return rows that match certain conditions.
Filters can be used on `select()`, `update()`, `upsert()`, and `delete()` queries.
If a Postgres function returns a table response, you can also apply filters.
Implement `URLQueryRepresentable` protocol in your own types to be able to use them as filter value.
Supported filtes are: `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`, `ilike`, `is`, `in`, `cs`, `cd`, `sl`, `sr`, `nxl`, `nxr`, `adj`, `ov`, `fts`, `plfts`, `phfts`, `wfts`. Check available operators in [PostgREST](https://postgrest.org/en/stable/references/api/tables_views.html#operators).
Applying FiltersChainingConditional ChainingFilter by values within a JSON columnFilter Foreign Tables
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
tryawait supabase .from("cities") .select("name, country_id") .eq("name", value:"The Shire")// Correcttryawait supabase .from("citites") .eq("name", value:"The Shire")// Incorrect .select("name, country_id")

```

Notes
## Match an associated value
With `select()`
```

1
2
3
4
tryawait supabase .from("instruments") .select("name") .match(["id":2, "name":"viola"])

```

Data source
Response
## Don't match the filter
Finds all rows that don't satisfy the filter.
  * `.not()` expects you to use the raw [PostgREST syntax](https://postgrest.org/en/stable/api.html#horizontal-filtering-rows) for the filter names and values.
```

1
2
3
4
5
.not("name", operator: .eq, value:"violin").not("arraycol", operator: .cs, value:#"{"a","b"}"#)// Use Postgres array {} for array column and 'cs' for contains..not("rangecol", operator: .cs, value:"(1,2]")// Use Postgres range syntax for range column..not("id", operator: .in, value:"(6,7)")// Use Postgres list () and 'in' for in_ filter..not("id", operator: .in, value:"(\(mylist.join(separator:",")))")// You can insert a Swift list array.

```



With `select()`
```

1
2
3
4
5
tryawait supabase .from("instruments") .select() .not("name", operator: .is, value:"") .execute()

```

## Match at least one filter
or() expects you to use the raw PostgREST syntax for the filter names and values.
```

1
2
.or(#"id.in.(5,6,7), arraycol.cs.{"a","b"}"#)// Use `()` for `in` filter, `{}` for array values and `cs` for `contains()`..or(#"id.in.(5,6,7), arraycol.cd.{"a","b"}"#)// Use `cd` for `containedBy()`

```

With `select()`Use `or` with `and`
```

1
2
3
4
tryawait supabase .from("instruments") .select("name") .or("id.eq.2,name.eq.cello")

```

Data source
Response
## Match the filter
filter() expects you to use the raw PostgREST syntax for the filter values.
```

1
2
.filter("id", operator:"in", value:"(5,6,7)")// Use `()` for `in` filter.filter("arraycol", operator:"cs", value:#"{"a","b"}"#)// Use `cs` for `contains()`, `{}` for array values

```

With `select()`On a foreign table
```

1
2
3
4
tryawait supabase .from("instruments") .select() .filter("name", operator:"in", value:#"("cello","guzheng")"#)

```

Data source
Response
## Using modifiers
Filters work on the row level—they allow you to return rows that only match certain conditions without changing the shape of the rows. Modifiers are everything that don't fit that definition—allowing you to change the format of the response (e.g. returning a CSV string).
Modifiers must be specified after filters. Some modifiers only apply for queries that return rows (e.g., `select()` or `rpc()` on a function that returns a table response).
## Return data after inserting
Perform a SELECT on the query result.
With `upsert()`
```

1
2
3
4
5
tryawait supabase  .from("instruments")  .upsert(InstrumentModel(id:1, name:"piano"))  .select()  .execute()

```

Data source
Response
## Order the results
Order the query result by column.
With `select()`On a foreign tableOrder parent table by a referenced table
```

1
2
3
4
5
tryawait supabase .from("instruments") .select("id, name") .order("id", ascending:false) .execute()

```

Data source
Response
## Limit the number of rows returned
Limit the query result by count.
With `select()`On a foreign table
```

1
2
3
4
5
tryawait supabase .from("instruments") .select("id, name") .limit(1) .execute()

```

Data source
Response
## Limit the query to a range
Limit the query result by from and to inclusively.
With `select()`
```

1
2
3
4
5
tryawait supabase .from("instruments") .select("name") .range(from:0, to:1) .execute()

```

Data source
Response
## Retrieve one row of data
By default PostgREST returns all JSON results in an array, even when there is only one item, use `single()` to return the first object unenclosed by an array.
With `select()`
```

1
2
3
4
5
6
tryawait supabase .from("instruments") .select("name") .limit(1) .single() .execute()

```

Data source
Response
## Retrieve as a CSV
Return data as CSV
```

1
2
3
4
5
tryawait supabase .from("instruments") .select() .csv() .execute()

```

Data source
Response
Notes
## Using explain
For debugging slow queries, you can get the [Postgres `EXPLAIN` execution plan](https://www.postgresql.org/docs/current/sql-explain.html) of a query using the `explain()` method. This works on any query, even for `rpc()` or writes.
Explain is not enabled by default as it can reveal sensitive information about your database. It's best to only enable this for testing environments but if you wish to enable it for production you can provide additional protection by using a `pre-request` function.
Follow the [Performance Debugging Guide](https://supabase.com/docs/guides/database/debugging-performance) to enable the functionality on your project.
Get the execution planGet the execution plan with analyze and verbose
```

1
2
3
4
5
6
tryawait supabase .from("instruments") .select() .explain() .execute() .value

```

Data source
Response
Notes
## Overview
The auth methods can be accessed via the `supabase.auth` namespace.
### Handling deep links[#](https://supabase.com/docs/reference/swift/initializing#handling-deep-links)
#### UIKit app lifecycle[#](https://supabase.com/docs/reference/swift/initializing#uikit-app-lifecycle)
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
publicfuncapplication(_application: UIApplication,didFinishLaunchingWithOptionslaunchOptions: [UIApplication.LaunchOptionsKey:Any]?)->Bool{iflet url = launchOptions?[.url] as? URL {  supabase.auth.handle(url)}returntrue}funcapplication(_app: UIApplication,openurl: URL,options: [UIApplication.OpenURLOptionsKey:Any])->Bool{ supabase.auth.handle(url)returntrue}#### UIKit app lifecycle with scenesIn your `SceneDelegate.swift`:```swiftfuncscene(_scene: UIScene, openURLContextsURLContexts: Set<UIOpenURLContext>){guardlet url = URLContexts.first?.urlelse{return} supabase.auth.handle(url)}

```

#### SwiftUI app lifecycle[#](https://supabase.com/docs/reference/swift/initializing#swiftui-app-lifecycle)
In your `AppDelegate.swift`:
```

1
2
3
4
SomeView() .onOpenURL{ url in  supabase.auth.handle(url)}

```

Create auth clientCreate auth client with custom storage
```

1
2
let supabase =SupabaseClient(supabaseURL: URL(string:"https://xyzcompany.supabase.co")!, supabaseKey:"public-anon-key")let auth = supabase.auth

```

## Create a new user
  * By default, the user needs to verify their email address before logging in. To turn this off, disable **Confirm email** in [your project](https://supabase.com/dashboard/project/_/auth/providers).
  * **Confirm email** determines if users need to confirm their email address after signing up. 
    * If **Confirm email** is enabled, a `user` is returned but `session` is null.
    * If **Confirm email** is disabled, both a `user` and a `session` are returned.
  * When the user confirms their email address, they are redirected to the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls) by default. You can modify your `SITE_URL` or add additional redirect URLs in [your project](https://supabase.com/dashboard/project/_/auth/url-configuration).
  * If signUp() is called for an existing confirmed user: 
    * When both **Confirm email** and **Confirm phone** (even when phone provider is disabled) are enabled in [your project](https://supabase.com/dashboard/project/_/auth/providers), an obfuscated/fake user object is returned.
    * When either **Confirm email** or **Confirm phone** (even when phone provider is disabled) is disabled, the error message, `User already registered` is returned.
  * To fetch the currently logged-in user, refer to [`getUser()`](https://supabase.com/docs/reference/swift/get-user).


### Parameters
  * emailOptionalString
One of `email` or `phone` must be provided.
  * phoneOptionalString
One of `email` or `phone` must be provided.
  * passwordRequiredString
  * dataOptionalJSONObject
A custom data object to store additional user metadata.
  * redirectToOptionalURL
Only for email signups. The redirect URL embedded in the email link. Must be a configured redirect URL for your Supabase instance.
  * captchaTokenOptionalString


Sign up with email and passwordSign up with a phone number and password (SMS)Sign up with a phone number and password (whatsapp)Sign up with additional user metadataSign up with a redirect URL
```

1
2
3
4
tryawait supabase.auth.signUp( email:"example@email.com", password:"example-password")

```

## Listen to auth events
  * Subscribes to important events occurring on the user's session.
  * Emitted events: 
    * `INITIAL_SESSION`
      * Emitted right after the Supabase client is constructed and the initial session from storage is loaded.
    * `SIGNED_IN`
      * Emitted each time a user session is confirmed or re-established, including on user sign in.
      * Avoid making assumptions as to when this event is fired, this may occur even when the user is already signed in. Instead, check the user object attached to the event to see if a new user has signed in and update your application's UI.
    * `SIGNED_OUT`
      * Emitted when the user signs out. This can be after: 
        * A call to `supabase.auth.signOut()`.
        * After the user's session has expired for any reason: 
          * User has signed out on another device.
          * The session has reached its timebox limit or inactivity timeout.
          * User has signed in on another device with single session per user enabled.
          * Check the [User Sessions](https://supabase.com/docs/guides/auth/sessions) docs for more information.
      * Use this to clean up any local storage your application has associated with the user.
    * `TOKEN_REFRESHED`
      * Emitted each time a new access and refresh token are fetched for the signed in user.
      * It's best practice and highly recommended to extract the access token (JWT) and store it in memory for further use in your application. 
        * Avoid frequent calls to `supabase.auth.session` for the same purpose.
      * There is a background process that keeps track of when the session should be refreshed so you will always receive valid tokens by listening to this event.
      * The frequency of this event is related to the JWT expiry limit configured on your project.
    * `USER_UPDATED`
      * Emitted each time the `supabase.auth.update(user:)` method finishes successfully. Listen to it to update your application's UI based on new profile information.
    * `PASSWORD_RECOVERY`
      * Emitted instead of the `SIGNED_IN` event when the user lands on a page that includes a password recovery link in the URL.
      * Use it to show a UI to the user where they can [reset their password](https://supabase.com/docs/guides/auth/passwords#resetting-a-users-password-forgot-password).


Listen to auth changesListen to a specific event
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
// Using AsyncStreamforawait(event, session)inawait supabase.auth.authStateChanges {print(event, session)}// Using Closurelet subscription =await supabase.auth.onAuthStateChange{ event, session inprint(event, session)}// call remove() to remove subscriptionsubscription.remove()

```

Notes
## Create an anonymous user
  * Returns an anonymous user
  * It is recommended to set up captcha for anonymous sign-ins to prevent abuse. You can pass in the captcha token in the `options` param.


Create an anonymous userCreate an anonymous user with custom user metadata
```

1
let session =tryawait supabase.auth.signInAnonymously(captchaToken: captchaToken)

```

## Sign in a user
  * Requires either an email and password or a phone number and password.


### Parameters
  * emailOptionalString
One of `email` or `phone` must be provided.
  * phoneOptionalString
One of `email` or `phone` must be provided.
  * passwordRequiredString
  * captchaTokenOptionalString


Sign in with email and passwordSign in with phone and password
```

1
2
3
4
tryawait supabase.auth.signIn( email:"example@email.com", password:"example-password")

```

## Sign in with ID Token
Sign In using ID Token
```

1
2
3
4
5
6
7
let session =tryawait supabase.auth.signInWithIdToken( credentials: OpenIDConnectCredentials(  provider: .apple,  idToken:"your-id-token",  nonce:"your nonce"))

```

Notes
## Sign in a user through OTP
  * Requires either an email or phone number.
  * This method is used for passwordless sign-ins where a OTP is sent to the user's email or phone number.
  * If the user doesn't exist, `signInWithOTP()` will signup the user instead. To restrict this behavior, you can set `shouldCreateUser` to `false``.
  * If you're using an email, you can configure whether you want the user to receive a magiclink or a OTP.
  * If you're using phone, you can configure whether you want the user to receive a OTP.
  * The magic link's destination URL is determined by the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls).
  * See [redirect URLs and wildcards](https://supabase.com/docs/guides/auth#redirect-urls-and-wildcards) to add additional redirect URLs to your project.
  * Magic links and OTPs share the same implementation. To send users a one-time code instead of a magic link, [modify the magic link email template](https://supabase.com/dashboard/project/_/auth/templates) to include `{{ .Token }}` instead of `{{ .ConfirmationURL }}`.
  * See our [Twilio Phone Auth Guide](https://supabase.com/docs/guides/auth/phone-login/twilio) for details about configuring WhatsApp sign in.


### Parameters
  * emailOptionalString
One of `email` or `phone` must be provided.
  * phoneOptionalString
One of `email` or `phone` must be provided.
  * redirectToOptionalString
Only for email signups. The redirect URL embedded in the email link. Must be a configured redirect URL for your Supabase instance.
  * channelOptionalMessagingChannel
The channel to use for sending messages. Only for phone signups.
  * shouldCreateUserOptionalBool
Whether to create the user if they don't already exist. Defaults to true.
  * dataOptionalJSONObject
A custom data object to store additional user metadata.
  * captchaTokenOptionalString


Sign in with emailSign in with SMS OTPSign in with WhatsApp OTP
```

1
2
3
4
tryawait supabase.auth.signInWithOTP( email:"example@email.com", redirectTo: URL(string:"my-app-scheme://")!)

```

Notes
## Sign in a user through OAuth
  * This method is used for signing in using a third-party provider.
  * Supabase supports many different [third-party providers](https://supabase.com/docs/guides/auth#providers).


### Parameters
  * providerRequiredProvider
The third-party provider.
  * redirectToOptionalURL
A URL to send the user to after they are confirmed.
  * scopesOptionalString
A space-separated list of scopes granted to the OAuth application.
  * queryParamsOptional[(name: String, value: String?)]
Additional query params.
  * configureOptionalCallback
A custom configuration callback for opening the OAuth flow externally.


Sign in with OAuth using ASWebAuthenticationSessionSign in with OAuth and customize flowSign in using a third-party providerSign in with scopes
```

1
2
3
4
5
let session =tryawait supabase.auth.signInWithOAuth( provider: .github){(session: ASWebAuthenticationSession)in// customize session}

```

Notes
## Sign in a user through SSO
  * Before you can call this method you need to [establish a connection](https://supabase.com/docs/guides/auth/sso/auth-sso-saml#managing-saml-20-connections) to an identity provider. Use the [CLI commands](https://supabase.com/docs/reference/cli/supabase-sso) to do this.
  * If you've associated an email domain to the identity provider, you can use the `domain` property to start a sign-in flow.
  * In case you need to use a different way to start the authentication flow with an identity provider, you can use the `providerId` property. For example: 
    * Mapping specific user email addresses with an identity provider.
    * Using different hints to identity the identity provider to be used by the user, like a company-specific page, IP address or other tracking information.


### Parameters
  * providerIdOptionalString
UUID of the SSO provider. One of `providerId` or `domain` is required.
  * domainOptionalString
Domain name of the organization to use SSO with. One of `providerId` or `domain` is required.
  * redirectToRequiredString
The URL to redirect the user to after they have signed in. Must be a configured redirect URL for your Supabase instance.
  * captchaTokenRequiredString


Sign in with email domainSign in with provider UUID
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
// You can extract the user's email domain and use it to trigger the// authentication flow with the correct identity provider.let url =tryawaitawait supabase.auth.signInWithSSO{  domain:"company.com"}// Open the URL using your preferred method to complete sign-in process. UIApplication.shared.open(url)

```

## Sign out a user
  * In order to use the `signOut()` method, the user needs to be signed in first.


Sign out
```

1
tryawait supabase.auth.signOut()

```

## Verify and log in through OTP
  * The `verifyOTP` method takes in different verification types. If a phone number is used, the type can either be `sms` or `phone_change`. If an email address is used, the type can be one of the following: `signup`, `magiclink`, `recovery`, `invite`, `email_change`, or `email`.
  * The verification type used should be determined based on the corresponding auth method called before `verifyOTP` to sign up / sign-in a user.


### Parameters
  * emailOptionalString
One of `phone`, `email`, or `token_hash` must be provided.
  * phoneOptionalString
One of `phone`, `email`, or `token_hash` must be provided.
  * token_hashOptionalString
The token hash from the user's email link. One of `phone`, `email`, or `token_hash` must be provided.
  * typeRequiredEmailOTPType | MobileOTPType
  * tokenOptionalString
The OTP sent to the user. Required if using `phone` or `email`.
  * redirectToOptionalURL
A URL to redirect the user to after they are confirmed. Must be in your configured redirect URLs.
  * captchaTokenOptionalString
Deprecated.


Verify Sms One-Time Password (OTP)Verify Signup One-Time Password (OTP)
```

1
2
3
4
5
tryawait supabase.auth.verifyOTP( phone:"+13334445555", token:"123456", type: .sms)

```

## Retrieve a session
  * Returns the session, refreshing it if necessary. If no session can be found, a `GoTrueError.sessionNotFound` error is thrown.


Get the session dataGet the current session without validation
```

1
tryawait supabase.auth.session

```

## Retrieve a new session
  * This method will refresh the session whether the current one is expired or not.


Refresh session using the current sessionRefresh session using a refresh token
```

1
let session =tryawait supabase.auth.refreshSession()

```

## Retrieve a user
  * This method is useful for checking if the user is authorized because it validates the user's access token JWT on the server.
  * Fetches the user object from the database instead of local session.
  * Should be used only when you require the most current user data. For faster results, `session.user` is recommended.


Get the logged in user with the current existing sessionGet the logged in user with a custom access token jwtGet current user
```

1
let user =tryawait supabase.auth.user()

```

## Update a user
  * In order to use the `updateUser()` method, the user needs to be signed in first.
  * By default, email updates sends a confirmation link to both the user's current and new email. To only send a confirmation link to the user's new email, disable **Secure email change** in your project's [email auth provider settings](https://supabase.com/dashboard/project/_/auth/providers).


Update the email for an authenticated userUpdate the phone number for an authenticated userUpdate the password for an authenticated userUpdate the user's metadataUpdate the user's password with a nonce
```

1
tryawait supabase.auth.update(user: UserAttributes(email:"new@email.com"))

```

Response
Notes
## Retrieve identities linked to a user
  * The user needs to be signed in to call `userIdentities()`.


Returns a list of identities linked to the user
```

1
let identities =tryawait supabase.auth.userIdentities()

```

## Link an identity to a user
  * The **Enable Manual Linking** option must be enabled from your [project's authentication settings](https://supabase.com/dashboard/project/_/settings/auth).
  * The user needs to be signed in to call `linkIdentity()`.
  * If the candidate identity is already linked to the existing user or another user, `linkIdentity()` will fail.


Link an identity to a userLink an identity to a user with custom URL opening logic
```

1
tryawait supabase.auth.linkIdentity(provider: provider)

```

Notes
## Unlink an identity from a user
  * The **Enable Manual Linking** option must be enabled from your [project's authentication settings](https://supabase.com/dashboard/project/_/settings/auth).
  * The user needs to be signed in to call `unlinkIdentity()`.
  * The user must have at least 2 identities in order to unlink an identity.
  * The identity to be unlinked must belong to the user.


Unlink an identity
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
// retrieve all identites linked to a userlet identities =tryawait supabase.auth.userIdentities()// find the google identitylet googleIdentity = identities.first{$0.provider== .google}// unlink the google identitytryawait supabase.auth.unlinkIdentity(googleIdentity)

```

## Send a password reauthentication nonce
  * This method is used together with `update(user:)` when a user's password needs to be updated.
  * If you require your user to reauthenticate before updating their password, you need to enable the **Secure password change** option in your [project's email provider settings](https://supabase.com/dashboard/project/_/auth/providers).
  * A user is only require to reauthenticate before updating their password if **Secure password change** is enabled and the user **hasn't recently signed in**. A user is deemed recently signed in if the session was created in the last 24 hours.
  * This method will send a nonce to the user's email. If the user doesn't have a confirmed email address, the method will send the nonce to the user's confirmed phone number instead.


Send reauthentication nonce
```

1
tryawait supabase.auth.reauthenticate()

```

Notes
## Resend an OTP
  * Resends a signup confirmation, email change, or phone change email to the user.
  * Passwordless sign-ins can be resent by calling the `signInWithOTP()` method again.
  * Password recovery emails can be resent by calling the `resetPasswordForEmail()` method again.
  * This method only resends an email or phone OTP to the user if there an initial signup, email change, or phone change request was made.
  * You can specify a redirect URL when you resend an email link using the `emailRedirectTo` option.


Resend an email signup confirmationResend a phone signup confirmationResend email change emailResend phone change OTP
```

1
2
3
4
5
tryawait supabase.auth.resend( email:"email@example.com", type: .signup, emailRedirectTo: URL(string:"my-app-scheme://"))

```

Notes
## Set the session data
  * `setSession()` takes in a refresh token and uses it to get a new session.
  * The refresh token can only be used once to obtain a new session.
  * [Refresh token rotation](https://supabase.com/docs/reference/auth/config#refresh_token_rotation_enabled) is enabled by default on all projects to guard against replay attacks.
  * You can configure the [`REFRESH_TOKEN_REUSE_INTERVAL`](https://supabase.com/docs/reference/auth/config#refresh_token_reuse_interval) which provides a short window in which the same refresh token can be used multiple times in the event of concurrency or offline issues.


Refresh the session
```

1
tryawait supabase.auth.setSession(accessToken:"access_token", refreshToken:"refresh_token")

```

Notes
## Exchange an auth code for a session
  * Used when `flowType` is set to `pkce` in client options.


Exchange Auth Code
```

1
tryawait supabase.auth.exchangeCodeForSession(authCode:"34e770dd-9ff9-416c-87fa-43b31d7ef225")

```

## Auth MFA
This section contains methods commonly used for Multi-Factor Authentication (MFA) and are invoked behind the `supabase.auth.mfa` namespace.
Currently, we only support time-based one-time password (TOTP) as the 2nd factor. We don't support recovery codes but we allow users to enroll more than 1 TOTP factor, with an upper limit of 10.
Having a 2nd TOTP factor for recovery frees the user of the burden of having to store their recovery codes somewhere. It also reduces the attack surface since multiple recovery codes are usually generated compared to just having 1 backup TOTP factor.
## Enroll a factor
  * Currently, `totp` is the only supported `factorType`. The returned `id` should be used to create a challenge.
  * To create a challenge, see [`mfa.challenge()`](https://supabase.com/docs/reference/swift/auth-mfa-challenge).
  * To verify a challenge, see [`mfa.verify()`](https://supabase.com/docs/reference/swift/auth-mfa-verify).
  * To create and verify a challenge in a single step, see [`mfa.challengeAndVerify()`](https://supabase.com/docs/reference/swift/auth-mfa-challengeandverify).


Enroll a time-based, one-time password (TOTP) factor
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
let response =tryawait supabase.auth.mfa.enroll( params: MFAEnrollParams(  issuer:"optional issuer",  friendlyName:"optional friendly name"))// Use the id to create a challenge.// The challenge can be verified by entering the code generated from the authenticator app.// The code will be generated upon scanning the qrCode or entering the secret into the authenticator app.let id = response.idlet type = response.typelet qrCode = response.totp?.qrCodelet secret = response.totp?.secretlet uri = response.totp?.uri

```

## Create a challenge
  * An [enrolled factor](https://supabase.com/docs/reference/swift/auth-mfa-enroll) is required before creating a challenge.
  * To verify a challenge, see [`mfa.verify()`](https://supabase.com/docs/reference/swift/auth-mfa-verify).


Create a challenge for a factor
```

1
2
3
4
5
let response =tryawait supabase.auth.mfa.challenge( params: MFAChallengeParams(  factorId:"34e770dd-9ff9-416c-87fa-43b31d7ef225"))

```

## Verify a challenge
  * To verify a challenge, please [create a challenge](https://supabase.com/docs/reference/swift/auth-mfa-challenge) first.


Verify a challenge for a factor
```

1
2
3
4
5
6
7
let session =tryawait supabase.auth.mfa.verify( params: MFAVerifyParams(  factorId:"34e770dd-9ff9-416c-87fa-43b31d7ef225",  challengeId:"4034ae6f-a8ce-4fb5-8ee5-69a5863a7c15",  code:"123456"))

```

## Create and verify a challenge
  * An [enrolled factor](https://supabase.com/docs/swift/javascript/auth-mfa-enroll) is required before invoking `challengeAndVerify()`.
  * Executes [`mfa.challenge()`](https://supabase.com/docs/reference/swift/auth-mfa-challenge) and [`mfa.verify()`](https://supabase.com/docs/reference/swift/auth-mfa-verify) in a single step.


Create and verify a challenge for a factor
```

1
2
3
4
5
6
let session =tryawait supabase.auth.mfa.challengeAndVerify( params: MFAChallengeAndVerifyParams(  factorId:"34e770dd-9ff9-416c-87fa-43b31d7ef225",  code:"123456"))

```

## Unenroll a factor
Unenroll a factor
```

1
2
3
4
5
let response =tryawait supabase.auth.mfa.unenroll( params: MFAUnenrollParams(  factorId:"34e770dd-9ff9-416c-87fa-43b31d7ef225"))

```

## Get Authenticator Assurance Level
  * Authenticator Assurance Level (AAL) is the measure of the strength of an authentication mechanism.
  * In Supabase, having an AAL of `aal1` refers to having the 1st factor of authentication such as an email and password or OAuth sign-in while `aal2` refers to the 2nd factor of authentication such as a time-based, one-time-password (TOTP).
  * If the user has a verified factor, the `nextLevel` field will return `aal2`, else, it will return `aal1`.


Get the AAL details of a session
```

1
2
3
4
let aal =tryawait supabase.auth.mfa.getAuthenticatorAssuranceLevel()let currentLevel = aal.currentLevellet nextLevel = aal.nextLevellet currentAuthenticationMethods = aal.currentAuthenticationMethods

```

## Auth Admin
  * Any method under the `supabase.auth.admin` namespace requires a `service_role` key.
  * These methods are considered admin methods and should be called on a trusted server. Never expose your `service_role` key in the browser.


Create server-side auth client
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
importSupabaselet supabase =SupabaseClient( supabaseURL: supabaseURL, supabaseKey: serviceRoleKey)// Access auth admin apilet adminAuthClient = supabase.auth.admin

```

## Delete a user
  * The `deleteUser()` method requires the user's ID, which maps to the `auth.users.id` column.


Removes a user
```

1
2
3
tryawait supabase.auth.admin.deleteUser( id:"715ed5db-f090-4b8c-a067-640ecee36aa0")

```

## List all factors for a user
List all factors for a user
```

1
let factors =tryawait supabase.auth.mfa.listFactors()

```

## Invokes a Supabase Edge Function.
Invoke a Supabase Edge Function.
  * Requires an Authorization header.
  * When you pass in a body to your function, we automatically attach the Content-Type header for `String`, and `Data`. If it doesn't match any of these types we assume the payload is `json`, serialize it and attach the `Content-Type` header as `application/json`. You can override this behaviour by passing in a `Content-Type` header of your own.


Invocation with `Decodable` responseInvocation with custom responseInvocation with streamed responseError handlingPassing custom headersInvoking a Function in the UsEast1 regionCalling with DELETE HTTP verbCalling with GET HTTP verbPass additional query params
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
structResponse:Decodable {// Expected response definition}let response: Response =tryawait supabase.functions .invoke("hello",  options: FunctionInvokeOptions(   body: ["foo":"bar"]))

```

## Subscribe to channel
  * By default, Broadcast and Presence are enabled for all projects.
  * By default, listening to database changes is disabled for new projects due to database performance and security concerns. You can turn it on by managing Realtime's [replication](https://supabase.com/docs/guides/api#realtime-api-overview).
  * You can receive the "previous" data for updates and deletes by setting the table's `REPLICA IDENTITY` to `FULL` (e.g., `ALTER TABLE your_table REPLICA IDENTITY FULL;`).
  * Row level security is not applied to delete statements. When RLS is enabled and replica identity is set to full, only the primary key is sent to clients.
  * Use AsyncStream or callbacks for listening to changes.


Listen to broadcast messagesListen to broadcast messages using callbackListen to presence updatesListen to presence updates using callbackListen to all database changesListen to all database changes using callbackListen to a specific tableListen to a specific table using callbackListen to insertsListen to inserts using callbackListen to updatesListen to updates using callbackListen to deletesListen to deletes using callbackListen to row level changesListen to row level changes using callback
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
let channel = supabase.channel("room1")let broadcastStream = channel.broadcastStream(event:"cursor-pos")await channel.subscribe()Task{forawait message in broadcastStream {print("Cursor position received", message)}}await channel.broadcast( event:"cursor-pos", message: ["x": .double(.random(in:0...1)),"y": .double(.random(in:0...1)) ])

```

## Unsubscribe from a channel
Unsubscribes and removes Realtime channel from Realtime client.
  * Removing a channel is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes.
  * Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.
  * If you removed all channels, the client automatically disconnects from the Realtime websocket. This can be disabled in the Realtime config by setting `disconnectOnNoSubscriptions` to false.


Remove a channelUnsubscribe from a channel
```

1
2
3
4
let channel = supabase.channel("channelId")//...await supabase.removeChannel(channel)

```

## Unsubscribe from all channels
Unsubscribes and removes all Realtime channels from Realtime client.
  * Removing channels is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.
  * If you removed all channels, the client automatically disconnects from the Realtime websocket. This can be disabled in the Realtime config by setting `disconnectOnNoSubscriptions` to false.


Remove all channels
```

1
await supabase.removeAllChannels()

```

## Retrieve all channels
Returns all Realtime channels.
Get all channels
```

1
let channels = supabase.channels

```

## Create a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `insert`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Create bucket
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
tryawait supabase.storage .createBucket("avatars",  options: BucketOptions(   public:false,   allowedMimeTypes: ["image/png"],   fileSizeLimit:1024))

```

## Retrieve a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `select`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Get bucket
```

1
2
let bucket =tryawait supabase.storage .getBucket("avatars")

```

## List all buckets
  * RLS policy permissions required: 
    * `buckets` table permissions: `select`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


List buckets
```

1
2
tryawait supabase.storage .listBuckets()

```

## Update a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `select` and `update`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Update bucket
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
tryawait supabase.storage .updateBucket("avatars",  options: BucketOptions(   public:false,   fileSizeLimit:1024,   allowedMimeTypes: ["image/png"]))

```

## Delete a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `select` and `delete`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Delete bucket
```

1
2
tryawait supabase.storage .deleteBucket("avatars")

```

## Empty a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `select`
    * `objects` table permissions: `select` and `delete`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Empty bucket
```

1
2
tryawait supabase.storage .emptyBucket("avatars")

```

## Upload a file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: only `insert` when you are uploading new files and `select`, `insert` and `update` when you are upserting files
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Upload file
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
let fileName ="avatar1.png"tryawait supabase.storage .from("avatars") .upload(  path:"public/\(fileName)",  file: fileData,  options: FileOptions(   cacheControl:"3600",   contentType:"image/png",   upsert:false))

```

## Download a file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Download fileDownload file with transformations
```

1
2
3
let data =tryawait supabase.storage .from("avatars") .download(path:"folder/avatar1.png")

```

## List all files in a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


List files in a bucketSearch files in a bucket
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
let files =tryawait supabase.storage .from("avatars") .list(  path:"folder",  options: SearchOptions(   limit:100,   offset:0,   sortBy: SortBy(column:"name", order:"asc")))

```

## Replace an existing file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `update` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Update file
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
let fileName ="avatar1.png"tryawait supabase.storage .from("avatars") .update(  path:"public/\(fileName)",  file: fileData,  options: FileOptions(   cacheControl:"3600",   contentType:"image/png",   upsert:true))

```

## Move an existing file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `update` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Move file
```

1
2
3
4
tryawait supabase .storage .from("avatars") .move(from:"public/avatar1.png", to:"private/avatar2.png")

```

## Copy an existing file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `insert` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Copy file
```

1
2
3
4
tryawait supabase .storage .from("avatars") .copy(from:"public/avatar1.png", to:"private/avatar2.png")

```

## Delete files in a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `delete` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Delete file
```

1
2
3
tryawait supabase.storage .from("avatars") .remove(paths: ["folder/avatar1.png"])

```

## Create a signed URL
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Create Signed URLCreate a signed URL for an asset with transformationsCreate a signed URL which triggers the download of the asset
```

1
2
3
let signedURL =tryawait supabase.storage .from("avatars") .createSignedURL(path:"folder/avatar1.png", expiresIn:60)

```

## Create signed URLs
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Create Signed URLs
```

1
2
3
4
let urls =tryawait supabase .storage .from("avatars") .createSignedURLs(paths: ["folder/avatar1.png", "folder/avatar2.png"], expiresIn:60)

```

## Retrieve public URL
  * The bucket needs to be set to public, either via [updateBucket()](https://supabase.com/docs/reference/javascript/storage-updatebucket) or by going to Storage on [supabase.com/dashboard](https://supabase.com/dashboard), clicking the overflow menu on a bucket and choosing "Make public"
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Returns the URL for an asset in a public bucketReturns the URL for an asset in a public bucket with transformationsReturns the URL which triggers the download of an asset in a public bucket
```

1
2
3
let publicURL =try supabase.storage .from("public-bucket") .getPublicURL(path:"folder/avatar1.png")

```

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



