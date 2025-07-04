---
url: https://supabase.com/blog/edge-functions-faster-smaller
scraped_at: 2025-05-25T08:39:35.763370
title: Edge Functions are now 2x smaller and boot 3x faster
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
# Edge Functions are now 2x smaller and boot 3x faster
12 Sep 2024
•
7 minute read
[![Nyannyacha avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fnyannyacha.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)NyannyachaEngineering](https://github.com/nyannyacha)
![Edge Functions are now 2x smaller and boot 3x faster](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fedge-functions-faster-smaller%2Fedge-fns-faster-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We’ve rolled out some exciting updates to Edge Functions which bring significant reductions to function size and boot time. If you’re using [npm modules](https://supabase.com/blog/edge-functions-node-npm) in your functions, you should see function sizes being halved and boot time reduced by 300% in most cases.
To take advantage of these performance improvements, you can redeploy your functions using the Supabase CLI v1.192.5 or later.
Let’s compare the bundle size and boot time using some popular examples.
## Benchmarks[#](https://supabase.com/blog/edge-functions-faster-smaller#benchmarks)
**Supabase JavaScript Client:**
| **CLI 1.190.0**| **CLI 1.192.5**| **Change**  
---|---|---|---  
Bundle size| 1.487MB| 640.4KB| -232.34%  
Boot time| 275ms| 25ms| -1100%  
`
1
import { createClient } from 'npm:@supabase/supabase-js@2'
23
Deno.serve(async (_req) => {
4
 try {
5
  const supabase = createClient(
6
   Deno.env.get('SUPABASE_URL') ?? '',
7
   Deno.env.get('SUPABASE_ANON_KEY') ?? '',
8
   { global: { headers: { Authorization: req.headers.get('Authorization')! } } }
9
  )
1011
  const { data, error } = await supabase.from('countries').select('*')
1213
  if (error) {
14
   throw error
15
  }
1617
  return new Response(JSON.stringify({ data }), {
18
   headers: { 'Content-Type': 'application/json' },
19
   status: 200,
20
  })
21
 } catch (err) {
22
  return new Response(String(err?.message ?? err), { status: 500 })
23
 }
24
})
`
**OpenAI:**
| **CLI 1.190.0**| **CLI 1.192.5**| **Change**  
---|---|---|---  
Bundle size| 2.533MB| 1.045MB| -242.39%  
Boot time| 459ms| 57ms| -805.26%  
`
1
import OpenAI from 'npm:openai@4.57.3'
23
const client = new OpenAI({
4
 apiKey: Deno.env.get('OPEN_AI_KEY'),
5
})
67
Deno.serve(async (req) => {
8
 const { query } = await req.json()
910
 const chatCompletion = await client.chat.completions.create({
11
  messages: [{ role: 'user', content: 'Say this is a test' }],
12
  model: 'gpt-3.5-turbo',
13
 })
1415
 return new Response(chatCompletion)
16
})
`
**Drizzle / node-postgres:**
| **CLI 1.190.0**| **CLI 1.192.5**|  Change  
---|---|---|---  
Bundle size| 929.5kB| 491.3kB| -189.19%  
Boot time| 301ms| 83ms| -362.65%  
`
1
import { drizzle } from 'npm:drizzle-orm@0.33.0/node-postgres'
2
import pg from 'npm:pg@8.12.0'
3
const { Client } = pg
45
import { pgTable, serial, text, varchar } from 'npm:drizzle-orm@0.33.0/pg-core'
67
export const users = pgTable('users', {
8
 id: serial('id').primaryKey(),
9
 fullName: text('full_name'),
10
 phone: varchar('phone', { length: 256 }),
11
})
1213
const client = new Client({
14
 connectionString: Deno.env.get('SUPABASE_DB_URL'),
15
})
1617
await client.connect()
18
const db = drizzle(client)
1920
Deno.serve(async (req) => {
21
 const allUsers = await db.select().from(users)
22
 console.log(allUsers)
2324
 return new Response('ok')
25
})
`
## How did we achieve these gains?[#](https://supabase.com/blog/edge-functions-faster-smaller#how-did-we-achieve-these-gains)
Let’s dive into the technical details.
### Lazy evaluating dependencies and reducing npm package section size[#](https://supabase.com/blog/edge-functions-faster-smaller#lazy-evaluating-dependencies-and-reducing-npm-package-section-size)
We use [eszip format](https://github.com/denoland/eszip) to bundle your function code and its dependencies when you deploy a function.
This binary format extracts the dependencies a function references from Deno's module graph and serializes them into a single file. It eliminates network requests at run time and avoids conflicts between dependencies.
This approach worked reasonably well until we added npm support. When functions started using npm modules, bundle sizes and boot times increased.
When a function is invoked, Edge Runtime loads the eszip binary for the function and passes it to a JavaScript worker (ie. isolate). The worker then loads the necessary modules from the eszip.
In the original implementation, before passing an eszip binary to the worker's module loader, we first checked the integrity of its contents. Each entry in it will have a checksum computed with the SHA-256 function immediately following the body bytes. By reading this and comparing it, we ensure that the eszip binary isn’t corrupted.
The problem is that calculating a checksum for every entry using SHA-256 is quite expensive, and we were pre-checking the integrity of all entries at a time when the worker doesn't even need that particular entry.
It is possible that some items that have been checked for integrity will not be referenced even if the worker reaches the end of its lifetime and reaches the end state.
Instead of performing the costly integrity check of all entries before passing it to the module loader, edge runtime lazily performs the integrity check whenever there is a request to load a specific entry from the eszip by the module loader.
This helped to significantly to reduce the boot times.
Another issue was that while serializing npm packages for embedding into eszip binaries, we used the JSON format. The entries in individual npm packages, which were already represented as bytes (`Vec<u8>`), were encoded as an array representation in JSON format (`[255, 216, 255, 224, 0, ...]`) instead of passing on as bytes, causing the outputs to bloat by up to 2x or more.
We refactored the serialization using the [`rkyv` crate](https://github.com/rkyv/rkyv) to encode this to lower to the byte level, which helped reducing the bundle sizes of eszip binaries containing npm packages.
You can find full details of the implementation in this PR <https://github.com/supabase/edge-runtime/pull/343>
### Using a more computationally efficient hashing function[#](https://supabase.com/blog/edge-functions-faster-smaller#using-a-more-computationally-efficient-hashing-function)
There was a [recent change](https://github.com/denoland/eszip/pull/181) in the eszip crate, which allowed the configuration of the source checksum.
This allowed us to switch to xxHash-3 over SHA_256 for the source checksums. Given that the checksums are used to ensure the integrity of sources in eszip, we could rely on a non-cryptographic hash algorithm that’s more computationally efficient.
![comparison of hash functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fedge-functions-faster-smaller%2Fhash-functions.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## How to redeploy your functions[#](https://supabase.com/blog/edge-functions-faster-smaller#how-to-redeploy-your-functions)
To get the advantage of these optimizations, follow these steps:
  * [Update Supabase CLI](https://supabase.com/docs/guides/cli/getting-started#updating-the-supabase-cli) to version is v1.195.2 or later.
  * Then, redeploy your functions by running `supabase functions deploy [FUNCTION_NAME]`


## Getting Help[#](https://supabase.com/blog/edge-functions-faster-smaller#getting-help)
[Supabase Edge Runtime](https://github.com/supabase/edge-runtime) is fully open-source, and we value community contributions. If you would like to make any improvements, feel free to dive into the source and [create an issue](https://github.com/supabase/edge-runtime/issues).
If you have any issues with Edge Functions in your hosted project, please request support via [superbase.help](http://supabase.help).
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&text=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&text=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&t=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)
[Last postLocal-first Realtime Apps with Expo and Legend-State23 September 2024](https://supabase.com/blog/local-first-expo-legend-state)
[Next postBuilding an Uber Clone with Flutter and Supabase5 September 2024](https://supabase.com/blog/flutter-uber-clone)
[functions](https://supabase.com/blog/tags/functions)
On this page
  * [Benchmarks](https://supabase.com/blog/edge-functions-faster-smaller#benchmarks)
  * [How did we achieve these gains?](https://supabase.com/blog/edge-functions-faster-smaller#how-did-we-achieve-these-gains)
    * [Lazy evaluating dependencies and reducing npm package section size](https://supabase.com/blog/edge-functions-faster-smaller#lazy-evaluating-dependencies-and-reducing-npm-package-section-size)
    * [Using a more computationally efficient hashing function](https://supabase.com/blog/edge-functions-faster-smaller#using-a-more-computationally-efficient-hashing-function)
  * [How to redeploy your functions](https://supabase.com/blog/edge-functions-faster-smaller#how-to-redeploy-your-functions)
  * [Getting Help](https://supabase.com/blog/edge-functions-faster-smaller#getting-help)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&text=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&text=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&t=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)
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

