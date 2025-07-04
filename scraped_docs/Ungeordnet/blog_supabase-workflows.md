---
url: https://supabase.com/blog/supabase-workflows
scraped_at: 2025-05-25T09:05:28.628740
title: Workflows are coming to Supabase
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
# Workflows are coming to Supabase
02 Apr 2021
•
9 minute read
[![Francesco Ceccon avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ffracek.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Francesco CecconEngineering](https://github.com/fracek)
![Workflows are coming to Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fworkflows%2Fworkflows-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
This week we [launched Supabase Storage](https://supabase.com/blog/supabase-storage), which leaves one other huge piece of the stack that everyone is asking for: Functions.
## TLDR[#](https://supabase.com/blog/supabase-workflows#tldr)
We're not releasing Functions today. Trust us, we know you want them. They are coming, just not today.
But we are building something that we think you're going to like: Workflows. We haven't finished building it yet, but Workflows are a "piece" of the Function story and arguably an even more exciting feature.
![Everyone wants functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fworkflows%2Ffunctions.jpg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Firebase Functions[#](https://supabase.com/blog/supabase-workflows#firebase-functions)
Firebase functions are relatively simple. If you use Serverless, AWS Lambda, Cloudflare Workers, Next.js API routes, or Netlify Functions, then you know how they work. A Firebase function executes some code which you provide, without you managing a server.
Specifically for Firebase, they have another key feature - they can be triggered by database events. For example, you can trigger a function whenever a Firestore Document is updated.
This is great, but it is still limited for a few real-world use cases. For example, what if you want to send an email to a user one day after a user signs up. Or one year? There is no queuing functionality in Firebase. You'd have to manage a process like this yourself, probably using a cron-job.
## A better solution?[#](https://supabase.com/blog/supabase-workflows#a-better-solution)
We searched for some open source tools which we think are solving this problem well. We looked at [NodeRed](https://supabase.com/blog/supabase-storage#designing-the-storage-middleware), [n8n](https://n8n.io/), [Airflow](http://airflow.apache.org/blog/airflow-two-point-oh-is-here/), and about 10 other tools. They are amazing tools on their own, but for the Supabase Stack they ultimately had the [same shortcomings](https://supabase.com/blog/supabase-storage#integration-with-the-supabase-ecosystem) that we found with Storage providers - most of them lacked deep Postgres integration.
We went back to the drawing board and asked, "if we could wave a wand and get the perfect solution, what would it look like?". The tool that came very close is [AWS Step Functions](https://aws.amazon.com/step-functions/). The only problem: it's not open source. Luckily, their [state language](https://states-language.net/spec.html) is.
Using this states language, we are [building an open source orchestration engine](https://github.com/supabase/workflows) for managing very complex Workflows with queueing, etc. It will be built with Elixir.
This engine won't execute code. Instead, it will coordinate and execute existing functions wherever they live: AWS, GCP, Azure, OpenFaas, and of course Postgres.
We plan to add "modules" which work natively: email services, notification services, and other platforms.
The engine is deeply integrated with Postgres. `Jobs`, `queues`, and `logs` will be stored and accessible by SQL. We'd like to give a shoutout to the [Oban](https://getoban.pro) team here, their robust job processing was a big missing piece for the engine. And most importantly, it's backed by Postgres!
Once ready, we will make this available in the Supabase Dashboard with a Zapier-like interface.
## What are Workflows[#](https://supabase.com/blog/supabase-workflows#what-are-workflows)
Workflows orchestrate and execute functions in response to a database event (insert, update, delete) or a HTTP call (direct invocation).
You can use them to rapidly develop microservices (once we have functions) without worrying about servers.
Workflows are stateless - the output of a state becomes the input of the next state.
Workflows are defined using Amazon States Languages, so you can import your workflows from AWS (although we are still building handlers for most AWS resources).
Workflows can be _persistent_ (the default). This means they are tolerant to server restarts, but it also means they need to use the database to store their state.
Workers can be _transient._ These are fully in-memory if you don't want to store the execution state (for example, IoT applications that trigger workflows very often). Transient workflows are not restarted if the server crashes or is restarted.
## Example[#](https://supabase.com/blog/supabase-workflows#example)
A typical use-case for workflows is sending emails. For example, you might want to send a user an email one day after they sign up. In database terms we can say: "trigger an email workflow whenever there is an insert on the `users` table."
Let's break this down into steps, then tie it all together at the end:
### Sending an email[#](https://supabase.com/blog/supabase-workflows#sending-an-email)
`
1
SendEmail:
2
 Type: Task
3
 Next: Complete
4
 Resource: my-email-service
5
 Parameters:
6
  api_key: my-api-key
7
  template_id: welcome-email
8
  payload:
9
   name.$: '$.record.name'
10
   email.$: '$.record.email'
`
Here we have a "Task" which triggers a call to an email service (like Mailgun or Postmark). Specifically, it's telling the service to send the `welcome-email` template, and it's providing it a `name` and an `email` as parameters.
### Waiting a day[#](https://supabase.com/blog/supabase-workflows#waiting-a-day)
Since we don't want to send the email immediately, we need to tell Workflows to wait one day
`
1
WaitOneDay:
2
 Type: Wait
3
 Next: SendEmail
4
 Seconds: 86400
`
Here "one day" is specified in seconds.
### Trigger on insert[#](https://supabase.com/blog/supabase-workflows#trigger-on-insert)
We mentioned that you could trigger a workflow whenever there is an "insert" on the `users` table. But what if you insert multiple users at once? Not a problem - we can loop through all the inserts with a `Map`:
`
1
EmailUsers:
2
 Type: Map
3
 End: true
4
 InputPath: '$.changes'
5
 Iterator:
6
  StartAt: CheckInsert
7
  States:
8
   CheckInsert:
9
    Type: Choice
10
    Default: Complete
11
    Choices:
12
     - Variable: '$.type'
13
      StringEquals: INSERT
14
      Next: WaitOneDay
`
In this part, we have a task "EmailUsers", which iterates through all the database events (`$.changes`) and checks if they are INSERTs.
### Tying it all together[#](https://supabase.com/blog/supabase-workflows#tying-it-all-together)
Let's see how it looks all together:
`
1
---
2
Comment: Email users after one day
3
StartAt: EmailUsers
4
States:
5
 EmailUsers:
6
  Type: Map
7
  End: true
8
  InputPath: '$.changes'
9
  Iterator:
10
   StartAt: CheckInsert
11
   States:
12
    CheckInsert:
13
     Type: Choice
14
     Default: Complete
15
     Choices:
16
      - Variable: '$.type'
17
       StringEquals: INSERT
18
       Next: WaitOneDay
19
    WaitOneDay:
20
     Type: Wait
21
     Next: SendEmail
22
     Seconds: 86400
23
    SendEmail:
24
     Type: Task
25
     Next: Complete
26
     Resource: send-templated-email
27
     Parameters:
28
      api_key: my-api-key
29
      template_id: welcome-email
30
      payload:
31
       name.$: '$.record.name'
32
       email.$: '$.record.email'
33
    Complete:
34
     Type: Succeed
`
The workflow receives the following JSON data from Supabase [Realtime](https://github.com/supabase/realtime):
`
1
{
2
 "changes": [
3
  {
4
   "columns": [
5
    {
6
     "flags": ["key"],
7
     "name": "id",
8
     "type": "int8",
9
     "type_modifier": 4294967295
10
    },
11
    {
12
     "flags": [],
13
     "name": "name",
14
     "type": "text",
15
     "type_modifier": 4294967295
16
    },
17
    {
18
     "flags": [],
19
     "name": "email",
20
     "type": "text",
21
     "type_modifier": 4294967295
22
    }
23
   ],
24
   "commit_timestamp": "2021-03-17T14:00:26Z",
25
   "record": {
26
    "id": "101492",
27
    "name": "Alfred",
28
    "email": "alfred@example.org"
29
   },
30
   "schema": "public",
31
   "table": "users",
32
   "type": "INSERT"
33
  }
34
 ],
35
 "commit_timestamp": "2021-03-17T14:00:26Z"
36
}
`
## Next Steps[#](https://supabase.com/blog/supabase-workflows#next-steps)
We've already open sourced the Workflow interpreter [here](https://github.com/supabase/workflows). It's built with Elixir, so you can find it on Hex [here](https://hexdocs.pm/workflows/Workflows.html).
After we've ironed out a few bugs we will integrate it into the Supabase Stack. As with all Supabase features, we'll add a [nice UI](https://ui.supabase.com/) to make prototyping extremely rapid. We'll integrate the UI with the code (via Git) to make sure everything is version controlled.
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-workflows&text=Workflows%20are%20coming%20to%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-workflows&text=Workflows%20are%20coming%20to%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-workflows&t=Workflows%20are%20coming%20to%20Supabase)
[Last postPgBouncer is now available in Supabase2 April 2021](https://supabase.com/blog/supabase-pgbouncer)
[Next postSupabase Launches NFT Marketplace1 April 2021](https://supabase.com/blog/supabase-nft-marketplace)
[functions](https://supabase.com/blog/tags/functions)[workflows](https://supabase.com/blog/tags/workflows)
On this page
  * [TLDR](https://supabase.com/blog/supabase-workflows#tldr)
  * [Firebase Functions](https://supabase.com/blog/supabase-workflows#firebase-functions)
  * [A better solution?](https://supabase.com/blog/supabase-workflows#a-better-solution)
  * [What are Workflows](https://supabase.com/blog/supabase-workflows#what-are-workflows)
  * [Example](https://supabase.com/blog/supabase-workflows#example)
  * [Next Steps](https://supabase.com/blog/supabase-workflows#next-steps)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-workflows&text=Workflows%20are%20coming%20to%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-workflows&text=Workflows%20are%20coming%20to%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-workflows&t=Workflows%20are%20coming%20to%20Supabase)
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

