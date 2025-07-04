---
url: https://supabase.com/partners/integrations/stytch
scraped_at: 2025-05-25T09:17:28.948292
title: Stytch | Works With Supabase
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
![Stytch](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fstytch%2Fstytch-logo.png&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Stytch
![Stytch](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fstytch%2Fstytch-1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Stytch](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fstytch%2Fstytch-2.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Stytch](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fstytch%2Fstytch-3.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
Stytch provides an all-in-one platform for passwordless auth. Stytch makes it easy for you to embed passwordless solutions into your websites and apps for better security, better conversion rates, and a better end user experience. Their easy-to-use SDKs and direct API access allows for maximum control and customization. In this example we will use Email magic links to create and log in our users, and Session management. There is an additional, optional step to enable Google One Tap which is an especially high-converting Google OAuth sign-up and login flow.
## Documentation
In this guide we will build a simple expense tracker web application using Stytch, Supabase, and Next.js.
[Stytch](https://stytch.com?utm_source=supabase&utm_medium=guide) provides an all-in-one platform for passwordless auth. Stytch makes it easy for you to embed passwordless solutions into your websites and apps for better security, better conversion rates, and a better end user experience. Their easy-to-use SDKs and direct API access allows for maximum control and customization. In this example we will use [Email magic links](https://stytch.com/products/email-magic-links?utm_source=supabase&utm_medium=guide) to create and log in our users, and Session management. There is an additional, optional step to enable [Google One Tap](https://stytch.com/blog/improving-conversion-with-google-one-tap?utm_source=supabase&utm_medium=guide) which is an especially high-converting Google OAuth sign-up and login flow.
We will leverage Supabase to store and authorize access to user data. Supabase makes it simple to set up Row Level Security (RLS) policies which ensure users can only read and write data that they are authorized to do so. If you do not already have a Supabase account, you will need to create one.
This guide will use [Next.js](https://nextjs.org/) which is a web application framework built on top of React. Stytch provides a [Node.js library](https://github.com/stytchauth/stytch-node) and a [React library](https://stytch.com/docs/sdks/javascript-sdk) which makes building Next.js apps super easy.
> Note: You can find a completed version of this project on [Github](https://github.com/stytchauth/stytch-nextjs-supabase).
## Step 0: Create a Stytch Account
If you already have a Stytch account you may skip this step.
Go to [Stytch](https://stytch.com?utm_source=supabase&utm_medium=guide), and create an account. Note that Stytch provides two ways to create an account, either via Google OAuth, or through Email magic links. This is the same user experience we will be building in this guide!
![Stytch redirect URL settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/01.png)
## Step 1: Set up Stytch redirect URLs
First we need to add the redirect URLs that will be used during the Email magic link flow. This step helps ensure bad actors cannot spoof your magic links and hijack redirects.
Navigate to your [redirect URL settings](https://stytch.com/dashboard/redirect-urls?utm_source=supabase&utm_medium=guide) in the Stytch dashboard, and under **Test environment** create an entry where the **URL** is `http://localhost:3000/api/authenticate` and the **Type** is `All`.
![Edit Stytch redirect URL settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/02.png)
After pressing **Confirm** , the redirect URLs dashboard will update to show your new entry. We will use this URL later on.
![Stytch redirect URL settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/03.png)
## Step 2: Create a Supabase project
From your [Supabase dashboard](https://supabase.com/dashboard/), click **New project**.
Enter a `Name` for your Supabase project.
Enter a secure `Database Password`.
Click **Create new project**. It may take a couple minutes for your project to be provisioned.
![New Supabase project settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/04.png)
## Step 3: Creating data in Supabase
Once your Supabase project is provisioned, click Table editor, then New table. This tool is available from the sidebar menu in the [Supabase dashboard](https://supabase.com/dashboard/).
Enter `expenses` as the **Name** field.
Select `Enable Row Level Security (RLS)`.
Add three new columns:
  * `user_id` as `text`
  * `title` as `text`
  * `value` as `float8`


Click **Save** to create the new table.
![Creating a new table](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/05.png)
From the Table editor view, select the expenses table and click **Insert row**.
Fill out the title and value fields (leave user_id blank for now) and click **Save**.
![Creating a new row](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/06.png)
Use **Insert Row** to further populate the table with expenses.
![Multiple rows](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/07.png)
## Step 4: Building a Next.js app
Using a terminal, create a new Next.js project:
`
1
npx create-next-app stytch-supabase-example
`
Next, within `stytch-supabase-example` create a `.env.local` file and enter the following values:
`
1
STYTCH_PROJECT_ENV=test
2
STYTCH_PROJECT_ID=GET_FROM_STYTCH_DASHBOARD
3
STYTCH_PUBLIC_TOKEN=GET_FROM_STYTCH_DASHBOARD
4
STYTCH_SECRET=GET_FROM_STYTCH_DASHBOARD
5
NEXT_PUBLIC_SUPABASE_URL=GET_FROM_SUPABASE_DASHBOARD
6
NEXT_PUBLIC_SUPABASE_KEY=GET_FROM_SUPABASE_DASHBOARD
7
SUPABASE_SIGNING_SECRET=GET_FROM_SUPABASE_DASHBOARD
`
> Note: Stytch values can be found in the project [dashboard](https://stytch.com/dashboard/api-keys?utm_source=supabase&utm_medium=guide) under **API Keys**.
![Stytch API keys](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/08.png)
> Note: Supabase values can be found under **Settings** > **API** for your project.
![Supabase API keys](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/09.png)
Start your Next.js development server to read in the new values from `.env.local`.
`
1
npm run dev
`
You should have a running Next.js application on `localhost:3000`.
## Step 5: Build the Login Form
Now we will replace the default Next.js home page with a login UI. We will use the Stytch React library.
> Note: Stytch provides direct API access for those that want to build login UI themselves
Install the `@stytch/stytch-react` library.
`
1
npm install @stytch/stytch-react
`
In the root directory, create a new folder named `components` and file in that folder named `/StytchLogin.js`. Within this file, paste the snippet below. This will configure, and style the Stytch React component to use Email magic links.
`
1
// components/StytchLogin.js
2
import React from 'react'
3
import { Stytch } from '@stytch/stytch-react'
45
const stytchConfig = {
6
 loginOrSignupView: {
7
  products: ['emailMagicLinks'],
8
  emailMagicLinksOptions: {
9
   loginRedirectURL: 'http://localhost:3000/api/authenticate',
10
   loginExpirationMinutes: 30,
11
   signupRedirectURL: 'http://localhost:3000/api/authenticate',
12
   signupExpirationMinutes: 30,
13
   createUserAsPending: true,
14
  },
15
 },
16
 style: {
17
  fontFamily: '"Helvetica New", Helvetica, sans-serif',
18
  width: '321px',
19
  primaryColor: '#0577CA',
20
 },
21
}
2223
const StytchLogin = ({ publicToken }) => {
24
 return (
25
  <Stytch
26
   publicToken={publicToken}
27
   loginOrSignupView={stytchConfig.loginOrSignupView}
28
   style={stytchConfig.style}
29
  />
30
 )
31
}
3233
export default StytchLogin
`
Additionally, create a profile component by creating a file called `Profile.js` in `/components`. We will use this component to render our expenses stored in Supabase later on.
`
1
// components/Profile.js
2
import React from 'react'
3
import Link from 'next/link'
45
export default function Profile({ user }) {
6
 return (
7
  <div>
8
   <h1>Welcome {user.userId}</h1>
9
   <h2>Your expenses</h2>
10
   {user.expenses?.length > 0 ? (
11
    user.expenses.map((expense) => (
12
     <p key={expense.id}>
13
      {expense.title}: ${expense.value}
14
     </p>
15
    ))
16
   ) : (
17
    <p>You have no expenses!</p>
18
   )}
1920
   <Link href="/api/logout" passHref>
21
    <button>
22
     <a>Logout</a>
23
    </button>
24
   </Link>
25
  </div>
26
 )
27
}
`
Finally, replace the contents of the file `/pages/index.js` to render our new `StytchLogin` and `Profile` components.
`
1
// pages/index.js
2
import styles from '../styles/Home.module.css'
3
import Profile from '../components/Profile'
4
import StytchLogin from '../components/StytchLogin'
56
const Index = ({ user, publicToken }) => {
7
 let content
8
 if (user) {
9
  content = <Profile user={user} />
10
 } else {
11
  content = <StytchLogin publicToken={publicToken} />
12
 }
1314
 return <div className={styles.main}>{content}</div>
15
}
1617
export async function getServerSideProps({ req, res }) {
18
 const user = null // Will update later
19
 return {
20
  props: { user, publicToken: process.env.STYTCH_PUBLIC_TOKEN },
21
 }
22
}
2324
export default Index
`
On `localhost:3000` there is now a login form prompting for your email address.
![Email login step one](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/10.png)
Enter your email address and press **Continue with email**.
![Email login step two](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/11.png)
In your inbox you will find a login request from your app.
![Email login step three](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/12.png)
However, if you click the link in the email you will get a 404. We need to build an API route to handle the email magic link authentication.
## Step 6: Authenticate and start a session
To make authentication easier we will use the Stytch Node.js library. Run
`
1
npm install stytch
`
Additionally, we will need to store the authenticated session in a cookie. Run
`
1
npm install cookies-next
`
Create a new folder named `utils` and inside a file named`stytchLogic.js` with the following contents
`
1
// utils/stytchLogic.js
2
import * as stytch from 'stytch'
3
import { getCookie, setCookies, removeCookies } from 'cookies-next'
45
export const SESSION_COOKIE = 'stytch_cookie'
67
let client
8
const loadStytch = () => {
9
 if (!client) {
10
  client = new stytch.Client({
11
   project_id: process.env.STYTCH_PROJECT_ID,
12
   secret: process.env.STYTCH_SECRET,
13
   env: process.env.STYTCH_PROJECT_ENV === 'live' ? stytch.envs.live : stytch.envs.test,
14
  })
15
 }
1617
 return client
18
}
1920
export const getAuthenticatedUserFromSession = async (req, res) => {
21
 const sessionToken = getCookie(SESSION_COOKIE, { req, res })
22
 if (!sessionToken) {
23
  return null
24
 }
2526
 try {
27
  const stytchClient = loadStytch()
28
  const resp = await stytchClient.sessions.authenticate({
29
   session_token: sessionToken,
30
  })
31
  return resp.session.user_id
32
 } catch (error) {
33
  console.log(error)
34
  return null
35
 }
36
}
3738
export const revokeAndClearSession = async (req, res) => {
39
 const sessionToken = getCookie(SESSION_COOKIE, { req, res })
4041
 if (sessionToken) {
42
  try {
43
   const stytchClient = loadStytch()
44
   await stytchClient.sessions.revoke({
45
    session_token: sessionToken,
46
   })
47
  } catch (error) {
48
   console.log(error)
49
  }
50
  removeCookies(SESSION_COOKIE, { req, res })
51
 }
5253
 return res.redirect('/')
54
}
5556
export const authenticateTokenStartSession = async (req, res) => {
57
 const { token, type } = req.query
58
 let sessionToken
59
 try {
60
  const stytchClient = loadStytch()
61
  const resp = await stytchClient.magicLinks.authenticate(token, {
62
   session_duration_minutes: 30,
63
  })
64
  sessionToken = resp.session_token
65
 } catch (error) {
66
  console.log(error)
67
  const errorString = JSON.stringify(error)
68
  return res.status(400).json({ errorString })
69
 }
7071
 setCookies(SESSION_COOKIE, sessionToken, {
72
  req,
73
  res,
74
  maxAge: 60 * 60 * 24,
75
  secure: true,
76
 })
7778
 return res.redirect('/')
79
}
`
This logic is responsible for setting up the Stytch client we will use to call the API. It provides functions we will use to login, logout, and validate user sessions.
In order to complete the email login flow, create a new file `pages/api/authenticate.js` with the contents:
`
1
// pages/api/authenticate.js
2
import { authenticateTokenStartSession } from '../../utils/stytchLogic'
34
export default async function handler(req, res) {
5
 return authenticateTokenStartSession(req, res)
6
}
`
We will also create a logout API endpoint with similar contents. In `pages/api/logout.js` include the following:
`
1
// pages/api/logout.js
2
import { revokeAndClearSession } from '../../utils/stytchLogic'
34
export default async function handler(req, res) {
5
 return revokeAndClearSession(req, res)
6
}
`
Finally, update `pages/index.js` by importing `getAuthenticatedUserFromSession`, and calling it to set the user variable in `getServerSideProps`.
`
1
// pages/index.js
2
import styles from '../styles/Home.module.css'
34
import StytchLogin from '../components/StytchLogin'
5
import Profile from '../components/Profile'
6
import { getAuthenticatedUserFromSession } from '../utils/stytchLogic'
78
const Index = ({ user, publicToken }) => {
9
 let content
10
 if (user) {
11
  content = <Profile user={user} />
12
 } else {
13
  content = <StytchLogin publicToken={publicToken} />
14
 }
1516
 return <div className={styles.main}>{content}</div>
17
}
1819
export async function getServerSideProps({ req, res }) {
20
 const userId = await getAuthenticatedUserFromSession(req, res)
21
 if (userId) {
22
  return {
23
   props: { user: { userId }, publicToken: process.env.STYTCH_PUBLIC_TOKEN },
24
  }
25
 }
26
 return {
27
  props: { publicToken: process.env.STYTCH_PUBLIC_TOKEN },
28
 }
29
}
3031
export default Index
`
Return to `localhost:3000`, and login again by sending yourself a new email. Upon clicking through in the email you should be presented with “Welcome $USER_ID”. If you refresh the page, you should remain in an authenticated state. If you press **Logout** then you should return to the login screen.
![Profile page](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/13.png)
Now that we have a working login flow with persistent authentication it is time to pull in our expense data from Supabase.
## Step 7: Requesting user data from Supabase
First, install the Supabase client:
`
1
npm install @supabase/supabase-js
`
In order to pass an authenticated `user_id` to Supabase we will package it within a JWT. Install jsonwebtoken:
`
1
npm install jsonwebtoken
`
Create a new file `utils/supabase.js` and add the following:
`
1
// utils/supabase.js
2
import { createClient } from '@supabase/supabase-js'
3
import jwt from 'jsonwebtoken'
45
const getSupabase = (userId) => {
6
 const supabase = createClient(
7
  process.env.NEXT_PUBLIC_SUPABASE_URL,
8
  process.env.NEXT_PUBLIC_SUPABASE_KEY
9
 )
1011
 if (userId) {
12
  const payload = {
13
   userId,
14
   exp: Math.floor(Date.now() / 1000) + 60 * 60,
15
  }
1617
  supabase.auth.session = () => ({
18
   access_token: jwt.sign(payload, process.env.SUPABASE_SIGNING_SECRET),
19
  })
20
 }
2122
 return supabase
23
}
2425
export { getSupabase }
`
Our payload for the JWT will contain our user's unique identifier from Stytch, their `user_id`. We are signing this JWT using Supabase's signing secret, so Supabase will be able to validate it is authentic and hasn't been tampered with in transit.
Let's load our expenses from Supabase on the home page! Update `pages/index.js` a final time to make a request for expense data from Supabase.
`
1
import styles from '../styles/Home.module.css'
23
import StytchLogin from '../components/StytchLogin'
4
import Profile from '../components/Profile'
5
import { getAuthenticatedUserFromSession } from '../utils/stytchLogic'
6
import { getSupabase } from '../utils/supabase'
78
const Index = ({ user, publicToken }) => {
9
 let content
10
 if (user) {
11
  content = <Profile user={user} />
12
 } else {
13
  content = <StytchLogin publicToken={publicToken} />
14
 }
1516
 return <div className={styles.main}>{content}</div>
17
}
1819
export async function getServerSideProps({ req, res }) {
20
 const userId = await getAuthenticatedUserFromSession(req, res)
2122
 if (userId) {
23
  const supabase = getSupabase(userId)
24
  const { data: expenses } = await supabase.from('expenses').select('*')
2526
  return {
27
   props: {
28
    user: { userId, expenses },
29
    publicToken: process.env.STYTCH_PUBLIC_TOKEN,
30
   },
31
  }
32
 } else {
33
  return {
34
   props: { publicToken: process.env.STYTCH_PUBLIC_TOKEN },
35
  }
36
 }
37
}
3839
export default Index
`
When we reload our application, we are still getting the empty state for expenses.
This is because we enabled Row Level Security, which blocks all requests by default and lets you granularly control access to the data in your database. To enable our user to select their expenses we need to write a RLS policy.
## Step 8: Write a policy to allow select
Our policy will need to know who our currently logged in user is to determine whether or not they should have access. Let's create a PostgreSQL function to extract the current user from our new JWT.
Navigate back to the Supabase dashboard, select SQL from the sidebar menu, and click **New query**. This will create a new query,, which will allow us to run any SQL against our Postgres database.
Write the following and click **Run**.
`
1
create or replace function auth.user_id() returns text as $$
2
 select nullif(current_setting('request.jwt.claims', true)::json->>'userId', '')::text;
3
$$ language sql stable;
`
You should see the output `Success, no rows returned`. This created a function called `auth.user_id()`, which will inspect the `userId` field of our JWT payload.
> Note: To learn more about PostgreSQL functions, check out this [deep dive video](https://www.youtube.com/watch?v=MJZCCpCYEqk).
Let's create a policy that checks whether this user is the owner of an expense.
Select **Authentication** from the Supabase sidebar menu, click **Policies** , then **New Policy**.
![Supabase authentication page](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/14.png)
From the modal, select **For full customization create a policy from scratch** and add the following.
![Supabase create policy page](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/15.png)
This policy is calling the function we just created to get the currently logged in user's `user_id` `auth.user_id()` and checking whether this matches the `user_id` column for the current expense. If it does, then it will allow the user to select it, otherwise it will continue to deny.
Click Review and then Save policy. After you've saved, click Enable RLS on the table to enable the policy we just created.
> Note: To learn more about RLS and policies, check out this [video](https://www.youtube.com/watch?v=Ow_Uzedfohk).
The last thing we need to do is update the `user_id` columns for our existing expenses.
Head back to the Supabase dashboard, and select Table editor from the sidebar. You will notice each entry has `user_id` set to `NULL`. We need to update this value to the proper `user_id`.
![Supabase null users in table](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/16.png)
To get the `user_id` for our Stytch user, you can pull it from the welcome page in our example app (eg `user-test-61497d40-f957-45cd-a6c8-5408d22e93bc`).
![Get user_id](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/17.png)
Update each row in Supabase to this `user_id`.
![Populate user_id](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/18.png)
Return to `localhost:3000`, and you will see your expenses listed.
![Listed expenses](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/19.png)
We now have a basic expense tracker application powered by Stytch, Supabase, and Next.js. From here you could add additional features like adding, editing, and organizing your expenses further.
> Note: You can find a completed version of this project on [Github](https://github.com/stytchauth/stytch-nextjs-supabase).
## Optional: Add Google One Tap
In this optional step, we will extend our application to allow users to login with Google One Tap in addition to Email magic links.
You will need to follow the first four steps of [this guide](https://stytch.com/docs/oauth?utm_source=supabase&utm_medium=guide#guides_google-sdk) to create a Google project, set up Google OAuth consent, and configure credentials and redirect URLs.
First, we will make some adjustments to the `StytchLogin` component. We will update the configuration, so that it uses both Google OAuth, and Email magic links.
`
1
// components/StytchLogin.js
2
import React from 'react'
3
import { Stytch } from '@stytch/stytch-react'
45
const stytchConfig = {
6
 loginOrSignupView: {
7
  products: ['oauth', 'emailMagicLinks'],
8
  oauthOptions: {
9
   providers: [
10
    {
11
     type: 'google',
12
     one_tap: true,
13
     position: 'embedded',
14
    },
15
   ],
16
   loginRedirectURL: 'http://localhost:3000/api/authenticate?type=oauth',
17
   signupRedirectURL: 'http://localhost:3000/api/authenticate?type=oauth',
18
  },
19
  emailMagicLinksOptions: {
20
   loginRedirectURL: 'http://localhost:3000/api/authenticate',
21
   loginExpirationMinutes: 30,
22
   signupRedirectURL: 'http://localhost:3000/api/authenticate',
23
   signupExpirationMinutes: 30,
24
   createUserAsPending: true,
25
  },
26
 },
27
 style: {
28
  fontFamily: '"Helvetica New", Helvetica, sans-serif',
29
  width: '321px',
30
  primaryColor: '#0577CA',
31
 },
32
}
3334
const StytchLogin = ({ publicToken }) => {
35
 return (
36
  <Stytch
37
   publicToken={publicToken}
38
   loginOrSignupView={stytchConfig.loginOrSignupView}
39
   style={stytchConfig.style}
40
  />
41
 )
42
}
4344
export default StytchLogin
`
We also need to make an adjustment to the function `authenticateTokenStartSession` in `stytchLogic.js`. Stytch has separate authentication endpoints for Email magic links and OAuth, so we need to route our token correctly.
`
1
// utils/stytchLogic.js
23
// leave the rest of the file contents as is
4
export const authenticateTokenStartSession = async (req, res) => {
5
 const { token, type } = req.query
6
 let sessionToken
7
 try {
8
  const stytchClient = loadStytch()
9
  if (type == 'oauth') {
10
   const resp = await stytchClient.oauth.authenticate(token, {
11
    session_duration_minutes: 30,
12
    session_management_type: 'stytch',
13
   })
14
   sessionToken = resp.session.stytch_session.session_token
15
  } else {
16
   const resp = await stytchClient.magicLinks.authenticate(token, {
17
    session_duration_minutes: 30,
18
   })
19
   sessionToken = resp.session_token
20
  }
21
 } catch (error) {
22
  console.log(error)
23
  const errorString = JSON.stringify(error)
24
  return res.status(400).json({ errorString })
25
 }
2627
 setCookies(SESSION_COOKIE, sessionToken, {
28
  req,
29
  res,
30
  maxAge: 60 * 60 * 24,
31
  secure: true,
32
 })
3334
 return res.redirect('/')
35
}
`
With these two changes you will now have a working Google One Tap authentication method along with email magic links.
![Google One Tap](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/stytch/documentation/20.png)
## Resources
  * [Stytch blog](https://stytch.com/blog?utm_source=supabase&utm_medium=guide)
  * [Stytch documentation](https://stytch.com/docs?utm_source=supabase&utm_medium=guide)


## Details
DeveloperStytch
Category[Auth](https://supabase.com/partners/integrations#auth)
Website[stytch.com](https://stytch.com/?utm_source=supabase&utm_medium=partner-gallery)
Documentation[Learn](https://stytch.com/?utm_source=supabase&utm_medium=partner-gallery)
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

