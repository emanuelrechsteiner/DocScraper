---
url: https://supabase.com/docs/guides/ai/examples/headless-vector-search
scraped_at: 2025-05-25T08:37:24.944374
title: Adding generative Q&A for your documentation | Supabase Docs
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
  2. JavaScript Examples
  3. [Adding generative Q&A to your documentation](https://supabase.com/docs/guides/ai/examples/headless-vector-search)


Adding generative Q&A for your documentation
Learn how to build a ChatGPT-style doc search powered using our headless search toolkit.
Supabase provides a [Headless Search Toolkit](https://github.com/supabase/headless-vector-search) for adding "Generative Q&A" to your documentation. The toolkit is "headless", so that you can integrate it into your existing website and style it to match your website theme.
You can see how this works with the Supabase docs. Just hit `cmd+k` and "ask" for something like "what are the features of Supabase?". You will see that the response is streamed back, using the information provided in the docs:
![headless search](https://supabase.com/docs/img/ai/headless-search/headless.png)
## Tech stack[#](https://supabase.com/docs/guides/ai/examples/headless-vector-search#tech-stack)
  * Supabase: Database & Edge Functions.
  * OpenAI: Embeddings and completions.
  * GitHub Actions: for ingesting your markdown docs.


## Toolkit[#](https://supabase.com/docs/guides/ai/examples/headless-vector-search#toolkit)
This toolkit consists of 2 parts:
  * The [Headless Vector Search](https://github.com/supabase/headless-vector-search) template which you can deploy in your own organization.
  * A [GitHub Action](https://github.com/supabase/embeddings-generator) which will ingest your markdown files, convert them to embeddings, and store them in your database.


## Usage[#](https://supabase.com/docs/guides/ai/examples/headless-vector-search#usage)
There are 3 steps to build similarity search inside your documentation:
  1. Prepare your database.
  2. Ingest your documentation.
  3. Add a search interface.


### Prepare your database[#](https://supabase.com/docs/guides/ai/examples/headless-vector-search#prepare-your-database)
To prepare, create a [new Supabase project](https://database.new) and store the database and API credentials, which you can find in the project [settings](https://supabase.com/dashboard/project/_/settings).
Now we can use the [Headless Vector Search](https://github.com/supabase/headless-vector-search#set-up) instructions to set up the database:
  1. Clone the repo to your local machine: `git clone git@github.com:supabase/headless-vector-search.git`
  2. Link the repo to your remote project: `supabase link --project-ref XXX`
  3. Apply the database migrations: `supabase db push`
  4. Set your OpenAI key as a secret: `supabase secrets set OPENAI_API_KEY=sk-xxx`
  5. Deploy the Edge Functions: `supabase functions deploy --no-verify-jwt`
  6. Expose `docs` schema via API in Supabase Dashboard [settings](https://supabase.com/dashboard/project/_/settings/api) > `API Settings` > `Exposed schemas`


### Ingest your documentation[#](https://supabase.com/docs/guides/ai/examples/headless-vector-search#ingest-your-documentation)
Now we need to push your documentation into the database as embeddings. You can do this manually, but to make it easier we've created a [GitHub Action](https://github.com/marketplace/actions/supabase-embeddings-generator) which can update your database every time there is a Pull Request.
In your knowledge base repository, create a new action called `.github/workflows/generate_embeddings.yml` with the following content:
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
name:'generate_embeddings'on:# run on main branch changespush:branches:-mainjobs:generate:runs-on:ubuntu-lateststeps:-uses:actions/checkout@v3-uses:supabase/embeddings-generator@v0.0.x# Update this to the latest version.with:supabase-url:'https://your-project-ref.supabase.co'# Update this to your project URL.supabase-service-role-key:${{ secrets.SUPABASE_SERVICE_ROLE_KEY }}openai-key:${{ secrets.OPENAI_API_KEY }}docs-root-path:'docs'# the path to the root of your md(x) files

```

Make sure to choose the latest version, and set your `SUPABASE_SERVICE_ROLE_KEY` and `OPENAI_API_KEY` as repository secrets in your repo settings (settings > secrets > actions).
### Add a search interface[#](https://supabase.com/docs/guides/ai/examples/headless-vector-search#add-a-search-interface)
Now inside your docs, you need to create a search interface. Because this is a headless interface, you can use it with any language. The only requirement is that you send the user query to the `query` Edge Function, which will stream an answer back from OpenAI. It might look something like this:
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
constonSubmit=(e:Event)=>{e.preventDefault()answer.value=""isLoading.value=trueconstquery=newURLSearchParams({query:inputRef.current!.value})constprojectUrl=`https://your-project-ref.supabase.co/functions/v1`constqueryURL=`${projectURL}/${query}`consteventSource=newEventSource(queryURL)eventSource.addEventListener("error",(err)=>{isLoading.value=falseconsole.error(err)})eventSource.addEventListener("message",(e:MessageEvent)=>{isLoading.value=falseif (e.data==="[DONE]") {eventSource.close()return}constcompletionResponse:CreateCompletionResponse=JSON.parse(e.data)consttext=completionResponse.choices[0].textanswer.value+=text});isLoading.value=true}

```

## Resources[#](https://supabase.com/docs/guides/ai/examples/headless-vector-search#resources)
  * Read about how we built [ChatGPT for the Supabase Docs](https://supabase.com/blog/chatgpt-supabase-docs).
  * Read the pgvector Docs for [Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)
  * See how to build something like this from scratch [using Next.js](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search).

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/ai/examples/headless-vector-search.mdx)
### Is this helpful?
No Yes
### On this page
[Tech stack](https://supabase.com/docs/guides/ai/examples/headless-vector-search#tech-stack)[Toolkit](https://supabase.com/docs/guides/ai/examples/headless-vector-search#toolkit)[Usage](https://supabase.com/docs/guides/ai/examples/headless-vector-search#usage)[Prepare your database](https://supabase.com/docs/guides/ai/examples/headless-vector-search#prepare-your-database)[Ingest your documentation](https://supabase.com/docs/guides/ai/examples/headless-vector-search#ingest-your-documentation)[Add a search interface](https://supabase.com/docs/guides/ai/examples/headless-vector-search#add-a-search-interface)[Resources](https://supabase.com/docs/guides/ai/examples/headless-vector-search#resources)
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



