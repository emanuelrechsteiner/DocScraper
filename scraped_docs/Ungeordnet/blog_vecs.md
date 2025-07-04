---
url: https://supabase.com/blog/vecs
scraped_at: 2025-05-25T08:42:46.158957
title: Supabase Vecs: a vector client for Postgres
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
# Supabase Vecs: a vector client for Postgres
29 May 2023
•
6 minute read
[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Oliver RiceEngineering](https://github.com/olirice)
![Supabase Vecs: a vector client for Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-06-01-vecs%2Fog-image.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Vecs](https://github.com/supabase/vecs) is a new Python library for managing embeddings in your Postgres database with the pgvector extension.
It handles:
  * Creating and indexing tables
  * Querying vectors by cosine distance, l2 distance, and max inner dot product
  * Filtering based on user-defined metadata


## Goals[#](https://supabase.com/blog/vecs#goals)
Our goal for `vecs` is to provide an interface that lets Postgres + pgvector look and feel like a dedicated vector store. It works with any Postgres database (or platform) that [supports pgvector](https://github.com/pgvector/pgvector/issues/54). It was designed with ease-of-use, interactivity, and exploratory data analysis in mind, but works equally well as a search workhorse.
If you're interested in the nuts and bolts of what's going on, it's trivial to drop into the SQL layer and see what's happening. Alternatively, folks who don't want to know what's happening in the database, don't need to care.
## Usage[#](https://supabase.com/blog/vecs#usage)
`Vecs` makes it easy to create a collection (table) and insert a few records - just 5 lines of code.
### Connecting[#](https://supabase.com/blog/vecs#connecting)
`
1
import vecs
23
DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"
45
# create vector store client
6
vx = vecs.create_client(DB_CONNECTION)
78
# create a collection of vectors with 3 dimensions
9
docs = vx.get_or_create_collection(name="docs", dimension=3)
`
The `get_or_create_collection` call sets up a table in the Postgres database specified by `DB_CONNECTION` in a schema named `vecs` with the user defined name `docs`.
Or, more specifically:
`
1
create table vecs.docs (
2
  id text primary key,
3
  vec vector(3) not null,
4
  metadata jsonb not null default '{}'::jsonb
5
);
`
### Insert/Update[#](https://supabase.com/blog/vecs#insertupdate)
We can insert a few records in that new SQL table/vecs collection using `Collection.upsert`.
`
1
# add records to the collection
2
docs.upsert(
3
  vectors=[
4
    (
5
     "vec0",      # the records user defined identifier
6
     [0.1, 0.2, 0.3], # the vector. A list or np.array
7
     {"year": 1973}  # associated metadata
8
    )
9
  ]
10
)
`
which will add the records to our table if the `id` `"vec0"` does not exist, or updates the existing record if it does exist.
### Query[#](https://supabase.com/blog/vecs#query)
You can query a vecs collection at any time without an index, but it's a best practices to create an index on your collection after inserting data.
`
1
docs.index()
`
Where `index` optionally takes an argument for the distance measure to index.
Finally, we can search the collection for similar vectors using the `query` method:
`
1
docs.query(
2
  query_vector=[0.10,0.21,0.29],  # required
3
  limit=1,             # (optional) number of records to return
4
  filters={"year": {"$eq": 1973}}, # (optional) metadata filters
5
  measure="cosine_distance",    # (optional) distance measure to use
6
  include_value=False,       # (optional) should distance measure values be returned?
7
  include_metadata=False,     # (optional) should record metadata be returned?
8
)
`
Which returns:
`
1
[("vec1", 0.000697, {"year": 1973})]
`
Since all metadata is stored in a `jsonb` column, there's a [lightweight but flexible DSL](https://supabase.github.io/vecs/concepts_metadata/) wrapped around it for filtering.
When you're done, disconnect with:
`
1
vx.disconnect()
`
And 90% of the time, that minimal interface is all you'll need to touch.
For more in-depth information about `vecs`, checkout the [API Quickstart](https://supabase.github.io/vecs/api/), [celebrity look-alike demo](https://github.com/supabase/supabase/blob/be1f4ea85e10cc8134e389dcdbe6a092b08612f1/examples/ai/face_similarity.ipynb), or [OpenAI integration example](https://supabase.github.io/vecs/integrations_openai/)
## Deploying with Supabase[#](https://supabase.com/blog/vecs#deploying-with-supabase)
As usual, if you combine [supabase/vecs](https://github.com/supabase/vecs) with the rest of Supabase, you get more than the sum of the parts. Once you're happy with your vecs collection, you can make it accessible to your front-end through a supabase client library by exposing the collection as a view in your public schema.
![Expose with view](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-06-01-vecs%2Fsingle-database.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
For example, you could create a view
`
1
create view public.docs as
2
  select
3
    id,
4
    embedding,
5
    metadata, # Expose the metadata as JSON
6
    (metadata->>'url')::text as url # Extract the URL as a string
7
  from
8
    vecs.docs
`
And then access it with the supabase-js client library within your applications:
`
1
const { data, error } = await supabase
2
 .from('docs')
3
 .select('id, embedding, metadata')
4
 .eq('url', '/hello-world')
`
For more deployment options, including enterprise scalable architecture, check out the [engineering for scale guide](https://supabase.com/docs/guides/ai/engineering-for-scale#simple-workloads).
## Future ideas[#](https://supabase.com/blog/vecs#future-ideas)
Currently, `vecs` is unopinionated about where vectors come from or how they're produced. While there will always be a need for generic vector storage and querying, it's becoming clear that text and image vectorization make up +95% of usage. That gives us the opportunity to streamline those workflows for users.
One option we're exploring is to optionally assign transformation pipelines to collections along the lines of:
`
1
# This is mock code only, not currently functional
23
docs: Collection =vx.get_or_create_collection(
4
  docs='docs',
5
  dimension=512,
6
  transform = TextPreprocessor( # this is new
7
    model="sentence-transformers/all-Mini-L6-v2"
8
  )
9
)
1011
docs.upsert([
12
  ("id_0", "# Some markdown", {}),
13
  ("id_1", "# Some more markdown", {})
14
])
`
so users can choose to work with their preferred media type without ever thinking about vectors.
Another direction we're considering is adding an async client to avoid blocking when waiting on the database or network i.e.
`
1
# This is mock code only, not currently functional
23
await docs.upsert([
4
  ("id_0", [0.1, 0.2, 0.3], {}),
5
])
`
Both possibilities are still up for debate. If you have view on either, feel free to weigh in on the [Feature Request: Preprocessing Transform](https://github.com/supabase/vecs/issues/5) and [Feature Request: Async Client](https://github.com/supabase/vecs/issues/6) GitHub issues.
## More info[#](https://supabase.com/blog/vecs#more-info)
  * Source code: [github.com/supabase/vecs](https://github.com/supabase/vecs)
  * Vecs Docs: [supabase.github.io/vecs/](https://supabase.github.io/vecs/)
  * Supabase Vector Toolkit: [supabase.com/docs/guides/ai](https://supabase.com/docs/guides/ai)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&text=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&text=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&t=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)
[Last postFlutter Hackathon Winners29 May 2023](https://supabase.com/blog/flutter-hackathon-winners)
[Next postChatGPT plugins now support Postgres & Supabase25 May 2023](https://supabase.com/blog/chatgpt-plugins-support-postgres)
[postgres](https://supabase.com/blog/tags/postgres)[AI](https://supabase.com/blog/tags/AI)[python](https://supabase.com/blog/tags/python)
On this page
  * [Goals](https://supabase.com/blog/vecs#goals)
  * [Usage](https://supabase.com/blog/vecs#usage)
    * [Connecting](https://supabase.com/blog/vecs#connecting)
    * [Insert/Update](https://supabase.com/blog/vecs#insertupdate)
    * [Query](https://supabase.com/blog/vecs#query)
  * [Deploying with Supabase](https://supabase.com/blog/vecs#deploying-with-supabase)
  * [Future ideas](https://supabase.com/blog/vecs#future-ideas)
  * [More info](https://supabase.com/blog/vecs#more-info)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&text=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&text=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvecs&t=Supabase%20Vecs%3A%20a%20vector%20client%20for%20Postgres)
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

