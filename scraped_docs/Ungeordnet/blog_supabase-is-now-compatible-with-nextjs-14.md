---
url: https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14
scraped_at: 2025-05-25T09:47:05.201361
title: Supabase is now compatible with Next.js 14
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
# Supabase is now compatible with Next.js 14
01 Nov 2023
•
7 minute read
[![Jon Meyers avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdijonmusters.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Jon MeyersDeveloper Advocate](https://twitter.com/jonmeyers_io)
![Supabase is now compatible with Next.js 14](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Fnextjs-compatible.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
As part of [Next.js Conf 2023](https://nextjs.org/conf), the team at Vercel released [Next.js 14](https://nextjs.org/blog/next-14). The huge headline feature was...
[![Tweet from Lee Robinson about Next.js 14 containing no new APIs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Flee-tweet-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://x.com/leeerob/status/1717596944623649198?s=20)
That's right, the headline feature is no new features!
This may sound underwhelming at first, but is incredibly good news for the stability of Next.js. This release comes with a huge number of performance and stability improvements—such as [Server Actions](https://nextjs.org/docs/app/api-reference/functions/server-actions) being marked as stable. This means we can finally start promoting this fantastically simple way of authenticating users—entirely server-side!
`
1
export default async function Page() {
2
 const signIn = async () => {
3
  'use server'
4
  supabase.auth.signInWithOAuth({...})
5
 }
67
 return (
8
  <form action={signIn}>
9
   <button>Sign in with GitHub</button>
10
  </form>
11
 )
12
}
`
With [Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components), fetching data in Next.js became as simple as:
`
1
export default async function Page() {
2
 const { data } = await supabase.from('...').select()
3
 return ...
4
}
`
With Server Actions, you can now place mutation logic alongside the Server Components responsible for fetching data and rendering the page:
`
1
export default async function Page() {
2
 const { data } = await supabase.from('...').select()
34
 const createNote = async () => {
5
  'use server'
6
  await supabase.from('...').insert({...})
7
 }
89
 return ...
10
}
`
> To hear more about our thoughts on Next.js Conf and the release of Next.js 14, check out our [Twitter space](https://twitter.com/i/spaces/1yoKMwNWbRjJQ?s=20). [Yuri](https://twitter.com/yuricodesbot), [Alaister](https://twitter.com/alaisteryoung), [Terry](https://twitter.com/saltcod) and [myself](https://twitter.com/jonmeyers_io) talk through how we use Next.js at Supabase and what we personally found most exciting about Next.js Conf and the release of Next.js 14.
## Is Supabase compatible with Next.js 14?[#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#is-supabase-compatible-with-nextjs-14)
Yes, it is! So much so that [Guillermo Rauch](https://twitter.com/rauchg) shouted us out in the keynote!
[![Tweet showing Guillermo Rauch mentioning Supabase as one of the companies compatible with the Next.js App Router](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Fguillermo-tweet-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://x.com/supabase/status/1717658742743761239?s=20)
Since the release of the [App Router](https://nextjs.org/docs/app)—launched as beta with Next.js 13—we have been working closely with the team at Vercel to ensure that Supabase is fully compatible with every part of Next.js.
So for the [App Router](https://nextjs.org/docs/app), that's:
  * [Client Components](https://nextjs.org/docs/app/building-your-application/rendering/client-components)
  * [Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)
  * [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)
  * [Server Actions](https://nextjs.org/docs/app/api-reference/functions/server-actions)
  * [Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware)


And for the [Pages Router](https://nextjs.org/docs/pages):
  * [`getServerSideProps` function](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
  * [`getStaticProps` function](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
  * [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
  * [Page Components](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)


So why does it require work on the Supabase side to make it compatible with Next.js?
## Configuring Supabase to use Cookies[#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#configuring-supabase-to-use-cookies)
By default, [`supabase-js`](https://supabase.com/docs/reference/javascript/introduction) uses `localStorage` to store the user's session. This works well for client-side apps, but will fail when you try to use [`supabase-js`](https://supabase.com/docs/reference/javascript/introduction) in a Server Component, as there is no concept of 'localStorage' on the server.
To do this, we need to configure `supabase-js` to use cookies instead of `localStorage` when running on the server. But this code is a little verbose to ask people to duplicate across every app they build with Supabase:
`
1
const supabase = createClient(supabaseUrl, supabaseAnonKey, {
2
 auth: {
3
  flowType: 'pkce',
4
  autoRefreshToken: false,
5
  detectSessionInUrl: false,
6
  persistSession: true,
7
  storage: {
8
   getItem: async (key: string) => {
9
    cookieStore.get(key)
10
   },
11
   setItem: async (key: string, value: string) => {
12
    cookieStore.set(key, value)
13
   },
14
   removeItem: async (key: string) => {
15
    cookieStore.remove(key)
16
   },
17
  },
18
 },
19
})
`
That takes care of the server-side pieces of Next.js, but since we recommend securing your apps with [Row Level Security (RLS) policies](https://www.youtube.com/watch?v=Ow_Uzedfohk), you can safely access your user's session client-side too. Therefore, we need to tell the browser how access that cookie too:
`
1
const supabase = createClient(supabaseUrl, supabaseAnonKey, {
2
 auth: {
3
  flowType: 'pkce',
4
  autoRefreshToken: true,
5
  detectSessionInUrl: true,
6
  persistSession: true,
7
  storage: {
8
   getItem: async (key: string) => {
9
    return parse(document.cookie[key])
10
   },
11
   setItem: async (key: string, value: string) => {
12
    document.cookie = serialize(key, value)
13
   },
14
  },
15
  removeItem: async (key: string) => {
16
   document.cookie = serialize(key, '', {
17
    maxAge: 0,
18
   })
19
  },
20
 },
21
})
`
That is a lot of very confusing code! So we decided to [create a package called `@supabase/ssr`](https://supabase.com/docs/guides/auth/server-side/overview) that does all of this for you. Then we took it one step further and created a [Next.js and Supabase Starter Template](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs), so you can just focus on building your awesome app! 🚀
> Check out my [Next.js Conf talk](https://www.youtube.com/watch?t=3880&v=FdiX5rHS_0Y) to see this starter template in action!
## How do I get started?[#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#how-do-i-get-started)
One command:
`
1
npx create-next-app@latest -e with-supabase
`
The landing page will guide you through the process of creating a Supabase project and configuring your environment variables.
Build ~~in a weekend~~ on a Friday night! Scale to millions!
## Meme zone[#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#meme-zone)
As you probably know, we love memes, so we are signing off with one about the least controversial commands coming out of Next.js Conf:
[![Tweet from Terry Sutton running the `with-supabase` command](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Fterry-tweet-dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://x.com/saltcod/status/1718959967955275843?s=20)
## More Supabase and Next.js resources[#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#more-supabase-and-nextjs-resources)
  * [Next.js Quickstart](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
  * [Build a User Management App with Next.js](https://supabase.com/docs/guides/getting-started/tutorials/with-nextjs)
  * [Server-Side Auth Overview](https://supabase.com/docs/guides/auth/server-side/overview)
  * [Fetching and caching Supabase data in Next.js 13 Server Components](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components)
  * [Infinite scroll with Next.js, Framer Motion, and Supabase](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&text=Supabase%20is%20now%20compatible%20with%20Next.js%2014)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&text=Supabase%20is%20now%20compatible%20with%20Next.js%2014)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&t=Supabase%20is%20now%20compatible%20with%20Next.js%2014)
[Last postSupabase Beta October 20236 November 2023](https://supabase.com/blog/beta-update-october-2023)
[Next postpgvector vs Pinecone: cost and performance10 October 2023](https://supabase.com/blog/pgvector-vs-pinecone)
[nextjs](https://supabase.com/blog/tags/nextjs)[intgrations](https://supabase.com/blog/tags/intgrations)
On this page
  * [Is Supabase compatible with Next.js 14?](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#is-supabase-compatible-with-nextjs-14)
  * [Configuring Supabase to use Cookies](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#configuring-supabase-to-use-cookies)
  * [How do I get started?](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#how-do-i-get-started)
  * [Meme zone](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#meme-zone)
  * [More Supabase and Next.js resources](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#more-supabase-and-nextjs-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&text=Supabase%20is%20now%20compatible%20with%20Next.js%2014)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&text=Supabase%20is%20now%20compatible%20with%20Next.js%2014)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&t=Supabase%20is%20now%20compatible%20with%20Next.js%2014)
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
![Tweet from Lee Robinson about Next.js 14 containing no new APIs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Flee-tweet-dark.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

