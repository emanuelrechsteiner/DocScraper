---
url: https://docs.runbear.io/integrations/apps/openai-assistants/api-calling
scraped_at: 2025-05-25T08:59:33.273415
title: API Function Calling | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
        * [Knowledge Bases](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling)
        * [Web Browsing](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing)
        * [OpenAPI Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi)
        * [API Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling)
        * [Current Date Fetching](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching)
        * [Zapier AI Actions](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions)
      * [LangChain](https://docs.runbear.io/integrations/apps/langchain/)
      * [Python Application](https://docs.runbear.io/integrations/apps/python-sdk/)
      * [Anthropic Claude](https://docs.runbear.io/integrations/apps/anthropic-claude/)
  * [FAQs](https://docs.runbear.io/faq)


  * [](https://docs.runbear.io/)
  * [Integrations](https://docs.runbear.io/integrations)
  * LLM Apps
  * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
  * API Function Calling


On this page
# API Function Calling
Runbear supports API function calling using [OpenAI Assistants Function Calling](https://platform.openai.com/docs/assistants/tools/function-calling). You can define custom actions by making one or more APIs available to Runbear. This feature is similar to [Actions in OpenAI GPTs](https://platform.openai.com/docs/actions).
## Common Use Cases[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#common-use-cases "Direct link to Common Use Cases")
API function calls enable utilizing external services. For example, you can:
  * Create assistants that answer questions by calling external APIs, e.g., `GET https://weatherapi.com/new-york`
  * Convert natural language into API calls, e.g., convert `"Who are my top customers?"` to `GET https://internal.service.com/customers/leaderboard` and call your internal API


⋯ And much more!
## Defining API Functions[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#defining-api-functions "Direct link to Defining API Functions")
Runbear API function is identical to [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling) except for the `__api__` field under `properties`. You define API specification in the field.
### `__api__` Schema[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#__api__-schema "Direct link to __api__-schema")
The `__api__` object is described as a JSON Schema object. See [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format.
field| type| description  
---|---|---  
type| string| It should be `"object"`  
value| object| A definition of the API  
value.url| string| URL of the API endpoint  
value.method| string (optional)| HTTP method to use (GET, POST, PUT, DELETE, etc.)  
value.headers| object (optional)| A JSON object of HTTP headers  
### Passing GET Parameters[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#passing-get-parameters "Direct link to Passing GET Parameters")
Parameters defined in `function.parameters.properties` of the [OpenAI Function Calling JSON Schema](https://platform.openai.com/docs/guides/function-calling) will be passed to the GET API request using query parameters.
You can also utilize the dynamic URL path by leveraging the `function.parameters.properties`. To use a parameter in the URL, assign a key and enclose it with curly braces (`{}`).
Example Function Calling JSON
```
{"name":"sample_function","parameters":{"type":"object","properties":{"example_path_parameter":{"type":"string","description":"Describe the parameter here."},"example_query_parameter":{"type":"string","description":"Describe the parameter here."},"__api__":{"type":"object","value":{"url":"https://your.domain/path/{example_path_parameter}/",}}},"required":["example_path_parameter","example_query_parameter"]},}
```

The example function will send a GET request to the URL below.
```
https://your.domain/path/generated_path_parameter/?example_query_parameter=Some%20Generated%20Query%20Parameter%20String
```

### Passing POST Parameters[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#passing-post-parameters "Direct link to Passing POST Parameters")
Parameters defined in `function.parameters.properties` of the [OpenAI Function Calling JSON Schema](https://platform.openai.com/docs/guides/function-calling) will be passed to the POST API request using body parameters.
Example POST method Function Calling JSON
```
{"name":"sample_post_function","parameters":{"type":"object","properties":{"example_body_parameter":{"type":"string","description":"Describe the parameter here."},"__api__":{"type":"object","value":{"url":"https://your.domain/path/","method":"POST",}}},"required":["example_body_parameter"]},}
```

The example function will send a POST request to `https://your.domain.path` with a JSON body:
```
{"example_body_parameter":"String generated by LLM"}
```

### API Function Example[​](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#api-function-example "Direct link to API Function Example")
The provided JSON example outlines an API function designed for sending requests to [swapi.dev](https://swapi.dev). It extracts `resource` and `search` value from user queries, injects the `resource` to the URL path, and adds `search` as the URL query parameter.
```
{"name":"search_starwars","parameters":{"type":"object","properties":{"search":{"type":"string","description":"Search keyword"},"resource":{"type":"string","description":"Type of searching resource. The value should be one of 'people', 'planets' or 'starships'."},"__api__":{"type":"object","value":{"url":"https://swapi.dev/api/{resource}/","method":"GET","headers":{"Content-Type":"application/json"}}}},"required":["search","resource"]},"description":"Search about the keyword from Starwars"}
```

[PreviousOpenAPI Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi)[NextCurrent Date Fetching](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching)
  * [Common Use Cases](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#common-use-cases)
  * [Defining API Functions](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#defining-api-functions)
    * [`__api__` Schema](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#__api__-schema)
    * [Passing GET Parameters](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#passing-get-parameters)
    * [Passing POST Parameters](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#passing-post-parameters)
    * [API Function Example](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling#api-function-example)


Docs
  * [Docs](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)


Community
  * [Twitter](https://twitter.com/runbear_io)
  * [LinkedIn](https://www.linkedin.com/company/runbear)


More
  * [Runbear](https://runbear.io)
  * [GitHub](https://github.com/runbear-io/plugbear-python-sdk)


Copyright © 2025 Runbear, Inc.

