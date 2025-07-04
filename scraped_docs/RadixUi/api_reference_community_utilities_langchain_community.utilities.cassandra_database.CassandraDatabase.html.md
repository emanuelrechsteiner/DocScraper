---
url: https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html
scraped_at: 2025-05-25T18:03:26.353690
title: CassandraDatabase — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#main-content)
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
    * [`tools`](https://python.langchain.com/api_reference/community/tools.html)
    * [`utilities`](https://python.langchain.com/api_reference/community/utilities.html)
      * [AlphaVantageAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.alpha_vantage.AlphaVantageAPIWrapper.html)
      * [ArceeDocument](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.ArceeDocument.html)
      * [ArceeDocumentAdapter](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.ArceeDocumentAdapter.html)
      * [ArceeDocumentSource](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.ArceeDocumentSource.html)
      * [ArceeRoute](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.ArceeRoute.html)
      * [ArceeWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.ArceeWrapper.html)
      * [DALMFilter](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.DALMFilter.html)
      * [DALMFilterType](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.DALMFilterType.html)
      * [ArxivAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arxiv.ArxivAPIWrapper.html)
      * [AskNewsAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.asknews.AskNewsAPIWrapper.html)
      * [SetupMode](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.astradb.SetupMode.html)
      * [LambdaWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.awslambda.LambdaWrapper.html)
      * [BibtexparserWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.bibtex.BibtexparserWrapper.html)
      * [BingSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.bing_search.BingSearchAPIWrapper.html)
      * [BraveSearchWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.brave_search.BraveSearchWrapper.html)
      * [SetupMode](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra.SetupMode.html)
      * [CassandraDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html)
      * [DatabaseError](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.DatabaseError.html)
      * [Table](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html)
      * [CUList](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.CUList.html)
      * [ClickupAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.ClickupAPIWrapper.html)
      * [Component](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.Component.html)
      * [Member](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.Member.html)
      * [Space](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.Space.html)
      * [Task](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.Task.html)
      * [Team](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.Team.html)
      * [DallEAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.dalle_image_generator.DallEAPIWrapper.html)
      * [DataForSeoAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.dataforseo_api_search.DataForSeoAPIWrapper.html)
      * [DataheraldAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.dataherald.DataheraldAPIWrapper.html)
      * [DriaAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.dria_index.DriaAPIWrapper.html)
      * [DuckDuckGoSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.duckduckgo_search.DuckDuckGoSearchAPIWrapper.html)
      * [FinancialDatasetsAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.financial_datasets.FinancialDatasetsAPIWrapper.html)
      * [GitHubAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.github.GitHubAPIWrapper.html)
      * [GitLabAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.gitlab.GitLabAPIWrapper.html)
      * [GoldenQueryAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.golden_query.GoldenQueryAPIWrapper.html)
      * [GoogleBooksAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_books.GoogleBooksAPIWrapper.html)
      * [GoogleFinanceAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_finance.GoogleFinanceAPIWrapper.html)
      * [GoogleJobsAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_jobs.GoogleJobsAPIWrapper.html)
      * [GoogleLensAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_lens.GoogleLensAPIWrapper.html)
      * [GoogleScholarAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_scholar.GoogleScholarAPIWrapper.html)
      * [GoogleSerperAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_serper.GoogleSerperAPIWrapper.html)
      * [GoogleTrendsAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_trends.GoogleTrendsAPIWrapper.html)
      * [GraphQLAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.graphql.GraphQLAPIWrapper.html)
      * [InfobipAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.infobip.InfobipAPIWrapper.html)
      * [JinaSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jina_search.JinaSearchAPIWrapper.html)
      * [JiraAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jira.JiraAPIWrapper.html)
      * [JiraOauth2](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jira.JiraOauth2.html)
      * [JiraOauth2Token](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jira.JiraOauth2Token.html)
      * [MaxComputeAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.max_compute.MaxComputeAPIWrapper.html)
      * [MerriamWebsterAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.merriam_webster.MerriamWebsterAPIWrapper.html)
      * [MetaphorSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.metaphor_search.MetaphorSearchAPIWrapper.html)
      * [MojeekSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.mojeek_search.MojeekSearchAPIWrapper.html)
      * [NasaAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nasa.NasaAPIWrapper.html)
      * [ASRInputType](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.ASRInputType.html)
      * [AudioStream](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.AudioStream.html)
      * [NVIDIARivaASR](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.NVIDIARivaASR.html)
      * [NVIDIARivaStream](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.NVIDIARivaStream.html)
      * [NVIDIARivaTTS](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.NVIDIARivaTTS.html)
      * [RivaASR](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaASR.html)
      * [RivaAudioEncoding](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaAudioEncoding.html)
      * [RivaAuthMixin](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaAuthMixin.html)
      * [RivaCommonConfigMixin](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaCommonConfigMixin.html)
      * [RivaTTS](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaTTS.html)
      * [SentinelT](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.SentinelT.html)
      * [HTTPVerb](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.HTTPVerb.html)
      * [OpenAPISpec](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html)
      * [OpenWeatherMapAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper.html)
      * [OracleSummary](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.oracleai.OracleSummary.html)
      * [OutlineAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.outline.OutlineAPIWrapper.html)
      * [ManagedPassioLifeAuth](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.passio_nutrition_ai.ManagedPassioLifeAuth.html)
      * [NoDiskStorage](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.passio_nutrition_ai.NoDiskStorage.html)
      * [NutritionAIAPI](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.passio_nutrition_ai.NutritionAIAPI.html)
      * [App](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html)
      * [Doc](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Doc.html)
      * [Framework](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Framework.html)
      * [IndexedDocument](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.IndexedDocument.html)
      * [PebbloLoaderAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.PebbloLoaderAPIWrapper.html)
      * [Routes](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Routes.html)
      * [Runtime](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Runtime.html)
      * [PolygonAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.polygon.PolygonAPIWrapper.html)
      * [Portkey](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.portkey.Portkey.html)
      * [PowerBIDataset](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.PowerBIDataset.html)
      * [PubMedAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pubmed.PubMedAPIWrapper.html)
      * [RedditSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.reddit_search.RedditSearchAPIWrapper.html)
      * [TokenEscaper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.redis.TokenEscaper.html)
      * [RememberizerAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.rememberizer.RememberizerAPIWrapper.html)
      * [GenericRequestsWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.GenericRequestsWrapper.html)
      * [JsonRequestsWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.JsonRequestsWrapper.html)
      * [Requests](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html)
      * [RequestsWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.RequestsWrapper.html)
      * [TextRequestsWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.TextRequestsWrapper.html)
      * [SceneXplainAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.scenexplain.SceneXplainAPIWrapper.html)
      * [SearchApiAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.searchapi.SearchApiAPIWrapper.html)
      * [SearxResults](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.searx_search.SearxResults.html)
      * [SearxSearchWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.searx_search.SearxSearchWrapper.html)
      * [SemanticScholarAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.semanticscholar.SemanticScholarAPIWrapper.html)
      * [HiddenPrints](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.serpapi.HiddenPrints.html)
      * [SerpAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.serpapi.SerpAPIWrapper.html)
      * [SparkSQL](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.spark_sql.SparkSQL.html)
      * [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html)
      * [StackExchangeAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.stackexchange.StackExchangeAPIWrapper.html)
      * [SteamWebAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.steam.SteamWebAPIWrapper.html)
      * [TavilySearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.tavily_search.TavilySearchAPIWrapper.html)
      * [TensorflowDatasets](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.tensorflow_datasets.TensorflowDatasets.html)
      * [TwilioAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.twilio.TwilioAPIWrapper.html)
      * [WikidataAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.wikidata.WikidataAPIWrapper.html)
      * [WikipediaAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.wikipedia.WikipediaAPIWrapper.html)
      * [WolframAlphaAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.wolfram_alpha.WolframAlphaAPIWrapper.html)
      * [YouAPIOutput](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouAPIOutput.html)
      * [YouDocument](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouDocument.html)
      * [YouHit](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouHit.html)
      * [YouHitMetadata](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouHitMetadata.html)
      * [YouSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouSearchAPIWrapper.html)
      * [ZapierNLAWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.zapier.ZapierNLAWrapper.html)
      * [get_num_tokens_anthropic](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.anthropic.get_num_tokens_anthropic.html)
      * [get_token_ids_anthropic](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.anthropic.get_token_ids_anthropic.html)
      * [aexecute_cql](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra.aexecute_cql.html)
      * [wrapped_response_future](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra.wrapped_response_future.html)
      * [extract_dict_elements_from_component_fields](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.extract_dict_elements_from_component_fields.html)
      * [fetch_data](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.fetch_data.html)
      * [fetch_first_id](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.fetch_first_id.html)
      * [fetch_folder_id](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.fetch_folder_id.html)
      * [fetch_list_id](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.fetch_list_id.html)
      * [fetch_space_id](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.fetch_space_id.html)
      * [fetch_team_id](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.fetch_team_id.html)
      * [load_query](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.load_query.html)
      * [parse_dict_through_component](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.parse_dict_through_component.html)
      * [desanitize](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.opaqueprompts.desanitize.html)
      * [sanitize](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.opaqueprompts.sanitize.html)
      * [is_http_retryable](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.passio_nutrition_ai.is_http_retryable.html)
      * [calculate_content_size](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.calculate_content_size.html)
      * [generate_size_based_batches](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.generate_size_based_batches.html)
      * [get_file_owner_from_path](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.get_file_owner_from_path.html)
      * [get_full_path](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.get_full_path.html)
      * [get_ip](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.get_ip.html)
      * [get_loader_full_path](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.get_loader_full_path.html)
      * [get_loader_type](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.get_loader_type.html)
      * [get_runtime](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.get_runtime.html)
      * [get_source_size](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.get_source_size.html)
      * [fix_table_name](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.fix_table_name.html)
      * [json_to_md](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.json_to_md.html)
      * [check_redis_module_exist](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.redis.check_redis_module_exist.html)
      * [get_client](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.redis.get_client.html)
      * [sanitize_schema](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.sanitize_schema.html)
      * [truncate_word](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.truncate_word.html)
      * [create_retry_decorator](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.vertexai.create_retry_decorator.html)
      * [get_client_info](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.vertexai.get_client_info.html)
      * [init_vertexai](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.vertexai.init_vertexai.html)
      * [load_image_from_gcs](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.vertexai.load_image_from_gcs.html)
      * [raise_vertex_import_error](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.vertexai.raise_vertex_import_error.html)
      * [ApifyWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.apify.ApifyWrapper.html)
      * [GooglePlacesAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_places_api.GooglePlacesAPIWrapper.html)
      * [GoogleSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html)
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
  * [`utilities`](https://python.langchain.com/api_reference/community/utilities.html)
  * CassandraDatabase


# CassandraDatabase[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#cassandradatabase "Link to this heading") 

_class_ langchain_community.utilities.cassandra_database.CassandraDatabase( 
    _session :Session|None=None_,     _exclude_tables :List[str]|None=None_,     _include_tables :List[str]|None=None_,     _cassio_init_kwargs :Dict[str,Any]|None=None_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase "Link to this definition")     
Apache Cassandra® database wrapper.
Methods
[`__init__`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.__init__ "langchain_community.utilities.cassandra_database.CassandraDatabase.__init__")([session, exclude_tables, ...]) |   
---|---  
[`fetch_all`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.fetch_all "langchain_community.utilities.cassandra_database.CassandraDatabase.fetch_all")(query, **kwargs) |   
[`fetch_one`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.fetch_one "langchain_community.utilities.cassandra_database.CassandraDatabase.fetch_one")(query, **kwargs) |   
[`format_keyspace_to_markdown`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.format_keyspace_to_markdown "langchain_community.utilities.cassandra_database.CassandraDatabase.format_keyspace_to_markdown")(keyspace[, tables]) | Generates a markdown representation of the schema for a specific keyspace by iterating over all tables within that keyspace and calling their as_markdown method.  
[`format_schema_to_markdown`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.format_schema_to_markdown "langchain_community.utilities.cassandra_database.CassandraDatabase.format_schema_to_markdown")() | Generates a markdown representation of the schema for all keyspaces and tables within the CassandraDatabase instance.  
[`get_context`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_context "langchain_community.utilities.cassandra_database.CassandraDatabase.get_context")() | Return db context that you may want in agent prompt.  
[`get_keyspace_tables`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_keyspace_tables "langchain_community.utilities.cassandra_database.CassandraDatabase.get_keyspace_tables")(keyspace) | Get the Table objects for the specified keyspace.  
[`get_table_data`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_table_data "langchain_community.utilities.cassandra_database.CassandraDatabase.get_table_data")(keyspace, table, predicate, limit) | Get data from the specified table in the specified keyspace.  
[`run`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.run "langchain_community.utilities.cassandra_database.CassandraDatabase.run")(query[, fetch]) | Execute a CQL query and return the results. 

Parameters:
      
  * **session** (_Optional_ _[__Session_ _]_)
  * **exclude_tables** (_Optional_ _[__List_ _[__str_ _]__]_)
  * **include_tables** (_Optional_ _[__List_ _[__str_ _]__]_)
  * **cassio_init_kwargs** (_Optional_ _[__Dict_ _[__str_ _,__Any_ _]__]_)



__init__( 
    _session :Session|None=None_,     _exclude_tables :List[str]|None=None_,     _include_tables :List[str]|None=None_,     _cassio_init_kwargs :Dict[str,Any]|None=None_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.__init__)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.__init__ "Link to this definition")      

Parameters:
    
  * **session** (_Optional_ _[__Session_ _]_)
  * **exclude_tables** (_Optional_ _[__List_ _[__str_ _]__]_)
  * **include_tables** (_Optional_ _[__List_ _[__str_ _]__]_)
  * **cassio_init_kwargs** (_Optional_ _[__Dict_ _[__str_ _,__Any_ _]__]_)



fetch_all( 
    _query :str_,     _** kwargs:Any_, ) → list[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.fetch_all)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.fetch_all "Link to this definition")      

Parameters:
    
  * **query** (_str_)
  * **kwargs** (_Any_)



Return type:
    
list 

fetch_one( 
    _query :str_,     _** kwargs:Any_, ) → Dict[str,Any][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.fetch_one)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.fetch_one "Link to this definition")      

Parameters:
    
  * **query** (_str_)
  * **kwargs** (_Any_)



Return type:
    
_Dict_[str, _Any_] 

format_keyspace_to_markdown( 
    _keyspace :str_,     _tables :List[[Table](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html#langchain_community.utilities.cassandra_database.Table "langchain_community.utilities.cassandra_database.Table")]|None=None_, ) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.format_keyspace_to_markdown)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.format_keyspace_to_markdown "Link to this definition")     
Generates a markdown representation of the schema for a specific keyspace by iterating over all tables within that keyspace and calling their as_markdown method. 

Parameters:
    
  * **keyspace** (_str_) – The name of the keyspace to generate markdown documentation for.
  * **tables** (_List_ _[_[_Table_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html#langchain_community.utilities.cassandra_database.Table "langchain_community.utilities.cassandra_database.Table") _]__|__None_) – list of tables in the keyspace; it will be resolved if not provided.



Returns:
    
A string containing the markdown representation of the specified keyspace schema. 

Return type:
    
str 

format_schema_to_markdown() → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.format_schema_to_markdown)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.format_schema_to_markdown "Link to this definition")
    
Generates a markdown representation of the schema for all keyspaces and tables within the CassandraDatabase instance. This method utilizes the format_keyspace_to_markdown method to create markdown sections for each keyspace, assembling them into a comprehensive schema document.
Iterates through each keyspace in the database, utilizing format_keyspace_to_markdown to generate markdown for each keyspace’s schema, including details of its tables. These sections are concatenated to form a single markdown document that represents the schema of the entire database or the subset of keyspaces that have been resolved in this instance. 

Returns:
    
A markdown string that documents the schema of all resolved keyspaces and their tables within this CassandraDatabase instance. This includes keyspace names, table names, comments, columns, partition keys, clustering keys, and indexes for each table. 

Return type:
    
str 

get_context() → Dict[str,Any][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.get_context)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_context "Link to this definition")
    
Return db context that you may want in agent prompt. 

Return type:
    
_Dict_[str, _Any_] 

get_keyspace_tables( 
    _keyspace :str_, ) → List[[Table](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html#langchain_community.utilities.cassandra_database.Table "langchain_community.utilities.cassandra_database.Table")][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.get_keyspace_tables)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_keyspace_tables "Link to this definition")     
Get the Table objects for the specified keyspace. 

Parameters:
    
**keyspace** (_str_) 

Return type:
    
_List_[[_Table_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html#langchain_community.utilities.cassandra_database.Table "langchain_community.utilities.cassandra_database.Table")] 

get_table_data( 
    _keyspace :str_,     _table :str_,     _predicate :str_,     _limit :int_, ) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.get_table_data)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_table_data "Link to this definition")     
Get data from the specified table in the specified keyspace. 

Parameters:
    
  * **keyspace** (_str_)
  * **table** (_str_)
  * **predicate** (_str_)
  * **limit** (_int_)



Return type:
    
str 

run( 
    _query :str_,     _fetch :str='all'_,     _** kwargs:Any_, ) → list|Dict[str,Any]|ResultSet[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.run)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.run "Link to this definition")     
Execute a CQL query and return the results. 

Parameters:
    
  * **query** (_str_)
  * **fetch** (_str_)
  * **kwargs** (_Any_)



Return type:
    
Union[list, Dict[str, Any], ResultSet]
Examples using CassandraDatabase
  * [Cassandra Database Toolkit](https://python.langchain.com/docs/integrations/tools/cassandra_database/)


On this page 
  * [`CassandraDatabase`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase)
    * [`__init__()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.__init__)
    * [`fetch_all()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.fetch_all)
    * [`fetch_one()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.fetch_one)
    * [`format_keyspace_to_markdown()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.format_keyspace_to_markdown)
    * [`format_schema_to_markdown()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.format_schema_to_markdown)
    * [`get_context()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_context)
    * [`get_keyspace_tables()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_keyspace_tables)
    * [`get_table_data()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.get_table_data)
    * [`run()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase.run)


© Copyright 2025, LangChain Inc. 

