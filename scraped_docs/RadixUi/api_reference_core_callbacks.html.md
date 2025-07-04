---
url: https://python.langchain.com/api_reference/core/callbacks.html
scraped_at: 2025-05-25T18:16:12.197875
title: callbacks — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/core/callbacks.html#main-content)
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
    * [`agents`](https://python.langchain.com/api_reference/core/agents.html)
    * [`beta`](https://python.langchain.com/api_reference/core/beta.html)
    * [`caches`](https://python.langchain.com/api_reference/core/caches.html)
    * [`callbacks`](https://python.langchain.com/api_reference/core/callbacks.html)
      * [AsyncCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.AsyncCallbackHandler.html)
      * [BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html)
      * [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html)
      * [CallbackManagerMixin](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.CallbackManagerMixin.html)
      * [ChainManagerMixin](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.ChainManagerMixin.html)
      * [LLMManagerMixin](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.LLMManagerMixin.html)
      * [RetrieverManagerMixin](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.RetrieverManagerMixin.html)
      * [RunManagerMixin](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.RunManagerMixin.html)
      * [ToolManagerMixin](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.ToolManagerMixin.html)
      * [FileCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.file.FileCallbackHandler.html)
      * [AsyncCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html)
      * [AsyncCallbackManagerForChainGroup](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup.html)
      * [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html)
      * [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html)
      * [AsyncCallbackManagerForRetrieverRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun.html)
      * [AsyncCallbackManagerForToolRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun.html)
      * [AsyncParentRunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncParentRunManager.html)
      * [AsyncRunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncRunManager.html)
      * [BaseRunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.BaseRunManager.html)
      * [CallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html)
      * [CallbackManagerForChainGroup](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainGroup.html)
      * [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html)
      * [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html)
      * [CallbackManagerForRetrieverRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForRetrieverRun.html)
      * [CallbackManagerForToolRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForToolRun.html)
      * [ParentRunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.ParentRunManager.html)
      * [RunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.RunManager.html)
      * [StdOutCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.stdout.StdOutCallbackHandler.html)
      * [StreamingStdOutCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.streaming_stdout.StreamingStdOutCallbackHandler.html)
      * [UsageMetadataCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.usage.UsageMetadataCallbackHandler.html)
      * [adispatch_custom_event](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.adispatch_custom_event.html)
      * [ahandle_event](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.ahandle_event.html)
      * [atrace_as_chain_group](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.atrace_as_chain_group.html)
      * [dispatch_custom_event](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.dispatch_custom_event.html)
      * [handle_event](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.handle_event.html)
      * [shielded](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.shielded.html)
      * [trace_as_chain_group](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.trace_as_chain_group.html)
      * [get_usage_metadata_callback](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.usage.get_usage_metadata_callback.html)
    * [`chat_history`](https://python.langchain.com/api_reference/core/chat_history.html)
    * [`chat_loaders`](https://python.langchain.com/api_reference/core/chat_loaders.html)
    * [`chat_sessions`](https://python.langchain.com/api_reference/core/chat_sessions.html)
    * [`document_loaders`](https://python.langchain.com/api_reference/core/document_loaders.html)
    * [`documents`](https://python.langchain.com/api_reference/core/documents.html)
    * [`embeddings`](https://python.langchain.com/api_reference/core/embeddings.html)
    * [`example_selectors`](https://python.langchain.com/api_reference/core/example_selectors.html)
    * [`exceptions`](https://python.langchain.com/api_reference/core/exceptions.html)
    * [`globals`](https://python.langchain.com/api_reference/core/globals.html)
    * [`indexing`](https://python.langchain.com/api_reference/core/indexing.html)
    * [`language_models`](https://python.langchain.com/api_reference/core/language_models.html)
    * [`load`](https://python.langchain.com/api_reference/core/load.html)
    * [`messages`](https://python.langchain.com/api_reference/core/messages.html)
    * [`output_parsers`](https://python.langchain.com/api_reference/core/output_parsers.html)
    * [`outputs`](https://python.langchain.com/api_reference/core/outputs.html)
    * [`prompt_values`](https://python.langchain.com/api_reference/core/prompt_values.html)
    * [`prompts`](https://python.langchain.com/api_reference/core/prompts.html)
    * [`rate_limiters`](https://python.langchain.com/api_reference/core/rate_limiters.html)
    * [`retrievers`](https://python.langchain.com/api_reference/core/retrievers.html)
    * [`runnables`](https://python.langchain.com/api_reference/core/runnables.html)
    * [`stores`](https://python.langchain.com/api_reference/core/stores.html)
    * [`structured_query`](https://python.langchain.com/api_reference/core/structured_query.html)
    * [`sys_info`](https://python.langchain.com/api_reference/core/sys_info.html)
    * [`tools`](https://python.langchain.com/api_reference/core/tools.html)
    * [`tracers`](https://python.langchain.com/api_reference/core/tracers.html)
    * [`utils`](https://python.langchain.com/api_reference/core/utils.html)
    * [`vectorstores`](https://python.langchain.com/api_reference/core/vectorstores.html)
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
  * [langchain-core: 0.3.61](https://python.langchain.com/api_reference/core/index.html)
  * `callbacks`


# `callbacks`[#](https://python.langchain.com/api_reference/core/callbacks.html#module-langchain_core.callbacks "Link to this heading")
**Callback handlers** allow listening to events in LangChain.
**Class hierarchy:**
```
BaseCallbackHandler --> <name>CallbackHandler # Example: AimCallbackHandler

```
Copy to clipboard
**Classes**
[`callbacks.base.AsyncCallbackHandler`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.AsyncCallbackHandler.html#langchain_core.callbacks.base.AsyncCallbackHandler "langchain_core.callbacks.base.AsyncCallbackHandler")() | Async callback handler for LangChain.  
---|---  
[`callbacks.base.BaseCallbackHandler`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")() | Base callback handler for LangChain.  
[`callbacks.base.BaseCallbackManager`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")(handlers) | Base callback manager for LangChain.  
[`callbacks.base.CallbackManagerMixin`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.CallbackManagerMixin.html#langchain_core.callbacks.base.CallbackManagerMixin "langchain_core.callbacks.base.CallbackManagerMixin")() | Mixin for callback manager.  
[`callbacks.base.ChainManagerMixin`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.ChainManagerMixin.html#langchain_core.callbacks.base.ChainManagerMixin "langchain_core.callbacks.base.ChainManagerMixin")() | Mixin for chain callbacks.  
[`callbacks.base.LLMManagerMixin`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.LLMManagerMixin.html#langchain_core.callbacks.base.LLMManagerMixin "langchain_core.callbacks.base.LLMManagerMixin")() | Mixin for LLM callbacks.  
[`callbacks.base.RetrieverManagerMixin`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.RetrieverManagerMixin.html#langchain_core.callbacks.base.RetrieverManagerMixin "langchain_core.callbacks.base.RetrieverManagerMixin")() | Mixin for Retriever callbacks.  
[`callbacks.base.RunManagerMixin`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.RunManagerMixin.html#langchain_core.callbacks.base.RunManagerMixin "langchain_core.callbacks.base.RunManagerMixin")() | Mixin for run manager.  
[`callbacks.base.ToolManagerMixin`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.ToolManagerMixin.html#langchain_core.callbacks.base.ToolManagerMixin "langchain_core.callbacks.base.ToolManagerMixin")() | Mixin for tool callbacks.  
[`callbacks.file.FileCallbackHandler`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.file.FileCallbackHandler.html#langchain_core.callbacks.file.FileCallbackHandler "langchain_core.callbacks.file.FileCallbackHandler")(filename) | Callback Handler that writes to a file.  
[`callbacks.manager.AsyncCallbackManager`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html#langchain_core.callbacks.manager.AsyncCallbackManager "langchain_core.callbacks.manager.AsyncCallbackManager")(handlers) | Async callback manager that handles callbacks from LangChain.  
[`callbacks.manager.AsyncCallbackManagerForChainGroup`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup "langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup")(...) | Async callback manager for the chain group.  
[`callbacks.manager.AsyncCallbackManagerForChainRun`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")(*, ...) | Async callback manager for chain run.  
[`callbacks.manager.AsyncCallbackManagerForLLMRun`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun")(*, ...) | Async callback manager for LLM run.  
[`callbacks.manager.AsyncCallbackManagerForRetrieverRun`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun "langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun")(*, ...) | Async callback manager for retriever run.  
[`callbacks.manager.AsyncCallbackManagerForToolRun`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun "langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun")(*, ...) | Async callback manager for tool run.  
[`callbacks.manager.AsyncParentRunManager`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncParentRunManager.html#langchain_core.callbacks.manager.AsyncParentRunManager "langchain_core.callbacks.manager.AsyncParentRunManager")(*, ...) | Async Parent Run Manager.  
[`callbacks.manager.AsyncRunManager`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncRunManager.html#langchain_core.callbacks.manager.AsyncRunManager "langchain_core.callbacks.manager.AsyncRunManager")(*, run_id, ...) | Async Run Manager.  
[`callbacks.manager.BaseRunManager`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.BaseRunManager.html#langchain_core.callbacks.manager.BaseRunManager "langchain_core.callbacks.manager.BaseRunManager")(*, run_id, ...) | Base class for run manager (a bound callback manager).  
[`callbacks.manager.CallbackManager`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager")(handlers) | Callback manager for LangChain.  
[`callbacks.manager.CallbackManagerForChainGroup`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainGroup.html#langchain_core.callbacks.manager.CallbackManagerForChainGroup "langchain_core.callbacks.manager.CallbackManagerForChainGroup")(...) | Callback manager for the chain group.  
[`callbacks.manager.CallbackManagerForChainRun`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun")(*, ...) | Callback manager for chain run.  
[`callbacks.manager.CallbackManagerForLLMRun`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun")(*, ...) | Callback manager for LLM run.  
[`callbacks.manager.CallbackManagerForRetrieverRun`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForRetrieverRun.html#langchain_core.callbacks.manager.CallbackManagerForRetrieverRun "langchain_core.callbacks.manager.CallbackManagerForRetrieverRun")(*, ...) | Callback manager for retriever run.  
[`callbacks.manager.CallbackManagerForToolRun`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForToolRun.html#langchain_core.callbacks.manager.CallbackManagerForToolRun "langchain_core.callbacks.manager.CallbackManagerForToolRun")(*, ...) | Callback manager for tool run.  
[`callbacks.manager.ParentRunManager`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.ParentRunManager.html#langchain_core.callbacks.manager.ParentRunManager "langchain_core.callbacks.manager.ParentRunManager")(*, ...[, ...]) | Sync Parent Run Manager.  
[`callbacks.manager.RunManager`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.RunManager.html#langchain_core.callbacks.manager.RunManager "langchain_core.callbacks.manager.RunManager")(*, run_id, ...) | Sync Run Manager.  
[`callbacks.stdout.StdOutCallbackHandler`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.stdout.StdOutCallbackHandler.html#langchain_core.callbacks.stdout.StdOutCallbackHandler "langchain_core.callbacks.stdout.StdOutCallbackHandler")([color]) | Callback Handler that prints to std out.  
[`callbacks.streaming_stdout.StreamingStdOutCallbackHandler`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.streaming_stdout.StreamingStdOutCallbackHandler.html#langchain_core.callbacks.streaming_stdout.StreamingStdOutCallbackHandler "langchain_core.callbacks.streaming_stdout.StreamingStdOutCallbackHandler")() | Callback handler for streaming.  
[`callbacks.usage.UsageMetadataCallbackHandler`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.usage.UsageMetadataCallbackHandler.html#langchain_core.callbacks.usage.UsageMetadataCallbackHandler "langchain_core.callbacks.usage.UsageMetadataCallbackHandler")() | Callback Handler that tracks AIMessage.usage_metadata.  
**Functions**
[`callbacks.manager.adispatch_custom_event`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.adispatch_custom_event.html#langchain_core.callbacks.manager.adispatch_custom_event "langchain_core.callbacks.manager.adispatch_custom_event")(...) | Dispatch an adhoc event to the handlers.  
---|---  
[`callbacks.manager.ahandle_event`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.ahandle_event.html#langchain_core.callbacks.manager.ahandle_event "langchain_core.callbacks.manager.ahandle_event")(handlers, ...) | Async generic event handler for AsyncCallbackManager.  
[`callbacks.manager.atrace_as_chain_group`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.atrace_as_chain_group.html#langchain_core.callbacks.manager.atrace_as_chain_group "langchain_core.callbacks.manager.atrace_as_chain_group")(...) | Get an async callback manager for a chain group in a context manager.  
[`callbacks.manager.dispatch_custom_event`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.dispatch_custom_event.html#langchain_core.callbacks.manager.dispatch_custom_event "langchain_core.callbacks.manager.dispatch_custom_event")(...) | Dispatch an adhoc event.  
[`callbacks.manager.handle_event`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.handle_event.html#langchain_core.callbacks.manager.handle_event "langchain_core.callbacks.manager.handle_event")(handlers, ...) | Generic event handler for CallbackManager.  
[`callbacks.manager.shielded`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.shielded.html#langchain_core.callbacks.manager.shielded "langchain_core.callbacks.manager.shielded")(func) | Makes so an awaitable method is always shielded from cancellation.  
[`callbacks.manager.trace_as_chain_group`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.trace_as_chain_group.html#langchain_core.callbacks.manager.trace_as_chain_group "langchain_core.callbacks.manager.trace_as_chain_group")(...) | Get a callback manager for a chain group in a context manager.  
[`callbacks.usage.get_usage_metadata_callback`](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.usage.get_usage_metadata_callback.html#langchain_core.callbacks.usage.get_usage_metadata_callback "langchain_core.callbacks.usage.get_usage_metadata_callback")([name]) | Get usage metadata callback.  
© Copyright 2025, LangChain Inc. 

