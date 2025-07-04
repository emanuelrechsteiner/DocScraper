---
url: https://supabase.com/blog/database-build-live-share
scraped_at: 2025-05-25T09:31:24.219565
title: Live Share: Connect to in-browser PGlite with any Postgres client
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
# Live Share: Connect to in-browser PGlite with any Postgres client
10 Oct 2024
•
8 minute read
[![Julien Goux avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjgoux.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Julien GouxEngineering](https://github.com/jgoux)
[![Greg Richardson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgregnr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Greg RichardsonEngineering](https://github.com/gregnr)
![Live Share: Connect to in-browser PGlite with any Postgres client](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdatabase-build-live-share%2Fdatabase-build-live-share-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We just rolled out an exciting new feature for [database.build](https://database.build/) ([formerly postgres.new](https://supabase.com/blog/database-build-live-share#new-name-databasebuild)): **Live Share**.
Live Share allows you to connect to your in-browser PGlite databases from _outside the browser_.
In case you missed it, database.build is an [in-browser Postgres sandbox with AI assistance](https://supabase.com/blog/postgres-new). You can spin up an unlimited number of Postgres databases and interact with them using natural language (via LLM). This is possible thanks to [PGlite](https://pglite.dev/) - a WASM build of Postgres that can run directly in the browser.
With database.build, simply describe what you would like to build and AI will help you scaffold your tables. You can also drag-and-drop CSVs to automatically generate tables based on their contents, then query them using regular SQL.
## How does Live Share work?[#](https://supabase.com/blog/database-build-live-share#how-does-live-share-work)
After creating a database on database.build, you can now tap its sidebar menu and choose **Live Share**. A unique Postgres connection string will appear which you can use to connect to the in-browser instance via any Postgres client.
![Live Share connection string](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdatabase-build-live-share%2Flive-share-connection-string--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You could, for example, copy-paste this connection string into `psql`. Once connected, you can interact with your in-browser PGlite instance as if it were any regular Postgres database.
Some other tools you might want to connect to this:
  * pg_dump: export your in-browser databases to other platforms!
  * ORM: test out your database directly within your app
  * IDE: browse your data using your favorite database IDE


_Note PGlite has a single-connection limit which may not work with all clients - see[Limitations](https://supabase.com/blog/database-build-live-share#limitations)._
## Under the hood[#](https://supabase.com/blog/database-build-live-share#under-the-hood)
To make this possible, we developed a [**websocket-to-tcp proxy**](https://github.com/supabase-community/postgres-new/tree/main/apps/browser-proxy) that relays Postgres wire protocol messages between the in-browser PGlite instance and a PostgreSQL client over TCP.
![Browser proxy diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdatabase-build-live-share%2Fdiagram--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
On the browser side, we establish a persistent Web Socket connection that acts as a reverse tunnel for future messages sent from clients. Since Web Sockets support bidirectional communication, we simply send Postgres client messages in reverse - from our proxy back through the Web Socket tunnel to the PGlite instance in the browser. We are running a server from the browser!
From the Postgres client side, we use pg-gateway to handle incoming TCP connections. It handles startup and authentication messages, then routes future messages back through the appropriate Web Socket tunnel to the browser.
[pg-gateway](https://github.com/supabase-community/pg-gateway) is an open source library we developed to speak the Postgres wire protocol from the server-side. It allows us to run a Postgres-native proxy - meaning we can host a single TCP server that understands Postgres wire messages and route connections to multiple downstream databases via a wildcard domain (`*.browser.db.build`).
![Browser proxy diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdatabase-build-live-share%2Frouting-diagram--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Though you might be thinking - API gateways like nginx and HAProxy already exist to reverse proxy connections. Why can't we use one of these to route Postgres connections?
### The reverse proxy rabbit hole[#](https://supabase.com/blog/database-build-live-share#the-reverse-proxy-rabbit-hole)
In order to proxy a connection, you need to know its intended destination. With a protocol like HTTP, this is easy: simply read the `HOST` header in the request and forward the connection to the appropriate downstream server. This is often referred to as “virtual hosting” and is how backends are able to serve multiple websites over a single IP/port.
Adding TLS encryption is slightly more complicated, but not too bad. The problem is: how do you read an HTTP `HOST` header if the channel is encrypted? Thankfully a TLS extension called Server Name Indication (SNI) was created to solve this problem, which passes the server name in plain text prior to encrypting the channel. The API gateway can simply read this server name and forward the connection to the appropriate downstream server.
Now back to Postgres. Let's say your Postgres client connects to the host `123.browser.db.build`. We need to retrieve the database ID (`123`) from the host name in order to know which Web Socket tunnel to proxy the connection to. Unfortunately this host name is lost by the time it arrives at the proxy, since your client will first resolve `123.browser.db.build` to an IP address via DNS before establishing the connection. And unlike HTTP, the Postgres wire protocol has no `HOST`-like header, so our gateway has no real way to know which downstream server the request was intended for.
_But_ - what if we encrypt the Postgres wire channel via TLS, and then just use the same SNI extension to identify the downstream server? This would give us a means to route, and then we can just use an existing API gateway like nginx (which supports TLS + SNI). Right?
Yes and no. While Postgres _does_ support TLS encryption, it must be established as an upgrade mechanism within its wire protocol. This means that, unlike HTTPS where a TLS handshake is established first before any future HTTP messages, Postgres first expects an unencrypted `SSLRequest` message and response prior to establishing the connection, similar to the `STARTTLS` message in other protocols like SMTP and IMAP.
This is where pg-gateway comes in. The library understands not only Postgres-specific startup and authentication messages, but also `SSLRequest` messages. When it receives an `SSLRequest` from the client, it establishes a TLS connection, and importantly, also reads the SNI server name sent by the client. Now we get the best of both worlds - we can encrypt the channel, handle startup and authentication, then forward future messages back through the appropriate Web Socket tunnel based on the ID we pull from the SNI server name.
## Limitations[#](https://supabase.com/blog/database-build-live-share#limitations)
Since PGlite is a [single-user mode compiled version of PostgreSQL](https://github.com/electric-sql/pglite?tab=readme-ov-file#how-it-works), you can only connect with one Postgres client at a time. If you try to connect multiple clients using the same connection string, you will receive a “too many clients” error.
We considered multiplexing multiple connections over a single PGlite connection, but the more we dug into it, the more we realized this is a bad idea. To get this to work, you'd need to factor in:
  * Shared transaction state, meaning you need to prevent interleaving messages from multiple clients if any of them is in the middle of a transaction.
  * Multi-message protocols, like the extended query protocol. You will need to prevent interleaving messages from multiple clients until an entire set of extended query messages completes.
  * Any other shared session state between connections that could cause unpredictable behavior.


Be aware that some ORMs like Prisma will create a shadow database and connect to it in parallel in order to generate migrations. This unfortunately will fail with PGlite due to the single-connection limit. If you wish to connect your database with Prisma, you will need to [manually configure your shadow database](https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#manually-configuring-the-shadow-database) to point to another temporary DB.
Some IDEs like DBeaver will attempt to open multiple connections in parallel by default. Be sure to disable these settings before connecting via Live Share.
Live Share is also limited to the protocol messages that PGlite supports. For example, `COPY ... FROM STDIN` is not yet supported, so attempting to run `/copy` commands from `psql` will result in the connection hanging.
For the initial release, we are also enforcing the following limits on the proxy:
  * 5-minute idle timeout per TCP client connection
  * 1-hour total timeout for the WebSocket server connection


If you hit any of these limits, just reconnect your Live Share session and you can continue on as before.
## New name: database.build[#](https://supabase.com/blog/database-build-live-share#new-name-databasebuild)
One last thing - we're transitioning postgres.new to a new name: database.build.
Why rename? The term “Postgres” is reserved for official Postgres projects and we don't want to mislead anyone. We're renaming to [database.build](https://database.build/) because, well, that's what this does. This will still be 100% Postgres-focused, just with a different URL.
## Always open source[#](https://supabase.com/blog/database-build-live-share#always-open-source)
Below are the repos for the projects mentioned in this post - open source as always. Feel free to give them a star, add an issue, or contribute some code yourself:
  * [PGlite](https://github.com/electric-sql/pglite) (Apache 2.0): A WASM build of Postgres.
  * [pg-gateway](https://github.com/supabase-community/pg-gateway) (MIT): Postgres wire protocol for the server-side.
  * [database-build](https://github.com/supabase-community/postgres-new) (Apache 2.0): The frontend and browser proxy for [database.build](https://database.build).


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-live-share&text=Live%20Share%3A%20Connect%20to%20in-browser%20PGlite%20with%20any%20Postgres%20client)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-live-share&text=Live%20Share%3A%20Connect%20to%20in-browser%20PGlite%20with%20any%20Postgres%20client)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-live-share&t=Live%20Share%3A%20Connect%20to%20in-browser%20PGlite%20with%20any%20Postgres%20client)
[Last postClickHouse Partnership, improved Postgres Replication, and Disk Management30 October 2024](https://supabase.com/blog/supabase-clickhouse-partnership)
[Next postMongoDB Realm & Device Sync Alternatives - Supabase9 October 2024](https://supabase.com/blog/mongodb-realm-and-device-sync-alternatives)
[AI](https://supabase.com/blog/tags/AI)[postgres](https://supabase.com/blog/tags/postgres)
On this page
  * [How does Live Share work?](https://supabase.com/blog/database-build-live-share#how-does-live-share-work)
  * [Under the hood](https://supabase.com/blog/database-build-live-share#under-the-hood)
    * [The reverse proxy rabbit hole](https://supabase.com/blog/database-build-live-share#the-reverse-proxy-rabbit-hole)
  * [Limitations](https://supabase.com/blog/database-build-live-share#limitations)
  * [New name: database.build](https://supabase.com/blog/database-build-live-share#new-name-databasebuild)
  * [Always open source](https://supabase.com/blog/database-build-live-share#always-open-source)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-live-share&text=Live%20Share%3A%20Connect%20to%20in-browser%20PGlite%20with%20any%20Postgres%20client)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-live-share&text=Live%20Share%3A%20Connect%20to%20in-browser%20PGlite%20with%20any%20Postgres%20client)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-live-share&t=Live%20Share%3A%20Connect%20to%20in-browser%20PGlite%20with%20any%20Postgres%20client)
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
![Live Share connection string](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdatabase-build-live-share%2Flive-share-connection-string--dark.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

