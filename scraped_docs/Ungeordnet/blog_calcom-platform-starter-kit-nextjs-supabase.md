---
url: https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase
scraped_at: 2025-05-25T09:09:01.024892
title: Cal.com launches Expert Marketplace built with Next.js and Supabase.
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
# Cal.com launches Expert Marketplace built with Next.js and Supabase.
18 Jun 2024
•
7 minute read
[![Richard Poelderl avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fp6l-richard.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Richard PoelderlGuest Author](https://github.com/p6l-richard)
[![Peer Richelsen avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2FPeerRich.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Peer RichelsenGuest Author](https://github.com/PeerRich)
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Cal.com launches Expert Marketplace built with Next.js and Supabase.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fcalcom_platform_starter%2Fcalcom_platform_starter_og.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Cal.com Platform Starter Kit is live on Product Hunt! Upvote now!](https://go.cal.com/producthunt)
Contrary to popular belief, due to the [biggest online beef marketing campaign](https://www.linkedin.com/posts/rajiv-ayyangar_the-product-hunt-showdown-of-the-century-activity-7184589230231166977-zqlv?utm_source=share&utm_medium=member_desktop) in modern history, Cal.com and Supabase are actually supa good friends, united by a common mission to build open source software.
So when the Cal.com team reached out about collaborating on their new platform starter kit, we were excited to work together. Finally we could collaborate on a [Product Hunt launch](https://go.cal.com/producthunt) instead of competing against each other.
## What's the stack?[#](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#whats-the-stack)
Initially the application was built to be run on SQLite. However, once requirements grew to include file storage, the Cal.com team remembered their Supabase frenemies and luckily, thanks to Prisma and Supabase, switching things over to Postgres three days before launch was a breeze.
## Prisma configuration for usage with Postgres on Supabase[#](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#prisma-configuration-for-usage-with-postgres-on-supabase)
When working with Prisma, your application will connect directly to your Postgres databases hosted on Supabase. To handle connection management efficiently, especially when working with serverless applications like Next.js, Supabase provides a connection pooler called [Supavisor](https://supabase.com/blog/supavisor-1-million) to make sure your database runs efficiently with increasing traffic.
The configuration is specified in the `schema.prisma` file where you provide the following connection strings:
schema.prisma
`
1
datasource db {
2
 provider = "postgresql"
3
 url    = env("POSTGRES_PRISMA_URL")
4
 directUrl = env("POSTGRES_URL_NON_POOLING")
5
 schemas  = ["prisma"] // see multi-schema support below
6
}
`
This loads the relevant Supabase connections strings from your `.env` file
.env
`
1
POSTGRES_PRISMA_URL="postgres://postgres.YOUR-PROJECT-REF:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres?pgbouncer=true&connection_limit=1" # Transaction Mode
2
POSTGRES_URL_NON_POOLING="postgres://postgres.YOUR-PROJECT-REF:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres" # Session Mode
`
You can find the values in the [project connect page](https://supabase.com/dashboard/project/_?showConnect=true) of your Supabase Dashboard.
For more details on using Prisma with Supabase, read the [official docs](https://supabase.com/partners/integrations/prisma).
### Multischema support in Prisma[#](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#multischema-support-in-prisma)
In Supabase the `public` schema is exposed via the autogenerated [PostgREST](https://supabase.com/docs/guides/api) API, which allows you to connect with your database from any environment that speaks HTTPS using the [Supabase client libraries](https://supabase.com/docs/guides/api/rest/client-libs) like [supabase-js](https://supabase.com/docs/reference/javascript/introduction) for example.
Since Prisma connects directly to your database, it's advisable to put your data on a separate schema that is not exposed via the API.
We can do this by enabling `multischema` support in the `schema.prisma` file:
schema.prisma
`
1
generator client {
2
 provider = "prisma-client-js"
3
 previewFeatures = ["multiSchema"]
4
}
56
model Account {
7
 id        String @id @default(cuid())
8
 // ...
910
 @@schema("prisma")
11
}
`
## React Dropzone and Supabase Storage for profile image uploads[#](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#react-dropzone-and-supabase-storage-for-profile-image-uploads)
[Supabase Storage](https://supabase.com/storage) is an S3 compatible cloud-based object store that allows you to store files securely. It is conveniently integrated with [Supabase Auth](https://supabase.com/auth) allowing you to easily limit access for uploads and downloads.
Cal.com's Platforms Starter Kit runs their authentication on Next.js' [Auth.js](https://authjs.dev/). Luckily though, Supabase Storage is supa flexible, allowing you to easily create signed upload URLs server-side to then upload assets from the client-side -- no matter which tech you choose to use for handling authentication for your app.
To facilitate this, we can create an API route in Next.js to generate these signed URLs:
src/app/api/supabase/storage/route.ts
`
1
import { auth } from '@/auth'
2
import { env } from '@/env'
3
import { createClient } from '@supabase/supabase-js'
45
export const dynamic = 'force-dynamic' // defaults to auto
6
export async function GET(request: Request) {
7
 try {
8
  const session = await auth()
9
  if (!session || !session.user.id) {
10
   return new Response('Unauthorized', { status: 401 })
11
  }
12
  const {
13
   user: { id },
14
  } = session
15
  // Generate signed upload url to use on client.
16
  const supabaseAdmin = createClient(env.NEXT_PUBLIC_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY)
1718
  const { data, error } = await supabaseAdmin.storage
19
   .from('avatars')
20
   .createSignedUploadUrl(id, { upsert: true })
21
  console.log(error)
22
  if (error) throw error
2324
  return new Response(JSON.stringify(data), {
25
   status: 200,
26
  })
27
 } catch (e) {
28
  console.error(e)
29
  return new Response('Internal Server Error', { status: 500 })
30
 }
31
}
`
The `createSignedUploadUrl` method returns a `token` which we can then use on the client-side to upload the file selected by [React Dropzone](https://react-dropzone.js.org/):
src/app/dashboard/settings/_components/supabase-react-dropzone.tsx
`
1
'use client'
23
import { env } from '@/env'
4
import { createClient } from '@supabase/supabase-js'
5
import Image from 'next/image'
6
import React, { useState } from 'react'
7
import { useDropzone } from 'react-dropzone'
89
export default function SupabaseReactDropzone({ userId }: { userId?: string } = {}) {
10
 const supabaseBrowserClient = createClient(
11
  env.NEXT_PUBLIC_SUPABASE_URL,
12
  env.NEXT_PUBLIC_SUPABASE_ANON_KEY
13
 )
14
 const { acceptedFiles, fileRejections, getRootProps, getInputProps } = useDropzone({
15
  maxFiles: 1,
16
  accept: {
17
   'image/jpeg': [],
18
   'image/png': [],
19
  },
20
  onDropAccepted: async (acceptedFiles) => {
21
   setAvatar(null)
22
   console.log(acceptedFiles)
23
   const { path, token }: { path: string; token: string } = await fetch(
24
    '/api/supabase/storage'
25
   ).then((res) => res.json())
2627
   const { data, error } = await supabaseBrowserClient.storage
28
    .from('avatars')
29
    .uploadToSignedUrl(path, token, acceptedFiles[0])
30
  },
31
 })
3233
 return (
34
  <div className="mx-auto mt-4 grid w-full gap-2">
35
   <div {...getRootProps({ className: 'dropzone' })}>
36
    <input {...getInputProps()} />
37
    <p>Drag 'n' drop some files here, or click to select files</p>
38
    <em>(Only *.jpeg and *.png images will be accepted)</em>
39
   </div>
40
  </div>
41
 )
42
}
`
## Custom Next.js Image loader for Supabase Storage[#](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#custom-nextjs-image-loader-for-supabase-storage)
Supabase Storage also conveniently integrates with the Next.js Image paradigm, by creating a [custom loader](https://supabase.com/docs/guides/storage/serving/image-transformations#nextjs-loader):
src/lib/supabase-image-loader.ts
`
1
import { env } from '@/env'
23
export default function supabaseLoader({ src, width, quality }) {
4
 return `${env.NEXT_PUBLIC_SUPABASE_URL}/storage/v1/object/public/${src}?width=${width}&quality=${quality || 75}`
5
}
`
Now we just need to register the custom loader in the `next.config.js` file:
next.config.js
`
1
images: {
2
 loader: "custom",
3
 loaderFile: "./src/lib/supabase-image-loader.ts",
4
},
`
and we can start using the Next.js Image component by simply providing the file path within Supabase Storage:
`
1
<Image
2
 alt="Expert image"
3
 className="aspect-square rounded-md object-cover"
4
 src="your-bucket-name/image.png"
5
 height="64"
6
 width="64"
7
/>
`
## Supabase Vercel Integration for one-click deploys[#](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#supabase-vercel-integration-for-one-click-deploys)
Supabase also provides a [Vercel Integration](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase) which makes managing environment variables across branches and deploy previews a breeze. When you connect your Supabase project to your Vercel project, the integration will keep your environment variables in sync.
And when using the [Vercel Deploy Button](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fcalcom%2Fplatform-starter-kit%2Ftree%2Fmain&env=NEXT_PUBLIC_REFRESH_URL,AUTH_SECRET,AUTH_TRUST_HOST,NEXT_PUBLIC_CAL_OAUTH_CLIENT_ID,NEXT_PUBLIC_CAL_API_URL,CAL_SECRET&envDescription=You%20can%20see%20how%20to%20populate%20the%20environment%20variables%20in%20our%20starter%20example%20%E2%86%92&envLink=https%3A%2F%2Fgithub.com%2Fcalcom%2Fplatform-starter-kit%2Ftree%2Fmain%2F.env.example&project-name=cal-platform-starter&repository-name=cal-platform-starter&demo-title=Cal.com%20Experts&demo-description=A%20marketplace%20to%20book%20appointments%20with%20experts&demo-url=https%3A%2F%2Fexperts.cal.com&demo-image=https%3A%2F%2Fgithub.com%2Fcalcom%2Fplatform-starter-kit%2Fassets%2F8019099%2F2e58f8da-a110-4a45-b9a4-dcffb45f9baa&integration-ids=oac_VqOgBHqhEoFTPzGkPd7L0iH6&external-id=https%3A%2F%2Fgithub.com%2Fcalcom%2Fplatform-starter-kit%2Ftree%2Fmain) the integration will automatically create a new Supabase project for you, populate the environment variables, and even run the database migration and seed scripts, meaning you're up and running with a full end-to-end application in no time!
## Contributing to open source[#](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#contributing-to-open-source)
Both Cal.com and Supabase are on a mission to create open source software, therefore this new platform starter kit is of course also open-source, allowing you to spin up your own marketplace with convenient scheduling in minutes! Of course this also means that you are very welcome to contribute additional features to the starter kit! You can [find the repository on GitHub](https://github.com/calcom/platform-starter-kit)!
## Resources[#](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#resources)
  * [Cal.com Platform Starter Kit GitHub repository](https://github.com/calcom/platform-starter-kit)
  * [Video explaining the platform starter kit](https://www.youtube.com/watch?v=wwo07ghiNn4)
  * [Cal.com](https://cal.com/)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalcom-platform-starter-kit-nextjs-supabase&text=Cal.com%20launches%20Expert%20Marketplace%20built%20with%20Next.js%20and%20Supabase.)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalcom-platform-starter-kit-nextjs-supabase&text=Cal.com%20launches%20Expert%20Marketplace%20built%20with%20Next.js%20and%20Supabase.)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalcom-platform-starter-kit-nextjs-supabase&t=Cal.com%20launches%20Expert%20Marketplace%20built%20with%20Next.js%20and%20Supabase.)
[Last postSelf-host Maps with Protomaps and Supabase Storage19 June 2024](https://supabase.com/blog/self-host-maps-storage-protomaps)
[Next postThe open source Kahoot alternative9 May 2024](https://supabase.com/blog/meetup-kahoot-alternative)
[open-source](https://supabase.com/blog/tags/open-source)[partnerships](https://supabase.com/blog/tags/partnerships)[nextjs](https://supabase.com/blog/tags/nextjs)
On this page
  * [What's the stack?](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#whats-the-stack)
  * [Prisma configuration for usage with Postgres on Supabase](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#prisma-configuration-for-usage-with-postgres-on-supabase)
  * [React Dropzone and Supabase Storage for profile image uploads](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#react-dropzone-and-supabase-storage-for-profile-image-uploads)
  * [Custom Next.js Image loader for Supabase Storage](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#custom-nextjs-image-loader-for-supabase-storage)
  * [Supabase Vercel Integration for one-click deploys](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#supabase-vercel-integration-for-one-click-deploys)
  * [Contributing to open source](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#contributing-to-open-source)
  * [Resources](https://supabase.com/blog/calcom-platform-starter-kit-nextjs-supabase#resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalcom-platform-starter-kit-nextjs-supabase&text=Cal.com%20launches%20Expert%20Marketplace%20built%20with%20Next.js%20and%20Supabase.)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalcom-platform-starter-kit-nextjs-supabase&text=Cal.com%20launches%20Expert%20Marketplace%20built%20with%20Next.js%20and%20Supabase.)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fcalcom-platform-starter-kit-nextjs-supabase&t=Cal.com%20launches%20Expert%20Marketplace%20built%20with%20Next.js%20and%20Supabase.)
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

