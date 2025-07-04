---
url: https://supabase.com/blog/dbdev
scraped_at: 2025-05-25T08:39:18.257186
title: dbdev: PostgreSQL Package Manager
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
# dbdev: PostgreSQL Package Manager
14 Apr 2023
•
11 minute read
[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Oliver RiceEngineering](https://github.com/olirice)
[![John Dalton avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdaltjoh-aws.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)John DaltonProduct Management Leader @ AWS](https://github.com/daltjoh-aws)
![dbdev: PostgreSQL Package Manager](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-one-more-thing%2Fday-5-dbdev-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we’re publicly previewing [**`database.dev`**](https://database.dev), a PostgreSQL package manager. At this stage the package registry is read-only. We've preloaded it with a handful of packages to showcase some of the more interesting possibilities.
![db dev landing page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-one-more-thing%2Fdbdev-landing.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
`dbdev` fills the same role for PostgreSQL as `npm` for JavaScript, `pip` for Python and `cargo` for Rust in that it enables publishing libraries and applications for repeatable deployment. We'll be releasing the tooling necessary for third-parties to publish packages to the registry once we’ve collected some community feedback and incorporate any great new ideas. Our goal is to create an [open ecosystem](https://github.com/supabase/dbdev) for packaging and discovering SQL.
The initial preview is compatible with [new projects](https://database.new) on the Supabase platform. It can also be installed on any PostgreSQL instance that support [`pg_tle`](https://github.com/aws/pg_tle) and [`pgsql-http`](https://github.com/pramsey/pgsql-http).
## Get Started with dbdev[#](https://supabase.com/blog/dbdev#get-started-with-dbdev)
The in-database client is the easiest way to get started. You can setup the installer by executing the SQL snippet available at [database.dev/installer](https://database.dev/installer).
Once the `dbdev` client is present, packages can be installed from the registry as shown below:
`
1
-- Load the package from the package index
2
select
3
 dbdev.install ('olirice-asciiplot');
45
-- Enable the extension
6
create extension "olirice-asciiplot" version '0.2.1';
`
You can explore all available packages on [database.dev](https://database.dev).
Notice that PostgreSQL sees the [`olirice-asciiplot`](https://database.dev/olirice/asciiplot) package as a native extension, rather than a raw snippet of SQL. That approach allows us to leverage PostgreSQL's builtin tooling for extension management.
With our extension installed, you can use it like any other PostgreSQL extension. Continuing with the [`olirice-asciiplot`](https://database.dev/olirice/asciiplot) example, we can call the `scatter` function it provides to create an ASCII scatterplot:
`
1
select
2
 scatter(
3
  val::numeric, -- x
4
  val::numeric, -- y
5
  'stonks!',  -- title
6
  15,      -- height
7
  50      -- width
8
 )
9
from
10
 generate_series(1,10) z(val);
11
/*
12
          stonks!
13
----------------------------------------------
14
|                    *
15
|
16
|                 *
17
|               *
18
|
19
|             *
20
|
21
|           *
22
|         *
23
|
24
|      *
25
|
26
|    *
27
|  *
28
*/
`
PostgreSQL's extension tooling is excellent, but it predates some practices learned from best-in-class package indexes like crates.io. To give developers a more modern development experience, we opted to layer additional strictness on top of what PostgreSQL imposes:
### Versioning[#](https://supabase.com/blog/dbdev#versioning)
The extension system has full support for versioning and migrations. Officially, PostgreSQL has loose constraints for version names. We made the choice to enforce a lite version of [Semantic Versioning](https://semver.org) that restricts version numbers to `major.minor.patch` so authors can communicate bug-fixes, features, and breaking changes in a familiar way.
### Namespaces[#](https://supabase.com/blog/dbdev#namespaces)
Two common challenges faced by package indexes are name squatting and typo squatting.
  * Name squatting: reserving names for future use
  * Typo squatting: reserving misspelling of existing package


The ethics of name squatting get dicey at scale while typo squatting is widely viewed as malicious behavior. To mitigate both issues, all packages published to [database.dev](https://database.dev) are namespaced to their owning organization or user’s handle. For example a package named [`olirice-index_advisor`](https://database.dev/olirice/index_advisor) was created by the account `olirice` under the name `index_advisor`. If another user, `some_user`, forks and republishes the project, it would be available under `some_user-index_advisor`. Problem solved ✅
## Running on Supabase[#](https://supabase.com/blog/dbdev#running-on-supabase)
[database.dev](https://database.dev) is not coupled to the Supabase platform. `dbdev` can load SQL libraries on any PostgreSQL instance with the required base extensions. However, using `dbdev` in tandem with Supabase yields some extra possibilities.
Supabase reflects APIs directly from your database’s structure, so a package can contain an entire stateful application, pre-configured with authentication, REST, GraphQL, and realtime change data capture all baked in!
For example, our friends at [LangChain](https://python.langchain.com/en/latest/index.html) published a Supabase backend for their docs search tool that uses a hybrid of document embeddings and full text search to find relevant documents for a user’s query
Its available at [`langchain-hybrid_search`](https://database.dev/langchain/hybrid_search) and here’s how you’d set it up:
`
1
select
2
 dbdev.install ('langchain-hybrid_search');
34
create extension if not exists vector;
56
create extension "langchain-hybrid_search" schema public version '1.0.0';
`
That creates the relevant `documents` table and associated search functions. Then, you can immediately hit it from your front end for best-in-class document search.
`
1
import { OpenAIEmbeddings } from 'langchain/embeddings/openai'
2
import { createClient } from '@supabase/supabase-js'
3
import { SupabaseHybridSearch } from 'langchain/retrievers/supabase'
45
const privateKey = process.env.SUPABASE_PRIVATE_KEY
6
if (!privateKey) throw new Error(`Expected env var SUPABASE_PRIVATE_KEY`)
78
const url = process.env.SUPABASE_URL
9
if (!url) throw new Error(`Expected env var SUPABASE_URL`)
1011
export const run = async () => {
12
 const client = createClient(url, privateKey)
1314
 const embeddings = new OpenAIEmbeddings()
1516
 const retriever = new SupabaseHybridSearch(embeddings, {
17
  client,
18
  // Below are the defaults, expecting that you set up your supabase table and functions according to the guide above. Please change if necessary.
19
  similarityK: 2,
20
  keywordK: 2,
21
  tableName: 'documents',
22
  similarityQueryName: 'match_documents',
23
  keywordQueryName: 'kw_match_documents',
24
 })
2526
 const results = await retriever.getRelevantDocuments('hello bye')
2728
 console.log(results)
29
}
`
## Package Highlights[#](https://supabase.com/blog/dbdev#package-highlights)
That's it for the [`dbdev`](http://database.new) announcement, but a package index is less interesting than what you can do with it! In that vein, the following highlights a few of packages I thought were interesting enough to callout:
### burggraf-pg_headerkit[#](https://supabase.com/blog/dbdev#burggraf-pg_headerkit)
[`burggraf-pg_headerkit`](https://database.dev/burggraf/pg_headerkit) is a toolkit for adding advanced features to PostgREST APIs (including Supabase REST):
  * rate limiting
  * IP allowlisting/denylisting
  * request logging


and more.
For example, you could apply a deny listing to your API using `hdr.in_deny_list()` in a row level security policy or view:
`
1
select
2
 *
3
from app.memos
4
where not hdr.in_deny_list();
`
### olirice-index_advisor[#](https://supabase.com/blog/dbdev#olirice-index_advisor)
[`olirice-index_advisor`](https://database.dev/olirice/index_advisor) is one of the projects we cut from [Launch Week 7](https://supabase.com/launch-week). It is simple tool that takes a query and recommends indexes to minimize the “total_cost” according to the query’s [explain plan](https://www.postgresql.org/docs/current/using-explain.html).
We ultimately ran out of time to squeeze the feature in, but the optimizer works just fine:
`
1
select dbdev.install('olirice-index_advisor');
2
create extension if not exists hypopg;
3
create extension "olirice-index_advisor";
45
-- Create a dummy table
6
create table account(
7
	id int primary key,
8
	name text
9
);
1011
-- Search for indexes to optimize "select id from account where name = 'adsf'"
12
select
13
	*
14
from
15
	index_advisor($$select id from account where name = 'Foo'$$)
`
which shows
`
1
| startup_cost_before | startup_cost_after | total_cost_before | total_cost_after | index_statements                   |
2
| ------------------- | ------------------ | ----------------- | ---------------- | ----------------------------------------------------- |
3
| 0.00        | 1.17        | 25.88       | 6.40       | {"CREATE INDEX ON public.account USING btree (name)"} |
`
In other words, it recommends the index `CREATE INDEX ON public.account USING btree (name)` which is expected to reduce the total cost from 25.88 to 6.40 for a 4x decrease.
`olirice-index_advisor` is compatible with tables, views, and materialized views. It can also see through views to find relevant indexes on underlying tables, and supports generic query arguments. For example, `$1` in `select id from account where name = $1`, which makes it compatible with queries from `pg_stat_statements` and queries generated by the REST API.
Keep an eye open for it in Launch Week 8.
### michelp-adminpack[#](https://supabase.com/blog/dbdev#michelp-adminpack)
[`michelp-adminpack`](https://database.dev/michelp/adminpack) is a collection of tools helpful for administrating your database that we often use internally at Supabase. It holds views for reviewing useful info for debugging and optimizing performance like duplicate indexes, index usage, and table size, to name a few.
For example, to identify potentially unused indexes that can be dropped, you could use the `index_usage` view, which has columns for:
Column| Type  
---|---  
schemaname| name  
tablename| name  
num_rows| bigint  
table_size| text  
index_name| name  
index_size| text  
unique| text  
number_of_scans| bigint  
tuples_read| bigint  
tuples_fetched| bigint  
## Limitations[#](https://supabase.com/blog/dbdev#limitations)
There are several procedural languages (PL) that can be embedded in PostgreSQL and used to define functions. The ones that ship with stock PostgreSQL are `SQL`, and `pl/pgSQL` but there others that can be installed separately, including `pl/v8` for JavaScript, or `pl/perl` for Perl. A **trusted** language has been restricted to remove potentially hazardous functionality like access to the network stack and file system. `pl/v8` and `pl/perl` are examples of trusted languages. In contrast, `pl/python3u` is **untrusted**.
A [Trusted Language Extension (TLE)](https://github.com/aws/pg_tle) is a [PostgreSQL extension](https://www.postgresql.org/docs/current/extend-extensions.html), written exclusively using trusted languages. In some ways that makes them less flexible than classic extensions, which can have C language components (more on that in a second). The advantage to TLEs is that they don't require direct access to the PostgreSQL server’s file system to install. That enables TLEs to be installed by end-users rather than by database administrators or hosting providers. TLEs are the enabling technology that allows a package manager like `dbdev` to function on hosted PostgreSQL platforms like Supabase.
For a more in-depth explanation of Trusted Language Extensions checkout [AWS's pg_tle on Supabase blog post](https://aws.amazon.com/blogs/opensource/supabase-makes-extensions-easier-for-developers-with-trusted-language-extensions-for-postgresql/) or dive into the code at [github.com/aws/pg_tle](https://github.com/aws/pg_tle).
A recent development in the PostgreSQL extension ecosystem is the 1.0 release of a new trusted language, [`pl/rust`](https://github.com/tcdi/plrust), allowing users to define SQL functions written in Rust. As a compiled language, `pl/rust` functions can execute an order of magnitude faster than `pl/pgSQL` for computationally heavy workloads. That closes the biggest capability gap between native extensions with C components and TLEs. `pl/rust` hasn’t released to Supabase yet, but we’re excited about rolling it out in the coming weeks.
## Please Give Feedback[#](https://supabase.com/blog/dbdev#please-give-feedback)
As this is a preview, we anticipate that there may be a few rough edges. If you do take the time to explore `dbdev` at this stage, please contribute to its development at [github.com/supabase/dbdev](https://github.com/supabase/dbdev).
We are particularly interested in hearing about:
  1. Any issues or bugs you encounter
  2. Feature requests and suggestions for improvement
  3. Contributions in the form of code, documentation, or testing


### More Launch Week 7
[Designing with AI![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fai-images%2F00-ai-images-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/designing-with-ai-midjourney)
[Supavisor![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fsupavisor%2Fsupavisor-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://github.com/supabase/supavisor)
[Open Source Logging![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday1%2Fself-hosted-logs-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-logs-self-hosted)
[Self-hosted Deno Edge Functions![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday2%2Fself-hosted-edge-functions-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)
[Storage v3: Resumable Uploads with support for 50GB files![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday3%2Fstorage-v3-thumb.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/storage-v3-resumable-uploads)
[Supabase Auth: SSO, Mobile, and Server-side support![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday4%2Fsso-support-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-auth-sso-pkce)
[Community Highlight![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fcommunity%2Fcommunity-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/launch-week-7-community-highlights)
[Studio Updates![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fstudio%2Fstudio-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/supabase-studio-2.0)
[dbdev![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2Fdbdev-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/dbdev)
[Postgres TLE![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2FpgTLE-thumb.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/blog/pg-tle)
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdbdev&text=dbdev%3A%20PostgreSQL%20Package%20Manager)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdbdev&text=dbdev%3A%20PostgreSQL%20Package%20Manager)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdbdev&t=dbdev%3A%20PostgreSQL%20Package%20Manager)
[Last postWhat's New in pg_graphql v1.221 April 2023](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)
[Next postLaunch Week 7 Community Highlights14 April 2023](https://supabase.com/blog/launch-week-7-community-highlights)
[launch-week](https://supabase.com/blog/tags/launch-week)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [Get Started with dbdev](https://supabase.com/blog/dbdev#get-started-with-dbdev)
    * [Versioning](https://supabase.com/blog/dbdev#versioning)
    * [Namespaces](https://supabase.com/blog/dbdev#namespaces)
  * [Running on Supabase](https://supabase.com/blog/dbdev#running-on-supabase)
  * [Package Highlights](https://supabase.com/blog/dbdev#package-highlights)
    * [burggraf-pg_headerkit](https://supabase.com/blog/dbdev#burggraf-pg_headerkit)
    * [olirice-index_advisor](https://supabase.com/blog/dbdev#olirice-index_advisor)
    * [michelp-adminpack](https://supabase.com/blog/dbdev#michelp-adminpack)
  * [Limitations](https://supabase.com/blog/dbdev#limitations)
  * [Please Give Feedback](https://supabase.com/blog/dbdev#please-give-feedback)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdbdev&text=dbdev%3A%20PostgreSQL%20Package%20Manager)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdbdev&text=dbdev%3A%20PostgreSQL%20Package%20Manager)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdbdev&t=dbdev%3A%20PostgreSQL%20Package%20Manager)
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
![db dev landing page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-one-more-thing%2Fdbdev-landing.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

