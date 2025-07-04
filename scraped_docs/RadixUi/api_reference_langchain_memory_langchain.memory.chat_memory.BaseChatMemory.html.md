---
url: https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html
scraped_at: 2025-05-25T17:56:39.378015
title: BaseChatMemory — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#main-content)
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
  * [`memory`](https://python.langchain.com/api_reference/langchain/memory.html)
  * BaseChatMemory


# BaseChatMemory[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#basechatmemory "Link to this heading") 

_class_ langchain.memory.chat_memory.BaseChatMemory[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "Link to this definition")
    
Bases: `BaseMemory`, `ABC`
Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.
Abstract base class for chat memory. 

**ATTENTION** This abstraction was created prior to when chat models had
    
native tool calling capabilities. It does **NOT** support native tool calling capabilities for chat models and will fail SILENTLY if used with a chat model that has native tool calling.
DO NOT USE THIS ABSTRACTION FOR NEW CODE. 

_param_ chat_memory _:[ BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _[Optional]_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.chat_memory "Link to this definition")


_param_ input_key _: str|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.input_key "Link to this definition")


_param_ output_key _: str|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.output_key "Link to this definition")


_param_ return_messages _: bool_ _= False_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.return_messages "Link to this definition")


_async_ aclear() → None[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory.aclear)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.aclear "Link to this definition")
    
Clear memory contents. 

Return type:
    
None 

_async_ aload_memory_variables( 
    _inputs :dict[str,Any]_, ) → dict[str,Any][#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.aload_memory_variables "Link to this definition")     
Async return key-value pairs given the text input to the chain. 

Parameters:
    
**inputs** (_dict_ _[__str_ _,__Any_ _]_) – The inputs to the chain. 

Returns:
    
A dictionary of key-value pairs. 

Return type:
    
dict[str, _Any_] 

_async_ asave_context( 
    _inputs :dict[str,Any]_,     _outputs :dict[str,str]_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory.asave_context)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.asave_context "Link to this definition")     
Save context from this conversation to buffer. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__Any_ _]_)
  * **outputs** (_dict_ _[__str_ _,__str_ _]_)



Return type:
    
None 

clear() → None[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory.clear)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.clear "Link to this definition")
    
Clear memory contents. 

Return type:
    
None 

_abstractmethod_ load_memory_variables( 
    _inputs :dict[str,Any]_, ) → dict[str,Any][#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.load_memory_variables "Link to this definition")     
Return key-value pairs given the text input to the chain. 

Parameters:
    
**inputs** (_dict_ _[__str_ _,__Any_ _]_) – The inputs to the chain. 

Returns:
    
A dictionary of key-value pairs. 

Return type:
    
dict[str, _Any_] 

save_context( 
    _inputs :dict[str,Any]_,     _outputs :dict[str,str]_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory.save_context)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.save_context "Link to this definition")     
Save context from this conversation to buffer. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__Any_ _]_)
  * **outputs** (_dict_ _[__str_ _,__str_ _]_)



Return type:
    
None 

_abstract property_memory_variables _: list[str]_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.memory_variables "Link to this definition")
    
The string keys this memory class will add to chain inputs.
On this page 
  * [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory)
    * [`chat_memory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.chat_memory)
    * [`input_key`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.input_key)
    * [`output_key`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.output_key)
    * [`return_messages`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.return_messages)
    * [`aclear()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.aclear)
    * [`aload_memory_variables()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.aload_memory_variables)
    * [`asave_context()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.asave_context)
    * [`clear()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.clear)
    * [`load_memory_variables()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.load_memory_variables)
    * [`save_context()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.save_context)
    * [`memory_variables`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory.memory_variables)


© Copyright 2025, LangChain Inc. 

