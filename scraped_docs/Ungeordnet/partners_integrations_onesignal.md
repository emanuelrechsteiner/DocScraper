---
url: https://supabase.com/partners/integrations/onesignal
scraped_at: 2025-05-25T09:00:34.553144
title: OneSignal | Works With Supabase
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
[Back](https://supabase.com/partners/integrations)
![OneSignal](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fonesignal%2Fonesignal-logo.png&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# OneSignal
![OneSignal](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fonesignal%2Fonesignal-1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![OneSignal](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fonesignal%2Fonesignal-2.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
OneSignal is a tool that allows you to send messages across different channels such as the following to keep your users engaged.
  * Push notifications
  * SMS
  * Emails
  * In-app notifications


Combined with Supabase Database Webhooks and you can provide realtime cloud messaging experience to your users.
You can get started with OneSignal and Supabase [here](https://supabase.com/docs/guides/integrations/onesignal).
## Documentation
[OneSignal](https://onesignal.com/) is a tool that allows you to send messages across different channels such as the following to keep your users engaged.
  * Push notifications
  * SMS
  * Emails
  * In-app notifications


Here is William giving us the overview of how OneSignal can work with Supabase to send notifications to your users.
In this guide, we will build a similar app and steps you through how you can integrate OneSignal with Supabase to create a seamless cloud messaging experience for your users using Database webhooks and edge functions through a simple Next.js application.
![Entity Diagram](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/diagram.png)
We will create a simple ordering app and use Supabase Database Webhooks in conjunction with Edge Function to provide a real-time push notification experience.
You can find the complete example app along with the edge functions code to send the notifications [here](https://github.com/supabase-community/onesignal).
![Ordering app UI](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/app-ui.png)
## Step 1: Getting started
Before we dive into the code, this guide assumes that you have the following ready
  * [Supabase](https://supabase.com/) project created
  * [OneSignal](https://onesignal.com/) app created
  * [Supabase CLI](https://supabase.com/docs/guides/cli) installed on your machine


Let’s create a Next.js app with tailwind CSS pre-installed
`
1
npx create-next-app -e with-tailwindcss --ts
`
We will then install the Supabase and OneSignal SDK.
`
1
npm i @supabase/supabase-js
2
npm i react-onesignal
`
After that, follow the instructions [here](https://documentation.onesignal.com/docs/web-push-custom-code-setup) to set up OneSignal for the web. You can set the URL of the app as a local host if you want to run the app locally, or add a remote URL if you want to deploy your app to a public hosting. You should add the file you obtain in step 4 of the instruction under the `public` directory of your Next.js app like [this](https://github.com/supabase-community/onesignal/tree/main/app/public).
## Step 2: Build Next.js app
The Next.js app will have a login form for the user to sign in, and a button that they can press to make an order once they are signed in. Update the `index.tsx` file to the following.
pages/index.tsx
`
1
import { createClient, User } from '@supabase/supabase-js'
2
import type { NextPage } from 'next'
3
import Head from 'next/head'
4
import React, { useEffect, useState } from 'react'
5
import OneSignal from 'react-onesignal'
67
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!
8
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
9
const oneSignalAppId = process.env.NEXT_PUBLIC_ONESIGNAL_APP_ID!
1011
const supabase = createClient(supabaseUrl, supabaseAnonKey)
1213
const Home: NextPage = () => {
14
 const [user, setUser] = useState<User | null>(null)
1516
 const [oneSignalInitialized, setOneSignalInitialized] =
17
  useState<boolean>(false)
1819
 /**
20
  * Initializes OneSignal SDK for a given Supabase User ID
21
  * @param uid Supabase User ID
22
  */
23
 const initializeOneSignal = async (uid: string) => {
24
  if (oneSignalInitialized) {
25
   return
26
  }
27
  setOneSignalInitialized(true)
28
  await OneSignal.init({
29
   appId: oneSignalAppId,
30
   notifyButton: {
31
    enable: true,
32
   },
3334
   allowLocalhostAsSecureOrigin: true,
35
  })
3637
  await OneSignal.login(uid)
38
 }
3940
 const sendMagicLink = async (event: React.FormEvent<HTMLFormElement>) => {
41
  event.preventDefault()
42
  const { email } = Object.fromEntries(new FormData(event.currentTarget))
43
  if (typeof email !== 'string') return
4445
  const { error } = await supabase.auth.signInWithOtp({ email })
46
  if (error) {
47
   alert(error.message)
48
  } else {
49
   alert('Check your email inbox')
50
  }
51
 }
5253
 // Place a order with the selected price
54
 const submitOrder = async (event: React.FormEvent<HTMLFormElement>) => {
55
  event.preventDefault()
56
  const { price } = Object.fromEntries(new FormData(event.currentTarget))
57
  if (typeof price !== 'string') return
5859
  const { error } = await supabase
60
   .from('orders')
61
   .insert({ price: Number(price) })
62
  if (error) {
63
   alert(error.message)
64
  }
65
 }
6667
 useEffect(() => {
68
  const initialize = async () => {
69
   const initialUser = (await supabase.auth.getUser())?.data.user
70
   setUser(initialUser ?? null)
71
   if (initialUser) {
72
    initializeOneSignal(initialUser.id)
73
   }
74
  }
7576
  initialize()
7778
  const authListener = supabase.auth.onAuthStateChange(
79
   async (event, session) => {
80
    const user = session?.user ?? null
81
    setUser(user)
82
    if (user) {
83
     initializeOneSignal(user.id)
84
    }
85
   }
86
  )
8788
  return () => {
89
   authListener.data.subscription.unsubscribe()
90
  }
91
 }, [])
9293
 return (
94
  <>
95
   <Head>
96
    <title>OneSignal Order Notification App</title>
97
    <link rel="icon" href="/favicon.ico" />
98
   </Head>
99100
   <main className="flex items-center justify-center min-h-screen bg-black">
101
    {user ? (
102
     <form className="flex flex-col space-y-2" onSubmit={submitOrder}>
103
      <select
104
       className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded block p-2"
105
       name="price"
106
      >
107
       <option value="100">$100</option>
108
       <option value="200">$200</option>
109
       <option value="300">$300</option>
110
      </select>
111
      <button
112
       type="submit"
113
       className="py-1 px-4 text-lg bg-green-400 rounded"
114
      >
115
       Place an Order
116
      </button>
117
     </form>
118
    ) : (
119
     <form className="flex flex-col space-y-2" onSubmit={sendMagicLink}>
120
      <input
121
       className="border-green-300 border rounded p-2 bg-transparent text-white"
122
       type="email"
123
       name="email"
124
       placeholder="Email"
125
      />
126
      <button
127
       type="submit"
128
       className="py-1 px-4 text-lg bg-green-400 rounded"
129
      >
130
       Send Magic Link
131
      </button>
132
     </form>
133
    )}
134
   </main>
135
  </>
136
 )
137
}
138139
export default Home
`
There is quite a bit of stuff going on here, but basically, it’s creating a simple UI for the user to sign in using the [magic link](https://supabase.com/docs/guides/auth/auth-magic-link), and once the user is signed in, will initialize OneSignal to ask the user to receive notifications on the website.
Notice that inside the `initializeOneSignal()` function, we use the Supabase user ID a to log the user into OneSignal. This allows us to later send push notifications to the user using their Supabase user ID from the backend, which is very handy.
`
1
await OneSignal.login(uid)
`
The front-end side of things is done here. Let’s get into the backend.
We also need to set our environment variables. Create a `.env.local` file and use the following template to set the environment variables. You can find your Supabase configuration in your dashboard under `settings > API`, and you can find the OneSignal app ID from `Settings > Keys & IDs`
`
1
NEXT_PUBLIC_SUPABASE_URL=YOUR_SUPABASE_URL
2
NEXT_PUBLIC_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY
3
NEXT_PUBLIC_ONESIGNAL_APP_ID=YOUR_ONESIGNAL_APP_ID
`
![Where to find OneSignal App ID](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/onesignal-app-id.png)
## Step 3: Create the Edge Function
Let’s create an edge function that will receive [database webhooks](https://supabase.com/docs/guides/database/webhooks) from the database and calls the OneSignal API to send the push notification.
`
1
supabase functions new notify
`
Replace the contents of `supabase/functions/notify/index.ts` with the following
`
1
import { serve } from 'https://deno.land/std@0.177.0/http/server.ts'
2
import * as OneSignal from 'https://esm.sh/@onesignal/node-onesignal@1.0.0-beta7'
34
const _OnesignalAppId_ = Deno.env.get('ONESIGNAL_APP_ID')!
5
const _OnesignalUserAuthKey_ = Deno.env.get('USER_AUTH_KEY')!
6
const _OnesignalRestApiKey_ = Deno.env.get('ONESIGNAL_REST_API_KEY')!
7
const configuration = OneSignal.createConfiguration({
8
 userKey: _OnesignalUserAuthKey_,
9
 appKey: _OnesignalRestApiKey_,
10
})
1112
const onesignal = new OneSignal.DefaultApi(configuration)
1314
serve(async (req) => {
15
 try {
16
  const { record } = await req.json()
1718
  // Build OneSignal notification object
19
  const notification = new OneSignal.Notification()
20
  notification.app_id = _OnesignalAppId_
21
  notification.include_external_user_ids = [record.user_id]
22
  notification.contents = {
23
   en: `You just spent $${record.price}!`,
24
  }
25
  const onesignalApiRes = await onesignal.createNotification(notification)
2627
  return new Response(
28
   JSON.stringify({ onesignalResponse: onesignalApiRes }),
29
   {
30
    headers: { 'Content-Type': 'application/json' },
31
   }
32
  )
33
 } catch (err) {
34
  console.error('Failed to create OneSignal notification', err)
35
  return new Response('Server error.', {
36
   headers: { 'Content-Type': 'application/json' },
37
   status: 400,
38
  })
39
 }
40
})
`
If you see bunch of errors in your editor, it's because your editor is not configured to use Deno. Follow the official setup guide [here](https://deno.land/manual@v1.28.3/getting_started/setup_your_environment) to setup your IDE to use Deno.
The function receives a `record` object, which is the row inserted in your `orders` table, and constructs a notification object to then send to OneSignal to deliver the push notification.
We also need to set the environment variable for the function. Create a `.env` file under your `supabase` directory and paste the following.
`
1
ONESIGNAL_APP_ID=YOUR_ONESIGNAL_APP_ID
2
USER_AUTH_KEY=YOUR_USER_AUTH_KEY
3
ONESIGNAL_REST_API_KEY=YOUR_ONESIGNAL_REST_API_KEY
`
`ONESIGNAL_APP_ID` and `ONESIGNAL_REST_API_KEY` can be found under `Settings > Keys & IDs` of your OneSignal app, and `USER_AUTH_KEY` can be found by going to `Account & API Keys` page by clicking your icon in the top right corner and scrolling to the `User Auth Key` section.
![Where to find OneSignal User Auth Key](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/onesignal-api-key.png)
Once your environment variables are filled in, you can run the following command to set the environment variable.
`
1
supabase secrets set --env-file ./supabase/.env
`
At this point, the function should be ready to be deployed! Run the following command to deploy your functions to the edge! The `no-verify-jwt` flag is required if you plan to call the function from a webhook.
`
1
supabase functions deploy notify --no-verify-jwt
`
## Step 4: Setting up the Supabase database
Finally, we get to set up the database! Run the following SQL to set up the `orders` table.
`
1
create table
2
 if not exists public.orders (
3
  id uuid not null primary key default uuid_generate_v4 (),
4
  created_at timestamptz not null default now (),
5
  user_id uuid not null default auth.uid (),
6
  price int8 not null
7
 );
`
As you can see, the `orders` table has 4 columns and 3 of them have default values. That means all we need to send from the front-end app is the price. That is why our insert statement looked very simple.
`
1
const { error } = await supabase.from('orders').insert({
2
 price: 100,
3
})
`
Let’s also set up the webhook so that whenever a new row is inserted in the `orders` table, it calls the edge function. Go to `Database > Webhooks` and create a new Database Webhook. The table should be set to `orders` and Events should be inserted. The type should be HTTP Request, the HTTP method should be POST, and the URL should be the URL of your edge function. Hit confirm to save the webhook configuration.
![Supabase Webhooks configuration](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/webhook.png)
At this point, the app should be complete! Run your app locally with `npm run dev`, or deploy your app to a hosting service and see how you receive a push notification when you place an order! Remember that if you decide to deploy your app to a hosting service, you would need to create another OneSignal app configured for your local address.
![Ordering app UI](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/app-ui.png)
## Resources
This particular example was using Next.js, but you can apply the same principles to implement send push notification, SMS, Emails, and in-app-notifications on other platforms as well.
  * [OneSignal + Flutter + Supabase example](https://github.com/OneSignalDevelopers/onesignal-supabase-sample-integration-supabase)
  * [OneSignal Mobile Quickstart](https://documentation.onesignal.com/docs/mobile-sdk-setup)
  * [OneSignal Documentation](https://documentation.onesignal.com/docs/onesignal-platform)
  * [OneSignal Onboarding guide](https://documentation.onesignal.com/docs/onboarding-with-onesignal)


## Details
DeveloperOneSignal
Category[Messaging](https://supabase.com/partners/integrations#messaging)
Website[onesignal.com](https://onesignal.com/)
Documentation[Learn](https://documentation.onesignal.com/docs)
Third-party integrations and docs are managed by Supabase partners.
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

