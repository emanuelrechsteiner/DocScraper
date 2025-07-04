---
url: https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html
scraped_at: 2025-05-25T18:15:04.185244
title: DropboxLoader — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#main-content)
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
      * [AcreomLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.acreom.AcreomLoader.html)
      * [AirbyteCDKLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteCDKLoader.html)
      * [AirbyteGongLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteGongLoader.html)
      * [AirbyteHubspotLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteHubspotLoader.html)
      * [AirbyteSalesforceLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteSalesforceLoader.html)
      * [AirbyteShopifyLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteShopifyLoader.html)
      * [AirbyteStripeLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteStripeLoader.html)
      * [AirbyteTypeformLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteTypeformLoader.html)
      * [AirbyteZendeskSupportLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteZendeskSupportLoader.html)
      * [AirbyteJSONLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte_json.AirbyteJSONLoader.html)
      * [AirtableLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airtable.AirtableLoader.html)
      * [ArcGISLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.arcgis_loader.ArcGISLoader.html)
      * [ArxivLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.arxiv.ArxivLoader.html)
      * [AssemblyAIAudioLoaderById](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.AssemblyAIAudioLoaderById.html)
      * [AssemblyAIAudioTranscriptLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.AssemblyAIAudioTranscriptLoader.html)
      * [TranscriptFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html)
      * [AsyncHtmlLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.async_html.AsyncHtmlLoader.html)
      * [AthenaLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.athena.AthenaLoader.html)
      * [AZLyricsLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azlyrics.AZLyricsLoader.html)
      * [AzureAIDataLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azure_ai_data.AzureAIDataLoader.html)
      * [AzureBlobStorageContainerLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azure_blob_storage_container.AzureBlobStorageContainerLoader.html)
      * [AzureBlobStorageFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azure_blob_storage_file.AzureBlobStorageFileLoader.html)
      * [BaiduBOSDirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.baiducloud_bos_directory.BaiduBOSDirectoryLoader.html)
      * [BaiduBOSFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.baiducloud_bos_file.BaiduBOSFileLoader.html)
      * [O365BaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.base_o365.O365BaseLoader.html)
      * [BibtexLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.bibtex.BibtexLoader.html)
      * [BiliBiliLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.bilibili.BiliBiliLoader.html)
      * [BlackboardLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blackboard.BlackboardLoader.html)
      * [CloudBlobLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blob_loaders.cloud_blob_loader.CloudBlobLoader.html)
      * [FileSystemBlobLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blob_loaders.file_system.FileSystemBlobLoader.html)
      * [YoutubeAudioLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blob_loaders.youtube_audio.YoutubeAudioLoader.html)
      * [BlockchainDocumentLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blockchain.BlockchainDocumentLoader.html)
      * [BlockchainType](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blockchain.BlockchainType.html)
      * [BraveSearchLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.brave_search.BraveSearchLoader.html)
      * [BrowserbaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.browserbase.BrowserbaseLoader.html)
      * [BrowserlessLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.browserless.BrowserlessLoader.html)
      * [CassandraLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.cassandra.CassandraLoader.html)
      * [ChatGPTLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.chatgpt.ChatGPTLoader.html)
      * [CHMParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.chm.CHMParser.html)
      * [UnstructuredCHMLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.chm.UnstructuredCHMLoader.html)
      * [AsyncChromiumLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.chromium.AsyncChromiumLoader.html)
      * [CollegeConfidentialLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.college_confidential.CollegeConfidentialLoader.html)
      * [ConcurrentLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.concurrent.ConcurrentLoader.html)
      * [ConfluenceLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ConfluenceLoader.html)
      * [ContentFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.confluence.ContentFormat.html)
      * [CoNLLULoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.conllu.CoNLLULoader.html)
      * [CouchbaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.couchbase.CouchbaseLoader.html)
      * [CSVLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.csv_loader.CSVLoader.html)
      * [UnstructuredCSVLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.csv_loader.UnstructuredCSVLoader.html)
      * [CubeSemanticLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.cube_semantic.CubeSemanticLoader.html)
      * [DatadogLogsLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.datadog_logs.DatadogLogsLoader.html)
      * [BaseDataFrameLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dataframe.BaseDataFrameLoader.html)
      * [DataFrameLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dataframe.DataFrameLoader.html)
      * [DedocAPIFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dedoc.DedocAPIFileLoader.html)
      * [DedocBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dedoc.DedocBaseLoader.html)
      * [DedocFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dedoc.DedocFileLoader.html)
      * [DiffbotLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.diffbot.DiffbotLoader.html)
      * [DirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.directory.DirectoryLoader.html)
      * [DiscordChatLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.discord.DiscordChatLoader.html)
      * [AzureAIDocumentIntelligenceLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.doc_intelligence.AzureAIDocumentIntelligenceLoader.html)
      * [DocusaurusLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.docusaurus.DocusaurusLoader.html)
      * [DropboxLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html)
      * [DuckDBLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.duckdb_loader.DuckDBLoader.html)
      * [OutlookMessageLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.email.OutlookMessageLoader.html)
      * [UnstructuredEmailLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.email.UnstructuredEmailLoader.html)
      * [UnstructuredEPubLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.epub.UnstructuredEPubLoader.html)
      * [EtherscanLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.etherscan.EtherscanLoader.html)
      * [EverNoteLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.evernote.EverNoteLoader.html)
      * [UnstructuredExcelLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.excel.UnstructuredExcelLoader.html)
      * [FacebookChatLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.facebook_chat.FacebookChatLoader.html)
      * [FaunaLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.fauna.FaunaLoader.html)
      * [FigmaFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.figma.FigmaFileLoader.html)
      * [FireCrawlLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.firecrawl.FireCrawlLoader.html)
      * [GenericLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.generic.GenericLoader.html)
      * [GeoDataFrameLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.geodataframe.GeoDataFrameLoader.html)
      * [GitLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.git.GitLoader.html)
      * [GitbookLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.gitbook.GitbookLoader.html)
      * [BaseGitHubLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.github.BaseGitHubLoader.html)
      * [GitHubIssuesLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.github.GitHubIssuesLoader.html)
      * [GithubFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.github.GithubFileLoader.html)
      * [GlueCatalogLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.glue_catalog.GlueCatalogLoader.html)
      * [GutenbergLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.gutenberg.GutenbergLoader.html)
      * [FileEncoding](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.helpers.FileEncoding.html)
      * [HNLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.hn.HNLoader.html)
      * [UnstructuredHTMLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.html.UnstructuredHTMLLoader.html)
      * [BSHTMLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html)
      * [HuggingFaceDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.hugging_face_dataset.HuggingFaceDatasetLoader.html)
      * [HuggingFaceModelLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.hugging_face_model.HuggingFaceModelLoader.html)
      * [IFixitLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.ifixit.IFixitLoader.html)
      * [UnstructuredImageLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.image.UnstructuredImageLoader.html)
      * [ImageCaptionLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.image_captions.ImageCaptionLoader.html)
      * [IMSDbLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.imsdb.IMSDbLoader.html)
      * [IuguLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.iugu.IuguLoader.html)
      * [JoplinLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.joplin.JoplinLoader.html)
      * [JSONLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.json_loader.JSONLoader.html)
      * [KineticaLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.kinetica_loader.KineticaLoader.html)
      * [LakeFSClient](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.lakefs.LakeFSClient.html)
      * [LakeFSLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.lakefs.LakeFSLoader.html)
      * [UnstructuredLakeFSLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.lakefs.UnstructuredLakeFSLoader.html)
      * [LarkSuiteDocLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.larksuite.LarkSuiteDocLoader.html)
      * [LarkSuiteWikiLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.larksuite.LarkSuiteWikiLoader.html)
      * [LLMSherpaFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.llmsherpa.LLMSherpaFileLoader.html)
      * [UnstructuredMarkdownLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.markdown.UnstructuredMarkdownLoader.html)
      * [MastodonTootsLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mastodon.MastodonTootsLoader.html)
      * [MaxComputeLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.max_compute.MaxComputeLoader.html)
      * [MWDumpLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mediawikidump.MWDumpLoader.html)
      * [MergedDataLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.merge.MergedDataLoader.html)
      * [MHTMLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mhtml.MHTMLLoader.html)
      * [MintbaseDocumentLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mintbase.MintbaseDocumentLoader.html)
      * [ModernTreasuryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.modern_treasury.ModernTreasuryLoader.html)
      * [MongodbLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mongodb.MongodbLoader.html)
      * [NeedleLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.needle.NeedleLoader.html)
      * [NewsURLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.news.NewsURLLoader.html)
      * [NotebookLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notebook.NotebookLoader.html)
      * [NotionDirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notion.NotionDirectoryLoader.html)
      * [NotionDBLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notiondb.NotionDBLoader.html)
      * [NucliaLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.nuclia.NucliaLoader.html)
      * [OBSDirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.obs_directory.OBSDirectoryLoader.html)
      * [OBSFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.obs_file.OBSFileLoader.html)
      * [ObsidianLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.obsidian.ObsidianLoader.html)
      * [UnstructuredODTLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.odt.UnstructuredODTLoader.html)
      * [OneDriveLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.onedrive.OneDriveLoader.html)
      * [OneDriveFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.onedrive_file.OneDriveFileLoader.html)
      * [OneNoteLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.onenote.OneNoteLoader.html)
      * [OpenCityDataLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.open_city_data.OpenCityDataLoader.html)
      * [OracleAutonomousDatabaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.oracleadb_loader.OracleAutonomousDatabaseLoader.html)
      * [OracleDocLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.oracleai.OracleDocLoader.html)
      * [OracleDocReader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.oracleai.OracleDocReader.html)
      * [OracleTextSplitter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.oracleai.OracleTextSplitter.html)
      * [ParseOracleDocMetadata](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.oracleai.ParseOracleDocMetadata.html)
      * [UnstructuredOrgModeLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.org_mode.UnstructuredOrgModeLoader.html)
      * [AzureOpenAIWhisperParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.AzureOpenAIWhisperParser.html)
      * [FasterWhisperParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.FasterWhisperParser.html)
      * [OpenAIWhisperParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.OpenAIWhisperParser.html)
      * [OpenAIWhisperParserLocal](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.OpenAIWhisperParserLocal.html)
      * [YandexSTTParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.YandexSTTParser.html)
      * [AzureAIDocumentIntelligenceParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.doc_intelligence.AzureAIDocumentIntelligenceParser.html)
      * [DocAIParsingResults](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.docai.DocAIParsingResults.html)
      * [DocumentLoaderAsParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.documentloader_adapter.DocumentLoaderAsParser.html)
      * [MimeTypeBasedParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.generic.MimeTypeBasedParser.html)
      * [GrobidParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.grobid.GrobidParser.html)
      * [ServerUnavailableException](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.grobid.ServerUnavailableException.html)
      * [BS4HTMLParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.html.bs4.BS4HTMLParser.html)
      * [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html)
      * [LLMImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.LLMImageBlobParser.html)
      * [RapidOCRBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.RapidOCRBlobParser.html)
      * [TesseractBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.TesseractBlobParser.html)
      * [CSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.c.CSegmenter.html)
      * [CobolSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.cobol.CobolSegmenter.html)
      * [CodeSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.code_segmenter.CodeSegmenter.html)
      * [CPPSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.cpp.CPPSegmenter.html)
      * [CSharpSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.csharp.CSharpSegmenter.html)
      * [ElixirSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.elixir.ElixirSegmenter.html)
      * [GoSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.go.GoSegmenter.html)
      * [JavaSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.java.JavaSegmenter.html)
      * [JavaScriptSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.javascript.JavaScriptSegmenter.html)
      * [KotlinSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.kotlin.KotlinSegmenter.html)
      * [LanguageParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.language_parser.LanguageParser.html)
      * [LuaSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.lua.LuaSegmenter.html)
      * [PerlSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.perl.PerlSegmenter.html)
      * [PHPSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.php.PHPSegmenter.html)
      * [PythonSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.python.PythonSegmenter.html)
      * [RubySegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.ruby.RubySegmenter.html)
      * [RustSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.rust.RustSegmenter.html)
      * [ScalaSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.scala.ScalaSegmenter.html)
      * [SQLSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.sql.SQLSegmenter.html)
      * [TreeSitterSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.tree_sitter_segmenter.TreeSitterSegmenter.html)
      * [TypeScriptSegmenter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.typescript.TypeScriptSegmenter.html)
      * [MsWordParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.msword.MsWordParser.html)
      * [AmazonTextractPDFParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.AmazonTextractPDFParser.html)
      * [DocumentIntelligenceParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.DocumentIntelligenceParser.html)
      * [PDFMinerParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PDFMinerParser.html)
      * [PDFPlumberParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PDFPlumberParser.html)
      * [PyMuPDFParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PyMuPDFParser.html)
      * [PyPDFParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PyPDFParser.html)
      * [PyPDFium2Parser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PyPDFium2Parser.html)
      * [TextParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.txt.TextParser.html)
      * [VsdxParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.vsdx.VsdxParser.html)
      * [AmazonTextractPDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.AmazonTextractPDFLoader.html)
      * [BasePDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.BasePDFLoader.html)
      * [DedocPDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.DedocPDFLoader.html)
      * [DocumentIntelligenceLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.DocumentIntelligenceLoader.html)
      * [MathpixPDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.MathpixPDFLoader.html)
      * [OnlinePDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.OnlinePDFLoader.html)
      * [PDFMinerLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PDFMinerLoader.html)
      * [PDFMinerPDFasHTMLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PDFMinerPDFasHTMLLoader.html)
      * [PDFPlumberLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PDFPlumberLoader.html)
      * [PagedPDFSplitter](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PagedPDFSplitter.html)
      * [PyMuPDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PyMuPDFLoader.html)
      * [PyPDFDirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PyPDFDirectoryLoader.html)
      * [PyPDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PyPDFLoader.html)
      * [PyPDFium2Loader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PyPDFium2Loader.html)
      * [UnstructuredPDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.UnstructuredPDFLoader.html)
      * [ZeroxPDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.ZeroxPDFLoader.html)
      * [PebbloSafeLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pebblo.PebbloSafeLoader.html)
      * [PebbloTextLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pebblo.PebbloTextLoader.html)
      * [PolarsDataFrameLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.polars_dataframe.PolarsDataFrameLoader.html)
      * [UnstructuredPowerPointLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.powerpoint.UnstructuredPowerPointLoader.html)
      * [PsychicLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.psychic.PsychicLoader.html)
      * [PubMedLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pubmed.PubMedLoader.html)
      * [PySparkDataFrameLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pyspark_dataframe.PySparkDataFrameLoader.html)
      * [PythonLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.python.PythonLoader.html)
      * [QuipLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.quip.QuipLoader.html)
      * [ReadTheDocsLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.readthedocs.ReadTheDocsLoader.html)
      * [RecursiveUrlLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.recursive_url_loader.RecursiveUrlLoader.html)
      * [RedditPostsLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.reddit.RedditPostsLoader.html)
      * [RoamLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.roam.RoamLoader.html)
      * [ColumnNotFoundError](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rocksetdb.ColumnNotFoundError.html)
      * [RocksetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rocksetdb.RocksetLoader.html)
      * [RSpaceLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rspace.RSpaceLoader.html)
      * [RSSFeedLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rss.RSSFeedLoader.html)
      * [UnstructuredRSTLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rst.UnstructuredRSTLoader.html)
      * [UnstructuredRTFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rtf.UnstructuredRTFLoader.html)
      * [S3DirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.s3_directory.S3DirectoryLoader.html)
      * [S3FileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.s3_file.S3FileLoader.html)
      * [ScrapflyLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.scrapfly.ScrapflyLoader.html)
      * [ScrapingAntLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.scrapingant.ScrapingAntLoader.html)
      * [SharePointLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.sharepoint.SharePointLoader.html)
      * [SitemapLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.sitemap.SitemapLoader.html)
      * [SlackDirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.slack_directory.SlackDirectoryLoader.html)
      * [SnowflakeLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.snowflake_loader.SnowflakeLoader.html)
      * [SpiderLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.spider.SpiderLoader.html)
      * [SpreedlyLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.spreedly.SpreedlyLoader.html)
      * [SQLDatabaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.sql_database.SQLDatabaseLoader.html)
      * [SRTLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.srt.SRTLoader.html)
      * [StripeLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.stripe.StripeLoader.html)
      * [SurrealDBLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.surrealdb.SurrealDBLoader.html)
      * [TelegramChatApiLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.telegram.TelegramChatApiLoader.html)
      * [TelegramChatFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.telegram.TelegramChatFileLoader.html)
      * [TelegramChatLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.telegram.TelegramChatLoader.html)
      * [TencentCOSDirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tencent_cos_directory.TencentCOSDirectoryLoader.html)
      * [TencentCOSFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tencent_cos_file.TencentCOSFileLoader.html)
      * [TensorflowDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tensorflow_datasets.TensorflowDatasetLoader.html)
      * [TextLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.text.TextLoader.html)
      * [TiDBLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tidb.TiDBLoader.html)
      * [ToMarkdownLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tomarkdown.ToMarkdownLoader.html)
      * [TomlLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.toml.TomlLoader.html)
      * [TrelloLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.trello.TrelloLoader.html)
      * [UnstructuredTSVLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tsv.UnstructuredTSVLoader.html)
      * [TwitterTweetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.twitter.TwitterTweetLoader.html)
      * [UnstructuredBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredBaseLoader.html)
      * [UnstructuredURLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url.UnstructuredURLLoader.html)
      * [PlaywrightEvaluator](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.PlaywrightEvaluator.html)
      * [PlaywrightURLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.PlaywrightURLLoader.html)
      * [UnstructuredHtmlEvaluator](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.UnstructuredHtmlEvaluator.html)
      * [SeleniumURLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_selenium.SeleniumURLLoader.html)
      * [VsdxLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.vsdx.VsdxLoader.html)
      * [WeatherDataLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.weather.WeatherDataLoader.html)
      * [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html)
      * [WhatsAppChatLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.whatsapp_chat.WhatsAppChatLoader.html)
      * [WikipediaLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.wikipedia.WikipediaLoader.html)
      * [Docx2txtLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.word_document.Docx2txtLoader.html)
      * [UnstructuredWordDocumentLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.word_document.UnstructuredWordDocumentLoader.html)
      * [UnstructuredXMLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.xml.UnstructuredXMLLoader.html)
      * [XorbitsLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.xorbits.XorbitsLoader.html)
      * [GoogleApiClient](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.GoogleApiClient.html)
      * [GoogleApiYoutubeLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.GoogleApiYoutubeLoader.html)
      * [TranscriptFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.TranscriptFormat.html)
      * [YoutubeLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.YoutubeLoader.html)
      * [YuqueLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.yuque.YuqueLoader.html)
      * [fetch_extensions](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.base_o365.fetch_extensions.html)
      * [fetch_mime_types](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.base_o365.fetch_mime_types.html)
      * [concatenate_rows](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.chatgpt.concatenate_rows.html)
      * [concatenate_rows](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.facebook_chat.concatenate_rows.html)
      * [detect_file_encodings](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.helpers.detect_file_encodings.html)
      * [concatenate_cells](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notebook.concatenate_cells.html)
      * [remove_newlines](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notebook.remove_newlines.html)
      * [extract_from_images_with_rapidocr](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.extract_from_images_with_rapidocr.html)
      * [get_parser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.registry.get_parser.html)
      * [default_joiner](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rocksetdb.default_joiner.html)
      * [concatenate_rows](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.telegram.concatenate_rows.html)
      * [text_to_docs](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.telegram.text_to_docs.html)
      * [get_elements_from_api](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.get_elements_from_api.html)
      * [satisfies_min_unstructured_version](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.satisfies_min_unstructured_version.html)
      * [validate_unstructured_version](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.validate_unstructured_version.html)
      * [concatenate_rows](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.whatsapp_chat.concatenate_rows.html)
      * [ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html)
      * [AstraDBLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.astradb.AstraDBLoader.html)
      * [BigQueryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.bigquery.BigQueryLoader.html)
      * [DocugamiLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.docugami.DocugamiLoader.html)
      * [GCSDirectoryLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.gcs_directory.GCSDirectoryLoader.html)
      * [GCSFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.gcs_file.GCSFileLoader.html)
      * [GoogleSpeechToTextLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.google_speech_to_text.GoogleSpeechToTextLoader.html)
      * [GoogleDriveLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.googledrive.GoogleDriveLoader.html)
      * [DocAIParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.docai.DocAIParser.html)
      * [UnstructuredAPIFileIOLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredAPIFileIOLoader.html)
      * [UnstructuredAPIFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredAPIFileLoader.html)
      * [UnstructuredFileIOLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredFileIOLoader.html)
      * [UnstructuredFileLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredFileLoader.html)
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
  * [`document_loaders`](https://python.langchain.com/api_reference/community/document_loaders.html)
  * DropboxLoader


# DropboxLoader[#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#dropboxloader "Link to this heading") 

_class_ langchain_community.document_loaders.dropbox.DropboxLoader[[source]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/dropbox.html#DropboxLoader)[#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader "Link to this definition")
    
Bases: [`BaseLoader`](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader"), `BaseModel`
Load files from Dropbox.
In addition to common files such as text and PDF files, it also supports _Dropbox Paper_ files.
Create a new model by parsing and validating input data from keyword arguments.
Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.
self is explicitly positional-only to allow self as a field name. 

_param_ dropbox_access_token _: str_ _[Required]_[#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.dropbox_access_token "Link to this definition")
    
Dropbox access token. 

_param_ dropbox_file_paths _: List[str]|None_ _= None_[#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.dropbox_file_paths "Link to this definition")
    
The file paths to load from. 

_param_ dropbox_folder_path _: str|None_ _= None_[#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.dropbox_folder_path "Link to this definition")
    
The folder path to load from. 

_param_ recursive _: bool_ _= False_[#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.recursive "Link to this definition")
    
Flag to indicate whether to load files recursively from subfolders. 

_async_ alazy_load() → AsyncIterator[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.alazy_load "Link to this definition")
    
A lazy loader for Documents. 

Return type:
    
AsyncIterator[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")] 

_async_ aload() → list[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.aload "Link to this definition")
    
Load data into Document objects. 

Return type:
    
list[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")] 

lazy_load() → Iterator[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.lazy_load "Link to this definition")
    
A lazy loader for Documents. 

Return type:
    
Iterator[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")] 

load() → List[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/dropbox.html#DropboxLoader.load)[#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.load "Link to this definition")
    
Load documents. 

Return type:
    
_List_[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")] 

load_and_split( 
    _text_splitter :[TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")|None=None_, ) → list[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][#](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.load_and_split "Link to this definition")     
Load Documents and split into chunks. Chunks are returned as Documents.
Do not override this method. It should be considered to be deprecated! 

Parameters:
    
**text_splitter** (_Optional_ _[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _]_) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter. 

Returns:
    
List of Documents. 

Return type:
    
list[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")]
Examples using DropboxLoader
  * [Dropbox](https://python.langchain.com/docs/integrations/document_loaders/dropbox/)


On this page 
  * [`DropboxLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader)
    * [`dropbox_access_token`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.dropbox_access_token)
    * [`dropbox_file_paths`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.dropbox_file_paths)
    * [`dropbox_folder_path`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.dropbox_folder_path)
    * [`recursive`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.recursive)
    * [`alazy_load()`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.alazy_load)
    * [`aload()`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.aload)
    * [`lazy_load()`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.lazy_load)
    * [`load()`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.load)
    * [`load_and_split()`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dropbox.DropboxLoader.html#langchain_community.document_loaders.dropbox.DropboxLoader.load_and_split)


© Copyright 2025, LangChain Inc. 

