---
url: https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning
scraped_at: 2025-05-25T08:35:42.890779
title: Generate image captions using Hugging Face | Supabase Docs
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
  3. [Generate image captions using Hugging Face](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning)


Generate image captions using Hugging Face
Use the Hugging Face Inference API to make calls to 100,000+ Machine Learning models from Supabase Edge Functions.
We can combine Hugging Face with [Supabase Storage](https://supabase.com/storage) and [Database Webhooks](https://supabase.com/docs/guides/database/webhooks) to automatically caption for any image we upload to a storage bucket.
## About Hugging Face[#](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning#about-hugging-face)
[Hugging Face](https://huggingface.co/) is the collaboration platform for the machine learning community.
[Huggingface.js](https://huggingface.co/docs/huggingface.js/index) provides a convenient way to make calls to 100,000+ Machine Learning models, making it easy to incorporate AI functionality into your [Supabase Edge Functions](https://supabase.com/edge-functions).
## Setup[#](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning#setup)
  * Open your Supabase project dashboard or [create a new project](https://supabase.com/dashboard/projects).
  * [Create a new bucket](https://supabase.com/dashboard/project/_/storage/buckets) called `images`.
  * Generate TypeScript types from remote Database.
  * Create a new Database table called `image_caption`. 
    * Create `id` column of type `uuid` which references `storage.objects.id`.
    * Create a `caption` column of type `text`.
  * Regenerate TypeScript types to include new `image_caption` table.
  * Deploy the function to Supabase: `supabase functions deploy huggingface-image-captioning`.
  * Create the Database Webhook in the [Supabase Dashboard](https://supabase.com/dashboard/project/_/database/hooks) to trigger the `huggingface-image-captioning` function anytime a record is added to the `storage.objects` table.


## Generate TypeScript types[#](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning#generate-typescript-types)
To generate the types.ts file for the storage and public schemas, run the following command in the terminal:
```

1
supabasegentypestypescript--project-id=your-project-ref--schema=storage,public>supabase/functions/huggingface-image-captioning/types.ts

```

## Code[#](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning#code)
Find the complete code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/huggingface-image-captioning).
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
import{serve}from'https://deno.land/std@0.168.0/http/server.ts'import{HfInference}from'https://esm.sh/@huggingface/inference@2.3.2'import{createClient}from'jsr:@supabase/supabase-js@2'import{Database}from'./types.ts'console.log('Hello from `huggingface-image-captioning` function!')consthf=newHfInference(Deno.env.get('HUGGINGFACE_ACCESS_TOKEN'))typeSoRecord=Database['storage']['Tables']['objects']['Row']interfaceWebhookPayload{type:'INSERT'|'UPDATE'|'DELETE'table:stringrecord:SoRecordschema:'public'old_record:null|SoRecord}serve(async(req)=>{constpayload:WebhookPayload=awaitreq.json()constsoRecord=payload.recordconstsupabaseAdminClient=createClient<Database>(// Supabase API URL - env var exported by default when deployed.Deno.env.get('SUPABASE_URL')??'',// Supabase API SERVICE ROLE KEY - env var exported by default when deployed.Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')??'')// Construct image url from storageconst{data,error}=awaitsupabaseAdminClient.storage.from(soRecord.bucket_id!).createSignedUrl(soRecord.path_tokens!.join('/'),60)if (error) throwerrorconst{signedUrl}=data// Run image captioning with HuggingfaceconstimgDesc=awaithf.imageToText({data:await(awaitfetch(signedUrl)).blob(),model:'nlpconnect/vit-gpt2-image-captioning',})// Store image caption in Database tableawaitsupabaseAdminClient.from('image_caption').insert({id:soRecord.id!,caption:imgDesc.generated_text}).throwOnError()returnnewResponse('ok')})

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/ai/examples/huggingface-image-captioning.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FOgnYxRkxEUw%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[About Hugging Face](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning#about-hugging-face)[Setup](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning#setup)[Generate TypeScript types](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning#generate-typescript-types)[Code](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning#code)
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



