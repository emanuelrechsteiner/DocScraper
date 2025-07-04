---
url: http://supabase.com/docs/guides/getting-started/quickstarts/kotlin
scraped_at: 2025-05-25T09:33:08.669411
title: Use Supabase with Android Kotlin | Supabase Docs
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
  2. Framework Quickstarts
  3. [Android Kotlin](https://supabase.com/docs/guides/getting-started/quickstarts/kotlin)


Use Supabase with Android Kotlin
Learn how to create a Supabase project, add some sample data to your database, and query the data from an Android Kotlin app.
1
### Create a Supabase project
Go to [database.new](https://database.new) and create a new Supabase project.
When your project is up and running, go to the [Table Editor](https://supabase.com/dashboard/project/_/editor), create a new table and insert some data.
Alternatively, you can run the following snippet in your project's [SQL Editor](https://supabase.com/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
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
-- Create the tablecreatetableinstruments ( id bigintprimary keygeneratedalwaysasidentity,nametextnot null);-- Insert some sample data into the tableinsert into instruments (name)values ('violin'), ('viola'), ('cello');altertable instruments enablerowlevelsecurity;

```

Make the data in your table publicly readable by adding an RLS policy:
```

1
2
3
4
createpolicy"public can read instruments"onpublic.instrumentsforselectto anonusing (true);

```

2
### Create an Android app with Android Studio
Open Android Studio > New > New Android Project.
3
### Install the Dependencies
Open `build.gradle.kts` (app) file and add the serialization plug, Ktor client, and Supabase client.
Replace the version placeholders `$kotlin_version` with the Kotlin version of the project, and `$supabase_version` and `$ktor_version` with the respective latest versions.
The latest supabase-kt version can be found [here](https://github.com/supabase-community/supabase-kt/releases) and Ktor version can be found [here](https://ktor.io/docs/welcome.html).
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
plugins {...kotlin("plugin.serialization") version "$kotlin_version"}...dependencies {...implementation(platform("io.github.jan-tennert.supabase:bom:$supabase_version"))implementation("io.github.jan-tennert.supabase:postgrest-kt")implementation("io.ktor:ktor-client-android:$ktor_version")}

```

4
### Add internet access permission
Add the following line to the `AndroidManifest.xml` file under the `manifest` tag and outside the `application` tag.
```

1
2
3
...<uses-permission android:name="android.permission.INTERNET"/>...

```

5
### Initialize the Supabase client
You can create a Supabase client whenever you need to perform an API call.
For the sake of simplicity, we will create a client in the `MainActivity.kt` file at the top just below the imports.
Replace the `supabaseUrl` and `supabaseKey` with your own:
###### Project URL
No project found
To get your Project URL, [log in](https://supabase.com/dashboard).
###### Anon key
No project found
To get your Anon key, [log in](https://supabase.com/dashboard).
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
import...val supabase =createSupabaseClient(  supabaseUrl ="https://xyzcompany.supabase.co",  supabaseKey ="your_public_anon_key" ) {install(Postgrest)}...

```

6
### Create a data model for instruments
Create a serializable data class to represent the data from the database.
Add the following below the `createSupabaseClient` function in the `MainActivity.kt` file.
```

1
2
3
4
5
@SerializabledataclassInstrument(val id: Int,val name: String,)

```

7
### Query data from the app
Use `LaunchedEffect` to fetch data from the database and display it in a `LazyColumn`.
Replace the default `MainActivity` class with the following code.
Note that we are making a network request from our UI code. In production, you should probably use a `ViewModel` to separate the UI and data fetching logic.
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
classMainActivity : ComponentActivity() {overridefunonCreate(savedInstanceState: Bundle?) {super.onCreate(savedInstanceState)setContent {SupabaseTutorialTheme {// A surface container using the 'background' color from the themeSurface(          modifier = Modifier.fillMaxSize(),          color = MaterialTheme.colorScheme.background        ) {InstrumentsList()        }      }    }  }}@ComposablefunInstrumentsList() {var instruments byremember { mutableStateOf<List<Instrument>>(listOf()) }LaunchedEffect(Unit) {withContext(Dispatchers.IO) {      instruments = supabase.from("instruments")               .select().decodeList<Instrument>()    }  }LazyColumn {items(      instruments,      key = { instrument -> instrument.id },    ) { instrument ->Text(        instrument.name,        modifier = Modifier.padding(8.dp),      )    }  }}

```

8
### Start the app
Run the app on an emulator or a physical device by clicking the `Run app` button in Android Studio.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/quickstarts/kotlin.mdx)
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



