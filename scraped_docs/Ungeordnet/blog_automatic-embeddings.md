---
url: https://supabase.com/blog/automatic-embeddings
scraped_at: 2025-05-25T08:38:23.731827
title: Automatic Embeddings in Postgres
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
# Automatic Embeddings in Postgres
01 Apr 2025
•
7 minute read
[![Greg Richardson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgregnr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Greg RichardsonEngineering](https://github.com/gregnr)
![Automatic Embeddings in Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-automatic-embeddings%2Fautomatic-embeddings-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Today we’re releasing [automatic embeddings](https://supabase.com/docs/guides/ai/automatic-embeddings) - automate embedding generation and updates using Supabase [Vector](https://supabase.com/modules/vector), [Queues](https://supabase.com/modules/queues), [Cron](https://supabase.com/modules/cron), and [pg_net](https://supabase.com/docs/guides/database/extensions/pg_net) extension, and [Edge Functions](https://supabase.com/edge-functions).
Embeddings power features like semantic search, recommendations, and retrieval-augmented generation (RAG). They represent text or other content as high-dimensional vectors. At query time, you convert the input into a vector and compare it to stored vectors to find similar items.
Postgres with [`pgvector`](https://github.com/pgvector/pgvector) already supports storing and searching over vectors. But generating and maintaining those embeddings has been left to the application. This often means building a separate pipeline just to keep vector data in sync.
Automatic embeddings bring that pipeline into the database. You can manage embedding generation using SQL, triggers, and extensions like `pgmq`, `pg_cron`, and `pg_net`. No new runtimes or services are required.
## The problem: external embedding pipelines create drift and complexity[#](https://supabase.com/blog/automatic-embeddings#the-problem-external-embedding-pipelines-create-drift-and-complexity)
Most teams implementing semantic features in Postgres end up building their own pipeline. The general pattern looks like this:
  1. Store source content (e.g. documents, tickets, articles)
  2. Generate an embedding using an external model
  3. Store the result in a vector column
  4. Re-run the embedding job if the content changes
  5. Handle retries if the model fails or times out


This pipeline is easy to describe but hard to implement. It introduces inconsistency between your source of truth (Postgres) and derived data (the embeddings). It also requires background workers, queues, observability, and external coordination.
Here are some ways this pipeline can fall apart:
  * **Drift**. If you update the content but forget to re-embed it, your search quality drops.
  * **Latency**. Some embedding APIs are slow or rate-limited. If you call them synchronously on write, you add latency to the write path.
  * **Lack of resilience**. If your background worker dies or the queue fails, you may not notice until things break.
  * **Schema duplication**. Your application ends up duplicating logic that could live in the schema.


## What are automatic embeddings?[#](https://supabase.com/blog/automatic-embeddings#what-are-automatic-embeddings)
Automatic embeddings move the vector generation step into Postgres. Not literally. Inference still happens via an external model, but the responsibility for coordinating that process becomes part of your database.
When a row is inserted or updated, Postgres can automatically enqueue a job to generate or refresh its embedding. That job runs in the background, retries if it fails, and stores the result back into the vector column.
This approach has a few benefits:
  * **No drift**. Embeddings stay in sync with content updates.
  * **Bring your own model**. You can point to any API that returns a vector.
  * **All SQL**. You can enqueue, inspect, and retry embedding jobs without leaving Postgres.


A number of use cases get easier when embeddings are automatically managed:
  * Build semantic search without leaving SQL
  * Keep embeddings fresh as data changes
  * Use vector search for deduplication or anomaly detection
  * Combine structured and semantic filters in a single query
  * Enrich or classify rows using embedding-based inheritance


## Design patterns for generating embeddings[#](https://supabase.com/blog/automatic-embeddings#design-patterns-for-generating-embeddings)
There are two approaches to automatic embeddings today:
### Generated columns[#](https://supabase.com/blog/automatic-embeddings#generated-columns)
`
1
create table documents (
2
 id uuid primary key,
3
 content text,
4
 embedding vector(1536) generated always as (embed(content)) stored
5
);
`
This uses a generated column to call an embedding function on write. It only works if your model is local and fast. In practice, this approach with the `embed()` function blocks the write path and doesn’t scale well.
### Trigger-based asynchronous embeddings[#](https://supabase.com/blog/automatic-embeddings#trigger-based-asynchronous-embeddings)
This is the pattern we use at Supabase. It uses a few common extensions:
  * SQL triggers to enqueue work when rows are inserted or updates
  * `pgmq` to enqueue embedding jobs inside a transactional message queue
  * `pg_net` to send async HTTP requests to an Edge Function (and in turn, embedding provider like OpenAI)
  * `pg_cron` to run workers that process the queue
  * `pgvector` for storing and searching over embeddings


You can inspect the queue, retry failed jobs, and customize the Edge Function used to generate embeddings. You can find the complete reference implementation in the [Supabase Automatic Embeddings Guide](https://supabase.com/docs/guides/ai/automatic-embeddings).
## How to use automatic embeddings[#](https://supabase.com/blog/automatic-embeddings#how-to-use-automatic-embeddings)
After applying the implementation from the guide, it is as easy as adding two triggers to a table.
### Set up the table[#](https://supabase.com/blog/automatic-embeddings#set-up-the-table)
First let’s create a `documents` table with an `embedding` column to store the vector.
`
1
-- Table to store documents with embeddings
2
create table documents (
3
 id integer primary key generated always as identity,
4
 title text not null,
5
 content text not null,
6
 embedding halfvec(1536),
7
 created_at timestamp with time zone default now()
8
);
910
-- Index for vector search over document embeddings
11
create index on documents using hnsw (embedding halfvec_cosine_ops);
`
### Create the embedding pipeline[#](https://supabase.com/blog/automatic-embeddings#create-the-embedding-pipeline)
Next we create an `embedding_input` function that tells the embedding generator what to use as the source content:
`
1
-- Customize the input for embedding generation
2
-- e.g. Concatenate title and content with a markdown header
3
create or replace function embedding_input(doc documents)
4
returns text
5
language plpgsql
6
immutable
7
as $$
8
begin
9
 return '# ' || doc.title || E'\n\n' || doc.content;
10
end;
11
$$;
`
This is useful for many embedding pipelines where you want your embedding to represent a combination of multiple text columns like title + content instead of a single column.
Finally we add two triggers:
`
1
-- Trigger for insert events
2
create trigger embed_documents_on_insert
3
 after insert
4
 on documents
5
 for each row
6
 execute function util.queue_embeddings('embedding_input', 'embedding');
78
-- Trigger for update events
9
create trigger embed_documents_on_update
10
 after update of title, content -- must match the columns in embedding_input()
11
 on documents
12
 for each row
13
 execute function util.queue_embeddings('embedding_input', 'embedding');
`
These ensure that embeddings are updated for both new records (inserts) and modified records (updates). Note that these triggers fire off “embedding jobs” that run asynchronously instead of blocking the write path with a long-running operation.
Under the hood, `pg_cron` will batch embedding jobs at an interval and send them off to an Edge Function to perform the actual embedding generation. The default generation logic looks something like this:
`
1
/**
2
 * Generates an embedding for the given text.
3
 */
4
async function generateEmbedding(text: string) {
5
 const response = await openai.embeddings.create({
6
  model: 'text-embedding-3-small',
7
  input: text,
8
 })
9
 const [data] = response.data
10
 if (!data) {
11
  throw new Error('failed to generate embedding')
12
 }
13
 return data.embedding
14
}
`
But you can adjust this to use any inference API and model that you prefer.
### Generate automatic embeddings and query the table[#](https://supabase.com/blog/automatic-embeddings#generate-automatic-embeddings-and-query-the-table)
Now, you can insert a new document into your table:
`
1
insert into documents (title, content)
2
values
3
 ('Understanding Vector Databases', 'Vector databases are specialized...');
`
This will kick off the embedding pipeline within a Supabase Edge Function. If you were to immediately query for the document you just inserted, the `embedding` column will be empty:
`
1
select id, embedding
2
from documents
3
where title = 'Understanding Vector Databases';
`
However, if you were to retry in a few seconds, the `embedding` column will be populated correctly. This is because the pipeline is asynchronous and the Edge Function will be working in the background to generate the embedding and store it properly.
Similarly, if you were to come back and update the row you added to the `documents` table, at first the `embedding` column will be null because the trigger initially resets it. The trigger also queues up the Edge Function that will generate and populate the `embedding` column, which should complete within seconds. This keeps your data and its associated embedding in sync.
## Conclusion[#](https://supabase.com/blog/automatic-embeddings#conclusion)
You can get started with automatic embeddings today:
  * [Read the full implementation details](https://supabase.com/docs/guides/ai/automatic-embeddings) in our docs
  * [Get started with Supabase](https://supabase.com/dashboard/sign-in?returnTo=%2Fprojects) and try it out today


[Launch Week 14](https://supabase.com/launch-week)
Mar 31 - Apr 04 '25
[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage
[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)[Community Meetups](https://supabase.com/events?category=meetup)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-embeddings&text=Automatic%20Embeddings%20in%20Postgres)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-embeddings&text=Automatic%20Embeddings%20in%20Postgres)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-embeddings&t=Automatic%20Embeddings%20in%20Postgres)
[Last postEdge Functions: Deploy from the Dashboard + Deno 2.11 April 2025](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)
[Next postIntroducing the Supabase UI Library31 March 2025](https://supabase.com/blog/supabase-ui-library)
[launch-week](https://supabase.com/blog/tags/launch-week)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [The problem: external embedding pipelines create drift and complexity](https://supabase.com/blog/automatic-embeddings#the-problem-external-embedding-pipelines-create-drift-and-complexity)
  * [What are automatic embeddings?](https://supabase.com/blog/automatic-embeddings#what-are-automatic-embeddings)
  * [Design patterns for generating embeddings](https://supabase.com/blog/automatic-embeddings#design-patterns-for-generating-embeddings)
    * [Generated columns](https://supabase.com/blog/automatic-embeddings#generated-columns)
    * [Trigger-based asynchronous embeddings](https://supabase.com/blog/automatic-embeddings#trigger-based-asynchronous-embeddings)
  * [How to use automatic embeddings](https://supabase.com/blog/automatic-embeddings#how-to-use-automatic-embeddings)
    * [Set up the table](https://supabase.com/blog/automatic-embeddings#set-up-the-table)
    * [Create the embedding pipeline](https://supabase.com/blog/automatic-embeddings#create-the-embedding-pipeline)
    * [Generate automatic embeddings and query the table](https://supabase.com/blog/automatic-embeddings#generate-automatic-embeddings-and-query-the-table)
  * [Conclusion](https://supabase.com/blog/automatic-embeddings#conclusion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-embeddings&text=Automatic%20Embeddings%20in%20Postgres)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-embeddings&text=Automatic%20Embeddings%20in%20Postgres)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fautomatic-embeddings&t=Automatic%20Embeddings%20in%20Postgres)
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

