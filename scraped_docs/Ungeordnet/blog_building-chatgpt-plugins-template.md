---
url: https://supabase.com/blog/building-chatgpt-plugins-template
scraped_at: 2025-05-25T08:57:52.803726
title: Building ChatGPT Plugins with Supabase Edge Runtime
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
# Building ChatGPT Plugins with Supabase Edge Runtime
15 May 2023
•
10 minute read
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Building ChatGPT Plugins with Supabase Edge Runtime](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-15-chatgpt-plugin-temnplate-deno%2Fchatgpt_plugin_template_deno.jpeg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
ChatGPT Plugins support is [rolling out in beta](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) this week! To help you get up and running quickly, we're releasing a [plugin template](https://github.com/supabase-community/chatgpt-plugin-template-deno) written in TypeScript and running on [Supabase Edge Runtime](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)!
Want to get started right away? [Fork the template on GitHub](https://github.com/supabase-community/chatgpt-plugin-template-deno)!
## Serving the manifest file[#](https://supabase.com/blog/building-chatgpt-plugins-template#serving-the-manifest-file)
The `ai-plugin.json` [manifest file](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest) is required for ChatGPT to identify our plugin, know what kind of authentication mechanism is used, understand where to find the OpenAPI definition, and some other details about our plugin. You can find the full list of supported parameters in the [OpenAI docs](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest).
Supabase Edge Runtime does currently not support hosting/serving of static files, however, we can import JSON files in our function and serve them as a JSON response. As this needs to be at the root of our domain, we add this to our [main function handler](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/functions/main/index.ts#L69-L74):
`
1
// functions/main/index.ts
2
import aiPlugins from './ai-plugins.json' with { type: 'json' }
34
// [...]
56
// Serve /.well-known/ai-plugin.json
7
if (service_name === '.well-known') {
8
 return new Response(JSON.stringify(aiPlugins), {
9
  headers: { ...corsHeaders, 'Content-Type': 'application/json' },
10
 })
11
}
`
Now, when running Edge Runtime locally via Docker, our plugin manifest will be available at <http://localhost:8000/.well-known/ai-plugin.json>
## Generating the OpenAPI definition with swagger-jsdoc[#](https://supabase.com/blog/building-chatgpt-plugins-template#generating-the-openapi-definition-with-swagger-jsdoc)
The [OpenAPI definition](https://platform.openai.com/docs/plugins/getting-started/openapi-definition) is required for ChatGPT to know how to underact with our API. Only endpoints included in there will be exposed to ChatGPT, which allows you to selectively make our endpoints available, or add specific endpoints for ChatGPT.
The OpenAPI definition can be either in YAML or JSON format. We’ll be using JSON and the same approach as above to serve it. Writing an OpenAPI definition is not something we will want to do by hand, luckily there is an open source tool called [swagger-jsdoc](https://github.com/Surnet/swagger-jsdoc) which we can use to annotate our endpoints with JSDoc comments and generate the OpenAPI definition with a [little script](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/scripts/generate-openapi-spec.ts).
`
1
// /scripts/generate-openapi-spec.ts
2
import swaggerJsdoc from 'npm:swagger-jsdoc@6.2.8'
34
const options = {
5
 definition: {
6
  openapi: '3.0.1',
7
  info: {
8
   title: 'TODO Plugin',
9
   description: `A plugin that allows the user to create and manage a TODO list using ChatGPT. If you do not know the user's username, ask them first before making queries to the plugin. Otherwise, use the username "global".`,
10
   version: '1.0.0',
11
  },
12
  servers: [{ url: 'http://localhost:8000' }],
13
 },
14
 apis: ['./functions/chatgpt-plugin/index.ts'], // files containing annotations as above
15
}
1617
const openapiSpecification = swaggerJsdoc(options)
18
const openapiString = JSON.stringify(openapiSpecification, null, 2)
19
const encoder = new TextEncoder()
20
const data = encoder.encode(openapiString)
21
await Deno.writeFile('./functions/chatgpt-plugin/openapi.json', data)
22
console.log(openapiString)
`
Since this script is run outside of the function execution, e.g. as a GitHub Action, we can use [npm specifiers](https://deno.com/manual/node/npm_specifiers) to import `swagger-jsdoc`.
Next, we create our `/functions/chatgpt-plugin/index.ts` [file](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/functions/chatgpt-plugin/index.ts) where we use the [Deno oak router](https://deno.land/x/oak) to build our API and annotate it with JSDOC comments.
`
1
// /functions/chatgpt-plugin/index.ts
2
import { Application, Router } from 'https://deno.land/x/oak@v11.1.0/mod.ts'
3
import openapi from './openapi.json' with { type: 'json' }
45
console.log('Hello from `chatgpt-plugin` Function!')
67
const _TODOS: { [key: string]: Array<string> } = {
8
 user: ['Build your own ChatGPT Plugin!'],
9
}
1011
/**
12
 * @openapi
13
 * components:
14
 *  schemas:
15
 *   getTodosResponse:
16
 *    type: object
17
 *    properties:
18
 *     todos:
19
 *      type: array
20
 *      items:
21
 *       type: string
22
 *      description: The list of todos.
23
 */
2425
const router = new Router()
26
router
27
 .get('/chatgpt-plugin', (ctx) => {
28
  ctx.response.body = 'Building ChatGPT plugins with Deno!'
29
 })
30
 /**
31
  * @openapi
32
  * /chatgpt-plugin/todos/{username}:
33
  *  get:
34
  *   operationId: getTodos
35
  *   summary: Get the list of todos
36
  *   parameters:
37
  *   - in: path
38
  *    name: username
39
  *    schema:
40
  *     type: string
41
  *    required: true
42
  *    description: The name of the user.
43
  *   responses:
44
  *    200:
45
  *     description: OK
46
  *     content:
47
  *      application/json:
48
  *       schema:
49
  *        $ref: '#/components/schemas/getTodosResponse'
50
  */
51
 .get('/chatgpt-plugin/todos/:username', (ctx) => {
52
  const username = ctx.params.username.toLowerCase()
53
  ctx.response.body = _TODOS[username] ?? []
54
 })
55
 .get('/chatgpt-plugin/openapi.json', (ctx) => {
56
  ctx.response.body = JSON.stringify(openapi)
57
  ctx.response.headers.set('Content-Type', 'application/json')
58
 })
5960
const app = new Application()
61
app.use(router.routes())
62
app.use(router.allowedMethods())
6364
await app.listen({ port: 8000 })
`
With our JSDoc annotation in place, we can now run the generation script in the terminal:
`
1
deno run --allow-read --allow-write scripts/generate-openapi-spec.ts
`
## Adding the CORS headers[#](https://supabase.com/blog/building-chatgpt-plugins-template#adding-the-cors-headers)
Lastly, we need to add some CORS headers to make the browser happy. We define them in a `/functions/_shared/cors.ts` [file](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/functions/_shared/cors.ts) so we can easily reuse them across our `main` and `chatgpt-plugins` function.
`
1
// /functions/_shared/cors.ts
2
export const corsHeaders = {
3
 'Access-Control-Allow-Origin': 'https://chat.openai.com',
4
 'Access-Control-Allow-Credentials': 'true',
5
 'Access-Control-Allow-Private-Network': 'true',
6
 'Access-Control-Allow-Headers': '*',
7
}
`
Now we can easily add them to all our `chatgpt-plugin` routes a middleware for our oak application.
`
1
// /functions/chatgpt-plugin/index.ts
2
import { Application, Router } from 'https://deno.land/x/oak@v11.1.0/mod.ts'
3
import { corsHeaders } from '../_shared/cors.ts'
45
// [...]
6
const app = new Application()
7
// ChatGPT specific CORS headers
8
app.use(async (ctx, next) => {
9
 await next()
10
 let key: keyof typeof corsHeaders
11
 for (key in corsHeaders) {
12
  ctx.response.headers.set(key, corsHeaders[key])
13
 }
14
})
15
app.use(router.routes())
16
app.use(router.allowedMethods())
1718
await app.listen({ port: 8000 })
`
## Running locally with Docker[#](https://supabase.com/blog/building-chatgpt-plugins-template#running-locally-with-docker)
Now that we’ve got all the pieces in place, let’s spin up Edge Runtime locally and test things out. For this, we need a [Dockerfile](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/Dockerfile) and for convenience, we can add a [docker-compose file](https://github.com/supabase-community/chatgpt-plugin-template-deno/blob/main/docker-compose.yml) also.
`
1
// Dockerfile
2
FROM ghcr.io/supabase/edge-runtime:v1.2.18
34
COPY ./functions /home/deno/functions
5
CMD [ "start", "--main-service", "/home/deno/functions/main" ]
`
This will pull down Edge Runtime v1.2.18 (you can check the l[atest release here](https://github.com/supabase/edge-runtime/releases)) and start up the main service (our `/functions/main/index.ts` function).
`
1
// docker-compose.yml
2
version: "3.9"
3
services:
4
 web:
5
  build: .
6
  volumes:
7
   - type: bind
8
    source: ./functions
9
    target: /home/deno/functions
10
  ports:
11
   - "8000:9000"
`
Edge Runtime will serve requests on port `9000`, so we’re creating a mapping from `[localhost:8000](http://localhost:8000)` where we want to serve our requests locally (of course you can adapt this to your needs) to port `9000` of our Docker container.
Furthermore, we’re using [bind mounts](https://docs.docker.com/storage/bind-mounts/) to mount our functions directory into the container. This allows us to make modifications to our functions without needing to rebuild the container after, making for a great local developer experience.
That’s it, now we can build and spin up our container from the terminal:
`
1
docker compose up --build
`
Go ahead and try it out by visiting:
  * <http://localhost:8000/chatgpt-plugin>
  * <http://localhost:8000/.well-known/ai-plugin.json>
  * <http://localhost:8000/chatgpt-plugin/openapi.json>
  * <http://localhost:8000/chatgpt-plugin/todos/user>


## Installing and testing the plugin locally[#](https://supabase.com/blog/building-chatgpt-plugins-template#installing-and-testing-the-plugin-locally)
You can conveniently test your plugin while running it on [localhost](http://localhost) using the [ChatGPT UI](https://chat.openai.com/):
  1. Select the plugin model from the top drop down, then select “Plugins”, “Plugin Store”, and finally “Develop your own plugin”.
  2. Enter `localhost:8000` and click "Find manifest file".
  3. Confirm with “Install [localhost](http://localhost) plugin”.


That’s it, now go ahead and ask some questions, e.g. you can start with “Do I have any todos?”
![ChatGPT Plugin demo on localhost](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-05-15-chatgpt-plugin-temnplate-deno%2Fchatgpt_plugin_demo_localhost.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
There you are, now go ahead and build your own plugin as it says on your todo list ;)
## Deploying to Fly.io[#](https://supabase.com/blog/building-chatgpt-plugins-template#deploying-to-flyio)
Once you’re happy with the functionality of your plugin, go ahead and deploy it to [Fly.io](http://Fly.io). After installing the [flyctl cli](https://fly.io/docs/hands-on/install-flyctl/), it only takes a couple of steps:
  * Change `http://localhost:8000` to your Fly domain in the `/main/ai-plugins.json` file
  * Open `fly.toml` and update the app name and optionally the region etc.
  * In your terminal, run `fly apps create` and specify the app name you just set in your `fly.toml` file.
  * Finally, run `fly deploy`.


There you go, now you’re ready to [release your plugin to the world](https://platform.openai.com/docs/plugins/production/faq) \o/
## Conclusion[#](https://supabase.com/blog/building-chatgpt-plugins-template#conclusion)
ChatGPT is a powerful new interface and its usage is growing rapidly. With ChatGPT Plugins you can allow your users to access your service directly from ChatGPT, using cutting edge technologies like TypeScript and Deno.
In a next step you can add authentication to your plugin, let us know on [Twitter](https://twitter.com/Supabase) if you’d be interested in a tutorial for that. We can’t wait to see what you will build!
## More AI resources[#](https://supabase.com/blog/building-chatgpt-plugins-template#more-ai-resources)
  * [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
  * [pgvector v0.5.0: Faster semantic search with HNSW indexes](https://supabase.com/blog/pgvector-v0-5-0-hnsw)
  * [OpenAI ChatGPT Plugin docs](https://platform.openai.com/docs/plugins/introduction)
  * [Docs pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&text=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&text=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&t=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)
[Last postChatGPT plugins now support Postgres & Supabase25 May 2023](https://supabase.com/blog/chatgpt-plugins-support-postgres)
[Next postFlutter Hackathon12 May 2023](https://supabase.com/blog/flutter-hackathon)
[AI](https://supabase.com/blog/tags/AI)[tutorial](https://supabase.com/blog/tags/tutorial)[functions](https://supabase.com/blog/tags/functions)
On this page
  * [Serving the manifest file](https://supabase.com/blog/building-chatgpt-plugins-template#serving-the-manifest-file)
  * [Generating the OpenAPI definition with swagger-jsdoc](https://supabase.com/blog/building-chatgpt-plugins-template#generating-the-openapi-definition-with-swagger-jsdoc)
  * [Adding the CORS headers](https://supabase.com/blog/building-chatgpt-plugins-template#adding-the-cors-headers)
  * [Running locally with Docker](https://supabase.com/blog/building-chatgpt-plugins-template#running-locally-with-docker)
  * [Installing and testing the plugin locally](https://supabase.com/blog/building-chatgpt-plugins-template#installing-and-testing-the-plugin-locally)
  * [Deploying to Fly.io](https://supabase.com/blog/building-chatgpt-plugins-template#deploying-to-flyio)
  * [Conclusion](https://supabase.com/blog/building-chatgpt-plugins-template#conclusion)
  * [More AI resources](https://supabase.com/blog/building-chatgpt-plugins-template#more-ai-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&text=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&text=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbuilding-chatgpt-plugins-template&t=Building%20ChatGPT%20Plugins%20with%20Supabase%20Edge%20Runtime)
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

