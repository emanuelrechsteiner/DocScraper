---
url: https://supabase.com/docs/guides/ai/integrations/llamaindex
scraped_at: 2025-05-25T09:26:11.356590
title: Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications. | Supabase Docs
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
  2. Third-Party Tools
  3. [LlamaIndex](https://supabase.com/docs/guides/ai/integrations/llamaindex)


Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications.
Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications.
This guide will walk you through a basic example using the LlamaIndex [`SupabaseVectorStore`](https://github.com/supabase/supabase/blob/master/examples/ai/llamaindex/llamaindex.ipynb).
## Project setup[#](https://supabase.com/docs/guides/ai/integrations/llamaindex#project-setup)
Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:
  1. [Create a new project](https://database.new/) in the Supabase dashboard.
  2. Enter your project details. Remember to store your password somewhere safe.


Your database will be available in less than a minute.
**Finding your credentials:**
You can find your project credentials on the dashboard:
  * [Database connection strings](https://supabase.com/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
  * [Database password](https://supabase.com/dashboard/project/_/settings/database): Reset database password here if you do not have it.
  * [API credentials](https://supabase.com/dashboard/project/_/settings/api): your serverless API URL and `anon` / `service_role` keys.


## Launching a notebook[#](https://supabase.com/docs/guides/ai/integrations/llamaindex#launching-a-notebook)
Launch our [LlamaIndex](https://github.com/supabase/supabase/blob/master/examples/ai/llamaindex/llamaindex.ipynb) notebook in Colab:
[![](https://supabase.com/docs/img/ai/colab-badge.svg)](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/llamaindex/llamaindex.ipynb)
At the top of the notebook, you'll see a button `Copy to Drive`. Click this button to copy the notebook to your Google Drive.
## Fill in your OpenAI credentials[#](https://supabase.com/docs/guides/ai/integrations/llamaindex#fill-in-your-openai-credentials)
Inside the Notebook, add your `OPENAI_API_KEY` key. Find the cell which contains this code:
```

1
2
import osos.environ['OPENAI_API_KEY']="[your_openai_api_key]"

```

## Connecting to your database[#](https://supabase.com/docs/guides/ai/integrations/llamaindex#connecting-to-your-database)
Inside the Notebook, find the cell which specifies the `DB_CONNECTION`. It will contain some code like this:
```

1
2
3
4
DB_CONNECTION="postgresql://<user>:<password>@<host>:<port>/<db_name>"# create vector store clientvx = vecs.create_client(DB_CONNECTION)

```

Replace the `DB_CONNECTION` with your own connection string. You can find the connection string on your project dashboard by clicking [Connect](https://supabase.com/dashboard/project/_?showConnect=true).
SQLAlchemy requires the connection string to start with `postgresql://` (instead of `postgres://`). Don't forget to rename this after copying the string from the dashboard.
You must use the "connection pooling" string (domain ending in `*.pooler.supabase.com`) with Google Colab since Colab does not support IPv6.
## Stepping through the notebook[#](https://supabase.com/docs/guides/ai/integrations/llamaindex#stepping-through-the-notebook)
Now all that's left is to step through the notebook. You can do this by clicking the "execute" button (`ctrl+enter`) at the top left of each code cell. The notebook guides you through the process of creating a collection, adding data to it, and querying it.
You can view the inserted items in the [Table Editor](https://supabase.com/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.
![Colab documents](https://supabase.com/docs/img/ai/google-colab/colab-documents.png)
## Resources[#](https://supabase.com/docs/guides/ai/integrations/llamaindex#resources)
  * Visit the LlamaIndex + `SupabaseVectorStore` [docs](https://gpt-index.readthedocs.io/en/latest/examples/vector_stores/SupabaseVectorIndexDemo.html)
  * Visit the official LlamaIndex [repo](https://github.com/jerryjliu/llama_index/)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/ai/integrations/llamaindex.mdx)
### Is this helpful?
No Yes
### On this page
[Project setup](https://supabase.com/docs/guides/ai/integrations/llamaindex#project-setup)[Launching a notebook](https://supabase.com/docs/guides/ai/integrations/llamaindex#launching-a-notebook)[Fill in your OpenAI credentials](https://supabase.com/docs/guides/ai/integrations/llamaindex#fill-in-your-openai-credentials)[Connecting to your database](https://supabase.com/docs/guides/ai/integrations/llamaindex#connecting-to-your-database)[Stepping through the notebook](https://supabase.com/docs/guides/ai/integrations/llamaindex#stepping-through-the-notebook)[Resources](https://supabase.com/docs/guides/ai/integrations/llamaindex#resources)
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



