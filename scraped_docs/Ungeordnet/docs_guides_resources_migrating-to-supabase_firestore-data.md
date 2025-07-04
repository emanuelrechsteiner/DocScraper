---
url: https://supabase.com/docs/guides/resources/migrating-to-supabase/firestore-data
scraped_at: 2025-05-25T09:43:21.975701
title: Migrated from Firebase Firestore to Supabase | Supabase Docs
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
[Platform](https://supabase.com/docs/guides/platform)
Add-ons
  * [Custom Domains](https://supabase.com/docs/guides/platform/custom-domains)
  * [Database Backups](https://supabase.com/docs/guides/platform/backups)
  * [IPv4 Address](https://supabase.com/docs/guides/platform/ipv4-address)
  * [Read Replicas](https://supabase.com/docs/guides/platform/read-replicas)
Upgrades & Migrations
  * [Upgrading](https://supabase.com/docs/guides/platform/upgrading)
  * [Migrating within Supabase](https://supabase.com/docs/guides/platform/migrating-within-supabase)
  * [Migrating to Supabase](https://supabase.com/docs/guides/platform/migrating-to-supabase)
  * [Auth0](https://supabase.com/docs/guides/platform/migrating-to-supabase/auth0)
  * [Firebase Auth](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth)
  * [Firestore Data](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data)
  * [Firebase Storage](https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-storage)
  * [Heroku](https://supabase.com/docs/guides/platform/migrating-to-supabase/heroku)
  * [Render](https://supabase.com/docs/guides/platform/migrating-to-supabase/render)
  * [Amazon RDS](https://supabase.com/docs/guides/platform/migrating-to-supabase/amazon-rds)
  * [Postgres](https://supabase.com/docs/guides/platform/migrating-to-supabase/postgres)
  * [Vercel Postgres](https://supabase.com/docs/guides/platform/migrating-to-supabase/vercel-postgres)
  * [Neon](https://supabase.com/docs/guides/platform/migrating-to-supabase/neon)
  * [MySQL](https://supabase.com/docs/guides/platform/migrating-to-supabase/mysql)
  * [MSSQL](https://supabase.com/docs/guides/platform/migrating-to-supabase/mssql)
Project & Account Management
  * [Access Control](https://supabase.com/docs/guides/platform/access-control)
  * [Multi-factor Authentication](https://supabase.com/docs/guides/platform/multi-factor-authentication)
  * [Transfer Project](https://supabase.com/docs/guides/platform/project-transfer)
  * [Single Sign-On](https://supabase.com/docs/guides/platform/sso)
Platform Configuration
  * [Regions](https://supabase.com/docs/guides/platform/regions)
  * [Compute and Disk](https://supabase.com/docs/guides/platform/compute-and-disk)
  * [Database Size](https://supabase.com/docs/guides/platform/database-size)
  * [HIPAA Projects](https://supabase.com/docs/guides/platform/hipaa-projects)
  * [Network Restrictions](https://supabase.com/docs/guides/platform/network-restrictions)
  * [Performance Tuning](https://supabase.com/docs/guides/platform/performance)
  * [SSL Enforcement](https://supabase.com/docs/guides/platform/ssl-enforcement)
  * [Default Platform Permissions](https://supabase.com/docs/guides/platform/permissions)
Billing
  * [About billing on Supabase](https://supabase.com/docs/guides/platform/billing-on-supabase)
  * [Get set up for billing](https://supabase.com/docs/guides/platform/get-set-up-for-billing)
  * [Manage your subscription](https://supabase.com/docs/guides/platform/manage-your-subscription)
  * [Manage your usage](https://supabase.com/docs/guides/platform/manage-your-usage)
  * [Your monthly invoice](https://supabase.com/docs/guides/platform/your-monthly-invoice)
  * [Control your costs](https://supabase.com/docs/guides/platform/cost-control)
  * [Credits](https://supabase.com/docs/guides/platform/credits)
  * [Billing FAQ](https://supabase.com/docs/guides/platform/billing-faq)


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
Platform
  1. [Platform](https://supabase.com/docs/guides/platform)
  2. More
  3. [Migrating to Supabase](https://supabase.com/docs/guides/platform/migrating-to-supabase)
  4. [Firestore Data](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data)


Migrated from Firebase Firestore to Supabase
Migrate your Firebase Firestore database to a Supabase Postgres database.
Supabase provides several [tools](https://github.com/supabase-community/firebase-to-supabase/tree/main/firestore) to convert data from a Firebase Firestore database to a Supabase Postgres database. The process copies the entire contents of a single Firestore `collection` to a single Postgres `table`.
The Firestore `collection` is "flattened" and converted to a table with basic columns of one of the following types: `text`, `numeric`, `boolean`, or `jsonb`. If your structure is more complex, you can write a program to split the newly-created `json` file into multiple, related tables before you import your `json` file(s) to Supabase.
## Set up the migration tool [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#set-up-migration-tool)
  1. Clone the [`firebase-to-supabase`](https://github.com/supabase-community/firebase-to-supabase) repository:
```

1
gitclonehttps://github.com/supabase-community/firebase-to-supabase.git

```

  2. In the `/firestore` directory, create a file named `supabase-service.json` with the following contents:
```

1
2
3
4
5
6
7
{"host":"database.server.com","password":"secretpassword","user":"postgres","database":"postgres","port":5432}

```

  3. On your project dashboard, click [Connect](https://supabase.com/dashboard/project/_?showConnect=true)
  4. Under the Session pooler, click on the View parameters under the connect string. Replace the `Host` and `User` fields with the values shown.
  5. Enter the password you used when you created your Supabase project in the `password` entry in the `supabase-service.json` file.


## Generate a Firebase private key [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#generate-firebase-private-key)
  1. Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project.
  2. Click the gear icon next to **Project Overview** in the sidebar and select **Project Settings**.
  3. Click **Service Accounts** and select **Firebase Admin SDK**.
  4. Click **Generate new private key**.
  5. Rename the downloaded file to `firebase-service.json`.


## Command line options[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#command-line-options)
### List all Firestore collections[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#list-all-firestore-collections)
`node collections.js`
### Dump Firestore collection to JSON file[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#dump-firestore-collection-to-json-file)
`node firestore2json.js <collectionName> [<batchSize>] [<limit>]`
  * `batchSize` (optional) defaults to 1000
  * output filename is `<collectionName>.json`
  * `limit` (optional) defaults to 0 (no limit)


#### Customize the JSON file with hooks[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#customize-the-json-file-with-hooks)
You can customize the way your JSON file is written using a [custom hook](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#custom-hooks). A common use for this is to "flatten" the JSON file, or to split nested data into separate, related database tables. For example, you could take a Firestore document that looks like this:
```

1
[{"user":"mark","score":100,"items":["hammer","nail","glue"]}]

```

And split it into two files (one table for users and one table for items):
```

1
[{"user":"mark","score":100}]

```

```

1
2
3
4
5
[{"user":"mark","item":"hammer"},{"user":"mark","item":"nail"},{"user":"mark","item":"glue"}]

```

### Import JSON file to Supabase (Postgres) [#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#import-to-supabase)
`node json2supabase.js <path_to_json_file> [<primary_key_strategy>] [<primary_key_name>]`
  * `<path_to_json_file>` The full path of the file you created in the previous step (`Dump Firestore collection to JSON file `), such as `./my_collection.json`
  * `[<primary_key_strategy>]` (optional) Is one of: 
    * `none` (default) No primary key is added to the table.
    * `smallserial` Creates a key using `(id SMALLSERIAL PRIMARY KEY)` (autoincrementing 2-byte integer).
    * `serial` Creates a key using `(id SERIAL PRIMARY KEY)` (autoincrementing 4-byte integer).
    * `bigserial` Creates a key using `(id BIGSERIAL PRIMARY KEY)` (autoincrementing 8-byte integer).
    * `uuid` Creates a key using `(id UUID PRIMARY KEY DEFAULT gen_random_uuid())` (randomly generated UUID).
    * `firestore_id` Creates a key using `(id TEXT PRIMARY KEY)` (uses existing `firestore_id` random text as key).
  * `[<primary_key_name>]` (optional) Name of primary key. Defaults to "id".


## Custom hooks[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#custom-hooks)
Hooks are used to customize the process of exporting a collection of Firestore documents to JSON. They can be used for:
  * Customizing or modifying keys
  * Calculating data
  * Flattening nested documents into related SQL tables


### Write a custom hook[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#write-a-custom-hook)
#### Create a `.js` file for your collection[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#create-a-js-file-for-your-collection)
If your Firestore collection is called `users`, create a file called `users.js` in the current folder.
#### Construct your `.js` file[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#construct-your-js-file)
The basic format of a hook file looks like this:
```

1
2
3
4
module.exports=(collectionName,doc,recordCounters,writeRecord)=>{// modify the doc herereturndoc}

```

##### Parameters
  * `collectionName`: The name of the collection you are processing.
  * `doc`: The current document (JSON object) being processed.
  * `recordCounters`: An internal object that keeps track of how many records have been processed in each collection.
  * `writeRecord`: This function automatically handles the process of writing data to other JSON files (useful for "flatting" your document into separate JSON files to be written to separate database tables). `writeRecord` takes the following parameters: 
    * `name`: Name of the JSON file to write to.
    * `doc`: The document to write to the file.
    * `recordCounters`: The same `recordCounters` object that was passed to this hook (just passes it on).


### Examples[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#examples)
#### Add a new (unique) numeric key to a collection[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#add-a-new-unique-numeric-key-to-a-collection)
```

1
2
3
4
module.exports=(collectionName,doc,recordCounters,writeRecord)=>{doc.unique_key=recordCounter[collectionName]+1returndoc}

```

#### Add a timestamp of when this record was dumped from Firestore[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#add-a-timestamp-of-when-this-record-was-dumped-from-firestore)
```

1
2
3
4
module.exports=(collectionName,doc,recordCounters,writeRecord)=>{doc.dump_time=newDate().toISOString()returndoc}

```

#### Flatten JSON into separate files[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#flatten-json-into-separate-files)
Flatten the `users` collection into separate files:
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
[{"uid":"abc123","name":"mark","score":100,"weapons":["toothpick","needle","rock"]},{"uid":"xyz789","name":"chuck","score":9999999,"weapons":["hand","foot","head"]}]

```

The `users.js` hook file:
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
module.exports=(collectionName,doc,recordCounters,writeRecord)=>{for (leti=0;i<doc.weapons.length;i++) {constweapon={uid:doc.uid,weapon:doc.weapons[i],}writeRecord('weapons',weapon,recordCounters)}deletedoc.weapons// moved to separate filereturndoc}

```

The result is two separate JSON files:
```

1
2
3
4
[{"uid":"abc123","name":"mark","score":100},{"uid":"xyz789","name":"chuck","score":9999999}]

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
[{"uid":"abc123","weapon":"toothpick"},{"uid":"abc123","weapon":"needle"},{"uid":"abc123","weapon":"rock"},{"uid":"xyz789","weapon":"hand"},{"uid":"xyz789","weapon":"foot"},{"uid":"xyz789","weapon":"head"}]

```

## Resources[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#resources)
  * [Supabase vs Firebase](https://supabase.com/alternatives/supabase-vs-firebase)
  * [Firestore Storage Migration](https://supabase.com/docs/guides/migrations/firebase-storage)
  * [Firebase Auth Migration](https://supabase.com/docs/guides/migrations/firebase-auth)


## Enterprise[#](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#enterprise)
[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/platform/migrating-to-supabase/firestore-data.mdx)
### Is this helpful?
No Yes
### On this page
[Set up the migration tool ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#set-up-migration-tool)[Generate a Firebase private key ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#generate-firebase-private-key)[Command line options](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#command-line-options)[List all Firestore collections](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#list-all-firestore-collections)[Dump Firestore collection to JSON file](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#dump-firestore-collection-to-json-file)[Import JSON file to Supabase (Postgres) ](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#import-to-supabase)[Custom hooks](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#custom-hooks)[Write a custom hook](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#write-a-custom-hook)[Examples](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#examples)[Resources](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#resources)[Enterprise](https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data#enterprise)
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



