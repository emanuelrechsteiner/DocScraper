---
url: https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html
scraped_at: 2025-05-25T18:14:13.883262
title: GoogleSearchAPIWrapper — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#main-content)
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
  * GoogleSearchAPIWrapper


# GoogleSearchAPIWrapper[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#googlesearchapiwrapper "Link to this heading") 

_class_ langchain_community.utilities.google_search.GoogleSearchAPIWrapper[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_search.html#GoogleSearchAPIWrapper)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper "Link to this definition")
    
Bases: `BaseModel`
Deprecated since version 0.0.33: Use `:class:`~langchain_google_community.GoogleSearchAPIWrapper`` instead. It will not be removed until langchain-community==1.0.
Wrapper for Google Search API.
Adapted from: Instructions adapted from <https://stackoverflow.com/questions/> 37083058/ programmatically-searching-google-in-python-using-custom-search
TODO: DOCS for using it 1. Install google-api-python-client - If you don’t already have a Google account, sign up. - If you have never created a Google APIs Console project, read the Managing Projects page and create a project in the Google API Console. - Install the library using pip install google-api-python-client
2. Enable the Custom Search API - Navigate to the APIs & Services→Dashboard panel in Cloud Console. - Click Enable APIs and Services. - Search for Custom Search API and click on it. - Click Enable. URL for it: <https://console.cloud.google.com/apis/library/customsearch.googleapis> .com
3. To create an API key: - Navigate to the APIs & Services → Credentials panel in Cloud Console. - Select Create credentials, then select API key from the drop-down menu. - The API key created dialog box displays your newly created key. - You now have an API_KEY
Alternatively, you can just generate an API key here: <https://developers.google.com/custom-search/docs/paid_element#api_key>
4. Setup Custom Search Engine so you can search the entire web - Create a custom search engine here: <https://programmablesearchengine.google.com/>. - In What to search to search, pick the Search the entire Web option. After search engine is created, you can click on it and find Search engine ID
> on the Overview page.
Create a new model by parsing and validating input data from keyword arguments.
Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.
self is explicitly positional-only to allow self as a field name. 

_param_ google_api_key _: str|None_ _= None_[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.google_api_key "Link to this definition")


_param_ google_cse_id _: str|None_ _= None_[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.google_cse_id "Link to this definition")


_param_ k _: int_ _= 10_[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.k "Link to this definition")


_param_ siterestrict _: bool_ _= False_[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.siterestrict "Link to this definition")


results( 
    _query :str_,     _num_results :int_,     _search_params :Dict[str,str]|None=None_, ) → List[Dict][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_search.html#GoogleSearchAPIWrapper.results)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.results "Link to this definition")     
Run query through GoogleSearch and return metadata. 

Parameters:
    
  * **query** (_str_) – The query to search for.
  * **num_results** (_int_) – The number of results to return.
  * **search_params** (_Dict_ _[__str_ _,__str_ _]__|__None_) – Parameters to be passed on search



Returns:
    
snippet - The description of the result. title - The title of the result. link - The link to the result. 

Return type:
    
A list of dictionaries with the following keys 

run(_query :str_) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_search.html#GoogleSearchAPIWrapper.run)[#](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.run "Link to this definition")
    
Run query through GoogleSearch and parse result. 

Parameters:
    
**query** (_str_) 

Return type:
    
str
Examples using GoogleSearchAPIWrapper
  * [Bittensor](https://python.langchain.com/docs/integrations/llms/bittensor/)


On this page 
  * [`GoogleSearchAPIWrapper`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper)
    * [`google_api_key`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.google_api_key)
    * [`google_cse_id`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.google_cse_id)
    * [`k`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.k)
    * [`siterestrict`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.siterestrict)
    * [`results()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.results)
    * [`run()`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_search.GoogleSearchAPIWrapper.html#langchain_community.utilities.google_search.GoogleSearchAPIWrapper.run)


© Copyright 2025, LangChain Inc. 

