---
url: https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html
scraped_at: 2025-05-25T18:10:43.166691
title: AstraDBStore — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#main-content)
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
  * AstraDBStore


# AstraDBStore[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#astradbstore "Link to this heading") 

_class_ langchain_community.storage.astradb.AstraDBStore( 
    _collection_name :str_,     _token :str|None=None_,     _api_endpoint :str|None=None_,     _astra_db_client :[AstraDB](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB")|None=None_,     _namespace :str|None=None_,     _*_ ,     _async_astra_db_client :AsyncAstraDB|None=None_,     _pre_delete_collection :bool=False_,     _setup_mode :[SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")=SetupMode.SYNC_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBStore)[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore "Link to this definition")     
Deprecated since version 0.0.22: Use `:class:`~langchain_astradb.AstraDBStore`` instead. It will not be removed until langchain-community==1.0.
BaseStore implementation using DataStax AstraDB as the underlying store.
The value type can be any type serializable by json.dumps. Can be used to store embeddings with the CacheBackedEmbeddings.
Documents in the AstraDB collection will have the format
```
{
"_id":"<key>",
"value":<value>
}

```
Copy to clipboard 

Parameters:
    
  * **collection_name** (_str_) – name of the Astra DB collection to create/use.
  * **token** (_Optional_ _[__str_ _]_) – API token for Astra DB usage.
  * **api_endpoint** (_Optional_ _[__str_ _]_) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.
  * **astra_db_client** (_Optional_ _[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _]_) – _alternative to token+api_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.
  * **async_astra_db_client** (_Optional_ _[__AsyncAstraDB_ _]_) – _alternative to token+api_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.
  * **namespace** (_Optional_ _[__str_ _]_) – namespace (aka keyspace) where the collection is created. Defaults to the database’s “default namespace”.
  * **setup_mode** ([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")) – mode used to create the Astra DB collection (SYNC, ASYNC or OFF).
  * **pre_delete_collection** (_bool_) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.


Methods
[`__init__`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.__init__ "langchain_community.storage.astradb.AstraDBStore.__init__")(collection_name[, token, ...]) | BaseStore implementation using DataStax AstraDB as the underlying store.  
---|---  
[`amdelete`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amdelete "langchain_community.storage.astradb.AstraDBStore.amdelete")(keys) | Async delete the given keys and their associated values.  
[`amget`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amget "langchain_community.storage.astradb.AstraDBStore.amget")(keys) | Async get the values associated with the given keys.  
[`amset`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amset "langchain_community.storage.astradb.AstraDBStore.amset")(key_value_pairs) | Async set the values for the given keys.  
[`ayield_keys`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.ayield_keys "langchain_community.storage.astradb.AstraDBStore.ayield_keys")(*[, prefix]) | Async get an iterator over keys that match the given prefix.  
[`decode_value`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.decode_value "langchain_community.storage.astradb.AstraDBStore.decode_value")(value) | Decodes value from Astra DB  
[`encode_value`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.encode_value "langchain_community.storage.astradb.AstraDBStore.encode_value")(value) | Encodes value for Astra DB  
[`mdelete`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mdelete "langchain_community.storage.astradb.AstraDBStore.mdelete")(keys) | Delete the given keys and their associated values.  
[`mget`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mget "langchain_community.storage.astradb.AstraDBStore.mget")(keys) | Get the values associated with the given keys.  
[`mset`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mset "langchain_community.storage.astradb.AstraDBStore.mset")(key_value_pairs) | Set the values for the given keys.  
[`yield_keys`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.yield_keys "langchain_community.storage.astradb.AstraDBStore.yield_keys")(*[, prefix]) | Get an iterator over keys that match the given prefix. 

__init__( 
    _collection_name :str_,     _token :str|None=None_,     _api_endpoint :str|None=None_,     _astra_db_client :[AstraDB](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB")|None=None_,     _namespace :str|None=None_,     _*_ ,     _async_astra_db_client :AsyncAstraDB|None=None_,     _pre_delete_collection :bool=False_,     _setup_mode :[SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")=SetupMode.SYNC_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBStore.__init__)[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.__init__ "Link to this definition")       
BaseStore implementation using DataStax AstraDB as the underlying store.
The value type can be any type serializable by json.dumps. Can be used to store embeddings with the CacheBackedEmbeddings.
Documents in the AstraDB collection will have the format
```
{
"_id":"<key>",
"value":<value>
}

```
Copy to clipboard 

Parameters:
    
  * **collection_name** (_str_) – name of the Astra DB collection to create/use.
  * **token** (_Optional_ _[__str_ _]_) – API token for Astra DB usage.
  * **api_endpoint** (_Optional_ _[__str_ _]_) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.
  * **astra_db_client** (_Optional_ _[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _]_) – _alternative to token+api_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.
  * **async_astra_db_client** (_Optional_ _[__AsyncAstraDB_ _]_) – _alternative to token+api_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.
  * **namespace** (_Optional_ _[__str_ _]_) – namespace (aka keyspace) where the collection is created. Defaults to the database’s “default namespace”.
  * **setup_mode** ([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")) – mode used to create the Astra DB collection (SYNC, ASYNC or OFF).
  * **pre_delete_collection** (_bool_) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.



Return type:
    
None 

_async_ amdelete(_keys :Sequence[str]_) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amdelete "Link to this definition")
    
Async delete the given keys and their associated values. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys to delete. 

Return type:
    
None 

_async_ amget( 
    _keys :Sequence[str]_, ) → List[V|None][#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amget "Link to this definition")     
Async get the values associated with the given keys. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys. 

Returns:
    
A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None. 

Return type:
    
_List_[_V_ | None] 

_async_ amset( 
    _key_value_pairs :Sequence[Tuple[str,V]]_, ) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amset "Link to this definition")     
Async set the values for the given keys. 

Parameters:
    
**key_value_pairs** (_Sequence_ _[__tuple_ _[__K_ _,__V_ _]__]_) – A sequence of key-value pairs. 

Return type:
    
None 

_async_ ayield_keys( 
    _*_ ,     _prefix :str|None=None_, ) → AsyncIterator[str][#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.ayield_keys "Link to this definition")     
Async get an iterator over keys that match the given prefix. 

Parameters:
    
**prefix** (_str_) – The prefix to match. 

Yields:
    
_Iterator[K | str]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store. 

Return type:
    
_AsyncIterator_[str] 

decode_value(_value :Any_) → Any[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBStore.decode_value)[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.decode_value "Link to this definition")
    
Decodes value from Astra DB 

Parameters:
    
**value** (_Any_) 

Return type:
    
_Any_ 

encode_value(_value :Any_) → Any[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBStore.encode_value)[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.encode_value "Link to this definition")
    
Encodes value for Astra DB 

Parameters:
    
**value** (_Any_) 

Return type:
    
_Any_ 

mdelete(_keys :Sequence[str]_) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mdelete "Link to this definition")
    
Delete the given keys and their associated values. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys to delete. 

Return type:
    
None 

mget( 
    _keys :Sequence[str]_, ) → List[V|None][#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mget "Link to this definition")     
Get the values associated with the given keys. 

Parameters:
    
**keys** (_Sequence_ _[__K_ _]_) – A sequence of keys. 

Returns:
    
A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None. 

Return type:
    
_List_[_V_ | None] 

mset( 
    _key_value_pairs :Sequence[Tuple[str,V]]_, ) → None[#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mset "Link to this definition")     
Set the values for the given keys. 

Parameters:
    
**key_value_pairs** (_Sequence_ _[__tuple_ _[__K_ _,__V_ _]__]_) – A sequence of key-value pairs. 

Return type:
    
None 

yield_keys( 
    _*_ ,     _prefix :str|None=None_, ) → Iterator[str][#](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.yield_keys "Link to this definition")     
Get an iterator over keys that match the given prefix. 

Parameters:
    
**prefix** (_str_) – The prefix to match. 

Yields:
    
_Iterator[K | str]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store. 

Return type:
    
_Iterator_[str]
On this page 
  * [`AstraDBStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore)
    * [`__init__()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.__init__)
    * [`amdelete()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amdelete)
    * [`amget()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amget)
    * [`amset()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.amset)
    * [`ayield_keys()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.ayield_keys)
    * [`decode_value()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.decode_value)
    * [`encode_value()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.encode_value)
    * [`mdelete()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mdelete)
    * [`mget()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mget)
    * [`mset()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.mset)
    * [`yield_keys()`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore.yield_keys)


© Copyright 2025, LangChain Inc. 
  *[*]: Keyword-only parameters separator (PEP 3102)

