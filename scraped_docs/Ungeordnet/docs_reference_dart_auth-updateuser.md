---
url: https://supabase.com/docs/reference/dart/auth-updateuser
scraped_at: 2025-05-25T09:36:20.934131
title: Flutter API Reference | Supabase Docs
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
Flutter
v2.0
  * [Introduction](https://supabase.com/docs/reference/dart/introduction)
  * [Installing](https://supabase.com/docs/reference/dart/installing)
  * [Initializing](https://supabase.com/docs/reference/dart/initializing)
  * [Upgrade guide](https://supabase.com/docs/reference/dart/upgrade-guide)
  * Database
    * [Fetch data](https://supabase.com/docs/reference/dart/select)
    * [Insert data](https://supabase.com/docs/reference/dart/insert)
    * [Update data](https://supabase.com/docs/reference/dart/update)
    * [Upsert data](https://supabase.com/docs/reference/dart/upsert)
    * [Delete data](https://supabase.com/docs/reference/dart/delete)
    * [Call a Postgres function](https://supabase.com/docs/reference/dart/rpc)
    * Using filters
    * Using modifiers
  * Auth
    * [Create a new user](https://supabase.com/docs/reference/dart/auth-signup)
    * [Listen to auth events](https://supabase.com/docs/reference/dart/auth-onauthstatechange)
    * [Create an anonymous user](https://supabase.com/docs/reference/dart/auth-signinanonymously)
    * [Sign in a user](https://supabase.com/docs/reference/dart/auth-signinwithpassword)
    * [Sign in with ID Token](https://supabase.com/docs/reference/dart/auth-signinwithidtoken)
    * [Sign in a user through OTP](https://supabase.com/docs/reference/dart/auth-signinwithotp)
    * [Sign in a user through OAuth](https://supabase.com/docs/reference/dart/auth-signinwithoauth)
    * [Sign in a user through SSO](https://supabase.com/docs/reference/dart/auth-signinwithsso)
    * [Sign out a user](https://supabase.com/docs/reference/dart/auth-signout)
    * [Verify and log in through OTP](https://supabase.com/docs/reference/dart/auth-verifyotp)
    * [Retrieve a session](https://supabase.com/docs/reference/dart/auth-getsession)
    * [Retrieve a new session](https://supabase.com/docs/reference/dart/auth-refreshsession)
    * [Retrieve a user](https://supabase.com/docs/reference/dart/auth-getuser)
    * [Update a user](https://supabase.com/docs/reference/dart/auth-updateuser)
    * [Retrieve identities linked to a user](https://supabase.com/docs/reference/dart/auth-getuseridentities)
    * [Link an identity to a user](https://supabase.com/docs/reference/dart/auth-linkidentity)
    * [Unlink an identity from a user](https://supabase.com/docs/reference/dart/auth-unlinkidentity)
    * [Send a password reauthentication nonce](https://supabase.com/docs/reference/dart/auth-reauthentication)
    * [Resend an OTP](https://supabase.com/docs/reference/dart/auth-resend)
    * [Set the session data](https://supabase.com/docs/reference/dart/auth-setsession)
    * Auth MFA
    * Auth Admin
  * Edge Functions
    * [Invokes a Supabase Edge Function.](https://supabase.com/docs/reference/dart/functions-invoke)
  * Realtime
    * [Listen to database changes](https://supabase.com/docs/reference/dart/stream)
    * [Subscribe to channel](https://supabase.com/docs/reference/dart/subscribe)
    * [Unsubscribe from a channel](https://supabase.com/docs/reference/dart/removechannel)
    * [Unsubscribe from all channels](https://supabase.com/docs/reference/dart/removeallchannels)
    * [Retrieve all channels](https://supabase.com/docs/reference/dart/getchannels)
  * Storage
    * [Create a bucket](https://supabase.com/docs/reference/dart/storage-createbucket)
    * [Retrieve a bucket](https://supabase.com/docs/reference/dart/storage-getbucket)
    * [List all buckets](https://supabase.com/docs/reference/dart/storage-listbuckets)
    * [Update a bucket](https://supabase.com/docs/reference/dart/storage-updatebucket)
    * [Delete a bucket](https://supabase.com/docs/reference/dart/storage-deletebucket)
    * [Empty a bucket](https://supabase.com/docs/reference/dart/storage-emptybucket)
    * [Upload a file](https://supabase.com/docs/reference/dart/storage-from-upload)
    * [Download a file](https://supabase.com/docs/reference/dart/storage-from-download)
    * [List all files in a bucket](https://supabase.com/docs/reference/dart/storage-from-list)
    * [Replace an existing file](https://supabase.com/docs/reference/dart/storage-from-update)
    * [Move an existing file](https://supabase.com/docs/reference/dart/storage-from-move)
    * [Delete files in a bucket](https://supabase.com/docs/reference/dart/storage-from-remove)
    * [Create a signed URL](https://supabase.com/docs/reference/dart/storage-from-createsignedurl)
    * [Retrieve public URL](https://supabase.com/docs/reference/dart/storage-from-getpublicurl)


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
Dart Reference v2.0
# Flutter Client Library
supabase_flutter[View on GitHub](https://github.com/supabase/supabase-flutter)
This reference documents every object and method available in Supabase's Flutter library, [supabase-flutter](https://pub.dev/packages/supabase_flutter). You can use supabase-flutter to interact with your Postgres database, listen to database changes, invoke Deno Edge Functions, build login and user management functionality, and manage large files.
We also provide a [supabase](https://pub.dev/packages/supabase) package for non-Flutter projects.
## Installing
### Install from pub.dev[#](https://supabase.com/docs/reference/dart/auth-updateuser#install-from-pubdev)
You can install Supabase package from [pub.dev](https://pub.dev/packages/supabase_flutter)
FlutterOther Dart Project
```

1
flutterpubaddsupabase_flutter

```

## Initializing
You can initialize Supabase with the static `initialize()` method of the `Supabase` class.
The Supabase client is your entrypoint to the rest of the Supabase functionality and is the easiest way to interact with everything we offer within the Supabase ecosystem.
### Parameters
  * urlRequiredstring
The unique Supabase URL which is supplied when you create a new project in your project dashboard.
  * anonKeyRequiredstring
The unique Supabase Key which is supplied when you create a new project in your project dashboard.
  * headersOptionalMap<String, String>
Custom header to be passed to the Supabase client.
  * httpClientOptionalClient
Custom http client to be used by the Supabase client.
  * authOptionsOptionalFlutterAuthClientOptions
Options to change the Auth behaviors.
Details
  * postgrestOptionsOptionalPostgrestClientOptions
Options to change the Postgrest behaviors.
Details
  * realtimeClientOptionsOptionalRealtimeClientOptions
Options to change the Realtime behaviors.
Details
  * storageOptionsOptionalStorageClientOptions
Options to change the Storage behaviors.
Details


For FlutterFor other Dart projects
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
Future<void> main() async {awaitSupabase.initialize(  url:'https://xyzcompany.supabase.co',  anonKey:'public-anon-key', );runApp(MyApp());}// Get a reference your Supabase clientfinal supabase =Supabase.instance.client;

```

## Upgrade guide
Although `supabase_flutter` v2 brings a few breaking changes, for the most part the public API should be the same with a few minor exceptions. We have brought numerous updates behind the scenes to make the SDK work more intuitively for Flutter and Dart developers.
## Upgrade the client library[#](https://supabase.com/docs/reference/dart/auth-updateuser#upgrade-the-client-library)
Make sure you are using v2 of the client library in your `pubspec.yaml` file.
```

1
supabase_flutter:^2.0.0

```

_Optionally_ passing custom configuration to `Supabase.initialize()` is now organized into separate objects:
BeforeAfter
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
awaitSupabase.initialize( url: supabaseUrl, anonKey: supabaseKey, authFlowType:AuthFlowType.pkce, storageRetryAttempts:10, realtimeClientOptions:constRealtimeClientOptions(  logLevel:RealtimeLogLevel.info, ),);

```

### Auth updates[#](https://supabase.com/docs/reference/dart/auth-updateuser#auth-updates)
#### Renaming Provider to OAuthProvider[#](https://supabase.com/docs/reference/dart/auth-updateuser#renaming-provider-to-oauthprovider)
`Provider` enum is renamed to `OAuthProvider`. Previously the `Provider` symbol often collided with classes in the [provider](https://pub.dev/packages/provider) package and developers needed to add import prefixes to avoid collisions. With the new update, developers can use Supabase and Provider in the same codebase without any import prefixes.
BeforeAfter
```

1
2
3
await supabase.auth.signInWithOAuth(Provider.google,);

```

#### Sign in with Apple method deprecated[#](https://supabase.com/docs/reference/dart/auth-updateuser#sign-in-with-apple-method-deprecated)
We have removed the [sign_in_with_apple](https://pub.dev/packages/sign_in_with_apple) dependency in v2. This is because not every developer needs to sign in with Apple, and we want to reduce the number of dependencies in the library.
With v2, you can import [sign_in_with_apple](https://pub.dev/packages/sign_in_with_apple) as a separate dependency if you need to sign in with Apple. We have also added `auth.generateRawNonce()` method to easily generate a secure nonce.
BeforeAfter
```

1
await supabase.auth.signInWithApple();

```

#### Initialization does not await for session refresh[#](https://supabase.com/docs/reference/dart/auth-updateuser#initialization-does-not-await-for-session-refresh)
In v1, `Supabase.initialize()` would await for the session to be refreshed before returning. This caused delays in the app's launch time, especially when the app is opened in a poor network environment.
In v2, `Supabase.initialize()` returns immediately after obtaining the session from the local storage, which makes the app launch faster. Because of this, there is no guarantee that the session is valid when the app starts.
If you need to make sure the session is valid, you can access the `isExpired` getter to check if the session is valid. If the session is expired, you can listen to the `onAuthStateChange` event and wait for a new `tokenRefreshed` event to be fired.
BeforeAfter
```

1
2
// Session is valid, no check requiredfinal session = supabase.auth.currentSession;

```

#### Removing Flutter Webview dependency for OAuth sign in[#](https://supabase.com/docs/reference/dart/auth-updateuser#removing-flutter-webview-dependency-for-oauth-sign-in)
In v1, on iOS you could pass a `BuildContext` to the `signInWithOAuth()` method to launch the OAuth flow in a Flutter Webview.
In v2, we have dropped the [webview_flutter](https://pub.dev/packages/webview_flutter) dependency in v2 to allow you to have full control over the UI of the OAuth flow. We now have [native support for Google and Apple sign in](https://supabase.com/docs/reference/dart/auth-signinwithidtoken), so opening an external browser is no longer needed on iOS.
Because of this update, we no longer need the `context` parameter, so we have removed the `context` parameter from the `signInWithOAuth()` method.
BeforeAfter
```

1
2
3
4
5
6
// Opens a webview on iOS.await supabase.auth.signInWithOAuth(Provider.github, authScreenLaunchMode:LaunchMode.inAppWebView, context: context,);

```

#### PKCE is the default auth flow type[#](https://supabase.com/docs/reference/dart/auth-updateuser#pkce-is-the-default-auth-flow-type)
[PKCE flow](https://supabase.com/blog/supabase-auth-sso-pkce#introducing-pkce), which is a more secure method for obtaining sessions from deep links, is now the default auth flow for any authentication involving deep links.
BeforeAfter
```

1
2
3
4
5
awaitSupabase.initialize( url:'SUPABASE_URL', anonKey:'SUPABASE_ANON_KEY', authFlowType:AuthFlowType.implicit,// set to implicit by default);

```

#### Auth callback host name parameter removed[#](https://supabase.com/docs/reference/dart/auth-updateuser#auth-callback-host-name-parameter-removed)
`Supabase.initialize()` no longer has the `authCallbackUrlHostname` parameter. The `supabase_flutter` SDK will automatically detect auth callback URLs and handle them internally.
BeforeAfter
```

1
2
3
4
5
awaitSupabase.initialize( url:'SUPABASE_URL', anonKey:'SUPABASE_ANON_KEY', authCallbackUrlHostname:'auth-callback',);

```

#### SupabaseAuth class removed[#](https://supabase.com/docs/reference/dart/auth-updateuser#supabaseauth-class-removed)
The `SupabaseAuth` had an `initialSession` member, which was used to obtain the initial session upon app start. This is now removed, and `currentSession` should be used to access the session at any time.
BeforeAfter
```

1
2
// Use `initialSession` to obtain the initial session when the app starts.final initialSession =awaitSupabaseAuth.initialSession;

```

### Data methods[#](https://supabase.com/docs/reference/dart/auth-updateuser#data-methods)
#### Insert and return data[#](https://supabase.com/docs/reference/dart/auth-updateuser#insert-and-return-data)
We made the query builder immutable, which means you can reuse the same query object to chain multiple filters and get the expected outcome.
BeforeAfter
```

1
2
3
4
5
6
7
// If you declare a query and chain filters on itfinal myQuery = supabase.from('my_table').select();final foo =await myQuery.eq('some_col','foo');// The `eq` filter above is applied in addition to the following filterfinal bar =await myQuery.eq('another_col','bar');

```

#### Renaming is and in filter[#](https://supabase.com/docs/reference/dart/auth-updateuser#renaming-is-and-in-filter)
Because `is` and `in` are [reserved keywords](https://dart.dev/languages/keywords) in Dart, v1 used `is_` and `in_` as query filter names. Users found the underscore confusing, so the query filters are now renamed to `isFilter` and `inFilter`.
BeforeAfter
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
final data =await supabase.from('users').select().is_('status',null);final data =await supabase.from('users').select().in_('status', ['ONLINE','OFFLINE']);

```

#### Deprecate FetchOption in favor of `count()` and `head()` methods[#](https://supabase.com/docs/reference/dart/auth-updateuser#deprecate-fetchoption-in-favor-of-count-and-head-methods)
`FetchOption()` on `.select()` is now deprecated, and new `.count()` and `head()` methods are added to the query builder.
`count()` on `.select()` performs the select while also getting the count value, and `.count()` directly on `.from()` performs a head request resulting in only fetching the count value.
BeforeAfter
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
// Request with count optionfinal res =await supabase.from('cities').select('name',constFetchOptions(    count:CountOption.exact,   ),  );final data = res.data;final count = res.count;// Request with count and head option// obtains the count value without fetching the data.final res =await supabase.from('cities').select('name',constFetchOptions(    count:CountOption.exact,    head:true,   ),  );final count = res.count;

```

#### PostgREST error codes[#](https://supabase.com/docs/reference/dart/auth-updateuser#postgrest-error-codes)
The `PostgrestException` instance thrown by the API methods has a `code` property. In v1, the `code` property contained the http status code.
In v2, the `code` property contains the [PostgREST error code](https://postgrest.org/en/stable/references/errors.html), which is more useful for debugging.
BeforeAfter
```

1
2
3
4
5
try {await supabase.from('countries').select();} onPostgrestExceptioncatch (error) { error.code;// Contains http status code}

```

### Realtime methods[#](https://supabase.com/docs/reference/dart/auth-updateuser#realtime-methods)
Realtime methods contains the biggest breaking changes. Most of these changes are to make the interface more type safe.
We have removed the `.on()` method and replaced it with `.onPostgresChanges()`, `.onBroadcast()`, and three different presence methods.
#### Postgres Changes[#](https://supabase.com/docs/reference/dart/auth-updateuser#postgres-changes)
Use the new `.onPostgresChanges()` method to listen to realtime changes in the database.
In v1, filters were not strongly typed because they took a `String` type. In v2, `filter` takes an object. Its properties are strictly typed to catch type errors.
The payload of the callback is now typed as well. In `v1`, the payload was returned as `dynamic`. It is now returned as a `PostgresChangePayload` object. The object contains the `oldRecord` and `newRecord` properties for accessing the data before and after the change.
BeforeAfter
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
supabase.channel('my_channel').on(RealtimeListenTypes.postgresChanges,ChannelFilter(  event:'*',  schema:'public',  table:'messages',  filter:'room_id=eq.200', ), (dynamic payload, [ref]) {finalMap<String, dynamic> newRecord = payload['new'];finalMap<String, dynamic> oldRecord = payload['old']; },).subscribe();

```

#### Broadcast[#](https://supabase.com/docs/reference/dart/auth-updateuser#broadcast)
Broadcast now uses the dedicated `.onBroadcast()` method, rather than the generic `.on()` method. Because the method is specific to broadcast, it takes fewer properties.
BeforeAfter
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
supabase.channel('my_channel').on(RealtimeListenTypes.broadcast,ChannelFilter(  event:'position', ), (dynamic payload, [ref]) {print(payload); },).subscribe();

```

#### Presence[#](https://supabase.com/docs/reference/dart/auth-updateuser#presence)
Realtime Presence gets three different methods for listening to three different presence events: `sync`, `join`, and `leave`. This allows the callback to be strictly typed.
BeforeAfter
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
final channel = supabase.channel('room1');channel.on(RealtimeListenTypes.presence,ChannelFilter(event:'sync'), (payload, [ref]) {print('Synced presence state: ${channel.presenceState()}'); },).on(RealtimeListenTypes.presence,ChannelFilter(event:'join'), (payload, [ref]) {print('Newly joined presences $payload'); },).on(RealtimeListenTypes.presence,ChannelFilter(event:'leave'), (payload, [ref]) {print('Newly left presences: $payload'); },).subscribe( (status, [error]) async {if (status =='SUBSCRIBED') {await channel.track({'online_at':DateTime.now().toIso8601String()});  } },);

```

## Fetch data
Perform a SELECT query on the table or view.
  * By default, Supabase projects will return a maximum of 1,000 rows. This setting can be changed in Project API Settings. It's recommended that you keep it low to limit the payload size of accidental or malicious requests. You can use `range()` queries to paginate through your data.
  * `select()` can be combined with [Filters](https://supabase.com/docs/reference/dart/using-filters)
  * `select()` can be combined with [Modifiers](https://supabase.com/docs/reference/dart/using-modifiers)
  * `apikey` is a reserved keyword if you're using the [Supabase Platform](https://supabase.com/docs/guides/platform) and [should be avoided as a column name](https://github.com/supabase/supabase/issues/5465).


### Parameters
  * columnsOptionalString
The columns to retrieve, separated by commas. Columns can be renamed when returned with `customName:columnName`


Getting your dataSelecting specific columnsQuery referenced tablesQuery referenced tables through a join tableQuery the same referenced table multiple timesFiltering through referenced tablesQuerying with count optionQuerying JSON dataQuerying referenced table with inner joinSwitching schemas per query
```

1
2
3
final data =await supabase.from('instruments').select();

```

Data source
Response
## Insert data
Perform an INSERT into the table or view.
### Parameters
  * valuesRequiredMap<String, dynamic> or List<Map<String, dynamic>>
The values to insert. Pass an object to insert a single row or an array to insert multiple rows.


Create a recordFetch inserted recordBulk create
```

1
2
3
await supabase.from('cities').insert({'name':'The Shire','country_id':554});

```

Data source
## Update data
Perform an UPDATE on the table or view.
  * `update()` should always be combined with [Filters](https://supabase.com/docs/reference/dart/using-filters) to target the item(s) you wish to update.


### Parameters
  * valuesRequiredMap<String, dynamic>
The values to update with.


Update your dataUpdate a record and return itUpdate JSON data
```

1
2
3
4
await supabase.from('instruments').update({ 'name':'piano' }).eq('id',1);

```

Data source
## Upsert data
Perform an UPSERT on the table or view. Depending on the column(s) passed to `onConflict`, `.upsert()` allows you to perform the equivalent of `.insert()` if a row with the corresponding `onConflict` columns doesn't exist, or if it does exist, perform an alternative action depending on `ignoreDuplicates`.
  * Primary keys must be included in `values` to use upsert.


### Parameters
  * valuesRequiredMap<String, dynamic> or List<Map<String, dynamic>>
The values to upsert with. Pass a Map to upsert a single row or an List to upsert multiple rows.
  * onConflictOptionalString
Comma-separated UNIQUE column(s) to specify how duplicate rows are determined. Two rows are duplicates if all the `onConflict` columns are equal.
  * ignoreDuplicatesOptionalbool
If `true`, duplicate rows are ignored. If `false`, duplicate rows are merged with existing rows.
  * defaultToNullOptionalbool
Make missing fields default to `null`. Otherwise, use the default value for the column. This only applies when inserting new rows, not when merging with existing rows where ignoreDuplicates is set to false. This also only applies when doing bulk upserts.


Upsert your dataBulk Upsert your dataUpserting into tables with constraints
```

1
2
3
4
final data =await supabase.from('instruments').upsert({ 'id':1,'name':'piano' }).select();

```

Data source
Response
## Delete data
Perform a DELETE on the table or view.
  * `delete()` should always be combined with [Filters](https://supabase.com/docs/reference/dart/using-filters) to target the item(s) you wish to delete.
  * If you use `delete()` with filters and you have RLS enabled, only rows visible through `SELECT` policies are deleted. Note that by default no rows are visible, so you need at least one `SELECT`/`ALL` policy that makes the rows visible.


Delete recordsDelete multiple recordsFetch deleted records
```

1
2
3
4
await supabase.from('countries').delete().eq('id',1);

```

Data source
## Call a Postgres function
Perform a function call.
You can call Postgres functions as Remote Procedure Calls, logic in your database that you can execute from anywhere. Functions are useful when the logic rarely changes—like for password resets and updates.
### Parameters
  * fnRequiredString
The function name to call.
  * paramsOptionalMap<String, dynamic>
The arguments to pass to the function call.


Call a Postgres function without argumentsCall a Postgres function with argumentsBulk processingCall a Postgres function with filters
```

1
2
final data =await supabase.rpc('hello_world');

```

Data source
Response
## Using filters
Filters allow you to only return rows that match certain conditions.
Filters can be used on `select()`, `update()`, `upsert()`, and `delete()` queries.
If a Database function returns a table response, you can also apply filters.
Applying FiltersChaining FiltersConditional ChainingFilter by values within a JSON columnFilter Referenced Tables
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
final data =await supabase.from('cities').select('name, country_id').eq('name','The Shire');// Correctfinal data =await supabase.from('cities').eq('name','The Shire') // Incorrect.select('name, country_id');

```

Notes
## Column is equal to a value
Match only rows where `column` is equal to `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredObject
The value to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('instruments').select().eq('name','viola');

```

Data source
Response
## Column is not equal to a value
Finds all rows whose value on the stated `column` doesn't match the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredObject
The value to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('instruments').select('id, name').neq('name','viola');

```

Data source
Response
## Column is greater than a value
Finds all rows whose value on the stated `column` is greater than the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredObject
The value to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('countries').select().gt('id',2);

```

Data source
Response
## Column is greater than or equal to a value
Finds all rows whose value on the stated `column` is greater than or equal to the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredObject
The value to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('countries').select().gte('id',2);

```

Data source
Response
## Column is less than a value
Finds all rows whose value on the stated `column` is less than the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredObject
The value to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('countries').select().lt('id',2);

```

Data source
Response
## Column is less than or equal to a value
Finds all rows whose value on the stated `column` is less than or equal to the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredObject
The value to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('countries').select().lte('id',2);

```

Data source
Response
## Column matches a pattern
Finds all rows whose value in the stated `column` matches the supplied `pattern` (case sensitive).
### Parameters
  * columnRequiredString
The column to filter on.
  * patternRequiredString
The pattern to match with.


With select()
```

1
2
3
4
final data =await supabase.from('planets').select().like('name','%Ea%');

```

Data source
Response
## Column matches a case-insensitive pattern
Finds all rows whose value in the stated `column` matches the supplied `pattern` (case insensitive).
### Parameters
  * columnRequiredString
The column to filter on.
  * patternRequiredString
The pattern to match with.


With select()
```

1
2
3
4
final data =await supabase.from('planets').select().ilike('name','%ea%');

```

Data source
Response
## Column is a value
A check for exact equality (null, true, false), finds all rows whose value on the stated `column` exactly match the specified `value`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valueRequiredObject?
The value to filter with.


Checking for nullness, true or false
```

1
2
3
4
final data =await supabase.from('countries').select().isFilter('name',null);

```

Data source
Response
Notes
## Column is in an array
Finds all rows whose value on the stated `column` is found on the specified `values`.
### Parameters
  * columnRequiredString
The column to filter on.
  * valuesRequiredList
The List to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('characters').select().inFilter('name', ['Luke','Leia']);

```

Data source
Response
Notes
## Column contains every element in a value
Only relevant for jsonb, array, and range columns. Match only rows where `column` contains every element appearing in `value`.
### Parameters
  * columnRequiredString
The jsonb, array, or range column to filter on.
  * valueRequiredObject
The jsonb, array, or range value to filter with.


On array columnsOn range columnsOn `jsonb` columns
```

1
2
3
4
final data =await supabase.from('issues').select().contains('tags', ['is:open','priority:low']);

```

Data source
Response
Notes
## Contained by value
Only relevant for jsonb, array, and range columns. Match only rows where every element appearing in `column` is contained by `value`.
### Parameters
  * columnRequiredString
The jsonb, array, or range column to filter on.
  * valueRequiredObject
The jsonb, array, or range value to filter with.


On array columnsOn range columnsOn `jsonb` columns
```

1
2
3
4
final data =await supabase.from('classes').select('name').containedBy('days', ['monday','tuesday','wednesday','friday']);

```

Data source
Response
## Greater than a range
Only relevant for range columns. Match only rows where every element in `column` is greater than any element in `range`.
### Parameters
  * columnRequiredString
The range column to filter on.
  * rangeRequiredString
The range to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('reservations').select().rangeGt('during','[2000-01-02 08:00, 2000-01-02 09:00)');

```

Data source
Response
Notes
## Greater than or equal to a range
Only relevant for range columns. Match only rows where every element in `column` is either contained in `range` or greater than any element in `range`.
### Parameters
  * columnRequiredString
The range column to filter on.
  * rangeRequiredString
The range to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('reservations').select().rangeGte('during','[2000-01-02 08:30, 2000-01-02 09:30)');

```

Data source
Response
Notes
## Less than a range
Only relevant for range columns. Match only rows where every element in `column` is less than any element in `range`.
### Parameters
  * columnRequiredString
The range column to filter on.
  * rangeRequiredString
The range to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('reservations').select().rangeLt('during','[2000-01-01 15:00, 2000-01-01 16:00)');

```

Data source
Response
Notes
## Less than or equal to a range
Only relevant for range columns. Match only rows where every element in `column` is either contained in `range` or less than any element in `range`.
### Parameters
  * columnRequiredString
The range column to filter on.
  * rangeRequiredString
The range to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('reservations').select().rangeLte('during','[2000-01-01 15:00, 2000-01-01 16:00)');

```

Data source
Response
Notes
## Mutually exclusive to a range
Only relevant for range columns. Match only rows where `column` is mutually exclusive to `range` and there can be no element between the two ranges.
### Parameters
  * columnRequiredString
The range column to filter on.
  * rangeRequiredString
The range to filter with.


With select()
```

1
2
3
4
final data =await supabase.from('reservations').select().rangeAdjacent('during','[2000-01-01 12:00, 2000-01-01 13:00)');

```

Data source
Response
Notes
## With a common element
Only relevant for array and range columns. Match only rows where `column` and `value` have an element in common.
### Parameters
  * columnRequiredString
The array or range column to filter on.
  * valueRequiredObject
The array or range value to filter with.


On array columnsOn range columns
```

1
2
3
4
final data =await supabase.from('issues').select('title').overlaps('tags', ['is:closed','severity:high']);

```

Data source
Response
## Match a string
Finds all rows whose tsvector value on the stated `column` matches to_tsquery(query).
### Parameters
  * columnRequiredString
The text or tsvector column to filter on.
  * queryRequiredString
The query text to match with.
  * configOptionalString
The text search configuration to use.
  * typeOptionalTextSearchType
Change how the `query` text is interpreted.


Text searchBasic normalizationFull normalizationWebsearch
```

1
2
3
4
5
6
final data =await supabase.from('quotes').select('catchphrase').textSearch('content',"'eggs' & 'ham'",  config:'english' );

```

Data source
Response
## Match an associated value
Finds all rows whose columns match the specified `query` object.
### Parameters
  * queryRequiredMap<String, dynamic>
The object to filter with, with column names as keys mapped to their filter values


With select()
```

1
2
3
4
final data =await supabase.from('instruments').select().match({ 'id':2,'name':'viola' });

```

Data source
Response
## Don't match the filter
Finds all rows which doesn't satisfy the filter.
  * `.not()` expects you to use the raw [PostgREST syntax](https://postgrest.org/en/stable/api.html#horizontal-filtering-rows) for the filter names and values.
```

1
2
3
4
5
.not('name','eq','violin').not('arraycol','cs','{"a","b"}') // Use Postgres array {} for array column and 'cs' for contains..not('rangecol','cs','(1,2]') // Use Postgres range syntax for range column..not('id','in','(6,7)') // Use Postgres list () and 'in' instead of `inFilter`..not('id','in','(${mylist.join(',')})') // You can insert a Dart list array.

```



### Parameters
  * columnRequiredString
The column to filter on.
  * operatorRequiredString
The operator to be negated to filter with, following PostgREST syntax.
  * valueOptionalObject
The value to filter with, following PostgREST syntax.


With select()With update()With delete()With rpc()
```

1
2
3
4
final data =await supabase.from('countries').select().not('name','is',null)

```

Data source
Response
## Match at least one filter
Finds all rows satisfying at least one of the filters.
  * `.or()` expects you to use the raw [PostgREST syntax](https://postgrest.org/en/stable/api.html#horizontal-filtering-rows) for the filter names and values.
```

1
2
3
.or('id.in.(6,7),arraycol.cs.{"a","b"}') // Use Postgres list () and 'in' instead of `inFilter`. Array {} and 'cs' for contains..or('id.in.(${mylist.join(',')}),arraycol.cs.{${mylistArray.join(',')}}')	// You can insert a Dart list for list or array column..or('id.in.(${mylist.join(',')}),rangecol.cs.(${mylistRange.join(',')}]')	// You can insert a Dart list for list or range column.

```



### Parameters
  * filtersRequiredString
The filters to use, following PostgREST syntax
  * referencedTableOptionalString
Set this to filter on referenced tables instead of the parent table


With select()Use `or` with `and`Use `or` on referenced tables
```

1
2
3
4
final data =await supabase.from('instruments').select('name').or('id.eq.2,name.eq.cello');

```

Data source
Response
## Match the filter
Match only rows which satisfy the filter. This is an escape hatch - you should use the specific filter methods wherever possible.
`.filter()` expects you to use the raw [PostgREST syntax](https://postgrest.org/en/stable/api.html#horizontal-filtering-rows) for the filter names and values, so it should only be used as an escape hatch in case other filters don't work.
```

1
2
3
4
.filter('arraycol','cs','{"a","b"}') // Use Postgres array {} and 'cs' for contains..filter('rangecol','cs','(1,2]') // Use Postgres range syntax for range column..filter('id','in','(6,7)') // Use Postgres list () and 'in' for in_ filter..filter('id','cs','{${mylist.join(',')}}') // You can insert a Dart array list.

```

### Parameters
  * columnRequiredString
The column to filter on.
  * operatorRequiredString
The operator to filter with, following PostgREST syntax.
  * valueRequiredObject
The value to filter with, following PostgREST syntax.


With select()With update()With delete()With rpc()On a referenced table
```

1
2
3
4
final data =await supabase.from('characters').select().filter('name','in','("Ron","Dumbledore")')

```

Data source
Response
## Using modifiers
Filters work on the row level. That is, they allow you to return rows that only match certain conditions without changing the shape of the rows. Modifiers are everything that don't fit that definition—allowing you to change the format of the response (e.g., returning a CSV string).
Modifiers must be specified after filters. Some modifiers only apply for queries that return rows (e.g., `select()` or `rpc()` on a function that returns a table response).
## Return data after inserting
With `upsert()`
```

1
2
3
4
final data =await supabase.from('instruments').upsert({ 'id':1,'name':'piano' }).select();

```

Data source
Response
## Order the results
Orders the result with the specified column.
### Parameters
  * columnRequiredString
The column to order by.
  * ascendingOptionalbool
Whether to order in ascending order. Default is `false`.
  * nullsFirstOptionalbool
Whether to order nulls first. Default is `false`.
  * referencedTableOptionalString
Specify the referenced table when ordering by a column in an embedded resource.


With select()On a referenced tableOrder parent table by a referenced table
```

1
2
3
4
final data =await supabase.from('instruments').select('id, name').order('id', ascending:false);

```

Data source
Response
## Limit the number of rows returned
Limits the result with the specified count.
### Parameters
  * countRequiredint
The maximum number of rows to return.
  * referencedTableOptionalint
Set this to limit rows of referenced tables instead of the parent table.


With select()On a referenced table
```

1
2
3
4
final data =await supabase.from('instruments').select('name').limit(1);

```

Data source
Response
## Limit the query to a range
Limits the result to rows within the specified range, inclusive.
### Parameters
  * fromRequiredint
The starting index from which to limit the result.
  * toRequiredint
The last index to which to limit the result.
  * referencedTableOptionalString
Set this to limit rows of referenced tables instead of the parent table.


With select()
```

1
2
3
4
final data =await supabase.from('instruments').select('name').range(0,1);

```

Data source
Response
## Retrieve one row of data
Retrieves only one row from the result. Result must be one row (e.g. using limit), otherwise this will result in an error.
With select()
```

1
2
3
4
5
final data =await supabase.from('instruments').select('name').limit(1).single();

```

Data source
Response
## Retrieve zero or one row of data
With `select()`
```

1
2
3
4
5
final data =await supabase.from('instruments').select().eq('name','guzheng').maybeSingle();

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
final data =await supabase.from('instruments').select().csv();

```

Data source
Response
Notes
## Using explain
For debugging slow queries, you can get the [Postgres `EXPLAIN` execution plan](https://www.postgresql.org/docs/current/sql-explain.html) of a query using the `explain()` method. This works on any query, even for `rpc()` or writes.
Explain is not enabled by default as it can reveal sensitive information about your database. It's best to only enable this for testing environments but if you wish to enable it for production you can provide additional protection by using a `pre-request` function.
Follow the [Performance Debugging Guide](https://supabase.com/docs/guides/database/debugging-performance) to enable the functionality on your project.
### Parameters
  * analyzeOptionalbool
If `true`, the query will be executed and the actual run time will be returned.
  * verboseOptionalbool
If `true`, the query identifier will be returned and `data` will include the output columns of the query.
  * settingsOptionalbool
If `true`, include information on configuration parameters that affect query planning.
  * buffersOptionalbool
If `true`, include information on buffer usage.
  * walOptionalbool
If `true`, include information on WAL record generation.


Get the execution planGet the execution plan with analyze and verbose
```

1
2
3
4
final data =await supabase.from('instruments').select().explain();

```

Data source
Response
Notes
## Create a new user
Creates a new user.
  * By default, the user needs to verify their email address before logging in. To turn this off, disable **Confirm email** in [your project](https://supabase.com/dashboard/project/_/auth/providers).
  * **Confirm email** determines if users need to confirm their email address after signing up. 
    * If **Confirm email** is enabled, a `user` is returned but `session` is null.
    * If **Confirm email** is disabled, both a `user` and a `session` are returned.
  * When the user confirms their email address, they are redirected to the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls) by default. You can modify your `SITE_URL` or add additional redirect URLs in [your project](https://supabase.com/dashboard/project/_/auth/url-configuration).
  * If signUp() is called for an existing confirmed user: 
    * When both **Confirm email** and **Confirm phone** (even when phone provider is disabled) are enabled in [your project](https://supabase.com/dashboard/project/_/auth/providers), an obfuscated/fake user object is returned.
    * When either **Confirm email** or **Confirm phone** (even when phone provider is disabled) is disabled, the error message, `User already registered` is returned.


### Parameters
  * emailOptionalString
User's email address to be used for email authentication.
  * phoneOptionalString
User's phone number to be used for phone authentication.
  * passwordRequiredString
Password to be used for authentication.
  * emailRedirectToOptionalString
The URL to redirect the user to after they confirm their email address.
  * dataOptionalMap<String, dynamic>
The user's metadata to be stored in the user's object.
  * captchaTokenOptionalString
The captcha token to be used for captcha verification.
  * channelOptionalOtpChannel
Messaging channel to use (e.g. whatsapp or sms). Defaults to `OtpChannel.sms`.


Sign up with an email and passwordSign up with a phone number and password (SMS)Sign up with additional metadataSign up with redirect URL
```

1
2
3
4
5
6
finalAuthResponse res =await supabase.auth.signUp( email:'example@email.com', password:'example-password',);finalSession? session = res.session;finalUser? user = res.user;

```

Response
## Listen to auth events
Receive a notification every time an auth event happens.
  * Types of auth events: `AuthChangeEvent.passwordRecovery`, `AuthChangeEvent.signedIn`, `AuthChangeEvent.signedOut`, `AuthChangeEvent.tokenRefreshed`, `AuthChangeEvent.userUpdated`and `AuthChangeEvent.userDeleted`


Listen to auth changesListen to a specific eventUnsubscribe from auth subscription
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
final authSubscription = supabase.auth.onAuthStateChange.listen((data) {finalAuthChangeEvent event = data.event;finalSession? session = data.session;print('event: $event, session: $session');switch (event) {caseAuthChangeEvent.initialSession:// handle initial sessioncaseAuthChangeEvent.signedIn:// handle signed incaseAuthChangeEvent.signedOut:// handle signed outcaseAuthChangeEvent.passwordRecovery:// handle password recoverycaseAuthChangeEvent.tokenRefreshed:// handle token refreshedcaseAuthChangeEvent.userUpdated:// handle user updatedcaseAuthChangeEvent.userDeleted:// handle user deletedcaseAuthChangeEvent.mfaChallengeVerified:// handle mfa challenge verified }});

```

## Create an anonymous user
Creates an anonymous user.
  * Returns an anonymous user
  * It is recommended to set up captcha for anonymous sign-ins to prevent abuse. You can pass in the captcha token in the `options` param.


### Parameters
  * dataOptionalMap<String, dynamic>
The user's metadata to be stored in the user's object.
  * captchaTokenOptionalString
The captcha token to be used for captcha verification.


Create an anonymous userCreate an anonymous user with custom user metadata
```

1
await supabase.auth.signInAnonymously();

```

Response
## Sign in a user
Log in an existing user using email or phone number with password.
  * Requires either an email and password or a phone number and password.


### Parameters
  * emailOptionalString
User's email address to be used for email authentication.
  * phoneOptionalString
User's phone number to be used for phone authentication.
  * passwordRequiredString
Password to be used for authentication.
  * captchaTokenOptionalString
The captcha token to be used for captcha verification.


Sign in with email and passwordSign in with phone and password
```

1
2
3
4
5
6
finalAuthResponse res =await supabase.auth.signInWithPassword( email:'example@email.com', password:'example-password',);finalSession? session = res.session;finalUser? user = res.user;

```

Response
## Sign in with ID Token
Allows you to perform native Google and Apple sign in by combining it with [google_sign_in](https://pub.dev/packages/google_sign_in) or [sign_in_with_apple](https://pub.dev/packages/sign_in_with_apple) packages.
### Parameters
  * providerRequiredOAuthProvider
The provider to perform the sign in with. Currently, `OAuthProvider.google` and `OAuthProvider.apple` are supported.
  * idTokenRequiredString
The identity token obtained from the third-party provider.
  * accessTokenOptionalString
Access token obtained from the third-party provider. Required for Google sign in.
  * nonceOptionalString
Raw nonce value used to perform the third-party sign in. Required for Apple sign-in.
  * captchaTokenOptionalString
The captcha token to be used for captcha verification.


Native Google sign inNative Apple Sign in
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
import'package:google_sign_in/google_sign_in.dart';import'package:supabase_flutter/supabase_flutter.dart';const webClientId ='<web client ID that you registered on Google Cloud, for example my-web.apps.googleusercontent.com>';const iosClientId ='<iOS client ID that you registered on Google Cloud, for example my-ios.apps.googleusercontent.com';finalGoogleSignIn googleSignIn =GoogleSignIn( clientId: iosClientId, serverClientId: webClientId,);final googleUser =await googleSignIn.signIn();final googleAuth =await googleUser!.authentication;final accessToken = googleAuth.accessToken;final idToken = googleAuth.idToken;if (accessToken ==null) {throw'No Access Token found.';}if (idToken ==null) {throw'No ID Token found.';}final response =await supabase.auth.signInWithIdToken( provider:OAuthProvider.google, idToken: idToken, accessToken: accessToken,);

```

Response
Notes
## Sign in a user through OTP
  * Requires either an email or phone number.
  * This method is used for passwordless sign-ins where an OTP is sent to the user's email or phone number.
  * If you're using an email, you can configure whether you want the user to receive a magiclink or an OTP.
  * If you're using phone, you can configure whether you want the user to receive an OTP.
  * The magic link's destination URL is determined by the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls). You can modify the `SITE_URL` or add additional redirect urls in [your project](https://supabase.com/dashboard/project/_/auth/url-configuration).


### Parameters
  * emailOptionalString
Email address to send the magic link or OTP to.
  * phoneOptionalString
Phone number to send the OTP to.
  * emailRedirectToOptionalString
The URL to redirect the user to after they click on the magic link.
  * shouldCreateUserOptionalbool
If set to false, this method will not create a new user. Defaults to true.
  * dataOptionalMap<String, dynamic>
The user's metadata to be stored in the user's object.
  * captchaTokenOptionalString
The captcha token to be used for captcha verification.
  * channelOptionalOtpChannel
Messaging channel to use (e.g. whatsapp or sms). Defaults to `OtpChannel.sms`.


Sign in with email.Sign in with SMS OTP.Sign in with WhatsApp OTP
```

1
2
3
4
await supabase.auth.signInWithOtp( email:'example@email.com', emailRedirectTo: kIsWeb ?null:'io.supabase.flutter://signin-callback/',);

```

Response
Notes
## Sign in a user through OAuth
Signs the user in using third-party OAuth providers.
  * This method is used for signing in using a third-party provider.
  * Supabase supports many different [third-party providers](https://supabase.com/docs/guides/auth#providers).


### Parameters
  * providerRequiredOAuthProvider
The OAuth provider to use for signing in.
  * redirectToOptionalString
The URL to redirect the user to after they sign in with the third-party provider.
  * scopesOptionalString
A list of scopes to request from the third-party provider.
  * authScreenLaunchModeOptionalLaunchMode
The launch mode for the auth screen. Defaults to `LaunchMode.platformDefault`.
  * queryParamsOptionalMap<String, String>
Additional query parameters to be passed to the OAuth flow.


Sign in using a third-party providerWith `redirectTo`With scopes
```

1
2
3
4
5
6
await supabase.auth.signInWithOAuth(OAuthProvider.github, redirectTo: kIsWeb ?null:'my.scheme://my-host',// Optionally set the redirect link to bring back the user via deeplink. authScreenLaunchMode:   kIsWeb ?LaunchMode.platformDefault :LaunchMode.externalApplication,// Launch the auth screen in a new webview on mobile.);

```

## Sign in a user through SSO
  * Before you can call this method you need to [establish a connection](https://supabase.com/docs/guides/auth/sso/auth-sso-saml#managing-saml-20-connections) to an identity provider. Use the [CLI commands](https://supabase.com/docs/reference/cli/supabase-sso) to do this.
  * If you've associated an email domain to the identity provider, you can use the `domain` property to start a sign-in flow.
  * In case you need to use a different way to start the authentication flow with an identity provider, you can use the `providerId` property. For example: 
    * Mapping specific user email addresses with an identity provider.
    * Using different hints to identify the correct identity provider, like a company-specific page, IP address or other tracking information.


### Parameters
  * providerIdOptionalString
The ID of the SSO provider to use for signing in.
  * domainOptionalString
The email domain to use for signing in.
  * redirectToOptionalString
The URL to redirect the user to after they sign in with the third-party provider.
  * captchaTokenOptionalString
The captcha token to be used for captcha verification.
  * launchModeOptionalLaunchMode
The launch mode for the auth screen. Defaults to `LaunchMode.platformDefault`.


Sign in with email domainSign in with provider UUID
```

1
2
3
await supabase.auth.signInWithSSO( domain:'company.com',);

```

## Sign out a user
Signs out the current user, if there is a logged in user.
  * In order to use the `signOut()` method, the user needs to be signed in first.


### Parameters
  * scopeOptionalSignOutScope
Whether to sign out from all devices or just the current device. Defaults to `SignOutScope.local`.


Sign out
```

1
await supabase.auth.signOut();

```

## Verify and log in through OTP
  * The `verifyOtp` method takes in different verification types. If a phone number is used, the type can either be `sms` or `phone_change`. If an email address is used, the type can be one of the following: `signup`, `magiclink`, `recovery`, `invite` or `email_change`.
  * The verification type used should be determined based on the corresponding auth method called before `verifyOtp` to sign up or sign in a user.


### Parameters
  * tokenRequiredString
The token that user was sent to their email or mobile phone
  * typeRequiredOtpType
Type of the OTP to verify
  * emailOptionalString
Email address that the OTP was sent to
  * phoneOptionalString
Phone number that the OTP was sent to
  * redirectToOptionalString
URI to redirect the user to after the OTP is verified
  * captchaTokenOptionalString
The captcha token to be used for captcha verification
  * tokenHashOptionalString
Token used in an email link


Verify Signup One-Time Password (OTP)Verify SMS One-Time Password (OTP)
```

1
2
3
4
5
6
7
finalAuthResponse res =await supabase.auth.verifyOTP( type:OtpType.signup, token: token, phone:'+13334445555',);finalSession? session = res.session;finalUser? user = res.user;

```

Response
## Retrieve a session
Returns the session data, if there is an active session.
Get the session data
```

1
finalSession? session = supabase.auth.currentSession;

```

Response
## Retrieve a new session
  * This method will refresh and return a new session whether the current one is expired or not.


Refresh session using the current session
```

1
2
finalAuthResponse res =await supabase.auth.refreshSession();final session = res.session;

```

Response
## Retrieve a user
Returns the user data, if there is a logged in user.
Get the logged in user
```

1
finalUser? user = supabase.auth.currentUser;

```

Response
## Update a user
Updates user data for a logged in user.
  * In order to use the `updateUser()` method, the user needs to be signed in first.
  * By default, email updates sends a confirmation link to both the user's current and new email. To only send a confirmation link to the user's new email, disable **Secure email change** in your project's [email auth provider settings](https://supabase.com/dashboard/project/_/auth/providers).


### Parameters
  * attributesRequiredUserAttributes
Attributes to update for the user.
Details
  * emailRedirectToOptionalString
The URI to redirect the user to after the email is updated.


Update the email for an authenticated userUpdate the password for an authenticated userUpdate the user's metadataUpdate the user's password with a nonce
```

1
2
3
4
5
6
finalUserResponse res =await supabase.auth.updateUser(UserAttributes(  email:'example@email.com', ),);finalUser? updatedUser = res.user;

```

Response
Notes
## Retrieve identities linked to a user
Gets all the identities linked to a user.
  * The user needs to be signed in to call `getUserIdentities()`.


Returns a list of identities linked to the user
```

1
final identities =await supabase.auth.getUserIdentities();

```

Response
## Link an identity to a user
Links an oauth identity to an existing user. This method supports the PKCE flow.
  * The **Enable Manual Linking** option must be enabled from your [project's authentication settings](https://supabase.com/dashboard/project/_/settings/auth).
  * The user needs to be signed in to call `linkIdentity()`.
  * If the candidate identity is already linked to the existing user or another user, `linkIdentity()` will fail.


### Parameters
  * providerRequiredOAuthProvider
The provider to link the identity to.
  * redirectToOptionalString
The URL to redirect the user to after they sign in with the third-party provider.
  * scopesOptionalString
A list of scopes to request from the third-party provider.
  * authScreenLaunchModeOptionalLaunchMode
The launch mode for the auth screen. Defaults to `LaunchMode.platformDefault`.
  * queryParamsOptionalMap<String, String>
Additional query parameters to be passed to the OAuth flow.


Link an identity to a user
```

1
await supabase.auth.linkIdentity(OAuthProvider.google);

```

## Unlink an identity from a user
Unlinks an identity from a user by deleting it. The user will no longer be able to sign in with that identity once it's unlinked.
  * The **Enable Manual Linking** option must be enabled from your [project's authentication settings](https://supabase.com/dashboard/project/_/settings/auth).
  * The user needs to be signed in to call `unlinkIdentity()`.
  * The user must have at least 2 identities in order to unlink an identity.
  * The identity to be unlinked must belong to the user.


### Parameters
  * identityRequiredUserIdentity
The user identity to unlink.


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
// retrieve all identites linked to a userfinal identities =await supabase.auth.getUserIdentities();// find the google identityfinal googleIdentity = identities.firstWhere( (element) => element.provider =='google',);// unlink the google identityawait supabase.auth.unlinkIdentity(googleIdentity);

```

## Send a password reauthentication nonce
  * This method is used together with `updateUser()` when a user's password needs to be updated.
  * This method sends a nonce to the user's email. If the user doesn't have a confirmed email address, the method sends the nonce to the user's confirmed phone number instead.


Send reauthentication nonce
```

1
await supabase.auth.reauthenticate();

```

Notes
## Resend an OTP
  * Resends a signup confirmation, email change, or phone change email to the user.
  * Passwordless sign-ins can be resent by calling the `signInWithOtp()` method again.
  * Password recovery emails can be resent by calling the `resetPasswordForEmail()` method again.
  * This method only resend an email or phone OTP to the user if an initial signup, email change, or phone change request was made.


Resend an email signup confirmation
```

1
2
3
4
finalResendResponse res =await supabase.auth.resend( type:OtpType.signup, email:'email@example.com',);

```

Notes
## Set the session data
  * `setSession()` takes in a refresh token and uses it to get a new session.
  * The refresh token can only be used once to obtain a new session.
  * [Refresh token rotation](https://supabase.com/docs/guides/cli/config#auth.enable_refresh_token_rotation) is enabled by default on all projects to guard against replay attacks.
  * You can configure the [`REFRESH_TOKEN_REUSE_INTERVAL`](https://supabase.com/docs/guides/cli/config#auth.refresh_token_reuse_interval) which provides a short window in which the same refresh token can be used multiple times in the event of concurrency or offline issues.


### Parameters
  * refreshTokenRequiredString
Refresh token to use to get a new session.


Refresh the session
```

1
2
3
4
final refreshToken = supabase.currentSession?.refreshToken ??'';finalAuthResponse response =await supabase.auth.setSession(refreshToken);final session = res.session;

```

Response
Notes
## Auth MFA
This section contains methods commonly used for Multi-Factor Authentication (MFA) and are invoked behind the `supabase.auth.mfa` namespace.
Currently, we only support time-based one-time password (TOTP) as the 2nd factor. We don't support recovery codes but we allow users to enroll more than 1 TOTP factor, with an upper limit of 10.
Having a 2nd TOTP factor for recovery means the user doesn't have to store their recovery codes. It also reduces the attack surface since the recovery factor is usually time-limited and not a single static code.
Learn more about implementing MFA on your application on our guide [here](https://supabase.com/docs/guides/auth/auth-mfa#overview).
## Enroll a factor
Starts the enrollment process for a new Multi-Factor Authentication (MFA) factor. This method creates a new `unverified` factor. To verify a factor, present the QR code or secret to the user and ask them to add it to their authenticator app. The user has to enter the code from their authenticator app to verify it.
  * Currently, `totp` is the only supported `factorType`. The returned `id` should be used to create a challenge.
  * To create a challenge, see [`mfa.challenge()`](https://supabase.com/docs/reference/dart/auth-mfa-challenge).
  * To verify a challenge, see [`mfa.verify()`](https://supabase.com/docs/reference/dart/auth-mfa-verify).
  * To create and verify a challenge in a single step, see [`mfa.challengeAndVerify()`](https://supabase.com/docs/reference/dart/auth-mfa-challengeandverify).


### Parameters
  * factorTypeOptionalString
Type of factor being enrolled.
  * issuerOptionalString
Domain which the user is enrolled with.
  * friendlyNameOptionalString
Human readable name assigned to the factor.


Enroll a time-based, one-time password (TOTP) factor
```

1
2
3
final res =await supabase.auth.mfa.enroll(factorType:FactorType.totp);final qrCodeUrl = res.totp.qrCode;

```

Response
## Create a challenge
Prepares a challenge used to verify that a user has access to a MFA factor.
  * An [enrolled factor](https://supabase.com/docs/reference/dart/auth-mfa-enroll) is required before creating a challenge.
  * To verify a challenge, see [`mfa.verify()`](https://supabase.com/docs/reference/dart/auth-mfa-verify).


### Parameters
  * factorIdRequiredString
System assigned identifier for authenticator device as returned by enroll


Create a challenge for a factor
```

1
2
3
final res =await supabase.auth.mfa.challenge( factorId:'34e770dd-9ff9-416c-87fa-43b31d7ef225',);

```

Response
## Verify a challenge
Verifies a code against a challenge. The verification code is provided by the user by entering a code seen in their authenticator app.
  * To verify a challenge, please [create a challenge](https://supabase.com/docs/reference/dart/auth-mfa-challenge) first.


### Parameters
  * factorIdRequiredString
System assigned identifier for authenticator device as returned by enroll
  * challengeIdRequiredString
The ID of the challenge to verify
  * codeRequiredString
The verification code on the user's authenticator app


Verify a challenge for a factor
```

1
2
3
4
5
final res =await supabase.auth.mfa.verify( factorId:'34e770dd-9ff9-416c-87fa-43b31d7ef225', challengeId:'4034ae6f-a8ce-4fb5-8ee5-69a5863a7c15', code:'123456',);

```

Response
## Create and verify a challenge
Helper method which creates a challenge and immediately uses the given code to verify against it thereafter. The verification code is provided by the user by entering a code seen in their authenticator app.
  * An [enrolled factor](https://supabase.com/docs/reference/dart/auth-mfa-enroll) is required before invoking `challengeAndVerify()`.
  * Executes [`mfa.challenge()`](https://supabase.com/docs/reference/dart/auth-mfa-challenge) and [`mfa.verify()`](https://supabase.com/docs/reference/dart/auth-mfa-verify) in a single step.


### Parameters
  * factorIdRequiredString
System assigned identifier for authenticator device as returned by enroll
  * codeRequiredString
The verification code on the user's authenticator app


Create and verify a challenge for a factor
```

1
2
3
4
final res =await supabase.auth.mfa.challengeAndVerify( factorId:'34e770dd-9ff9-416c-87fa-43b31d7ef225', code:'123456',);

```

Response
## Unenroll a factor
Unenroll removes a MFA factor. A user has to have an `aal2` authenticator level in order to unenroll a `verified` factor.
### Parameters
  * factorIdRequiredString
System assigned identifier for authenticator device as returned by enroll


Unenroll a factor
```

1
2
3
final res =await supabase.auth.mfa.unenroll('34e770dd-9ff9-416c-87fa-43b31d7ef225',);

```

Response
## Get Authenticator Assurance Level
Returns the Authenticator Assurance Level (AAL) for the active session.
  * Authenticator Assurance Level (AAL) is the measure of the strength of an authentication mechanism.
  * In Supabase, having an AAL of `aal1` means the user has signed in with their first factor, such as email, password, or OAuth sign-in. An AAL of `aal2` means the user has also signed in with their second factor, such as a time-based, one-time-password (TOTP).
  * If the user has a verified factor, the `nextLevel` field returns `aal2`. Otherwise, it returns `aal1`.


Get the AAL details of a session
```

1
2
3
4
final res = supabase.auth.mfa.getAuthenticatorAssuranceLevel();final currentLevel = res.currentLevel;final nextLevel = res.nextLevel;final currentAuthenticationMethods = res.currentAuthenticationMethods;

```

Response
## Auth Admin
  * Any method under the `supabase.auth.admin` namespace requires a `service_role` key.
  * These methods are considered admin methods and should be called on a trusted server. Never expose your `service_role` key in the Flutter app.


Create server-side auth client
```

1
final supabase =SupabaseClient(supabaseUrl, serviceRoleKey);

```

## Retrieve a user
Get user by id.
  * Fetches the user object from the database based on the user's id.
  * The `getUserById()` method requires the user's id which maps to the `auth.users.id` column.


### Parameters
  * uidRequiredString
User ID of the user to fetch.


Fetch the user object using the access_token jwt
```

1
2
final res =await supabase.auth.admin.getUserById(userId);final user = res.user;

```

Response
## List all users
Get a list of users.
  * Defaults to return 50 users per page.


### Parameters
  * pageOptionalint
What page of users to return.
  * pageOptionalint
How many users to be returned per page. Defaults to 50.


Get a page of usersPaginated list of users
```

1
2
// Returns the first 50 users.finalList<User> users =await supabase.auth.admin.listUsers();

```

Response
## Create a user
Creates a new user.
  * To confirm the user's email address or phone number, set `email_confirm` or `phone_confirm` to true. Both arguments default to false.
  * `createUser()` will not send a confirmation email to the user. You can use [`inviteUserByEmail()`](https://supabase.com/docs/reference/dart/auth-admin-inviteuserbyemail) if you want to send them an email invite instead.
  * If you are sure that the created user's email or phone number is legitimate and verified, you can set the `email_confirm` or `phone_confirm` param to `true`.


### Parameters
  * attributesRequiredAdminUserAttributes
Attributes to create the user with.
Details


With custom user metadataAuto-confirm the user's emailAuto-confirm the user's phone number
```

1
2
3
4
5
final res =await supabase.auth.admin.createUser(AdminUserAttributes( email:'user@email.com', password:'password', userMetadata: {'name':'Yoda'},));

```

Response
## Delete a user
Delete a user.
  * The `deleteUser()` method requires the user's ID, which maps to the `auth.users.id` column.


### Parameters
  * idRequiredString
ID of the user to be deleted.


Removes a user
```

1
2
await supabase.auth.admin.deleteUser('715ed5db-f090-4b8c-a067-640ecee36aa0');

```

## Send an email invite link
Sends an invite link to the user's email address.
### Parameters
  * emailRequiredString
Email address of the user to invite.
  * redirectToOptionalString
URI to redirect the user to after they open the invite link.
  * dataOptionalMap<String, dynamic>
A custom data object to store the user's metadata. This maps to the `auth.users.user_metadata` column.


Invite a user
```

1
2
3
finalUserResponse res =await supabase.auth.admin.inviteUserByEmail('email@example.com');finalUser? user = res.user;

```

Response
## Generate an email link
Generates email links and OTPs to be sent via a custom email provider.
  * The following types can be passed into `generateLink()`: `signup`, `magiclink`, `invite`, `recovery`, `emailChangeCurrent`, `emailChangeNew`, `phoneChange`.
  * `generateLink()` only generates the email link for `email_change_email` if the "Secure email change" setting is enabled under the "Email" provider in your Supabase project.
  * `generateLink()` handles the creation of the user for `signup`, `invite` and `magiclink`.


### Parameters
  * typeRequiredGenerateLinkType
The type of invite link to generate.
  * emailRequiredString
Email address of the user to invite.
  * passwordOptionalString
Password for the user. Required for `signup` type.
  * redirectToOptionalString
URI to redirect the user to after they open the invite link.
  * dataOptionalMap<String, dynamic>
A custom data object to store the user's metadata. This maps to the `auth.users.user_metadata` column.


Generate a signup link
```

1
2
3
4
5
6
final res =await supabase.auth.admin.generateLink( type:GenerateLinkType.signup, email:'email@example.com', password:'secret',);final actionLink = res.properties.actionLink;

```

Response
## Update a user
### Parameters
  * uidRequiredGenerateLinkType
User ID of the user to update.
  * attributesRequiredAdminUserAttributes
Attributes to update for the user.
Details


Updates a user's email
```

1
2
3
4
5
6
await supabase.auth.admin.updateUserById('6aa5d0d4-2a9f-4483-b6c8-0cf4c6c98ac4', attributes:AdminUserAttributes(  email:'new@email.com', ),);

```

## Invokes a Supabase Edge Function.
Invokes a Supabase Function. See the [guide](https://supabase.com/docs/guides/functions) for details on writing Functions.
  * Requires an Authorization header.
  * Invoke params generally match the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) spec.


### Parameters
  * functionNameRequiredString
The name of the function to invoke.
  * headersOptionalMap<String, String>
Custom headers to send with the request.
  * bodyOptionalMap<String, String>
The body of the request.
  * methodOptionalHttpMethod
HTTP method of the request. Defaults to POST.


Basic invocation.Parsing custom headers.
```

1
2
final res =await supabase.functions.invoke('hello', body: {'foo':'baa'});final data = res.data;

```

## Listen to database changes
Returns real-time data from your table as a `Stream`.
  * Realtime is disabled by default for new tables. You can turn it on by [managing replication](https://supabase.com/docs/guides/realtime/postgres-changes#replication-setup).
  * `stream()` will emit the initial data as well as any further change on the database as `Stream<List<Map<String, dynamic>>>` by combining Postgrest and Realtime.
  * Takes a list of primary key column names that will be used to update and delete the proper records within the SDK.
  * The following filters are available 
    * `.eq('column', value)` listens to rows where the column equals the value
    * `.neq('column', value)` listens to rows where the column does not equal the value
    * `.gt('column', value)` listens to rows where the column is greater than the value
    * `.gte('column', value)` listens to rows where the column is greater than or equal to the value
    * `.lt('column', value)` listens to rows where the column is less than the value
    * `.lte('column', value)` listens to rows where the column is less than or equal to the value
    * `.inFilter('column', [val1, val2, val3])` listens to rows where the column is one of the values


Listen to a tableWith filter, order and limitWith an IN filterUsing `stream()` with `StreamBuilder`
```

1
2
3
4
5
supabase.from('countries').stream(primaryKey: ['id']).listen((List<Map<String, dynamic>> data) {// Do something awesome with the data});

```

## Subscribe to channel
Subscribe to realtime changes in your database.
  * Realtime is disabled by default for new tables. You can turn it on by [managing replication](https://supabase.com/docs/guides/realtime/postgres-changes#replication-setup).
  * If you want to receive the "previous" data for updates and deletes, you will need to set `REPLICA IDENTITY` to `FULL`, like this: `ALTER TABLE your_table REPLICA IDENTITY FULL;`


Listen to database changesListen to insertsListen to updatesListen to deletesListen to multiple eventsListen to row level changesListen to broadcast messagesListen to presence events
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
supabase.channel('public:countries').onPostgresChanges(    event:PostgresChangeEvent.all,    schema:'public',    table:'countries',    callback: (payload) {print('Change received: ${payload.toString()}');    }).subscribe();

```

## Unsubscribe from a channel
Unsubscribes and removes Realtime channel from Realtime client.
  * Removing a channel is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.


Remove a channel
```

1
final status =await supabase.removeChannel(channel);

```

## Unsubscribe from all channels
Unsubscribes and removes all Realtime channels from Realtime client.
  * Removing channels is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.


Remove all channels
```

1
final statuses =await supabase.removeAllChannels();

```

## Retrieve all channels
Returns all Realtime channels.
Get all channels
```

1
final channels = supabase.getChannels();

```

## Create a bucket
Creates a new Storage bucket
  * Policy permissions required: 
    * `buckets` permissions: `insert`
    * `objects` permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * idRequiredString
A unique identifier for the bucket you are creating.
  * bucketOptionsOptionalBucketOptions
A parameter to optionally make the bucket public.
Details


Create bucket
```

1
2
3
finalString bucketId =await supabase.storage.createBucket('avatars');

```

Response
## Retrieve a bucket
Retrieves the details of an existing Storage bucket.
  * Policy permissions required: 
    * `buckets` permissions: `select`
    * `objects` permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * idRequiredString
The unique identifier of the bucket you would like to retrieve.


Get bucket
```

1
2
3
finalBucket bucket =await supabase.storage.getBucket('avatars');

```

Response
## List all buckets
Retrieves the details of all Storage buckets within an existing product.
  * Policy permissions required: 
    * `buckets` permissions: `select`
    * `objects` permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


List buckets
```

1
2
3
finalList<Bucket> buckets =await supabase.storage.listBuckets();

```

Response
## Update a bucket
Updates a new Storage bucket
  * Policy permissions required: 
    * `buckets` permissions: `update`
    * `objects` permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * idRequiredString
A unique identifier for the bucket you are updating.
  * bucketOptionsRequiredBucketOptions
A parameter to optionally make the bucket public.
Details


Update bucket
```

1
2
3
finalString res =await supabase.storage.updateBucket('avatars',constBucketOptions(public:false));

```

Response
## Delete a bucket
Deletes an existing bucket. A bucket can't be deleted with existing objects inside it. You must first `empty()` the bucket.
  * Policy permissions required: 
    * `buckets` permissions: `select` and `delete`
    * `objects` permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * idRequiredString
A unique identifier for the bucket you are deleting.


Delete bucket
```

1
2
3
finalString res =await supabase.storage.deleteBucket('avatars');

```

Response
## Empty a bucket
Removes all objects inside a single bucket.
  * Policy permissions required: 
    * `buckets` permissions: `select`
    * `objects` permissions: `select` and `delete`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * idRequiredString
A unique identifier for the bucket you are emptying.


Empty bucket
```

1
2
3
finalString res =await supabase.storage.emptyBucket('avatars');

```

Response
## Upload a file
Uploads a file to an existing bucket.
  * Policy permissions required: 
    * `buckets` permissions: none
    * `objects` permissions: `insert`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The relative file path. Should be of the format folder/subfolder/filename.png. The bucket must already exist before attempting to update.
  * fileRequiredFile or Uint8List
File object to be stored in the bucket.
  * fileOptionsOptionalFileOptions
Details
  * retryAttemptsOptionalint
Sets the retryAttempts parameter set across the storage client. Defaults to 10.
  * retryControllerOptionalStorageRetryController
Pass a RetryController instance and call `cancel()` to cancel the retry attempts.


Upload fileUpload file on web
```

1
2
3
4
5
6
final avatarFile =File('path/to/file');finalString fullPath =await supabase.storage.from('avatars').upload('public/avatar1.png',   avatarFile,   fileOptions:constFileOptions(cacheControl:'3600', upsert:false),  );

```

Response
## Download a file
Downloads a file.
  * Policy permissions required: 
    * `buckets` permissions: none
    * `objects` permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The full path and file name of the file to be downloaded. For example folder/image.png.
  * transformOptionalTransformOptions
Transform the asset before serving it to the client.
Details


Download fileWith transform
```

1
2
3
4
finalUint8List file =await supabase.storage.from('avatars').download('avatar1.png');

```

Response
## List all files in a bucket
Lists all the files within a bucket.
  * Policy permissions required: 
    * `buckets` permissions: none
    * `objects` permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The folder path.
  * searchOptionsOptionalSearchOptions
Options for the search operations such as limit and offset.
Details


List files in a bucket
```

1
2
3
4
finalList<FileObject> objects =await supabase.storage.from('avatars').list();

```

Response
## Replace an existing file
Replaces an existing file at the specified path with a new one.
  * Policy permissions required: 
    * `buckets` permissions: none
    * `objects` permissions: `update` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The relative file path. Should be of the format folder/subfolder/filename.png. The bucket must already exist before attempting to update.
  * fileRequiredFile or Uint8List
File object to be stored in the bucket.
  * fileOptionsOptionalFileOptions
Details
  * retryAttemptsOptionalint
Sets the retryAttempts parameter set across the storage client. Defaults to 10.
  * retryControllerOptionalStorageRetryController
Pass a RetryController instance and call `cancel()` to cancel the retry attempts.


Update fileUpdate file on web
```

1
2
3
4
5
6
final avatarFile =File('path/to/local/file');finalString path =await supabase.storage.from('avatars').update('public/avatar1.png',   avatarFile,   fileOptions:constFileOptions(cacheControl:'3600', upsert:false),  );

```

Response
## Move an existing file
Moves an existing file, optionally renaming it at the same time.
  * Policy permissions required: 
    * `buckets` permissions: none
    * `objects` permissions: `update` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * fromPathRequiredString
The original file path, including the current file name. For example folder/image.png.
  * toPathRequiredString
The new file path, including the new file name. For example folder/image-new.png.


Move file
```

1
2
3
4
finalString result =await supabase.storage.from('avatars').move('public/avatar1.png','private/avatar2.png');

```

Response
## Delete files in a bucket
Deletes files within the same bucket
  * Policy permissions required: 
    * `buckets` permissions: none
    * `objects` permissions: `delete` and `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathsRequiredList<String>
A list of files to delete, including the path and file name. For example ['folder/image.png'].


Delete file
```

1
2
3
4
finalList<FileObject> objects =await supabase.storage.from('avatars').remove(['avatar1.png']);

```

Response
## Create a signed URL
Create signed url to download file without requiring permissions. This URL can be valid for a set number of seconds.
  * Policy permissions required: 
    * `buckets` permissions: none
    * `objects` permissions: `select`
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The file path, including the file name. For example folder/image.png.
  * expiresInRequiredint
The number of seconds until the signed URL expires. For example, 60 for a URL which is valid for one minute.
  * transformOptionalTransformOptions
Transform the asset before serving it to the client.
Details


Create Signed URLWith transform
```

1
2
3
4
finalString signedUrl =await supabase.storage.from('avatars').createSignedUrl('avatar1.png',60);

```

## Retrieve public URL
Retrieve URLs for assets in public buckets
  * The bucket needs to be set to public, either via [updateBucket()](https://supabase.com/docs/reference/dart/storage-updatebucket) or by going to Storage on [supabase.com/dashboard](https://supabase.com/dashboard), clicking the overflow menu on a bucket and choosing "Make public"
  * Policy permissions required: 
    * `buckets` permissions: none
    * `objects` permissions: none
  * Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works


### Parameters
  * pathRequiredString
The path and name of the file to generate the public URL for. For example folder/image.png.
  * transformOptionalTransformOptions
Transform the asset before serving it to the client.
Details


Returns the URL for an asset in a public bucketWith transform
```

1
2
3
4
finalString publicUrl = supabase.storage.from('public-bucket').getPublicUrl('avatar1.png');

```

Response
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



