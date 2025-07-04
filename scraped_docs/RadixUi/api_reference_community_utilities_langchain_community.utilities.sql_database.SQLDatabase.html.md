---
url: https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html
scraped_at: 2025-05-25T17:56:50.243756
title: SQLDatabase — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#main-content)
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
  * SQLDatabase


# SQLDatabase[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#sqldatabase "Link to this heading") 

_class_ langchain_community.utilities.sql_database.SQLDatabase( 
    _engine :Engine_,     _schema :str|None=None_,     _metadata :MetaData|None=None_,     _ignore_tables :List[str]|None=None_,     _include_tables :List[str]|None=None_,     _sample_rows_in_table_info :int=3_,     _indexes_in_table_info :bool=False_,     _custom_table_info :dict|None=None_,     _view_support :bool=False_,     _max_string_length :int=300_,     _lazy_table_reflection :bool=False_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "Link to this definition")     
SQLAlchemy wrapper around a database.
Create engine from database URI.
Attributes
`dialect` | Return string representation of dialect to use.  
---|---  
`table_info` | Information about all tables in the database.  
Methods
[`__init__`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.__init__ "langchain_community.utilities.sql_database.SQLDatabase.__init__")(engine[, schema, metadata, ...]) | Create engine from database URI.  
---|---  
[`from_cnosdb`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_cnosdb "langchain_community.utilities.sql_database.SQLDatabase.from_cnosdb")([url, user, password, tenant, ...]) | Class method to create an SQLDatabase instance from a CnosDB connection.  
[`from_databricks`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_databricks "langchain_community.utilities.sql_database.SQLDatabase.from_databricks")(catalog, schema[, host, ...]) |   
[`from_uri`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_uri "langchain_community.utilities.sql_database.SQLDatabase.from_uri")(database_uri[, engine_args]) | Construct a SQLAlchemy engine from URI.  
[`get_context`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_context "langchain_community.utilities.sql_database.SQLDatabase.get_context")() | Return db context that you may want in agent prompt.  
[`get_table_info`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_info "langchain_community.utilities.sql_database.SQLDatabase.get_table_info")([table_names, get_col_comments]) | Get information about specified tables.  
[`get_table_info_no_throw`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_info_no_throw "langchain_community.utilities.sql_database.SQLDatabase.get_table_info_no_throw")([table_names]) | Get information about specified tables.  
[`get_table_names`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_names "langchain_community.utilities.sql_database.SQLDatabase.get_table_names")() |   
[`get_usable_table_names`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_usable_table_names "langchain_community.utilities.sql_database.SQLDatabase.get_usable_table_names")() | Get names of tables available.  
[`run`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.run "langchain_community.utilities.sql_database.SQLDatabase.run")(command[, fetch, include_columns, ...]) | Execute a SQL command and return a string representing the results.  
[`run_no_throw`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.run_no_throw "langchain_community.utilities.sql_database.SQLDatabase.run_no_throw")(command[, fetch, ...]) | Execute a SQL command and return a string representing the results. 

Parameters:
      
  * **engine** (_Engine_)
  * **schema** (_Optional_ _[__str_ _]_)
  * **metadata** (_Optional_ _[__MetaData_ _]_)
  * **ignore_tables** (_Optional_ _[__List_ _[__str_ _]__]_)
  * **include_tables** (_Optional_ _[__List_ _[__str_ _]__]_)
  * **sample_rows_in_table_info** (_int_)
  * **indexes_in_table_info** (_bool_)
  * **custom_table_info** (_Optional_ _[__dict_ _]_)
  * **view_support** (_bool_)
  * **max_string_length** (_int_)
  * **lazy_table_reflection** (_bool_)



__init__( 
    _engine :Engine_,     _schema :str|None=None_,     _metadata :MetaData|None=None_,     _ignore_tables :List[str]|None=None_,     _include_tables :List[str]|None=None_,     _sample_rows_in_table_info :int=3_,     _indexes_in_table_info :bool=False_,     _custom_table_info :dict|None=None_,     _view_support :bool=False_,     _max_string_length :int=300_,     _lazy_table_reflection :bool=False_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.__init__)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.__init__ "Link to this definition")     
Create engine from database URI. 

Parameters:
    
  * **engine** (_Engine_)
  * **schema** (_str_ _|__None_)
  * **metadata** (_MetaData_ _|__None_)
  * **ignore_tables** (_List_ _[__str_ _]__|__None_)
  * **include_tables** (_List_ _[__str_ _]__|__None_)
  * **sample_rows_in_table_info** (_int_)
  * **indexes_in_table_info** (_bool_)
  * **custom_table_info** (_dict_ _|__None_)
  * **view_support** (_bool_)
  * **max_string_length** (_int_)
  * **lazy_table_reflection** (_bool_)



_classmethod_ from_cnosdb( 
    _url :str='127.0.0.1:8902'_,     _user :str='root'_,     _password :str=''_,     _tenant :str='cnosdb'_,     _database :str='public'_, ) → [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.from_cnosdb)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_cnosdb "Link to this definition")     
Class method to create an SQLDatabase instance from a CnosDB connection. This method requires the ‘cnos-connector’ package. If not installed, it can be added using pip install cnos-connector. 

Parameters:
    
  * **url** (_str_) – The HTTP connection host name and port number of the CnosDB service, excluding “<http://>” or “<https://>”, with a default value of “127.0.0.1:8902”.
  * **user** (_str_) – The username used to connect to the CnosDB service, with a default value of “root”.
  * **password** (_str_) – The password of the user connecting to the CnosDB service, with a default value of “”.
  * **tenant** (_str_) – The name of the tenant used to connect to the CnosDB service, with a default value of “cnosdb”.
  * **database** (_str_) – The name of the database in the CnosDB tenant.



Returns:
    
An instance of SQLDatabase configured with the provided CnosDB connection details. 

Return type:
    
[SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase") 

_classmethod_ from_databricks( 
    _catalog :str_,     _schema :str_,     _host :str|None=None_,     _api_token :str|None=None_,     _warehouse_id :str|None=None_,     _cluster_id :str|None=None_,     _engine_args :dict|None=None_,     _** kwargs:Any_, ) → [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.from_databricks)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_databricks "Link to this definition")     
Deprecated since version 0.3.18: For performing structured retrieval using Databricks SQL, see the latest best practices and recommended APIs at <https://docs.unitycatalog.io/ai/integrations/langchain/> instead It will not be removed until langchain-community==1.0.
Class method to create an SQLDatabase instance from a Databricks connection. This method requires the ‘databricks-sql-connector’ package. If not installed, it can be added using pip install databricks-sql-connector. 

Parameters:
    
  * **catalog** (_str_) – The catalog name in the Databricks database.
  * **schema** (_str_) – The schema name in the catalog.
  * **host** (_Optional_ _[__str_ _]_) – The Databricks workspace hostname, excluding ‘<https://>’ part. If not provided, it attempts to fetch from the environment variable ‘DATABRICKS_HOST’. If still unavailable and if running in a Databricks notebook, it defaults to the current workspace hostname. Defaults to None.
  * **api_token** (_Optional_ _[__str_ _]_) – The Databricks personal access token for accessing the Databricks SQL warehouse or the cluster. If not provided, it attempts to fetch from ‘DATABRICKS_TOKEN’. If still unavailable and running in a Databricks notebook, a temporary token for the current user is generated. Defaults to None.
  * **warehouse_id** (_Optional_ _[__str_ _]_) – The warehouse ID in the Databricks SQL. If provided, the method configures the connection to use this warehouse. Cannot be used with ‘cluster_id’. Defaults to None.
  * **cluster_id** (_Optional_ _[__str_ _]_) – The cluster ID in the Databricks Runtime. If provided, the method configures the connection to use this cluster. Cannot be used with ‘warehouse_id’. If running in a Databricks notebook and both ‘warehouse_id’ and ‘cluster_id’ are None, it uses the ID of the cluster the notebook is attached to. Defaults to None.
  * **engine_args** (_Optional_ _[__dict_ _]_) – The arguments to be used when connecting Databricks. Defaults to None.
  * ****kwargs** (_Any_) – Additional keyword arguments for the from_uri method.



Returns:
     

An instance of SQLDatabase configured with the provided
    
Databricks connection details. 

Return type:
    
[SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase") 

Raises:
    
**ValueError** – If ‘databricks-sql-connector’ is not found, or if both ‘warehouse_id’ and ‘cluster_id’ are provided, or if neither ‘warehouse_id’ nor ‘cluster_id’ are provided and it’s not executing inside a Databricks notebook. 

_classmethod_ from_uri( 
    _database_uri :str|URL_,     _engine_args :dict|None=None_,     _** kwargs:Any_, ) → [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.from_uri)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_uri "Link to this definition")     
Construct a SQLAlchemy engine from URI. 

Parameters:
    
  * **database_uri** (_str_ _|__URL_)
  * **engine_args** (_dict_ _|__None_)
  * **kwargs** (_Any_)



Return type:
    
[_SQLDatabase_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase") 

get_context() → Dict[str,Any][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_context)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_context "Link to this definition")
    
Return db context that you may want in agent prompt. 

Return type:
    
_Dict_[str, _Any_] 

get_table_info( 
    _table_names :List[str]|None=None_,     _get_col_comments :bool=False_, ) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_table_info)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_info "Link to this definition")     
Get information about specified tables.
Follows best practices as specified in: Rajkumar et al, 2022 (<https://arxiv.org/abs/2204.00498>)
If sample_rows_in_table_info, the specified number of sample rows will be appended to each table description. This can increase performance as demonstrated in the paper. 

Parameters:
    
  * **table_names** (_List_ _[__str_ _]__|__None_)
  * **get_col_comments** (_bool_)



Return type:
    
str 

get_table_info_no_throw( 
    _table_names :List[str]|None=None_, ) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_table_info_no_throw)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_info_no_throw "Link to this definition")     
Get information about specified tables.
Follows best practices as specified in: Rajkumar et al, 2022 (<https://arxiv.org/abs/2204.00498>)
If sample_rows_in_table_info, the specified number of sample rows will be appended to each table description. This can increase performance as demonstrated in the paper. 

Parameters:
    
**table_names** (_List_ _[__str_ _]__|__None_) 

Return type:
    
str 

get_table_names() → Iterable[str][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_table_names)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_names "Link to this definition")
    
Deprecated since version 0.0.1: Use [`get_usable_table_names()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_usable_table_names "langchain_community.utilities.sql_database.SQLDatabase.get_usable_table_names") instead. It will not be removed until langchain-community==1.0.
Get names of tables available. 

Return type:
    
_Iterable_[str] 

get_usable_table_names() → Iterable[str][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_usable_table_names)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_usable_table_names "Link to this definition")
    
Get names of tables available. 

Return type:
    
_Iterable_[str] 

run( 
    _command :str|Executable_,     _fetch :Literal['all','one','cursor']='all'_,     _include_columns :bool=False_,     _*_ ,     _parameters :Dict[str,Any]|None=None_,     _execution_options :Dict[str,Any]|None=None_, ) → str|Sequence[Dict[str,Any]]|Result[Any][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.run)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.run "Link to this definition")     
Execute a SQL command and return a string representing the results.
If the statement returns rows, a string of the results is returned. If the statement returns no rows, an empty string is returned. 

Parameters:
    
  * **command** (_str_ _|__Executable_)
  * **fetch** (_Literal_ _[__'all'__,__'one'__,__'cursor'__]_)
  * **include_columns** (_bool_)
  * **parameters** (_Dict_ _[__str_ _,__Any_ _]__|__None_)
  * **execution_options** (_Dict_ _[__str_ _,__Any_ _]__|__None_)



Return type:
    
str | _Sequence_[_Dict_[str, _Any_]] | _Result_[_Any_] 

run_no_throw( 
    _command :str_,     _fetch :Literal['all','one']='all'_,     _include_columns :bool=False_,     _*_ ,     _parameters :Dict[str,Any]|None=None_,     _execution_options :Dict[str,Any]|None=None_, ) → str|Sequence[Dict[str,Any]]|Result[Any][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.run_no_throw)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.run_no_throw "Link to this definition")     
Execute a SQL command and return a string representing the results.
If the statement returns rows, a string of the results is returned. If the statement returns no rows, an empty string is returned.
If the statement throws an error, the error message is returned. 

Parameters:
    
  * **command** (_str_)
  * **fetch** (_Literal_ _[__'all'__,__'one'__]_)
  * **include_columns** (_bool_)
  * **parameters** (_Dict_ _[__str_ _,__Any_ _]__|__None_)
  * **execution_options** (_Dict_ _[__str_ _,__Any_ _]__|__None_)



Return type:
    
str | _Sequence_[_Dict_[str, _Any_]] | _Result_[_Any_]
Examples using SQLDatabase
  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)
  * [CnosDB](https://python.langchain.com/docs/integrations/providers/cnosdb/)
  * [How to better prompt when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_prompting/)
  * [How to deal with large databases when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_large_db/)
  * [How to do query validation as part of SQL question-answering](https://python.langchain.com/docs/how_to/sql_query_checking/)
  * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)
  * [Rebuff](https://python.langchain.com/docs/integrations/providers/rebuff/)
  * [SQLDatabase Toolkit](https://python.langchain.com/docs/integrations/tools/sql_database/)


On this page 
  * [`SQLDatabase`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase)
    * [`__init__()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.__init__)
    * [`from_cnosdb()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_cnosdb)
    * [`from_databricks()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_databricks)
    * [`from_uri()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.from_uri)
    * [`get_context()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_context)
    * [`get_table_info()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_info)
    * [`get_table_info_no_throw()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_info_no_throw)
    * [`get_table_names()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_table_names)
    * [`get_usable_table_names()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.get_usable_table_names)
    * [`run()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.run)
    * [`run_no_throw()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase.run_no_throw)


© Copyright 2025, LangChain Inc. 
  *[*]: Keyword-only parameters separator (PEP 3102)

