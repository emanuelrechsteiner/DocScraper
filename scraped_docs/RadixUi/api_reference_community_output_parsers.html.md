---
url: https://python.langchain.com/api_reference/community/output_parsers.html
scraped_at: 2025-05-25T18:11:25.850667
title: output_parsers — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/output_parsers.html#main-content)
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
  * [Langchain](https://python.langchain.com/api_reference/langchain/index.html)
  * [Text Splitters](https://python.langchain.com/api_reference/text_splitters/index.html)
  * [Community](https://python.langchain.com/api_reference/community/index.html)
    * [`adapters`](https://python.langchain.com/api_reference/community/adapters.html)
    * [`agent_toolkits`](https://python.langchain.com/api_reference/community/agent_toolkits.html)
    * [`agents`](https://python.langchain.com/api_reference/community/agents.html)
    * [`cache`](https://python.langchain.com/api_reference/community/cache.html)
    * [`callbacks`](https://python.langchain.com/api_reference/community/callbacks.html)
    * [`chains`](https://python.langchain.com/api_reference/community/chains.html)
    * [`chat_loaders`](https://python.langchain.com/api_reference/community/chat_loaders.html)
    * [`chat_message_histories`](https://python.langchain.com/api_reference/community/chat_message_histories.html)
    * [`chat_models`](https://python.langchain.com/api_reference/community/chat_models.html)
    * [`cross_encoders`](https://python.langchain.com/api_reference/community/cross_encoders.html)
    * [`docstore`](https://python.langchain.com/api_reference/community/docstore.html)
    * [`document_compressors`](https://python.langchain.com/api_reference/community/document_compressors.html)
    * [`document_loaders`](https://python.langchain.com/api_reference/community/document_loaders.html)
    * [`document_transformers`](https://python.langchain.com/api_reference/community/document_transformers.html)
    * [`embeddings`](https://python.langchain.com/api_reference/community/embeddings.html)
    * [`example_selectors`](https://python.langchain.com/api_reference/community/example_selectors.html)
    * [`graph_vectorstores`](https://python.langchain.com/api_reference/community/graph_vectorstores.html)
    * [`graphs`](https://python.langchain.com/api_reference/community/graphs.html)
    * [`indexes`](https://python.langchain.com/api_reference/community/indexes.html)
    * [`llms`](https://python.langchain.com/api_reference/community/llms.html)
    * [`memory`](https://python.langchain.com/api_reference/community/memory.html)
    * [`output_parsers`](https://python.langchain.com/api_reference/community/output_parsers.html)
      * [JsonKeyOutputFunctionsParser](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.JsonKeyOutputFunctionsParser.html)
      * [JsonOutputFunctionsParser](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.JsonOutputFunctionsParser.html)
      * [OutputFunctionsParser](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.OutputFunctionsParser.html)
      * [PydanticAttrOutputFunctionsParser](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser.html)
      * [PydanticOutputFunctionsParser](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.PydanticOutputFunctionsParser.html)
      * [GuardrailsOutputParser](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.rail_parser.GuardrailsOutputParser.html)
    * [`query_constructors`](https://python.langchain.com/api_reference/community/query_constructors.html)
    * [`retrievers`](https://python.langchain.com/api_reference/community/retrievers.html)
    * [`storage`](https://python.langchain.com/api_reference/community/storage.html)
    * [`tools`](https://python.langchain.com/api_reference/community/tools.html)
    * [`utilities`](https://python.langchain.com/api_reference/community/utilities.html)
    * [`utils`](https://python.langchain.com/api_reference/community/utils.html)
    * [`vectorstores`](https://python.langchain.com/api_reference/community/vectorstores.html)
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
  * [langchain-community: 0.3.24](https://python.langchain.com/api_reference/community/index.html)
  * `output_parsers`


# `output_parsers`[#](https://python.langchain.com/api_reference/community/output_parsers.html#module-langchain_community.output_parsers "Link to this heading")
**OutputParser** classes parse the output of an LLM call.
**Class hierarchy:**
```
BaseLLMOutputParser --> BaseOutputParser --> <name>OutputParser # GuardrailsOutputParser

```
Copy to clipboard
**Main helpers:**
```
Serializable, Generation, PromptValue

```
Copy to clipboard
**Classes**
[`output_parsers.ernie_functions.JsonKeyOutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.JsonKeyOutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.JsonKeyOutputFunctionsParser "langchain_community.output_parsers.ernie_functions.JsonKeyOutputFunctionsParser") | Parse an output as the element of the Json object.  
---|---  
[`output_parsers.ernie_functions.JsonOutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.JsonOutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.JsonOutputFunctionsParser "langchain_community.output_parsers.ernie_functions.JsonOutputFunctionsParser") | Parse an output as the Json object.  
[`output_parsers.ernie_functions.OutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.OutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.OutputFunctionsParser "langchain_community.output_parsers.ernie_functions.OutputFunctionsParser") | Parse an output that is one of sets of values.  
[`output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser "langchain_community.output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser") | Parse an output as an attribute of a pydantic object.  
[`output_parsers.ernie_functions.PydanticOutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.PydanticOutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.PydanticOutputFunctionsParser "langchain_community.output_parsers.ernie_functions.PydanticOutputFunctionsParser") | Parse an output as a pydantic object.  
[`output_parsers.rail_parser.GuardrailsOutputParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.rail_parser.GuardrailsOutputParser.html#langchain_community.output_parsers.rail_parser.GuardrailsOutputParser "langchain_community.output_parsers.rail_parser.GuardrailsOutputParser") | Parse the output of an LLM call using Guardrails.  
© Copyright 2025, LangChain Inc. 

