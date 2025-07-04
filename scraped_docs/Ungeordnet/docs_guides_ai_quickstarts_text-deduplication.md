---
url: https://supabase.com/docs/guides/ai/quickstarts/text-deduplication
scraped_at: 2025-05-25T09:04:07.735674
title: Semantic Text Deduplication | Supabase Docs
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
  3. [Text Deduplication](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication)


Semantic Text Deduplication
Finding duplicate movie reviews with Supabase Vecs.
This guide will walk you through a ["Semantic Text Deduplication"](https://github.com/supabase/supabase/blob/master/examples/ai/semantic_text_deduplication.ipynb) example using Colab and Supabase Vecs. You'll learn how to find similar movie reviews using embeddings, and remove any that seem like duplicates. You will:
  1. Launch a Postgres database that uses pgvector to store embeddings
  2. Launch a notebook that connects to your database
  3. Load the IMDB dataset
  4. Use the `sentence-transformers/all-MiniLM-L6-v2` model to create an embedding representing the semantic meaning of each review.
  5. Search for all duplicates.


## Project setup[#](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#project-setup)
Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:
  1. [Create a new project](https://database.new/) in the Supabase dashboard.
  2. Enter your project details. Remember to store your password somewhere safe.


Your database will be available in less than a minute.
**Finding your credentials:**
You can find your project credentials on the dashboard:
  * [Database connection strings](https://supabase.com/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
  * [Database password](https://supabase.com/dashboard/project/_/settings/database): Reset database password here if you do not have it.
  * [API credentials](https://supabase.com/dashboard/project/_/settings/api): your serverless API URL and `anon` / `service_role` keys.


## Launching a notebook[#](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#launching-a-notebook)
Launch our [`semantic_text_deduplication`](https://github.com/supabase/supabase/blob/master/examples/ai/semantic_text_deduplication.ipynb) notebook in Colab:
[![](https://supabase.com/docs/img/ai/colab-badge.svg)](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/semantic_text_deduplication.ipynb)
At the top of the notebook, you'll see a button `Copy to Drive`. Click this button to copy the notebook to your Google Drive.
## Connecting to your database[#](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#connecting-to-your-database)
Inside the Notebook, find the cell which specifies the `DB_CONNECTION`. It will contain some code like this:
```

1
2
3
4
5
6
import vecsDB_CONNECTION="postgresql://<user>:<password>@<host>:<port>/<db_name>"# create vector store clientvx = vecs.create_client(DB_CONNECTION)

```

Replace the `DB_CONNECTION` with your own connection string. You can find the connection string on your project dashboard by clicking [Connect](https://supabase.com/dashboard/project/_?showConnect=true).
SQLAlchemy requires the connection string to start with `postgresql://` (instead of `postgres://`). Don't forget to rename this after copying the string from the dashboard.
You must use the "connection pooling" string (domain ending in `*.pooler.supabase.com`) with Google Colab since Colab does not support IPv6.
## Stepping through the notebook[#](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#stepping-through-the-notebook)
Now all that's left is to step through the notebook. You can do this by clicking the "execute" button (`ctrl+enter`) at the top left of each code cell. The notebook guides you through the process of creating a collection, adding data to it, and querying it.
You can view the inserted items in the [Table Editor](https://supabase.com/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.
![Colab documents](https://supabase.com/docs/img/ai/google-colab/colab-documents.png)
## Deployment[#](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#deployment)
If you have your own infrastructure for deploying Python apps, you can continue to use `vecs` as described in this guide.
Alternatively if you would like to quickly deploy using Supabase, check out our guide on using the [Hugging Face Inference API](https://supabase.com/docs/guides/ai/hugging-face) in Edge Functions using TypeScript.
## Next steps[#](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#next-steps)
You can now start building your own applications with Vecs. Check our [examples](https://supabase.com/docs/guides/ai#examples) for ideas.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/ai/quickstarts/text-deduplication.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#project-setup)[Launching a notebook](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#launching-a-notebook)[Connecting to your database](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#connecting-to-your-database)[Stepping through the notebook](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#stepping-through-the-notebook)[Deployment](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#deployment)[Next steps](https://supabase.com/docs/guides/ai/quickstarts/text-deduplication#next-steps)
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



