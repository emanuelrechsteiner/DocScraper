---
url: https://supabase.com/blog/offline-first-flutter-apps
scraped_at: 2025-05-25T08:45:05.571210
title: Building offline-first mobile apps with Supabase, Flutter and Brick
---

  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
  * Product 
  * Developers 
  * [Enterprise](https://supabase.com/enterprise)
  * [Pricing](https://supabase.com/pricing)
  * [Docs](https://supabase.com/docs)
  * [Blog](https://supabase.com/blog)


[83.3K](https://github.com/supabase/supabase)[Sign in](https://supabase.com/dashboard)[Start your project](https://supabase.com/dashboard)
Open main menu
[Back](https://supabase.com/blog)
[Blog](https://supabase.com/blog)
# Building offline-first mobile apps with Supabase, Flutter and Brick
08 Oct 2024
•
9 minute read
[![Tim Shedor avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ftshedor.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Tim ShedorGuest Author](https://github.com/tshedor)
[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Tyler ShukertDevRel](https://twitter.com/dshukertjr)
![Building offline-first mobile apps with Supabase, Flutter and Brick](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-offline-first%2Fflutter-offline-first.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Don’t have time for reading? Skip to [the example](https://github.com/GetDutchie/brick/tree/main/example_supabase).
Brick is an [all-in-one](https://www.youtube.com/watch?v=2noLcro9iIw) data manager for Flutter that handles querying and uploading between Supabase and local caches like SQLite. Using Brick, developers can focus on implementing the application without [worrying about translating or storing their data](https://www.youtube.com/watch?v=jm5i7e_BQq0).
Most significantly, Brick focuses on offline-first data parity: an app should function the same with or without connectivity.
### Why Offline?[#](https://supabase.com/blog/offline-first-flutter-apps#why-offline)
The worst version of your app is always the unusable one. People use their phones on subways, airplanes, and on sub-3G connections. Building for offline-first provides the best user experience when you can’t guarantee steady bandwidth.
Even if you’re online-only, Brick’s round trip time is drastically shorter because all data [from Supabase is stored in a local cache](https://getdutchie.github.io/brick/#/offline_first/offline_first_with_supabase_repository). When you query the same data again, your app retrieves the local copy, reducing the time and expense of a round trip. And, if SQLite isn’t performant enough, Brick also offers a third cache in memory. When requests are made while the app is offline, they’ll be [continually retried until the app comes online](https://getdutchie.github.io/brick/#/offline_first/offline_queue), ensuring that your local state syncs up to your remote state.
Of course, you can [always opt-out of the cache](https://getdutchie.github.io/brick/#/offline_first/policies) on a request-by-request basis for sensitive or must-be-fresh data.
### Getting Started[#](https://supabase.com/blog/offline-first-flutter-apps#getting-started)
Create a Flutter app:
`
1
flutter create my_app
`
Add the Brick dependencies to your `pubspec.yaml`:
`
1
dependencies:
2
 brick_offline_first_with_supabase: ^1.0.0
3
 sqflite: ^2.3.0
4
 brick_sqlite: ^3.1.0
5
 uuid: ^3.0.4
67
dev_dependencies:
8
 brick_offline_first_with_supabase_build: ^1.0.0
9
 build_runner: ^2.4.0
`
Set up directories for Brick’s generated code:
`
1
mkdir -p lib/brick/adapters lib/brick/db;
`
Brick synthesizes your remote data to your local data through code generation. From a Supabase table, create Dart fields that match the table’s columns:
`
1
// Your model definition can live anywhere in lib/**/* as long as it has the .model.dart suffix
2
// Assume this file is saved at my_app/lib/src/users/user.model.dart
34
import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
5
import 'package:brick_sqlite/brick_sqlite.dart';
6
import 'package:brick_supabase/brick_supabase.dart';
7
import 'package:uuid/uuid.dart';
89
@ConnectOfflineFirstWithSupabase(
10
 supabaseConfig: SupabaseSerializable(tableName: 'users'),
11
)
12
class User extends OfflineFirstWithSupabaseModel {
13
 final String name;
1415
 // Be sure to specify an index that **is not** auto incremented in your table.
16
 // An offline-first strategy requires distributed clients to create
17
 // indexes without fear of collision.
18
 @Supabase(unique: true)
19
 @Sqlite(index: true, unique: true)
20
 final String id;
2122
 User({
23
  String? id,
24
  required this.name,
25
 }) : this.id = id ?? const Uuid().v4();
26
}
`
When some (or all) of your models have been defined, generate the code:
`
1
dart run build_runner build
`
This will generate adapters to serialize/deserialize to and from Supabase. Migrations for SQLite are also generated for any new, dropped, or changed columns. Check these migrations after they are generated - Brick is smart, but not as smart as you.
After every model change, run this command to ensure your adapters will serialize/deserialize the way they need to.
### The Repository[#](https://supabase.com/blog/offline-first-flutter-apps#the-repository)
Your application does not need to touch SQLite or Supabase directly. By [interacting with this single entrypoint](https://getdutchie.github.io/brick/#/data), Brick makes the hard choices under the hood about where to fetch and when to cache while the application code remains consistent in online or offline modes.
Finally, run your app:
`
1
// Saved in my_app/lib/src/brick/repository.dart
2
import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
3
import 'package:brick_sqlite/brick_sqlite.dart';
4
// This hide is for Brick's @Supabase annotation; in most cases,
5
// supabase_flutter **will not** be imported in application code.
6
import 'package:brick_supabase/brick_supabase.dart' hide Supabase;
7
import 'package:sqflite_common/sqlite_api.dart';
8
import 'package:supabase_flutter/supabase_flutter.dart';
910
import 'brick.g.dart';
1112
class Repository extends OfflineFirstWithSupabaseRepository {
13
 static late Repository? _instance;
1415
 Repository._({
16
  required super.supabaseProvider,
17
  required super.sqliteProvider,
18
  required super.migrations,
19
  required super.offlineRequestQueue,
20
  super.memoryCacheProvider,
21
 });
2223
 factory Repository() => _instance!;
2425
 static Future<void> configure(DatabaseFactory databaseFactory) async {
26
  final (client, queue) = OfflineFirstWithSupabaseRepository.clientQueue(
27
   databaseFactory: databaseFactory,
28
  );
2930
  await Supabase.initialize(
31
   url: supabaseUrl,
32
   anonKey: supabaseAnonKey,
33
   httpClient: client,
34
  );
3536
  final provider = SupabaseProvider(
37
   Supabase.instance.client,
38
   modelDictionary: supabaseModelDictionary,
39
  );
4041
  _instance = Repository._(
42
   supabaseProvider: provider,
43
   sqliteProvider: SqliteProvider(
44
    'my_repository.sqlite',
45
    databaseFactory: databaseFactory,
46
    modelDictionary: sqliteModelDictionary,
47
   ),
48
   migrations: migrations,
49
   offlineRequestQueue: queue,
50
   // Specify class types that should be cached in memory
51
   memoryCacheProvider: MemoryCacheProvider(),
52
  );
53
 }
54
}
`
`
1
import 'package:my_app/brick/repository.dart';
2
import 'package:sqflite/sqflite.dart' show databaseFactory;
34
Future<void> main() async {
5
 await Repository.configure(databaseFactory);
6
 // .initialize() does not need to be invoked within main()
7
 // It can be invoked from within a state manager or within
8
 // an initState()
9
 await Repository().initialize();
10
 runApp(MyApp());
11
}
`
Which `databaseFactory` is used depends on your platform. For unit testing, use `import 'package:sqflite_common_ffi/sqflite_ffi.dart' show databaseFactory`. Please see SQFlite’s docs for specific installation and usage instructions on [web](https://github.com/tekartik/sqflite/tree/master/packages_web/sqflite_common_ffi_web#use-the-proper-factory), [Linux](https://github.com/tekartik/sqflite/tree/master/sqflite_common_ffi#linux), or [Windows](https://github.com/tekartik/sqflite/tree/master/sqflite_common_ffi#windows).
## Usage[#](https://supabase.com/blog/offline-first-flutter-apps#usage)
The fun part. [Brick’s DSL queries](https://getdutchie.github.io/brick/#/supabase/query) are written once and transformed for local and remote integration. For example, to retrieve all users with the name “Thomas”:
`
1
await Repository().get<User>(query: Query.where('name', 'Thomas'));
`
Or query by association:
`
1
// Assuming we had a model `Order` with a `user` association
2
await Repository().get<Order>(query: Query.where('user', Where.exact('name', 'Thomas'));
`
Queries can be [much more advanced](https://getdutchie.github.io/brick/#/data/query), leveraging `contains`, `not`, `like` operators as well as sub clauses. Please note that, as of writing, not [all Supabase operators are supported](https://getdutchie.github.io/brick/#/supabase/query?id=where).
**Reactivity**
Beyond async requests, you can subscribe to a stream of updated local data from anywhere in your app (for example, if you pull-to-refresh a list of users, all listeners will be notified of the new data):
`
1
final Stream<List<User>> usersStream = Repository().subscribe<User>(query: Query.where('name', 'Thomas'));
`
This **does not** leverage Supabase’s channels by default; if Supabase updates, your app will not be notified. This opt-in feature is [currently under active development](https://github.com/GetDutchie/brick/issues/454).
**Upserting**
After a model has been created, it can uploaded to Supabase without serializing it to JSON first:
`
1
await Repository().upsert<User>(User(name: 'Thomas'));
`
All attached associations [will be upserted too](https://getdutchie.github.io/brick/#/supabase/models?id=upsert-behavior).
## Other Tips[#](https://supabase.com/blog/offline-first-flutter-apps#other-tips)
### Foreign Keys/Associations[#](https://supabase.com/blog/offline-first-flutter-apps#foreign-keysassociations)
Easily connect related models/tables:
`
1
import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
2
import 'package:brick_sqlite/brick_sqlite.dart';
3
import 'package:brick_supabase/brick_supabase.dart';
4
import 'package:my_app/lib/src/users/user.model.dart';
5
import 'package:uuid/uuid.dart';
67
@ConnectOfflineFirstWithSupabase(
8
 supabaseConfig: SupabaseSerializable(tableName: 'orders'),
9
)
10
class Order extends OfflineFirstWithSupabaseModel {
11
 // Like Supabase's client, specifying a foreign_key
12
 // is possible but only necessary if there are joins
13
 // with multiple foreign keys
14
 // @Supabase(foreignKey: 'user_id')
15
 final User user;
1617
 @Supabase(unique: true)
18
 @Sqlite(index: true, unique: true)
19
 final String id;
2021
 Order({
22
  String? id,
23
  required this.user,
24
 }) : this.id = id ?? const Uuid().v4();
25
}
`
Brick allows very granular [model configuration](https://getdutchie.github.io/brick/#/supabase/models) - you can specify specific tables, [individual columns](https://getdutchie.github.io/brick/#/supabase/fields), and more.
### Testing[#](https://supabase.com/blog/offline-first-flutter-apps#testing)
Quickly mock your Supabase endpoints to add uncluttered [unit testing](https://getdutchie.github.io/brick/#/supabase/testing?id=testing):
`
1
import 'package:brick_supabase/testing.dart';
2
import 'package:test/test.dart'
34
void main() {
5
 // Pass an instance of your model dictionary to the mock server.
6
 // This permits quick generation of fields and generated responses
7
 final mock = SupabaseMockServer(modelDictionary: supabaseModelDictionary);
89
 group('MyClass', () {
10
  setUp(mock.setUp);
1112
  tearDown(mock.tearDown);
1314
  test('#myMethod', () async {
15
   // If your request won't exactly match the columns of MyModel, provide
16
   // the query list to the `fields:` parameter
17
   final req = SupabaseRequest<MyModel>();
18
   final resp = SupabaseResponse([
19
    // mock.serialize converts models to expected Supabase payloads
20
    // but you don't need to use it - any jsonEncode-able object
21
    // can be passed to SupabaseRepsonse
22
    await mock.serialize(MyModel(name: 'Demo 1', id: '1')),
23
    await mock.serialize(MyModel(name: 'Demo 2', id: '2')),
24
   ]);
25
   // This method stubs the server based on the described requests
26
   // and their matched responses
27
   mock.handle({req: resp});
28
   final provider = SupabaseProvider(mock.client, modelDictionary: supabaseModelDictionary);
29
   final retrieved = await provider.get<MyModel>();
30
   expect(retrieved, hasLength(2));
31
  });
32
 });
33
}
`
## Further Reading[#](https://supabase.com/blog/offline-first-flutter-apps#further-reading)
Brick manages a lot. It can be overwhelming at times. But it’s been used in production across thousands of devices for more than five years, so it’s got a sturdy CV. There’s likely an existing solution to a seemingly novel problem. Please [reach out to the community or package maintainers](https://github.com/GetDutchie/brick/issues) with any questions.
  * Example: [Brick with Supabase](https://github.com/GetDutchie/brick/tree/main/example_supabase)
  * Video: [**Brick Architecture**](https://www.youtube.com/watch?v=2noLcro9iIw). An explanation of Brick parlance with [a supplemental analogy](https://medium.com/flutter-community/brick-your-app-five-compelling-reasons-and-a-pizza-analogy-to-make-your-data-accessible-8d802e1e526e).
  * Video: [**Brick Basics**](https://www.youtube.com/watch?v=jm5i7e_BQq0). An overview of essential Brick mechanics.
  * [Build a User Management App with Flutter](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&text=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&text=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&t=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)
[Last postMongoDB Realm & Device Sync Alternatives - Supabase9 October 2024](https://supabase.com/blog/mongodb-realm-and-device-sync-alternatives)
[Next postSupabase Launch Week 12 Hackathon Winners30 September 2024](https://supabase.com/blog/lw12-hackathon-winners)
[mobile](https://supabase.com/blog/tags/mobile)[local-first](https://supabase.com/blog/tags/local-first)[flutter](https://supabase.com/blog/tags/flutter)
On this page
  * [Usage](https://supabase.com/blog/offline-first-flutter-apps#usage)
  * [Other Tips](https://supabase.com/blog/offline-first-flutter-apps#other-tips)
  * [Further Reading](https://supabase.com/blog/offline-first-flutter-apps#further-reading)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&text=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&text=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&t=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)
## Build in a weekend, scale to millions
[Start your project](https://supabase.com/dashboard)[Request a demo](https://supabase.com/contact/sales)
## Footer
We protect your data.[More on Security](https://supabase.com/security)
  * SOC2 Type 2 Certified
  * HIPAA Compliant


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)
###### Product
  * [Database](https://supabase.com/database)
  * [Auth](https://supabase.com/auth)
  * [Functions](https://supabase.com/edge-functions)
  * [Realtime](https://supabase.com/realtime)
  * [Storage](https://supabase.com/storage)
  * [Vector](https://supabase.com/modules/vector)
  * [Cron](https://supabase.com/modules/cron)
  * [Pricing](https://supabase.com/pricing)
  * [Launch Week](https://supabase.com/launch-week)
  * [AI Builders](https://supabase.com/solutions/ai-builders)


###### Resources
  * [Support](https://supabase.com/support)
  * [System Status](https://status.supabase.com/)
  * [Become a Partner](https://supabase.com/partners)
  * [Integrations](https://supabase.com/partners/integrations)
  * [Brand Assets / Logos](https://supabase.com/brand-assets)
  * [Security and Compliance](https://supabase.com/security)
  * [DPA](https://supabase.com/legal/dpa)
  * [SOC2](https://supabase.com/security)
  * [HIPAA](https://forms.supabase.com/hipaa2)


###### Developers
  * [Documentation](https://supabase.com/docs)
  * [Supabase UI](https://supabase.com/ui)
  * [Changelog](https://supabase.com/changelog)
  * [Contributing](https://github.com/supabase/supabase/blob/master/CONTRIBUTING.md)
  * [Open Source](https://supabase.com/open-source)
  * [SupaSquad](https://supabase.com/supasquad)
  * [DevTo](https://dev.to/supabase)
  * [RSS](https://supabase.com/rss.xml)


###### Company
  * [Blog](https://supabase.com/blog)
  * [Customer Stories](https://supabase.com/customers)
  * [Careers](https://supabase.com/careers)
  * [Company](https://supabase.com/company)
  * [Events & Webinars](https://supabase.com/events)
  * [General Availability](https://supabase.com/ga)
  * [Terms of Service](https://supabase.com/terms)
  * [Privacy Policy](https://supabase.com/privacy)
  * Privacy Settings
  * [Acceptable Use Policy](https://supabase.com/aup)
  * [Support Policy](https://supabase.com/support-policy)
  * [Service Level Agreement](https://supabase.com/sla)
  * [Humans.txt](https://supabase.com/humans.txt)
  * [Lawyers.txt](https://supabase.com/lawyers.txt)
  * [Security.txt](https://supabase.com/.well-known/security.txt)


© Supabase Inc
Toggle theme

