---
url: https://supabase.com/blog/supavisor-1-million
scraped_at: 2025-05-25T08:56:54.079709
title: Supavisor: Scaling Postgres to 1 Million Connections
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
# Supavisor: Scaling Postgres to 1 Million Connections
11 Aug 2023
•
14 minute read
[![Egor Romanov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fegor-romanov.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Egor RomanovEngineering](https://github.com/egor-romanov)
[![Chase Granberry avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fchasers.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Chase GranberryEngineering](https://github.com/chasers)
[![Stanislav Muzhyk avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fabc3.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Stanislav MuzhykEngineering](https://github.com/abc3)
![Supavisor: Scaling Postgres to 1 Million Connections](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-5%2Fsupavisor-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
One of the most [widely-discussed shortcomings](https://news.ycombinator.com/item?id=24735012) of Postgres is it's connection system. Every Postgres connection has a reasonably high memory footprint, and determining the maximum number of connections your database can handle is a [bit of an art](https://momjian.us/main/blogs/pgblog/2020.html#April_22_2020).
A common solution is [connection pooling](https://supabase.com/docs/guides/database/connecting-to-postgres#how-connection-pooling-works). Supabase currently offers [pgbouncer](http://www.pgbouncer.org/) which is single-threaded, making it difficult to scale. We've seen some [novel ways](https://twitter.com/viggy28/status/1677674197664038912?s=12&t=_WCn3v_QJ7tkQLvOvkZkqg) to scale pgbouncer, but we have a [few other goals](https://github.com/supabase/supavisor#motivation) in mind for our platform.
And so we've built [Supavisor](https://github.com/supabase/supavisor), a Postgres connection pooler that can handle millions of connections.
## What is Supavisor?[#](https://supabase.com/blog/supavisor-1-million#what-is-supavisor)
Supavisor is a scalable, cloud-native Postgres connection pooler. It has been developed with multi-tenancy in mind, handling millions of connections without significant overhead or latency. Supavisor is built in Elixir, in partnership with [José Valim](https://twitter.com/josevalim) (the creator of Elixir) and the [Dashbit](https://dashbit.co/) team.
![diagram of supavisor architecture](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fpooler-diagram-github--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supavisor will enable us to build some exciting new features for your Postgres cluster:
  * query caching
  * automatic read-replica load balancing
  * query blocking
  * and much more


## Benchmarking 1 million connections[#](https://supabase.com/blog/supavisor-1-million#benchmarking-1-million-connections)
We've benchmarked the characteristics Supavisor exhibits under load before rolling it out to our entire Postgres fleet. We tested how we can scale the cluster vertically and horizontally. These results have given us confidence that Supavisor is ready.
### Setup[#](https://supabase.com/blog/supavisor-1-million#setup)
We use a [custom load-testing application](https://github.com/supabase/benchmarks) to test the features of the Supabase platform. It consists of:
  1. Terraform scripts for creating a testing environment on AWS.
  2. k6 as the load generator. We used the k6 guides for [running large-scale tests](https://k6.io/docs/testing-guides/running-large-tests/) and [fine-tuning OS](https://k6.io/docs/misc/fine-tuning-os/) to tweak the config for AWS instances.
  3. Grafana + Prometheus for monitoring.


To simulate 1,000,000 concurrent active connections, we used 20 AWS EC2 instances with 16 cores and 32GB of RAM. We ran the tests for up to 2 hours to ensure that the Supavisor can handle load over long periods.
### Establishing a baseline[#](https://supabase.com/blog/supavisor-1-million#establishing-a-baseline)
In the first test, we set up a single ARM 16-core Supavisor instance on Ubuntu 22.04.2 aarch64 connected to one database instance.
![diagram supavisor 1 instance dark](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fsupavisor-tests--baseline.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We wanted to assess the capacity of a single Supavisor instance. We achieved:
  * 250,000 concurrent connections to Supavisor
  * Supavisor was running with a pool of 400 direct connections to the database
  * The system was processing 20,000 queries per second (QPS)


![diagram supavisor 1 instance dark](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fsupavisor-tests--250k-test.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
With this setup the database is the bottleneck - 20,000 QPS was the maximum this instance could handle. Increasing QPS would have been possible with a larger instance or read-replicas, but we wanted to focus on the scalability of Supavisor's connection limit (not Postgres's). Since Supavisor is built with multi-tenancy, addition of read-replicas is as easy as sending a single post request.
![chart connections baseline light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fchart-baseline-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Supavisor's scaling capabilities[#](https://supabase.com/blog/supavisor-1-million#supavisors-scaling-capabilities)
In the next step, we focused on Supavisor's vertical scaling capabilities by connecting **500,000 concurrent users** with a 64-core Supavisor instance while the single database instance configuration remained the same.
![diagram supavisor 1 instance dark](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fsupavisor-tests--500k-test.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The system showed no signs of instability or performance degradation. QPS remained constant at 20,000, proving that an increased number of connections doesn't negatively affect Supavisor's overall performance (this is generally expected from a [BEAM-based language](https://stressgrid.com/blog/webserver_benchmark/) like Elixir).
![chart connections vertical scaling light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fchart-vertical-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We also monitored how the load was distributed over Supavisor instance's cores:
![cpu load vertical scaling light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fcpu-vertical-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The load is spread evenly between all cores, which is great. CPU usage is high, signaling that the current setup has reached its capacity: a single Supavisor instance with 64 core handles around 500,000 connections. With this reference number, we moved on to horizontal scaling tests.
### Scaling to 1,000,000 connections[#](https://supabase.com/blog/supavisor-1-million#scaling-to-1000000-connections)
To examine horizontal scalability, we deployed two 64-core Supavisor instances, with the first instance connected directly to the database and the other relaying queries through the first.
![diagram supavisor 1 instance dark](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fsupavisor-tests--scaling-to-1million.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
In the Supavisor architecture, only a single node holds direct connections to each database instance. When you add more Postgres databases or read-replicas, Supavisor spreads the connections to the replicas. Every Supavisor instance can accept incoming connections and either execute queries themselves (if they directly connected) or relay to another node (if not).
This setup successfully handled:
  * **1,003,200 simultaneous connections** to the Supavisor instances.
  * **20,000 QPS** or **1.2 million queries per minute.** Each connection executed a `select` query once every 50 seconds.


![chart connections 1 million light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fchart-1m-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Within the cluster:
  * The directly connected instance was under almost the same load as when handling 500,000 concurrent clients in a single-node mode.
  * The relaying instance was extremely over-resourced. Most cores had little-to-no workload because relayed connections are more lightweight.


![cpu load 1 million light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fcpu-1m-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
In a multi-tenant setup (or when using Read-Replicas), the load is much more evenly spread because all Supavisor instances connect to comparable numbers of databases and have both direct and relayed connections evenly distributed between each other.
![diagram supavisor 1 instance dark](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fsupavisor-tests--multi-tenant-concept.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Supavisor's impact on query duration[#](https://supabase.com/blog/supavisor-1-million#supavisors-impact-on-query-duration)
To measure the impact on query duration, we started with 5,000 queries per second. This allows us to exclude side effects from the database side (long query execution times).
The query used in the experiment was the following:
`
1
select *
2
from (
3
  values
4
  (1, 'one'),
5
  (2, 'two'),
6
  (3, 'three')
7
) as t (num, letter);
`
We found with Supavisor median query duration was less than 2ms. And this includes not only time from client to Supavisor but the whole roundtrip: from Client to Supavisor ➡️ from Supavisor to Postgres ➡️ then query execution time on Postgres ➡️ and back to Supavisor ➡️ and to the Client.
| Query Duration  
---|---  
Median| 2ms  
p95| 3ms  
p99| 23ms  
![chart query duration for 5k qps light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fchart-5k-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We can see that 95% of queries were completed in less than 3 milliseconds. A slightly higher query duration at the beginning of the test can be explained by the dynamic nature of Supavisor-to-Database connection pool. It is being scaled up to the hard limit when more clients establish connections to Supavisor itself and scaled back down when users leave.
We continued to scale up to 20,000QPS to assess the impact on query duration and measured a median of 18.4ms:
| Query Duration  
---|---  
Median| 18.4ms  
p95| 46.9ms  
p99| 68ms  
![chart query duration for 20k qps light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fchart-20k-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Database experiences much more load and more concurrent queries, which leads to higher execution times on the database side. And here are some metrics from the database side:
![Postgres metrics](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fpostgres-metrics.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The scalability can be further enhanced by adding more databases (or read-replicas if you want to scale a single app) to increase QPS or deploying additional Supavisor instances to accommodate tens of millions of concurrent connections.
### Supavisor on Supabase Platform[#](https://supabase.com/blog/supavisor-1-million#supavisor-on-supabase-platform)
We compared our current PgBouncer setup with the new Supavisor setup to assess any impact on query duration.
_Current architecture_
Currently, every Supabase project comes with its own PgBouncer server running on the same instance as the Postgres database to ensure that the latency is as low as possible. But this setup comes with a trade-off: it uses the same compute resources as your database.
![diagram supavisor 1 instance dark](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fsupavisor-tests--pgbouncer.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
_Supavisor architecture_
In the future, you connect to a distinct multi-tenant Supavisor cluster through a load-balancer. The Supavisor cluster maintains a connection pool to your database. In this case the pooler doesn't consume additional CPU and RAM resources on the database server, but it does involve extra network latency.
![diagram supavisor 1 instance dark](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fsupavisor-tests--supavisor-and-supabase.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We ran 5,000 queries per second for each configuration, this time experimenting with `insert` query. To make the experiment more realistic, we enabled the PostGIS extension to store coordinates:
`
1
insert into positions (
2
  stud_id,
3
  first_name,
4
  last_name,
5
  title,
6
  reports_to,
7
  timestamp,
8
  location,
9
  email
10
)
11
values (
12
  ${name},
13
  'Virtual ${name}',
14
  'User ${name}',
15
  'Load Tester',
16
  1,
17
  ${Date.now()},
18
  st_point(-73.946${x}, 40.807${y}),
19
  'vu${name}@acme.corp'
20
);
`
We observed an additional 2ms required each query to be executed on the Supavisor architecture compared to PgBouncer architecture.
| Query Duration with Supavisor| Query Duration with PgBouncer  
---|---|---  
Median| 4ms| 1ms  
p95| 4ms| 2ms  
p99| 5ms| 3ms  
![chart query duration for 5k qps inserts with supavisor light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fchart-supavisor-duration-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Fig.1 - Query Duration with Supavisor
![chart query duration for 5k qps inserts with pgbouncer light](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fchart-pgbouncer-duration-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Fig.2 - Query Duration with PgBouncer
### Getting started[#](https://supabase.com/blog/supavisor-1-million#getting-started)
Supavisor has been rolled out to all Supabase projects in all regions.
Contact [support](https://supabase.com/dashboard/support/new) to start using it today, and we'll provide connection details. We will be exposing a new connection string in project dashboards over the next few weeks.
You'll be able to use both PgBouncer and Supavisor for a few months in parallel. Nothing will change with your PgBouncer setup if you need to switch back.
Supavisor will be added to the self-hosted stack as soon as we have tested it across our database fleet. That said - we're confident that it's ready for use if you want to try it with your own Postgres database. [Sequin](https://sequin.io/), one of our partners, has been using Supavisor for several months:
> With Supavisor, we've been able to ship incredible features that would have been very hard to build otherwise. For example, our customers can now read from and write to Salesforce and HubSpot via Postgres. We achieve this by intercepting queries that route through Supavisor.
> We chose Supavisor because it's scalable, multi-tenant, and written in Elixir. We were able to integrate it easily with our own Elixir infrastructure. As partners, we look forward to helping shape the future of Postgres connection pooling with Supabase.
> ![Anthony Accomazzo, Co-founder of Sequin. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fanthony-accomazzo.jpeg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> Anthony Accomazzo, Co-founder of Sequin.
## Conclusion[#](https://supabase.com/blog/supavisor-1-million#conclusion)
Supavisor's vertical and horizontal scaling ability make it the optimal solution for developers who aim to create applications that can effortlessly scale, even under extreme workloads, avoiding issues such as "too many connections" and enabling the full power of edge functions and serverless.
If you are interested in exploring Supavisor's potential or want to implement its scalability in your upcoming project, check out [the GitHub repository](https://github.com/supabase/supavisor) to know more.
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-1-million&text=Supavisor%3A%20Scaling%20Postgres%20to%201%20Million%20Connections)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-1-million&text=Supavisor%3A%20Scaling%20Postgres%20to%201%20Million%20Connections)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-1-million&t=Supavisor%3A%20Scaling%20Postgres%20to%201%20Million%20Connections)
[Last postSupabase is now HIPAA and SOC2 Type 2 compliant11 August 2023](https://supabase.com/blog/supabase-soc2-hipaa)
[Next postSupabase Integrations Marketplace10 August 2023](https://supabase.com/blog/supabase-integrations-marketplace)
[launch-week](https://supabase.com/blog/tags/launch-week)[supavisor](https://supabase.com/blog/tags/supavisor)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [What is Supavisor?](https://supabase.com/blog/supavisor-1-million#what-is-supavisor)
  * [Benchmarking 1 million connections](https://supabase.com/blog/supavisor-1-million#benchmarking-1-million-connections)
    * [Setup](https://supabase.com/blog/supavisor-1-million#setup)
    * [Establishing a baseline](https://supabase.com/blog/supavisor-1-million#establishing-a-baseline)
    * [Supavisor's scaling capabilities](https://supabase.com/blog/supavisor-1-million#supavisors-scaling-capabilities)
    * [Scaling to 1,000,000 connections](https://supabase.com/blog/supavisor-1-million#scaling-to-1000000-connections)
    * [Supavisor's impact on query duration](https://supabase.com/blog/supavisor-1-million#supavisors-impact-on-query-duration)
    * [Supavisor on Supabase Platform](https://supabase.com/blog/supavisor-1-million#supavisor-on-supabase-platform)
    * [Getting started](https://supabase.com/blog/supavisor-1-million#getting-started)
  * [Conclusion](https://supabase.com/blog/supavisor-1-million#conclusion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-1-million&text=Supavisor%3A%20Scaling%20Postgres%20to%201%20Million%20Connections)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-1-million&text=Supavisor%3A%20Scaling%20Postgres%20to%201%20Million%20Connections)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-1-million&t=Supavisor%3A%20Scaling%20Postgres%20to%201%20Million%20Connections)
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
![diagram of supavisor architecture](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-11-supavisor-1-million%2Fpooler-diagram-github--dark.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

