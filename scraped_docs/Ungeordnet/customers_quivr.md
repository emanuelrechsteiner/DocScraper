---
url: http://supabase.com/customers/quivr
scraped_at: 2025-05-25T09:39:26.287976
title: Quivr launch 5,000 Vector databases on Supabase.
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
[Back](https://supabase.com/customers)
[Customer Stories](https://supabase.com/customers)
# Quivr launch 5,000 Vector databases on Supabase.
Learn how one of the most popular Generative AI projects uses Supabase as their Vector Store.
![Quivr launch 5,000 Vector databases on Supabase. logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fquivr.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
About
Quivr is an open source 'second brain'. It's like a private ChatGPT, personalized with your own data: you upload your documents and you can then search and ask questions using generative AI.
[https://quivr.app](https://quivr.app)
Use caseGenerative AI
SolutionsSupabase Vector, Supabase Auth
Ready to get started?
[Contact sales](https://supabase.com/contact/enterprise)
## The challenge: Building a second brain[#](https://supabase.com/customers/quivr#the-challenge-building-a-second-brain)
In May of 2023, [Stan Girard's](https://twitter.com/_StanGirard) started building small prototypes that allowed him to "chat with documents". After 2 weeks of research, he settled on an idea - build a "second brain" where a user could dump all their digital knowledge (audio, URLs, text, and code) into a vector store and query it with GPT4.
He built the first version in a single afternoon, pushed it to GitHub, and then [tweeted about it](https://twitter.com/_StanGirard/status/1657021618571313155?s=20). One viral tweet later, and [Quivr](https://github.com/StanGirard/quivr) was born.
## Choosing a vector database[#](https://supabase.com/customers/quivr#choosing-a-vector-database)
A critical piece of the tech stack was the vector store. Stan needed a place to store millions of embeddings. After comparing between Supabase, Pinecone, and Chroma, he settled on [Supabase Vector](https://supabase.com/vector), our open source vector offering for developing AI applications. The decision was driven largely by his familiarity with Postgres, and the tight integration with Vercel.
> Supabase Vector powered by pgvector allowed us to create a simple and efficient product. We are storing over 1.6 million embeddings and the performance and results are great. Open source develop can easily contribute thanks to the SQL syntax known by millions of developers.
> ![Stan Girard, Founder of Quivr. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fstan-girard-avatar.jpeg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> Stan Girard, Founder of Quivr.
## Building an open source community[#](https://supabase.com/customers/quivr#building-an-open-source-community)
It didn't take long for the Quivr community to grow. After the viral launch, the [Quivr repo](https://github.com/StanGirard/quivr) stayed at number 1 on [GitHub Trending](https://github.com/trending) for 4 days. Today, it has over 22,000 GitHub stars and 67 contributors. Supabase has been a key part of the open source stack since the beginning.
> Because Supabase is open source, the possibility of running it locally made it a better choice compared with other products like Auth0. Since Auth is integrated with the Vector database it made Quivr much simpler. Features like Storage and Edge Functions allowed us to expand Quivr's functionality while keeping the project simple.
> ![Stan Girard, Founder of Quivr. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fstan-girard-avatar.jpeg&w=64&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
> Stan Girard, Founder of Quivr.
## Launching 5000 databases[#](https://supabase.com/customers/quivr#launching-5000-databases)
One of the most pivotal growth events was getting picked up by [an influential YouTuber](https://www.youtube.com/watch?v=rFEbz93G9U8). His 11-minute overview of Quivr launched over 2000 Quivr projects on Supabase in one week. There are now 5,100 Quivr databases on Supabase, making it one of the most influential communities on the Supabase platform.
## Launching a hosted product[#](https://supabase.com/customers/quivr#launching-a-hosted-product)
Stan also launched a [hosted version of Quivr](https://www.quivr.app/), for users to sign up and get started immediately, without requiring any self-hosting infrastructure. Quivr's open source success has translated through their hosted platform, with 17,000 signups in just over 2 months, with 200 new users joining every day. The hosted database provides embedding storage for 1.6 million vectors and similarity search for over 100,000 files.
With 500 daily active users, the [Quivr.app](http://Quivr.app) is becoming the preferred way for users to create a second brain.
## Tech Stack[#](https://supabase.com/customers/quivr#tech-stack)
  * Backend: Fast API + Langchain, hosted on AWS Fargate
  * Frontend: Next.js, hosted on Vercel
  * Database: Supabase Vector, using pgvector
  * LLM: OpenAI, Anthropic, Nomic
  * Semantic search using GPT For ALL, Anthropic, and OpenAI
  * Auth: Supabase Auth


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

