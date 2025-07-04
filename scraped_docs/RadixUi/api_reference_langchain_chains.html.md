---
url: https://python.langchain.com/api_reference/langchain/chains.html
scraped_at: 2025-05-25T17:55:38.608368
title: chains — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/langchain/chains.html#main-content)
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
  * `chains`


# `chains`[#](https://python.langchain.com/api_reference/langchain/chains.html#module-langchain.chains "Link to this heading")
**Chains** are easily reusable components linked together.
Chains encode a sequence of calls to components like models, document retrievers, other Chains, etc., and provide a simple interface to this sequence.
The Chain interface makes it easy to create apps that are:
>   * **Stateful:** add Memory to any Chain to give it state,
>   * **Observable:** pass Callbacks to a Chain to execute additional functionality, like logging, outside the main sequence of component calls,
>   * **Composable:** combine Chains with other components, including other Chains.
> 

**Class hierarchy:**
```
Chain --> <name>Chain # Examples: LLMChain, MapReduceChain, RouterChain

```
Copy to clipboard
**Classes**
[`chains.base.Chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") | Abstract base class for creating structured sequences of calls to components.  
---|---  
[`chains.combine_documents.base.BaseCombineDocumentsChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.BaseCombineDocumentsChain.html#langchain.chains.combine_documents.base.BaseCombineDocumentsChain "langchain.chains.combine_documents.base.BaseCombineDocumentsChain") | Base interface for chains combining documents.  
[`chains.combine_documents.reduce.AsyncCombineDocsProtocol`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol.html#langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol "langchain.chains.combine_documents.reduce.AsyncCombineDocsProtocol")(...) | Interface for the combine_docs method.  
[`chains.combine_documents.reduce.CombineDocsProtocol`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.CombineDocsProtocol.html#langchain.chains.combine_documents.reduce.CombineDocsProtocol "langchain.chains.combine_documents.reduce.CombineDocsProtocol")(...) | Interface for the combine_docs method.  
[`chains.constitutional_ai.models.ConstitutionalPrinciple`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.models.ConstitutionalPrinciple.html#langchain.chains.constitutional_ai.models.ConstitutionalPrinciple "langchain.chains.constitutional_ai.models.ConstitutionalPrinciple") | Class for a constitutional principle.  
[`chains.conversational_retrieval.base.BaseConversationalRetrievalChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.BaseConversationalRetrievalChain.html#langchain.chains.conversational_retrieval.base.BaseConversationalRetrievalChain "langchain.chains.conversational_retrieval.base.BaseConversationalRetrievalChain") | Chain for chatting with an index.  
[`chains.conversational_retrieval.base.ChatVectorDBChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.ChatVectorDBChain.html#langchain.chains.conversational_retrieval.base.ChatVectorDBChain "langchain.chains.conversational_retrieval.base.ChatVectorDBChain") | Chain for chatting with a vector database.  
[`chains.conversational_retrieval.base.InputType`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.InputType.html#langchain.chains.conversational_retrieval.base.InputType "langchain.chains.conversational_retrieval.base.InputType") | Input type for ConversationalRetrievalChain.  
[`chains.elasticsearch_database.base.ElasticsearchDatabaseChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.elasticsearch_database.base.ElasticsearchDatabaseChain.html#langchain.chains.elasticsearch_database.base.ElasticsearchDatabaseChain "langchain.chains.elasticsearch_database.base.ElasticsearchDatabaseChain") | Chain for interacting with Elasticsearch Database.  
[`chains.flare.base.FlareChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.flare.base.FlareChain.html#langchain.chains.flare.base.FlareChain "langchain.chains.flare.base.FlareChain") | Chain that combines a retriever, a question generator, and a response generator.  
[`chains.flare.base.QuestionGeneratorChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.flare.base.QuestionGeneratorChain.html#langchain.chains.flare.base.QuestionGeneratorChain "langchain.chains.flare.base.QuestionGeneratorChain") | Chain that generates questions from uncertain spans.  
[`chains.flare.prompts.FinishedOutputParser`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.flare.prompts.FinishedOutputParser.html#langchain.chains.flare.prompts.FinishedOutputParser "langchain.chains.flare.prompts.FinishedOutputParser") | Output parser that checks if the output is finished.  
[`chains.hyde.base.HypotheticalDocumentEmbedder`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.hyde.base.HypotheticalDocumentEmbedder.html#langchain.chains.hyde.base.HypotheticalDocumentEmbedder "langchain.chains.hyde.base.HypotheticalDocumentEmbedder") | Generate hypothetical document for query, and then embed that.  
[`chains.moderation.OpenAIModerationChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.moderation.OpenAIModerationChain.html#langchain.chains.moderation.OpenAIModerationChain "langchain.chains.moderation.OpenAIModerationChain") | Pass input through a moderation endpoint.  
[`chains.natbot.crawler.Crawler`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.natbot.crawler.Crawler.html#langchain.chains.natbot.crawler.Crawler "langchain.chains.natbot.crawler.Crawler")() | A crawler for web pages.  
[`chains.natbot.crawler.ElementInViewPort`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.natbot.crawler.ElementInViewPort.html#langchain.chains.natbot.crawler.ElementInViewPort "langchain.chains.natbot.crawler.ElementInViewPort") | A typed dictionary containing information about elements in the viewport.  
[`chains.openai_functions.citation_fuzzy_match.FactWithEvidence`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.FactWithEvidence.html#langchain.chains.openai_functions.citation_fuzzy_match.FactWithEvidence "langchain.chains.openai_functions.citation_fuzzy_match.FactWithEvidence") | Class representing a single statement.  
[`chains.openai_functions.citation_fuzzy_match.QuestionAnswer`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.QuestionAnswer.html#langchain.chains.openai_functions.citation_fuzzy_match.QuestionAnswer "langchain.chains.openai_functions.citation_fuzzy_match.QuestionAnswer") | A question and its answer as a list of facts each one should have a source.  
[`chains.openai_functions.openapi.SimpleRequestChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.openapi.SimpleRequestChain.html#langchain.chains.openai_functions.openapi.SimpleRequestChain "langchain.chains.openai_functions.openapi.SimpleRequestChain") | Chain for making a simple request to an API endpoint.  
[`chains.openai_functions.qa_with_structure.AnswerWithSources`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.AnswerWithSources.html#langchain.chains.openai_functions.qa_with_structure.AnswerWithSources "langchain.chains.openai_functions.qa_with_structure.AnswerWithSources") | An answer to the question, with sources.  
[`chains.prompt_selector.BasePromptSelector`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.BasePromptSelector.html#langchain.chains.prompt_selector.BasePromptSelector "langchain.chains.prompt_selector.BasePromptSelector") | Base class for prompt selectors.  
[`chains.prompt_selector.ConditionalPromptSelector`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.ConditionalPromptSelector.html#langchain.chains.prompt_selector.ConditionalPromptSelector "langchain.chains.prompt_selector.ConditionalPromptSelector") | Prompt collection that goes through conditionals.  
[`chains.qa_with_sources.loading.LoadingCallable`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.loading.LoadingCallable.html#langchain.chains.qa_with_sources.loading.LoadingCallable "langchain.chains.qa_with_sources.loading.LoadingCallable")(...) | Interface for loading the combine documents chain.  
[`chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain.html#langchain.chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain "langchain.chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain") | Question-answering with sources over an index.  
[`chains.qa_with_sources.vector_db.VectorDBQAWithSourcesChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.vector_db.VectorDBQAWithSourcesChain.html#langchain.chains.qa_with_sources.vector_db.VectorDBQAWithSourcesChain "langchain.chains.qa_with_sources.vector_db.VectorDBQAWithSourcesChain") | Question-answering with sources over a vector database.  
[`chains.query_constructor.base.StructuredQueryOutputParser`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.StructuredQueryOutputParser.html#langchain.chains.query_constructor.base.StructuredQueryOutputParser "langchain.chains.query_constructor.base.StructuredQueryOutputParser") | Output parser that parses a structured query.  
[`chains.query_constructor.parser.ISO8601Date`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.ISO8601Date.html#langchain.chains.query_constructor.parser.ISO8601Date "langchain.chains.query_constructor.parser.ISO8601Date") | A date in ISO 8601 format (YYYY-MM-DD).  
[`chains.query_constructor.parser.ISO8601DateTime`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.ISO8601DateTime.html#langchain.chains.query_constructor.parser.ISO8601DateTime "langchain.chains.query_constructor.parser.ISO8601DateTime") | A datetime in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).  
[`chains.query_constructor.parser.QueryTransformer`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.QueryTransformer.html#langchain.chains.query_constructor.parser.QueryTransformer "langchain.chains.query_constructor.parser.QueryTransformer")(*args) | Transform a query string into an intermediate representation.  
[`chains.query_constructor.schema.AttributeInfo`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.schema.AttributeInfo.html#langchain.chains.query_constructor.schema.AttributeInfo "langchain.chains.query_constructor.schema.AttributeInfo") | Information about a data source attribute.  
[`chains.question_answering.chain.LoadingCallable`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.question_answering.chain.LoadingCallable.html#langchain.chains.question_answering.chain.LoadingCallable "langchain.chains.question_answering.chain.LoadingCallable")(...) | Interface for loading the combine documents chain.  
[`chains.router.base.MultiRouteChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.base.MultiRouteChain.html#langchain.chains.router.base.MultiRouteChain "langchain.chains.router.base.MultiRouteChain") | Use a single chain to route an input to one of multiple candidate chains.  
[`chains.router.base.Route`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.base.Route.html#langchain.chains.router.base.Route "langchain.chains.router.base.Route")(destination, ...) | Create new instance of Route(destination, next_inputs)  
[`chains.router.base.RouterChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.base.RouterChain.html#langchain.chains.router.base.RouterChain "langchain.chains.router.base.RouterChain") | Chain that outputs the name of a destination chain and the inputs to it.  
[`chains.router.embedding_router.EmbeddingRouterChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.embedding_router.EmbeddingRouterChain.html#langchain.chains.router.embedding_router.EmbeddingRouterChain "langchain.chains.router.embedding_router.EmbeddingRouterChain") | Chain that uses embeddings to route between options.  
[`chains.router.llm_router.RouterOutputParser`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.llm_router.RouterOutputParser.html#langchain.chains.router.llm_router.RouterOutputParser "langchain.chains.router.llm_router.RouterOutputParser") | Parser for output of router chain in the multi-prompt chain.  
[`chains.router.multi_retrieval_qa.MultiRetrievalQAChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.multi_retrieval_qa.MultiRetrievalQAChain.html#langchain.chains.router.multi_retrieval_qa.MultiRetrievalQAChain "langchain.chains.router.multi_retrieval_qa.MultiRetrievalQAChain") | A multi-route chain that uses an LLM router chain to choose amongst retrieval qa chains.  
[`chains.sequential.SequentialChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sequential.SequentialChain.html#langchain.chains.sequential.SequentialChain "langchain.chains.sequential.SequentialChain") | Chain where the outputs of one chain feed directly into next.  
[`chains.sequential.SimpleSequentialChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sequential.SimpleSequentialChain.html#langchain.chains.sequential.SimpleSequentialChain "langchain.chains.sequential.SimpleSequentialChain") | Simple chain where the outputs of one step feed directly into next.  
[`chains.sql_database.query.SQLInput`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.SQLInput.html#langchain.chains.sql_database.query.SQLInput "langchain.chains.sql_database.query.SQLInput") | Input for a SQL Chain.  
[`chains.sql_database.query.SQLInputWithTables`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.SQLInputWithTables.html#langchain.chains.sql_database.query.SQLInputWithTables "langchain.chains.sql_database.query.SQLInputWithTables") | Input for a SQL Chain.  
[`chains.summarize.chain.LoadingCallable`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.summarize.chain.LoadingCallable.html#langchain.chains.summarize.chain.LoadingCallable "langchain.chains.summarize.chain.LoadingCallable")(...) | Interface for loading the combine documents chain.  
[`chains.transform.TransformChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.transform.TransformChain.html#langchain.chains.transform.TransformChain "langchain.chains.transform.TransformChain") | Chain that transforms the chain output.  
**Functions**
[`chains.combine_documents.reduce.acollapse_docs`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.acollapse_docs.html#langchain.chains.combine_documents.reduce.acollapse_docs "langchain.chains.combine_documents.reduce.acollapse_docs")(...) | Execute a collapse function on a set of documents and merge their metadatas.  
---|---  
[`chains.combine_documents.reduce.collapse_docs`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.collapse_docs.html#langchain.chains.combine_documents.reduce.collapse_docs "langchain.chains.combine_documents.reduce.collapse_docs")(...) | Execute a collapse function on a set of documents and merge their metadatas.  
[`chains.combine_documents.reduce.split_list_of_docs`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.split_list_of_docs.html#langchain.chains.combine_documents.reduce.split_list_of_docs "langchain.chains.combine_documents.reduce.split_list_of_docs")(...) | Split Documents into subsets that each meet a cumulative length constraint.  
[`chains.combine_documents.stuff.create_stuff_documents_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.stuff.create_stuff_documents_chain.html#langchain.chains.combine_documents.stuff.create_stuff_documents_chain "langchain.chains.combine_documents.stuff.create_stuff_documents_chain")(...) | Create a chain for passing a list of Documents to a model.  
[`chains.example_generator.generate_example`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.example_generator.generate_example.html#langchain.chains.example_generator.generate_example "langchain.chains.example_generator.generate_example")(...) | Return another example given a list of examples for a prompt.  
[`chains.history_aware_retriever.create_history_aware_retriever`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.history_aware_retriever.create_history_aware_retriever.html#langchain.chains.history_aware_retriever.create_history_aware_retriever "langchain.chains.history_aware_retriever.create_history_aware_retriever")(...) | Create a chain that takes conversation history and returns documents.  
[`chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable.html#langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable "langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable")(llm) | Create a citation fuzzy match Runnable.  
[`chains.openai_functions.openapi.openapi_spec_to_openai_fn`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.openapi.openapi_spec_to_openai_fn.html#langchain.chains.openai_functions.openapi.openapi_spec_to_openai_fn "langchain.chains.openai_functions.openapi.openapi_spec_to_openai_fn")(spec) | Convert a valid OpenAPI spec to the JSON Schema format expected for OpenAI  
[`chains.openai_functions.utils.get_llm_kwargs`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.utils.get_llm_kwargs.html#langchain.chains.openai_functions.utils.get_llm_kwargs "langchain.chains.openai_functions.utils.get_llm_kwargs")(...) | Return the kwargs for the LLMChain constructor.  
[`chains.prompt_selector.is_chat_model`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.is_chat_model.html#langchain.chains.prompt_selector.is_chat_model "langchain.chains.prompt_selector.is_chat_model")(llm) | Check if the language model is a chat model.  
[`chains.prompt_selector.is_llm`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.is_llm.html#langchain.chains.prompt_selector.is_llm "langchain.chains.prompt_selector.is_llm")(llm) | Check if the language model is a LLM.  
[`chains.query_constructor.base.construct_examples`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.construct_examples.html#langchain.chains.query_constructor.base.construct_examples "langchain.chains.query_constructor.base.construct_examples")(...) | Construct examples from input-output pairs.  
[`chains.query_constructor.base.fix_filter_directive`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.fix_filter_directive.html#langchain.chains.query_constructor.base.fix_filter_directive "langchain.chains.query_constructor.base.fix_filter_directive")(...) | Fix invalid filter directive.  
[`chains.query_constructor.base.get_query_constructor_prompt`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.get_query_constructor_prompt.html#langchain.chains.query_constructor.base.get_query_constructor_prompt "langchain.chains.query_constructor.base.get_query_constructor_prompt")(...) | Create query construction prompt.  
[`chains.query_constructor.base.load_query_constructor_runnable`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.load_query_constructor_runnable.html#langchain.chains.query_constructor.base.load_query_constructor_runnable "langchain.chains.query_constructor.base.load_query_constructor_runnable")(...) | Load a query constructor runnable chain.  
[`chains.query_constructor.parser.get_parser`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.get_parser.html#langchain.chains.query_constructor.parser.get_parser "langchain.chains.query_constructor.parser.get_parser")([...]) | Return a parser for the query language.  
[`chains.retrieval.create_retrieval_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval.create_retrieval_chain.html#langchain.chains.retrieval.create_retrieval_chain "langchain.chains.retrieval.create_retrieval_chain")(...) | Create retrieval chain that retrieves documents and then passes them on.  
[`chains.sql_database.query.create_sql_query_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.create_sql_query_chain.html#langchain.chains.sql_database.query.create_sql_query_chain "langchain.chains.sql_database.query.create_sql_query_chain")(llm, db) | Create a chain that generates SQL queries.  
[`chains.structured_output.base.get_openai_output_parser`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.get_openai_output_parser.html#langchain.chains.structured_output.base.get_openai_output_parser "langchain.chains.structured_output.base.get_openai_output_parser")(...) | Get the appropriate function output parser given the user functions.  
[`chains.summarize.chain.load_summarize_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.summarize.chain.load_summarize_chain.html#langchain.chains.summarize.chain.load_summarize_chain "langchain.chains.summarize.chain.load_summarize_chain")(llm) | Load summarizing chain.  
**Deprecated classes**
[`chains.api.base.APIChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.api.base.APIChain.html#langchain.chains.api.base.APIChain "langchain.chains.api.base.APIChain") |   
---|---  
[`chains.combine_documents.base.AnalyzeDocumentChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.AnalyzeDocumentChain.html#langchain.chains.combine_documents.base.AnalyzeDocumentChain "langchain.chains.combine_documents.base.AnalyzeDocumentChain") |   
[`chains.combine_documents.map_reduce.MapReduceDocumentsChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.map_reduce.MapReduceDocumentsChain.html#langchain.chains.combine_documents.map_reduce.MapReduceDocumentsChain "langchain.chains.combine_documents.map_reduce.MapReduceDocumentsChain") |   
[`chains.combine_documents.map_rerank.MapRerankDocumentsChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.map_rerank.MapRerankDocumentsChain.html#langchain.chains.combine_documents.map_rerank.MapRerankDocumentsChain "langchain.chains.combine_documents.map_rerank.MapRerankDocumentsChain") |   
[`chains.combine_documents.reduce.ReduceDocumentsChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.reduce.ReduceDocumentsChain.html#langchain.chains.combine_documents.reduce.ReduceDocumentsChain "langchain.chains.combine_documents.reduce.ReduceDocumentsChain") |   
[`chains.combine_documents.refine.RefineDocumentsChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.refine.RefineDocumentsChain.html#langchain.chains.combine_documents.refine.RefineDocumentsChain "langchain.chains.combine_documents.refine.RefineDocumentsChain") |   
[`chains.combine_documents.stuff.StuffDocumentsChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.stuff.StuffDocumentsChain.html#langchain.chains.combine_documents.stuff.StuffDocumentsChain "langchain.chains.combine_documents.stuff.StuffDocumentsChain") |   
[`chains.constitutional_ai.base.ConstitutionalChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.base.ConstitutionalChain.html#langchain.chains.constitutional_ai.base.ConstitutionalChain "langchain.chains.constitutional_ai.base.ConstitutionalChain") |   
[`chains.conversation.base.ConversationChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversation.base.ConversationChain.html#langchain.chains.conversation.base.ConversationChain "langchain.chains.conversation.base.ConversationChain") |   
[`chains.conversational_retrieval.base.ConversationalRetrievalChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.ConversationalRetrievalChain.html#langchain.chains.conversational_retrieval.base.ConversationalRetrievalChain "langchain.chains.conversational_retrieval.base.ConversationalRetrievalChain") |   
[`chains.llm.LLMChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain") |   
[`chains.llm_checker.base.LLMCheckerChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_checker.base.LLMCheckerChain.html#langchain.chains.llm_checker.base.LLMCheckerChain "langchain.chains.llm_checker.base.LLMCheckerChain") |   
[`chains.llm_math.base.LLMMathChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_math.base.LLMMathChain.html#langchain.chains.llm_math.base.LLMMathChain "langchain.chains.llm_math.base.LLMMathChain") |   
[`chains.llm_summarization_checker.base.LLMSummarizationCheckerChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain.html#langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain") |   
[`chains.mapreduce.MapReduceChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.mapreduce.MapReduceChain.html#langchain.chains.mapreduce.MapReduceChain "langchain.chains.mapreduce.MapReduceChain") |   
[`chains.natbot.base.NatBotChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.natbot.base.NatBotChain.html#langchain.chains.natbot.base.NatBotChain "langchain.chains.natbot.base.NatBotChain") |   
[`chains.qa_generation.base.QAGenerationChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_generation.base.QAGenerationChain.html#langchain.chains.qa_generation.base.QAGenerationChain "langchain.chains.qa_generation.base.QAGenerationChain") |   
[`chains.qa_with_sources.base.BaseQAWithSourcesChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.base.BaseQAWithSourcesChain.html#langchain.chains.qa_with_sources.base.BaseQAWithSourcesChain "langchain.chains.qa_with_sources.base.BaseQAWithSourcesChain") |   
[`chains.qa_with_sources.base.QAWithSourcesChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.base.QAWithSourcesChain.html#langchain.chains.qa_with_sources.base.QAWithSourcesChain "langchain.chains.qa_with_sources.base.QAWithSourcesChain") |   
[`chains.retrieval_qa.base.BaseRetrievalQA`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval_qa.base.BaseRetrievalQA.html#langchain.chains.retrieval_qa.base.BaseRetrievalQA "langchain.chains.retrieval_qa.base.BaseRetrievalQA") |   
[`chains.retrieval_qa.base.RetrievalQA`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval_qa.base.RetrievalQA.html#langchain.chains.retrieval_qa.base.RetrievalQA "langchain.chains.retrieval_qa.base.RetrievalQA") |   
[`chains.retrieval_qa.base.VectorDBQA`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval_qa.base.VectorDBQA.html#langchain.chains.retrieval_qa.base.VectorDBQA "langchain.chains.retrieval_qa.base.VectorDBQA") |   
[`chains.router.llm_router.LLMRouterChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.llm_router.LLMRouterChain.html#langchain.chains.router.llm_router.LLMRouterChain "langchain.chains.router.llm_router.LLMRouterChain") |   
[`chains.router.multi_prompt.MultiPromptChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.multi_prompt.MultiPromptChain.html#langchain.chains.router.multi_prompt.MultiPromptChain "langchain.chains.router.multi_prompt.MultiPromptChain") |   
**Deprecated functions**
[`chains.loading.load_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.loading.load_chain.html#langchain.chains.loading.load_chain "langchain.chains.loading.load_chain")(path, **kwargs) |   
---|---  
[`chains.loading.load_chain_from_config`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.loading.load_chain_from_config.html#langchain.chains.loading.load_chain_from_config "langchain.chains.loading.load_chain_from_config")(...) |   
[`chains.openai_functions.base.create_openai_fn_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.base.create_openai_fn_chain.html#langchain.chains.openai_functions.base.create_openai_fn_chain "langchain.chains.openai_functions.base.create_openai_fn_chain")(...) |   
[`chains.openai_functions.base.create_structured_output_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.base.create_structured_output_chain.html#langchain.chains.openai_functions.base.create_structured_output_chain "langchain.chains.openai_functions.base.create_structured_output_chain")(...) |   
[`chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_chain.html#langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_chain "langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_chain")(llm) |   
[`chains.openai_functions.extraction.create_extraction_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.extraction.create_extraction_chain.html#langchain.chains.openai_functions.extraction.create_extraction_chain "langchain.chains.openai_functions.extraction.create_extraction_chain")(...) |   
[`chains.openai_functions.extraction.create_extraction_chain_pydantic`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.extraction.create_extraction_chain_pydantic.html#langchain.chains.openai_functions.extraction.create_extraction_chain_pydantic "langchain.chains.openai_functions.extraction.create_extraction_chain_pydantic")(...) |   
[`chains.openai_functions.openapi.get_openapi_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.openapi.get_openapi_chain.html#langchain.chains.openai_functions.openapi.get_openapi_chain "langchain.chains.openai_functions.openapi.get_openapi_chain")(spec) |   
[`chains.openai_functions.qa_with_structure.create_qa_with_sources_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.create_qa_with_sources_chain.html#langchain.chains.openai_functions.qa_with_structure.create_qa_with_sources_chain "langchain.chains.openai_functions.qa_with_structure.create_qa_with_sources_chain")(llm) |   
[`chains.openai_functions.qa_with_structure.create_qa_with_structure_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.create_qa_with_structure_chain.html#langchain.chains.openai_functions.qa_with_structure.create_qa_with_structure_chain "langchain.chains.openai_functions.qa_with_structure.create_qa_with_structure_chain")(...) |   
[`chains.openai_functions.tagging.create_tagging_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.tagging.create_tagging_chain.html#langchain.chains.openai_functions.tagging.create_tagging_chain "langchain.chains.openai_functions.tagging.create_tagging_chain")(...) |   
[`chains.openai_functions.tagging.create_tagging_chain_pydantic`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.tagging.create_tagging_chain_pydantic.html#langchain.chains.openai_functions.tagging.create_tagging_chain_pydantic "langchain.chains.openai_functions.tagging.create_tagging_chain_pydantic")(...) |   
[`chains.openai_tools.extraction.create_extraction_chain_pydantic`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_tools.extraction.create_extraction_chain_pydantic.html#langchain.chains.openai_tools.extraction.create_extraction_chain_pydantic "langchain.chains.openai_tools.extraction.create_extraction_chain_pydantic")(...) |   
[`chains.qa_with_sources.loading.load_qa_with_sources_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.loading.load_qa_with_sources_chain.html#langchain.chains.qa_with_sources.loading.load_qa_with_sources_chain "langchain.chains.qa_with_sources.loading.load_qa_with_sources_chain")(llm) |   
[`chains.query_constructor.base.load_query_constructor_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.load_query_constructor_chain.html#langchain.chains.query_constructor.base.load_query_constructor_chain "langchain.chains.query_constructor.base.load_query_constructor_chain")(...) |   
[`chains.question_answering.chain.load_qa_chain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.question_answering.chain.load_qa_chain.html#langchain.chains.question_answering.chain.load_qa_chain "langchain.chains.question_answering.chain.load_qa_chain")(llm) |   
[`chains.structured_output.base.create_openai_fn_runnable`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.create_openai_fn_runnable.html#langchain.chains.structured_output.base.create_openai_fn_runnable "langchain.chains.structured_output.base.create_openai_fn_runnable")(...) |   
[`chains.structured_output.base.create_structured_output_runnable`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.create_structured_output_runnable.html#langchain.chains.structured_output.base.create_structured_output_runnable "langchain.chains.structured_output.base.create_structured_output_runnable")(...) |   
© Copyright 2025, LangChain Inc. 

