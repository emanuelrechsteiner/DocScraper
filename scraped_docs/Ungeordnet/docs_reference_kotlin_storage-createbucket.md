---
url: https://supabase.com/docs/reference/kotlin/storage-createbucket
scraped_at: 2025-05-25T09:16:28.265768
title: Kotlin API Reference | Supabase Docs
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
kotlin
v3.0
  * [Introduction](https://supabase.com/docs/reference/kotlin/introduction)
  * [Installing](https://supabase.com/docs/reference/kotlin/installing)
  * [Initializing](https://supabase.com/docs/reference/kotlin/initializing)
  * Database
    * [Fetch data](https://supabase.com/docs/reference/kotlin/select)
    * [Insert data](https://supabase.com/docs/reference/kotlin/insert)
    * [Update data](https://supabase.com/docs/reference/kotlin/update)
    * [Upsert data](https://supabase.com/docs/reference/kotlin/upsert)
    * [Delete data](https://supabase.com/docs/reference/kotlin/delete)
    * [Call a Postgres function](https://supabase.com/docs/reference/kotlin/rpc)
    * Using filters
    * Using modifiers
  * Auth
    * [Overview](https://supabase.com/docs/reference/kotlin/auth-api)
    * [Create a new user](https://supabase.com/docs/reference/kotlin/auth-signup)
    * [Listen to auth events](https://supabase.com/docs/reference/kotlin/auth-onauthstatechange)
    * [Create an anonymous user](https://supabase.com/docs/reference/kotlin/auth-signinanonymously)
    * [Sign in a user](https://supabase.com/docs/reference/kotlin/auth-signinwithpassword)
    * [Sign in with ID Token](https://supabase.com/docs/reference/kotlin/auth-signinwithidtoken)
    * [Sign in a user through OTP](https://supabase.com/docs/reference/kotlin/auth-signinwithotp)
    * [Sign in a user through OAuth](https://supabase.com/docs/reference/kotlin/auth-signinwithoauth)
    * [Sign in a user through SSO](https://supabase.com/docs/reference/kotlin/auth-signinwithsso)
    * [Sign out a user](https://supabase.com/docs/reference/kotlin/auth-signout)
    * [Send a password reset request](https://supabase.com/docs/reference/kotlin/auth-resetpasswordforemail)
    * [Verify and log in through OTP](https://supabase.com/docs/reference/kotlin/auth-verifyotp)
    * [Retrieve a session](https://supabase.com/docs/reference/kotlin/auth-getsession)
    * [Retrieve a new session](https://supabase.com/docs/reference/kotlin/auth-refreshsession)
    * [Retrieve a user](https://supabase.com/docs/reference/kotlin/auth-getuser)
    * [Update a user](https://supabase.com/docs/reference/kotlin/auth-updateuser)
    * [Retrieve identities linked to a user](https://supabase.com/docs/reference/kotlin/auth-getuseridentities)
    * [Link an identity to a user](https://supabase.com/docs/reference/kotlin/auth-linkidentity)
    * [Unlink an identity from a user](https://supabase.com/docs/reference/kotlin/auth-unlinkidentity)
    * [Send a password reauthentication nonce](https://supabase.com/docs/reference/kotlin/auth-reauthentication)
    * [Resend an OTP](https://supabase.com/docs/reference/kotlin/auth-resend)
    * [Set the session data](https://supabase.com/docs/reference/kotlin/auth-setsession)
    * [Exchange an auth code for a session](https://supabase.com/docs/reference/kotlin/auth-exchangecodeforsession)
    * Auth MFA
    * Auth Admin
  * Edge Functions
    * [Invokes a Supabase Edge Function.](https://supabase.com/docs/reference/kotlin/functions-invoke)
  * Realtime
    * [Listen to database changes](https://supabase.com/docs/reference/kotlin/stream)
    * [Subscribe to channel](https://supabase.com/docs/reference/kotlin/subscribe)
    * [Unsubscribe from a channel](https://supabase.com/docs/reference/kotlin/removechannel)
    * [Unsubscribe from all channels](https://supabase.com/docs/reference/kotlin/removeallchannels)
    * [Retrieve all channels](https://supabase.com/docs/reference/kotlin/getchannels)
    * [Broadcast a message](https://supabase.com/docs/reference/kotlin/broadcastmessage)
  * Storage
    * [Create a bucket](https://supabase.com/docs/reference/kotlin/storage-createbucket)
    * [Retrieve a bucket](https://supabase.com/docs/reference/kotlin/storage-getbucket)
    * [List all buckets](https://supabase.com/docs/reference/kotlin/storage-listbuckets)
    * [Update a bucket](https://supabase.com/docs/reference/kotlin/storage-updatebucket)
    * [Delete a bucket](https://supabase.com/docs/reference/kotlin/storage-deletebucket)
    * [Empty a bucket](https://supabase.com/docs/reference/kotlin/storage-emptybucket)
    * [Upload a file](https://supabase.com/docs/reference/kotlin/storage-from-upload)
    * [Download a file](https://supabase.com/docs/reference/kotlin/storage-from-download)
    * [List all files in a bucket](https://supabase.com/docs/reference/kotlin/storage-from-list)
    * [Replace an existing file](https://supabase.com/docs/reference/kotlin/storage-from-update)
    * [Move an existing file](https://supabase.com/docs/reference/kotlin/storage-from-move)
    * [Copy an existing file](https://supabase.com/docs/reference/kotlin/storage-from-copy)
    * [Delete files in a bucket](https://supabase.com/docs/reference/kotlin/storage-from-remove)
    * [Create a signed URL](https://supabase.com/docs/reference/kotlin/storage-from-createsignedurl)
    * [Create signed URLs](https://supabase.com/docs/reference/kotlin/storage-from-createsignedurls)
    * [Create signed upload URL](https://supabase.com/docs/reference/kotlin/storage-from-createsigneduploadurl)
    * [Upload to a signed URL](https://supabase.com/docs/reference/kotlin/storage-from-uploadtosignedurl)
    * [Retrieve public URL](https://supabase.com/docs/reference/kotlin/storage-from-getpublicurl)


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
Kotlin Reference v3.0
# kotlin Client Library
@supabase-community/supabase-kt[View on GitHub](https://github.com/supabase-community/supabase-kt)
This reference documents every object and method available in Supabase's Kotlin Multiplatform library, [supabase-kt](https://github.com/supabase-community/supabase-kt). You can use supabase-kt to interact with your Postgres database, listen to database changes, invoke Deno Edge Functions, build login and user management functionality, and manage large files.
To see supported Kotlin targets, check the corresponding module README on [GitHub](https://github.com/supabase-community/supabase-kt).
To migrate from version 2.X to 3.0.0, see the [migration guide](https://github.com/supabase-community/supabase-kt/blob/master/MIGRATION.md)
The Kotlin client library is created and maintained by the Supabase community, and is not an official library. Please be tolerant of areas where the library is still being developed, and — as with all the libraries — feel free to contribute wherever you find issues.
Huge thanks to official maintainer, [jan-tennert](https://github.com/jan-tennert).
## Installing
### Add one or more modules to your project[#](https://supabase.com/docs/reference/kotlin/storage-createbucket#add-one-or-more-modules-to-your-project)
[![latest stable supabase-kt version](https://img.shields.io/github/release/supabase-community/supabase-kt?label=stable)](https://github.com/supabase-community/supabase-kt/releases)[![latest supabase-kt version](https://img.shields.io/maven-central/v/io.github.jan-tennert.supabase/supabase-kt?label=experimental)](https://github.com/supabase-community/supabase-kt/releases)
Add dependency to your build file using the BOM.
The available modules are:
  * [**auth-kt**](https://github.com/supabase-community/supabase-kt/tree/master/Auth)
  * [**realtime-kt**](https://github.com/supabase-community/supabase-kt/tree/master/Realtime)
  * [**storage-kt**](https://github.com/supabase-community/supabase-kt/tree/master/Storage)
  * [**functions-kt**](https://github.com/supabase-community/supabase-kt/tree/master/Functions)
  * [**postgrest-kt**](https://github.com/supabase-community/supabase-kt/tree/master/Postgrest)
  * Other plugins also available [here](https://github.com/supabase-community/supabase-kt/tree/master/plugins)


Checkout the different READMEs for information about supported Kotlin targets.
_Note that the minimum Android SDK version is 26. For lower versions, you need to enable[core library desugaring](https://developer.android.com/studio/write/java8-support#library-desugaring)._
build.gradle.ktsbuild.gradlepom.xml
```

1
2
3
4
implementation(platform("io.github.jan-tennert.supabase:bom:VERSION"))implementation("io.github.jan-tennert.supabase:postgrest-kt")implementation("io.github.jan-tennert.supabase:auth-kt")implementation("io.github.jan-tennert.supabase:realtime-kt")

```

### Add Ktor Client Engine to each of your Kotlin targets (required)[#](https://supabase.com/docs/reference/kotlin/storage-createbucket#add-ktor-client-engine-to-each-of-your-kotlin-targets-required)
You can find a list of engines [here](https://ktor.io/docs/http-client-engines.html)
  * Note that not all Ktor engines support Websockets. So if you plan to use the Realtime module, make sure to use an engine that supports Websockets. Checkout the [engine limitations](https://ktor.io/docs/client-engines.html#limitations) for more information.
  * If using `supabase-kt` 3.0.0 and above, you need to use Ktor version 3.0.0-rc-1 or later.


build.gradle.ktsbuild.gradlepom.xml
```

1
implementation("io.ktor:ktor-client-[engine]:KTOR_VERSION")

```

Multiplatform example:
build.gradle.kts
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
val commonMain bygetting {dependencies {//supabase modules  }}val jvmMain bygetting {dependencies {implementation("io.ktor:ktor-client-cio:KTOR_VERSION")  }}val androidMain bygetting {dependsOn(jvmMain)}val jsMain bygetting {dependencies {implementation("io.ktor:ktor-client-js:KTOR_VERSION")  }}val iosMain bygetting {dependencies {implementation("io.ktor:ktor-client-darwin:KTOR_VERSION")  }}

```

### Serialization[#](https://supabase.com/docs/reference/kotlin/storage-createbucket#serialization)
supabase-kt provides several different ways to encode and decode your custom objects. By default, [KotlinX Serialization](https://github.com/Kotlin/kotlinx.serialization) is used.
Use [KotlinX Serialization](https://github.com/Kotlin/kotlinx.serialization).
build.gradle.ktsbuild.gradlepom.xml
```

1
2
3
plugins {kotlin("plugin.serialization") version "KOTLIN_VERSION"}

```

```

1
2
3
4
5
6
val supabase =createSupabaseClient(supabaseUrl, supabaseKey) {//Already the default serializer, but you can provide a custom Json instance (optional):  defaultSerializer =KotlinXSerializer(Json {//apply your custom config  })}

```

Use [Moshi](https://github.com/square/moshi).
build.gradle.ktsbuild.gradlepom.xml
```

1
implementation("io.github.jan-tennert.supabase:serializer-moshi:VERSION")

```

```

1
2
3
val supabase =createSupabaseClient(supabaseUrl, supabaseKey) {  defaultSerializer =MoshiSerializer()}

```

Use [Jackson](https://github.com/FasterXML/jackson-module-kotlin).
build.gradle.ktsbuild.gradlepom.xml
```

1
implementation("io.github.jan-tennert.supabase:serializer-jackson:VERSION")

```

```

1
2
3
val supabase =createSupabaseClient(supabaseUrl, supabaseKey) {  defaultSerializer =JacksonSerializer()}

```

Use custom serializer.
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
classCustomSerializer: SupabaseSerializer {overridefun <T : Any> encode(type: KType, value: T): String {//encode value to string  }overridefun <T : Any> decode(type: KType, value: String): T {//decode value  }}

```

```

1
2
3
val supabase =createSupabaseClient(supabaseUrl, supabaseKey) {  defaultSerializer =CustomSerializer()}

```

## Initializing
### Create Supabase Client[#](https://supabase.com/docs/reference/kotlin/storage-createbucket#create-supabase-client)
Independently of which Supabase module you are using, you will need to initialize the main client first and install the module.
To create a new client, you can use the `createSupabaseClient` function.
When installing a module, you can pass a block to configure it.
### OAuth and OTP link verification[#](https://supabase.com/docs/reference/kotlin/storage-createbucket#oauth-and-otp-link-verification)
[supabase-kt](https://github.com/supabase-community/supabase-kt) provides several platform implementations for OAuth and OTP link verification.
**On Desktop platforms (JVM, MacOS*, Linux, Windows)** , it uses a HTTP Callback Server to receive the session data from a successful OAuth login. The success page can be customized via `AuthConfig#httpCallbackConfig` * If no deeplinks are being used.
_Note: OTP link verification such as sign ups are not supported on JVM. You may have to send a verification token rather than a url in your email. To send the token, rather than a redirect url, change`{{ .ConfirmationURL }}` in your sign up email to `{{ .Token }}`_
**On Android, iOS & MacOS**, OAuth and OTP verification use deeplinks. Refer to the guide below on how to setup deeplinks. Alternatively you can use [Native Google Auth](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=android). **On JS** , it uses the website origin as the callback url. Session importing gets handled automatically. **tvOS & watchOS** currently have no default implementation. Feel free to create a PR.
You always make your own implementation and use `auth.parseSessionFromFragment(fragment)` or `auth.parseSessionFromUrl(url)` to let [supabase-kt](https://github.com/supabase-community/supabase-kt) handle the parsing after receiving a callback. Then you can simply use `auth.importSession(session)`.
### Configure deeplink callbacks for Authentication[#](https://supabase.com/docs/reference/kotlin/storage-createbucket#configure-deeplink-callbacks-for-authentication)
Deeplinks are supported on Android, iOS and MacOS.
  1. **Set up a deeplink** On Android, set up a [deeplink](https://developer.android.com/training/app-links/deep-linking) in your Android manifest. On iOS and MacOS, set up a [url scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app).
  2. **Add your deeplink to the[redirect URLs](https://supabase.com/dashboard/project/_/auth/url-configuration)** **Pattern** : scheme://host
  3. **Configure the Auth plugin** Set the `host` and `scheme` in the Auth config: 
```

1
2
3
4
5
6
7
install(Auth) {  host ="deeplink host"// this can be anything, eg. your package name or app/company url (not your Supabase url)  scheme ="deeplink scheme"// On Android only, you can set OAuth and SSO logins to open in a custom tab, rather than an external browser:  defaultExternalAuthAction = ExternalAuthAction.CustomTabs() //defaults to ExternalAuthAction.ExternalBrowser}

```

  4. **Call platform specific function on startup** On Android: `supabase.handleDeeplinks(intent)` If you don't want a separate activity, just call this function at the top of your `onCreate` function in your MainActivity. On iOS/MacOS: `supabase.handleDeeplinks(url)`


Then you can log in using OAuth:
```

1
supabase.auth.signInWith(Google)

```

Or open OTP links directly in your app.
### PKCE Authentication flow[#](https://supabase.com/docs/reference/kotlin/storage-createbucket#pkce-authentication-flow)
supabase-kt supports the [PKCE authentication flow](https://supabase.com/blog/supabase-auth-sso-pkce). To use it, change the `flowType` in the Auth configuration:
```

1
2
3
install(Auth) { flowType = FlowType.PKCE}

```

That's it! If you already implemented deeplinks to handle OTPs and OAuth you don't have to change anything!
### Parameters
  * supabaseUrlRequiredString
The unique Supabase URL which is supplied when you create a new project in your project dashboard.
  * supabaseKeyRequiredString
The unique Supabase Key which is supplied when you create a new project in your project dashboard.
  * builderOptionalSupabaseClientBuilder.() -> Unit
Apply additional configuration and install plugins.
Details


Initialize ClientConfigure Auth moduleConfigure PostgREST moduleConfigure Storage moduleConfigure Realtime moduleConfigure Functions pluginConfigure GraphQL plugin
```

1
2
3
4
5
6
7
8
val supabase =createSupabaseClient(  supabaseUrl ="https://xyzcompany.supabase.co",  supabaseKey ="public-anon-key") {install(Auth)install(Postgrest)//install other modules}

```

## Fetch data
Perform a SELECT query on the table or view.
  * When calling a `decode` method, you have to provide a [serializable class](https://supabase.com/docs/reference/kotlin/installing#serialization) as the type parameter.
  * You can provide a `Columns` object to select specific columns.
  * You can provide a [filter](https://supabase.com/docs/reference/kotlin/using-filters) block to filter the results


### Parameters
  * columnsOptionalColumns
The columns to retrieve, defaults to `Columns.ALL`. You can also use `Columns.list`, `Columns.type` or `Columns.raw` to specify the columns.
  * headOptionalBoolean
If true, select will delete the selected data.
  * requestOptionalPostgrestRequestBuilder.() -> Unit
Additional configuration & filtering for the request.


Getting your dataSelecting specific columnsQuery foreign tablesQuery the same foreign table multiple timesQuerying with count optionQuerying JSON data
```

1
val city = supabase.from("cities").select().decodeSingle<City>()

```

## Insert data
Perform an INSERT into the table or view.
  * When calling an `insert` method, you have to provide a [serializable value](https://supabase.com/docs/reference/kotlin/installing#serialization).
  * By default, `insert` will not return the inserted data. If you want to return the inserted data, you can use the `select()` method inside the request.


### Parameters
  * valueRequiredT or List<T>
The value(s) you want to insert. `T` can be any serializable type.
  * requestOptionalPostgrestRequestBuilder.() -> Unit
Additional configuration & filtering for the request.


Create a recordCreate a record and return itBulk create
```

1
2
val city =City(name ="The Shire", countryId =554)supabase.from("cities").insert(city)

```

## Update data
Perform an UPDATE on the table or view.
  * `update()` should always be combined with a [filter](https://supabase.com/docs/reference/kotlin/using-filters) block to avoid updating all records.
  * When calling `insert` or `update`, you have to provide a [serializable value](https://supabase.com/docs/reference/kotlin/installing#serialization) in the function parameter.
  * By default, `update` will not return the inserted data. If you want to return the inserted data, you can use the `select()` method inside the request.


### Parameters
  * valueRequiredT or PostgrestUpdate.() -> Unit = {}
The new value, can be either a serializable value or PostgrestUpdate DSL where you can set new values per column.
  * requestOptionalPostgrestRequestBuilder.() -> Unit
Additional configuration & filtering for the request.


Updating your dataUpdate a record and return itUpdating JSON data
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
supabase.from("characters").update(  {    Country::name setTo "Han Solo"//orset("name", "Han Solo")  }) {filter {    Character::id eq 1//oreq("id", 1)  }}

```

## Upsert data
Perform an UPSERT on the table or view. Depending on the column(s) passed to `onConflict`, `.upsert()` allows you to perform the equivalent of `.insert()` if a row with the corresponding `onConflict` columns doesn't exist, or if it does exist, perform an alternative action depending on `ignoreDuplicates`.
  * Primary keys should be included in the data payload in order for an update to work correctly.
  * Primary keys must be natural, not surrogate. There are however, [workarounds](https://github.com/PostgREST/postgrest/issues/1118) for surrogate primary keys.
  * If you need to insert new data and update existing data at the same time, use [Postgres triggers](https://github.com/supabase/postgrest-js/issues/173#issuecomment-825124550).
  * When calling `insert` or `update`, you have to provide a [serializable value](https://supabase.com/docs/reference/kotlin/installing#serialization) in the function parameter.
  * By default, `upsert` will not return the inserted data. If you want to return the inserted data, you can use the `select()` method inside the request.


### Parameters
  * valueRequiredT or List<T>
The value(s) you want to insert. `T` can be any serializable type.
  * requestOptionalPostgrestRequestBuilder.() -> Unit
Additional configuration & filtering for the request.


Upsert your dataUpsert your data and return itUpserting into tables with constraintsReturn the exact number of rows
```

1
2
val toUpsert =Message(id =3, message ="foo", username ="supabot")supabase.from("messages").upsert(toUpsert)

```

## Delete data
Perform a DELETE on the table or view.
  * `delete()` should always be combined with a [filter](https://supabase.com/docs/reference/kotlin/using-filters) block to target the item(s) you wish to delete.
  * If you use `delete()` with filters and you have [RLS](https://supabase.com/docs/learn/auth-deep-dive/auth-row-level-security) enabled, only rows visible through `SELECT` policies are deleted. Note that by default no rows are visible, so you need at least one `SELECT`/`ALL` policy that makes the rows visible.
  * By default, `delete` will not return the deleted data. If you want to return the deleted data, you can use the `select()` method inside the request.


### Parameters
  * requestOptionalPostgrestRequestBuilder.() -> Unit
Additional configuration & filtering for the request.


Delete recordsFetch deleted records
```

1
2
3
4
5
6
7
supabase.from("cities").delete {filter {    City::id eq 666//oreq("id", 666)  }}

```

## Call a Postgres function
You can call stored procedures as a "Remote Procedure Call".
That's a fancy way of saying that you can put some logic into your database then call it from anywhere. It's especially useful when the logic rarely changes - like password resets and updates.
  * When calling `rpc` with parameters, you have to provide a [serializable value](https://supabase.com/docs/reference/kotlin/installing#serialization) in the function parameter.


### Parameters
  * functionRequiredString
The name of the function
  * parametersOptionalT
Parameters to pass to the function. T can be any serializable type.
  * requestOptionalPostgrestRequestBuilder.() -> Unit
Additional configuration & filtering for the request.


Call a stored procedureWith Parameters
```

1
supabase.postgrest.rpc("hello_world")

```

Notes
## Using filters
Filters allow you to only return rows that match certain conditions.
Filters can be used on `select()`, `update()`, and `delete()` queries.
You can use two different types for applying filters:
```

1
eq("country_id", 1)

```

And using a class property:
```

1
City::countryId eq 1

```

As you can see on the property syntax: the name of the `countryId` gets converted to `country_id`.
By default, this is done by converting camel case to snake case, but you can customize this by changing the `propertyConversionMethod` in the Postgrest Config
If a database function returns a table response, you can also apply filters.
Applying a filter blockMultiple filters on one columnFilter by values within a JSON columnFilter Foreign Tables
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name", "country_id")) {filter {    City::name eq "The Shire"//oreq("name", "The Shire")  }}

```

Notes
## Column is equal to a value
Finds all rows whose value on the stated `column` exactly matches the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredAny
The value to filter with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name", "country_id")) {filter {    City::name eq "The Shire"//oreq("name", "The Shire")  }}

```

## Column is not equal to a value
Finds all rows whose value on the stated `column` doesn't match the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredAny
The value to filter with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name", "country_id")) {filter {    City::name neq "The Shire"//orneq("name", "The Shire")  }}

```

## Column is greater than a value
Finds all rows whose value on the stated `column` is greater than the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredAny
The value to filter with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::countryId gt 300//orgt("country_id", 300)  }}

```

## Column is greater than or equal to a value
Finds all rows whose value on the stated `column` is greater than or equal to the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredAny
The value to filter with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::countryId gte 300//orgte("country_id", 300)  }}

```

## Column is less than a value
Finds all rows whose value on the stated `column` is less than the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredAny
The value to filter with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::countryId lt 300//orlt("country_id", 300)  }}

```

## Column is less than or equal to a value
Finds all rows whose value on the stated `column` is less than or equal to the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredAny
The value to filter with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::countryId lte 300//orlte("country_id", 300)  }}

```

## Column matches a pattern
Finds all rows whose value in the stated `column` matches the supplied `pattern` (case sensitive).
### Parameters
  * columnRequiredString
The column to filter on.
  * patternRequiredString
The pattern to match with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::name like "%la%"//orlike("name", "%la%")  }}

```

## Column matches a case-insensitive pattern
Finds all rows whose value in the stated `column` matches the supplied `pattern` (case insensitive).
### Parameters
  * columnRequiredString
The column to filter on.
  * patternRequiredString
The pattern to match with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::name ilike "%la%"//orilike("name", "%la%")  }}

```

## Column is a value
A check for exact equality (null, true, false), finds all rows whose value on the stated `column` exactly match the specified `value`.
`is_` and `in_` filter methods are suffixed with `_` to avoid collisions with reserved keywords.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredBoolean?
The value to filter with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::name isExact null//orexact("name", null)  }}

```

## Column is in an array
Finds all rows whose value on the stated `column` is found on the specified `values`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valuesRequiredList<Any>
The values to filter with.


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::name isIn listOf("Hobbiton", "Edoras")//orisIn("name", listOf("Hobbiton", "Edoras"))  }}

```

## Column contains every element in a value
Only relevant for jsonb, array, and range columns. Match only rows where `column` contains every element appearing in `value`.
### Parameters
  * columnRequiredString
The jsonb, array, or range column to filter on
  * valueRequiredList<Any>
The jsonb, array, or range value to filter with


With `select()`With `update()`With `delete()`With `rpc()`
```

1
2
3
4
5
6
7
supabase.from("cities").select(columns = Columns.list("name")) {filter {    City::mainExports contains listOf("oil")//orcontains("main_exports", listOf("oil"))  }}

```

## Greater than a range
Only relevant for range columns. Match only rows where every element in column is greater than any element in range.
### Parameters
  * columnRequiredString
The column to filter on.
  * valuesRequiredPair<Any, Any>
The values to filter with.


With `select()`
```

1
2
3
4
5
6
7
supabase.from("reservations").select {filter {     Reservation::duringrangeGt ("2000-01-02 08:30" to "2000-01-02 09:30")//orrangeGt("during", "2000-01-02 08:30" to "2000-01-02 09:30")   } }

```

Data source
Response
Notes
## Greater than or equal to a range
Only relevant for range columns. Match only rows where every element in column is either contained in range or greater than any element in range.
### Parameters
  * columnRequiredString
The column to filter on.
  * valuesRequiredPair<Any, Any>
The values to filter with.


With `select()`
```

1
2
3
4
5
6
7
supabase.from("reservations").select {filter {     Reservation::duringrangeGte ("2000-01-02 08:30" to "2000-01-02 09:30")//orrangeGte("during", "2000-01-02 08:30" to "2000-01-02 09:30")   } }

```

Data source
Response
Notes
## Less than a range
Only relevant for range columns. Match only rows where every element in column is less than any element in range.
### Parameters
  * columnRequiredString
The column to filter on.
  * valuesRequiredPair<Any, Any>
The values to filter with.


With `select()`
```

1
2
3
4
5
6
7
supabase.from("reservations").select {filter {     Reservation::duringrangeLt ("2000-01-02 08:30" to "2000-01-02 09:30")//orrangeLt("during", "2000-01-02 08:30" to "2000-01-02 09:30")   } }

```

Data source
Response
Notes
## Less than or equal to a range
Only relevant for range columns. Match only rows where every element in column is either contained in range or less than any element in range.
### Parameters
  * columnRequiredString
The column to filter on.
  * valuesRequiredPair<Any, Any>
The values to filter with.


With `select()`
```

1
2
3
4
5
6
7
supabase.from("reservations").select {filter {     Reservation::duringrangeLte ("2000-01-02 08:30" to "2000-01-02 09:30")//orrangeLte("during", "2000-01-02 08:30" to "2000-01-02 09:30")   } }

```

Data source
Response
Notes
## Mutually exclusive to a range
Only relevant for range columns. Match only rows where column is mutually exclusive to range and there can be no element between the two ranges.
### Parameters
  * columnRequiredString
The column to filter on.
  * valuesRequiredPair<Any, Any>
The values to filter with.


With `select()`
```

1
2
3
4
5
6
7
supabase.from("reservations").select {filter {     Reservation::duringadjacent ("2000-01-02 08:30" to "2000-01-02 09:30")//oradjacent("during", "2000-01-02 08:30" to "2000-01-02 09:30")   } }

```

Data source
Response
## With a common element
Only relevant for array and range columns. Match only rows where column and value have an element in common.
### Parameters
  * columnRequiredString
The column to filter on.
  * valuesRequiredList<Any>
The values to filter with.


On array columnsOn range columns
```

1
2
3
4
5
6
7
supabase.from("issues").select(columns = Columns.list("title")) {filter {    Issue::tags overlaps listOf("is:closed", "severity:high")//oroverlaps("tags", listOf("is:closed", "severity:high"))  }}

```

Data source
Response
## Match a string
Only relevant for text and tsvector columns. Match only rows where `column` matches the query string in `query`.
For more information, see [Postgres full text search](https://supabase.com/docs/guides/database/full-text-search).
### Parameters
  * columnRequiredString
The text or tsvector column to filter on
  * queryRequiredString
The query text to match with
  * textSearchTypeOptionalTextSearchType
The type of text search to use. Defaults to `TextSearchType.NONE`.
  * configOptionalString
The text search configuration to use.


Text searchSearch multiple columnsBasic normalizationFull normalizationWebsearch
```

1
2
3
4
5
supabase.from("quotes").select(columns = Columns.list("catchphrase")) {filter {textSearch(column ="catchphrase", query ="'fat' & 'cat'", config ="english", type = TextSearchType.YOUR_TYPE)  }}

```

## Don't match the filter
Finds all rows that don't satisfy the filter.
  * `.filterNot()` expects you to use the raw [PostgREST syntax](https://postgrest.org/en/stable/api.html#horizontal-filtering-rows) for the filter names and values.


### Parameters
  * columnRequiredString
The column to filter on.
  * operatorRequiredFilterOperator
The operator to use for the filter.
  * valueRequiredAny
The value to filter with.


With `select()`
```

1
2
3
4
5
supabase.from("countries").select {filter {filterNot("name", FilterOperation.IS, "")  }}

```

## Match at least one filter
Finds all rows satisfying at least one of the filters.
### Parameters
  * negateOptionalBoolean
If true, negate the entire block.
  * blockRequiredPostgrestFilterBuilder.() -> Unit
The block to apply the `or` filter to.


With `select()`Use `or` with `and`
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
supabase.from("countries").select(columns = Columns.list("name")) {filter {or {      Country::id eq 2      Country::name eq "Mordor"//oreq("id", 2)eq("name", "Mordor")    }  }}

```

## Match the filter
filter() expects you to use the raw PostgREST syntax for the filter values.
### Parameters
  * columnRequiredString
The column to filter on.
  * operatorRequiredFilterOperator
The operator to use for the filter.
  * valueRequiredAny
The value to filter with.


With `select()`On a foreign table
```

1
2
3
4
5
supabase.from("characters").select {filter {filter(column ="name", operator= FilterOperator.IN, value="('Han', 'Katniss')")  }}

```

Data source
Response
## Using modifiers
Filters work on the row level—they allow you to return rows that only match certain conditions without changing the shape of the rows. Modifiers are everything that don't fit that definition—allowing you to change the format of the response (e.g., returning a CSV string).
Modifiers are be specified next to the filter block. Some modifiers only apply for queries that return rows (e.g., `select()` or `rpc()` on a function that returns a table response).
## Return data after inserting
### Parameters
  * columnsOptionalColumns
The columns to select.


With `upsert()`
```

1
2
3
4
val toUpsert =Country(id =2, name ="Mordor")val count = supabase.from("countries").upsert(toUpsert) {select()}.decodeSingle<Country>()

```

Data source
Response
## Order the results
Order the query result by column.
### Parameters
  * columnRequiredString
The column to order by.
  * orderRequiredOrder
The order to use.
  * nullsFirstOptionalBoolean
Whether to order nulls first.
  * referencedTableOptionalString
The foreign table to order by.


With `select()`On a foreign tableOrder parent table by a referenced table
```

1
2
3
supabase.from("characters").select(columns = Columns.list("id", "name")) {order(column ="id", order = Order.DESCENDING)}

```

Data source
Response
## Limit the number of rows returned
Limit the query result by count.
### Parameters
  * countRequiredLong
The number of rows to limit the result to.
  * referencedTableOptionalString
The foreign table to limit by.


With `select()`On a foreign table
```

1
2
3
supabase.from("characters").select {limit(count =1)}

```

Data source
Response
## Limit the query to a range
Limit the query result by from and to inclusively.
### Parameters
  * fromRequiredLong
The start of the range.
  * toRequiredLong
The end of the range.
  * referencedTableOptionalString
The foreign table to limit by.


With `select()`
```

1
2
3
supabase.from("characters").select {range(1L..5L)}

```

Data source
Response
## Retrieve one row of data
With `select()`
```

1
2
3
4
val result = supabase.from("characters").select(Columns.list("name")) {limit(1)single()}

```

Data source
Response
## Retrieve as a CSV
Return data as CSV
```

1
2
3
val (csvData, _) = supabase.from("characters").select {csv()}

```

Data source
Response
Notes
## Using explain
For debugging slow queries, you can get the [Postgres `EXPLAIN` execution plan](https://www.postgresql.org/docs/current/sql-explain.html) of a query using the `explain()` method. This works on any query, even for `rpc()` or writes.
Explain is not enabled by default as it can reveal sensitive information about your database. It's best to only enable this for testing environments but if you wish to enable it for production you can provide additional protection by using a `pre-request` function.
Follow the [Performance Debugging Guide](https://supabase.com/docs/guides/api/rest/debugging-performance) to enable the functionality on your project.
### Parameters
  * analyzeOptionalBoolean
If `true`, the query will be executed and the actual run time will be returned
  * verboseOptionalBoolean
If `true`, the query identifier will be returned and `data` will include the output columns of the query
  * settingsOptionalBoolean
If `true`, include information on configuration parameters that affect query planning
  * buffersOptionalBoolean
If `true`, include information on buffer usage
  * walOptionalBoolean
If `true`, include information on WAL record generation
  * formatOptionalString
The format of the output, can be `"text"` (default) or `"json"`


Get the execution plan
```

1
2
3
val result = supabase.from("characters").select {explain()}

```

Data source
Response
Notes
## Overview
  * The auth methods can be accessed via the Supabase Auth client.


Create auth client
```

1
2
val supabase =createSupabaseClient(supabaseUrl ="https://xyzcompany.supabase.co'", supabaseKey ="public-anon-key") { ... }val auth = supabase.auth

```

## Create a new user
Creates a new user.
  * By default, the user needs to verify their email address before logging in. To turn this off, disable **Confirm email** in [your project](https://supabase.com/dashboard/project/_/auth/providers).
  * **Confirm email** determines if users need to confirm their email address after signing up. 
    * If **Confirm email** is enabled, the return value is the user and you won't be logged in automatically.
    * If **Confirm email** is disabled, the return value is null and you will be logged in instead.
  * When the user confirms their email address, they are redirected to the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls) by default. You can modify your `SITE_URL` or add additional redirect URLs in [your project](https://supabase.com/dashboard/project/_/auth/url-configuration).
  * To learn how to handle OTP links & OAuth refer to [initializing](https://supabase.com/docs/reference/kotlin/initializing)
  * If signUpWith() is called for an existing confirmed user: 
    * When both **Confirm email** and **Confirm phone** (even when phone provider is disabled) are enabled in [your project](https://supabase.com/dashboard/project/_/auth/providers), an obfuscated/fake user object is returned.
    * When either **Confirm email** or **Confirm phone** (even when phone provider is disabled) is disabled, the error message, `User already registered` is returned.


### Parameters
  * providerRequiredEmail or Phone
The provider to use for the user's authentication. In this case `Email` or `Phone`.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configOptionalEmail.Config.() -> Unit or Phone.Config.() -> Unit
The configuration for signing in with `Email` or `Phone`.
Details


Sign up with emailSign up with a phone number and password (whatsapp)Sign up with a phone number and password (sms)Sign up with additional user metadataSign up with a redirect URL
```

1
2
3
4
val user = supabase.auth.signUpWith(Email) {  email ="example@email.com"  password ="example-password"}

```

## Listen to auth events
Listen to session changes.
Listen to auth changes
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
supabase.auth.sessionStatus.collect {when(it) {is SessionStatus.Authenticated -> {println("Received new authenticated session.")when(it.source) { //Check the source of the session        SessionSource.External ->TODO()is SessionSource.Refresh ->TODO()is SessionSource.SignIn ->TODO()is SessionSource.SignUp ->TODO()        SessionSource.Storage ->TODO()        SessionSource.Unknown ->TODO()is SessionSource.UserChanged ->TODO()is SessionSource.UserIdentitiesChanged ->TODO()      }    }    SessionStatus.Initializing ->println("Initializing")is SessionStatus.RefreshFailure ->println("Refresh failure ${it.cause}") //Either a network error or a internal server erroris SessionStatus.NotAuthenticated -> {if(it.isSignOut) {println("User signed out")      } else {println("User not signed in")      }    }  }}

```

Notes
## Create an anonymous user
  * Creates an anonymous user.
  * The user can be retrieved by calling `supabase.auth.currentUserOrNull()`.
  * It is recommended to set up captcha for anonymous sign-ins to prevent abuse. You can pass in the captcha token in the `options` param.


### Parameters
  * captchaTokenOptionalString?
The captcha token when having captcha enabled.
  * dataOptionalJsonObject? or T
Extra user data to pass in.


Create an anonymous userCreate an anonymous user with custom user metadata
```

1
supabase.auth.signInAnonymously(captchaToken ="token")

```

## Sign in a user
Logs in an existing user.
  * Requires either an email and password or a phone number and password.


### Parameters
  * providerRequiredEmail or Phone
The provider to use for the user's authentication, in this case `Email` or `Phone`.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configOptionalEmail.Config.() -> Unit or Phone.Config.() -> Unit
The configuration for signing in with `Email` or `Phone`.
Details


Sign in with email and passwordSign in with phone and password
```

1
2
3
4
supabase.auth.signInWith(Email) {  email ="example@email.com"  password ="example-password"}

```

## Sign in with ID Token
### Parameters
  * providerRequiredIDToken
The provider to use for the user's authentication. For this method it will be `IDToken`.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configOptionalIDToken.Config.() -> Unit
The configuration for signing in with an id token.
Details


Sign In using ID Token
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
supabase.auth.signInWith(IDToken) {  idToken ="token"  provider = Google //Also supported: Apple, Azure and Facebook//optional:  nonce ="nonce"data=buildJsonObject {//...  }}

```

## Sign in a user through OTP
Sends a OTP to the user's email or phone number.
  * Requires either an email or phone number.
  * This method is used for passwordless sign-ins where a OTP is sent to the user's email or phone number.
  * If the user doesn't exist, `signInWith(OTP)` will signup the user instead. To restrict this behavior, you can set `createUser` to `false`.
  * The method `signUpWith(OTP)` does the exact same thing as `signInWith(OTP)`, so it doesn't matter which one you use.
  * If you're using an email, you can configure whether you want the user to receive a magiclink or a OTP.
  * If you're using phone, you can configure whether you want the user to receive a OTP.
  * The magic link's destination URL is determined by the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls).
  * See [redirect URLs and wildcards](https://supabase.com/docs/guides/auth/overview#redirect-urls-and-wildcards) to add additional redirect URLs to your project.
  * To learn how to handle OTP links & OAuth refer to [initializing](https://supabase.com/docs/reference/kotlin/initializing)
  * Magic links and OTPs share the same implementation. To send users a one-time code instead of a magic link, [modify the magic link email template](https://supabase.com/dashboard/project/_/auth/templates) to include `{{ .Token }}` instead of `{{ .ConfirmationURL }}`.


### Parameters
  * providerRequiredOTP
The provider to use for the user's authentication, in this case `OTP`.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configOptionalOTP.Config.() -> Unit
The configuration for signing in with `OTP`.
Details


Sign in with emailSign in with SMS OTP
```

1
2
3
supabase.auth.signInWith(OTP) {  email ="example@email.com"}

```

Notes
## Sign in a user through OAuth
  * This method is used for signing in using a third-party provider.
  * Supabase supports many different [third-party providers](https://supabase.com/docs/guides/auth#providers).
  * To learn how to handle OTP links & OAuth refer to [initializing](https://supabase.com/docs/reference/kotlin/initializing)


### Parameters
  * providerRequiredOAuthProvider
The OAuth provider to use for the user's authentication, for example `Google` or `Github`.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configOptionalExternalAuthConfig.() -> Unit
The configuration for signing in with an OAuth provider.
Details


Sign in using a third-party providerSign in using a third-party provider with scopesCreate a custom urlCreate a custom url with scopes
```

1
supabase.auth.signInWith(Github)

```

## Sign in a user through SSO
  * Before you can call this method you need to [establish a connection](https://supabase.com/docs/guides/auth/sso/auth-sso-saml#managing-saml-20-connections) to an identity provider. Use the [CLI commands](https://supabase.com/docs/reference/cli/supabase-sso) to do this.
  * If you've associated an email domain to the identity provider, you can change the `domain` property in the `signInWith(SSO)` method to start a sign-in flow.
  * In case you need to use a different way to start the authentication flow with an identity provider, you can change the `providerId` property. For example: 
    * Mapping specific user email addresses with an identity provider.
    * Using different hints to identity the identity provider to be used by the user, like a company-specific page, IP address or other tracking information.
  * To learn how to handle OTP links & OAuth refer to [initializing](https://supabase.com/docs/reference/kotlin/initializing)


### Parameters
  * providerRequiredSSO
The OAuth provider to use for the user's authentication, in this case `SSO`.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configOptionalExternalAuthConfig.() -> Unit
The configuration for signing in with an OAuth provider.
Details


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
// You can extract the user's email domain and use it to trigger the// authentication flow with the correct identity provider. supabase.auth.signInWith(SSO) {   domain ="company.com" }//the url was opened automatically, if you don't want that, provide a custom redirect url

```

## Sign out a user
Logs out the current user.
  * In order to use the `signOut()` method, the user needs to be signed in first.


### Parameters
  * scopeOptionalSignOutScope
The scope of the sign-out.


Sign outSign out all sessionsSign out all sessions except the current
```

1
supabase.auth.signOut()

```

## Send a password reset request
Sends a password reset request to the given email address.
  * The password reset flow consist of 2 broad steps: (i) Allow the user to login via the password reset link; (ii) Update the user's password.
  * The `resetPasswordForEmail()` only sends a password reset link to the user's email. To update the user's password, see [`updateUser()`](https://supabase.com/docs/reference/kotlin/auth-updateuser).
  * The user gets redirected back to your app, assuming you setup [OTP handling](https://supabase.com/docs/reference/kotlin/initializing)
  * After the user has been redirected successfully, prompt them for a new password and call `updateUser()`: 
```

1
2
3
supabase.auth.updateUser {  password ="1234567"}

```



### Parameters
  * emailRequiredString
The email to send the password reset email to.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * captchaTokenOptionalString?
The captcha token when having captcha enabled.


Send password reset email
```

1
supabase.auth.resetPasswordForEmail(email ="example@email.com")

```

## Verify and log in through OTP
  * Verifying an OTP is done through either `verifyPhoneOtp` or `verifyEmailOtp`.
  * The verification type used should be determined based on the corresponding auth method called before using `verifyPhoneOtp`/`verifyEmailOtp` to sign up / sign-in a user.


### Parameters
  * typeRequiredOtpType.Email or OtpType.Phone
The OTP type. Depending on the type, an email or phone has to be specified as parameter.
  * email/phoneRequiredString
The email or phone number, depending on which type you specified.
  * tokenRequiredString
The token to verify.
  * captchaTokenOptionalString?
The captcha token when having captcha enabled.


Verify an Email OTPVerify an Phone OTP
```

1
supabase.auth.verifyEmailOtp(type = OtpType.Email.EMAIL, email ="example@email.com", token ="token")

```

Notes
## Retrieve a session
Returns the current session, or `null` if there is none.
Get the session data
```

1
val session = supabase.auth.currentSessionOrNull()

```

## Retrieve a new session
This method will refresh the session whether the current one is expired or not.
  * This is done automatically, but can be disabled in the Auth config.


### Parameters
  * refreshTokenRequiredString
The refresh token to use.


Refresh current sessionRefresh session using the refresh token
```

1
val session = supabase.auth.refreshCurrentSession()

```

## Retrieve a user
  * This method gets the user object from the current session.
  * Fetches the user object from the database instead of local session.
  * Should be used only when you require the most current user data. For faster results, `getCurrentSessionOrNull()?.user` is recommended.


### Parameters
  * jwtRequiredString
The JWT token.


Get the logged in user with the current sessionGet a user based on their access token
```

1
val user = supabase.auth.retrieveUserForCurrentSession(updateSession =true)

```

Notes
## Update a user
Modifies the user data.
  * In order to use the `updateUser()` method, the user needs to be signed in first.
  * By default, email updates sends a confirmation link to both the user's current and new email. To only send a confirmation link to the user's new email, disable **Secure email change** in your project's [email auth provider settings](https://supabase.com/dashboard/project/_/auth/providers).


### Parameters
  * updateCurrentUserOptionalBoolean
Whether to update the local session with the new user. Defaults to `true`.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configRequiredUserUpdateBuilder.() -> Unit
Details


Update the email for an authenticated userUpdate the password for an authenticated userUpdate the user's metadata
```

1
2
3
val user = supabase.auth.updateUser {  email ="newEmail@email.com"}

```

Notes
## Retrieve identities linked to a user
  * The user needs to be signed in to call `currentIdentitiesOrNull()`.


Returns a list of identities linked to the user
```

1
2
3
4
//get the identities from the current userval identities = supabase.auth.currentIdentitiesOrNull()//Or retrieve themval identities = supabase.auth.retrieveUserForCurrentSession().identities

```

## Link an identity to a user
  * The **Enable Manual Linking** option must be enabled from your [project's authentication settings](https://supabase.com/dashboard/project/_/settings/auth).
  * The user needs to be signed in to call `linkIdentity()`.
  * If the candidate identity is already linked to the existing user or another user, `linkIdentity()` will fail.
  * This method works similarly to `signInWith()` using an OAuthProvider. To learn how to handle OTP links & OAuth refer to [initializing](https://supabase.com/docs/reference/kotlin/initializing)


### Parameters
  * providerRequiredOAuthProvider
The OAuth provider you want to link the user with.
  * redirectUrlOptionalString?
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configOptionalExternalAuthConfigDefaults.() -> Unit
Extra configuration.
Details


Link an identity to a user
```

1
2
3
4
supabase.auth.linkIdentity(OAuthProvider)//Example:supabase.auth.linkIdentity(Google)

```

## Unlink an identity from a user
  * The **Enable Manual Linking** option must be enabled from your [project's authentication settings](https://supabase.com/dashboard/project/_/settings/auth).
  * The user needs to be signed in to call `unlinkIdentity()`.
  * The user must have at least 2 identities in order to unlink an identity.
  * The identity to be unlinked must belong to the user.


### Parameters
  * identityIdRequiredString
The id of the OAuth identity
  * updateLocalUserOptionalBoolean
Whether to delete the identity from the local user or not. Defaults to `true`.


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
//get all identities linked to a userval identities = supabase.auth.currentIdentitiesOrNull() ?: emptyList()//find the google identity linked to the userval googleIdentity = identities.first { it.provider =="google" }//unlink the google identity from the usersupabase.auth.unlinkIdentity(googleIdentity.identityId!!)

```

## Send a password reauthentication nonce
  * This method is used together with `updateUser()` when a user's password needs to be updated.
  * This method will send a nonce to the user's email. If the user doesn't have a confirmed email address, the method will send the nonce to the user's confirmed phone number instead.


Send reauthentication nonce
```

1
supabase.auth.reauthenticate()

```

Notes
## Resend an OTP
  * Resends a signup confirmation, email change or phone change email to the user.
  * Passwordless sign-ins can be resent by calling the `signInWith(OTP)` method again.
  * Password recovery emails can be resent by calling the `resetPasswordForEmail()` method again.
  * This method will only resend an email or phone OTP to the user if there was an initial signup, email change or phone change request being made.


### Parameters
  * typeRequiredOtpType.Email or OtpType.Phone
The OTP type. Depending on the type, an email or phone has to be specified as parameter.
  * email/phoneRequiredString
The email or phone number, depending on which type you specified.
  * captchaTokenOptionalString?
The captcha token when having captcha enabled.


Resend an email signup confirmationResend a phone signup confirmationResend email change emailResend phone change OTP
```

1
supabase.auth.resendEmail(OtpType.Email.SIGNUP, "example@email.com")

```

Notes
## Set the session data
Changes the local session.
  * `importSession()` takes in a UserSession.
  * [Refresh token rotation](https://supabase.com/docs/reference/auth/config#refresh_token_rotation_enabled) is enabled by default on all projects to guard against replay attacks.
  * You can configure the [`REFRESH_TOKEN_REUSE_INTERVAL`](https://supabase.com/docs/reference/auth/config#refresh_token_reuse_interval) which provides a short window in which the same refresh token can be used multiple times in the event of concurrency or offline issues.


### Parameters
  * sessionRequiredUserSession
The session to set.


Set local session
```

1
supabase.auth.importSession(UserSession(accessToken ="token", refreshToken ="refresh", expiresIn =2000, tokenType ="Bearer", user =null))

```

Notes
## Exchange an auth code for a session
  * Used when `flowType` is set to `FlowType.PKCE` in the Auth configuration.


### Parameters
  * codeRequiredString
The code to exchange.
  * saveSessionOptionalBoolean
Whether to save the session. Defaults to true.


Exchange Auth Code
```

1
supabase.auth.exchangeCodeForSession("34e770dd-9ff9-416c-87fa-43b31d7ef225")

```

## Auth MFA
This section contains methods commonly used for Multi-Factor Authentication (MFA) and are invoked behind the `supabase.auth.mfa` namespace.
Currently, we only support time-based one-time password (TOTP) as the 2nd factor. We don't support recovery codes but we allow users to enroll more than 1 TOTP factor, with an upper limit of 10.
Having a 2nd TOTP factor for recovery frees the user of the burden of having to store their recovery codes somewhere. It also reduces the attack surface since multiple recovery codes are usually generated compared to just having 1 backup TOTP factor.
## Enroll a factor
Enrolls a new factor.
  * Use `FactorType.TOTP` or `FactorType.Phone` as the factorType and use the returned id to create a challenge.
  * To create a challenge, see [`mfa.createChallenge()`](https://supabase.com/docs/reference/kotlin/auth-mfa-challenge).
  * To verify a challenge, see [`mfa.verifyChallenge()`](https://supabase.com/docs/reference/kotlin/auth-mfa-verify).
  * To create and verify a challenge in a single step, see [`mfa.createChallengeAndVerify()`](https://supabase.com/docs/reference/kotlin/auth-mfa-challengeandverify).


### Parameters
  * factorTypeRequiredFactorType<C, R>
The type of MFA factor to enroll. Currently supports `FactorType.TOTP` and `FactorType.Phone`.
  * issuerOptionalString?
Domain which the user is enrolling with.
  * configOptionalConfig.() -> Unit
Factor type specific configuration.


Enroll a time-based, one-time password (TOTP) factorEnroll a Phone FactorCheck the local user for verified factorsRetrieve verified factors
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
val factor = supabase.auth.mfa.enroll(factorType = FactorType.TOTP, friendlyName ="Your friendly Name") {// Optional   issuer ="example.com"}// Use the id to create a challenge.// The challenge can be verified by entering the code generated from the authenticator app.// The code will be generated upon scanning the qr_code or entering the secret into the authenticator app.val (id, type, qrCode) = factor.data//qrCode is a svg as a stringval (factorId, factorType, _) = factorval challenge = supabase.auth.mfa.createChallenge(factor.id)

```

## Create a challenge
Creates a challenge for a factor.
  * An [enrolled factor](https://supabase.com/docs/reference/kotlin/auth-mfa-enroll) is required before creating a challenge.
  * To verify a challenge, see [`mfa.verifyChallenge()`](https://supabase.com/docs/reference/kotlin/auth-mfa-verify).
  * A phone factor sends a code to the user upon challenge. The channel defaults to `Phone.Channel.SMS` unless otherwise specified.


### Parameters
  * factorIdRequiredString
The id of the MFA factor you want to create a challenge for.
  * channelOptionalPhone.Channel?
The channel to send the challenge to. Defaults to `Phone.Channel.SMS`.


Create a challenge for a factor
```

1
val challenge = supabase.auth.mfa.createChallenge(factorId ="34e770dd-9ff9-416c-87fa-43b31d7ef225")

```

## Verify a challenge
Verifies a challenge for a factor.
  * To verify a challenge, please [create a challenge](https://supabase.com/docs/reference/kotlin/auth-mfa-challenge) first.


### Parameters
  * factorIdRequiredString
The id of the MFA factor to verify.
  * challengeIdRequiredString
The id of the challenge to verify.
  * codeRequiredString
The code used to verify.
  * saveSessionOptionalBoolean
Whether to save the session. Defaults to true.


Verify a challenge for a factor
```

1
2
3
4
5
6
supabase.auth.mfa.verifyChallenge(  factorId ="34e770dd-9ff9-416c-87fa-43b31d7ef225",  challengeId ="4034ae6f-a8ce-4fb5-8ee5-69a5863a7c15",  code ="123456",  saveSession =true// this is set to true by default, but you can set it to false if you want to handle the session yourself)

```

## Create and verify a challenge
Creates and verifies a challenge for a factor.
  * Creating and verifying a challenge in a single step is not supported by the `Phone` factor type.
  * An [enrolled factor](https://supabase.com/docs/reference/kotlin/auth-mfa-enroll) is required before invoking `createChallengeAndVerify()`.
  * Executes [`mfa.createChallenge()`](https://supabase.com/docs/reference/kotlin/auth-mfa-challenge) and [`mfa.verifyChallenge()`](https://supabase.com/docs/reference/kotlin/auth-mfa-verify) in a single step.


### Parameters
  * factorIdRequiredString
The id of the MFA factor to verify.
  * codeRequiredString
The code used to verify.
  * saveSessionOptionalBoolean
Whether to save the session. Defaults to true.


Create and verify a challenge for a factor
```

1
2
3
4
5
supabase.auth.mfa.createChallengeAndVerify(  factorId ="34e770dd-9ff9-416c-87fa-43b31d7ef225",  code ="123456",  saveSession =true// this is set to true by default, but you can set it to false if you want to handle the session yourself)

```

## Unenroll a factor
Unenroll removes a MFA factor. A user has to have an `AAL2` authentication level in order to unenroll a verified factor.
### Parameters
  * factorIdRequiredString
The id of the factor you want to unenroll.


Unenroll a factor
```

1
supabase.auth.mfa.unenroll(factorId ="34e770dd-9ff9-416c-87fa-43b31d7ef225")

```

## Get Authenticator Assurance Level
  * Authenticator Assurance Level (AAL) is the measure of the strength of an authentication mechanism.
  * In Supabase, having an AAL of `aal1` refers to having the 1st factor of authentication such as an email and password or OAuth sign-in while `aal2` refers to the 2nd factor of authentication such as a time-based, one-time-password (TOTP).
  * If the user has a verified factor, the `next` field will return `AuthenticatorAssuranceLevel.AAL2`, else, it will return `AuthenticatorAssuranceLevel.AAL1`.


Get the AAL details of the current sessionCheck whether the user has at least one verified factorCheck whether the user is logged in using AAL2
```

1
val (current, next) = supabase.auth.mfa.getAuthenticatorAssuranceLevel()

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
10
11
12
13
val supabase =createSupabaseClient(  supabaseUrl ="https://id.supabase.co",  supabaseKey ="supabaseKey") {install(Auth) {minimalSettings() //disables session saving and auto-refreshing  }// install other plugins (these will use the service role key)}supabase.auth.importAuthToken("service_role")// Access auth admin apival adminAuthClient = supabase.auth.admin

```

## Retrieve a user
Fetches the user object from the database based on the user's id.
  * The `retrieveUserById()` method requires the user's id which maps to the `auth.users.id` column.


### Parameters
  * uidRequiredString
The id of the user you want to retrieve.


Fetch the user object using the access_token jwt
```

1
val user = supabase.auth.admin.retrieveUserById(uid ="f2a0b0a0-6b1a-4b7a-8f1a-4b7a6b1a8f1a")

```

## List all users
Retrieves a list of users.
  * Defaults to return 50 users per page.


### Parameters
  * pageOptionalInt
The page number to retrieve.
  * perPageOptionalInt
The number of users to retrieve per page.


Get a page of usersPaginated list of users
```

1
val users = supabase.auth.admin.retrieveUsers()

```

## Create a user
Creates a new user.
  * To confirm the user's email address or phone number, set `autoConfirm` to true. Both arguments default to false.


### Parameters
  * builderRequiredAdminUserBuilder.Email.() -> Unit or AdminUserBuilder.Phone.() -> Unit
The builder to create a new user.
Details


Create user with emailCreate user with phoneAuto-confirm the user's emailAuto-confirm the user's phone number
```

1
2
3
4
5
6
7
val userWithEmail = supabase.auth.admin.createUserWithEmail {  email ="example@email.com"  password ="secretpassword"userMetadata {put("name", "John")  }}

```

## Delete a user
Deletes a user from the database.
  * The `deleteUser()` method requires the user's ID, which maps to the `auth.users.id` column.


### Parameters
  * uidRequiredString
The id of the user you want to delete.


Removes a user
```

1
supabase.auth.admin.deleteUser(uid ="uid")

```

## Send an email invite link
Sends an invite link to the user's email address.
### Parameters
  * emailRequiredString
The email to send the invite to.
  * redirectToOptionalString
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * dataOptionalJsonObject
Custom data to create the user with.


Invite a user
```

1
2
3
4
5
6
7
8
supabase.auth.admin.inviteUserByEmail(  email ="example@email.com",//optional:  redirectTo ="https://example.com/redirect",data=buildJsonObject {put("custom", "value")  })

```

## Generate an email link
Generates email links and OTPs to be sent via a custom email provider.
### Parameters
  * typeRequiredLinkType<C>
The type of link to generate, e.g. `LinkType.Signup`.
  * redirectToOptionalString
The redirect url to use. If you don't specify this, the platform specific will be used, like deeplinks on android.
  * configOptionalC.() -> Unit
The builder to create a new link.


Generate a signup linkGenerate an invite linkGenerate a magic linkGenerate a recovery linkGenerate links to change current email address
```

1
2
3
4
val (url, user) = supabase.auth.admin.generateLinkFor(LinkType.Signup) {  email ="example@email.com"  password ="secretpassword"}

```

## Update a user
Updates the user data.
### Parameters
  * uidRequiredString
The id of the user you want to update.
  * builderRequiredAdminUserUpdateBuilder.() -> Unit
The builder to update the user.
Details


Updates a user's emailUpdates a user's passwordUpdates a user's metadataUpdates a user's app_metadataConfirms a user's email addressConfirms a user's phone number
```

1
2
3
supabase.auth.admin.updateUserById(uid ="id") {  email ="example@email.com"}

```

## List all factors for a user
Lists all factors associated to a user.
### Parameters
  * uidRequiredString
The id of the user you want to list factors for.


List all factors for a user
```

1
const factors = supabase.auth.admin.retrieveFactors(uid ="id")

```

## Delete a factor for a user
Deletes a factor on a user. This will log the user out of all active sessions if the deleted factor was verified.
### Parameters
  * uidRequiredString
The id of the user you want to delete a factor for.
  * factorIdRequiredString
The id of the factor you want to delete.


Delete a factor for a user
```

1
supabase.auth.admin.deleteFactor(uid ="id", factorId ="factor_id")

```

## Invokes a Supabase Edge Function.
Invokes a Supabase Function. See the [guide](https://supabase.com/docs/guides/functions) for details on writing Functions.
  * When invoking a function with parameters, you have to provide a [serializable value](https://supabase.com/docs/reference/kotlin/installing#serialization) in the function parameter.
  * Requires an Authorization header.


### Parameters
  * functionRequiredString
The name of the function to invoke.
  * bodyOptionalT
The body to send with the request. T can be any serializable type.
  * regionOptionalFunctionRegion
The region where the function is invoked. Defaults to `Functions.Config#defaultRegion`.
  * headersOptionalHeaders
The headers to send with the request.


Basic invocationBasic invocation with bodyReuse function by saving it to a variable
```

1
2
3
4
val response = supabase.functions.invoke("function_name")// Decode the response body to a serializable classvaldata= response.body<FunctionResponse>()

```

## Listen to database changes
Return real-time data from your table as a [Flow](https://kotlinlang.org/docs/flow.html).
  * Realtime is disabled by default for new tables. You can turn it on by [managing replication](https://supabase.com/docs/guides/realtime/postgres-changes#replication-setup).
  * `selectAsFlow` and `selectSingleValueAsFlow` will emit the initial data and then listen for changes.
  * Takes in a `filter` parameter to filter the data and a `primaryKey` parameter to cache the data by the primary key.
  * This method requires both the `Realtime` and `Postgrest` plugins to be installed.
  * The type parameter `T` must be a [serializable class](https://supabase.com/docs/reference/kotlin/installing#serialization).
  * If you want more control over the realtime updates, you can use the `Realtime` plugin directly.


### Parameters
  * primaryKeyRequiredKProperty1<Data, Value> or PrimaryKey<Data>
The primary key to cache the data by. Can be a property reference or a custom primary key.
  * channelNameOptionalString
The name of the channel to use for the realtime updates. If null, a channel name following the format "schema:table:id" will be used
  * filterOptionalPostgrestFilterBuilder.() -> Unit or FilterOperation
The filter to apply to the data.


Listen for changes in multiple rowsListen for changes in multiple rows with a filterListen for changes in a single row
```

1
2
3
4
5
6
val flow: Flow<List<Country>> = supabase.from("countries").selectAsFlow(Country::id)flow.collect {for (country in it) {println(country.name)  }}

```

## Subscribe to channel
Subscribe to realtime changes in your database.
  * Realtime is disabled by default for new Projects for better database performance and security. You can turn it on by [managing replication](https://supabase.com/docs/guides/database/api#managing-realtime).
  * If you want to receive the "previous" data for updates and deletes, you will need to set `REPLICA IDENTITY` to `FULL`, like this: `ALTER TABLE your_table REPLICA IDENTITY FULL;`
  * When using a method with a generic type like `track`, `broadcast` or `broadcastFlow`, you have to provide a [serializable class](https://supabase.com/docs/reference/kotlin/installing#serialization) as the type parameter.
  * Presence, Broadcast and Database updates are sent through a [Flow](https://kotlinlang.org/docs/flow.html)


Listen to broadcastsListen to presence updatesListen to all database changesListen to a specific tableListen to insertsListen to updatesListen to deletesListen to row level changes
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
@SerializabledataclassMessage(val content: String, val sender: String)val channel = supabase.channel("channelId") {// optional config}val broadcastFlow = channel.broadcastFlow<Message>(event ="message")// Collect the flowbroadcastFlow.onEach { // it: Messageprintln(it)}.launchIn(coroutineScope) // launch a new coroutine to collect the flowchannel.subscribe(blockUntilSubscribed =true)

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
5
val channel = supabase.channel("channelId") {//optional config}//...supabase.realtime.removeChannel(channel)

```

## Unsubscribe from all channels
Unsubscribes and removes all Realtime channels from Realtime client.
  * Removing channels is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.
  * If you removed all channels, the client automatically disconnects from the Realtime websocket. This can be disabled in the Realtime config by setting `disconnectOnNoSubscriptions` to false.


Remove all channels
```

1
supabase.realtime.removeAllChannels()

```

## Retrieve all channels
Returns all Realtime channels.
Get all channels
```

1
val channels = supabase.realtime.subscriptions.entries

```

## Broadcast a message
Broadcast a message to all connected clients to a channel.
  * When using REST you don't need to subscribe to the channel


Send a message via websocketSend a message via REST
```

1
2
3
4
5
6
val channel = supabase.channel("room1")channel.subscribe(blockUntilSubscribed =true)channel.broadcast("cursor-pos", message =buildJsonObject {put("x", 10)put("y", 20)})

```

Response
## Create a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `insert`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * idRequiredString
The id of the bucket you want to create.
  * builderOptionalBucketBuilder.() -> Unit
The builder to create a new bucket.
Details


Create bucket
```

1
2
3
4
supabase.storage.createBucket(id ="icons") {public=true  fileSizeLimit =5.megabytes}

```

## Retrieve a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `select`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


Get bucket
```

1
val bucket = supabase.storage.retrieveBucketById(bucketId ="avatars")

```

## List all buckets
  * RLS policy permissions required: 
    * `buckets` table permissions: `select`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


List buckets
```

1
val buckets = supabase.storage.retrieveBuckets()

```

## Update a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `select` and `update`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * idRequiredString
The id of the bucket you want to create.
  * builderOptionalBucketBuilder.() -> Unit
The builder to create a new bucket.
Details


Update bucket
```

1
2
3
4
5
supabase.storage.updateBucket("cards") {public=false  fileSizeLimit =20.megabytesallowedMimeTypes(ContentType.Image.PNG, ContentType.Image.JPEG)}

```

## Delete a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `select` and `delete`
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * bucketIdRequiredString
The id of the bucket you want to delete.


Delete bucket
```

1
supabase.storage.deleteBucket(bucketId ="icons")

```

## Empty a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: `select`
    * `objects` table permissions: `select` and `delete`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * bucketIdRequiredString
The id of the bucket you want to empty.


Empty bucket
```

1
supabase.storage.emptyBucket(bucketId ="icons")

```

## Upload a file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `insert`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works
  * Resumable uploads use a `Disk` cache by default to store the upload urls. You can customize that in the Auth config by changing the `resumable.cache` property.


### Parameters
  * pathRequiredString
The path of the file you want to upload.
  * dataRequiredByteArray
The data of the file you want to upload.
  * optionsOptionalUploadOptionBuilder.() -> Unit
Additional options for the upload.
Details


Upload fileUpload file with progressCreate resumable uploadStart and resumable uploadPause resumable uploadCancel resumable uploadListen to the resumable upload stateContinue previous uploads
```

1
2
3
4
5
6
7
8
val bucket = supabase.storage.from("avatars")bucket.upload("myIcon.png", byteArray) {  upsert =false}//on JVM you can use java.io.Filebucket.upload("myIcon.png", file) {  upsert =false}

```

## Download a file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The path of the file you want to download.
  * optionsOptionalDownloadOptionBuilder.() -> Unit
Additional options for the download.
Details


Download file from non-public bucketDownload file from public bucketDownload file with transformationDownload file with progress
```

1
2
3
4
val bucket = supabase.storage.from("avatars")val bytes = bucket.downloadAuthenticated("test.png")//or on JVM:bucket.downloadAuthenticatedTo("test.png", File("test.png"))

```

## List all files in a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


List files in a bucket
```

1
2
val bucket = supabase.storage.from("avatars")val files = bucket.list()

```

## Replace an existing file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `update` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The path of the file you want to upload.
  * dataRequiredByteArray
The data of the file you want to upload.
  * optionsOptionalUploadOptionBuilder.() -> Unit
Additional options for the upload.
Details


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
val bucket = supabase.storage.from("avatars")bucket.update("myIcon.png", byteArray) {  upsert =false}//on JVM you can use java.io.Filebucket.update("myIcon.png", file) {  upsert =false}

```

## Move an existing file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `update` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * fromRequiredString
The path of the file you want to move.
  * toRequiredString
The new path of the file.
  * destinationBucketOptionalString
The destination bucket of the file.


Move file
```

1
2
val bucket = supabase.storage.from("avatars")bucket.move("icon1.png", "icon2.png")

```

## Copy an existing file
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `insert` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * fromRequiredString
The path of the file you want to copy.
  * toRequiredString
The new path of the file.
  * destinationBucketOptionalString
The destination bucket of the file.


Copy file
```

1
supabase.storage.from("test").copy(from ="avatar.png", to ="avatar2.png")

```

## Delete files in a bucket
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `delete` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathsRequiredvararg String
The paths of the files you want to remove.


Delete file
```

1
2
val bucket = supabase.storage.from("avatars")bucket.delete("test.png", "test2.png")

```

## Create a signed URL
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The path of the file you want to create a signed url for.
  * expiresInRequiredDuration
The duration the signed url should be valid for.
  * builderOptionalImageTransformation.() -> Unit
The transformation to apply to the image.
Details


Create Signed URLCreate Signed URL with transformation
```

1
2
val bucket = supabase.storage.from("avatars")val url = bucket.createSignedUrl(path ="icon.png", expiresIn =3.minutes)

```

## Create signed URLs
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * expiresInRequiredDuration
The duration the signed url should be valid for.
  * pathsRequiredvararg String
The paths of the files you want to create signed urls for.


Create Signed URLs
```

1
val urls = supabase.storage.from("avatars").createSignedUrls(20.minutes, "avata1.jpg", "avatar2.jpg")

```

## Create signed upload URL
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: `insert`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The path of the file you want to upload.
  * upsertOptionalBoolean
Whether to overwrite the file if it already exists.


Create Signed Upload URL
```

1
val url = supabase.storage.from("avatars").createSignedUploadUrl("avatar.png")

```

## Upload to a signed URL
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The path of the file you want to upload.
  * tokenRequiredString
The token you received from `createSignedUploadUrl`.
  * dataOptionalByteArray
The data of the file you want to upload.
  * optionsOptionalUploadOptionBuilder.() -> Unit
Additional options for the upload.
Details


Upload to a signed URL
```

1
2
3
supabase.storage.from("avatars").uploadToSignedUrl(path ="avatar.jpg", token ="token-from-createSignedUploadUrl", data= bytes)//or on JVM:supabase.storage.from("avatars").uploadToSignedUrl(path ="avatar.jpg", token ="token-from-createSignedUploadUrl", file =File("avatar.jpg"))

```

## Retrieve public URL
  * The bucket needs to be set to public, either via [updateBucket()](https://supabase.com/docs/reference/kotlin/storage-updatebucket) or by going to Storage on [supabase.com/dashboard](https://supabase.com/dashboard), clicking the overflow menu on a bucket and choosing "Make public"
  * RLS policy permissions required: 
    * `buckets` table permissions: none
    * `objects` table permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The path of the file you want to get the public url for.


Returns the URL for an asset in a public bucketReturns the URL for an asset in a public bucket with transformations
```

1
val url = supabase.storage.from("public-bucket").publicUrl("folder/avatar1.png")

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



