---
url: https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html
scraped_at: 2025-05-25T17:58:59.748102
title: InMemoryChatMessageHistory — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#main-content)
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
      * [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html)
      * [InMemoryChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html)
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
  * [`chat_history`](https://python.langchain.com/api_reference/core/chat_history.html)
  * InMemoryChatMessageHistory


# InMemoryChatMessageHistory[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#inmemorychatmessagehistory "Link to this heading") 

_class_ langchain_core.chat_history.InMemoryChatMessageHistory[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#InMemoryChatMessageHistory)[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory "Link to this definition")
    
Bases: [`BaseChatMessageHistory`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory"), `BaseModel`
In memory implementation of chat message history.
Stores messages in a memory list.
Create a new model by parsing and validating input data from keyword arguments.
Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.
self is explicitly positional-only to allow self as a field name. 

_param_ messages _: list[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")]__[Optional]_[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.messages "Link to this definition")
    
A list of messages stored in memory. 

_async_ aadd_messages( 
    _messages :Sequence[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")]_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#InMemoryChatMessageHistory.aadd_messages)[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.aadd_messages "Link to this definition")     
Async add messages to the store. 

Parameters:
    
**messages** (_Sequence_ _[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _]_) – The messages to add. 

Return type:
    
None 

_async_ aclear() → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#InMemoryChatMessageHistory.aclear)[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.aclear "Link to this definition")
    
Async clear all messages from the store. 

Return type:
    
None 

add_ai_message( 
    _message :[AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage "langchain_core.messages.ai.AIMessage")|str_, ) → None[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.add_ai_message "Link to this definition")     
Convenience method for adding an AI message string to the store.
Please note that this is a convenience method. Code should favor the bulk add_messages interface instead to save on round-trips to the underlying persistence layer.
This method may be deprecated in a future release. 

Parameters:
    
**message** ([_AIMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage "langchain_core.messages.ai.AIMessage") _|__str_) – The AI message to add. 

Return type:
    
None 

add_message( 
    _message :[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#InMemoryChatMessageHistory.add_message)[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.add_message "Link to this definition")     
Add a self-created message to the store. 

Parameters:
    
**message** ([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")) – The message to add. 

Return type:
    
None 

add_messages( 
    _messages :Sequence[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")]_, ) → None[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.add_messages "Link to this definition")     
Add a list of messages.
Implementations should over-ride this method to handle bulk addition of messages in an efficient manner to avoid unnecessary round-trips to the underlying store. 

Parameters:
    
**messages** (_Sequence_ _[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _]_) – A sequence of BaseMessage objects to store. 

Return type:
    
None 

add_user_message( 
    _message :[HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html#langchain_core.messages.human.HumanMessage "langchain_core.messages.human.HumanMessage")|str_, ) → None[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.add_user_message "Link to this definition")     
Convenience method for adding a human message string to the store.
Please note that this is a convenience method. Code should favor the bulk add_messages interface instead to save on round-trips to the underlying persistence layer.
This method may be deprecated in a future release. 

Parameters:
    
**message** ([_HumanMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html#langchain_core.messages.human.HumanMessage "langchain_core.messages.human.HumanMessage") _|__str_) – The human message to add to the store. 

Return type:
    
None 

_async_ aget_messages() → list[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")][[source]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#InMemoryChatMessageHistory.aget_messages)[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.aget_messages "Link to this definition")
    
Async version of getting messages.
Can over-ride this method to provide an efficient async implementation. In general, fetching messages may involve IO to the underlying persistence layer. 

Returns:
    
List of messages. 

Return type:
    
list[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")] 

clear() → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#InMemoryChatMessageHistory.clear)[#](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.clear "Link to this definition")
    
Clear all messages from the store. 

Return type:
    
None
Examples using InMemoryChatMessageHistory
  * [# Legacy](https://python.langchain.com/docs/versions/migrating_chains/conversation_chain/)
  * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)
  * [ChatNVIDIA](https://python.langchain.com/docs/integrations/chat/nvidia_ai_endpoints/)
  * [How to migrate from legacy LangChain agents to LangGraph](https://python.langchain.com/docs/how_to/migrate_agent/)
  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)


On this page 
  * [`InMemoryChatMessageHistory`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory)
    * [`messages`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.messages)
    * [`aadd_messages()`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.aadd_messages)
    * [`aclear()`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.aclear)
    * [`add_ai_message()`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.add_ai_message)
    * [`add_message()`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.add_message)
    * [`add_messages()`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.add_messages)
    * [`add_user_message()`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.add_user_message)
    * [`aget_messages()`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.aget_messages)
    * [`clear()`](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.InMemoryChatMessageHistory.html#langchain_core.chat_history.InMemoryChatMessageHistory.clear)


© Copyright 2025, LangChain Inc. 

