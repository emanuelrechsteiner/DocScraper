---
url: https://python.langchain.com/api_reference/langchain/memory.html
scraped_at: 2025-05-25T18:06:14.989469
title: memory — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/langchain/memory.html#main-content)
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
    * [`agents`](https://python.langchain.com/api_reference/langchain/agents.html)
    * [`callbacks`](https://python.langchain.com/api_reference/langchain/callbacks.html)
    * [`chains`](https://python.langchain.com/api_reference/langchain/chains.html)
    * [`chat_models`](https://python.langchain.com/api_reference/langchain/chat_models.html)
    * [`embeddings`](https://python.langchain.com/api_reference/langchain/embeddings.html)
    * [`evaluation`](https://python.langchain.com/api_reference/langchain/evaluation.html)
    * [`globals`](https://python.langchain.com/api_reference/langchain/globals.html)
    * [`hub`](https://python.langchain.com/api_reference/langchain/hub.html)
    * [`indexes`](https://python.langchain.com/api_reference/langchain/indexes.html)
    * [`memory`](https://python.langchain.com/api_reference/langchain/memory.html)
      * [CombinedMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.combined.CombinedMemory.html)
      * [ReadOnlySharedMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.readonly.ReadOnlySharedMemory.html)
      * [SimpleMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.simple.SimpleMemory.html)
      * [ConversationVectorStoreTokenBufferMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html)
      * [get_prompt_input_key](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.utils.get_prompt_input_key.html)
      * [ConversationBufferMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html)
      * [ConversationStringBufferMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationStringBufferMemory.html)
      * [ConversationBufferWindowMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer_window.ConversationBufferWindowMemory.html)
      * [BaseChatMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html)
      * [BaseEntityStore](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.BaseEntityStore.html)
      * [ConversationEntityMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.ConversationEntityMemory.html)
      * [InMemoryEntityStore](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.InMemoryEntityStore.html)
      * [RedisEntityStore](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.RedisEntityStore.html)
      * [SQLiteEntityStore](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.SQLiteEntityStore.html)
      * [UpstashRedisEntityStore](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.UpstashRedisEntityStore.html)
      * [ConversationSummaryMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary.ConversationSummaryMemory.html)
      * [SummarizerMixin](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary.SummarizerMixin.html)
      * [ConversationSummaryBufferMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary_buffer.ConversationSummaryBufferMemory.html)
      * [ConversationTokenBufferMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.token_buffer.ConversationTokenBufferMemory.html)
      * [VectorStoreRetrieverMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore.VectorStoreRetrieverMemory.html)
    * [`model_laboratory`](https://python.langchain.com/api_reference/langchain/model_laboratory.html)
    * [`output_parsers`](https://python.langchain.com/api_reference/langchain/output_parsers.html)
    * [`retrievers`](https://python.langchain.com/api_reference/langchain/retrievers.html)
    * [`runnables`](https://python.langchain.com/api_reference/langchain/runnables.html)
    * [`smith`](https://python.langchain.com/api_reference/langchain/smith.html)
    * [`storage`](https://python.langchain.com/api_reference/langchain/storage.html)
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
  * [langchain: 0.3.25](https://python.langchain.com/api_reference/langchain/index.html)
  * `memory`


# `memory`[#](https://python.langchain.com/api_reference/langchain/memory.html#module-langchain.memory "Link to this heading")
**Memory** maintains Chain state, incorporating context from past runs.
**Class hierarchy for Memory:**
```
BaseMemory --> BaseChatMemory --> <name>Memory # Examples: ZepMemory, MotorheadMemory

```
Copy to clipboard
**Main helpers:**
```
BaseChatMessageHistory

```
Copy to clipboard
**Chat Message History** stores the chat message history in different stores.
**Class hierarchy for ChatMessageHistory:**
```
BaseChatMessageHistory --> <name>ChatMessageHistory # Example: ZepChatMessageHistory

```
Copy to clipboard
**Main helpers:**
```
AIMessage, BaseMessage, HumanMessage

```
Copy to clipboard
**Classes**
[`memory.combined.CombinedMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.combined.CombinedMemory.html#langchain.memory.combined.CombinedMemory "langchain.memory.combined.CombinedMemory") | Combining multiple memories' data together.  
---|---  
[`memory.readonly.ReadOnlySharedMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.readonly.ReadOnlySharedMemory.html#langchain.memory.readonly.ReadOnlySharedMemory "langchain.memory.readonly.ReadOnlySharedMemory") | Memory wrapper that is read-only and cannot be changed.  
[`memory.simple.SimpleMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.simple.SimpleMemory.html#langchain.memory.simple.SimpleMemory "langchain.memory.simple.SimpleMemory") | Simple memory for storing context or other information that shouldn't ever change between prompts.  
[`memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory "langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory") | Conversation chat memory with token limit and vectordb backing.  
**Functions**
[`memory.utils.get_prompt_input_key`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.utils.get_prompt_input_key.html#langchain.memory.utils.get_prompt_input_key "langchain.memory.utils.get_prompt_input_key")(inputs, ...) | Get the prompt input key.  
---|---  
**Deprecated classes**
[`memory.buffer.ConversationBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory "langchain.memory.buffer.ConversationBufferMemory") |   
---|---  
[`memory.buffer.ConversationStringBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationStringBufferMemory.html#langchain.memory.buffer.ConversationStringBufferMemory "langchain.memory.buffer.ConversationStringBufferMemory") |   
[`memory.buffer_window.ConversationBufferWindowMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer_window.ConversationBufferWindowMemory.html#langchain.memory.buffer_window.ConversationBufferWindowMemory "langchain.memory.buffer_window.ConversationBufferWindowMemory") |   
[`memory.chat_memory.BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory") |   
[`memory.entity.BaseEntityStore`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.BaseEntityStore.html#langchain.memory.entity.BaseEntityStore "langchain.memory.entity.BaseEntityStore") |   
[`memory.entity.ConversationEntityMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.ConversationEntityMemory.html#langchain.memory.entity.ConversationEntityMemory "langchain.memory.entity.ConversationEntityMemory") |   
[`memory.entity.InMemoryEntityStore`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.InMemoryEntityStore.html#langchain.memory.entity.InMemoryEntityStore "langchain.memory.entity.InMemoryEntityStore") |   
[`memory.entity.RedisEntityStore`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.RedisEntityStore.html#langchain.memory.entity.RedisEntityStore "langchain.memory.entity.RedisEntityStore") |   
[`memory.entity.SQLiteEntityStore`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.SQLiteEntityStore.html#langchain.memory.entity.SQLiteEntityStore "langchain.memory.entity.SQLiteEntityStore") |   
[`memory.entity.UpstashRedisEntityStore`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.UpstashRedisEntityStore.html#langchain.memory.entity.UpstashRedisEntityStore "langchain.memory.entity.UpstashRedisEntityStore") |   
[`memory.summary.ConversationSummaryMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary.ConversationSummaryMemory.html#langchain.memory.summary.ConversationSummaryMemory "langchain.memory.summary.ConversationSummaryMemory") |   
[`memory.summary.SummarizerMixin`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary.SummarizerMixin.html#langchain.memory.summary.SummarizerMixin "langchain.memory.summary.SummarizerMixin") |   
[`memory.summary_buffer.ConversationSummaryBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.summary_buffer.ConversationSummaryBufferMemory.html#langchain.memory.summary_buffer.ConversationSummaryBufferMemory "langchain.memory.summary_buffer.ConversationSummaryBufferMemory") |   
[`memory.token_buffer.ConversationTokenBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.token_buffer.ConversationTokenBufferMemory.html#langchain.memory.token_buffer.ConversationTokenBufferMemory "langchain.memory.token_buffer.ConversationTokenBufferMemory") |   
[`memory.vectorstore.VectorStoreRetrieverMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore.VectorStoreRetrieverMemory.html#langchain.memory.vectorstore.VectorStoreRetrieverMemory "langchain.memory.vectorstore.VectorStoreRetrieverMemory") |   
© Copyright 2025, LangChain Inc. 

