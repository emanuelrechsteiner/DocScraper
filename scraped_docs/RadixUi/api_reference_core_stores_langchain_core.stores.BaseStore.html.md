---
url: https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html
scraped_at: 2025-05-25T18:12:40.067085
title: BaseStore — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#main-content)
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
  * [`stores`](https://python.langchain.com/api_reference/core/stores.html)
  * BaseStore


# BaseStore[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#basestore "Link to this heading") 

_class_ langchain_core.stores.BaseStore[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "Link to this definition")
    
Abstract interface for a key-value store.
This is an interface that’s meant to abstract away the details of different key-value stores. It provides a simple interface for getting, setting, and deleting key-value pairs.
The basic methods are mget, mset, and mdelete for getting, setting, and deleting multiple key-value pairs at once. The yield_keys method is used to iterate over keys that match a given prefix.
The async versions of these methods are also provided, which are meant to be used in async contexts. The async methods are named with an a prefix, e.g., amget, amset, amdelete, and ayield_keys.
By default, the amget, amset, amdelete, and ayield_keys methods are implemented using the synchronous methods. If the store can natively support async operations, it should override these methods.
By design the methods only accept batches of keys and values, and not single keys or values. This is done to force user code to work with batches which will usually be more efficient by saving on round trips to the store.
Examples
```
fromlangchain.storageimport BaseStore
classMyInMemoryStore(BaseStore[str, int]):
  def__init__(self):
    self.store = {}
  defmget(self, keys):
    return [self.store.get(key) for key in keys]
  defmset(self, key_value_pairs):
    for key, value in key_value_pairs:
      self.store[key] = value
  defmdelete(self, keys):
    for key in keys:
      if key in self.store:
        del self.store[key]
  defyield_keys(self, prefix=None):
    if prefix is None:
      yield from self.store.keys()
    else:
      for key in self.store.keys():
        if key.startswith(prefix):
          yield key

```
Copy to clipboard
Methods
[`amdelete`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amdelete "langchain_core.stores.BaseStore.amdelete")(keys) | Async delete the given keys and their associated values.  
---|---  
[`amget`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amget "langchain_core.stores.BaseStore.amget")(keys) | Async get the values associated with the given keys.  
[`amset`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amset "langchain_core.stores.BaseStore.amset")(key_value_pairs) | Async set the values for the given keys.  
[`ayield_keys`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.ayield_keys "langchain_core.stores.BaseStore.ayield_keys")(*[, prefix]) | Async get an iterator over keys that match the given prefix.  
[`mdelete`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mdelete "langchain_core.stores.BaseStore.mdelete")(keys) | Delete the given keys and their associated values.  
[`mget`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mget "langchain_core.stores.BaseStore.mget")(keys) | Get the values associated with the given keys.  
[`mset`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mset "langchain_core.stores.BaseStore.mset")(key_value_pairs) | Set the values for the given keys.  
[`yield_keys`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.yield_keys "langchain_core.stores.BaseStore.yield_keys")(*[, prefix]) | Get an iterator over keys that match the given prefix. 

_async_ amdelete( 
    _keys :Sequence[K]_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.amdelete)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amdelete "Link to this definition")       
Async delete the given keys and their associated values. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys to delete. 

Return type:
    
None 

_async_ amget( 
    _keys :Sequence[K]_, ) → list[V|None][[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.amget)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amget "Link to this definition")     
Async get the values associated with the given keys. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys. 

Returns:
    
A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None. 

Return type:
    
list[_V_ | None] 

_async_ amset( 
    _key_value_pairs :Sequence[tuple[K,V]]_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.amset)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amset "Link to this definition")     
Async set the values for the given keys. 

Parameters:
    
**key_value_pairs** (_Sequence_ _[__tuple_ _[__K_ _,__V_ _]__]_) – A sequence of key-value pairs. 

Return type:
    
None 

_async_ ayield_keys( 
    _*_ ,     _prefix :str|None=None_, ) → AsyncIterator[K]|AsyncIterator[str][[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.ayield_keys)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.ayield_keys "Link to this definition")     
Async get an iterator over keys that match the given prefix. 

Parameters:
    
**prefix** (_str_) – The prefix to match. 

Yields:
    
_Iterator[K | str]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store. 

Return type:
    
_AsyncIterator_[_K_] | _AsyncIterator_[str] 

_abstractmethod_ mdelete( 
    _keys :Sequence[K]_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.mdelete)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mdelete "Link to this definition")     
Delete the given keys and their associated values. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys to delete. 

Return type:
    
None 

_abstractmethod_ mget( 
    _keys :Sequence[K]_, ) → list[V|None][[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.mget)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mget "Link to this definition")     
Get the values associated with the given keys. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys. 

Returns:
    
A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None. 

Return type:
    
list[_V_ | None] 

_abstractmethod_ mset( 
    _key_value_pairs :Sequence[tuple[K,V]]_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.mset)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mset "Link to this definition")     
Set the values for the given keys. 

Parameters:
    
**key_value_pairs** (_Sequence_ _[__tuple_ _[__K_ _,__V_ _]__]_) – A sequence of key-value pairs. 

Return type:
    
None 

_abstractmethod_ yield_keys( 
    _*_ ,     _prefix :str|None=None_, ) → Iterator[K]|Iterator[str][[source]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.yield_keys)[#](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.yield_keys "Link to this definition")     
Get an iterator over keys that match the given prefix. 

Parameters:
    
**prefix** (_str_) – The prefix to match. 

Yields:
    
_Iterator[K | str]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store. 

Return type:
    
_Iterator_[_K_] | _Iterator_[str]
Examples using BaseStore
  * [Fleet AI Context](https://python.langchain.com/docs/integrations/retrievers/fleet_context/)


On this page 
  * [`BaseStore`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore)
    * [`amdelete()`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amdelete)
    * [`amget()`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amget)
    * [`amset()`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.amset)
    * [`ayield_keys()`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.ayield_keys)
    * [`mdelete()`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mdelete)
    * [`mget()`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mget)
    * [`mset()`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.mset)
    * [`yield_keys()`](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore.yield_keys)


© Copyright 2025, LangChain Inc. 
  *[*]: Keyword-only parameters separator (PEP 3102)

