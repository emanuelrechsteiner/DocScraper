---
url: https://supabase.com/blog/using-supabase-replit
scraped_at: 2025-05-25T09:49:19.066795
title: Using Supabase in Replit
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
# Using Supabase in Replit
11 Mar 2021
•
4 minute read
[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Ant WilsonCTO and Co-Founder](https://github.com/awalias)
![Using Supabase in Replit](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Freplit-og.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Replit.com](http://replit.com) is an awesome new browser based IDE where you can code alone or collaboratively with friends using their awesome multiplayer features! It's particularly useful for education, and sharing code examples with others.
They support a ton of different languages and execution environments and even recently introduced a simple key value store you can use to persist data.
As a Replit user, if you want to access larger amounts of data direct from your repl, or if you fancy accessing some super-powerful query tools, at some point you may want to start interacting with a relational database. Supabase is a good fit here; just like Replit, you don't need to worry about servers, and hosting, you can just click a few buttons and get a fully featured relational database which you can start communicating with directly from javacript, using supabase-js.
Here's how to start a Supabase + Node.js repl:
Sign up for [replit.com](http://replit.com) and hit new repl in the top left
![Untitled-2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-march%2Fu3dljulzsyqu58i75epn.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Select node.js, give it a name, and click Create repl
![Untitled-1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-march%2F7rcfbb12sfabevto571j.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Import supabase's createClient method and hit run to install the required libs:
`
1
const { createClient } = require('@supabase/supabase-js')
`
Setup a new Supabase project and grab the URL and anon key from Settings > API. Create the client in javascript using:
`
1
const supabase = createClient(
2
 'https://ajsstlnzcmdmzbtcgbbd.supabase.co',
3
 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
4
)
`
![Untitled-3](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-march%2F5j5aqyjdh74qm83slmli.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Now that supabase is connected you'll want to add some data to your db, you can grab any SQL dataset on the web, or make your own, but the fasted way to test is to open the SQL tab in the Supabase dashboard and click the Countries sample database and click Run.
![Untitled-4](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-march%2F54yykm6h9hqpric87zad.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
From within your repl you can now query your countries table like:
`
1
// .then() syntax
2
supabase.
3
 .from('countries')
4
 .select('*')
5
 .limit(5)
6
 .then(console.log)
7
 .catch(console.error)
89
// or...
10
// async/await syntax
11
const main = async() => {
12
 const { data, error } = supabase
13
  .from('countries')
14
  .select('*')
15
  .limit(5)
1617
 if (error) {
18
  console.log(error)
19
  return
20
 }
2122
 console.log(data)
23
}
24
main()
`
Once this is working, if you want to learn more about the [query interface](https://supabase.com/docs/reference/javascript/filter) you might want to try some of these challenges:
`
1
// 1. List all the countries in Antarctica
2
// 2. Fetch the iso3 code of the country with ID 3
3
// 3. List the countries with 'Island' in the name
4
// 4. Count the number of countries that start with 'Z' or 'Q'
5
// 5. Fetch all the Countries where continents is null
`
There are full solutions provided in the video version of this blog, but some examples you may find useful are:
`
1
// or
2
const { data, error } = await supabase
3
 .from('cities')
4
 .select('name, country_id')
5
 .or('id.eq.20,id.eq.30')
67
// is
8
const { data, error } = await supabase.from('cities').select('name, country_id').is('name', null)
910
// in
11
const { data, error } = await supabase
12
 .from('cities')
13
 .select('name, country_id')
14
 .in('name', ['Rio de Janeiro', 'San Francisco'])
1516
// neq (not equal to)
17
const { data, error } = await supabase
18
 .from('cities')
19
 .select('name, country_id')
20
 .neq('name', 'The shire')
2122
// full docs here: /docs/reference/javascript/filter
`
We look forward to showing off some more Supabase + Replit examples.
You can find my example repl here: <https://repl.it/@awalias/supabase-test#index.js>
Supabase has a Free Plan, head over to <https://supabase.com/dashboard> to get started.
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&text=Using%20Supabase%20in%20Replit)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&text=Using%20Supabase%20in%20Replit)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&t=Using%20Supabase%20in%20Replit)
[Last postDevelopers stay up to date with intheloop.dev22 March 2021](https://supabase.com/blog/In-The-Loop)
[Next postToad, a link shortener with simple APIs for low-coders8 March 2021](https://supabase.com/blog/toad-a-link-shortener-with-simple-apis-for-low-coders)
[replit](https://supabase.com/blog/tags/replit)[node-js](https://supabase.com/blog/tags/node-js)[postgres](https://supabase.com/blog/tags/postgres)
On this page
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&text=Using%20Supabase%20in%20Replit)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&text=Using%20Supabase%20in%20Replit)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-replit&t=Using%20Supabase%20in%20Replit)
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

