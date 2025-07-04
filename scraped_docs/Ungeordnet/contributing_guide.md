---
url: https://docs.firecrawl.dev/contributing/guide
scraped_at: 2025-05-25T08:34:13.868144
title: Running locally | Firecrawl
---

[Firecrawl Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo-dark.png)](https://firecrawl.dev)
v1
Search...
⌘KAsk AI
  * [Status](https://firecrawl.betteruptime.com)
  * Support
  * [mendableai/firecrawl38.791](https://github.com/mendableai/firecrawl)
  * [mendableai/firecrawl38.791](https://github.com/mendableai/firecrawl)


Search...
Navigation
Contributing
Running locally
[Documentation](https://docs.firecrawl.dev/introduction)[SDKs](https://docs.firecrawl.dev/sdks/overview)[Learn](https://www.firecrawl.dev/blog/category/tutorials)[Integrations](https://www.firecrawl.dev/app)[API Reference](https://docs.firecrawl.dev/api-reference/introduction)
* [Playground](https://firecrawl.dev/playground)
* [Blog](https://firecrawl.dev/blog)
* [Community](https://discord.gg/gSmWdAkdwd)
* [Changelog](https://firecrawl.dev/changelog)
##### Get Started
  * [Quickstart](https://docs.firecrawl.dev/introduction)
  * [MCP Server](https://docs.firecrawl.dev/mcp)
  * [Launch Week III (New)](https://docs.firecrawl.dev/launch-week)
  * [Rate Limits](https://docs.firecrawl.dev/rate-limits)
  * [Advanced Scraping Guide](https://docs.firecrawl.dev/advanced-scraping-guide)


##### Standard Features
  * Scrape
  * Crawl
  * [Map](https://docs.firecrawl.dev/features/map)
  * [Search](https://docs.firecrawl.dev/features/search)


##### Agentic Features
  * [Extract](https://docs.firecrawl.dev/features/extract)
  * [FIRE-1](https://docs.firecrawl.dev/agents/fire-1)


##### Alpha tools
  * LLMs.txt API
  * Deep Research API


##### Contributing
  * [Open Source vs Cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud)
  * [Running locally](https://docs.firecrawl.dev/contributing/guide)
  * [Self-hosting](https://docs.firecrawl.dev/contributing/self-host)


Contributing
# Running locally
Copy page
Learn how to run Firecrawl locally to run on your own and/or contribute to the project.
Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally so you can run it on your own and contribute.
If you’re contributing, note that the process is similar to other open-source repos, i.e., fork Firecrawl, make changes, run tests, PR.
If you have any questions or would like help getting on board, join our Discord community [here](https://discord.gg/gSmWdAkdwd) for more information or submit an issue on Github [here](https://github.com/mendableai/firecrawl/issues/new/choose)!
## 
[​](https://docs.firecrawl.dev/contributing/guide#running-the-project-locally)
Running the project locally
First, start by installing dependencies:
  1. node.js [instructions](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)
  2. pnpm [instructions](https://pnpm.io/installation)
  3. redis [instructions](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)


Set environment variables in a `.env` file in the `/apps/api/` directory. You can copy over the template in `.env.example`.
To start, we won’t set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features)
Copy
```
# ./apps/api/.env
# ===== Required ENVS ======
NUM_WORKERS_PER_QUEUE=8 
PORT=3002
HOST=0.0.0.0
#for self-hosting using docker, use redis://redis:6379. For running locally, use redis://localhost:6379
REDIS_URL=redis://localhost:6379
#for self-hosting using docker, use redis://redis:6379. For running locally, use redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379 
PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/html
## To turn on DB authentication, you need to set up supabase.
USE_DB_AUTHENTICATION=false
# ===== Optional ENVS ======
# Supabase Setup (used to support DB authentication, advanced logging, etc.)
SUPABASE_ANON_TOKEN= 
SUPABASE_URL= 
SUPABASE_SERVICE_TOKEN=
# Other Optionals
# use if you've set up authentication and want to test with a real API key
TEST_API_KEY=
# set if you'd like to test the scraping rate limit
RATE_LIMIT_TEST_API_KEY_SCRAPE=
# set if you'd like to test the crawling rate limit
RATE_LIMIT_TEST_API_KEY_CRAWL=
# add for LLM dependednt features (image alt generation, etc.)
OPENAI_API_KEY=
BULL_AUTH_KEY=@
# use if you're configuring basic logging with logtail
LOGTAIL_KEY=
# set if you have a llamaparse key you'd like to use to parse pdfs
LLAMAPARSE_API_KEY=
# set if you'd like to send slack server health status messages
SLACK_WEBHOOK_URL=
# set if you'd like to send posthog events like job logs
POSTHOG_API_KEY=
# set if you'd like to send posthog events like job logs
POSTHOG_HOST=
# set if you'd like to use the fire engine closed beta
FIRE_ENGINE_BETA_URL=
# Proxy Settings for Playwright (Alternative you can can use a proxy service like oxylabs, which rotates IPs for you on every request)
PROXY_SERVER=
PROXY_USERNAME=
PROXY_PASSWORD=
# set if you'd like to block media requests to save proxy bandwidth
BLOCK_MEDIA=
# Set this to the URL of your webhook when using the self-hosted version of FireCrawl
SELF_HOSTED_WEBHOOK_URL=
# Resend API Key for transactional emails
RESEND_API_KEY=
# LOGGING_LEVEL determines the verbosity of logs that the system will output.
# Available levels are:
# NONE - No logs will be output.
# ERROR - For logging error messages that indicate a failure in a specific operation.
# WARN - For logging potentially harmful situations that are not necessarily errors.
# INFO - For logging informational messages that highlight the progress of the application.
# DEBUG - For logging detailed information on the flow through the system, primarily used for debugging.
# TRACE - For logging more detailed information than the DEBUG level.
# Set LOGGING_LEVEL to one of the above options to control logging output.
LOGGING_LEVEL=INFO

```

### 
[​](https://docs.firecrawl.dev/contributing/guide#installing-dependencies)
Installing dependencies
First, install the dependencies using pnpm.
Copy
```
# cd apps/api # to make sure you're in the right folder
pnpm install # make sure you have pnpm version 9+!

```

### 
[​](https://docs.firecrawl.dev/contributing/guide#running-the-project)
Running the project
You’re going to need to open 3 terminals for running the services. Here is [a video guide accurate as of Oct 2024](https://youtu.be/LHqg5QNI4UY) (optional: 4 terminals for running the services and testing).
### 
[​](https://docs.firecrawl.dev/contributing/guide#terminal-1-setting-up-redis)
Terminal 1 - setting up redis
Run the command anywhere within your project
Copy
```
redis-server

```

### 
[​](https://docs.firecrawl.dev/contributing/guide#terminal-2-setting-up-workers)
Terminal 2 - setting up workers
Now, navigate to the apps/api/ directory and run:
Copy
```
pnpm run workers
# if you are going to use the [llm-extract feature](https://github.com/mendableai/firecrawl/pull/586/), you should also export OPENAI_API_KEY=sk-______

```

This will start the workers who are responsible for processing crawl jobs.
### 
[​](https://docs.firecrawl.dev/contributing/guide#terminal-3-setting-up-the-main-server)
Terminal 3 - setting up the main server
To do this, navigate to the apps/api/ directory. If you haven’t installed pnpm already, you can do so here: <https://pnpm.io/installation>
Next, run your server with:
Copy
```
pnpm run start

```

### 
[​](https://docs.firecrawl.dev/contributing/guide#optional-terminal-4-sending-our-first-request)
 _(Optional)_ Terminal 4 - sending our first request
Alright, now let’s send our first request.
Copy
```
curl -X GET http://localhost:3002/test

```

This should return the response Hello, world!
If you’d like to test the crawl endpoint, you can run this
Copy
```
curl -X POST http://localhost:3002/v0/crawl \
  -H 'Content-Type: application/json' \
  -d '{
   "url": "https://docs.firecrawl.dev"
  }'

```

## 
[​](https://docs.firecrawl.dev/contributing/guide#tests%3A)
Tests:
The best way to do this is run the test with `npm run test:local-no-auth` if you’d like to run the tests without authentication.
If you’d like to run the tests with authentication, run `npm run test:prod`
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/contributing/guide.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /contributing/guide)
[Open Source vs Cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud)[Self-hosting](https://docs.firecrawl.dev/contributing/self-host)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Running the project locally](https://docs.firecrawl.dev/contributing/guide#running-the-project-locally)
  * [Installing dependencies](https://docs.firecrawl.dev/contributing/guide#installing-dependencies)
  * [Running the project](https://docs.firecrawl.dev/contributing/guide#running-the-project)
  * [Terminal 1 - setting up redis](https://docs.firecrawl.dev/contributing/guide#terminal-1-setting-up-redis)
  * [Terminal 2 - setting up workers](https://docs.firecrawl.dev/contributing/guide#terminal-2-setting-up-workers)
  * [Terminal 3 - setting up the main server](https://docs.firecrawl.dev/contributing/guide#terminal-3-setting-up-the-main-server)
  * [(Optional) Terminal 4 - sending our first request](https://docs.firecrawl.dev/contributing/guide#optional-terminal-4-sending-our-first-request)
  * [Tests:](https://docs.firecrawl.dev/contributing/guide#tests%3A)


Assistant
Responses are generated using AI and may contain mistakes.

