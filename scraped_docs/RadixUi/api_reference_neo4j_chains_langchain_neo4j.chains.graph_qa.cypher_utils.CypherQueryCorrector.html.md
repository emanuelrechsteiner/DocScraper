---
url: https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html
scraped_at: 2025-05-25T18:06:11.600983
title: CypherQueryCorrector — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#main-content)
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
    * [`chains`](https://python.langchain.com/api_reference/neo4j/chains.html)
      * [GraphCypherQAChain](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.GraphCypherQAChain.html)
      * [CypherQueryCorrector](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html)
      * [Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html)
      * [construct_schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.construct_schema.html)
      * [get_function_response](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.get_function_response.html)
    * [`chat_message_histories`](https://python.langchain.com/api_reference/neo4j/chat_message_histories.html)
    * [`graphs`](https://python.langchain.com/api_reference/neo4j/graphs.html)
    * [`query_constructors`](https://python.langchain.com/api_reference/neo4j/query_constructors.html)
    * [`vectorstores`](https://python.langchain.com/api_reference/neo4j/vectorstores.html)
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
  * [langchain-neo4j: 0.4.0](https://python.langchain.com/api_reference/neo4j/index.html)
  * [`chains`](https://python.langchain.com/api_reference/neo4j/chains.html)
  * CypherQueryCorrector


# CypherQueryCorrector[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#cypherquerycorrector "Link to this heading") 

_class_ langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector( 
    _schemas :List[[Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")]_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector "Link to this definition")     
Used to correct relationship direction in generated Cypher statements. This code is copied from the winner’s submission to the Cypher competition: [sakusaku-rich/cypher-direction-competition](https://github.com/sakusaku-rich/cypher-direction-competition) 

Parameters:
    
**schemas** (_List_ _[_[_Schema_](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema") _]_) – list of schemas
Attributes
`node_pattern` |   
---|---  
`node_relation_node_pattern` |   
`path_pattern` |   
`property_pattern` |   
`relation_type_pattern` |   
Methods
[`__init__`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.__init__ "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.__init__")(schemas) |   
---|---  
[`clean_node`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.clean_node "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.clean_node")(node) |   
[`correct_query`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.correct_query "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.correct_query")(query) |   
[`detect_labels`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_labels "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_labels")(str_node, node_variable_dict) |   
[`detect_node_variables`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_node_variables "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_node_variables")(query) |   
[`detect_relation_types`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_relation_types "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_relation_types")(str_relation) |   
[`extract_node_variable`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.extract_node_variable "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.extract_node_variable")(part) |   
[`extract_paths`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.extract_paths "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.extract_paths")(query) |   
[`judge_direction`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.judge_direction "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.judge_direction")(relation) |   
[`verify_schema`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.verify_schema "langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.verify_schema")(from_node_labels, ...) |  

__init__( 
    _schemas :List[[Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")]_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.__init__)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.__init__ "Link to this definition")      

Parameters:
      
**schemas** (_List_ _[_[_Schema_](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema") _]_) – list of schemas 

clean_node(_node :str_) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.clean_node)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.clean_node "Link to this definition")
     

Parameters:
    
**node** (_str_) – node in string format 

Return type:
    
str 

correct_query(_query :str_) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.correct_query)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.correct_query "Link to this definition")
     

Parameters:
    
**query** (_str_) – cypher query 

Return type:
    
str 

detect_labels( 
    _str_node :str_,     _node_variable_dict :Dict[str,Any]_, ) → List[str][[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.detect_labels)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_labels "Link to this definition")      

Parameters:
    
  * **str_node** (_str_) – node in string format
  * **node_variable_dict** (_Dict_ _[__str_ _,__Any_ _]_) – dictionary of node variables



Return type:
    
_List_[str] 

detect_node_variables( 
    _query :str_, ) → Dict[str,List[str]][[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.detect_node_variables)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_node_variables "Link to this definition")      

Parameters:
    
**query** (_str_) – cypher query 

Return type:
    
_Dict_[str, _List_[str]] 

detect_relation_types( 
    _str_relation :str_, ) → Tuple[str,List[str]][[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.detect_relation_types)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_relation_types "Link to this definition")      

Parameters:
    
**str_relation** (_str_) – relation in string format 

Return type:
    
_Tuple_[str, _List_[str]] 

extract_node_variable( 
    _part :str_, ) → str|None[[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.extract_node_variable)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.extract_node_variable "Link to this definition")      

Parameters:
    
**part** (_str_) – node in string format 

Return type:
    
str | None 

extract_paths( 
    _query :str_, ) → List[str][[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.extract_paths)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.extract_paths "Link to this definition")      

Parameters:
    
**query** (_str_) – cypher query 

Return type:
    
_List_[str] 

judge_direction(_relation :str_) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.judge_direction)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.judge_direction "Link to this definition")
     

Parameters:
    
**relation** (_str_) – relation in string format 

Return type:
    
str 

verify_schema( 
    _from_node_labels :List[str]_,     _relation_types :List[str]_,     _to_node_labels :List[str]_, ) → bool[[source]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chains/graph_qa/cypher_utils.html#CypherQueryCorrector.verify_schema)[#](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.verify_schema "Link to this definition")      

Parameters:
    
  * **from_node_labels** (_List_ _[__str_ _]_) – labels of the from node
  * **relation_type** – type of the relation
  * **to_node_labels** (_List_ _[__str_ _]_) – labels of the to node
  * **relation_types** (_List_ _[__str_ _]_)



Return type:
    
bool
Examples using CypherQueryCorrector
  * [How to map values to a graph database](https://python.langchain.com/docs/how_to/graph_mapping/)


On this page 
  * [`CypherQueryCorrector`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector)
    * [`__init__()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.__init__)
    * [`clean_node()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.clean_node)
    * [`correct_query()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.correct_query)
    * [`detect_labels()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_labels)
    * [`detect_node_variables()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_node_variables)
    * [`detect_relation_types()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.detect_relation_types)
    * [`extract_node_variable()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.extract_node_variable)
    * [`extract_paths()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.extract_paths)
    * [`judge_direction()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.judge_direction)
    * [`verify_schema()`](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html#langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.verify_schema)


© Copyright 2025, LangChain Inc. 

