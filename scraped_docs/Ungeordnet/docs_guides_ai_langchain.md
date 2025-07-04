---
url: https://supabase.com/docs/guides/ai/langchain
scraped_at: 2025-05-25T09:26:44.180109
title: LangChain | Supabase Docs
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
  3. [LangChain](https://supabase.com/docs/guides/ai/langchain)


LangChain
[LangChain](https://langchain.com/) is a popular framework for working with AI, Vectors, and embeddings. LangChain supports using Supabase as a [vector store](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase), using the `pgvector` extension.
## Initializing your database[#](https://supabase.com/docs/guides/ai/langchain#initializing-your-database)
Prepare you database with the relevant tables:
DashboardSQL
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
32
33
34
35
36
37
38
-- Enable the pgvector extension to work with embedding vectorscreate extension vector;-- Create a table to store your documentscreatetabledocuments ( id bigserialprimary key, content text, -- corresponds to Document.pageContent metadata jsonb, -- corresponds to Document.metadata embedding vector(1536) -- 1536 works for OpenAI embeddings, change if needed);-- Create a function to search for documentscreatefunctionmatch_documents ( query_embedding vector(1536), match_count intdefaultnull,filter jsonb DEFAULT'{}') returnstable ( id bigint, content text, metadata jsonb, similarity float)language plpgsqlas $$#variable_conflict use_columnbeginreturn queryselect  id,  content,  metadata,1- (documents.embedding<=> query_embedding) as similarityfrom documentswhere metadata @>filterorder bydocuments.embedding<=> query_embeddinglimit match_count;end;$$;

```

## Usage[#](https://supabase.com/docs/guides/ai/langchain#usage)
You can now search your documents using any Node.js application. This is intended to be run on a secure server route.
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
import{SupabaseVectorStore}from'langchain/vectorstores/supabase'import{OpenAIEmbeddings}from'langchain/embeddings/openai'import{createClient}from'@supabase/supabase-js'constsupabaseKey=process.env.SUPABASE_SERVICE_ROLE_KEYif (!supabaseKey) thrownewError(`Expected SUPABASE_SERVICE_ROLE_KEY`)consturl=process.env.SUPABASE_URLif (!url) thrownewError(`Expected env var SUPABASE_URL`)exportconstrun=async()=>{constclient=createClient(url,supabaseKey)constvectorStore=awaitSupabaseVectorStore.fromTexts(['Hello world','Bye bye',"What's this?"],[{id:2},{id:1},{id:3}],newOpenAIEmbeddings(),{client,tableName:'documents',queryName:'match_documents',})constresultOne=awaitvectorStore.similaritySearch('Hello world',1)console.log(resultOne)}

```

### Simple metadata filtering[#](https://supabase.com/docs/guides/ai/langchain#simple-metadata-filtering)
Given the above `match_documents` Postgres function, you can also pass a filter parameter to only return documents with a specific metadata field value. This filter parameter is a JSON object, and the `match_documents` function will use the Postgres JSONB Containment operator `@>` to filter documents by the metadata field values you specify. See details on the [Postgres JSONB Containment operator](https://www.postgresql.org/docs/current/datatype-json.html#JSON-CONTAINMENT) for more information.
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
32
import{SupabaseVectorStore}from'langchain/vectorstores/supabase'import{OpenAIEmbeddings}from'langchain/embeddings/openai'import{createClient}from'@supabase/supabase-js'// First, follow set-up instructions aboveconstprivateKey=process.env.SUPABASE_SERVICE_ROLE_KEYif (!privateKey) thrownewError(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)consturl=process.env.SUPABASE_URLif (!url) thrownewError(`Expected env var SUPABASE_URL`)exportconstrun=async()=>{constclient=createClient(url,privateKey)constvectorStore=awaitSupabaseVectorStore.fromTexts(['Hello world','Hello world','Hello world'],[{user_id:2},{user_id:1},{user_id:3}],newOpenAIEmbeddings(),{client,tableName:'documents',queryName:'match_documents',})constresult=awaitvectorStore.similaritySearch('Hello world',1,{user_id:3,})console.log(result)}

```

### Advanced metadata filtering[#](https://supabase.com/docs/guides/ai/langchain#advanced-metadata-filtering)
You can also use query builder-style filtering ([similar to how the Supabase JavaScript library works](https://supabase.com/docs/reference/javascript/using-filters)) instead of passing an object. Note that since the filter properties will be in the metadata column, you need to use arrow operators (`->` for integer or `->>` for text) as defined in [PostgREST API documentation](https://postgrest.org/en/stable/references/api/tables_views.html?highlight=operators#json-columns) and specify the data type of the property (e.g. the column should look something like `metadata->some_int_value::int`).
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
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
import{SupabaseFilterRPCCall,SupabaseVectorStore}from'langchain/vectorstores/supabase'import{OpenAIEmbeddings}from'langchain/embeddings/openai'import{createClient}from'@supabase/supabase-js'// First, follow set-up instructions aboveconstprivateKey=process.env.SUPABASE_SERVICE_ROLE_KEYif (!privateKey) thrownewError(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)consturl=process.env.SUPABASE_URLif (!url) thrownewError(`Expected env var SUPABASE_URL`)exportconstrun=async()=>{constclient=createClient(url,privateKey)constembeddings=newOpenAIEmbeddings()conststore=newSupabaseVectorStore(embeddings,{client,tableName:'documents',})constdocs=[{pageContent:'This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to expand upon the notion of quantum fluff, a theoretical concept where subatomic particles coalesce to form transient multidimensional spaces. Yet, this abstraction holds no real-world application or comprehensible meaning, reflecting a cosmic puzzle.',metadata:{b:1,c:10,stuff:'right'},},{pageContent:'This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to proceed by discussing the echo of virtual tweets in the binary corridors of the digital universe. Each tweet, like a pixelated canary, hums in an unseen frequency, a fascinatingly perplexing phenomenon that, while conjuring vivid imagery, lacks any concrete implication or real-world relevance, portraying a paradox of multidimensional spaces in the age of cyber folklore.',metadata:{b:2,c:9,stuff:'right'},},{pageContent:'hello',metadata:{b:1,c:9,stuff:'right'}},{pageContent:'hello',metadata:{b:1,c:9,stuff:'wrong'}},{pageContent:'hi',metadata:{b:2,c:8,stuff:'right'}},{pageContent:'bye',metadata:{b:3,c:7,stuff:'right'}},{pageContent:"what's this",metadata:{b:4,c:6,stuff:'right'}},]awaitstore.addDocuments(docs)constfuncFilterA:SupabaseFilterRPCCall=(rpc)=>rpc.filter('metadata->b::int','lt',3).filter('metadata->c::int','gt',7).textSearch('content',`'multidimensional' & 'spaces'`,{config:'english',})constresultA=awaitstore.similaritySearch('quantum',4,funcFilterA)constfuncFilterB:SupabaseFilterRPCCall=(rpc)=>rpc.filter('metadata->b::int','lt',3).filter('metadata->c::int','gt',7).filter('metadata->>stuff','eq','right')constresultB=awaitstore.similaritySearch('hello',2,funcFilterB)console.log(resultA,resultB)}

```

## Hybrid search[#](https://supabase.com/docs/guides/ai/langchain#hybrid-search)
LangChain supports the concept of a hybrid search, which combines Similarity Search with Full Text Search. Read the official docs to get started: [Supabase Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid).
You can install the LangChain Hybrid Search function though our [database.dev package manager](https://database.dev/langchain/hybrid_search).
## Resources[#](https://supabase.com/docs/guides/ai/langchain#resources)
  * Official [LangChain site](https://langchain.com/).
  * Official [LangChain docs](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase).
  * Supabase [Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid).

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/ai/langchain.mdx)
### Is this helpful?
No Yes
### On this page
[Initializing your database](https://supabase.com/docs/guides/ai/langchain#initializing-your-database)[Usage](https://supabase.com/docs/guides/ai/langchain#usage)[Simple metadata filtering](https://supabase.com/docs/guides/ai/langchain#simple-metadata-filtering)[Advanced metadata filtering](https://supabase.com/docs/guides/ai/langchain#advanced-metadata-filtering)[Hybrid search](https://supabase.com/docs/guides/ai/langchain#hybrid-search)[Resources](https://supabase.com/docs/guides/ai/langchain#resources)
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



