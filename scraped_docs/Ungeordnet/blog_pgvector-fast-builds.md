---
url: https://supabase.com/blog/pgvector-fast-builds
scraped_at: 2025-05-25T08:41:43.743743
title: pgvector 0.6.0: 30x faster with parallel index builds
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
# pgvector 0.6.0: 30x faster with parallel index builds
30 Jan 2024
•
14 minute read
[![Egor Romanov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fegor-romanov.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Egor RomanovEngineering](https://github.com/egor-romanov)
![pgvector 0.6.0: 30x faster with parallel index builds](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-01-30-pgvector-fast-builds%2Fpgvector6.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
pgvector 0.6.0 was released today, with a significant improvement: parallel builds for HNSW indexes. Building an HNSW index is now up to 30x faster for unlogged tables.
This release is a huge step forward for pgvector, making it easier to tune HNSW build parameters and increase search accuracy and performance.
## HNSW indexes in pgvector[#](https://supabase.com/blog/pgvector-fast-builds#hnsw-indexes-in-pgvector)
We explored [how HNSW works](https://supabase.com/blog/increase-performance-pgvector-hnsw#how-does-hnsw-work) in an earlier post, so as a quick recap: HNSW is an algorithm for approximate nearest neighbor search. It uses proximity graphs and consists of two parts: hierarchical and navigatable small world. It operates over multiple layers with different densities or distances between nodes, where layers represent different connection lengths between nodes. Thus allowing HNSW to search, insert, and delete in linearithmic time.
## pgvector parallel index builds[#](https://supabase.com/blog/pgvector-fast-builds#pgvector-parallel-index-builds)
Prior to 0.6.0, pgvector only supported building indexes using a single thread - a big bottleneck for large datasets. For example, building an index for 1 million vectors of 1536 dimensions would take around 1 hour and 27 minutes (with `'m'=16, 'ef_construction'=200`).
With parallel index builds you can build an index for the same dataset in 9.5 minutes - 9 times faster:
![pgvector 0.6.0 vs 0.5.1 performance comparison with 9x faster build time](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-01-30-pgvector-fast-builds%2Ffastbuilds-comparison--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Performance comparison: pgvector 0.5 vs 0.6[#](https://supabase.com/blog/pgvector-fast-builds#performance-comparison-pgvector-05-vs-06)
We tested index build time with the [dbpedia-entities-openai-1M](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M) dataset (1 million vectors, 1536 dimensions) to compare the performance of parallel and single-threaded index HNSW builds. At the same time, we verified that the resulting indexes are the same in terms of accuracy and queries per second (QPS).
We ran benchmarks on various database sizes to see the impact of parallel builds:
  * 4XL instance (16 cores 64GB RAM)
  * 16XL instance (64 cores 256GB RAM)


### 4XL instance (16 cores 64GB RAM)[#](https://supabase.com/blog/pgvector-fast-builds#4xl-instance-16-cores-64gb-ram)
This benchmark used the following parameters:
| 0.5.1| 0.6.0  
---|---|---  
mainenance_work_mem| 30GB| 30GB  
max_parallel_maintenance_workers| -| 15  
`max_parallel_maintenance_workers` controls how many parallel threads are used to build an index. In further sections we will refer to the total number of workers, including the leader.
Results
![pgvector 0.6.0 vs 0.5.1 performance comparison with different build parameters](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-01-30-pgvector-fast-builds%2Fbuild-params--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The index build time is 7-9 times faster for 0.6.0, while queries per second and accuracy stay the same for both versions:
  * `v0.5.1`: averaged 938 QPS and 0.963 accuracy across all benchmarks.
  * `v0.6.0`: averaged 950 QPS and 0.963 accuracy across all benchmarks.


### 16XL instance (64 cores 256GB RAM)[#](https://supabase.com/blog/pgvector-fast-builds#16xl-instance-64-cores-256gb-ram)
You can further improve index build performance using a more powerful instance (up to 13.5x for these parameters).
Results
![pgvector 0.6.0 build times with different workers count](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-01-30-pgvector-fast-builds%2Fworkers--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The index build time is not linearly proportional to the number of cores used. A sensible default for `max_parallel_maintenance_workers` is `CPU count / 2` , the default we set on the Supabase platform. Accuracy and QPS are not affected by `max_parallel_maintenance_workers`.
##### Pro tip: optimizing your bills
The trick is to use a large database while you build the index and then switch back to a cheaper instance after the index is built.
### Embeddings with unlogged tables[#](https://supabase.com/blog/pgvector-fast-builds#embeddings-with-unlogged-tables)
Building time can be reduced _even further_ using unlogged tables.
An unlogged table in Postgres is a table whose modifications are not recorded in the write-ahead log (trading performance for data reliability). Unlogged tables are a great option for embeddings because the raw data is often stored separately and the embeddings can be recreated from the source data at any time.
One of the steps of index creation is the final scan and WAL writing. This is generally short but not parallelizable. Using unlogged tables allows you to skip the WAL, with an impressive impact:
ef_construction| Build time: v0.5.1| Build time: v0.6.0 (unlogged)| Improvement  
---|---|---|---  
64| 38m 08s| 1m 38s| 23x  
100| 1h 06m 59s| 2m 10s| 31x  
200| 1h 27m 45s| 3m 37s| 24x  
## Getting started[#](https://supabase.com/blog/pgvector-fast-builds#getting-started)
pgvector 0.6.0 was [just released](https://github.com/pgvector/pgvector/releases/tag/v0.6.0) and will be available on Supabase projects soon. Again, a special shout out to Andrew Kane and everyone else who [worked on parallel index builds](https://github.com/pgvector/pgvector/issues/409).
## More pgvector and AI resources[#](https://supabase.com/blog/pgvector-fast-builds#more-pgvector-and-ai-resources)
  * [pgvector v0.5.0: Faster semantic search with HNSW indexes](https://supabase.com/blog/increase-performance-pgvector-hnsw)
  * [How to build ChatGPT Plugin from scratch with Supabase Edge Runtime](https://supabase.com/blog/building-chatgpt-plugins-template)
  * [Docs pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)
  * [Choosing Compute Add-on for AI workloads](https://supabase.com/docs/guides/ai/choosing-compute-addon)
  * [pgvector: Fewer dimensions are better](https://supabase.com/blog/fewer-dimensions-are-better-pgvector)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-fast-builds&text=pgvector%200.6.0%3A%2030x%20faster%20with%20parallel%20index%20builds)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-fast-builds&text=pgvector%200.6.0%3A%2030x%20faster%20with%20parallel%20index%20builds)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-fast-builds&t=pgvector%200.6.0%3A%2030x%20faster%20with%20parallel%20index%20builds)
[Last postNoSQL Postgres: Add MongoDB compatibility to your Supabase projects with FerretDB31 January 2024](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio)
[Next postGetting started with Ruby on Rails and Postgres on Supabase29 January 2024](https://supabase.com/blog/ruby-on-rails-postgres)
[AI](https://supabase.com/blog/tags/AI)[performance](https://supabase.com/blog/tags/performance)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [HNSW indexes in pgvector](https://supabase.com/blog/pgvector-fast-builds#hnsw-indexes-in-pgvector)
  * [pgvector parallel index builds](https://supabase.com/blog/pgvector-fast-builds#pgvector-parallel-index-builds)
  * [Performance comparison: pgvector 0.5 vs 0.6](https://supabase.com/blog/pgvector-fast-builds#performance-comparison-pgvector-05-vs-06)
    * [4XL instance (16 cores 64GB RAM)](https://supabase.com/blog/pgvector-fast-builds#4xl-instance-16-cores-64gb-ram)
    * [16XL instance (64 cores 256GB RAM)](https://supabase.com/blog/pgvector-fast-builds#16xl-instance-64-cores-256gb-ram)
    * [Embeddings with unlogged tables](https://supabase.com/blog/pgvector-fast-builds#embeddings-with-unlogged-tables)
  * [Getting started](https://supabase.com/blog/pgvector-fast-builds#getting-started)
  * [More pgvector and AI resources](https://supabase.com/blog/pgvector-fast-builds#more-pgvector-and-ai-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-fast-builds&text=pgvector%200.6.0%3A%2030x%20faster%20with%20parallel%20index%20builds)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-fast-builds&text=pgvector%200.6.0%3A%2030x%20faster%20with%20parallel%20index%20builds)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-fast-builds&t=pgvector%200.6.0%3A%2030x%20faster%20with%20parallel%20index%20builds)
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
![pgvector 0.6.0 vs 0.5.1 performance comparison with 9x faster build time](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-01-30-pgvector-fast-builds%2Ffastbuilds-comparison--dark.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

