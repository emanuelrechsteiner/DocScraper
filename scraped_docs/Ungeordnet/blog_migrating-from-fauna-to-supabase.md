---
url: https://supabase.com/blog/migrating-from-fauna-to-supabase
scraped_at: 2025-05-25T09:35:50.938284
title: Migrating from Fauna to Supabase
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
# Migrating from Fauna to Supabase
21 Mar 2025
•
8 minute read
[![Prashant Sridharan avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F914007%3Fv%3D4&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Prashant SridharanProduct Marketing](https://x.com/CoolAssPuppy)
![Migrating from Fauna to Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffauna-transition%2Ffauna-transition-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Fauna recently announced they will sunset their product by the end of May 2025, prompting engineering teams to find reliable alternatives quickly. Supabase offers a natural migration path for Fauna users, providing a robust, scalable, and open-source alternative built on Postgres.
## The implications of Fauna sunsetting[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#the-implications-of-fauna-sunsetting)
Fauna was known for its serverless database model, offering easy scalability, flexible data modeling, and integrated GraphQL APIs. Teams depending on Fauna must now evaluate alternatives carefully, considering impacts on data modeling, querying, and backend logic.
Migrating away from Fauna requires adjustments in query logic, schema definition, and overall application architecture.
## Why Supabase is a strong replacement for Fauna[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#why-supabase-is-a-strong-replacement-for-fauna)
Supabase is an open-source Postgres development platform that offers:
  * **Managed Postgres database** : Stability, reliability, and strong SQL ecosystem with mature tooling.
  * **Automatically generated REST APIs (via PostgREST)** : Direct analog to Fauna’s built-in API functionality.
  * **Native JSONB Support:** Supabase supports JSONB data types as well as JSON functions and operators to efficiently query collection-style data, prior to full-fledged normalization.
  * **Real-time database updates** , integrated authentication, secure file storage, and edge functions.
  * **Row-level security** : Built directly into the database, allowing precise access control.
  * **Robust TypeScript support** : Seamless integration with modern development workflows.
  * **Full ACID compliance** : Stronger transactional guarantees than Fauna.
  * **Predictable pricing** : Transparent, usage-based billing that avoids surprises.
  * **Improved local and remote development workflow** : Efficient, predictable, and familiar to most developers.
  * **Global community**. Supabase has a vibrant community of users and contributors around the world.


## Migrating from Fauna to Supabase: a step-by-step guide[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#migrating-from-fauna-to-supabase-a-step-by-step-guide)
Migrating across data structures can be difficult, and normalizing large sets of unstructured or semi-structured data can take time. Given the May 30th Fauna Sunset deadline, we recommend a two-phase approach to ensure your application stays online.
**Phase 1: Export and load Into Supabase**
In this phase, your data is safely moved to Supabase before the Fauna sunset date and your applications will still function properly.
  1. Export data from Fauna
  2. Import JSON data into Supabase
  3. Transition existing Fauna API calls to Supabase PostgREST APIs


**Phase 2: Optimize and enhance**
In this phase, with your data secured and your applications still functional, you can safely and confidently complete the transition to Supabase.
  1. SQL data normalization and PostgREST update
  2. Incorporation of additional Supabase features such as authentication, and object storage


## Phase 1[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#phase-1)
Phase 1 of the Fauna to Supabase migration focuses on exporting your data from Fauna, importing into Supabase as a JSONB data type, and rewriting your data APIs to use the Supabase SDK.
### Step 1: Export data from Fauna[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-1-export-data-from-fauna)
Fauna allows exporting collections through their admin dashboard or CLI. Use the Fauna CLI to export your collections to Amazon S3 in JSON format:
`
1
fauna export create s3 \
2
 --database <database_name> \
3
 --collection <collection_name> \
4
 --bucket <s3_bucket_name> \
5
 --path <s3_bucket_path> \
6
 --format simple
`
Fauna has [also provided instructions](https://docs.fauna.com/fauna/current/migrate/?lang=javascript) using the Fauna Query Language.
### Step 2: Import JSON Data into Supabase[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-2-import-json-data-into-supabase)
Create a table in Supabase with a JSONB column to store raw Fauna documents:
`
1
create table fauna_users_raw (
2
 id uuid primary key default gen_random_uuid(),
3
 data jsonb not null
4
);
`
Then, ingest the exported JSON data into this Supabase table using this custom script:
`
1
import { createClient } from '@supabase/supabase-js'
2
import fs from 'fs'
34
const supabaseUrl = 'YOUR_SUPABASE_URL'
5
const supabaseKey = 'YOUR_SUPABASE_API_KEY'
6
const tableName = 'YOUR_TABLE_NAME'
7
const jsonFilePath = './filename.json'
89
const supabase = createClient(supabaseUrl, supabaseKey)
1011
async function loadDocumentsToSupabase() {
12
 try {
13
  // Read JSON file
14
  const rawData = fs.readFileSync(jsonFilePath)
15
  const dataArray = JSON.parse(rawData).map((data) => ({ data }))
1617
  // Insert data into Supabase
18
  const { error } = await supabase.from(tableName).insert(dataArray)
1920
  if (error) {
21
   console.error('Error inserting data:', error)
22
   return
23
  }
2425
  console.log(`Successfully inserted ${dataArray.length} records into ${tableName}`)
26
 } catch (error) {
27
  console.error('Error in process:', error)
28
 }
29
}
3031
loadDocumentsToSupabase()
`
### Step 3: Transition Fauna API calls to Supabase PostgREST[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-3-transition-fauna-api-calls-to-supabase-postgrest)
Once your data has been structured into tables, Supabase automatically generates REST APIs for each table via PostgREST, allowing effortless querying from your application.
Here’s a Fauna query example (using FQL) for obtaining data from a `users` table:
`
1
import { Client, fql } from 'fauna'
23
const client = new Client({ secret: '<your-fauna-secret>' })
45
const usersQuery = fql`
6
 users.all() {
7
  name,
8
  email
9
 }
10
`
1112
client
13
 .query(usersQuery)
14
 .then((data) => console.log(data))
15
 .catch((error) => console.error('Error fetching users:', error))
`
And here’s the equivalent Supabase REST API call:
`
1
import { createClient } from '@supabase/supabase-js'
23
const supabase = createClient('https://<your-project>.supabase.co', '<your-api-key>')
45
const { data, error } = await supabase.from('users').select(`
6
  user: metadata->user
7
 `)
8
// the -> operator returns values as jsonb for the user collection
910
if (error) console.error(error)
11
else console.log(data)
`
## Phase 2:[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#phase-2)
Once you have brought your collections over to Supabase, you may find you would benefit from data normalization. As Supabase is built on top of Postgres, having normalized data will lead to significant performance benefits that cannot be matched by a set of collections stored in JSONB.
### Step 1: Normalize the data using SQL[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-1-normalize-the-data-using-sql)
Once your data is imported as JSONB, leverage the powerful Postgres JSON functions to incrementally normalize and populate relational tables. In this example, we’re importing data from a rudimentary `users` table:
`
1
-- Example normalization for users
2
INSERT INTO users (name, email)
3
SELECT
4
 data->'data'->'name' AS name,
5
 data->'data'->'email' AS email
6
FROM fauna_users_raw;
78
-- Example normalization of nested orders
9
INSERT INTO orders (user_id, product, quantity)
10
SELECT
11
 u.id,
12
 order_data->>'product',
13
 (order_data->>'quantity')::INTEGER
14
FROM fauna_users_raw f
15
JOIN users u ON (f.data->'data'->>'email') = u.email,
16
LATERAL jsonb_array_elements(f.data->'data'->'orders') AS order_data;
`
### Step 1.5: Rewrite PostgREST to query normalized data[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-15-rewrite-postgrest-to-query-normalized-data)
Once your data has been structured into tables, Supabase automatically generates REST APIs for each table via PostgREST, allowing effortless querying from your application.
Here’s the PostgREST query for JSONB data from Phase 1:
`
1
import { createClient } from '@supabase/supabase-js'
23
const supabase = createClient('https://<your-project>.supabase.co', '<your-api-key>')
45
const { data, error } = await supabase.from('users').select(`
6
  user: metadata->user
7
 `)
8
// the -> operator returns values as jsonb for the user collection
910
if (error) console.error(error)
11
else console.log(data)
`
And here’s the equivalent Supabase REST API call with normalized data:
`
1
import { createClient } from '@supabase/supabase-js'
23
const supabase = createClient('https://<your-project>.supabase.co', '<your-api-key>')
45
const { data, error } = await supabase.from('users').select('name, email')
67
if (error) console.error(error)
8
else console.log(data)
`
### Step 2: Add more Supabase features[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-2-add-more-supabase-features)
Once your data is migrated, you can start to use Supabase to its fullest:
  * [**Authentication**](https://supabase.com/auth). Let your users login with email, Google, Apple, GitHub, and more. Secure and trusted.
  * [**Role-Based Access Control (RBAC)**](https://supabase.com/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac). Secure your data properly.
  * [**Storage**](https://supabase.com/storage). Affordable and fast, for all the videos and images you need in your app.
  * [**Edge Functions**](https://supabase.com/edge-functions). Custom backend logic when you want to dive into code.
  * [**Realtime**](https://supabase.com/realtime). Build immersive multi-player, collaborative experiences.
  * [**AI Ready**](https://supabase.com/modules/vector). When you’re ready to explore vectors and the power of AI, Supabase is there with industry-standard tools to guide you.
  * [**Foreign Data Wrappers (FDW)**](https://supabase.com/docs/guides/database/extensions/wrappers/overview). Pull data from Google Sheets, Airtable, MySQL, and more, as if they were part of Supabase natively.
  * **Instant and secure deployment**. No need to set up servers, manage DevOps, or tweak security settings.


## Key considerations and trade-offs[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#key-considerations-and-trade-offs)
  * **Schema Flexibility** : Postgres schemas require careful planning compared to Fauna’s more flexible data structures.
  * **Migration Complexity** : Fauna’s nested structures necessitate normalization scripts.
  * **Query Refactoring** : Fauna’s FQL/GraphQL queries must be translated to SQL queries.
  * **Add indexes** : Use the Index Advisor in the Supabase Dashboard to further optimize your tables.


## Conclusion[#](https://supabase.com/blog/migrating-from-fauna-to-supabase#conclusion)
This is no doubt a stressful time as you transition away from Fauna. Supabase is here to help you every step of the way. Reach out to us and we can help you plan your transition and provide assistance.
Supabase is a comprehensive, scalable replacement for Fauna. Supabase is built on Postgres and offers a robust relational model, powerful security features, and predictable pricing. Supabase enables engineering teams to confidently transition away from Fauna thanks to its SQL ecosystem, more mature/better tooling, row level security, strong typescript support, and full ACID compliance. Thoughtful planning and methodical execution will ensure a seamless migration and long-term reliability.
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmigrating-from-fauna-to-supabase&text=Migrating%20from%20Fauna%20to%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmigrating-from-fauna-to-supabase&text=Migrating%20from%20Fauna%20to%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fmigrating-from-fauna-to-supabase&t=Migrating%20from%20Fauna%20to%20Supabase)
[Last postPostgres Language Server: Initial Release29 March 2025](https://supabase.com/blog/postgres-language-server)
[Next postMigrating from the MongoDB Data API to Supabase20 March 2025](https://supabase.com/blog/migrating-mongodb-data-api-with-supabase)
[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [The implications of Fauna sunsetting](https://supabase.com/blog/migrating-from-fauna-to-supabase#the-implications-of-fauna-sunsetting)
  * [Why Supabase is a strong replacement for Fauna](https://supabase.com/blog/migrating-from-fauna-to-supabase#why-supabase-is-a-strong-replacement-for-fauna)
  * [Migrating from Fauna to Supabase: a step-by-step guide](https://supabase.com/blog/migrating-from-fauna-to-supabase#migrating-from-fauna-to-supabase-a-step-by-step-guide)
  * [Phase 1](https://supabase.com/blog/migrating-from-fauna-to-supabase#phase-1)
    * [Step 1: Export data from Fauna](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-1-export-data-from-fauna)
    * [Step 2: Import JSON Data into Supabase](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-2-import-json-data-into-supabase)
    * [Step 3: Transition Fauna API calls to Supabase PostgREST](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-3-transition-fauna-api-calls-to-supabase-postgrest)
  * [Phase 2:](https://supabase.com/blog/migrating-from-fauna-to-supabase#phase-2)
    * [Step 1: Normalize the data using SQL](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-1-normalize-the-data-using-sql)
    * [Step 1.5: Rewrite PostgREST to query normalized data](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-15-rewrite-postgrest-to-query-normalized-data)
    * [Step 2: Add more Supabase features](https://supabase.com/blog/migrating-from-fauna-to-supabase#step-2-add-more-supabase-features)
  * [Key considerations and trade-offs](https://supabase.com/blog/migrating-from-fauna-to-supabase#key-considerations-and-trade-offs)
  * [Conclusion](https://supabase.com/blog/migrating-from-fauna-to-supabase#conclusion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmigrating-from-fauna-to-supabase&text=Migrating%20from%20Fauna%20to%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmigrating-from-fauna-to-supabase&text=Migrating%20from%20Fauna%20to%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fmigrating-from-fauna-to-supabase&t=Migrating%20from%20Fauna%20to%20Supabase)
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

