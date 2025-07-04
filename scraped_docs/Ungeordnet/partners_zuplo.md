---
url: https://supabase.com/partners/zuplo
scraped_at: 2025-05-25T09:45:23.609161
title: Zuplo | Works With Supabase
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
![Zuplo](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fzuplo%2Fzuplo_logo.png&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Zuplo
![Zuplo](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fzuplo%2Fzuplo_og.avif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
[Zuplo](https://zuplo.com/) is a fully-managed API gateway that offers the easiest way to securely and safely share your API. In this guide we look at how you can combine Zuplo and Supabase to create a public API with rate-limiting, a self-serve developer portal, and API-key authentication and much more.
## Documentation
There is an [accompanying video for this article](https://www.youtube.com/watch?v=GJSkbxMnWxE).
![zuplo layout](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/zuplo/documentation/arch.png)
In this example we're going to work with a simple table that allows people to read and write entries to a Supabase table that contains some reviews of skis. Because this is an API for developers, we have to assume that they may be calling it from another backend service and can't login as a user using the standard Supabase method. In this scenario, API keys are often a better choice - see [Wait, you're not using API keys?](https://zuplo.com/blog/2022/05/03/you-should-be-using-api-keys/).
We'll allow people, with a valid API key, to read data from the ski results table and to create new records. Hopefully it's obvious that there are many ways that you can extend this example to add more behavior like roles based access, with custom policies, custom handlers and more.
## Setting up Supabase
If you haven't already, create a new project in Supabase and create a table called ski-reviews with the following columns:
  * id (int8)
  * created_at (timestamptz)
  * make (text)
  * model (text)
  * year (int8)
  * rating (int2)
  * author (text)


Manually enter a couple of rows of data, so that we have something to read from the DB.
## The `Get all` reviews route in Zuplo
Login to Zuplo at [portal.zuplo.com](https://portal.zuplo.com) and create a new project in Zuplo - I went with `supabase-ski-reviews`.
Select the **File** tab and choose **Routes**. Add your first route with the following settings:
  * method: `GET`
  * path: `/reviews`
  * summary: `Get all reviews`
  * version: `v1`
  * CORS: `Anything goes`


And in the request handler section, paste the `READ ALL ROWS` URL of your Supabase backend (you can get to this in the **API docs** section of Supabase)
  * URL Rewrite: `https://YOUR_SUPABASE_URL.supabase.co/rest/v1/ski-reviews?select=*`
  * Forward Search: `unchecked`


In order to call the Supabase backend I need to add some authentication headers to the outgoing request.
Expand the **Policies** section of your route. Click **Add policy** on the **Request** pipeline.
We don't want to forward any headers that the client sends us to Supabase, so find the **Clear Headers Policy** and add that to your inbound pipeline. Note, that we will allow the `content-type` header to flow through, so this should be your policy config.
`
1
{
2
 "export": "ClearHeadersInboundPolicy",
3
 "module": "$import(@zuplo/runtime)",
4
 "options": {
5
  "exclude": ["content-type"]
6
 }
7
}
`
Next, we need to add the credentials to the outgoing request. We'll need to get the JWT token from supabase - you'll find it in **Settings** > **API** as shown below:
![secret_role jwt](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/zuplo/documentation/secret-role.png)
Once you've got your service_role JWT, click **Add Policy** again on the **Request** pipeline and choose the **Add/Set Headers Policy** and configure it as follows:
`
1
{
2
 "export": "SetHeadersInboundPolicy",
3
 "module": "$import(@zuplo/runtime)",
4
 "options": {
5
  "headers": [
6
   {
7
    "name": "apikey",
8
    "value": "$env(SUPABASE_API_KEY)",
9
    "overwrite": true
10
   },
11
   {
12
    "name": "authorization",
13
    "value": "$env(SUPABASE_AUTHZ_HEADER)",
14
    "overwrite": true
15
   }
16
  ]
17
 }
18
}
`
Save your changes.
Next, create two secret [environment variables](https://zuplo.com/docs/deployments/environment-variables) as follows:
  * SUPABASE_API_KEY: `"YOUR_SUPABASE_SECRET_ROLE_JWT"`
  * SUPABASE_AUTHZ_HEADER: `"Bearer YOUR_SUPABASE_SECRET_ROLE_JWT"`


Obviously, in both instances replace `YOUR_SUPABASE_SECRET_ROLE_JWT` with your service_role JWT from Supabase.
You are now ready to invoke your API gateway and see data flow through from your Supabase backend!
Click on the **open in browser** button shown below and you should see the JSON, flowing from Supabase in your browser 👏.
![open in browser](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/zuplo/documentation/open-in-browser.png)
## Adding authentication
At this point, that route is wide open to the world so we need to secure it. We'll do this using API keys. You can follow this guide [Add API key Authentication](https://zuplo.com/docs/quickstarts/add-api-key-auth). Be sure to drag the API Key authentication policy to the very top of your **Request** pipeline. Come back here when you're done.
Welcome back! You've now learned how to secure your API with API-Keys.
## Adding a Create route
Next we'll add a route that allows somebody to create a review. Add another route with the following settings
  * method: `POST`
  * path: `/reviews`
  * summary: `Create a new review`
  * version: `v1`
  * CORS: `Anything goes`


And the request handler as follows:
  * URL Rewrite: `https://YOUR_SUPABASE_URL.supabase.co/rest/v1/ski-reviews`
  * Forward Search: `unchecked`


Expand the policies section and add the same policies (note you can reuse policies by picking from the existing policies at the top of the library)
![existing policies](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/zuplo/documentation/existing-policies.png)
  * api-key-auth-inbound
  * clear-headers-inbound
  * set-headers-inbound


Now your **create** route is secured and will automatically set the right headers before calling Supabase. That was easy.
You can test this out by using the **API Test Console** to invoke your new endpoint. Go to the **API Test Console** and create a new test called `create-review.json`.
  * Method: `POST`
  * Path: `/v1/reviews`
  * Headers: 
    * `content-type`: `application/json`
    * `authorization`: `Bearer YOUR_ZUPLO_API_KEY`
  * Body:


`
1
{
2
 "make": "Rossignol",
3
 "model": "Soul HD7",
4
 "rating": 5,
5
 "year": 2019
6
}
`
![Test console](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/zuplo/documentation/test-console.png)
If you invoke your API by clicking `Test` you should see that you get a **201 Created** - congratulations!
## Add validation to your post
To make your API more usable and more secure it is good practice to validate incoming requests. In this case we will add a JSON Schema document and use it to validate the incoming body to our POST.
Create a new schema document called `new-review.json`.
![new schema](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/zuplo/documentation/new-schema.png)
This example fits the ski-reviews table we described above
`
1
{
2
 "$id": "http://example.com/example.json",
3
 "type": "object",
4
 "default": {},
5
 "title": "Root Schema",
6
 "required": ["make", "model", "rating", "year"],
7
 "additionalProperties": false,
8
 "properties": {
9
  "make": {
10
   "type": "string",
11
   "default": "",
12
   "title": "The make Schema",
13
   "examples": ["DPS"]
14
  },
15
  "model": {
16
   "type": "string",
17
   "default": "",
18
   "title": "The model Schema",
19
   "examples": ["Pagoda"]
20
  },
21
  "rating": {
22
   "type": "integer",
23
   "default": 0,
24
   "title": "The rating Schema",
25
   "examples": [5]
26
  },
27
  "year": {
28
   "type": "integer",
29
   "default": 0,
30
   "title": "The year Schema",
31
   "examples": [2018]
32
  }
33
 },
34
 "examples": [
35
  {
36
   "make": "DPS",
37
   "model": "Pagoda",
38
   "rating": 5,
39
   "year": 2018,
40
   "author": "Josh"
41
  }
42
 ]
43
}
`
Now add a new policy to **request** pipeline for your `Create new review` route. Choose the **JSON Body Validation** policy and configure it to use your newly created JSON schema document:
`
1
{
2
 "export": "ValidateJsonSchemaInbound",
3
 "module": "$import(@zuplo/runtime)",
4
 "options": {
5
  "validator": "$import(./schemas/new-review.json)"
6
 }
7
}
`
This policy can be dragged to the first position in your pipeline.
Now to test this is working, go back to your API test console and change the body of your `create-review.json` test to be invalid (add a new property for example). You should find that you get a `400 Bad Request` response.
![400 Bad Request](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/zuplo/documentation/400-bad.png)
Finally, lean back and marvel at your beautiful Developer Portal that took almost zero effort to get this far, wow! Hopefully you already found the link for this when adding API key support :)
![Developer Portal](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/zuplo/documentation/dev-portal.png)
Zuplo can also be used to handle Supabase JWT tokens for any API, learn more at [API Authentication with Supabase JWT Tokens](https://zuplo.com/blog/2022/11/15/api-authentication-with-supabase-jwt)
## Details
Watch an introductory video
![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
DeveloperZuplo
Category[API](https://supabase.com/partners/integrations#api)
Website[zuplo.com](https://zuplo.com/)
Documentation[Learn](https://zuplo.com/)
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

