---
url: https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html
scraped_at: 2025-05-25T18:01:06.574397
title: UpstashRedisStore — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#main-content)
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
    * [`query_constructors`](https://python.langchain.com/api_reference/community/query_constructors.html)
    * [`retrievers`](https://python.langchain.com/api_reference/community/retrievers.html)
    * [`storage`](https://python.langchain.com/api_reference/community/storage.html)
      * [AstraDBBaseStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBBaseStore.html)
      * [CassandraByteStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.cassandra.CassandraByteStore.html)
      * [MongoDBByteStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.mongodb.MongoDBByteStore.html)
      * [MongoDBStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.mongodb.MongoDBStore.html)
      * [RedisStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.redis.RedisStore.html)
      * [LangchainKeyValueStores](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.sql.LangchainKeyValueStores.html)
      * [SQLStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.sql.SQLStore.html)
      * [UpstashRedisByteStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisByteStore.html)
      * [items_equal](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.sql.items_equal.html)
      * [AstraDBByteStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBByteStore.html)
      * [AstraDBStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html)
      * [UpstashRedisStore](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html)
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
  * [`storage`](https://python.langchain.com/api_reference/community/storage.html)
  * UpstashRedisStore


# UpstashRedisStore[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#upstashredisstore "Link to this heading") 

_class_ langchain_community.storage.upstash_redis.UpstashRedisStore( 
    _*_ ,     _client :Any=None_,     _url :str|None=None_,     _token :str|None=None_,     _ttl :int|None=None_,     _namespace :str|None=None_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/upstash_redis.html#UpstashRedisStore)[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore "Link to this definition")     
Deprecated since version 0.0.1: Use [`UpstashRedisByteStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisByteStore.html#langchain_community.storage.upstash_redis.UpstashRedisByteStore "langchain_community.storage.upstash_redis.UpstashRedisByteStore") instead.
BaseStore implementation using Upstash Redis as the underlying store to store strings.
Deprecated in favor of the more generic UpstashRedisByteStore.
Initialize the UpstashRedisStore with HTTP API.
Must provide either an Upstash Redis client or a url. 

Parameters:
    
  * **client** (_Any_) – An Upstash Redis instance
  * **url** (_str_ _|__None_) – UPSTASH_REDIS_REST_URL
  * **token** (_str_ _|__None_) – UPSTASH_REDIS_REST_TOKEN
  * **ttl** (_int_ _|__None_) – time to expire keys in seconds if provided, if None keys will never expire
  * **namespace** (_str_ _|__None_) – if provided, all keys will be prefixed with this namespace


Methods
[`__init__`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.__init__ "langchain_community.storage.upstash_redis.UpstashRedisStore.__init__")(*[, client, url, token, ttl, namespace]) | Initialize the UpstashRedisStore with HTTP API.  
---|---  
[`amdelete`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amdelete "langchain_community.storage.upstash_redis.UpstashRedisStore.amdelete")(keys) | Async delete the given keys and their associated values.  
[`amget`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amget "langchain_community.storage.upstash_redis.UpstashRedisStore.amget")(keys) | Async get the values associated with the given keys.  
[`amset`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amset "langchain_community.storage.upstash_redis.UpstashRedisStore.amset")(key_value_pairs) | Async set the values for the given keys.  
[`ayield_keys`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.ayield_keys "langchain_community.storage.upstash_redis.UpstashRedisStore.ayield_keys")(*[, prefix]) | Async get an iterator over keys that match the given prefix.  
[`mdelete`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mdelete "langchain_community.storage.upstash_redis.UpstashRedisStore.mdelete")(keys) | Delete the given keys.  
[`mget`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mget "langchain_community.storage.upstash_redis.UpstashRedisStore.mget")(keys) | Get the values associated with the given keys.  
[`mset`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mset "langchain_community.storage.upstash_redis.UpstashRedisStore.mset")(key_value_pairs) | Set the given key-value pairs.  
[`yield_keys`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.yield_keys "langchain_community.storage.upstash_redis.UpstashRedisStore.yield_keys")(*[, prefix]) | Yield keys in the store. 

__init__( 
    _*_ ,     _client :Any=None_,     _url :str|None=None_,     _token :str|None=None_,     _ttl :int|None=None_,     _namespace :str|None=None_, ) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.__init__ "Link to this definition")       
Initialize the UpstashRedisStore with HTTP API.
Must provide either an Upstash Redis client or a url. 

Parameters:
    
  * **client** (_Any_) – An Upstash Redis instance
  * **url** (_str_ _|__None_) – UPSTASH_REDIS_REST_URL
  * **token** (_str_ _|__None_) – UPSTASH_REDIS_REST_TOKEN
  * **ttl** (_int_ _|__None_) – time to expire keys in seconds if provided, if None keys will never expire
  * **namespace** (_str_ _|__None_) – if provided, all keys will be prefixed with this namespace



Return type:
    
None 

_async_ amdelete( 
    _keys :Sequence[K]_, ) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amdelete "Link to this definition")     
Async delete the given keys and their associated values. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys to delete. 

Return type:
    
None 

_async_ amget( 
    _keys :Sequence[K]_, ) → list[V|None][#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amget "Link to this definition")     
Async get the values associated with the given keys. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys. 

Returns:
    
A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None. 

Return type:
    
list[_V_ | None] 

_async_ amset( 
    _key_value_pairs :Sequence[tuple[K,V]]_, ) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amset "Link to this definition")     
Async set the values for the given keys. 

Parameters:
    
**key_value_pairs** (_Sequence_ _[__tuple_ _[__K_ _,__V_ _]__]_) – A sequence of key-value pairs. 

Return type:
    
None 

_async_ ayield_keys( 
    _*_ ,     _prefix :str|None=None_, ) → AsyncIterator[K]|AsyncIterator[str][#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.ayield_keys "Link to this definition")     
Async get an iterator over keys that match the given prefix. 

Parameters:
    
**prefix** (_str_) – The prefix to match. 

Yields:
    
_Iterator[K | str]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store. 

Return type:
    
_AsyncIterator_[_K_] | _AsyncIterator_[str] 

mdelete( 
    _keys :Sequence[str]_, ) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mdelete "Link to this definition")     
Delete the given keys. 

Parameters:
    
**keys** (_Sequence_ _[__str_ _]_) 

Return type:
    
None 

mget( 
    _keys :Sequence[str]_, ) → List[str|None][#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mget "Link to this definition")     
Get the values associated with the given keys. 

Parameters:
    
**keys** (_Sequence_ _[__str_ _]_) 

Return type:
    
_List_[str | None] 

mset( 
    _key_value_pairs :Sequence[Tuple[str,str]]_, ) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mset "Link to this definition")     
Set the given key-value pairs. 

Parameters:
    
**key_value_pairs** (_Sequence_ _[__Tuple_ _[__str_ _,__str_ _]__]_) 

Return type:
    
None 

yield_keys( 
    _*_ ,     _prefix :str|None=None_, ) → Iterator[str][#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.yield_keys "Link to this definition")     
Yield keys in the store. 

Parameters:
    
**prefix** (_str_ _|__None_) 

Return type:
    
_Iterator_[str]
On this page 
  * [`UpstashRedisStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore)
    * [`__init__()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.__init__)
    * [`amdelete()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amdelete)
    * [`amget()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amget)
    * [`amset()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.amset)
    * [`ayield_keys()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.ayield_keys)
    * [`mdelete()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mdelete)
    * [`mget()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mget)
    * [`mset()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.mset)
    * [`yield_keys()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore.yield_keys)


© Copyright 2025, LangChain Inc. 
  *[*]: Keyword-only parameters separator (PEP 3102)

