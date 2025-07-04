---
url: https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html
scraped_at: 2025-05-25T17:54:32.595338
title: ConversationBufferMemory — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#main-content)
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
  * ConversationBufferMemory


# ConversationBufferMemory[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#conversationbuffermemory "Link to this heading") 

_class_ langchain.memory.buffer.ConversationBufferMemory[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory "Link to this definition")
    
Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory")
Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.
A basic memory implementation that simply stores the conversation history.
This stores the entire conversation history in memory without any additional processing.
Note that additional processing may be required in some situations when the conversation history is too large to fit in the context window of the model. 

_param_ ai_prefix _: str_ _= 'AI'_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.ai_prefix "Link to this definition")


_param_ chat_memory _:[ BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _[Optional]_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.chat_memory "Link to this definition")


_param_ human_prefix _: str_ _= 'Human'_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.human_prefix "Link to this definition")


_param_ input_key _: str|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.input_key "Link to this definition")


_param_ output_key _: str|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.output_key "Link to this definition")


_param_ return_messages _: bool_ _= False_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.return_messages "Link to this definition")


_async_ abuffer() → Any[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.abuffer)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.abuffer "Link to this definition")
    
String buffer of memory. 

Return type:
    
_Any_ 

_async_ abuffer_as_messages() → list[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")][[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.abuffer_as_messages)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.abuffer_as_messages "Link to this definition")
    
Exposes the buffer as a list of messages in case return_messages is False. 

Return type:
    
list[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")] 

_async_ abuffer_as_str() → str[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.abuffer_as_str)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.abuffer_as_str "Link to this definition")
    
Exposes the buffer as a string in case return_messages is True. 

Return type:
    
str 

_async_ aclear() → None[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.aclear "Link to this definition")
    
Clear memory contents. 

Return type:
    
None 

_async_ aload_memory_variables( 
    _inputs :dict[str,Any]_, ) → dict[str,Any][[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.aload_memory_variables)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.aload_memory_variables "Link to this definition")     
Return key-value pairs given the text input to the chain. 

Parameters:
    
**inputs** (_dict_ _[__str_ _,__Any_ _]_) 

Return type:
    
dict[str, _Any_] 

_async_ asave_context( 
    _inputs :dict[str,Any]_,     _outputs :dict[str,str]_, ) → None[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.asave_context "Link to this definition")     
Save context from this conversation to buffer. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__Any_ _]_)
  * **outputs** (_dict_ _[__str_ _,__str_ _]_)



Return type:
    
None 

clear() → None[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.clear "Link to this definition")
    
Clear memory contents. 

Return type:
    
None 

load_memory_variables( 
    _inputs :dict[str,Any]_, ) → dict[str,Any][[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.load_memory_variables)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.load_memory_variables "Link to this definition")     
Return history buffer. 

Parameters:
    
**inputs** (_dict_ _[__str_ _,__Any_ _]_) 

Return type:
    
dict[str, _Any_] 

save_context( 
    _inputs :dict[str,Any]_,     _outputs :dict[str,str]_, ) → None[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.save_context "Link to this definition")     
Save context from this conversation to buffer. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__Any_ _]_)
  * **outputs** (_dict_ _[__str_ _,__str_ _]_)



Return type:
    
None 

_property_ buffer _: Any_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.buffer "Link to this definition")
    
String buffer of memory. 

_property_ buffer_as_messages _: list[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")]_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.buffer_as_messages "Link to this definition")
    
Exposes the buffer as a list of messages in case return_messages is False. 

_property_ buffer_as_str _: str_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.buffer_as_str "Link to this definition")
    
Exposes the buffer as a string in case return_messages is True.
Examples using ConversationBufferMemory
  * [# Legacy](https://python.langchain.com/docs/versions/migrating_chains/conversation_chain/)
  * [Bittensor](https://python.langchain.com/docs/integrations/llms/bittensor/)
  * [Gradio](https://python.langchain.com/docs/integrations/tools/gradio_tools/)
  * [Llama2Chat](https://python.langchain.com/docs/integrations/chat/llama2_chat/)
  * [Memorize](https://python.langchain.com/docs/integrations/tools/memorize/)
  * [Reddit Search ](https://python.langchain.com/docs/integrations/tools/reddit_search/)
  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)
  * [SceneXplain](https://python.langchain.com/docs/integrations/tools/sceneXplain/)
  * [Xata](https://python.langchain.com/docs/integrations/memory/xata_chat_message_history/)


On this page 
  * [`ConversationBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory)
    * [`ai_prefix`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.ai_prefix)
    * [`chat_memory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.chat_memory)
    * [`human_prefix`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.human_prefix)
    * [`input_key`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.input_key)
    * [`output_key`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.output_key)
    * [`return_messages`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.return_messages)
    * [`abuffer()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.abuffer)
    * [`abuffer_as_messages()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.abuffer_as_messages)
    * [`abuffer_as_str()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.abuffer_as_str)
    * [`aclear()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.aclear)
    * [`aload_memory_variables()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.aload_memory_variables)
    * [`asave_context()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.asave_context)
    * [`clear()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.clear)
    * [`load_memory_variables()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.load_memory_variables)
    * [`save_context()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.save_context)
    * [`buffer`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.buffer)
    * [`buffer_as_messages`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.buffer_as_messages)
    * [`buffer_as_str`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory.buffer_as_str)


© Copyright 2025, LangChain Inc. 

