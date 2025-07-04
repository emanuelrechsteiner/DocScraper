---
url: https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html
scraped_at: 2025-05-25T17:54:35.985828
title: ConversationVectorStoreTokenBufferMemory — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#main-content)
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
  * ConversationVectorStoreTokenBufferMemory


# ConversationVectorStoreTokenBufferMemory[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#conversationvectorstoretokenbuffermemory "Link to this heading") 

_class_ langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore_token_buffer_memory.html#ConversationVectorStoreTokenBufferMemory)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory "Link to this definition")
    
Bases: [`ConversationTokenBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.token_buffer.ConversationTokenBufferMemory.html#langchain.memory.token_buffer.ConversationTokenBufferMemory "langchain.memory.token_buffer.ConversationTokenBufferMemory")
Conversation chat memory with token limit and vectordb backing.
load_memory_variables() will return a dict with the key “history”. It contains background information retrieved from the vector store plus recent lines of the current conversation.
To help the LLM understand the part of the conversation stored in the vectorstore, each interaction is timestamped and the current date and time is also provided in the history. A side effect of this is that the LLM will have access to the current date and time.
Initialization arguments:
This class accepts all the initialization arguments of ConversationTokenBufferMemory, such as llm. In addition, it accepts the following additional arguments
> 

retriever: (required) A VectorStoreRetriever object to use
    
> as the vector backing store 

split_chunk_size: (optional, 1000) Token chunk split size
    
> for long messages generated by the AI 

previous_history_template: (optional) Template used to format
    
> the contents of the prompt history
Example using ChromaDB:
```
fromlangchain.memory.token_buffer_vectorstore_memoryimport (
    ConversationVectorStoreTokenBufferMemory
)
fromlangchain_chromaimport Chroma
fromlangchain_community.embeddingsimport HuggingFaceInstructEmbeddings
fromlangchain_openaiimport OpenAI
embedder = HuggingFaceInstructEmbeddings(
        query_instruction="Represent the query for retrieval: "
)
chroma = Chroma(collection_name="demo",
        embedding_function=embedder,
        collection_metadata={"hnsw:space": "cosine"},
        )
retriever = chroma.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
      'k': 5,
      'score_threshold': 0.75,
    },
)
conversation_memory = ConversationVectorStoreTokenBufferMemory(
    return_messages=True,
    llm=OpenAI(),
    retriever=retriever,
    max_token_limit = 1000,
)
conversation_memory.save_context({"Human": "Hi there"},
                 {"AI": "Nice to meet you!"}
)
conversation_memory.save_context({"Human": "Nice day isn't it?"},
                 {"AI": "I love Wednesdays."}
)
conversation_memory.load_memory_variables({"input": "What time is it?"})

```
Copy to clipboard 

_param_ ai_prefix _: str_ _= 'AI'_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.ai_prefix "Link to this definition")


_param_ chat_memory _:[ BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _[Optional]_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.chat_memory "Link to this definition")


_param_ human_prefix _: str_ _= 'Human'_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.human_prefix "Link to this definition")


_param_ input_key _: str|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.input_key "Link to this definition")


_param_ llm _:[ BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _[Required]_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.llm "Link to this definition")


_param_ max_token_limit _: int_ _= 2000_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.max_token_limit "Link to this definition")


_param_ memory_key _: str_ _= 'history'_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.memory_key "Link to this definition")


_param_ output_key _: str|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.output_key "Link to this definition")


_param_ previous_history_template _: str_ _= '\nCurrent date and time: {current_time}.\n\nPotentially relevant timestamped excerpts of previous conversations (you \ndo not need to use these if irrelevant):\n{previous_history}\n\n'_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.previous_history_template "Link to this definition")


_param_ retriever _:[ VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_ _[Required]_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.retriever "Link to this definition")


_param_ return_messages _: bool_ _= False_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.return_messages "Link to this definition")


_param_ split_chunk_size _: int_ _= 1000_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.split_chunk_size "Link to this definition")


_async_ aclear() → None[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.aclear "Link to this definition")
    
Clear memory contents. 

Return type:
    
None 

_async_ aload_memory_variables( 
    _inputs :dict[str,Any]_, ) → dict[str,Any][#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.aload_memory_variables "Link to this definition")     
Async return key-value pairs given the text input to the chain. 

Parameters:
    
**inputs** (_dict_ _[__str_ _,__Any_ _]_) – The inputs to the chain. 

Returns:
    
A dictionary of key-value pairs. 

Return type:
    
dict[str, _Any_] 

_async_ asave_context( 
    _inputs :dict[str,Any]_,     _outputs :dict[str,str]_, ) → None[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.asave_context "Link to this definition")     
Save context from this conversation to buffer. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__Any_ _]_)
  * **outputs** (_dict_ _[__str_ _,__str_ _]_)



Return type:
    
None 

clear() → None[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.clear "Link to this definition")
    
Clear memory contents. 

Return type:
    
None 

load_memory_variables( 
    _inputs :dict[str,Any]_, ) → dict[str,Any][[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore_token_buffer_memory.html#ConversationVectorStoreTokenBufferMemory.load_memory_variables)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.load_memory_variables "Link to this definition")     
Return history and memory buffer. 

Parameters:
    
**inputs** (_dict_ _[__str_ _,__Any_ _]_) 

Return type:
    
dict[str, _Any_] 

save_context( 
    _inputs :dict[str,Any]_,     _outputs :dict[str,str]_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore_token_buffer_memory.html#ConversationVectorStoreTokenBufferMemory.save_context)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.save_context "Link to this definition")     
Save context from this conversation to buffer. Pruned. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__Any_ _]_)
  * **outputs** (_dict_ _[__str_ _,__str_ _]_)



Return type:
    
None 

save_remainder() → None[[source]](https://python.langchain.com/api_reference/_modules/langchain/memory/vectorstore_token_buffer_memory.html#ConversationVectorStoreTokenBufferMemory.save_remainder)[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.save_remainder "Link to this definition")
    
Save the remainder of the conversation buffer to the vector store.
This is useful if you have made the vectorstore persistent, in which case this can be called before the end of the session to store the remainder of the conversation. 

Return type:
    
None 

_property_ buffer _: Any_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.buffer "Link to this definition")
    
String buffer of memory. 

_property_ buffer_as_messages _: list[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")]_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.buffer_as_messages "Link to this definition")
    
Exposes the buffer as a list of messages in case return_messages is True. 

_property_ buffer_as_str _: str_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.buffer_as_str "Link to this definition")
    
Exposes the buffer as a string in case return_messages is False. 

_property_ memory_retriever _:[ VectorStoreRetrieverMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore.VectorStoreRetrieverMemory.html#langchain.memory.vectorstore.VectorStoreRetrieverMemory "langchain.memory.vectorstore.VectorStoreRetrieverMemory")_[#](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.memory_retriever "Link to this definition")
    
Return a memory retriever from the passed retriever object.
On this page 
  * [`ConversationVectorStoreTokenBufferMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory)
    * [`ai_prefix`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.ai_prefix)
    * [`chat_memory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.chat_memory)
    * [`human_prefix`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.human_prefix)
    * [`input_key`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.input_key)
    * [`llm`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.llm)
    * [`max_token_limit`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.max_token_limit)
    * [`memory_key`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.memory_key)
    * [`output_key`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.output_key)
    * [`previous_history_template`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.previous_history_template)
    * [`retriever`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.retriever)
    * [`return_messages`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.return_messages)
    * [`split_chunk_size`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.split_chunk_size)
    * [`aclear()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.aclear)
    * [`aload_memory_variables()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.aload_memory_variables)
    * [`asave_context()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.asave_context)
    * [`clear()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.clear)
    * [`load_memory_variables()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.load_memory_variables)
    * [`save_context()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.save_context)
    * [`save_remainder()`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.save_remainder)
    * [`buffer`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.buffer)
    * [`buffer_as_messages`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.buffer_as_messages)
    * [`buffer_as_str`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.buffer_as_str)
    * [`memory_retriever`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.html#langchain.memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory.memory_retriever)


© Copyright 2025, LangChain Inc. 

