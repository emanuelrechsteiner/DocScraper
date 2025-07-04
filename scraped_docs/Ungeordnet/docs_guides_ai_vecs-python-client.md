---
url: http://supabase.com/docs/guides/ai/vecs-python-client
scraped_at: 2025-05-25T09:49:01.771936
title: Python client | Supabase Docs
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
[AI & Vectors](https://supabase.com/docs/guides/ai)
  * [Overview](https://supabase.com/docs/guides/ai)
  * [Concepts](https://supabase.com/docs/guides/ai/concepts)
  * [Structured & unstructured](https://supabase.com/docs/guides/ai/structured-unstructured)
Learn
  * [Vector columns](https://supabase.com/docs/guides/ai/vector-columns)
  * [Vector indexes](https://supabase.com/docs/guides/ai/vector-indexes)
  * [Automatic embeddings](https://supabase.com/docs/guides/ai/automatic-embeddings)
  * [Engineering for scale](https://supabase.com/docs/guides/ai/engineering-for-scale)
  * [Choosing Compute Add-on](https://supabase.com/docs/guides/ai/choosing-compute-addon)
  * [Going to Production](https://supabase.com/docs/guides/ai/going-to-prod)
  * [RAG with Permissions](https://supabase.com/docs/guides/ai/rag-with-permissions)
Search
  * [Semantic search](https://supabase.com/docs/guides/ai/semantic-search)
  * [Keyword search](https://supabase.com/docs/guides/ai/keyword-search)
  * [Hybrid search](https://supabase.com/docs/guides/ai/hybrid-search)
JavaScript Examples
  * [OpenAI completions using Edge Functions](https://supabase.com/docs/guides/ai/examples/openai)
  * [Generate image captions using Hugging Face](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning)
  * [Generate Embeddings](https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings)
  * [Adding generative Q&A to your documentation](https://supabase.com/docs/guides/ai/examples/headless-vector-search)
  * [Adding generative Q&A to your Next.js site](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search)
Python Client
  * [Choosing a Client](https://supabase.com/docs/guides/ai/python-clients)
  * [API](https://supabase.com/docs/guides/ai/python/api)
  * [Collections](https://supabase.com/docs/guides/ai/python/collections)
  * [Indexes](https://supabase.com/docs/guides/ai/python/indexes)
  * [Metadata](https://supabase.com/docs/guides/ai/python/metadata)
Python Examples
  * [Developing locally with Vecs](https://supabase.com/docs/guides/ai/vecs-python-client)
  * [Creating and managing collections](https://supabase.com/docs/guides/ai/quickstarts/hello-world)
  * [Text Deduplication](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication)
  * [Face similarity search](https://supabase.com/docs/guides/ai/quickstarts/face-similarity)
  * [Image search with OpenAI CLIP](https://supabase.com/docs/guides/ai/examples/image-search-openai-clip)
  * [Semantic search with Amazon Titan](https://supabase.com/docs/guides/ai/examples/semantic-image-search-amazon-titan)
  * [Building ChatGPT Plugins](https://supabase.com/docs/guides/ai/examples/building-chatgpt-plugins)
Third-Party Tools
  * [LangChain](https://supabase.com/docs/guides/ai/langchain)
  * [Hugging Face](https://supabase.com/docs/guides/ai/hugging-face)
  * [Google Colab](https://supabase.com/docs/guides/ai/google-colab)
  * [LlamaIndex](https://supabase.com/docs/guides/ai/integrations/llamaindex)
  * [Roboflow](https://supabase.com/docs/guides/ai/integrations/roboflow)
  * [Amazon Bedrock](https://supabase.com/docs/guides/ai/integrations/amazon-bedrock)
  * [Mixpeek](https://supabase.com/docs/guides/ai/examples/mixpeek-video-search)


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
AI & Vectors
  1. [AI & Vectors](https://supabase.com/docs/guides/ai)
  2. Python Examples
  3. [Developing locally with Vecs](https://supabase.com/docs/guides/ai/vecs-python-client)


Python client
Manage unstructured vector stores in PostgreSQL.
Supabase provides a Python client called [`vecs`](https://github.com/supabase/vecs) for managing unstructured vector stores. This client provides a set of useful tools for creating and querying collections in Postgres using the [pgvector](https://supabase.com/docs/guides/database/extensions/pgvector) extension.
## Quick start[#](https://supabase.com/docs/guides/ai/vecs-python-client#quick-start)
Let's see how Vecs works using a local database. Make sure you have the Supabase CLI [installed](https://supabase.com/docs/guides/cli#installation) on your machine.
### Initialize your project[#](https://supabase.com/docs/guides/ai/vecs-python-client#initialize-your-project)
Start a local Postgres instance in any folder using the `init` and `start` commands. Make sure you have Docker running!
```

1
2
3
4
5
# Initialize your projectsupabaseinit# Start Postgressupabasestart

```

### Create a collection[#](https://supabase.com/docs/guides/ai/vecs-python-client#create-a-collection)
Inside a Python shell, run the following commands to create a new collection called "docs", with 3 dimensions.
```

1
2
3
4
5
6
7
import vecs# create vector store clientvx = vecs.create_client("postgresql://postgres:postgres@localhost:54322/postgres")# create a collection of vectors with 3 dimensionsdocs = vx.get_or_create_collection(name="docs",dimension=3)

```

### Add embeddings[#](https://supabase.com/docs/guides/ai/vecs-python-client#add-embeddings)
Now we can insert some embeddings into our "docs" collection using the `upsert()` command:
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
import vecs# create vector store clientdocs = vecs.get_or_create_collection(name="docs",dimension=3)# a collection of vectors with 3 dimensionsvectors=[("vec0",[0.1,0.2,0.3],{"year":1973}),("vec1",[0.7,0.8,0.9],{"year":2012})]# insert our vectorsdocs.upsert(vectors=vectors)

```

### Query the collection[#](https://supabase.com/docs/guides/ai/vecs-python-client#query-the-collection)
You can now query the collection to retrieve a relevant match:
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
import vecsdocs = vecs.get_or_create_collection(name="docs",dimension=3)# query the collection filtering metadata for "year" = 2012docs.query(data=[0.4,0.5,0.6],# requiredlimit=1,# number of records to returnfilters={"year":{"$eq":2012}},# metadata filters)

```

## Deep dive[#](https://supabase.com/docs/guides/ai/vecs-python-client#deep-dive)
For a more in-depth guide on `vecs` collections, see [API](https://supabase.com/docs/guides/ai/python/api).
## Resources[#](https://supabase.com/docs/guides/ai/vecs-python-client#resources)
  * Official Vecs Documentation: <https://supabase.github.io/vecs/api>
  * Source Code: <https://github.com/supabase/vecs>

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/ai/vecs-python-client.mdx)
### Is this helpful?
No Yes
### On this page
[Quick start](https://supabase.com/docs/guides/ai/vecs-python-client#quick-start)[Initialize your project](https://supabase.com/docs/guides/ai/vecs-python-client#initialize-your-project)[Create a collection](https://supabase.com/docs/guides/ai/vecs-python-client#create-a-collection)[Add embeddings](https://supabase.com/docs/guides/ai/vecs-python-client#add-embeddings)[Query the collection](https://supabase.com/docs/guides/ai/vecs-python-client#query-the-collection)[Deep dive](https://supabase.com/docs/guides/ai/vecs-python-client#deep-dive)[Resources](https://supabase.com/docs/guides/ai/vecs-python-client#resources)
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



