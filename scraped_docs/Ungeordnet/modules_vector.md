---
url: http://supabase.com/modules/vector
scraped_at: 2025-05-25T09:45:35.098222
title: Supabase Vector | The Postgres Vector database and AI Toolkit
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
[Vector](https://supabase.com/modules/vector)[Cron](https://supabase.com/modules/cron)[Queues](https://supabase.com/modules/queues)
[ Docs](https://supabase.com/docs/guides/ai)
Supabase Vector
[AI Engineer SummitWatch our CEO's talk](https://youtu.be/qw4PrtyvJI0?t=10584)
# The Postgres Vector database and AI Toolkit
An open source Vector database for developing AI applications. Use pgvector to store, index, and access embeddings, and our AI toolkit to build AI applications with Hugging Face and OpenAI.
[Launch a free database](https://supabase.com/dashboard)[Explore documentation](https://supabase.com/docs/guides/ai)
### Postgres + pgvector
Use pgvector to store, query, and index your vector embeddings at scale in a Postgres instance.
![OpenAi logo](https://supabase.com/_next/image?url=%2Fimages%2Fproduct%2Fvector%2Fopenai-logo-light.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### OpenAI and More
Easily connect to any LLM or embeddings API, including Hugging Face, SageMaker and more.
### Secure and Scalable
Supabase is SOC2 Type 2 compliant, and comes with an advanced permissions system.
### Deploy Globally
Choose from many globally-distributed data centres or self-host on your own cloud.
## Leverage the tools you love
![Diagram of Machine Learning tools that integrate with Supabase Vector](https://supabase.com/_next/image?url=%2Fimages%2Fproduct%2Fvector%2Fvector-tools-dark.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Simple yetpowerful APIs
Easy-to-use client libraries for managing and querying vector stores in Postgres.
[Explore documentation](https://supabase.com/docs/guides/ai/vecs-python-client)
[![Google Colaboratory logo](https://supabase.com/_next/image?url=%2Fimages%2Flogos%2Fgoogle-colaboratory.svg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Open in Colab](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb)
```
docs = vx.create_collection(name="docs", dimension=3)

# add records to the collectiondocs.upsert(
  vectors=[
    (
"vec0",      # the vector's identifier     [0.1, 0.2, 0.3], # the vector. list or np.array     {"year": 1973}  # associated metadata    ),
    (
"vec1",
     [0.7, 0.8, 0.9],
     {"year": 2012}
    )
  ]
)
    
```

[![Google Colaboratory logo](https://supabase.com/_next/image?url=%2Fimages%2Flogos%2Fgoogle-colaboratory.svg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Open in Colab](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb)
```
# get an existing collectiondocs = vx.get_collection(name="docs")

# index the collection to be queried by cosine distancedocs.create_index(measure=vecs.IndexMeasure.cosine_distance)
# Available options for query measure are:## vecs.IndexMeasure.cosine_distance# vecs.IndexMeasure.l2_distance# vecs.IndexMeasure.max_inner_product
# or use the default (cosine_distance)docs.create_index()
   
```

[![Google Colaboratory logo](https://supabase.com/_next/image?url=%2Fimages%2Flogos%2Fgoogle-colaboratory.svg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Open in Colab](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb)
```
# get an existing collectiondocs = vx.get_collection(name="docs")

# Query vectors with optional Metadata Filteringdocs.query(
  query_vector=[0.4,0.5,0.6],
  filters={"year": {"$eq": 2012}}, # metadata filters)
   
```

[![Google Colaboratory logo](https://supabase.com/_next/image?url=%2Fimages%2Flogos%2Fgoogle-colaboratory.svg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Open in Colab](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb)
Store
Efficiently upsert millions of vectors with important metadata.
Index
Query
Efficiently upsert millions of vectors with important metadata.
## What you can buildwith Supabase Vector?
Scale effortlessly from experimentation to production-ready AI applications.
#### Semantic Search
Search your own knowledge base by semantic similarity.
[View example](https://supabase.com/docs/guides/ai/examples/headless-vector-search)
#### ChatGPT Plugins
Enhance chatbot memory with content-based long-term retention.
[View example](https://supabase.com/docs/guides/ai/examples/building-chatgpt-plugins)
#### OpenAI completions
Generate GPT text completions using OpenAI in Edge Functions.
[View example](https://supabase.com/docs/guides/ai/examples/openai)
#### Image Similarity
Transform images into image vector representations to detect similarity patterns.
[Open in Colab](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/face_similarity.ipynb)
#### Data Management
Automatically tag, deduplicate or detect patterns in your vector store.
[Open in Colab](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/semantic_text_deduplication.ipynb)
#### Next.js Vector Search
Learn how to build ChatGPT-style doc search powered by Next.js and OpenAI.
[View example](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search)
## Powerful FeaturesScale to millions
Develop, integrate, and deploy secure and enterprise-grade AI applications at unprecedented speed.
[Explore documentation](https://supabase.com/docs/guides/ai)
## Fully managed or Self-Hosted
Start with our hassle-free cloud platform, or self-host to keep everything within your infrastructure. You choose.
## Global & Multi-Region
Automatically provision and configure a fleet of applications across multiple regions to reduce read latency.
## Integrated
Store vector embeddings in the same database as your transactional data, simplifying your applications and improving performance.
## No Vendor Lock-In
Supabase uses open source tools to increase portability and avoid lock-in, making it easy to migrate in and out.
## Automatic Backups
Protect your data using automatic backups with Point In Time Recovery to ensure it's always safe and recoverable.
## Highly Scalable
Designed for unparalleled high performance and availability at global scale.
### Customers building on Supabase Vector
[![Supabase + mozilla](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Flight%2Fmozilla.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> We store embeddings in a PostgreSQL database, hosted by Supabase, to perform a similarity search to identify the most relevant sections within the MDN.
Hermina Condei, Director at MDN, MozillaRead Customer Story](https://developer.mozilla.org/en-US/blog/introducing-ai-help/)[![Supabase + quivr](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Flight%2Fquivr.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> Supabase Vector powered by pgvector allowed us to create a simple and efficient product. We are storing over 1.6 million embeddings and the performance and results are great. Open source develop can easily contribute thanks to the SQL syntax known by millions of developers.
Stan Girard, Founder of QuivrRead Customer Story](https://supabase.com/customers/quivr)[![Supabase + mendableai](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Flight%2Fmendableai.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> We tried other vector databases - we tried Faiss, we tried Weaviate, we tried Pinecone. If you’re just doing vector search they’re great, but if you need to store a bunch of metadata that becomes a huge pain.
Caleb Peffer, CEO at MendableRead Customer Story](https://supabase.com/customers/mendableai)
## Supabase Vector for Enterprise
Talk to one of our experts about scaling Supabase Vector and managing embeddings at scale.
[Fill out Enterprise Form](https://forms.supabase.com/enterprise)
## Pick your SupaPower(s)
Supabase products are built to work both in isolation and seamlessly together to ensure the most flexible and scalable developer experience.
[Database](https://supabase.com/database)
[Authentication](https://supabase.com/auth)
[Storage](https://supabase.com/storage)
[Edge Functions](https://supabase.com/edge-functions)
[Realtime](https://supabase.com/realtime)
[Vector](https://supabase.com/vector)
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

