---
url: https://supabase.com/blog/python-support
scraped_at: 2025-05-25T09:44:35.244319
title: Supabase Python
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
# Supabase Python
16 Aug 2024
•
6 minute read
[![Guilherme Souza avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgrdsdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Guilherme SouzaEngineering](https://github.com/grdsdev)
![Supabase Python](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fthumb_python.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
As the Supabase community has grown, so has demand for a diverse collection of client libraries and framework specific SDKs. This demand for the most part has been serviced by the open source community itself, which currently maintains [dozens of libraries](https://github.com/supabase-community/#client-libraries).
When folks make requests to the hosted Supabase service we're able to build up a good picture of how broadly some of these libraries are used, and when a particular library achieves broad adoption it makes sense for us to add official support for it. Examples of libraries that have made the leap from community supported to officially supported include [supabase-flutter](https://github.com/supabase/supabase-flutter) and [supabase-swift](https://github.com/supabase/supabase-swift/).
There has always been incredible community support for the Python client libraries, over the last year and a half however we've seen a huge surge in adoption. This has been driven by the broad adoption of Supabase in the AI and ML community, many of whom are keen Pythonistas.
So today, we're announcing that the following Python Client Libraries are now officially supported on the Supabase platform:
  * [supabase-py](https://github.com/supabase/supabase-py)
  * [auth-py](https://github.com/supabase/auth-py)
  * [storage-py](https://github.com/supabase/storage-py)
  * [functions-py](https://github.com/supabase/functions-py)
  * [realtime-py](https://github.com/supabase/realtime-py)


[supabase-py](https://github.com/supabase/supabase-py) was originally started by maintainer [lqmanh](https://github.com/lqmanh) in September of 2020, and was shortly after joined by [fedden](https://github.com/fedden) and [J0](https://github.com/J0) (who went on to become a full time member of the Supabase Team). In recent years development has been driven by [silentworks](https://github.com/silentworks) and [juancarlospaco](https://github.com/juancarlospaco) who have both been instrumental in the push to reaching feature parity with [supabase-js](https://github.com/supabase/supabase-js).
Thank you so much to everyone who has contributed to the client libs so far and hopefully we'll see more community libs making the push for official support in the future.
Below is an overview of some recent features added to the collection of Python libs.
## Enabled HTTP2 by default[#](https://supabase.com/blog/python-support#enabled-http2-by-default)
Supabase clients will automatically use HTTP 2.0 when available by default, offering a seamless performance boost to your existing applications.
This improvement is implemented in a completely transparent way, and requires no changes to your existing code, while potentially delivering significant latency reduction and performance enhancements.
See also:
  * <https://github.com/supabase/functions-py/pull/115>
  * <https://github.com/supabase/auth-py/pull/534>
  * <https://github.com/supabase/postgrest-py/pull/462>
  * <https://github.com/supabase/storage-py/pull/271>


## Follow redirects by default[#](https://supabase.com/blog/python-support#follow-redirects-by-default)
Supabase clients now automatically follow all HTTP redirects by default, aligning with the behavior of Supabase clients in other programming languages.
This enhancement improves consistency across the ecosystem and simplifies the handling of redirects, reducing the need for manual intervention in common scenarios like URL changes or load balancing.
See also:
  * <https://github.com/supabase/postgrest-py/pull/449>
  * <https://github.com/supabase/functions-py/pull/107>
  * <https://github.com/supabase/storage-py/pull/257>
  * <https://github.com/supabase/auth-py/pull/511>


## Keep-alive enabled by default[#](https://supabase.com/blog/python-support#keep-alive-enabled-by-default)
Supabase clients now automatically include a `keep-alive` HTTP header by default, that was sometimes missing, addressing this inconsistency in previous versions.
This enhancement optimizes connection management, potentially reducing latency, and improving performance by maintaining persistent connections with the server, especially beneficial for applications making very frequent API calls.
## Edge Functions Regions[#](https://supabase.com/blog/python-support#edge-functions-regions)
Added support for specifying the region that the edge function will run on (a region is basically a physical location in the world).
See also:
  * <https://github.com/supabase/functions-py/pull/126>


## Realtime V2[#](https://supabase.com/blog/python-support#realtime-v2)
Realtime has been upgraded to version `2.0` with lots of improvements and fixes, including updated examples and the new Presence-related features (broadcast, subscribe, track, etc).
See also:
  * <https://github.com/supabase/realtime-py/pull/139>
  * <https://github.com/supabase/realtime-py/pull/178>


## Auth improvements[#](https://supabase.com/blog/python-support#auth-improvements)
Anonymous logins have been added to the Auth client, including a new `is_anonymous` boolean property that has been added to the class `User`, also `sign_in_with_id_token()` and `sign_in_with_sso()` methods have been added to the Auth Client, among a lot of other bug fixes.
See also:
  * <https://github.com/supabase/auth-py/pull/528>
  * <https://github.com/supabase/auth-py/pull/548>
  * <https://github.com/supabase/auth-py/pull/553>
  * <https://github.com/supabase/auth-py/pull/506>


## Postgrest quoting/escaping in queries[#](https://supabase.com/blog/python-support#postgrest-quotingescaping-in-queries)
Supabase improved PostgreSQL query safety by implementing `sanitize_param()` for parameter sanitization in internal SQL queries on the client-side, ensuring more secure data handling and query execution across all operations.
## Running with unverified SSL[#](https://supabase.com/blog/python-support#running-with-unverified-ssl)
Some users need to run the Supabase clients with invalid or unverified SSL for whatever reason (SSL debuggers/tracers/profilers/etc in development environments), a new optional boolean argument was added to the constructors of the clients, then passing `verify=False` enables it to run with unverified SSL without warnings.
`
1
from postgrest import SyncPostgrestClient
23
url: str = "https://example.com"
4
h: dict = {"Custom-Header": "value"}
56
with SyncPostgrestClient(url, schema="pub", headers=h, verify = False) as client:
7
  session = client.session
8
  assert session.base_url == "https://example.com"
`
See also:
  * <https://github.com/supabase/functions-py/pull/106>
  * <https://github.com/supabase/storage-py/pull/256>
  * <https://github.com/supabase/auth-py/pull/506>
  * <https://github.com/supabase/postgrest-py/pull/448>
  * <https://github.com/supabase/supabase-py/pull/813>


## Close socket in Realtime[#](https://supabase.com/blog/python-support#close-socket-in-realtime)
The Supabase Realtime library now includes a new `close()` method for closing the socket connections.
This addition provides developers with finer control over the connection lifecycle, allowing explicit closing of the socket connections when needed.
`
1
import os
2
from realtime import AsyncRealtimeClient
34
def callback1(payload):
5
  print("Callback 1: ", payload)
67
SUPABASE_ID: str = os.environ.get("SUPABASE_ID")
8
API_KEY: str = os.environ.get("SUPABASE_KEY")
910
URL: str = f"wss://{SUPABASE_ID}.supabase.co/realtime/v1/websocket"
1112
client = AsyncRealtimeClient(URL, API_KEY)
13
await client.connect()
1415
channel_1 = s.channel("realtime:public:sample")
16
channel_1.subscribe().on_postgres_changes("INSERT", callback1)
1718
await client.listen()
19
await client.close()
`
See also:
  * <https://github.com/supabase-community/realtime-py/pull/142>


## Edge Functions timeouts[#](https://supabase.com/blog/python-support#edge-functions-timeouts)
Timeouts for Edge Functions are now fixed and long-running functions finish correctly, there is no longer a library client-side internal timeout cutting off the functions.
Users can now confidently implement more complex operations in Edge Functions.
`
1
import os
2
from supabase import create_client
3
from supabase.lib.client_options import ClientOptions
45
url: str = os.environ.get("SUPABASE_URL")
6
key: str = os.environ.get("SUPABASE_KEY")
78
options = ClientOptions(function_client_timeout = 15)
9
client = create_client(url, key, options)
1011
client.functions.url = "http://127.0.0.1:54321/functions/v1/hello-world"
12
print(client.functions.invoke("hello"))
`
See also:
  * <https://github.com/supabase/functions-py/pull/120>
  * <https://github.com/supabase/supabase-py/pull/846>


## New tool Vec2pg to migrate data to Supabase[#](https://supabase.com/blog/python-support#new-tool-vec2pg-to-migrate-data-to-supabase)
A new simple and extensible CLI tool to migrate vector data from other services and SASS into Supabase was created, it can migrate vector data from Pinecone and Qdrant into Supabase with a single command, streamlining workflows and enhancing data portability across AI and ML projects.
You can vote for other vector database providers to be added in the future!
See also:
  * <https://github.com/supabase-community/vec2pg>
  * <https://github.com/supabase-community/vec2pg/pull/5>
  * <https://github.com/supabase-community/vec2pg/issues/6>


## Updated CI[#](https://supabase.com/blog/python-support#updated-ci)
Continuous Integration builds for all the libraries have been upgraded and made more strict (linters, etc).
See also:
  * <https://github.com/supabase/supabase-py/pull/772>
  * <https://github.com/supabase/supabase-py/pull/774>
  * <https://github.com/supabase/functions-py/pull/93>
  * <https://github.com/supabase/functions-py/pull/92>
  * <https://github.com/supabase/storage-py/pull/240>
  * <https://github.com/supabase/storage-py/pull/237>
  * <https://github.com/supabase/realtime-py/pull/132>
  * <https://github.com/supabase/realtime-py/pull/131>
  * <https://github.com/supabase/postgrest-py/pull/424>
  * <https://github.com/supabase/postgrest-py/pull/422>
  * <https://github.com/supabase/functions-py/pull/139>
  * <https://github.com/supabase/storage-py/pull/287>
  * <https://github.com/supabase/auth-py/pull/572>
  * <https://github.com/supabase/postgrest-py/pull/484>
  * <https://github.com/supabase/supabase-py/pull/887>
  * <https://github.com/supabase/realtime-py/pull/182>


## Miscellaneous[#](https://supabase.com/blog/python-support#miscellaneous)
  * Unittests coverage was improved across all code repositories.
  * Cyclomatic complexity has been analyzed and improved in all the libraries (mccabe, prospector).
  * Multiple fixes for code style, symbol naming, documentation, comments, and docstrings.


## Contributing[#](https://supabase.com/blog/python-support#contributing)
If you'd like to get involved in contributing to our Python client libraries see [here](https://github.com/supabase/supabase-py/blob/main/CONTRIBUTING.md) for some information on how to contribute, and check the list of [open issues](https://github.com/supabase/supabase-py/issues) for some inspiration on what to work on.
## Getting started[#](https://supabase.com/blog/python-support#getting-started)
Full documentation is available for the Supabase Python Client libraries on the [Supabase Docs site](https://supabase.com/docs/reference/python/introduction).
[Launch Week12](https://supabase.com/launch-week/12)
12-16 August
[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage
[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)[02 -pg_replicate](https://news.ycombinator.com/item?id=41209994)[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)[06 -vec2pg](https://supabase.com/blog/vec2pg)[07 -pg_graphql](https://supabase.com/blog/pg-graphql-1-5-7)[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)[09 -python-support](https://supabase.com/blog/python-support)[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&text=Supabase%20Python)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&text=Supabase%20Python)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&t=Supabase%20Python)
[Last postPostgREST 12.2: Prometheus metrics16 August 2024](https://supabase.com/blog/postgrest-12-2)
[Next postThe Supabase Book by David Lorenz16 August 2024](https://supabase.com/blog/supabase-book-by-david-lorenz)
[launch-week](https://supabase.com/blog/tags/launch-week)[database](https://supabase.com/blog/tags/database)
On this page
  * [Enabled HTTP2 by default](https://supabase.com/blog/python-support#enabled-http2-by-default)
  * [Follow redirects by default](https://supabase.com/blog/python-support#follow-redirects-by-default)
  * [Keep-alive enabled by default](https://supabase.com/blog/python-support#keep-alive-enabled-by-default)
  * [Edge Functions Regions](https://supabase.com/blog/python-support#edge-functions-regions)
  * [Realtime V2](https://supabase.com/blog/python-support#realtime-v2)
  * [Auth improvements](https://supabase.com/blog/python-support#auth-improvements)
  * [Postgrest quoting/escaping in queries](https://supabase.com/blog/python-support#postgrest-quotingescaping-in-queries)
  * [Running with unverified SSL](https://supabase.com/blog/python-support#running-with-unverified-ssl)
  * [Close socket in Realtime](https://supabase.com/blog/python-support#close-socket-in-realtime)
  * [Edge Functions timeouts](https://supabase.com/blog/python-support#edge-functions-timeouts)
  * [New tool Vec2pg to migrate data to Supabase](https://supabase.com/blog/python-support#new-tool-vec2pg-to-migrate-data-to-supabase)
  * [Updated CI](https://supabase.com/blog/python-support#updated-ci)
  * [Miscellaneous](https://supabase.com/blog/python-support#miscellaneous)
  * [Contributing](https://supabase.com/blog/python-support#contributing)
  * [Getting started](https://supabase.com/blog/python-support#getting-started)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&text=Supabase%20Python)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&text=Supabase%20Python)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpython-support&t=Supabase%20Python)
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

