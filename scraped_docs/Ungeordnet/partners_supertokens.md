---
url: https://supabase.com/partners/supertokens
scraped_at: 2025-05-25T09:12:00.570619
title: SuperTokens | Works With Supabase
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
![SuperTokens](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fsupertokens%2Fsuper_tokens_logo.png&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# SuperTokens
![SuperTokens](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fsupertokens%2Fsuper_tokens_og.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
SuperTokens is an open source authentication solution which provides many stratergies for authenticating and managing users. You can use the managed service for easy setup or you can self host the solution to have complete control over your data.
With SuperTokens, Supabase can be used to store and authorize access to user data. Supabase makes it simple to setup Row Level Security(RLS) policies which ensure users can only read and write data that belongs to them.
## Documentation
[SuperTokens](https://www.supertokens.com) is an open source authentication solution which provides many stratergies for authenticating and managing users. You can use the managed service for easy setup or you can self host the solution to have complete control over your data.
In this guide we will build a simple web application using SuperTokens, Supabase, and Next.js. You will be able to sign up using SuperTokens and your email and user ID will be stored in Supabase. Once authenticated the frontend will be able to query Supabase and retrieve the user's email. Our example app will be using the [Email-Password and Social Login](https://supertokens.com/docs/thirdpartyemailpassword/introduction) recipe for authentication and session management.
We will use Supabase to store and authorize access to user data. Supabase makes it simple to setup Row Level Security(RLS) policies which ensure users can only read and write data that belongs to them.
### Demo App
You can find a demo app using SuperTokens, Supabase and Nexts.js on [Github](https://github.com/supertokens/supertokens-auth-react/tree/master/examples/with-supabase)
## Step 1: Create a new Supabase project
From your [Supabase dashboard](https://supabase.com/dashboard/), click `New project`.
Enter a `Name` for your Supabase project.
Enter a secure `Database Password`.
Select the same `Region` you host your app's backend in.
Click `Create new project`.
![New Supabase project settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/supertokens/documentation/supabase_dashboard_create.png)
## Step 2: Creating tables in Supabase
From the sidebar menu in the [Supabase dashboard](https://supabase.com/dashboard/), click `Table editor`, then `New table`.
Enter `users` as the `Name` field.
Select `Enable Row Level Security (RLS)`.
Remove the default columns
Create two new columns:
  * `user_id` as `text` as primary key
  * `email` as `text`


Click `Save` to create the new table.
![Users table](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/supertokens/documentation/supabase_table_create.png)
## Step 3: Setup your Next.js App with SuperTokens.
Since the scope of this guide is limited to the integration between SuperTokens and Supabase, you can refer to the SuperTokens website to see [how to setup your Next.js app with SuperTokens](https://supertokens.com/docs/thirdpartyemailpassword/nextjs/about).
Once you finish setting up your app, you will be greeted with the following screen
![SuperTokens Auth Screen](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/supertokens/documentation/supertokens_thirdpartyemailpassword_auth_screen.png)
## Step 4: Creating a Supabase JWT to access Supabase
In our Nextjs app when a user signs up, we want to store the user's email in Supabase. We would then retrieve this email from Supabase and display it on our frontend.
To use the Supabase client to query the database we will need to create a JWT signed with your Supabase app's signing secret. This JWT will also need to contain the user's userId so Supabase knows an authenticated user is making the request.
To create this flow we will need to modify SuperTokens so that, when a user signs up or signs in, a JWT signed with Supabase's signing secret is created and attached to the user's session. Attaching the JWT to the user's session will allow us to retrieve the Supabase JWT on the frontend and backend (post session verification), using which we can query Supabase.
We want to create a Supabase JWT when we are creating a SuperTokens' session. This can be done by overriding the `createNewSession` function in your backend config.
`
1
// config/backendConfig.ts
23
import ThirdPartyEmailPasswordNode from "supertokens-node/recipe/thirdpartyemailpassword";
4
import SessionNode from "supertokens-node/recipe/session";
5
import { TypeInput } from "supertokens-node/lib/build/types";
6
import { appInfo } from "./appInfo";
7
import jwt from "jsonwebtoken";
89
let backendConfig = (): TypeInput => {
10
  return {
11
    framework: "express",
12
    supertokens: {
13
      connectionURI: "https://try.supertokens.com",
14
    },
15
    appInfo,
16
    recipeList: [
17
      ThirdPartyEmailPasswordNode.init({...}),
18
      SessionNode.init({
19
        override: {
20
          functions: (originalImplementation) => {
21
            return {
22
              ...originalImplementation,
23
              // We want to create a JWT which contains the users userId signed with Supabase's secret so
24
              // it can be used by Supabase to validate the user when retrieving user data from their service.
25
              // We store this token in the accessTokenPayload so it can be accessed on the frontend and on the backend.
26
              createNewSession: async function (input) {
27
                const payload = {
28
                  userId: input.userId,
29
                  exp: Math.floor(Date.now() / 1000) + 60 * 60,
30
                };
3132
                const supabase_jwt_token = jwt.sign(payload, process.env.SUPABASE_SIGNING_SECRET);
3334
                input.accessTokenPayload = {
35
                  ...input.accessTokenPayload,
36
                  supabase_token: supabase_jwt_token,
37
                };
3839
                return await originalImplementation.createNewSession(input);
40
              },
41
            };
42
          },
43
        },
44
      }),
45
    ],
46
    isInServerlessEnv: true,
47
  };
48
};
`
As seen above, we will be using the `jsonwebtoken` library to create a JWT signed with Supabase's signing secret whose payload contains the user's userId.
We will be storing this token in the `accessTokenPayload` which will essentially allow us to access the `supabase_token` on the frontend and backend whilst the user is logged in.
## Step 5: Creating a Supabase client
Create a new file called `utils/supabase.ts` and add the following:
`
1
// utils/supabase.ts
23
import { createClient } from '@supabase/supabase-js'
45
const getSupabase = (access_token) => {
6
 const supabase = createClient(
7
  process.env.NEXT_PUBLIC_SUPABASE_URL,
8
  process.env.NEXT_PUBLIC_SUPABASE_KEY
9
 )
1011
 supabase.auth.session = () => ({
12
  access_token,
13
 })
1415
 return supabase
16
}
1718
export { getSupabase }
`
This will be our client for talking to Supabase. We can pass it an `access_token` and it will be attached to our request. This `access_token` is the same as the `supabase_token` we had created earlier.
## Step 6: Inserting users into Supabase when they sign up:
In our example app there are two ways for signing up a user. Email-Password and Social Login based authentication. We will need to override both these APIs such that when a user signs up, their email mapped to their userId is stored in Supabase.
`
1
// config/backendConfig.ts
23
import ThirdPartyEmailPasswordNode from "supertokens-node/recipe/thirdpartyemailpassword";
4
import SessionNode from "supertokens-node/recipe/session";
5
import { TypeInput } from "supertokens-node/lib/build/types";
6
import { appInfo } from "./appInfo";
7
import jwt from "jsonwebtoken";
8
import { getSupabase } from "../utils/supabase";
910
let backendConfig = (): TypeInput => {
11
  return {
12
    framework: "express",
13
    supertokens: {
14
      connectionURI: "https://try.supertokens.com",
15
    },
16
    appInfo,
17
    recipeList: [
18
      ThirdPartyEmailPasswordNode.init({
19
        providers: [...],
20
        override: {
21
          apis: (originalImplementation) => {
22
            return {
23
              ...originalImplementation,
24
              // the thirdPartySignInUpPost function handles sign up/in via Social login
25
              thirdPartySignInUpPOST: async function (input) {
26
                if (originalImplementation.thirdPartySignInUpPOST === undefined) {
27
                  throw Error("Should never come here");
28
                }
2930
                // call the sign up/in api for social login
31
                let response = await originalImplementation.thirdPartySignInUpPOST(input);
3233
                // check that there is no issue with sign up and that a new user is created
34
                if (response.status === "OK" && response.createdNewUser) {
3536
                  // retrieve the accessTokenPayload from the user's session
37
                  const accessTokenPayload = response.session.getAccessTokenPayload();
3839
                  // create a supabase client with the supabase_token from the accessTokenPayload
40
                  const supabase = getSupabase(accessTokenPayload.supabase_token);
4142
                  // store the user's email mapped to their userId in Supabase
43
                  const { error } = await supabase
44
                    .from("users")
45
                    .insert({ email: response.user.email, user_id: response.user.id });
4647
                  if (error !== null) {
4849
                    throw error;
50
                  }
51
                }
5253
                return response;
54
              },
55
              // the emailPasswordSignUpPOST function handles sign up via Email-Password
56
              emailPasswordSignUpPOST: async function (input) {
57
                if (originalImplementation.emailPasswordSignUpPOST === undefined) {
58
                  throw Error("Should never come here");
59
                }
6061
                let response = await originalImplementation.emailPasswordSignUpPOST(input);
6263
                if (response.status === "OK") {
6465
                  // retrieve the accessTokenPayload from the user's session
66
                  const accessTokenPayload = response.session.getAccessTokenPayload();
6768
                  // create a supabase client with the supabase_token from the accessTokenPayload
69
                  const supabase = getSupabase(accessTokenPayload.supabase_token);
7071
                  // store the user's email mapped to their userId in Supabase
72
                  const { error } = await supabase
73
                    .from("users")
74
                    .insert({ email: response.user.email, user_id: response.user.id });
7576
                  if (error !== null) {
7778
                    throw error;
79
                  }
80
                }
8182
                return response;
83
              },
84
            };
85
          },
86
        },
87
      }),
88
      SessionNode.init({...}),
89
    ],
90
    isInServerlessEnv: true,
91
  };
92
};
`
As seen above, we will be overriding the `emailPasswordSignUpPOST` and `thirdPartySignInUpPOST` APIs such that if a user signs up, we retrieve the Supabase JWT (which we created in the `createNewSession` function) from the user's accessTokenPayload and send a request to Supabase to insert the email-userid mapping.
## Step 7: Retrieving the user's email on the frontend
Now that our backend is setup we can modify our frontend to retrieve the user's email from Supabase.
`
1
// pages/index.tsx
23
import React, { useState, useEffect } from 'react'
4
import Head from 'next/head'
5
import styles from '../styles/Home.module.css'
6
import ThirdPartyEmailPassword, {
7
 ThirdPartyEmailPasswordAuth,
8
} from 'supertokens-auth-react/recipe/thirdpartyemailpassword'
9
import dynamic from 'next/dynamic'
10
import { useSessionContext } from 'supertokens-auth-react/recipe/session'
11
import { getSupabase } from '../utils/supabase'
1213
export default function Home() {
14
 return (
15
  // We will wrap the ProtectedPage component with ThirdPartyEmailPasswordAuth so only an
16
  // authenticated user can access it. This will also allow us to access the users session information
17
  // within the component.
18
  <ThirdPartyEmailPasswordAuth>
19
   <ProtectedPage />
20
  </ThirdPartyEmailPasswordAuth>
21
 )
22
}
2324
function ProtectedPage() {
25
 // retrieve the authenticated user's accessTokenPayload and userId from the sessionContext
26
 const { accessTokenPayload, userId } = useSessionContext()
2728
 if (sessionContext.loading === true) {
29
  return null
30
 }
3132
 const [userEmail, setEmail] = useState('')
33
 useEffect(() => {
34
  async function getUserEmail() {
35
   // retrieve the supabase client who's JWT contains users userId, this will be
36
   // used by supabase to check that the user can only access table entries which contain their own userId
37
   const supabase = getSupabase(accessTokenPayload.supabase_token)
3839
   // retrieve the user's name from the users table whose email matches the email in the JWT
40
   const { data } = await supabase.from('users').select('email').eq('user_id', userId)
4142
   if (data.length > 0) {
43
    setEmail(data[0].email)
44
   }
45
  }
46
  getUserEmail()
47
 }, [])
4849
 return (
50
  <div className={styles.container}>
51
   <Head>
52
    <title>SuperTokens 💫</title>
53
    <link rel="icon" href="/favicon.ico" />
54
   </Head>
5556
   <main className={styles.main}>
57
    <p className={styles.description}>
58
     You are authenticated with SuperTokens! (UserId: {userId})
59
     <br />
60
     Your email retrieved from Supabase: {userEmail}
61
    </p>
62
   </main>
63
  </div>
64
 )
65
}
`
As seen above we will be using SuperTokens `useSessionContext` hook to retrieve the authenticated user's `userId` and `accessTokenPayload`. Using React's `useEffect` hook we can use the Supabase client to retrieve the user's email from Supabase using the JWT retrieved from the user's `accessTokenPayload` and their `userId`.
## Step 8: Create Policies to enforce Row Level Security for Select and Insert requests
To enforce Row Level Security for the `Users` table we will need to create policies for Select and Insert requests.
These polices will retrieve the userId from the JWT and check if it matches the userId in the Supabase table
To do this we will need a PostgreSQL function to extract the userId from the JWT.
The payload in the JWT will have the following structure:
`
1
// JWT payload
2
{
3
  userId,
4
  exp
5
}
`
To create the PostgreSQL function, lets navigate back to the Supabase dashboard, select `SQL` from the sidebar menu, and click `New query`. This will create a new query called `new sql snippet`, which will allow us to run any SQL against our Postgres database.
Write the following and click `Run`.
`
1
create or replace function auth.user_id() returns text as $$
2
 select nullif(current_setting('request.jwt.claims', true)::json->>'userId', '')::text;
3
$$ language sql stable;
`
This will create a function called `auth.user_id()`, which will inspect the `userId` field of our JWT payload.
### SELECT query policy
Our first policy will check whether the user is the owner of the email.
Select `Authentication` from the Supabase sidebar menu, click `Policies`, and then `New Policy` on the `Users` table.
![Create new policy](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/supertokens/documentation/create_policy.png)
From the modal, select `Create a policy from scratch` and add the following.
![Policy settings for SELECT](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/supertokens/documentation/policy_config_select.png)
This policy is calling the PostgreSQL function we just created to get the currently logged in user's ID `auth.user_id()` and checking whether this matches the `user_id` column for the current `email`. If it does, then it will allow the user to select it, otherwise it will continue to deny.
Click `Review` and then `Save policy`.
### INSERT query policy
Our second policy will check whether the `user_id` being inserted is the same as the `userId` in the JWT.
Create another policy and add the following:
![Policy settings for INSERT](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/supertokens/documentation/policy_config_insert.png)
Similar to the previous policy we are calling the PostgreSQL function we created to get the currently logged in user's ID `auth.user_id()` and check whether this matches the `user_id` column for the row we are trying to insert. If it does, then it will allow the user to insert the row, otherwise it will continue to deny.
Click `Review` and then `Save policy`.
## Step 9: Test your changes
You can now sign up and you should see the following screen:
![SuperTokens App Authenticated](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/supertokens/documentation/supabase_app_authenticated_screen.png)
If you navigate to your table you should see a new row with the user's `user_id` and `email`.
![Supabase Users table](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/supertokens/documentation/table_with_user.png)
## Resources
  * [SuperTokens](https://supertokens.com/) official website.
  * [SuperTokens community](https://supertokens.com/discord).
  * [SuperTokens documentation](https://supertokens.com/docs/guides).


## Details
DeveloperSuperTokens
Category[Auth](https://supabase.com/partners/integrations#auth)
Website[supertokens.com](https://supertokens.com/)
Documentation[Learn](https://supertokens.com/)
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

