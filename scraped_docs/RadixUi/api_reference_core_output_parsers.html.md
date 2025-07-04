---
url: https://python.langchain.com/api_reference/core/output_parsers.html
scraped_at: 2025-05-25T18:06:18.314262
title: output_parsers — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/core/output_parsers.html#main-content)
Back to top `⌘`+`K`
[ ![🦜🔗 LangChain documentation - Home](https://python.langchain.com/api_reference/_static/wordmark-api.svg) ![🦜🔗 LangChain documentation - Home](https://python.langchain.com/api_reference/_static/wordmark-api-dark.svg) ](https://python.langchain.com/api_reference/index.html)
  * [ Reference ](https://python.langchain.com/api_reference/reference.html)


`⌘`+`K`
[Docs](https://python.langchain.com/)
Light Dark System Settings
  * [ GitHub](https://github.com/langchain-ai/langchain)
  * [ X / Twitter](https://twitter.com/langchainai)


`⌘`+`K`
  * [ Reference ](https://python.langchain.com/api_reference/reference.html)


[Docs](https://python.langchain.com/)
Light Dark System Settings
  * [ GitHub](https://github.com/langchain-ai/langchain)
  * [ X / Twitter](https://twitter.com/langchainai)


Section Navigation
Base packages
  * [Core](https://python.langchain.com/api_reference/core/index.html)
    * [`agents`](https://python.langchain.com/api_reference/core/agents.html)
    * [`beta`](https://python.langchain.com/api_reference/core/beta.html)
    * [`caches`](https://python.langchain.com/api_reference/core/caches.html)
    * [`callbacks`](https://python.langchain.com/api_reference/core/callbacks.html)
    * [`chat_history`](https://python.langchain.com/api_reference/core/chat_history.html)
    * [`chat_loaders`](https://python.langchain.com/api_reference/core/chat_loaders.html)
    * [`chat_sessions`](https://python.langchain.com/api_reference/core/chat_sessions.html)
    * [`document_loaders`](https://python.langchain.com/api_reference/core/document_loaders.html)
    * [`documents`](https://python.langchain.com/api_reference/core/documents.html)
    * [`embeddings`](https://python.langchain.com/api_reference/core/embeddings.html)
    * [`example_selectors`](https://python.langchain.com/api_reference/core/example_selectors.html)
    * [`exceptions`](https://python.langchain.com/api_reference/core/exceptions.html)
    * [`globals`](https://python.langchain.com/api_reference/core/globals.html)
    * [`indexing`](https://python.langchain.com/api_reference/core/indexing.html)
    * [`language_models`](https://python.langchain.com/api_reference/core/language_models.html)
    * [`load`](https://python.langchain.com/api_reference/core/load.html)
    * [`messages`](https://python.langchain.com/api_reference/core/messages.html)
    * [`output_parsers`](https://python.langchain.com/api_reference/core/output_parsers.html)
      * [BaseGenerationOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html)
      * [BaseLLMOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html)
      * [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html)
      * [JsonOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.JsonOutputParser.html)
      * [SimpleJsonOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.SimpleJsonOutputParser.html)
      * [CommaSeparatedListOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.CommaSeparatedListOutputParser.html)
      * [ListOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.ListOutputParser.html)
      * [MarkdownListOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.MarkdownListOutputParser.html)
      * [NumberedListOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.NumberedListOutputParser.html)
      * [JsonKeyOutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.JsonKeyOutputFunctionsParser.html)
      * [JsonOutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.JsonOutputFunctionsParser.html)
      * [OutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.OutputFunctionsParser.html)
      * [PydanticAttrOutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticAttrOutputFunctionsParser.html)
      * [PydanticOutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html)
      * [JsonOutputKeyToolsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.JsonOutputKeyToolsParser.html)
      * [JsonOutputToolsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.JsonOutputToolsParser.html)
      * [PydanticToolsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.PydanticToolsParser.html)
      * [PydanticOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.pydantic.PydanticOutputParser.html)
      * [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)
      * [BaseCumulativeTransformOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.transform.BaseCumulativeTransformOutputParser.html)
      * [BaseTransformOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.transform.BaseTransformOutputParser.html)
      * [XMLOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.XMLOutputParser.html)
      * [droplastn](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.droplastn.html)
      * [make_invalid_tool_call](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.make_invalid_tool_call.html)
      * [parse_tool_call](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.parse_tool_call.html)
      * [parse_tool_calls](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.parse_tool_calls.html)
      * [nested_element](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.nested_element.html)
    * [`outputs`](https://python.langchain.com/api_reference/core/outputs.html)
    * [`prompt_values`](https://python.langchain.com/api_reference/core/prompt_values.html)
    * [`prompts`](https://python.langchain.com/api_reference/core/prompts.html)
    * [`rate_limiters`](https://python.langchain.com/api_reference/core/rate_limiters.html)
    * [`retrievers`](https://python.langchain.com/api_reference/core/retrievers.html)
    * [`runnables`](https://python.langchain.com/api_reference/core/runnables.html)
    * [`stores`](https://python.langchain.com/api_reference/core/stores.html)
    * [`structured_query`](https://python.langchain.com/api_reference/core/structured_query.html)
    * [`sys_info`](https://python.langchain.com/api_reference/core/sys_info.html)
    * [`tools`](https://python.langchain.com/api_reference/core/tools.html)
    * [`tracers`](https://python.langchain.com/api_reference/core/tracers.html)
    * [`utils`](https://python.langchain.com/api_reference/core/utils.html)
    * [`vectorstores`](https://python.langchain.com/api_reference/core/vectorstores.html)
  * [Langchain](https://python.langchain.com/api_reference/langchain/index.html)
  * [Text Splitters](https://python.langchain.com/api_reference/text_splitters/index.html)
  * [Community](https://python.langchain.com/api_reference/community/index.html)
  * [Experimental](https://python.langchain.com/api_reference/experimental/index.html)


Integrations
  * [AI21](https://python.langchain.com/api_reference/ai21/index.html)
  * [Anthropic](https://python.langchain.com/api_reference/anthropic/index.html)
  * [AstraDB](https://python.langchain.com/api_reference/astradb/index.html)
  * [AWS](https://python.langchain.com/api_reference/aws/index.html)
  * [Azure Ai](https://python.langchain.com/api_reference/azure_ai/index.html)
  * [Azure Dynamic Sessions](https://python.langchain.com/api_reference/azure_dynamic_sessions/index.html)
  * [Cerebras](https://python.langchain.com/api_reference/cerebras/index.html)
  * [Chroma](https://python.langchain.com/api_reference/chroma/index.html)
  * [Cohere](https://python.langchain.com/api_reference/cohere/index.html)
  * [Deepseek](https://python.langchain.com/api_reference/deepseek/index.html)
  * [Elasticsearch](https://python.langchain.com/api_reference/elasticsearch/index.html)
  * [Exa](https://python.langchain.com/api_reference/exa/index.html)
  * [Fireworks](https://python.langchain.com/api_reference/fireworks/index.html)
  * [Google Community](https://python.langchain.com/api_reference/google_community/index.html)
  * [Google GenAI](https://python.langchain.com/api_reference/google_genai/index.html)
  * [Google VertexAI](https://python.langchain.com/api_reference/google_vertexai/index.html)
  * [Groq](https://python.langchain.com/api_reference/groq/index.html)
  * [Huggingface](https://python.langchain.com/api_reference/huggingface/index.html)
  * [IBM](https://python.langchain.com/api_reference/ibm/index.html)
  * [Milvus](https://python.langchain.com/api_reference/milvus/index.html)
  * [MistralAI](https://python.langchain.com/api_reference/mistralai/index.html)
  * [MongoDB](https://python.langchain.com/api_reference/mongodb/index.html)
  * [Neo4J](https://python.langchain.com/api_reference/neo4j/index.html)
  * [Nomic](https://python.langchain.com/api_reference/nomic/index.html)
  * [Nvidia Ai Endpoints](https://python.langchain.com/api_reference/nvidia_ai_endpoints/index.html)
  * [Ollama](https://python.langchain.com/api_reference/ollama/index.html)
  * [OpenAI](https://python.langchain.com/api_reference/openai/index.html)
  * [Perplexity](https://python.langchain.com/api_reference/perplexity/index.html)
  * [Pinecone](https://python.langchain.com/api_reference/pinecone/index.html)
  * [Postgres](https://python.langchain.com/api_reference/postgres/index.html)
  * [Prompty](https://python.langchain.com/api_reference/prompty/index.html)
  * [Qdrant](https://python.langchain.com/api_reference/qdrant/index.html)
  * [Redis](https://python.langchain.com/api_reference/redis/index.html)
  * [Sema4](https://python.langchain.com/api_reference/sema4/index.html)
  * [Snowflake](https://python.langchain.com/api_reference/snowflake/index.html)
  * [Sqlserver](https://python.langchain.com/api_reference/sqlserver/index.html)
  * [Standard Tests](https://python.langchain.com/api_reference/standard_tests/index.html)
  * [Tavily](https://python.langchain.com/api_reference/tavily/index.html)
  * [Together](https://python.langchain.com/api_reference/together/index.html)
  * [Unstructured](https://python.langchain.com/api_reference/unstructured/index.html)
  * [Upstage](https://python.langchain.com/api_reference/upstage/index.html)
  * [Weaviate](https://python.langchain.com/api_reference/weaviate/index.html)
  * [XAI](https://python.langchain.com/api_reference/xai/index.html)


  * [ ](https://python.langchain.com/api_reference/index.html)
  * [LangChain Python API Reference](https://python.langchain.com/api_reference/reference.html)
  * [langchain-core: 0.3.61](https://python.langchain.com/api_reference/core/index.html)
  * `output_parsers`


# `output_parsers`[#](https://python.langchain.com/api_reference/core/output_parsers.html#module-langchain_core.output_parsers "Link to this heading")
**OutputParser** classes parse the output of an LLM call.
**Class hierarchy:**
```
BaseLLMOutputParser --> BaseOutputParser --> <name>OutputParser # ListOutputParser, PydanticOutputParser

```
Copy to clipboard
**Main helpers:**
```
Serializable, Generation, PromptValue

```
Copy to clipboard
**Classes**
[`output_parsers.base.BaseGenerationOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") | Base class to parse the output of an LLM call.  
---|---  
[`output_parsers.base.BaseLLMOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html#langchain_core.output_parsers.base.BaseLLMOutputParser "langchain_core.output_parsers.base.BaseLLMOutputParser")() | Abstract base class for parsing the outputs of a model.  
[`output_parsers.base.BaseOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | Base class to parse the output of an LLM call.  
[`output_parsers.json.JsonOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.JsonOutputParser.html#langchain_core.output_parsers.json.JsonOutputParser "langchain_core.output_parsers.json.JsonOutputParser") | Parse the output of an LLM call to a JSON object.  
[`output_parsers.json.SimpleJsonOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.SimpleJsonOutputParser.html#langchain_core.output_parsers.json.SimpleJsonOutputParser "langchain_core.output_parsers.json.SimpleJsonOutputParser") | alias of [`JsonOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.JsonOutputParser.html#langchain_core.output_parsers.json.JsonOutputParser "langchain_core.output_parsers.json.JsonOutputParser")  
[`output_parsers.list.CommaSeparatedListOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.CommaSeparatedListOutputParser.html#langchain_core.output_parsers.list.CommaSeparatedListOutputParser "langchain_core.output_parsers.list.CommaSeparatedListOutputParser") | Parse the output of an LLM call to a comma-separated list.  
[`output_parsers.list.ListOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.ListOutputParser.html#langchain_core.output_parsers.list.ListOutputParser "langchain_core.output_parsers.list.ListOutputParser") | Parse the output of an LLM call to a list.  
[`output_parsers.list.MarkdownListOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.MarkdownListOutputParser.html#langchain_core.output_parsers.list.MarkdownListOutputParser "langchain_core.output_parsers.list.MarkdownListOutputParser") | Parse a Markdown list.  
[`output_parsers.list.NumberedListOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.NumberedListOutputParser.html#langchain_core.output_parsers.list.NumberedListOutputParser "langchain_core.output_parsers.list.NumberedListOutputParser") | Parse a numbered list.  
[`output_parsers.openai_functions.JsonKeyOutputFunctionsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.JsonKeyOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.JsonKeyOutputFunctionsParser "langchain_core.output_parsers.openai_functions.JsonKeyOutputFunctionsParser") | Parse an output as the element of the Json object.  
[`output_parsers.openai_functions.JsonOutputFunctionsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.JsonOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.JsonOutputFunctionsParser "langchain_core.output_parsers.openai_functions.JsonOutputFunctionsParser") | Parse an output as the Json object.  
[`output_parsers.openai_functions.OutputFunctionsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.OutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.OutputFunctionsParser "langchain_core.output_parsers.openai_functions.OutputFunctionsParser") | Parse an output that is one of sets of values.  
[`output_parsers.openai_functions.PydanticAttrOutputFunctionsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticAttrOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticAttrOutputFunctionsParser "langchain_core.output_parsers.openai_functions.PydanticAttrOutputFunctionsParser") | Parse an output as an attribute of a pydantic object.  
[`output_parsers.openai_functions.PydanticOutputFunctionsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser "langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser") | Parse an output as a pydantic object.  
[`output_parsers.openai_tools.JsonOutputKeyToolsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.JsonOutputKeyToolsParser.html#langchain_core.output_parsers.openai_tools.JsonOutputKeyToolsParser "langchain_core.output_parsers.openai_tools.JsonOutputKeyToolsParser") | Parse tools from OpenAI response.  
[`output_parsers.openai_tools.JsonOutputToolsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.JsonOutputToolsParser.html#langchain_core.output_parsers.openai_tools.JsonOutputToolsParser "langchain_core.output_parsers.openai_tools.JsonOutputToolsParser") | Parse tools from OpenAI response.  
[`output_parsers.openai_tools.PydanticToolsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.PydanticToolsParser.html#langchain_core.output_parsers.openai_tools.PydanticToolsParser "langchain_core.output_parsers.openai_tools.PydanticToolsParser") | Parse tools from OpenAI response.  
[`output_parsers.pydantic.PydanticOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.pydantic.PydanticOutputParser.html#langchain_core.output_parsers.pydantic.PydanticOutputParser "langchain_core.output_parsers.pydantic.PydanticOutputParser") | Parse an output using a pydantic model.  
[`output_parsers.string.StrOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html#langchain_core.output_parsers.string.StrOutputParser "langchain_core.output_parsers.string.StrOutputParser") | OutputParser that parses LLMResult into the top likely string.  
[`output_parsers.transform.BaseCumulativeTransformOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.transform.BaseCumulativeTransformOutputParser.html#langchain_core.output_parsers.transform.BaseCumulativeTransformOutputParser "langchain_core.output_parsers.transform.BaseCumulativeTransformOutputParser") | Base class for an output parser that can handle streaming input.  
[`output_parsers.transform.BaseTransformOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.transform.BaseTransformOutputParser.html#langchain_core.output_parsers.transform.BaseTransformOutputParser "langchain_core.output_parsers.transform.BaseTransformOutputParser") | Base class for an output parser that can handle streaming input.  
[`output_parsers.xml.XMLOutputParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.XMLOutputParser.html#langchain_core.output_parsers.xml.XMLOutputParser "langchain_core.output_parsers.xml.XMLOutputParser") | Parse an output using xml format.  
**Functions**
[`output_parsers.list.droplastn`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.droplastn.html#langchain_core.output_parsers.list.droplastn "langchain_core.output_parsers.list.droplastn")(iter, n) | Drop the last n elements of an iterator.  
---|---  
[`output_parsers.openai_tools.make_invalid_tool_call`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.make_invalid_tool_call.html#langchain_core.output_parsers.openai_tools.make_invalid_tool_call "langchain_core.output_parsers.openai_tools.make_invalid_tool_call")(...) | Create an InvalidToolCall from a raw tool call.  
[`output_parsers.openai_tools.parse_tool_call`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.parse_tool_call.html#langchain_core.output_parsers.openai_tools.parse_tool_call "langchain_core.output_parsers.openai_tools.parse_tool_call")(...) | Parse a single tool call.  
[`output_parsers.openai_tools.parse_tool_calls`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.parse_tool_calls.html#langchain_core.output_parsers.openai_tools.parse_tool_calls "langchain_core.output_parsers.openai_tools.parse_tool_calls")(...) | Parse a list of tool calls.  
[`output_parsers.xml.nested_element`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.nested_element.html#langchain_core.output_parsers.xml.nested_element "langchain_core.output_parsers.xml.nested_element")(path, elem) | Get nested element from path.  
© Copyright 2025, LangChain Inc. 

