---
url: https://supabase.com/blog/pgvector-performance
scraped_at: 2025-05-25T08:38:33.620563
title: pgvector 0.4.0 performance
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
# pgvector 0.4.0 performance
13 Jul 2023
•
13 minute read
[![Egor Romanov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fegor-romanov.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Egor RomanovEngineering](https://github.com/egor-romanov)
[![Pavel Borisov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F63344111%3Fv%3D4&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Pavel BorisovPostgres Engineer](https://github.com/pashkinelfe)
![pgvector 0.4.0 performance](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Fvector-benchmarks-thumb.jpeg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
🚀 The incorporation of the HNSW index in pgvector v0.5.0 ensures lightning-fast vector searches. We tested it, benchmarked it, and shared everything. [Read the new post](https://supabase.com/blog/increase-performance-pgvector-hnsw)
There are a few pgvector benchmarks floating around the internet, most recently a [pgvector vs Qdrant](https://nirantk.com/writing/pgvector-vs-qdrant/) comparison by NirantK. We wanted to reproduce (or improve!) the results.
There is an obvious bias here: we're a Postgres company. It's not our goal to prove that pgvector is better than Qdrant for running vector workloads. From everything we hear about Qdrant, it's fantastic.
Our goals in this article are:
  1. To show the strengths and limitations of the _current version_ of pgvector.
  2. Highlight some improvements that are coming to pgvector.
  3. Prove to you that it's completely viable for production workloads and give you some tips on using it at scale. We'll show you how to run 1 million Open AI embeddings at ~1800 queries per second with 91% accuracy, or 670 queries per second with 98% accuracy.


## Benchmark Methodology[#](https://supabase.com/blog/pgvector-performance#benchmark-methodology)
We've used the [ANN Benchmarks](https://github.com/erikbern/ann-benchmarks) methodology, a standard for benchmarking vector databases.
The key elements are:
  * **Helper scripts:** a Python test runner which is responsible for data upload, index creation, and query execution. This uses [qdrant's vector-db-benchmark](https://github.com/qdrant/vector-db-benchmark) repo. The “engine” in this repo uses [Vecs](https://github.com/supabase/vecs), a Python client for pgvector.
  * **Runtime:** Each test runs for at least 30-40 minutes and includes a series of experiments executed at various concurrency levels. This process allowed us to gauge the engine's performance under different load types. Subsequently, we averaged the results.
  * **Pre-warming RAM:** We executed 10,000 to 50,000 “warm-up” queries before each benchmark, matching the number of probes as the benchmark. Additionally, we executed about 1,000 queries with probes ranging from three to ten times the benchmark's probes. Both of these help with RAM utilization.


![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Fvecs-bench--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Hardware[#](https://supabase.com/blog/pgvector-performance#hardware)
All compute add-ons available on Supabase were used to run our benchmarks. Each add-on variant has a different allocation of RAM and CPU cores, the details of which are available in our docs. Each Supabase compute add-on comes with a specific set of optimizations ([version 2023-07](https://gist.github.com/egor-romanov/323e2847851bbd758081511785573c08)).
Instance| CPU| Memory  
---|---|---  
2XL| 8-core ARM (dedicated)| 32 GB  
4XL| 16-core ARM (dedicated)| 64 GB  
8XL| 32-core ARM (dedicated)| 128 GB  
12XL| 48-core ARM (dedicated)| 192 GB  
16XL| 64-core ARM (dedicated)| 256 GB  
## Dataset[#](https://supabase.com/blog/pgvector-performance#dataset)
We tested using the same dataset as the Qdrant comparison: [dbpedia-entities-openai-1M](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M). This dataset includes 1M embeddings with 1536 dimensions (created using OpenAI). The embeddings are created by Wikipedia articles. It's a great dataset!
We also have some useful [benchmarks in our docs](https://supabase.com/docs/guides/ai/choosing-compute-addon#results) for [gist-960-angular](http://corpus-texmex.irisa.fr/) (1M image embeddings, 960 dimensions) and [GloVe Reddit comments](https://nlp.stanford.edu/projects/glove/) (1.6M text embeddings, 512 dimensions).
## Baseline[#](https://supabase.com/blog/pgvector-performance#baseline)
Let's start with NirantK's results as a baseline:
![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Fnirantk--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
They aren't very flattering! Repeating our statements above, these benchmarks use the defaults for both engines. Our goal now is to replicate the results, and then see what improvements need to be made as developers scale up their workload.
## Results[#](https://supabase.com/blog/pgvector-performance#results)
Our tests mirrored NirantK's: but incorporated slight variations:
Same:
  * We used the same dataset
  * We used the same hardware: a 2XL instance on Supabase, which offers the same core and RAM count as NirantK's machine - 8 cores and 32 GB of RAM


Changed:
  * We used the pre-warming technique described earlier.
  * We used the `inner-product` distance function.
  * We set `lists` constant for an index equal to 2000 instead of 1000.
  * We adjusted the [Probes](https://github.com/pgvector/pgvector#query-options) in various runs to benchmark the difference (NirantK's tests used `probes = 1`).


The resulting figures were significantly different after these changes.
### PROBES = 10[#](https://supabase.com/blog/pgvector-performance#probes--10)
With the changes above and probes set to 10, pgvector was faster and more accurate:
  * accuracy@10 of 0.91
  * QPS (queries per second) of 380


![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Fpgvector-optimized--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### PROBES = 40[#](https://supabase.com/blog/pgvector-performance#probes--40)
If we increase the probes from 10 to 40, pgvector was not just substantially faster but also boasted almost the same accuracy as Qdrant:
  * accuracy@10 of 0.98
  * QPS of 140


![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Fpgvector-qdrant--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Scaling the database[#](https://supabase.com/blog/pgvector-performance#scaling-the-database)
Another key takeaway is that the performance scales predictably with the size of the database. For instance, a 4XL instance achieves accuracy@10 of 0.98 and QPS of 270 with probes set to 40. Moreover, an 8XL compute add-on analogously obtains accuracy@10 of 0.98 and an QPS of 470, surpassing the results of Qdrant.
The Qdrant benchmark uses “default” configuration and is in not indicative of its capabilities after modifying the configuration.
![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Fpgvector-8xl--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Although more compute is required to match Qdrant's accuracy and QPS levels concurrently, this is still a satisfying outcome. It means that it's not a _necessity_ to use another vector database. You can put everything in Postgres to lower your operational complexity.
### Final results: pgvector performance[#](https://supabase.com/blog/pgvector-performance#final-results-pgvector-performance)
Putting it all together, we find that we can predictably scale our database to match the performance we need.
With a 64-core, 256 GB server we achieve ~1800 QPS and 0.91 accuracy. This is for pgvector 0.4.0, and we've heard that the latest version (0.4.4) already has significant improvements. We'll release those benchmarks as soon as we have them.
![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Fsize-to-rps--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Other performance factors[#](https://supabase.com/blog/pgvector-performance#other-performance-factors)
It's been about 5 months since we [added](https://supabase.com/blog/openai-embeddings-postgres-vector) pgvector to the platform. Since then we've discovered a few other important things to keep in mind.
### Increasing lists improves performance[#](https://supabase.com/blog/pgvector-performance#increasing-lists-improves-performance)
Another way to improve performance without throwing more compute would be to increase `lists`.
We ran a test to measure the impact of list size: we uploaded 90,000 vectors from the Wikipedia dataset and then queried 10,000 vectors from the same dataset. The documentation recommends to use `lists` constant of `number of vectors / 1000`. In this case, it would be 90.
But as our experiment shows, we can improve QPS if we increase `lists` (i.e. with more lists in the index we need to get less index data to get the same accuracy). So for 95% accuracy, we can take any of:
  * 3% of index data = 270 lists
  * 6% of index data = 90 lists
  * 13% of index data = 30 lists


![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Flists-count--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
This also has an important caveat: building the index takes longer with more lists. Here we measure the index build time for a dataset containing 900,000 vectors:
So if you can afford an index build time of 1 hour or more, you can go with `lists=5000` (`number of vectors / 200`) or more!
![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Flists-for-1m--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You may need to increase `maintenance_work_mem` to be able to create an index with high values for `lists`. For example:
`
1
SET maintenance_work_mem TO '7168 MB';
`
Keeping in mind that the overall index size is almost the same, and only index build time increases, we can say that it's better to use more lists for better select queries speed.
### Real data has higher accuracy than random data[#](https://supabase.com/blog/pgvector-performance#real-data-has-higher-accuracy-than-random-data)
Embeddings created from “real” data are more likely to be clustered together, whereas random embeddings are more likely to be scattered. In other words, real embeddings are very far from being randomly distributed. This might seem obvious, but it's an important call-out for benchmarks.
Embeddings generated for similarity search using “real world data” will be more correlated, so the accuracy will be higher as well. You can see the difference in this chart using 10,000 Wikipedia embeddings, vs 10,000 randomly-generated embeddings:
![multi database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-13-pgvector-performance%2Frandom-data--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Optimizing pgvector performance[#](https://supabase.com/blog/pgvector-performance#optimizing-pgvector-performance)
Armed with all this information, we can safely give you a few tips and strategies for optimizing your pgvector workloads.
### Tips[#](https://supabase.com/blog/pgvector-performance#tips)
First, a few generic tips which you can pick and choose from:
  1. **Adjust your Postgres config.** It should be aligned with RAM & CPU cores. [Find more details here](https://gist.github.com/egor-romanov/323e2847851bbd758081511785573c08).
  2. Prefer `inner-product` to `L2` or `Cosine` distances if your vectors are normalized (like `text-embedding-ada-002`). If embeddings are not normalized, `Cosine` distance should give the best results with an index.
  3. **Pre-warm your database.** Implement the warm-up technique we described earlier before transitioning to production.
  4. **Establish your workload.** Increasing the lists constant for the pgvector index can accelerate your queries (at the expense of a slower build). For instance, for benchmarks with OpenAI embeddings, we employed a `lists` constant of 2000 (`number of vectors / 500`) as opposed to the suggested 1000 (`number of vectors / 1000`).
  5. **Benchmark your own specific workloads.** Doing this during cache warm-up helps gauge the best value for the `probes` constant, balancing accuracy with QPS.


### Going into production[#](https://supabase.com/blog/pgvector-performance#going-into-production)
Before running your pgvector workload in production, here are a few steps you can take to maximize performance.
  1. Over-provision RAM during preparation. You can scale down in step `5`, but it's better to start with a larger size to get the best results for RAM requirements. (We'd recommend at least 8XL if you're using Supabase.)
  2. Upload your data to the database. If you use [`vecs`](https://supabase.com/docs/guides/ai/python/api) library, it will automatically generate an index with default parameters.
  3. Run a benchmark using randomly generated queries and see the results. Again, you can use `vecs` library with the `ann-benchmarks` tool. Do it with probes set to 10 (default) and then with probes set to 100 or more, so QPS will be lower than 10.
  4. Take a look at the RAM usage, and save it as a note for yourself. You would likely want to use compute add-on in the future that would have the same amount of RAM as used at the moment (both actual RAM usage and RAM used for cache and buffers).
  5. Scale down your compute add-on to the one that would have the same amount of RAM as used at the moment.
  6. Repeat step 3. to load the data into RAM. You should see that QPS is increased on subsequent runs, and stop when it no longer increases. Then repeat the benchmark with probes set to a higher value as well if you didn't do it before on that compute add-on size.
  7. Run a benchmark using real queries and see the results. You can use `vecs` library for that as well with `ann-benchmarks` tool. Do it with probes set to 10 (default) and then gradually increase/decrease probes value until you see that both accuracy and QPS match your requirements.
  8. If you want higher QPS and you don't expect to have frequent inserts and reindexing, you can increase `lists` constantly. You have to rebuild the index with higher lists value and repeat steps 6-7 to find the best combination of `lists` and `probes` constants to achieve the best QPS and accuracy values. Higher `lists` mean that index will build slower, but you can achieve better QPS and accuracy. Higher probes mean that select queries will be slower, but you can achieve better accuracy.


## The pgvector roadmap[#](https://supabase.com/blog/pgvector-performance#the-pgvector-roadmap)
pgvector is still early in development. As with any open source tool, it needs time and resources to make it better. Supabase plans to continue supporting Andrew with his development of pgvector.
What's next on the roadmap? Andrew has an impressive list of features [planned for v0.5.0](https://github.com/pgvector/pgvector/issues/27):
✅ [Adding HNSW](https://supabase.com/blog/increase-performance-pgvector-hnsw): an index with better speed & accuracy than IVFFlat (at a higher memory cost)
  * Product quantization: better storage for IVFFLAT, improving speed and recall
  * Parallel index builds: building your IVFFLAT indexes will be much faster


## More AI resources[#](https://supabase.com/blog/pgvector-performance#more-ai-resources)
  * [How to build ChatGPT Plugin from scratch with Supabase Edge Runtime](https://supabase.com/blog/building-chatgpt-plugins-template)
  * [Docs pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)
  * [pgvector vs Qdrant](https://nirantk.com/writing/pgvector-vs-qdrant)
  * [Choosing Compute Add-on for AI workloads](https://supabase.com/docs/guides/ai/choosing-compute-addon)
  * [pgvector v0.5.0: Faster semantic search with HNSW indexes](https://supabase.com/blog/pgvector-v0-5-0-hnsw)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-performance&text=pgvector%200.4.0%20performance)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-performance&text=pgvector%200.4.0%20performance)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-performance&t=pgvector%200.4.0%20performance)
[Last postGetting started with Flutter authentication18 July 2023](https://supabase.com/blog/flutter-authentication)
[Next postWhat is new in PostgREST v11.1?12 July 2023](https://supabase.com/blog/postgrest-11-1-release)
[AI](https://supabase.com/blog/tags/AI)[performance](https://supabase.com/blog/tags/performance)[postgres](https://supabase.com/blog/tags/postgres)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [Benchmark Methodology](https://supabase.com/blog/pgvector-performance#benchmark-methodology)
  * [Hardware](https://supabase.com/blog/pgvector-performance#hardware)
  * [Dataset](https://supabase.com/blog/pgvector-performance#dataset)
  * [Baseline](https://supabase.com/blog/pgvector-performance#baseline)
  * [Results](https://supabase.com/blog/pgvector-performance#results)
  * [Other performance factors](https://supabase.com/blog/pgvector-performance#other-performance-factors)
  * [Optimizing pgvector performance](https://supabase.com/blog/pgvector-performance#optimizing-pgvector-performance)
  * [The pgvector roadmap](https://supabase.com/blog/pgvector-performance#the-pgvector-roadmap)
  * [More AI resources](https://supabase.com/blog/pgvector-performance#more-ai-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-performance&text=pgvector%200.4.0%20performance)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-performance&text=pgvector%200.4.0%20performance)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpgvector-performance&t=pgvector%200.4.0%20performance)
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

