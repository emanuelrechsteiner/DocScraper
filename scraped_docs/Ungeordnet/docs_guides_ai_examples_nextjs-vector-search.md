---
url: https://supabase.com/docs/guides/ai/examples/nextjs-vector-search
scraped_at: 2025-05-25T08:57:37.388710
title: Vector search with Next.js and OpenAI | Supabase Docs
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
  3. [Adding generative Q&A to your Next.js site](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search)


Vector search with Next.js and OpenAI
Learn how to build a ChatGPT-style doc search powered by Next.js, OpenAI, and Supabase.
While our [Headless Vector search](https://supabase.com/docs/guides/ai/examples/headless-vector-search) provides a toolkit for generative Q&A, in this tutorial we'll go more in-depth, build a custom ChatGPT-like search experience from the ground-up using Next.js. You will:
  1. Convert your markdown into embeddings using OpenAI.
  2. Store you embeddings in Postgres using pgvector.
  3. Deploy a function for answering your users' questions.


You can read our [Supabase Clippy](https://supabase.com/blog/chatgpt-supabase-docs) blog post for a full example.
We assume that you have a Next.js project with a collection of `.mdx` files nested inside your `pages` directory. We will start developing locally with the Supabase CLI and then push our local database changes to our hosted Supabase project. You can find the [full Next.js example on GitHub](https://github.com/supabase-community/nextjs-openai-doc-search).
## Create a project[#](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#create-a-project)
  1. [Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.
  2. Enter your project details.
  3. Wait for the new database to launch.


## Prepare the database[#](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#prepare-the-database)
Let's prepare the database schema. We can use the "OpenAI Vector Search" quickstart in the [SQL Editor](https://supabase.com/dashboard/project/_/sql), or you can copy/paste the SQL below and run it yourself.
DashboardSQL
  1. Go to the [SQL Editor](https://supabase.com/dashboard/project/_/sql) page in the Dashboard.
  2. Click **OpenAI Vector Search**.
  3. Click **Run**.


## Pre-process the knowledge base at build time[#](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#pre-process-the-knowledge-base-at-build-time)
With our database set up, we need to process and store all `.mdx` files in the `pages` directory. You can find the full script [here](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/lib/generate-embeddings.ts), or follow the steps below:
1
### Generate Embeddings
Create a new file `lib/generate-embeddings.ts` and copy the code over from [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/lib/generate-embeddings.ts).
```

1
2
3
curl\https://raw.githubusercontent.com/supabase-community/nextjs-openai-doc-search/main/lib/generate-embeddings.ts \-o "lib/generate-embeddings.ts"

```

2
### Set up environment variables
We need some environment variables to run the script. Add them to your `.env` file and make sure your `.env` file is not committed to source control! You can get your local Supabase credentials by running `supabase status`.
```

1
2
3
4
5
6
NEXT_PUBLIC_SUPABASE_URL=NEXT_PUBLIC_SUPABASE_ANON_KEY=SUPABASE_SERVICE_ROLE_KEY=# Get your key at https://platform.openai.com/account/api-keysOPENAI_API_KEY=

```

3
### Run script at build time
Include the script in your `package.json` script commands to enable Vercel to automatically run it at build time.
```

1
2
3
4
5
6
"scripts": {"dev":"next dev","build":"pnpm run embeddings && next build","start":"next start","embeddings":"tsx lib/generate-embeddings.ts"},

```

## Create text completion with OpenAI API[#](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#create-text-completion-with-openai-api)
Anytime a user asks a question, we need to create an embedding for their question, perform a similarity search, and then send a text completion request to the OpenAI API with the query and then context content merged together into a prompt.
All of this is glued together in a [Vercel Edge Function](https://vercel.com/docs/concepts/functions/edge-functions), the code for which can be found on [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/pages/api/vector-search.ts).
1
### Create Embedding for Question
In order to perform similarity search we need to turn the question into an embedding.
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
constembeddingResponse=awaitfetch('https://api.openai.com/v1/embeddings',{method:'POST',headers:{Authorization:`Bearer ${openAiKey}`,'Content-Type':'application/json',},body:JSON.stringify({model:'text-embedding-ada-002',input:sanitizedQuery.replaceAll('\n',''),}),})if (embeddingResponse.status!==200) {thrownewApplicationError('Failed to create embedding for question',embeddingResponse)}const{data:[{embedding}],}=awaitembeddingResponse.json()

```

2
### Perform similarity search
Using the `embeddingResponse` we can now perform similarity search by performing an remote procedure call (RPC) to the database function we created earlier.
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
const{error:matchError,data:pageSections}=awaitsupabaseClient.rpc('match_page_sections',{embedding,match_threshold:0.78,match_count:10,min_content_length:50,})

```

3
### Perform text completion request
With the relevant content for the user's question identified, we can now build the prompt and make a text completion request via the OpenAI API.
If successful, the OpenAI API will respond with a `text/event-stream` response that we can forward to the client where we'll process the event stream to smoothly print the answer to the user.
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
constprompt=codeBlock`${oneLine`  You are a very enthusiastic Supabase representative who loves  to help people! Given the following sections from the Supabase  documentation, answer the question using only that information,  outputted in markdown format. If you are unsure and the answer  is not explicitly written in the documentation, say  "Sorry, I don't know how to help with that."`} Context sections:${contextText} Question: """${sanitizedQuery} """ Answer as markdown (including related code snippets if available):`constcompletionOptions:CreateCompletionRequest={model:'gpt-3.5-turbo-instruct',prompt,max_tokens:512,temperature:0,stream:true,}constresponse=awaitfetch('https://api.openai.com/v1/completions',{method:'POST',headers:{Authorization:`Bearer ${openAiKey}`,'Content-Type':'application/json',},body:JSON.stringify(completionOptions),})if (!response.ok) {consterror=awaitresponse.json()thrownewApplicationError('Failed to generate completion',error)}// Proxy the streamed SSE response from OpenAIreturnnewResponse(response.body,{headers:{'Content-Type':'text/event-stream',},})

```

## Display the answer on the frontend[#](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#display-the-answer-on-the-frontend)
In a last step, we need to process the event stream from the OpenAI API and print the answer to the user. The full code for this can be found on [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/components/SearchDialog.tsx).
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
consthandleConfirm=React.useCallback(async(query:string)=>{setAnswer(undefined)setQuestion(query)setSearch('')dispatchPromptData({index:promptIndex,answer:undefined,query})setHasError(false)setIsLoading(true)consteventSource=newSSE(`api/vector-search`,{headers:{apikey:process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY??'',Authorization:`Bearer ${process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY}`,'Content-Type':'application/json',},payload:JSON.stringify({query}),})functionhandleError<T>(err:T){setIsLoading(false)setHasError(true)console.error(err)}eventSource.addEventListener('error',handleError)eventSource.addEventListener('message',(e:any)=>{try{setIsLoading(false)if (e.data==='[DONE]') {setPromptIndex((x)=>{returnx+1})return}constcompletionResponse:CreateCompletionResponse=JSON.parse(e.data)consttext=completionResponse.choices[0].textsetAnswer((answer)=>{constcurrentAnswer=answer??''dispatchPromptData({index:promptIndex,answer:currentAnswer+text,})return (answer??'') +text})}catch (err) {handleError(err)}})eventSource.stream()eventSourceRef.current=eventSourcesetIsLoading(true)},[promptIndex,promptData])

```

## Learn more[#](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#learn-more)
Want to learn more about the awesome tech that is powering this?
  * Read about how we built [ChatGPT for the Supabase Docs](https://supabase.com/blog/chatgpt-supabase-docs).
  * Read the pgvector Docs for [Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)
  * Watch Greg's video for a full breakdown:

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/ai/examples/nextjs-vector-search.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FxmfNUCjszh4%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Create a project](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#create-a-project)[Prepare the database](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#prepare-the-database)[Pre-process the knowledge base at build time](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#pre-process-the-knowledge-base-at-build-time)[Create text completion with OpenAI API](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#create-text-completion-with-openai-api)[Display the answer on the frontend](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#display-the-answer-on-the-frontend)[Learn more](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search#learn-more)
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



