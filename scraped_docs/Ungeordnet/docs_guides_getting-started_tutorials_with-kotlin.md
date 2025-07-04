---
url: http://supabase.com/docs/guides/getting-started/tutorials/with-kotlin
scraped_at: 2025-05-25T09:04:00.303587
title: Build a Product Management Android App with Jetpack Compose | Supabase Docs
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
  3. [Android Kotlin](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin)


Build a Product Management Android App with Jetpack Compose
This tutorial demonstrates how to build a basic product management app. The app demonstrates management operations, photo upload, account creation and authentication using:
  * [Supabase Database](https://supabase.com/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](https://supabase.com/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
  * [Supabase Auth](https://supabase.com/docs/guides/auth) - users log in through magic links sent to their email (without having to set up a password).
  * [Supabase Storage](https://supabase.com/docs/guides/storage) - users can upload a profile photo.


![manage-product-cover](https://supabase.com/docs/img/guides/kotlin/manage-product-cover.png)
If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/hieuwu/product-sample-supabase-kt).
## Project setup[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#project-setup)
Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.
### Create a project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-a-project)
  1. [Create a new project](https://app.supabase.com) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


### Set up the database schema[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-the-database-schema)
Now we are going to set up the database schema. You can just copy/paste the SQL from below and run it yourself.
SQL
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
-- Create a table for public profilescreatetablepublic.products (  id uuid not nulldefault gen_random_uuid (),nametextnot null,  price realnot null,imagetextnull,constraint products_pkey primary key (id) ) tablespace pg_default;-- Set up Storage!insert intostorage.buckets (id, name)values ('Product Image', 'Product Image');-- Set up access controls for storage.-- See https://supabase.com/docs/guides/storage/security/access-control#policy-examples for more details.CREATEPOLICY"Enable read access for all users"ON"storage"."objects"AS PERMISSIVE FORSELECTTO publicUSING (true)CREATEPOLICY"Enable insert for all users"ON"storage"."objects"AS PERMISSIVE FORINSERTTO authenticated, anonWITHCHECK (true)CREATEPOLICY"Enable update for all users"ON"storage"."objects"AS PERMISSIVE FORUPDATETO publicUSING (true)WITHCHECK (true)

```

### Get the API keys[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#get-the-api-keys)
Now that you've created some database tables, you are ready to insert data using the auto-generated API. We just need to get the Project URL and `anon` key from the API settings.
  1. Go to the [API Settings](https://app.supabase.com/project/_/settings/api) page in the Dashboard.
  2. Find your Project `URL`, `anon`, and `service_role` keys on this page.


### Set up Google authentication[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-google-authentication)
From the [Google Console](https://console.developers.google.com/apis/library), create a new project and add OAuth2 credentials.
![Create Google OAuth credentials](https://supabase.com/docs/img/guides/kotlin/google-cloud-oauth-credentials-create.png)
In your [Supabase Auth settings](https://app.supabase.com/project/_/auth/providers) enable Google as a provider and set the required credentials as outlined in the [auth docs](https://supabase.com/docs/guides/auth/social-login/auth-google).
## Building the app[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#building-the-app)
### Create new Android project[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-new-android-project)
Open Android Studio > New Project > Base Activity (Jetpack Compose).
![Android Studio new project](https://supabase.com/docs/img/guides/kotlin/android-studio-new-project.png)
### Set up API key and secret securely[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-api-key-and-secret-securely)
#### Create local environment secret[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-local-environment-secret)
Create or edit the `local.properties` file at the root (same level as `build.gradle`) of your project.
> **Note** : Do not commit this file to your source control, for example, by adding it to your `.gitignore` file!
```

1
2
SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEYSUPABASE_URL=YOUR_SUPABASE_URL

```

#### Read and set value to `BuildConfig`[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#read-and-set-value-to-buildconfig)
In your `build.gradle` (app) file, create a `Properties` object and read the values from your `local.properties` file by calling the `buildConfigField` method:
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
defaultConfig {  applicationId "com.example.manageproducts"  minSdkVersion 22  targetSdkVersion 33  versionCode 5  versionName "1.0"  testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"// Set value part  Properties properties = new Properties()  properties.load(project.rootProject.file("local.properties").newDataInputStream())buildConfigField("String", "SUPABASE_ANON_KEY", "\"${properties.getProperty("SUPABASE_ANON_KEY")}\"")buildConfigField("String", "SECRET", "\"${properties.getProperty("SECRET")}\"")buildConfigField("String", "SUPABASE_URL", "\"${properties.getProperty("SUPABASE_URL")}\"")}

```

#### Use value from `BuildConfig`[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#use-value-from-buildconfig)
Read the value from `BuildConfig`:
```

1
2
val url = BuildConfig.SUPABASE_URLval apiKey = BuildConfig.SUPABASE_ANON_KEY

```

### Set up Supabase dependencies[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-supabase-dependencies)
![Gradle dependencies](https://supabase.com/docs/img/guides/kotlin/gradle-dependencies.png)
In the `build.gradle` (app) file, add these dependencies then press "Sync now." Replace the dependency version placeholders `$supabase_version` and `$ktor_version` with their respective latest versions.
```

1
2
3
4
5
6
implementation "io.github.jan-tennert.supabase:postgrest-kt:$supabase_version"implementation "io.github.jan-tennert.supabase:storage-kt:$supabase_version"implementation "io.github.jan-tennert.supabase:auth-kt:$supabase_version"implementation "io.ktor:ktor-client-android:$ktor_version"implementation "io.ktor:ktor-client-core:$ktor_version"implementation "io.ktor:ktor-utils:$ktor_version"

```

Also in the `build.gradle` (app) file, add the plugin for serialization. The version of this plugin should be the same as your Kotlin version.
```

1
2
3
4
5
plugins {...  id 'org.jetbrains.kotlin.plugin.serialization' version '$kotlin_version'...}

```

### Set up Hilt for dependency injection[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-hilt-for-dependency-injection)
In the `build.gradle` (app) file, add the following:
```

1
2
3
implementation "com.google.dagger:hilt-android:$hilt_version"annotationProcessor "com.google.dagger:hilt-compiler:$hilt_version"implementation("androidx.hilt:hilt-navigation-compose:1.0.0")

```

Create a new `ManageProductApplication.kt` class extending Application with `@HiltAndroidApp` annotation:
```

1
2
3
// ManageProductApplication.kt@HiltAndroidAppclassManageProductApplication: Application()

```

Open the `AndroidManifest.xml` file, update name property of Application tag:
```

1
2
3
4
5
<application...android:name=".ManageProductApplication"...</application>

```

Create the `MainActivity`:
```

1
2
3
4
@AndroidEntryPointclassMainActivity : ComponentActivity() {//This will come later}

```

### Provide Supabase instances with Hilt[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#provide-supabase-instances-with-hilt)
To make the app easier to test, create a `SupabaseModule.kt` file as follows:
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
@InstallIn(SingletonComponent::class)@ModuleobjectSupabaseModule {@Provides@SingletonfunprovideSupabaseClient(): SupabaseClient {returncreateSupabaseClient(      supabaseUrl = BuildConfig.SUPABASE_URL,      supabaseKey = BuildConfig.SUPABASE_ANON_KEY    ) {install(Postgrest)install(Auth) {        flowType = FlowType.PKCE        scheme ="app"        host ="supabase.com"      }install(Storage)    }  }@Provides@SingletonfunprovideSupabaseDatabase(client: SupabaseClient): Postgrest {return client.postgrest  }@Provides@SingletonfunprovideSupabaseAuth(client: SupabaseClient): Auth {return client.auth  }@Provides@SingletonfunprovideSupabaseStorage(client: SupabaseClient): Storage {return client.storage  }}

```

### Create a data transfer object[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-a-data-transfer-object)
Create a `ProductDto.kt` class and use annotations to parse data from Supabase:
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
@SerializabledataclassProductDto(@SerialName("name")val name: String,@SerialName("price")val price: Double,@SerialName("image")val image: String?,@SerialName("id")val id: String,)

```

Create a Domain object in `Product.kt` expose the data in your view:
```

1
2
3
4
5
6
dataclassProduct(val id: String,val name: String,val price: Double,val image: String?)

```

### Implement repositories[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#implement-repositories)
Create a `ProductRepository` interface and its implementation named `ProductRepositoryImpl`. This holds the logic to interact with data sources from Supabase. Do the same with the `AuthenticationRepository`.
Create the Product Repository:
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
interfaceProductRepository {suspendfuncreateProduct(product: Product): BooleansuspendfungetProducts(): List<ProductDto>?suspendfungetProduct(id: String): ProductDtosuspendfundeleteProduct(id: String)suspendfunupdateProduct(    id: String, name: String, price: Double, imageName: String, imageFile: ByteArray  )}

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
classProductRepositoryImpl@Injectconstructor(privateval postgrest: Postgrest,privateval storage: Storage,) : ProductRepository {overridesuspendfuncreateProduct(product: Product): Boolean {returntry {withContext(Dispatchers.IO) {val productDto =ProductDto(          name = product.name,          price = product.price,        )        postgrest.from("products").insert(productDto)true      }true    } catch (e: java.lang.Exception) {throw e    }  }overridesuspendfungetProducts(): List<ProductDto>? {returnwithContext(Dispatchers.IO) {val result = postgrest.from("products")        .select().decodeList<ProductDto>()      result    }  }overridesuspendfungetProduct(id: String): ProductDto {returnwithContext(Dispatchers.IO) {      postgrest.from("products").select {filter {eq("id", id)        }      }.decodeSingle<ProductDto>()    }  }overridesuspendfundeleteProduct(id: String) {returnwithContext(Dispatchers.IO) {      postgrest.from("products").delete {filter {eq("id", id)        }      }    }  }overridesuspendfunupdateProduct(    id: String,    name: String,    price: Double,    imageName: String,    imageFile: ByteArray  ) {withContext(Dispatchers.IO) {if (imageFile.isNotEmpty()) {val imageUrl =          storage.from("Product%20Image").upload(            path ="$imageName.png",data= imageFile,            upsert =true          )        postgrest.from("products").update({set("name", name)set("price", price)set("image", buildImageUrl(imageFileName = imageUrl))        }) {filter {eq("id", id)          }        }      } else {        postgrest.from("products").update({set("name", name)set("price", price)        }) {filter {eq("id", id)          }        }      }    }  }// Because I named the bucket as "Product Image" so when it turns to an url, it is "%20"// For better approach, you should create your bucket name without space symbolprivatefunbuildImageUrl(imageFileName: String) ="${BuildConfig.SUPABASE_URL}/storage/v1/object/public/${imageFileName}".replace(" ", "%20")}

```

Create the Authentication Repository:
```

1
2
3
4
5
interfaceAuthenticationRepository {suspendfunsignIn(email: String, password: String): BooleansuspendfunsignUp(email: String, password: String): BooleansuspendfunsignInWithGoogle(): Boolean}

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
classAuthenticationRepositoryImpl@Injectconstructor(privateval auth: Auth) : AuthenticationRepository {overridesuspendfunsignIn(email: String, password: String): Boolean {returntry {      auth.signInWith(Email) {this.email = emailthis.password = password      }true    } catch (e: Exception) {false    }  }overridesuspendfunsignUp(email: String, password: String): Boolean {returntry {      auth.signUpWith(Email) {this.email = emailthis.password = password      }true    } catch (e: Exception) {false    }  }overridesuspendfunsignInWithGoogle(): Boolean {returntry {      auth.signInWith(Google)true    } catch (e: Exception) {false    }  }}

```

### Implement screens[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#implement-screens)
To navigate screens, use the AndroidX navigation library. For routes, implement a `Destination` interface:
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
interfaceDestination {val route: Stringval title: String}objectProductListDestination : Destination {overrideval route ="product_list"overrideval title ="Product List"}objectProductDetailsDestination : Destination {overrideval route ="product_details"overrideval title ="Product Details"constval productId ="product_id"val arguments =listOf(navArgument(name = productId) {    type = NavType.StringType  })funcreateRouteWithParam(productId: String) ="$route/${productId}"}objectAddProductDestination : Destination {overrideval route ="add_product"overrideval title ="Add Product"}objectAuthenticationDestination: Destination {overrideval route ="authentication"overrideval title ="Authentication"}objectSignUpDestination: Destination {overrideval route ="signup"overrideval title ="Sign Up"}

```

This will help later for navigating between screens.
Create a `ProductListViewModel`:
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
@HiltViewModelclassProductListViewModel@Injectconstructor(privateval productRepository: ProductRepository,) : ViewModel() {privateval _productList =MutableStateFlow<List<Product>?>(listOf())val productList: Flow<List<Product>?> = _productListprivateval _isLoading =MutableStateFlow(false)val isLoading: Flow<Boolean> = _isLoadinginit {getProducts()  }fungetProducts() {    viewModelScope.launch {val products = productRepository.getProducts()      _productList.emit(products?.map { it -> it.asDomainModel() })    }  }funremoveItem(product: Product) {    viewModelScope.launch {val newList =mutableListOf<Product>().apply { _productList.value?.let { addAll(it) } }      newList.remove(product)      _productList.emit(newList.toList())// Call api to remove      productRepository.deleteProduct(id = product.id)// Then fetch againgetProducts()    }  }privatefunProductDto.asDomainModel(): Product {returnProduct(      id =this.id,      name =this.name,      price =this.price,      image =this.image    )  }}

```

Create the `ProductListScreen.kt`:
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
@OptIn(ExperimentalMaterial3Api::class, ExperimentalMaterialApi::class)@ComposablefunProductListScreen(  modifier: Modifier= Modifier,  navController: NavController,  viewModel: ProductListViewModel=hiltViewModel(),) {val isLoading by viewModel.isLoading.collectAsState(initial =false)val swipeRefreshState =rememberSwipeRefreshState(isRefreshing = isLoading)SwipeRefresh(state = swipeRefreshState, onRefresh = { viewModel.getProducts() }) {Scaffold(      topBar = {TopAppBar(          backgroundColor = MaterialTheme.colorScheme.primary,          title = {Text(              text =stringResource(R.string.product_list_text_screen_title),              color = MaterialTheme.colorScheme.onPrimary,            )          },        )      },      floatingActionButton = {AddProductButton(onClick = { navController.navigate(AddProductDestination.route) })      }    ) { padding ->val productList = viewModel.productList.collectAsState(initial =listOf()).valueif (!productList.isNullOrEmpty()) {LazyColumn(          modifier = modifier.padding(padding),          contentPadding =PaddingValues(5.dp)        ) {itemsIndexed(            items = productList,            key = { _, product -> product.name }) { _, item ->val state =rememberDismissState(              confirmStateChange = {if (it == DismissValue.DismissedToStart) {// Handle item removed                  viewModel.removeItem(item)                }true              }            )SwipeToDismiss(              state = state,              background = {val color byanimateColorAsState(                  targetValue =when (state.dismissDirection) {                    DismissDirection.StartToEnd -> MaterialTheme.colorScheme.primary                    DismissDirection.EndToStart -> MaterialTheme.colorScheme.primary.copy(                      alpha =0.2f                    )null-> Color.Transparent                  }                )Box(                  modifier = modifier                    .fillMaxSize()                    .background(color = color)                    .padding(16.dp),                ) {Icon(                    imageVector = Icons.Filled.Delete,                    contentDescription =null,                    tint = MaterialTheme.colorScheme.primary,                    modifier = modifier.align(Alignment.CenterEnd)                  )                }              },              dismissContent = {ProductListItem(                  product = item,                  modifier = modifier,                  onClick = {                    navController.navigate(                      ProductDetailsDestination.createRouteWithParam(                        item.id                      )                    )                  },                )              },              directions =setOf(DismissDirection.EndToStart),            )          }        }      } else {Text("Product list is empty!")      }    }  }}@ComposableprivatefunAddProductButton(  modifier: Modifier= Modifier,  onClick: () -> Unit,) {FloatingActionButton(    modifier = modifier,    onClick = onClick,    containerColor = MaterialTheme.colorScheme.primary,    contentColor = MaterialTheme.colorScheme.onPrimary  ) {Icon(      imageVector = Icons.Filled.Add,      contentDescription =null,    )  }}

```

Create the `ProductDetailsViewModel.kt`:
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
@HiltViewModelclassProductDetailsViewModel@Injectconstructor(privateval productRepository: ProductRepository,  savedStateHandle: SavedStateHandle,  ) : ViewModel() {privateval _product =MutableStateFlow<Product?>(null)val product: Flow<Product?> = _productprivateval _name =MutableStateFlow("")val name: Flow<String> = _nameprivateval _price =MutableStateFlow(0.0)val price: Flow<Double> = _priceprivateval _imageUrl =MutableStateFlow("")val imageUrl: Flow<String> = _imageUrlinit {val productId = savedStateHandle.get<String>(ProductDetailsDestination.productId)    productId?.let {getProduct(productId = it)    }  }privatefungetProduct(productId: String) {    viewModelScope.launch {val result = productRepository.getProduct(productId).asDomainModel()      _product.emit(result)      _name.emit(result.name)      _price.emit(result.price)    }  }funonNameChange(name: String) {    _name.value= name  }funonPriceChange(price: Double) {    _price.value= price  }funonSaveProduct(image: ByteArray) {    viewModelScope.launch {      productRepository.updateProduct(        id = _product.value?.id,        price = _price.value,        name = _name.value,        imageFile = image,        imageName ="image_${_product.value.id}",      )    }  }funonImageChange(url: String) {    _imageUrl.value= url  }privatefunProductDto.asDomainModel(): Product {returnProduct(      id =this.id,      name =this.name,      price =this.price,      image =this.image    )  }}

```

Create the `ProductDetailsScreen.kt`:
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
@OptIn(ExperimentalCoilApi::class)@SuppressLint("UnusedMaterialScaffoldPaddingParameter")@ComposablefunProductDetailsScreen(  modifier: Modifier= Modifier,  viewModel: ProductDetailsViewModel=hiltViewModel(),  navController: NavController,  productId: String?,) {val snackBarHostState =remember { SnackbarHostState() }val coroutineScope =rememberCoroutineScope()Scaffold(    snackbarHost = { SnackbarHost(snackBarHostState) },    topBar = {TopAppBar(        navigationIcon = {IconButton(onClick = {            navController.navigateUp()          }) {Icon(              imageVector = Icons.Filled.ArrowBack,              contentDescription =null,              tint = MaterialTheme.colorScheme.onPrimary            )          }        },        backgroundColor = MaterialTheme.colorScheme.primary,        title = {Text(            text =stringResource(R.string.product_details_text_screen_title),            color = MaterialTheme.colorScheme.onPrimary,          )        },      )    }  ) {val name = viewModel.name.collectAsState(initial ="")val price = viewModel.price.collectAsState(initial =0.0)var imageUrl = Uri.parse(viewModel.imageUrl.collectAsState(initial =null).value)val contentResolver = LocalContext.current.contentResolverColumn(      modifier = modifier        .padding(16.dp)        .fillMaxSize()    ) {val galleryLauncher =rememberLauncherForActivityResult(ActivityResultContracts.GetContent())        { uri ->          uri?.let {if (it.toString() != imageUrl.toString()) {              viewModel.onImageChange(it.toString())            }          }        }Image(        painter =rememberImagePainter(imageUrl),        contentScale = ContentScale.Fit,        contentDescription =null,        modifier = Modifier          .padding(16.dp, 8.dp)          .size(100.dp)          .align(Alignment.CenterHorizontally)      )IconButton(modifier = modifier.align(alignment = Alignment.CenterHorizontally),        onClick = {          galleryLauncher.launch("image/*")        }) {Icon(          imageVector = Icons.Filled.Edit,          contentDescription =null,          tint = MaterialTheme.colorScheme.primary        )      }OutlinedTextField(        label = {Text(            text ="Product name",            color = MaterialTheme.colorScheme.primary,            style = MaterialTheme.typography.titleMedium          )        },        maxLines =2,        shape =RoundedCornerShape(32),        modifier = modifier.fillMaxWidth(),value= name.value,        onValueChange = {          viewModel.onNameChange(it)        },      )Spacer(modifier = modifier.height(12.dp))OutlinedTextField(        label = {Text(            text ="Product price",            color = MaterialTheme.colorScheme.primary,            style = MaterialTheme.typography.titleMedium          )        },        maxLines =2,        shape =RoundedCornerShape(32),        modifier = modifier.fillMaxWidth(),value= price.value.toString(),        keyboardOptions =KeyboardOptions(keyboardType = KeyboardType.Number),        onValueChange = {          viewModel.onPriceChange(it.toDouble())        },      )Spacer(modifier = modifier.weight(1f))Button(        modifier = modifier.fillMaxWidth(),        onClick = {if (imageUrl.host?.contains("supabase") ==true) {            viewModel.onSaveProduct(image =byteArrayOf())          } else {val image =uriToByteArray(contentResolver, imageUrl)            viewModel.onSaveProduct(image = image)          }          coroutineScope.launch {            snackBarHostState.showSnackbar(              message ="Product updated successfully !",              duration = SnackbarDuration.Short            )          }        }) {Text(text ="Save changes")      }Spacer(modifier = modifier.height(12.dp))OutlinedButton(        modifier = modifier          .fillMaxWidth(),        onClick = {          navController.navigateUp()        }) {Text(text ="Cancel")      }    }  }}privatefungetBytes(inputStream: InputStream): ByteArray {val byteBuffer =ByteArrayOutputStream()val bufferSize =1024val buffer =ByteArray(bufferSize)var len =0while (inputStream.read(buffer).also { len = it } !=-1) {    byteBuffer.write(buffer, 0, len)  }return byteBuffer.toByteArray()}privatefunuriToByteArray(contentResolver: ContentResolver, uri: Uri): ByteArray {if (uri == Uri.EMPTY) {returnbyteArrayOf()  }val inputStream = contentResolver.openInputStream(uri)if (inputStream !=null) {returngetBytes(inputStream)  }returnbyteArrayOf()}

```

Create a `AddProductScreen`:
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
@SuppressLint("UnusedMaterial3ScaffoldPaddingParameter")@OptIn(ExperimentalMaterial3Api::class)@ComposablefunAddProductScreen(  modifier: Modifier= Modifier,  navController: NavController,  viewModel: AddProductViewModel=hiltViewModel(),) {Scaffold(    topBar = {TopAppBar(        navigationIcon = {IconButton(onClick = {            navController.navigateUp()          }) {Icon(              imageVector = Icons.Filled.ArrowBack,              contentDescription =null,              tint = MaterialTheme.colorScheme.onPrimary            )          }        },        backgroundColor = MaterialTheme.colorScheme.primary,        title = {Text(            text =stringResource(R.string.add_product_text_screen_title),            color = MaterialTheme.colorScheme.onPrimary,          )        },      )    }  ) { padding ->val navigateAddProductSuccess =      viewModel.navigateAddProductSuccess.collectAsState(initial =null).valueval isLoading =      viewModel.isLoading.collectAsState(initial =null).valueif (isLoading ==true) {LoadingScreen(message ="Adding Product",        onCancelSelected = {          navController.navigateUp()        })    } else {SuccessScreen(        message ="Product added",        onMoreAction = {          viewModel.onAddMoreProductSelected()        },        onNavigateBack = {          navController.navigateUp()        })    }  }}

```

Create the `AddProductViewModel.kt`:
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
@HiltViewModelclassAddProductViewModel@Injectconstructor(privateval productRepository: ProductRepository,) : ViewModel() {privateval _isLoading =MutableStateFlow(false)val isLoading: Flow<Boolean> = _isLoadingprivateval _showSuccessMessage =MutableStateFlow(false)val showSuccessMessage: Flow<Boolean> = _showSuccessMessagefunonCreateProduct(name: String, price: Double) {if (name.isEmpty() || price <=0) return    viewModelScope.launch {      _isLoading.value=trueval product =Product(        id = UUID.randomUUID().toString(),        name = name,        price = price,      )      productRepository.createProduct(product = product)      _isLoading.value=false      _showSuccessMessage.emit(true)    }  }}

```

Create a `SignUpViewModel`:
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
@HiltViewModelclassSignUpViewModel@Injectconstructor(privateval authenticationRepository: AuthenticationRepository) : ViewModel() {privateval _email =MutableStateFlow("")val email: Flow<String> = _emailprivateval _password =MutableStateFlow("")val password = _passwordfunonEmailChange(email: String) {    _email.value= email  }funonPasswordChange(password: String) {    _password.value= password  }funonSignUp() {    viewModelScope.launch {      authenticationRepository.signUp(        email = _email.value,        password = _password.value      )    }  }}

```

Create the `SignUpScreen.kt`:
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
@ComposablefunSignUpScreen(  modifier: Modifier= Modifier,  navController: NavController,  viewModel: SignUpViewModel=hiltViewModel()) {val snackBarHostState =remember { SnackbarHostState() }val coroutineScope =rememberCoroutineScope()Scaffold(    snackbarHost = { androidx.compose.material.SnackbarHost(snackBarHostState) },    topBar = {TopAppBar(        navigationIcon = {IconButton(onClick = {            navController.navigateUp()          }) {Icon(              imageVector = Icons.Filled.ArrowBack,              contentDescription =null,              tint = MaterialTheme.colorScheme.onPrimary            )          }        },        backgroundColor = MaterialTheme.colorScheme.primary,        title = {Text(            text ="Sign Up",            color = MaterialTheme.colorScheme.onPrimary,          )        },      )    }  ) { paddingValues ->Column(      modifier = modifier        .padding(paddingValues)        .padding(20.dp)    ) {val email = viewModel.email.collectAsState(initial ="")val password = viewModel.password.collectAsState()OutlinedTextField(        label = {Text(            text ="Email",            color = MaterialTheme.colorScheme.primary,            style = MaterialTheme.typography.titleMedium          )        },        maxLines =1,        shape =RoundedCornerShape(32),        modifier = modifier.fillMaxWidth(),value= email.value,        onValueChange = {          viewModel.onEmailChange(it)        },      )OutlinedTextField(        label = {Text(            text ="Password",            color = MaterialTheme.colorScheme.primary,            style = MaterialTheme.typography.titleMedium          )        },        maxLines =1,        shape =RoundedCornerShape(32),        modifier = modifier          .fillMaxWidth()          .padding(top =12.dp),value= password.value,        onValueChange = {          viewModel.onPasswordChange(it)        },      )val localSoftwareKeyboardController = LocalSoftwareKeyboardController.currentButton(modifier = modifier        .fillMaxWidth()        .padding(top =12.dp),        onClick = {          localSoftwareKeyboardController?.hide()          viewModel.onSignUp()          coroutineScope.launch {            snackBarHostState.showSnackbar(              message ="Create account successfully. Sign in now!",              duration = SnackbarDuration.Long            )          }        }) {Text("Sign up")      }    }  }}

```

Create a `SignInViewModel`:
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
@HiltViewModelclassSignInViewModel@Injectconstructor(privateval authenticationRepository: AuthenticationRepository) : ViewModel() {privateval _email =MutableStateFlow("")val email: Flow<String> = _emailprivateval _password =MutableStateFlow("")val password = _passwordfunonEmailChange(email: String) {    _email.value= email  }funonPasswordChange(password: String) {    _password.value= password  }funonSignIn() {    viewModelScope.launch {      authenticationRepository.signIn(        email = _email.value,        password = _password.value      )    }  }funonGoogleSignIn() {    viewModelScope.launch {      authenticationRepository.signInWithGoogle()    }  }}

```

Create the `SignInScreen.kt`:
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
@OptIn(ExperimentalMaterial3Api::class, ExperimentalComposeUiApi::class)@ComposablefunSignInScreen(  modifier: Modifier= Modifier,  navController: NavController,  viewModel: SignInViewModel=hiltViewModel()) {val snackBarHostState =remember { SnackbarHostState() }val coroutineScope =rememberCoroutineScope()Scaffold(    snackbarHost = { androidx.compose.material.SnackbarHost(snackBarHostState) },    topBar = {TopAppBar(        navigationIcon = {IconButton(onClick = {            navController.navigateUp()          }) {Icon(              imageVector = Icons.Filled.ArrowBack,              contentDescription =null,              tint = MaterialTheme.colorScheme.onPrimary            )          }        },        backgroundColor = MaterialTheme.colorScheme.primary,        title = {Text(            text ="Login",            color = MaterialTheme.colorScheme.onPrimary,          )        },      )    }  ) { paddingValues ->Column(      modifier = modifier        .padding(paddingValues)        .padding(20.dp)    ) {val email = viewModel.email.collectAsState(initial ="")val password = viewModel.password.collectAsState()      androidx.compose.material.OutlinedTextField(        label = {Text(            text ="Email",            color = MaterialTheme.colorScheme.primary,            style = MaterialTheme.typography.titleMedium          )        },        maxLines =1,        shape =RoundedCornerShape(32),        modifier = modifier.fillMaxWidth(),value= email.value,        onValueChange = {          viewModel.onEmailChange(it)        },      )      androidx.compose.material.OutlinedTextField(        label = {Text(            text ="Password",            color = MaterialTheme.colorScheme.primary,            style = MaterialTheme.typography.titleMedium          )        },        maxLines =1,        shape =RoundedCornerShape(32),        modifier = modifier          .fillMaxWidth()          .padding(top =12.dp),value= password.value,        onValueChange = {          viewModel.onPasswordChange(it)        },      )val localSoftwareKeyboardController = LocalSoftwareKeyboardController.currentButton(modifier = modifier        .fillMaxWidth()        .padding(top =12.dp),        onClick = {          localSoftwareKeyboardController?.hide()          viewModel.onGoogleSignIn()        }) {Text("Sign in with Google")      }Button(modifier = modifier        .fillMaxWidth()        .padding(top =12.dp),        onClick = {          localSoftwareKeyboardController?.hide()          viewModel.onSignIn()          coroutineScope.launch {            snackBarHostState.showSnackbar(              message ="Sign in successfully !",              duration = SnackbarDuration.Long            )          }        }) {Text("Sign in")      }OutlinedButton(modifier = modifier        .fillMaxWidth()        .padding(top =12.dp), onClick = {        navController.navigate(SignUpDestination.route)      }) {Text("Sign up")      }    }  }}

```

### Implement the `MainActivity`[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#implement-the-mainactivity)
In the `MainActivity` you created earlier, show your newly created screens:
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
@AndroidEntryPointclassMainActivity : ComponentActivity() {@Injectlateinitvar supabaseClient: SupabaseClient@OptIn(ExperimentalMaterial3Api::class)overridefunonCreate(savedInstanceState: Bundle?) {super.onCreate(savedInstanceState)setContent {ManageProductsTheme {// A surface container using the 'background' color from the themeval navController =rememberNavController()val currentBackStack by navController.currentBackStackEntryAsState()val currentDestination = currentBackStack?.destinationScaffold { innerPadding ->NavHost(            navController,            startDestination = ProductListDestination.route,            Modifier.padding(innerPadding)          ) {composable(ProductListDestination.route) {ProductListScreen(                navController = navController              )            }composable(AuthenticationDestination.route) {SignInScreen(                navController = navController              )            }composable(SignUpDestination.route) {SignUpScreen(                navController = navController              )            }composable(AddProductDestination.route) {AddProductScreen(                navController = navController              )            }composable(              route ="${ProductDetailsDestination.route}/{${ProductDetailsDestination.productId}}",              arguments = ProductDetailsDestination.arguments            ) { navBackStackEntry ->val productId =                navBackStackEntry.arguments?.getString(ProductDetailsDestination.productId)ProductDetailsScreen(                productId = productId,                navController = navController,              )            }          }        }      }    }  }}

```

### Create the success screen[#](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-the-success-screen)
To handle OAuth and OTP signins, create a new activity to handle the deep link you set in `AndroidManifest.xml`:
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
<?xml version="1.0" encoding="utf-8"?><manifest xmlns:android="http://schemas.android.com/apk/res/android"xmlns:tools="http://schemas.android.com/tools"><uses-permission android:name="android.permission.INTERNET"/><applicationandroid:name=".ManageProductApplication"android:allowBackup="true"android:dataExtractionRules="@xml/data_extraction_rules"android:enableOnBackInvokedCallback="true"android:fullBackupContent="@xml/backup_rules"android:icon="@mipmap/ic_launcher"android:label="@string/app_name"android:supportsRtl="true"android:theme="@style/Theme.ManageProducts"tools:targetApi="31"><activityandroid:name=".DeepLinkHandlerActivity"android:exported="true"android:theme="@style/Theme.ManageProducts"><intent-filter android:autoVerify="true"><action android:name="android.intent.action.VIEW"/><category android:name="android.intent.category.DEFAULT"/><category android:name="android.intent.category.BROWSABLE"/><dataandroid:host="supabase.com"android:scheme="app"/></intent-filter></activity><activityandroid:name=".MainActivity"android:exported="true"android:label="@string/app_name"android:theme="@style/Theme.ManageProducts"><intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter></activity></application></manifest>

```

Then create the `DeepLinkHandlerActivity`:
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
@AndroidEntryPointclassDeepLinkHandlerActivity : ComponentActivity() {@Injectlateinitvar supabaseClient: SupabaseClientprivatelateinitvar callback: (String, String) -> UnitoverridefunonCreate(savedInstanceState: Bundle?) {super.onCreate(savedInstanceState)    supabaseClient.handleDeeplinks(intent = intent,      onSessionSuccess = { userSession ->        Log.d("LOGIN", "Log in successfully with user info: ${userSession.user}")        userSession.user?.apply {callback(email ?: "", createdAt.toString())        }      })setContent {val navController =rememberNavController()val emailState =remember { mutableStateOf("") }val createdAtState =remember { mutableStateOf("") }LaunchedEffect(Unit) {        callback = { email, created ->          emailState.value= email          createdAtState.value= created        }      }ManageProductsTheme {Surface(          modifier = Modifier.fillMaxSize(),          color = MaterialTheme.colorScheme.background        ) {SignInSuccessScreen(            modifier = Modifier.padding(20.dp),            navController = navController,            email = emailState.value,            createdAt = createdAtState.value,            onClick = { navigateToMainApp() }          )        }      }    }  }privatefunnavigateToMainApp() {val intent =Intent(this, MainActivity::class.java).apply {      flags = Intent.FLAG_ACTIVITY_CLEAR_TOP    }startActivity(intent)  }}

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/tutorials/with-kotlin.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#project-setup)[Create a project](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-a-project)[Set up the database schema](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-the-database-schema)[Get the API keys](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#get-the-api-keys)[Set up Google authentication](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-google-authentication)[Building the app](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#building-the-app)[Create new Android project](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-new-android-project)[Set up API key and secret securely](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-api-key-and-secret-securely)[Set up Supabase dependencies](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-supabase-dependencies)[Set up Hilt for dependency injection](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#set-up-hilt-for-dependency-injection)[Provide Supabase instances with Hilt](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#provide-supabase-instances-with-hilt)[Create a data transfer object](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-a-data-transfer-object)[Implement repositories](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#implement-repositories)[Implement screens](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#implement-screens)[Implement the MainActivity](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#implement-the-mainactivity)[Create the success screen](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin#create-the-success-screen)
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



