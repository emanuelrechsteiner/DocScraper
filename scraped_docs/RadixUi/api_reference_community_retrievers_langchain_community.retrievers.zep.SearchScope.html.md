---
url: https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html
scraped_at: 2025-05-25T18:09:47.761835
title: SearchScope — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#main-content)
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
      * [ArceeRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.arcee.ArceeRetriever.html)
      * [ArxivRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.arxiv.ArxivRetriever.html)
      * [AskNewsRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.asknews.AskNewsRetriever.html)
      * [AzureAISearchRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.azure_ai_search.AzureAISearchRetriever.html)
      * [AzureCognitiveSearchRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.azure_ai_search.AzureCognitiveSearchRetriever.html)
      * [RetrievalConfig](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.bedrock.RetrievalConfig.html)
      * [VectorSearchConfig](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.bedrock.VectorSearchConfig.html)
      * [BM25Retriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.bm25.BM25Retriever.html)
      * [BreebsRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.breebs.BreebsRetriever.html)
      * [ChaindeskRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.chaindesk.ChaindeskRetriever.html)
      * [ChatGPTPluginRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.chatgpt_plugin_retriever.ChatGPTPluginRetriever.html)
      * [DataberryRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.databerry.DataberryRetriever.html)
      * [DocArrayRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.docarray.DocArrayRetriever.html)
      * [SearchType](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.docarray.SearchType.html)
      * [DriaRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.dria_index.DriaRetriever.html)
      * [ElasticSearchBM25Retriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.elastic_search_bm25.ElasticSearchBM25Retriever.html)
      * [EmbedchainRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.embedchain.EmbedchainRetriever.html)
      * [GoogleCloudEnterpriseSearchRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.google_vertex_ai_search.GoogleCloudEnterpriseSearchRetriever.html)
      * [KayAiRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kay.KayAiRetriever.html)
      * [AdditionalResultAttribute](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.AdditionalResultAttribute.html)
      * [AdditionalResultAttributeValue](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.AdditionalResultAttributeValue.html)
      * [DocumentAttribute](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.DocumentAttribute.html)
      * [DocumentAttributeValue](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.DocumentAttributeValue.html)
      * [Highlight](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.Highlight.html)
      * [QueryResult](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.QueryResult.html)
      * [QueryResultItem](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.QueryResultItem.html)
      * [ResultItem](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.ResultItem.html)
      * [RetrieveResult](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.RetrieveResult.html)
      * [RetrieveResultItem](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.RetrieveResultItem.html)
      * [TextWithHighLights](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.TextWithHighLights.html)
      * [KNNRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.knn.KNNRetriever.html)
      * [LlamaIndexGraphRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.llama_index.LlamaIndexGraphRetriever.html)
      * [LlamaIndexRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.llama_index.LlamaIndexRetriever.html)
      * [MetalRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.metal.MetalRetriever.html)
      * [MilvusRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.milvus.MilvusRetriever.html)
      * [NanoPQRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.nanopq.NanoPQRetriever.html)
      * [NeedleRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.needle.NeedleRetriever.html)
      * [OutlineRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.outline.OutlineRetriever.html)
      * [PineconeHybridSearchRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.pinecone_hybrid_search.PineconeHybridSearchRetriever.html)
      * [PubMedRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.pubmed.PubMedRetriever.html)
      * [RememberizerRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.rememberizer.RememberizerRetriever.html)
      * [RemoteLangChainRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.remote_retriever.RemoteLangChainRetriever.html)
      * [SVMRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.svm.SVMRetriever.html)
      * [SearchDepth](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.tavily_search_api.SearchDepth.html)
      * [TavilySearchAPIRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.tavily_search_api.TavilySearchAPIRetriever.html)
      * [TFIDFRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.tfidf.TFIDFRetriever.html)
      * [NeuralDBRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.thirdai_neuraldb.NeuralDBRetriever.html)
      * [VespaRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.vespa_retriever.VespaRetriever.html)
      * [QuestionListOutputParser](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.web_research.QuestionListOutputParser.html)
      * [SearchQueries](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.web_research.SearchQueries.html)
      * [WebResearchRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.web_research.WebResearchRetriever.html)
      * [WikipediaRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.wikipedia.WikipediaRetriever.html)
      * [YouRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.you.YouRetriever.html)
      * [SearchScope](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html)
      * [SearchType](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchType.html)
      * [ZepRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.ZepRetriever.html)
      * [ZepCloudRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep_cloud.ZepCloudRetriever.html)
      * [ZillizRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zilliz.ZillizRetriever.html)
      * [default_preprocessing_func](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.bm25.default_preprocessing_func.html)
      * [clean_excerpt](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.clean_excerpt.html)
      * [combined_text](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.combined_text.html)
      * [create_index](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.knn.create_index.html)
      * [MilvusRetreiver](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.milvus.MilvusRetreiver.html)
      * [create_index](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.nanopq.create_index.html)
      * [create_index](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.pinecone_hybrid_search.create_index.html)
      * [hash_text](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.pinecone_hybrid_search.hash_text.html)
      * [create_index](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.svm.create_index.html)
      * [ZillizRetreiver](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zilliz.ZillizRetreiver.html)
      * [AmazonKnowledgeBasesRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.bedrock.AmazonKnowledgeBasesRetriever.html)
      * [CohereRagRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.cohere_rag_retriever.CohereRagRetriever.html)
      * [GoogleDocumentAIWarehouseRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.google_cloud_documentai_warehouse.GoogleDocumentAIWarehouseRetriever.html)
      * [GoogleVertexAIMultiTurnSearchRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.google_vertex_ai_search.GoogleVertexAIMultiTurnSearchRetriever.html)
      * [GoogleVertexAISearchRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.google_vertex_ai_search.GoogleVertexAISearchRetriever.html)
      * [AmazonKendraRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.AmazonKendraRetriever.html)
      * [QdrantSparseVectorRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.qdrant_sparse_vector_retriever.QdrantSparseVectorRetriever.html)
      * [WeaviateHybridSearchRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.weaviate_hybrid_search.WeaviateHybridSearchRetriever.html)
    * [`storage`](https://python.langchain.com/api_reference/community/storage.html)
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
  * [`retrievers`](https://python.langchain.com/api_reference/community/retrievers.html)
  * SearchScope


# SearchScope[#](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#searchscope "Link to this heading") 

_class_ langchain_community.retrievers.zep.SearchScope(_value_)[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/zep.html#SearchScope)[#](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#langchain_community.retrievers.zep.SearchScope "Link to this definition")
    
Which documents to search. Messages or Summaries? 

messages _= 'messages'_[#](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#langchain_community.retrievers.zep.SearchScope.messages "Link to this definition")
    
Search chat history messages. 

summary _= 'summary'_[#](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#langchain_community.retrievers.zep.SearchScope.summary "Link to this definition")
    
Search chat history summaries.
Examples using SearchScope
  * [Zep Open Source](https://python.langchain.com/docs/integrations/retrievers/zep_memorystore/)


On this page 
  * [`SearchScope`](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#langchain_community.retrievers.zep.SearchScope)
    * [`messages`](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#langchain_community.retrievers.zep.SearchScope.messages)
    * [`summary`](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#langchain_community.retrievers.zep.SearchScope.summary)


© Copyright 2025, LangChain Inc. 

