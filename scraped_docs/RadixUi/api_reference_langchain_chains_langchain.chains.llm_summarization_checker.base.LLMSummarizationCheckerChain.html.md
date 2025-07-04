---
url: https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html
scraped_at: 2025-05-25T18:10:21.247910
title: LLMSummarizationCheckerChain — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#main-content)
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
  * LLMSummarizationCheckerChain


# LLMSummarizationCheckerChain[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#llmsummarizationcheckerchain "Link to this heading") 

_class_ langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain[[source]](https://python.langchain.com/api_reference/_modules/langchain/chains/llm_summarization_checker/base.html#LLMSummarizationCheckerChain)[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain "Link to this definition")
    
Bases: [`Chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")
Deprecated since version 0.2.13: See LangGraph guides for a variety of self-reflection and corrective strategies for question-answering and other tasks: <https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/> It will not be removed until langchain==1.0.
Chain for question-answering with self-verification.
Example
```
fromlangchain_community.llmsimport OpenAI
fromlangchain.chainsimport LLMSummarizationCheckerChain
llm = OpenAI(temperature=0.0)
checker_chain = LLMSummarizationCheckerChain.from_llm(llm)

```
Copy to clipboard
Note
LLMSummarizationCheckerChain implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃
The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more. 

_param_ are_all_true_prompt _:[ PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")_ _= PromptTemplate(input_variables=['checked_assertions'], input_types={}, partial_variables={}, template='Below are some assertions that have been fact checked and are labeled as true or false.\n\nIf all of the assertions are true, return "True". If any of the assertions are false, return "False".\n\nHere are some examples:\n===\n\nChecked Assertions: """\n- The sky is red: False\n- Water is made of lava: False\n- The sun is a star: True\n"""\nResult: False\n\n===\n\nChecked Assertions: """\n- The sky is blue: True\n- Water is wet: True\n- The sun is a star: True\n"""\nResult: True\n\n===\n\nChecked Assertions: """\n- The sky is blue - True\n- Water is made of lava- False\n- The sun is a star - True\n"""\nResult: False\n\n===\n\nChecked Assertions:"""\n{checked_assertions}\n"""\nResult:')_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.are_all_true_prompt "Link to this definition")
    
[Deprecated] 

_param_ callback_manager _:[ BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.callback_manager "Link to this definition")
    
[DEPRECATED] Use callbacks instead. 

_param_ callbacks _: Callbacks_ _= None_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.callbacks "Link to this definition")
    
Optional list of callback handlers (or callback manager). Defaults to None. Callback handlers are called throughout the lifecycle of a call to a chain, starting with on_chain_start, ending with on_chain_end or on_chain_error. Each custom chain can optionally call additional callback methods, see Callback docs for full details. 

_param_ check_assertions_prompt _:[ PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")_ _= PromptTemplate(input_variables=['assertions'], input_types={}, partial_variables={}, template='You are an expert fact checker. You have been hired by a major news organization to fact check a very important story.\n\nHere is a bullet point list of facts:\n"""\n{assertions}\n"""\n\nFor each fact, determine whether it is true or false about the subject. If you are unable to determine whether the fact is true or false, output "Undetermined".\nIf the fact is false, explain why.\n\n')_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.check_assertions_prompt "Link to this definition")
    
[Deprecated] 

_param_ create_assertions_prompt _:[ PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")_ _= PromptTemplate(input_variables=['summary'], input_types={}, partial_variables={}, template='Given some text, extract a list of facts from the text.\n\nFormat your output as a bulleted list.\n\nText:\n"""\n{summary}\n"""\n\nFacts:')_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.create_assertions_prompt "Link to this definition")
    
[Deprecated] 

_param_ llm _:[ BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.llm "Link to this definition")
    
[Deprecated] LLM wrapper to use. 

_param_ max_checks _: int_ _= 2_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.max_checks "Link to this definition")
    
Maximum number of times to check the assertions. Default to double-checking. 

_param_ memory _: BaseMemory|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.memory "Link to this definition")
    
Optional memory object. Defaults to None. Memory is a class that gets called at the start and at the end of every chain. At the start, memory loads variables and passes them along in the chain. At the end, it saves any returned variables. There are many different types of memory - please see memory docs for the full catalog. 

_param_ metadata _: dict[str,Any]|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.metadata "Link to this definition")
    
Optional metadata associated with the chain. Defaults to None. This metadata will be associated with each call to this chain, and passed as arguments to the handlers defined in callbacks. You can use these to eg identify a specific instance of a chain with its use case. 

_param_ revised_summary_prompt _:[ PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")_ _= PromptTemplate(input_variables=['checked_assertions', 'summary'], input_types={}, partial_variables={}, template='Below are some assertions that have been fact checked and are labeled as true or false. If the answer is false, a suggestion is given for a correction.\n\nChecked Assertions:\n"""\n{checked_assertions}\n"""\n\nOriginal Summary:\n"""\n{summary}\n"""\n\nUsing these checked assertions, rewrite the original summary to be completely true.\n\nThe output should have the same structure and formatting as the original summary.\n\nSummary:')_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.revised_summary_prompt "Link to this definition")
    
[Deprecated] 

_param_ sequential_chain _:[ SequentialChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sequential.SequentialChain.html#langchain.chains.sequential.SequentialChain "langchain.chains.sequential.SequentialChain")_ _[Required]_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.sequential_chain "Link to this definition")


_param_ tags _: list[str]|None_ _= None_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.tags "Link to this definition")
    
Optional list of tags associated with the chain. Defaults to None. These tags will be associated with each call to this chain, and passed as arguments to the handlers defined in callbacks. You can use these to eg identify a specific instance of a chain with its use case. 

_param_ verbose _: bool_ _[Optional]_[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.verbose "Link to this definition")
    
Whether or not run in verbose mode. In verbose mode, some intermediate logs will be printed to the console. Defaults to the global verbose value, accessible via langchain.globals.get_verbose(). 

_classmethod_ from_llm( 
    _llm :[BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _create_assertions_prompt :[PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")=PromptTemplate(input_variables=['summary'], input_types={}, partial_variables={}, template='Given some text, extract a list of facts from the text.\n\nFormat your output as a bulleted list.\n\nText:\n"""\n{summary}\n"""\n\nFacts:')_,     _check_assertions_prompt :[PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")=PromptTemplate(input_variables=['assertions'], input_types={}, partial_variables={}, template='You are an expert fact checker. You have been hired by a major news organization to fact check a very important story.\n\nHere is a bullet point list of facts:\n"""\n{assertions}\n"""\n\nFor each fact, determine whether it is true or false about the subject. If you are unable to determine whether the fact is true or false, output "Undetermined".\nIf the fact is false, explain why.\n\n')_,     _revised_summary_prompt :[PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")=PromptTemplate(input_variables=['checked_assertions', 'summary'], input_types={}, partial_variables={}, template='Below are some assertions that have been fact checked and are labeled as true or false. If the answer is false, a suggestion is given for a correction.\n\nChecked Assertions:\n"""\n{checked_assertions}\n"""\n\nOriginal Summary:\n"""\n{summary}\n"""\n\nUsing these checked assertions, rewrite the original summary to be completely true.\n\nThe output should have the same structure and formatting as the original summary.\n\nSummary:')_,     _are_all_true_prompt :[PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")=PromptTemplate(input_variables=['checked_assertions'], input_types={}, partial_variables={}, template='Below are some assertions that have been fact checked and are labeled as true or false.\n\nIf all of the assertions are true, return "True". If any of the assertions are false, return "False".\n\nHere are some examples:\n===\n\nChecked Assertions: """\n- The sky is red: False\n- Water is made of lava: False\n- The sun is a star: True\n"""\nResult: False\n\n===\n\nChecked Assertions: """\n- The sky is blue: True\n- Water is wet: True\n- The sun is a star: True\n"""\nResult: True\n\n===\n\nChecked Assertions: """\n- The sky is blue - True\n- Water is made of lava- False\n- The sun is a star - True\n"""\nResult: False\n\n===\n\nChecked Assertions:"""\n{checked_assertions}\n"""\nResult:')_,     _verbose :bool=False_,     _** kwargs:Any_, ) → [LLMSummarizationCheckerChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain")[[source]](https://python.langchain.com/api_reference/_modules/langchain/chains/llm_summarization_checker/base.html#LLMSummarizationCheckerChain.from_llm)[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.from_llm "Link to this definition")      

Parameters:
    
  * **llm** ([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel"))
  * **create_assertions_prompt** ([_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate"))
  * **check_assertions_prompt** ([_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate"))
  * **revised_summary_prompt** ([_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate"))
  * **are_all_true_prompt** ([_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate"))
  * **verbose** (_bool_)
  * **kwargs** (_Any_)



Return type:
    
[_LLMSummarizationCheckerChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain") 

__call__( 
    _inputs :dict[str,Any]|Any_,     _return_only_outputs :bool=False_,     _callbacks :list[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")]|[BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")|None=None_,     _*_ ,     _tags :list[str]|None=None_,     _metadata :dict[str,Any]|None=None_,     _run_name :str|None=None_,     _include_run_info :bool=False_, ) → dict[str,Any][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.__call__ "Link to this definition")     
Deprecated since version 0.1.0: Use [`invoke()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.invoke "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.invoke") instead. It will not be removed until langchain==1.0.
Execute the chain. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__Any_ _]__|__Any_) – Dictionary of inputs, or single input if chain expects only one param. Should contain all inputs specified in Chain.input_keys except for inputs that will be set by the chain’s memory.
  * **return_only_outputs** (_bool_) – Whether to return only outputs in the response. If True, only new keys generated by this chain will be returned. If False, both input keys and new keys generated by this chain will be returned. Defaults to False.
  * **callbacks** (_list_ _[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_) – Callbacks to use for this chain run. These will be called in addition to callbacks passed to the chain during construction, but only these runtime callbacks will propagate to calls to other objects.
  * **tags** (_list_ _[__str_ _]__|__None_) – List of string tags to pass to all callbacks. These will be passed in addition to tags passed to the chain during construction, but only these runtime tags will propagate to calls to other objects.
  * **metadata** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Optional metadata associated with the chain. Defaults to None
  * **include_run_info** (_bool_) – Whether to include run info in the response. Defaults to False.
  * **run_name** (_str_ _|__None_)



Returns:
     

A dict of named outputs. Should contain all outputs specified in
    
Chain.output_keys. 

Return type:
    
dict[str, _Any_] 

_async_ abatch( 
    _inputs :list[Input]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|list[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")]|None=None_,     _*_ ,     _return_exceptions :bool=False_,     _** kwargs:Any|None_, ) → list[Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.abatch "Link to this definition")     
Default implementation runs ainvoke in parallel using asyncio.gather.
The default implementation of batch works well for IO bound runnables.
Subclasses should override this method if they can batch more efficiently; e.g., if the underlying Runnable uses an API which supports a batch mode. 

Parameters:
    
  * **inputs** (_list_ _[__Input_ _]_) – A list of inputs to the Runnable.
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__list_ _[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _]__|__None_) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details. Defaults to None.
  * **return_exceptions** (_bool_) – Whether to return exceptions instead of raising them. Defaults to False.
  * **kwargs** (_Any_ _|__None_) – Additional keyword arguments to pass to the Runnable.



Returns:
    
A list of outputs from the Runnable. 

Return type:
    
list[_Output_] 

_async_ abatch_as_completed( 
    _inputs :Sequence[Input]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|Sequence[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")]|None=None_,     _*_ ,     _return_exceptions :bool=False_,     _** kwargs:Any|None_, ) → AsyncIterator[tuple[int,Output|Exception]][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.abatch_as_completed "Link to this definition")     
Run ainvoke in parallel on a list of inputs.
Yields results as they complete. 

Parameters:
    
  * **inputs** (_Sequence_ _[__Input_ _]_) – A list of inputs to the Runnable.
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__Sequence_ _[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _]__|__None_) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details. Defaults to None. Defaults to None.
  * **return_exceptions** (_bool_) – Whether to return exceptions instead of raising them. Defaults to False.
  * **kwargs** (_Any_ _|__None_) – Additional keyword arguments to pass to the Runnable.



Yields:
    
A tuple of the index of the input and the output from the Runnable. 

Return type:
    
_AsyncIterator_[tuple[int, _Output_ | Exception]] 

_async_ acall( 
    _inputs :dict[str,Any]|Any_,     _return_only_outputs :bool=False_,     _callbacks :list[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")]|[BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")|None=None_,     _*_ ,     _tags :list[str]|None=None_,     _metadata :dict[str,Any]|None=None_,     _run_name :str|None=None_,     _include_run_info :bool=False_, ) → dict[str,Any][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.acall "Link to this definition")     
Deprecated since version 0.1.0: Use [`ainvoke()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.ainvoke "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.ainvoke") instead. It will not be removed until langchain==1.0.
Asynchronously execute the chain. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__Any_ _]__|__Any_) – Dictionary of inputs, or single input if chain expects only one param. Should contain all inputs specified in Chain.input_keys except for inputs that will be set by the chain’s memory.
  * **return_only_outputs** (_bool_) – Whether to return only outputs in the response. If True, only new keys generated by this chain will be returned. If False, both input keys and new keys generated by this chain will be returned. Defaults to False.
  * **callbacks** (_list_ _[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_) – Callbacks to use for this chain run. These will be called in addition to callbacks passed to the chain during construction, but only these runtime callbacks will propagate to calls to other objects.
  * **tags** (_list_ _[__str_ _]__|__None_) – List of string tags to pass to all callbacks. These will be passed in addition to tags passed to the chain during construction, but only these runtime tags will propagate to calls to other objects.
  * **metadata** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Optional metadata associated with the chain. Defaults to None
  * **include_run_info** (_bool_) – Whether to include run info in the response. Defaults to False.
  * **run_name** (_str_ _|__None_)



Returns:
     

A dict of named outputs. Should contain all outputs specified in
    
Chain.output_keys. 

Return type:
    
dict[str, _Any_] 

_async_ ainvoke( 
    _input :dict[str,Any]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any_, ) → dict[str,Any][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.ainvoke "Link to this definition")     
Default implementation of ainvoke, calls invoke from a thread.
The default implementation allows usage of async code even if the Runnable did not implement a native async version of invoke.
Subclasses should override this method if they can run asynchronously. 

Parameters:
    
  * **input** (_dict_ _[__str_ _,__Any_ _]_)
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_)
  * **kwargs** (_Any_)



Return type:
    
dict[str, _Any_] 

apply( 
    _input_list :list[dict[str,Any]]_,     _callbacks :list[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")]|[BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")|None=None_, ) → list[dict[str,str]][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.apply "Link to this definition")     
Deprecated since version 0.1.0: Use [`batch()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.batch "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.batch") instead. It will not be removed until langchain==1.0.
Call the chain on all inputs in the list. 

Parameters:
    
  * **input_list** (_list_ _[__dict_ _[__str_ _,__Any_ _]__]_)
  * **callbacks** (_list_ _[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_)



Return type:
    
list[dict[str, str]] 

_async_ aprep_inputs( 
    _inputs :dict[str,Any]|Any_, ) → dict[str,str][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.aprep_inputs "Link to this definition")     
Prepare chain inputs, including adding inputs from memory. 

Parameters:
    
**inputs** (_dict_ _[__str_ _,__Any_ _]__|__Any_) – Dictionary of raw inputs, or single input if chain expects only one param. Should contain all inputs specified in Chain.input_keys except for inputs that will be set by the chain’s memory. 

Returns:
    
A dictionary of all inputs, including those added by the chain’s memory. 

Return type:
    
dict[str, str] 

_async_ aprep_outputs( 
    _inputs :dict[str,str]_,     _outputs :dict[str,str]_,     _return_only_outputs :bool=False_, ) → dict[str,str][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.aprep_outputs "Link to this definition")     
Validate and prepare chain outputs, and save info about this run to memory. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__str_ _]_) – Dictionary of chain inputs, including any inputs added by chain memory.
  * **outputs** (_dict_ _[__str_ _,__str_ _]_) – Dictionary of initial chain outputs.
  * **return_only_outputs** (_bool_) – Whether to only return the chain outputs. If False, inputs are also added to the final outputs.



Returns:
    
A dict of the final chain outputs. 

Return type:
    
dict[str, str] 

_async_ arun( 
    _* args:Any_,     _callbacks :list[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")]|[BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")|None=None_,     _tags :list[str]|None=None_,     _metadata :dict[str,Any]|None=None_,     _** kwargs:Any_, ) → Any[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.arun "Link to this definition")     
Deprecated since version 0.1.0: Use [`ainvoke()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.ainvoke "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.ainvoke") instead. It will not be removed until langchain==1.0.
Convenience method for executing chain.
The main difference between this method and Chain.__call__ is that this method expects inputs to be passed directly in as positional arguments or keyword arguments, whereas Chain.__call__ expects a single input dictionary with all the inputs 

Parameters:
    
  * ***args** (_Any_) – If the chain expects a single input, it can be passed in as the sole positional argument.
  * **callbacks** (_list_ _[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_) – Callbacks to use for this chain run. These will be called in addition to callbacks passed to the chain during construction, but only these runtime callbacks will propagate to calls to other objects.
  * **tags** (_list_ _[__str_ _]__|__None_) – List of string tags to pass to all callbacks. These will be passed in addition to tags passed to the chain during construction, but only these runtime tags will propagate to calls to other objects.
  * ****kwargs** (_Any_) – If the chain expects multiple inputs, they can be passed in directly as keyword arguments.
  * **metadata** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * ****kwargs**



Returns:
    
The chain output. 

Return type:
    
_Any_
Example
```
# Suppose we have a single-input chain that takes a 'question' string:
await chain.arun("What's the temperature in Boise, Idaho?")
# -> "The temperature in Boise is..."
# Suppose we have a multi-input chain that takes a 'question' string
# and 'context' string:
question = "What's the temperature in Boise, Idaho?"
context = "Weather report for Boise, Idaho on 07/03/23..."
await chain.arun(question=question, context=context)
# -> "The temperature in Boise is..."

```
Copy to clipboard 

_async_ astream( 
    _input :Input_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any|None_, ) → AsyncIterator[Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.astream "Link to this definition")     
Default implementation of astream, which calls ainvoke.
Subclasses should override this method if they support streaming output. 

Parameters:
    
  * **input** (_Input_) – The input to the Runnable.
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_) – The config to use for the Runnable. Defaults to None.
  * **kwargs** (_Any_ _|__None_) – Additional keyword arguments to pass to the Runnable.



Yields:
    
The output of the Runnable. 

Return type:
    
_AsyncIterator_[_Output_] 

_async_ astream_events( 
    _input :Any_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _*_ ,     _version :Literal['v1','v2']='v2'_,     _include_names :Sequence[str]|None=None_,     _include_types :Sequence[str]|None=None_,     _include_tags :Sequence[str]|None=None_,     _exclude_names :Sequence[str]|None=None_,     _exclude_types :Sequence[str]|None=None_,     _exclude_tags :Sequence[str]|None=None_,     _** kwargs:Any_, ) → AsyncIterator[StreamEvent][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.astream_events "Link to this definition")     
Generate a stream of events.
Use to create an iterator over StreamEvents that provide real-time information about the progress of the Runnable, including StreamEvents from intermediate results.
A StreamEvent is a dictionary with the following schema:
  * 

`event`: **str** - Event names are of the
    
format: on_[runnable_type]_(start|stream|end).
  * `name`: **str** - The name of the Runnable that generated the event.
  * 

`run_id`: **str** - randomly generated ID associated with the given execution of
    
the Runnable that emitted the event. A child Runnable that gets invoked as part of the execution of a parent Runnable is assigned its own unique ID.
  * 

`parent_ids`: **list[str]** - The IDs of the parent runnables that
    
generated the event. The root Runnable will have an empty list. The order of the parent IDs is from the root to the immediate parent. Only available for v2 version of the API. The v1 version of the API will return an empty list.
  * 

`tags`: **Optional[list[str]]** - The tags of the Runnable that generated
    
the event.
  * 

`metadata`: **Optional[dict[str, Any]]** - The metadata of the Runnable
    
that generated the event.
  * `data`: **dict[str, Any]**


Below is a table that illustrates some events that might be emitted by various chains. Metadata fields have been omitted from the table for brevity. Chain definitions have been included after the table.
**ATTENTION** This reference table is for the V2 version of the schema.
event | name | chunk | input | output  
---|---|---|---|---  
on_chat_model_start | [model name] |  | {“messages”: [[SystemMessage, HumanMessage]]} |   
on_chat_model_stream | [model name] | AIMessageChunk(content=”hello”) |  |   
on_chat_model_end | [model name] |  | {“messages”: [[SystemMessage, HumanMessage]]} | AIMessageChunk(content=”hello world”)  
on_llm_start | [model name] |  | {‘input’: ‘hello’} |   
on_llm_stream | [model name] | ‘Hello’ |  |   
on_llm_end | [model name] |  | ‘Hello human!’ |   
on_chain_start | format_docs |  |  |   
on_chain_stream | format_docs | “hello world!, goodbye world!” |  |   
on_chain_end | format_docs |  | [Document(…)] | “hello world!, goodbye world!”  
on_tool_start | some_tool |  | {“x”: 1, “y”: “2”} |   
on_tool_end | some_tool |  |  | {“x”: 1, “y”: “2”}  
on_retriever_start | [retriever name] |  | {“query”: “hello”} |   
on_retriever_end | [retriever name] |  | {“query”: “hello”} | [Document(…), ..]  
on_prompt_start | [template_name] |  | {“question”: “hello”} |   
on_prompt_end | [template_name] |  | {“question”: “hello”} | ChatPromptValue(messages: [SystemMessage, …])  
In addition to the standard events, users can also dispatch custom events (see example below).
Custom events will be only be surfaced with in the v2 version of the API!
A custom event has following format:
Attribute | Type | Description  
---|---|---  
name | str | A user defined name for the event.  
data | Any | The data associated with the event. This can be anything, though we suggest making it JSON serializable.  
Here are declarations associated with the standard events shown above:
format_docs:
```
defformat_docs(docs: list[Document]) -> str:
'''Format the docs.'''
  return ", ".join([doc.page_content for doc in docs])
format_docs = RunnableLambda(format_docs)

```
Copy to clipboard
some_tool:
```
@tool
defsome_tool(x: int, y: str) -> dict:
'''Some_tool.'''
  return {"x": x, "y": y}

```
Copy to clipboard
prompt:
```
template = ChatPromptTemplate.from_messages(
  [("system", "You are Cat Agent 007"), ("human", "{question}")]
).with_config({"run_name": "my_template", "tags": ["my_template"]})

```
Copy to clipboard
Example:
```
fromlangchain_core.runnablesimport RunnableLambda
async defreverse(s: str) -> str:
  return s[::-1]
chain = RunnableLambda(func=reverse)
events = [
  event async for event in chain.astream_events("hello", version="v2")
]
# will produce the following events (run_id, and parent_ids
# has been omitted for brevity):
[
  {
    "data": {"input": "hello"},
    "event": "on_chain_start",
    "metadata": {},
    "name": "reverse",
    "tags": [],
  },
  {
    "data": {"chunk": "olleh"},
    "event": "on_chain_stream",
    "metadata": {},
    "name": "reverse",
    "tags": [],
  },
  {
    "data": {"output": "olleh"},
    "event": "on_chain_end",
    "metadata": {},
    "name": "reverse",
    "tags": [],
  },
]

```
Copy to clipboard
Example: Dispatch Custom Event
```
fromlangchain_core.callbacks.managerimport (
  adispatch_custom_event,
)
fromlangchain_core.runnablesimport RunnableLambda, RunnableConfig
importasyncio

async defslow_thing(some_input: str, config: RunnableConfig) -> str:
"""Do something that takes a long time."""
  await asyncio.sleep(1) # Placeholder for some slow operation
  await adispatch_custom_event(
    "progress_event",
    {"message": "Finished step 1 of 3"},
    config=config # Must be included for python < 3.10
  )
  await asyncio.sleep(1) # Placeholder for some slow operation
  await adispatch_custom_event(
    "progress_event",
    {"message": "Finished step 2 of 3"},
    config=config # Must be included for python < 3.10
  )
  await asyncio.sleep(1) # Placeholder for some slow operation
  return "Done"
slow_thing = RunnableLambda(slow_thing)
async for event in slow_thing.astream_events("some_input", version="v2"):
  print(event)

```
Copy to clipboard 

Parameters:
    
  * **input** (_Any_) – The input to the Runnable.
  * **config** (_Optional_ _[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _]_) – The config to use for the Runnable.
  * **version** (_Literal_ _[__'v1'__,__'v2'__]_) – The version of the schema to use either v2 or v1. Users should use v2. v1 is for backwards compatibility and will be deprecated in 0.4.0. No default will be assigned until the API is stabilized. custom events will only be surfaced in v2.
  * **include_names** (_Optional_ _[__Sequence_ _[__str_ _]__]_) – Only include events from runnables with matching names.
  * **include_types** (_Optional_ _[__Sequence_ _[__str_ _]__]_) – Only include events from runnables with matching types.
  * **include_tags** (_Optional_ _[__Sequence_ _[__str_ _]__]_) – Only include events from runnables with matching tags.
  * **exclude_names** (_Optional_ _[__Sequence_ _[__str_ _]__]_) – Exclude events from runnables with matching names.
  * **exclude_types** (_Optional_ _[__Sequence_ _[__str_ _]__]_) – Exclude events from runnables with matching types.
  * **exclude_tags** (_Optional_ _[__Sequence_ _[__str_ _]__]_) – Exclude events from runnables with matching tags.
  * **kwargs** (_Any_) – Additional keyword arguments to pass to the Runnable. These will be passed to astream_log as this implementation of astream_events is built on top of astream_log.



Yields:
    
An async stream of StreamEvents. 

Raises:
    
**NotImplementedError** – If the version is not v1 or v2. 

Return type:
    
AsyncIterator[StreamEvent] 

batch( 
    _inputs :list[Input]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|list[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")]|None=None_,     _*_ ,     _return_exceptions :bool=False_,     _** kwargs:Any|None_, ) → list[Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.batch "Link to this definition")     
Default implementation runs invoke in parallel using a thread pool executor.
The default implementation of batch works well for IO bound runnables.
Subclasses should override this method if they can batch more efficiently; e.g., if the underlying Runnable uses an API which supports a batch mode. 

Parameters:
    
  * **inputs** (_list_ _[__Input_ _]_)
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__list_ _[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _]__|__None_)
  * **return_exceptions** (_bool_)
  * **kwargs** (_Any_ _|__None_)



Return type:
    
list[_Output_] 

batch_as_completed( 
    _inputs :Sequence[Input]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|Sequence[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")]|None=None_,     _*_ ,     _return_exceptions :bool=False_,     _** kwargs:Any|None_, ) → Iterator[tuple[int,Output|Exception]][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.batch_as_completed "Link to this definition")     
Run invoke in parallel on a list of inputs.
Yields results as they complete. 

Parameters:
    
  * **inputs** (_Sequence_ _[__Input_ _]_)
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__Sequence_ _[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _]__|__None_)
  * **return_exceptions** (_bool_)
  * **kwargs** (_Any_ _|__None_)



Return type:
    
_Iterator_[tuple[int, _Output_ | Exception]] 

bind( 
    _** kwargs:Any_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.bind "Link to this definition")     
Bind arguments to a Runnable, returning a new Runnable.
Useful when a Runnable in a chain requires an argument that is not in the output of the previous Runnable or included in the user input. 

Parameters:
    
**kwargs** (_Any_) – The arguments to bind to the Runnable. 

Returns:
    
A new Runnable with the arguments bound. 

Return type:
    
[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[_Input_ , _Output_]
Example:
```
fromlangchain_community.chat_modelsimport ChatOllama
fromlangchain_core.output_parsersimport StrOutputParser
llm = ChatOllama(model='llama2')
# Without bind.
chain = (
  llm
  | StrOutputParser()
)
chain.invoke("Repeat quoted words exactly: 'One two three four five.'")
# Output is 'One two three four five.'
# With bind.
chain = (
  llm.bind(stop=["three"])
  | StrOutputParser()
)
chain.invoke("Repeat quoted words exactly: 'One two three four five.'")
# Output is 'One two'

```
Copy to clipboard 

configurable_alternatives( 
    _which :[ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")_,     _*_ ,     _default_key :str='default'_,     _prefix_keys :bool=False_,     _** kwargs:[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output]|Callable[[],[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output]]_, ) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.configurable_alternatives "Link to this definition")     
Configure alternatives for Runnables that can be set at runtime. 

Parameters:
    
  * **which** ([_ConfigurableField_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")) – The ConfigurableField instance that will be used to select the alternative.
  * **default_key** (_str_) – The default key to use if no alternative is selected. Defaults to “default”.
  * **prefix_keys** (_bool_) – Whether to prefix the keys with the ConfigurableField id. Defaults to False.
  * ****kwargs** ([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _[__Input_ _,__Output_ _]__|__Callable_ _[__[__]__,_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _[__Input_ _,__Output_ _]__]_) – A dictionary of keys to Runnable instances or callables that return Runnable instances.



Returns:
    
A new Runnable with the alternatives configured. 

Return type:
    
[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")
```
fromlangchain_anthropicimport ChatAnthropic
fromlangchain_core.runnables.utilsimport ConfigurableField
fromlangchain_openaiimport ChatOpenAI
model = ChatAnthropic(
  model_name="claude-3-sonnet-20240229"
).configurable_alternatives(
  ConfigurableField(id="llm"),
  default_key="anthropic",
  openai=ChatOpenAI()
)
# uses the default model ChatAnthropic
print(model.invoke("which organization created you?").content)
# uses ChatOpenAI
print(
  model.with_config(
    configurable={"llm": "openai"}
  ).invoke("which organization created you?").content
)

```
Copy to clipboard 

configurable_fields( 
    _** kwargs:[ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")|[ConfigurableFieldSingleOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption")|[ConfigurableFieldMultiOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")_, ) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.configurable_fields "Link to this definition")     
Configure particular Runnable fields at runtime. 

Parameters:
    
****kwargs** ([_ConfigurableField_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField") _|_[_ConfigurableFieldSingleOption_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption") _|_[_ConfigurableFieldMultiOption_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")) – A dictionary of ConfigurableField instances to configure. 

Returns:
    
A new Runnable with the fields configured. 

Return type:
    
[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")
```
fromlangchain_core.runnablesimport ConfigurableField
fromlangchain_openaiimport ChatOpenAI
model = ChatOpenAI(max_tokens=20).configurable_fields(
  max_tokens=ConfigurableField(
    id="output_token_number",
    name="Max tokens in the output",
    description="The maximum number of tokens in the output",
  )
)
# max_tokens = 20
print(
  "max_tokens_20: ",
  model.invoke("tell me something about chess").content
)
# max_tokens = 200
print("max_tokens_200: ", model.with_config(
  configurable={"output_token_number": 200}
  ).invoke("tell me something about chess").content
)

```
Copy to clipboard 

invoke( 
    _input :dict[str,Any]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any_, ) → dict[str,Any][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.invoke "Link to this definition")     
Transform a single input into an output. 

Parameters:
    
  * **input** (_dict_ _[__str_ _,__Any_ _]_) – The input to the Runnable.
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details.
  * **kwargs** (_Any_)



Returns:
    
The output of the Runnable. 

Return type:
    
dict[str, _Any_] 

prep_inputs( 
    _inputs :dict[str,Any]|Any_, ) → dict[str,str][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.prep_inputs "Link to this definition")     
Prepare chain inputs, including adding inputs from memory. 

Parameters:
    
**inputs** (_dict_ _[__str_ _,__Any_ _]__|__Any_) – Dictionary of raw inputs, or single input if chain expects only one param. Should contain all inputs specified in Chain.input_keys except for inputs that will be set by the chain’s memory. 

Returns:
    
A dictionary of all inputs, including those added by the chain’s memory. 

Return type:
    
dict[str, str] 

prep_outputs( 
    _inputs :dict[str,str]_,     _outputs :dict[str,str]_,     _return_only_outputs :bool=False_, ) → dict[str,str][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.prep_outputs "Link to this definition")     
Validate and prepare chain outputs, and save info about this run to memory. 

Parameters:
    
  * **inputs** (_dict_ _[__str_ _,__str_ _]_) – Dictionary of chain inputs, including any inputs added by chain memory.
  * **outputs** (_dict_ _[__str_ _,__str_ _]_) – Dictionary of initial chain outputs.
  * **return_only_outputs** (_bool_) – Whether to only return the chain outputs. If False, inputs are also added to the final outputs.



Returns:
    
A dict of the final chain outputs. 

Return type:
    
dict[str, str] 

run( 
    _* args:Any_,     _callbacks :list[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")]|[BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")|None=None_,     _tags :list[str]|None=None_,     _metadata :dict[str,Any]|None=None_,     _** kwargs:Any_, ) → Any[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.run "Link to this definition")     
Deprecated since version 0.1.0: Use [`invoke()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.invoke "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.invoke") instead. It will not be removed until langchain==1.0.
Convenience method for executing chain.
The main difference between this method and Chain.__call__ is that this method expects inputs to be passed directly in as positional arguments or keyword arguments, whereas Chain.__call__ expects a single input dictionary with all the inputs 

Parameters:
    
  * ***args** (_Any_) – If the chain expects a single input, it can be passed in as the sole positional argument.
  * **callbacks** (_list_ _[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_) – Callbacks to use for this chain run. These will be called in addition to callbacks passed to the chain during construction, but only these runtime callbacks will propagate to calls to other objects.
  * **tags** (_list_ _[__str_ _]__|__None_) – List of string tags to pass to all callbacks. These will be passed in addition to tags passed to the chain during construction, but only these runtime tags will propagate to calls to other objects.
  * ****kwargs** (_Any_) – If the chain expects multiple inputs, they can be passed in directly as keyword arguments.
  * **metadata** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * ****kwargs**



Returns:
    
The chain output. 

Return type:
    
_Any_
Example
```
# Suppose we have a single-input chain that takes a 'question' string:
chain.run("What's the temperature in Boise, Idaho?")
# -> "The temperature in Boise is..."
# Suppose we have a multi-input chain that takes a 'question' string
# and 'context' string:
question = "What's the temperature in Boise, Idaho?"
context = "Weather report for Boise, Idaho on 07/03/23..."
chain.run(question=question, context=context)
# -> "The temperature in Boise is..."

```
Copy to clipboard 

save( 
    _file_path :Path|str_, ) → None[#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.save "Link to this definition")     
Save the chain. 

Expects Chain._chain_type property to be implemented and for memory to be
    
null. 

Parameters:
    
**file_path** (_Path_ _|__str_) – Path to file to save the chain to. 

Return type:
    
None
Example
```
chain.save(file_path="path/chain.yaml")

```
Copy to clipboard 

stream( 
    _input :Input_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any|None_, ) → Iterator[Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.stream "Link to this definition")     
Default implementation of stream, which calls invoke.
Subclasses should override this method if they support streaming output. 

Parameters:
    
  * **input** (_Input_) – The input to the Runnable.
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_) – The config to use for the Runnable. Defaults to None.
  * **kwargs** (_Any_ _|__None_) – Additional keyword arguments to pass to the Runnable.



Yields:
    
The output of the Runnable. 

Return type:
    
_Iterator_[_Output_] 

with_alisteners( 
    _*_ ,     _on_start :AsyncListener|None=None_,     _on_end :AsyncListener|None=None_,     _on_error :AsyncListener|None=None_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_alisteners "Link to this definition")     
Bind async lifecycle listeners to a Runnable, returning a new Runnable.
on_start: Asynchronously called before the Runnable starts running. on_end: Asynchronously called after the Runnable finishes running. on_error: Asynchronously called if the Runnable throws an error.
The Run object contains information about the run, including its id, type, input, output, error, start_time, end_time, and any tags or metadata added to the run. 

Parameters:
    
  * **on_start** (_Optional_ _[__AsyncListener_ _]_) – Asynchronously called before the Runnable starts running. Defaults to None.
  * **on_end** (_Optional_ _[__AsyncListener_ _]_) – Asynchronously called after the Runnable finishes running. Defaults to None.
  * **on_error** (_Optional_ _[__AsyncListener_ _]_) – Asynchronously called if the Runnable throws an error. Defaults to None.



Returns:
    
A new Runnable with the listeners bound. 

Return type:
    
[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input, Output]
Example:
```
fromlangchain_core.runnablesimport RunnableLambda, Runnable
fromdatetimeimport datetime, timezone
importtime
importasyncio
defformat_t(timestamp: float) -> str:
  return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()
async deftest_runnable(time_to_sleep : int):
  print(f"Runnable[{time_to_sleep}s]: starts at {format_t(time.time())}")
  await asyncio.sleep(time_to_sleep)
  print(f"Runnable[{time_to_sleep}s]: ends at {format_t(time.time())}")
async deffn_start(run_obj : Runnable):
  print(f"on start callback starts at {format_t(time.time())}")
  await asyncio.sleep(3)
  print(f"on start callback ends at {format_t(time.time())}")
async deffn_end(run_obj : Runnable):
  print(f"on end callback starts at {format_t(time.time())}")
  await asyncio.sleep(2)
  print(f"on end callback ends at {format_t(time.time())}")
runnable = RunnableLambda(test_runnable).with_alisteners(
  on_start=fn_start,
  on_end=fn_end
)
async defconcurrent_runs():
  await asyncio.gather(runnable.ainvoke(2), runnable.ainvoke(3))
asyncio.run(concurrent_runs())
Result:
on start callback starts at 2025-03-01T07:05:22.875378+00:00
on start callback starts at 2025-03-01T07:05:22.875495+00:00
on start callback ends at 2025-03-01T07:05:25.878862+00:00
on start callback ends at 2025-03-01T07:05:25.878947+00:00
Runnable[2s]: starts at 2025-03-01T07:05:25.879392+00:00
Runnable[3s]: starts at 2025-03-01T07:05:25.879804+00:00
Runnable[2s]: ends at 2025-03-01T07:05:27.881998+00:00
on end callback starts at 2025-03-01T07:05:27.882360+00:00
Runnable[3s]: ends at 2025-03-01T07:05:28.881737+00:00
on end callback starts at 2025-03-01T07:05:28.882428+00:00
on end callback ends at 2025-03-01T07:05:29.883893+00:00
on end callback ends at 2025-03-01T07:05:30.884831+00:00

```
Copy to clipboard 

with_config( 
    _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_config "Link to this definition")     
Bind config to a Runnable, returning a new Runnable. 

Parameters:
    
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_) – The config to bind to the Runnable.
  * **kwargs** (_Any_) – Additional keyword arguments to pass to the Runnable.



Returns:
    
A new Runnable with the config bound. 

Return type:
    
[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[_Input_ , _Output_] 

with_fallbacks(_fallbacks: Sequence[Runnable[Input, Output]], *, exceptions_to_handle: tuple[type[BaseException], ...] = (<class 'Exception'>,), exception_key: Optional[str] = None_) → RunnableWithFallbacksT[Input,Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_fallbacks "Link to this definition")
    
Add fallbacks to a Runnable, returning a new Runnable.
The new Runnable will try the original Runnable, and then each fallback in order, upon failures. 

Parameters:
    
  * **fallbacks** (_Sequence_ _[_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _[__Input_ _,__Output_ _]__]_) – A sequence of runnables to try if the original Runnable fails.
  * **exceptions_to_handle** (_tuple_ _[__type_ _[__BaseException_ _]__,__...__]_) – A tuple of exception types to handle. Defaults to (Exception,).
  * **exception_key** (_Optional_ _[__str_ _]_) – If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If None, exceptions will not be passed to fallbacks. If used, the base Runnable and its fallbacks must accept a dictionary as input. Defaults to None.



Returns:
    
A new Runnable that will try the original Runnable, and then each fallback in order, upon failures. 

Return type:
    
RunnableWithFallbacksT[Input, Output]
Example
```
fromtypingimport Iterator
fromlangchain_core.runnablesimport RunnableGenerator

def_generate_immediate_error(input: Iterator) -> Iterator[str]:
  raise ValueError()
  yield ""

def_generate(input: Iterator) -> Iterator[str]:
  yield from "foo bar"

runnable = RunnableGenerator(_generate_immediate_error).with_fallbacks(
  [RunnableGenerator(_generate)]
  )
print(''.join(runnable.stream({}))) #foo bar

```
Copy to clipboard 

Parameters:
    
  * **fallbacks** (_Sequence_ _[_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _[__Input_ _,__Output_ _]__]_) – A sequence of runnables to try if the original Runnable fails.
  * **exceptions_to_handle** (_tuple_ _[__type_ _[__BaseException_ _]__,__...__]_) – A tuple of exception types to handle.
  * **exception_key** (_Optional_ _[__str_ _]_) – If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If None, exceptions will not be passed to fallbacks. If used, the base Runnable and its fallbacks must accept a dictionary as input.



Returns:
    
A new Runnable that will try the original Runnable, and then each fallback in order, upon failures. 

Return type:
    
RunnableWithFallbacksT[Input, Output] 

with_listeners( 
    _*_ ,     _on_start :Callable[[Run],None]|Callable[[Run,[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")],None]|None=None_,     _on_end :Callable[[Run],None]|Callable[[Run,[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")],None]|None=None_,     _on_error :Callable[[Run],None]|Callable[[Run,[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")],None]|None=None_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_listeners "Link to this definition")     
Bind lifecycle listeners to a Runnable, returning a new Runnable.
on_start: Called before the Runnable starts running, with the Run object. on_end: Called after the Runnable finishes running, with the Run object. on_error: Called if the Runnable throws an error, with the Run object.
The Run object contains information about the run, including its id, type, input, output, error, start_time, end_time, and any tags or metadata added to the run. 

Parameters:
    
  * **on_start** (_Optional_ _[__Union_ _[__Callable_ _[__[__Run_ _]__,__None_ _]__,__Callable_ _[__[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _]__,__None_ _]__]__]_) – Called before the Runnable starts running. Defaults to None.
  * **on_end** (_Optional_ _[__Union_ _[__Callable_ _[__[__Run_ _]__,__None_ _]__,__Callable_ _[__[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _]__,__None_ _]__]__]_) – Called after the Runnable finishes running. Defaults to None.
  * **on_error** (_Optional_ _[__Union_ _[__Callable_ _[__[__Run_ _]__,__None_ _]__,__Callable_ _[__[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _]__,__None_ _]__]__]_) – Called if the Runnable throws an error. Defaults to None.



Returns:
    
A new Runnable with the listeners bound. 

Return type:
    
[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input, Output]
Example:
```
fromlangchain_core.runnablesimport RunnableLambda
fromlangchain_core.tracers.schemasimport Run
importtime
deftest_runnable(time_to_sleep : int):
  time.sleep(time_to_sleep)
deffn_start(run_obj: Run):
  print("start_time:", run_obj.start_time)
deffn_end(run_obj: Run):
  print("end_time:", run_obj.end_time)
chain = RunnableLambda(test_runnable).with_listeners(
  on_start=fn_start,
  on_end=fn_end
)
chain.invoke(2)

```
Copy to clipboard 

with_retry(_*, retry_if_exception_type: tuple[type[BaseException], ...] = (<class 'Exception'>,), wait_exponential_jitter: bool = True, exponential_jitter_params: Optional[ExponentialJitterParams] = None, stop_after_attempt: int = 3_) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_retry "Link to this definition")
    
Create a new Runnable that retries the original Runnable on exceptions. 

Parameters:
    
  * **retry_if_exception_type** (_tuple_ _[__type_ _[__BaseException_ _]__,__...__]_) – A tuple of exception types to retry on. Defaults to (Exception,).
  * **wait_exponential_jitter** (_bool_) – Whether to add jitter to the wait time between retries. Defaults to True.
  * **stop_after_attempt** (_int_) – The maximum number of attempts to make before giving up. Defaults to 3.
  * **exponential_jitter_params** (_Optional_ _[_[_ExponentialJitterParams_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.retry.ExponentialJitterParams.html#langchain_core.runnables.retry.ExponentialJitterParams "langchain_core.runnables.retry.ExponentialJitterParams") _]_) – Parameters for `tenacity.wait_exponential_jitter`. Namely: `initial`, `max`, `exp_base`, and `jitter` (all float values).



Returns:
    
A new Runnable that retries the original Runnable on exceptions. 

Return type:
    
[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input, Output]
Example:
```
fromlangchain_core.runnablesimport RunnableLambda
count = 0

def_lambda(x: int) -> None:
  global count
  count = count + 1
  if x == 1:
    raise ValueError("x is 1")
  else:
     pass

runnable = RunnableLambda(_lambda)
try:
  runnable.with_retry(
    stop_after_attempt=2,
    retry_if_exception_type=(ValueError,),
  ).invoke(1)
except ValueError:
  pass
assert (count == 2)

```
Copy to clipboard 

with_types( 
    _*_ ,     _input_type :type[Input]|None=None_,     _output_type :type[Output]|None=None_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_types "Link to this definition")     
Bind input and output types to a Runnable, returning a new Runnable. 

Parameters:
    
  * **input_type** (_type_ _[__Input_ _]__|__None_) – The input type to bind to the Runnable. Defaults to None.
  * **output_type** (_type_ _[__Output_ _]__|__None_) – The output type to bind to the Runnable. Defaults to None.



Returns:
    
A new Runnable with the types bound. 

Return type:
    
[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[_Input_ , _Output_]
On this page 
  * [`LLMSummarizationCheckerChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain)
    * [`are_all_true_prompt`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.are_all_true_prompt)
    * [`callback_manager`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.callback_manager)
    * [`callbacks`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.callbacks)
    * [`check_assertions_prompt`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.check_assertions_prompt)
    * [`create_assertions_prompt`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.create_assertions_prompt)
    * [`llm`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.llm)
    * [`max_checks`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.max_checks)
    * [`memory`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.memory)
    * [`metadata`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.metadata)
    * [`revised_summary_prompt`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.revised_summary_prompt)
    * [`sequential_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.sequential_chain)
    * [`tags`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.tags)
    * [`verbose`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.verbose)
    * [`from_llm()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.from_llm)
    * [`__call__()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.__call__)
    * [`abatch()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.abatch)
    * [`abatch_as_completed()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.abatch_as_completed)
    * [`acall()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.acall)
    * [`ainvoke()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.ainvoke)
    * [`apply()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.apply)
    * [`aprep_inputs()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.aprep_inputs)
    * [`aprep_outputs()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.aprep_outputs)
    * [`arun()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.arun)
    * [`astream()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.astream)
    * [`astream_events()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.astream_events)
    * [`batch()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.batch)
    * [`batch_as_completed()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.batch_as_completed)
    * [`bind()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.bind)
    * [`configurable_alternatives()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.configurable_alternatives)
    * [`configurable_fields()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.configurable_fields)
    * [`invoke()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.invoke)
    * [`prep_inputs()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.prep_inputs)
    * [`prep_outputs()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.prep_outputs)
    * [`run()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.run)
    * [`save()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.save)
    * [`stream()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.stream)
    * [`with_alisteners()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_alisteners)
    * [`with_config()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_config)
    * [`with_fallbacks()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_fallbacks)
    * [`with_listeners()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_listeners)
    * [`with_retry()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_retry)
    * [`with_types()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.with_types)


© Copyright 2025, LangChain Inc. 
  *[*]: Keyword-only parameters separator (PEP 3102)

