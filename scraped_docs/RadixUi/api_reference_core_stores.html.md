---
url: https://python.langchain.com/api_reference/core/stores.html
scraped_at: 2025-05-25T18:02:49.659595
title: stores — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/core/stores.html#main-content)
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
    * [`outputs`](https://python.langchain.com/api_reference/core/outputs.html)
    * [`prompt_values`](https://python.langchain.com/api_reference/core/prompt_values.html)
    * [`prompts`](https://python.langchain.com/api_reference/core/prompts.html)
    * [`rate_limiters`](https://python.langchain.com/api_reference/core/rate_limiters.html)
    * [`retrievers`](https://python.langchain.com/api_reference/core/retrievers.html)
    * [`runnables`](https://python.langchain.com/api_reference/core/runnables.html)
    * [`stores`](https://python.langchain.com/api_reference/core/stores.html)
      * [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html)
      * [InMemoryBaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryBaseStore.html)
      * [InMemoryByteStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryByteStore.html)
      * [InMemoryStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryStore.html)
      * [InvalidKeyException](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InvalidKeyException.html)
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
  * `stores`


# `stores`[#](https://python.langchain.com/api_reference/core/stores.html#module-langchain_core.stores "Link to this heading")
**Store** implements the key-value stores and storage helpers.
Module provides implementations of various key-value stores that conform to a simple key-value interface.
The primary goal of these storages is to support implementation of caching.
**Classes**
[`stores.BaseStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")() | Abstract interface for a key-value store.  
---|---  
[`stores.InMemoryBaseStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryBaseStore.html#langchain_core.stores.InMemoryBaseStore "langchain_core.stores.InMemoryBaseStore")() | In-memory implementation of the BaseStore using a dictionary.  
[`stores.InMemoryByteStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryByteStore.html#langchain_core.stores.InMemoryByteStore "langchain_core.stores.InMemoryByteStore")() | In-memory store for bytes.  
[`stores.InMemoryStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryStore.html#langchain_core.stores.InMemoryStore "langchain_core.stores.InMemoryStore")() | In-memory store for any type of data.  
[`stores.InvalidKeyException`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InvalidKeyException.html#langchain_core.stores.InvalidKeyException "langchain_core.stores.InvalidKeyException") | Raised when a key is invalid; e.g., uses incorrect characters.  
© Copyright 2025, LangChain Inc. 

