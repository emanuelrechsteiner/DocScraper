---
url: https://supabase.com/blog/mcp-server
scraped_at: 2025-05-25T09:50:23.034981
title: Supabase MCP Server
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
# Supabase MCP Server
04 Apr 2025
•
9 minute read
[![Greg Richardson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgregnr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Greg RichardsonEngineering](https://github.com/gregnr)
![Supabase MCP Server](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-5-mcp-server%2Fthumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We are launching an official [Supabase MCP server](https://github.com/supabase-community/supabase-mcp). You can use this server to connect your favorite AI tools (such as [Cursor](https://www.cursor.com/) or [Claude](https://claude.ai/download)) directly with Supabase.
## What is an MCP Server?[#](https://supabase.com/blog/mcp-server#what-is-an-mcp-server)
MCP stands for [Model Context Protocol](https://modelcontextprotocol.io). It standardizes how Large Language Models (LLMs) talk to platforms like Supabase.
Our MCP server connects your AI tools to Supabase so that they can perform tasks like launching databases, managing tables, fetching config, and querying data on your behalf.
For example, here is Cursor building a Next.js + Supabase app, fetching a Supabase URL and anonymous key, and saving them to a `.env.local` file for Next.js to consume:
## Tools[#](https://supabase.com/blog/mcp-server#tools)
MCP servers use Tools, which are a bit like "abilities". There are over 20 tools available in the Supabase MCP server.
You can:
  * Design tables and track them using migrations
  * Fetch data and run reports using SQL queries
  * Create database branches for development (experimental)
  * Fetch project configuration
  * Spin up new Supabase projects
  * Pause and restore projects
  * Retrieve logs to debug issues
  * Generate TypeScript types based on your database schema


For a full list of abilities, see [Tools](https://github.com/supabase-community/supabase-mcp#tools) in the project README.
## Setup[#](https://supabase.com/blog/mcp-server#setup)
You can [setup](https://github.com/supabase-community/supabase-mcp#2-configure-mcp-client) Supabase MCP on most AI clients using the following JSON:
.cursor/mcp.json
`
1
{
2
 "mcpServers": {
3
  "supabase": {
4
   "command": "npx",
5
   "args": [
6
    "-y",
7
    "@supabase/mcp-server-supabase@latest",
8
    "--access-token",
9
    "<personal-access-token>"
10
   ]
11
  }
12
 }
13
}
`
You'll need to create a [personal access token (PAT)](https://supabase.com/dashboard/account/tokens) for the `<personal-access-token>` field. This token authenticates the MCP server with your Supabase account.
Some clients expect a slightly modified JSON format, and Windows users will have to prefix this command with `cmd /c`. For detailed step-by-step instructions for each client and OS, see our [MCP documentation](https://supabase.com/docs/guides/getting-started/mcp).
## How does MCP work?[#](https://supabase.com/blog/mcp-server#how-does-mcp-work)
If you're new to MCP, it's worth digging into the protocol to understand how it came to be and what features it offers.
Most large language models (LLMs) today support “tool calling” where the model can choose to invoke a developer-provided tool (like `get_weather`) based on the context of the conversation (like “What is the weather in Houston?”). This has opened the door to agent-like experiences where LLMs can call tools that interact with the outside world on your behalf.
As a developer, you tell the LLM which tools are available by providing a JSON schema containing your tools and what parameters they accept:
`
1
{
2
 "name": "get_weather",
3
 "description": "Get the current weather for a specific location",
4
 "parameters": {
5
  "type": "object",
6
  "properties": {
7
   "location": {
8
    "type": "string",
9
    "description": "The city and state/country, e.g. 'San Francisco, CA' or 'Paris, France'"
10
   }
11
  },
12
  "required": ["location"]
13
 }
14
}
`
This JSON schema format is standard across most LLMs. But, importantly, the implementation of each tool is not. It's up to you as the developer to connect the `get_weather` tool call with a weather API somewhere in order to fulfill the request.
Because of this, developers often found themselves duplicating tool implementations across projects and apps. And within any given app, end users could only use tools that were hand picked by its developers. There was no opportunity for a plugin-style tool ecosystem where users could bring their own tools.
### The MCP standard[#](https://supabase.com/blog/mcp-server#the-mcp-standard)
MCP solves this by standardizing the tool ecosystem. That is, it creates a protocol that is understood by both clients (eg. Cursor) and tool providers (eg. Supabase), while decoupling them from each other. Cursor simply needs to implement the client side of the MCP spec and instantly its LLM works with any server that also implements MCP. Cursor (and any other AI app) can let their users bring their own tools as long as those tools implement MCP.
### Resources and prompts[#](https://supabase.com/blog/mcp-server#resources-and-prompts)
MCP also incorporates some other (optional) primitives beyond tool calling: resources and prompts. Resources allow servers to expose any arbitrary data and content that can be read by clients and used as context for LLMs. This could include:
  * File contents
  * Database records
  * API responses
  * Live system data
  * Screenshots and images
  * Log files
  * And more


Prompts allow servers to define reusable prompt templates that clients can surface to users and LLMs. It gives the server the opportunity to define custom instructions and best practices for the LLM when interacting with its services.
Today, most clients only support the tool primitive. We're excited to see how apps decide to adopt resources and prompts so that we can make the Supabase MCP experience even better in those environments.
For more information on the model context protocol, see the [official MCP docs](https://modelcontextprotocol.io/introduction).
## What's next?[#](https://supabase.com/blog/mcp-server#whats-next)
We believe MCP has a lot of potential in the AI builder world and we want to continue to invest in it. Here are some features on our roadmap:
### Create and deploy Edge Functions[#](https://supabase.com/blog/mcp-server#create-and-deploy-edge-functions)
Supabase Edge Functions allow you to run custom, server side code from our edge network closest to your users. We [just announced](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1) the ability to create and deploy Edge Functions directly from the Supabase Dashboard. So, it would only be fitting also create and deploy Edge Functions directly from your favorite AI assistant.
### Native authorization[#](https://supabase.com/blog/mcp-server#native-authorization)
The latest revision of the MCP spec (2025-03-26 as of writing) now includes official [authorization support](https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/authorization/). This means that, unlike today where we require you to manually create a personal access token for the server, future versions will allow you to authenticate with Supabase using a standard OAuth 2 login flow. This flow would look something like:
  1. Connect Supabase MCP with your AI app/IDE
  2. Your AI app opens a browser window where you login to Supabase directly
  3. After successful login, you jump back to your AI app, fully authenticated


This would be no different than any other “login with X” OAuth flow that we see with apps today. We think this will both simplify the MCP setup experience and also provide better, more granular access to your Supabase account.
### Better schema discovery[#](https://supabase.com/blog/mcp-server#better-schema-discovery)
When designing a database using AI, it's helpful to give the LLM access to your existing schema so that it knows exactly what SQL to execute when making modifications (like `alter table`). Currently we provide a single `list_tables` tool that the LLM can use to fetch your tables. While this is useful, there are a lot of other database objects like views, triggers, functions, and policies that should also be readily available.
Today if the LLM needs access to one of these other objects, it can run the generic `execute_sql` tool to fetch them from the `information_schema`. For example, to fetch all triggers in your database, the LLM might run:
`
1
select
2
  event_object_schema as schema,
3
  event_object_table as table,
4
  trigger_name,
5
  event_manipulation as event,
6
  action_statement as definition
7
from
8
	information_schema.triggers
9
order by
10
	event_object_schema, event_object_table;
`
This often works, but it requires the LLM to know the exact structure of the `information_schema` tables, consumes many tokens due to verbose SQL queries, and creates opportunities for errors when parsing the results. We think a more structured and terse query method can improve discoverability and reduce excess token usage. Stay tuned!
### More protections[#](https://supabase.com/blog/mcp-server#more-protections)
Some of us trust AI _a little too much_ with our databases. Supabase supports [database branching](https://supabase.com/docs/guides/deployment/branching) to allow you to spin up separate development databases as you design new features, then merge them back when you're ready. This means that if something went terribly wrong, you can easily reset your branch to a earlier version and continue where you left off.
Our MCP server already supports branching today, but we think we can add even more protections like auto detecting destructive operations and requiring confirmation before executing them.
## Get started with Supabase MCP[#](https://supabase.com/blog/mcp-server#get-started-with-supabase-mcp)
We've built the Supabase MCP server to bridge the gap between AI tools and your databases, letting you focus on building instead of context-switching between tools.
The MCP protocol is evolving with proposals like the new [Streamable HTTP transport](https://github.com/modelcontextprotocol/specification/pull/206) that supports fully stateless servers without requiring long-lived connections. We're following these developments closely and evaluating how they might benefit the Supabase MCP experience.
If you run into issues or have ideas for new tools we should add, [open an issue](https://github.com/supabase-community/supabase-mcp/issues/new) on the GitHub repo. We're particularly interested in hearing about your experiences with schema discovery, database branching, and other safety features as we continue to refine its protections.
Check out our [docs](https://supabase.com/docs/guides/getting-started/mcp) for the latest updates and examples of what you can build with Supabase MCP.
[Launch Week 14](https://supabase.com/launch-week)
Mar 31 - Apr 04 '25
[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage
[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)[Community Meetups](https://supabase.com/events?category=meetup)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmcp-server&text=Supabase%20MCP%20Server)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmcp-server&text=Supabase%20MCP%20Server)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fmcp-server&t=Supabase%20MCP%20Server)
[Last postTop 10 Launches of Launch Week 144 April 2025](https://supabase.com/blog/launch-week-14-top-10)
[Next postData API Routes to Nearest Read Replica4 April 2025](https://supabase.com/blog/data-api-nearest-read-replica)
[launch-week](https://supabase.com/blog/tags/launch-week)
On this page
  * [What is an MCP Server?](https://supabase.com/blog/mcp-server#what-is-an-mcp-server)
  * [Tools](https://supabase.com/blog/mcp-server#tools)
  * [Setup](https://supabase.com/blog/mcp-server#setup)
  * [How does MCP work?](https://supabase.com/blog/mcp-server#how-does-mcp-work)
    * [The MCP standard](https://supabase.com/blog/mcp-server#the-mcp-standard)
    * [Resources and prompts](https://supabase.com/blog/mcp-server#resources-and-prompts)
  * [What's next?](https://supabase.com/blog/mcp-server#whats-next)
    * [Create and deploy Edge Functions](https://supabase.com/blog/mcp-server#create-and-deploy-edge-functions)
    * [Native authorization](https://supabase.com/blog/mcp-server#native-authorization)
    * [Better schema discovery](https://supabase.com/blog/mcp-server#better-schema-discovery)
    * [More protections](https://supabase.com/blog/mcp-server#more-protections)
  * [Get started with Supabase MCP](https://supabase.com/blog/mcp-server#get-started-with-supabase-mcp)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmcp-server&text=Supabase%20MCP%20Server)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fmcp-server&text=Supabase%20MCP%20Server)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fmcp-server&t=Supabase%20MCP%20Server)
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

