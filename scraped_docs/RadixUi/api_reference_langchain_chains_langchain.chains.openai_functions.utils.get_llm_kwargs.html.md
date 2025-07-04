---
url: https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.utils.get_llm_kwargs.html
scraped_at: 2025-05-25T18:05:38.683722
title: get_llm_kwargs — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.utils.get_llm_kwargs.html#main-content)
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
      * [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html)
      * [BaseCombineDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.BaseCombineDocumentsChain.html)
      * [AsyncCombineDocsProtocol](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol.html)
      * [CombineDocsProtocol](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.CombineDocsProtocol.html)
      * [ConstitutionalPrinciple](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.models.ConstitutionalPrinciple.html)
      * [BaseConversationalRetrievalChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.BaseConversationalRetrievalChain.html)
      * [ChatVectorDBChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.ChatVectorDBChain.html)
      * [InputType](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.InputType.html)
      * [ElasticsearchDatabaseChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.elasticsearch_database.base.ElasticsearchDatabaseChain.html)
      * [FlareChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.flare.base.FlareChain.html)
      * [QuestionGeneratorChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.flare.base.QuestionGeneratorChain.html)
      * [FinishedOutputParser](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.flare.prompts.FinishedOutputParser.html)
      * [HypotheticalDocumentEmbedder](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.hyde.base.HypotheticalDocumentEmbedder.html)
      * [OpenAIModerationChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.moderation.OpenAIModerationChain.html)
      * [Crawler](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.natbot.crawler.Crawler.html)
      * [ElementInViewPort](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.natbot.crawler.ElementInViewPort.html)
      * [FactWithEvidence](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.FactWithEvidence.html)
      * [QuestionAnswer](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.QuestionAnswer.html)
      * [SimpleRequestChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.openapi.SimpleRequestChain.html)
      * [AnswerWithSources](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.AnswerWithSources.html)
      * [BasePromptSelector](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.BasePromptSelector.html)
      * [ConditionalPromptSelector](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.ConditionalPromptSelector.html)
      * [LoadingCallable](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.loading.LoadingCallable.html)
      * [RetrievalQAWithSourcesChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain.html)
      * [VectorDBQAWithSourcesChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.vector_db.VectorDBQAWithSourcesChain.html)
      * [StructuredQueryOutputParser](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.StructuredQueryOutputParser.html)
      * [ISO8601Date](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.ISO8601Date.html)
      * [ISO8601DateTime](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.ISO8601DateTime.html)
      * [QueryTransformer](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.QueryTransformer.html)
      * [AttributeInfo](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.schema.AttributeInfo.html)
      * [LoadingCallable](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.question_answering.chain.LoadingCallable.html)
      * [MultiRouteChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.base.MultiRouteChain.html)
      * [Route](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.base.Route.html)
      * [RouterChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.base.RouterChain.html)
      * [EmbeddingRouterChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.embedding_router.EmbeddingRouterChain.html)
      * [RouterOutputParser](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.llm_router.RouterOutputParser.html)
      * [MultiRetrievalQAChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.multi_retrieval_qa.MultiRetrievalQAChain.html)
      * [SequentialChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sequential.SequentialChain.html)
      * [SimpleSequentialChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sequential.SimpleSequentialChain.html)
      * [SQLInput](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.SQLInput.html)
      * [SQLInputWithTables](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.SQLInputWithTables.html)
      * [LoadingCallable](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.summarize.chain.LoadingCallable.html)
      * [TransformChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.transform.TransformChain.html)
      * [acollapse_docs](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.acollapse_docs.html)
      * [collapse_docs](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.collapse_docs.html)
      * [split_list_of_docs](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.split_list_of_docs.html)
      * [create_stuff_documents_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.stuff.create_stuff_documents_chain.html)
      * [generate_example](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.example_generator.generate_example.html)
      * [create_history_aware_retriever](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.history_aware_retriever.create_history_aware_retriever.html)
      * [create_citation_fuzzy_match_runnable](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable.html)
      * [openapi_spec_to_openai_fn](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.openapi.openapi_spec_to_openai_fn.html)
      * [get_llm_kwargs](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.utils.get_llm_kwargs.html)
      * [is_chat_model](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.is_chat_model.html)
      * [is_llm](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.is_llm.html)
      * [construct_examples](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.construct_examples.html)
      * [fix_filter_directive](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.fix_filter_directive.html)
      * [get_query_constructor_prompt](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.get_query_constructor_prompt.html)
      * [load_query_constructor_runnable](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.load_query_constructor_runnable.html)
      * [get_parser](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.get_parser.html)
      * [create_retrieval_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval.create_retrieval_chain.html)
      * [create_sql_query_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.create_sql_query_chain.html)
      * [get_openai_output_parser](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.get_openai_output_parser.html)
      * [load_summarize_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.summarize.chain.load_summarize_chain.html)
      * [APIChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.api.base.APIChain.html)
      * [AnalyzeDocumentChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.AnalyzeDocumentChain.html)
      * [MapReduceDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.map_reduce.MapReduceDocumentsChain.html)
      * [MapRerankDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.map_rerank.MapRerankDocumentsChain.html)
      * [ReduceDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.ReduceDocumentsChain.html)
      * [RefineDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.refine.RefineDocumentsChain.html)
      * [StuffDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.stuff.StuffDocumentsChain.html)
      * [ConstitutionalChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.base.ConstitutionalChain.html)
      * [ConversationChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversation.base.ConversationChain.html)
      * [ConversationalRetrievalChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.ConversationalRetrievalChain.html)
      * [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html)
      * [LLMCheckerChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_checker.base.LLMCheckerChain.html)
      * [LLMMathChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_math.base.LLMMathChain.html)
      * [LLMSummarizationCheckerChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html)
      * [MapReduceChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.mapreduce.MapReduceChain.html)
      * [NatBotChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.natbot.base.NatBotChain.html)
      * [QAGenerationChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_generation.base.QAGenerationChain.html)
      * [BaseQAWithSourcesChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.base.BaseQAWithSourcesChain.html)
      * [QAWithSourcesChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.base.QAWithSourcesChain.html)
      * [BaseRetrievalQA](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval_qa.base.BaseRetrievalQA.html)
      * [RetrievalQA](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval_qa.base.RetrievalQA.html)
      * [VectorDBQA](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval_qa.base.VectorDBQA.html)
      * [LLMRouterChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.llm_router.LLMRouterChain.html)
      * [MultiPromptChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.multi_prompt.MultiPromptChain.html)
      * [load_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.loading.load_chain.html)
      * [load_chain_from_config](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.loading.load_chain_from_config.html)
      * [create_openai_fn_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.base.create_openai_fn_chain.html)
      * [create_structured_output_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.base.create_structured_output_chain.html)
      * [create_citation_fuzzy_match_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_chain.html)
      * [create_extraction_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.extraction.create_extraction_chain.html)
      * [create_extraction_chain_pydantic](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.extraction.create_extraction_chain_pydantic.html)
      * [get_openapi_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.openapi.get_openapi_chain.html)
      * [create_qa_with_sources_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.create_qa_with_sources_chain.html)
      * [create_qa_with_structure_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.create_qa_with_structure_chain.html)
      * [create_tagging_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.tagging.create_tagging_chain.html)
      * [create_tagging_chain_pydantic](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.tagging.create_tagging_chain_pydantic.html)
      * [create_extraction_chain_pydantic](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_tools.extraction.create_extraction_chain_pydantic.html)
      * [load_qa_with_sources_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.loading.load_qa_with_sources_chain.html)
      * [load_query_constructor_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.load_query_constructor_chain.html)
      * [load_qa_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.question_answering.chain.load_qa_chain.html)
      * [create_openai_fn_runnable](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.create_openai_fn_runnable.html)
      * [create_structured_output_runnable](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.create_structured_output_runnable.html)
    * [`chat_models`](https://python.langchain.com/api_reference/langchain/chat_models.html)
    * [`embeddings`](https://python.langchain.com/api_reference/langchain/embeddings.html)
    * [`evaluation`](https://python.langchain.com/api_reference/langchain/evaluation.html)
    * [`globals`](https://python.langchain.com/api_reference/langchain/globals.html)
    * [`hub`](https://python.langchain.com/api_reference/langchain/hub.html)
    * [`indexes`](https://python.langchain.com/api_reference/langchain/indexes.html)
    * [`memory`](https://python.langchain.com/api_reference/langchain/memory.html)
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
  * [`chains`](https://python.langchain.com/api_reference/langchain/chains.html)
  * get_llm_kwargs


# get_llm_kwargs[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.utils.get_llm_kwargs.html#get-llm-kwargs "Link to this heading") 

langchain.chains.openai_functions.utils.get_llm_kwargs(_function :dict_) → dict[[source]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/utils.html#get_llm_kwargs)[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.utils.get_llm_kwargs.html#langchain.chains.openai_functions.utils.get_llm_kwargs "Link to this definition")
    
Return the kwargs for the LLMChain constructor. 

Parameters:
    
**function** (_dict_) – The function to use. 

Returns:
    
The kwargs for the LLMChain constructor. 

Return type:
    
dict
On this page 
  * [`get_llm_kwargs()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.utils.get_llm_kwargs.html#langchain.chains.openai_functions.utils.get_llm_kwargs)


© Copyright 2025, LangChain Inc. 

