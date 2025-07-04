---
url: https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_tools.html
scraped_at: 2025-05-25T18:03:33.581683
title: load_tools — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_tools.html#main-content)
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
      * [AINetworkToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.ainetwork.toolkit.AINetworkToolkit.html)
      * [AmadeusToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.amadeus.toolkit.AmadeusToolkit.html)
      * [AzureAiServicesToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.azure_ai_services.AzureAiServicesToolkit.html)
      * [AzureCognitiveServicesToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.azure_cognitive_services.AzureCognitiveServicesToolkit.html)
      * [CassandraDatabaseToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.cassandra_database.toolkit.CassandraDatabaseToolkit.html)
      * [ClickupToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.clickup.toolkit.ClickupToolkit.html)
      * [CogniswitchToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.cogniswitch.toolkit.CogniswitchToolkit.html)
      * [ConneryToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.connery.toolkit.ConneryToolkit.html)
      * [FileManagementToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.file_management.toolkit.FileManagementToolkit.html)
      * [FinancialDatasetsToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.financial_datasets.toolkit.FinancialDatasetsToolkit.html)
      * [BranchName](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.BranchName.html)
      * [CommentOnIssue](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.CommentOnIssue.html)
      * [CreateFile](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.CreateFile.html)
      * [CreatePR](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.CreatePR.html)
      * [CreateReviewRequest](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.CreateReviewRequest.html)
      * [DeleteFile](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.DeleteFile.html)
      * [DirectoryPath](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.DirectoryPath.html)
      * [GetIssue](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.GetIssue.html)
      * [GetPR](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.GetPR.html)
      * [GitHubToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.GitHubToolkit.html)
      * [NoInput](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.NoInput.html)
      * [ReadFile](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.ReadFile.html)
      * [SearchCode](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.SearchCode.html)
      * [SearchIssuesAndPRs](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.SearchIssuesAndPRs.html)
      * [TagName](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.TagName.html)
      * [UpdateFile](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.UpdateFile.html)
      * [GitLabToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.gitlab.toolkit.GitLabToolkit.html)
      * [GmailToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.gmail.toolkit.GmailToolkit.html)
      * [JiraToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.jira.toolkit.JiraToolkit.html)
      * [JsonToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.json.toolkit.JsonToolkit.html)
      * [MultionToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.multion.toolkit.MultionToolkit.html)
      * [NasaToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.nasa.toolkit.NasaToolkit.html)
      * [NLATool](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.nla.tool.NLATool.html)
      * [NLAToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.nla.toolkit.NLAToolkit.html)
      * [O365Toolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.office365.toolkit.O365Toolkit.html)
      * [RequestsDeleteToolWithParsing](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.planner.RequestsDeleteToolWithParsing.html)
      * [RequestsGetToolWithParsing](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.planner.RequestsGetToolWithParsing.html)
      * [RequestsPatchToolWithParsing](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.planner.RequestsPatchToolWithParsing.html)
      * [RequestsPostToolWithParsing](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.planner.RequestsPostToolWithParsing.html)
      * [RequestsPutToolWithParsing](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.planner.RequestsPutToolWithParsing.html)
      * [ReducedOpenAPISpec](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec.html)
      * [OpenAPIToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.toolkit.OpenAPIToolkit.html)
      * [RequestsToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.toolkit.RequestsToolkit.html)
      * [PlayWrightBrowserToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.playwright.toolkit.PlayWrightBrowserToolkit.html)
      * [PolygonToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.polygon.toolkit.PolygonToolkit.html)
      * [PowerBIToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit.html)
      * [SlackToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.slack.toolkit.SlackToolkit.html)
      * [SparkSQLToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.spark_sql.toolkit.SparkSQLToolkit.html)
      * [SQLDatabaseToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit.html)
      * [SteamToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.steam.toolkit.SteamToolkit.html)
      * [ZapierToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.zapier.toolkit.ZapierToolkit.html)
      * [create_json_agent](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.json.base.create_json_agent.html)
      * [get_all_tool_names](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.get_all_tool_names.html)
      * [load_huggingface_tool](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_huggingface_tool.html)
      * [load_tools](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_tools.html)
      * [raise_dangerous_tools_exception](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.raise_dangerous_tools_exception.html)
      * [create_openapi_agent](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.base.create_openapi_agent.html)
      * [create_openapi_agent](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.planner.create_openapi_agent.html)
      * [reduce_openapi_spec](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.spec.reduce_openapi_spec.html)
      * [create_pbi_agent](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.base.create_pbi_agent.html)
      * [create_pbi_chat_agent](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.chat_base.create_pbi_chat_agent.html)
      * [create_spark_sql_agent](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.spark_sql.base.create_spark_sql_agent.html)
      * [create_sql_agent](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.sql.base.create_sql_agent.html)
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
  * [`agent_toolkits`](https://python.langchain.com/api_reference/community/agent_toolkits.html)
  * load_tools


# load_tools[#](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_tools.html#load-tools "Link to this heading") 

langchain_community.agent_toolkits.load_tools.load_tools( 
    _tool_names :List[str]_,     _llm :[BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")|None=None_,     _callbacks :list[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")]|[BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")|None=None_,     _allow_dangerous_tools :bool=False_,     _** kwargs:Any_, ) → List[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")][[source]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/load_tools.html#load_tools)[#](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_tools.html#langchain_community.agent_toolkits.load_tools.load_tools "Link to this definition")     
Load tools based on their name.
Tools allow agents to interact with various resources and services like APIs, databases, file systems, etc.
Please scope the permissions of each tools to the minimum required for the application.
For example, if an application only needs to read from a database, the database tool should not be given write permissions. Moreover consider scoping the permissions to only allow accessing specific tables and impose user-level quota for limiting resource usage.
Please read the APIs of the individual tools to determine which configuration they support.
See [Security](<https://python.langchain.com/docs/security>) for more information. 

Parameters:
    
  * **tool_names** (_List_ _[__str_ _]_) – name of tools to load.
  * **llm** ([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _|__None_) – An optional language model may be needed to initialize certain tools. Defaults to None.
  * **callbacks** (_list_ _[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_) – Optional callback manager or list of callback handlers. If not provided, default global callback manager will be used.
  * **allow_dangerous_tools** (_bool_) – Optional flag to allow dangerous tools. Tools that contain some level of risk. Please use with caution and read the documentation of these tools to understand the risks and how to mitigate them. Refer to <https://python.langchain.com/docs/security> for more information. Please note that this list may not be fully exhaustive. It is your responsibility to understand which tools you’re using and the risks associated with them. Defaults to False.
  * **kwargs** (_Any_) – Additional keyword arguments.



Returns:
    
List of tools. 

Raises:
    
  * **ValueError** – If the tool name is unknown.
  * **ValueError** – If the tool requires an LLM to be provided.
  * **ValueError** – If the tool requires some parameters that were not provided.
  * **ValueError** – If the tool is a dangerous tool and allow_dangerous_tools is False.



Return type:
    
_List_[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")]
Examples using load_tools
  * [AWS Lambda](https://python.langchain.com/docs/integrations/tools/awslambda/)
  * [Aim](https://python.langchain.com/docs/integrations/providers/aim_tracking/)
  * [Amazon API Gateway](https://python.langchain.com/docs/integrations/llms/amazon_api_gateway/)
  * [ArXiv](https://python.langchain.com/docs/integrations/tools/arxiv/)
  * [Argilla](https://python.langchain.com/docs/integrations/callbacks/argilla/)
  * [ChatGPT Plugins](https://python.langchain.com/docs/integrations/tools/chatgpt_plugins/)
  * [ClearML](https://python.langchain.com/docs/integrations/providers/clearml_tracking/)
  * [Comet](https://python.langchain.com/docs/integrations/providers/comet_tracking/)
  * [Comet Tracing](https://python.langchain.com/docs/integrations/callbacks/comet_tracing/)
  * [Dall-E Image Generator](https://python.langchain.com/docs/integrations/tools/dalle_image_generator/)
  * [DataForSEO](https://python.langchain.com/docs/integrations/providers/dataforseo/)
  * [Dataherald](https://python.langchain.com/docs/integrations/providers/dataherald/)
  * [Eleven Labs Text2Speech](https://python.langchain.com/docs/integrations/tools/eleven_labs_tts/)
  * [Flyte](https://python.langchain.com/docs/integrations/providers/flyte/)
  * [Golden](https://python.langchain.com/docs/integrations/providers/golden/)
  * [Google](https://python.langchain.com/docs/integrations/providers/google/)
  * [Google Drive](https://python.langchain.com/docs/integrations/tools/google_drive/)
  * [Google Finance](https://python.langchain.com/docs/integrations/tools/google_finance/)
  * [Google Jobs](https://python.langchain.com/docs/integrations/tools/google_jobs/)
  * [GraphQL](https://python.langchain.com/docs/integrations/tools/graphql/)
  * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)
  * [Human as a tool](https://python.langchain.com/docs/integrations/tools/human_tools/)
  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)
  * [MLX](https://python.langchain.com/docs/integrations/chat/mlx/)
  * [MLflow](https://python.langchain.com/docs/integrations/providers/mlflow_tracking/)
  * [Memorize](https://python.langchain.com/docs/integrations/tools/memorize/)
  * [OpenWeatherMap](https://python.langchain.com/docs/integrations/providers/openweathermap/)
  * [SageMaker Tracking](https://python.langchain.com/docs/integrations/callbacks/sagemaker_tracking/)
  * [SceneXplain](https://python.langchain.com/docs/integrations/tools/sceneXplain/)
  * [SearchApi](https://python.langchain.com/docs/integrations/providers/searchapi/)
  * [SearxNG Search API](https://python.langchain.com/docs/integrations/providers/searx/)
  * [SerpAPI](https://python.langchain.com/docs/integrations/providers/serpapi/)
  * [Serper - Google Search API](https://python.langchain.com/docs/integrations/providers/google_serper/)
  * [Stack Exchange](https://python.langchain.com/docs/integrations/providers/stackexchange/)
  * [Streamlit](https://python.langchain.com/docs/integrations/callbacks/streamlit/)
  * [WandB Tracing](https://python.langchain.com/docs/integrations/providers/wandb_tracing/)
  * [Weights & Biases](https://python.langchain.com/docs/integrations/providers/wandb_tracking/)
  * [Wolfram Alpha](https://python.langchain.com/docs/integrations/providers/wolfram_alpha/)


On this page 
  * [`load_tools()`](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_tools.html#langchain_community.agent_toolkits.load_tools.load_tools)


© Copyright 2025, LangChain Inc. 

