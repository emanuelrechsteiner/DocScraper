---
url: https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html
scraped_at: 2025-05-25T18:14:46.041493
title: BaseStreamEvent — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#main-content)
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
      * [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html)
      * [RunnableBinding](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableBinding.html)
      * [RunnableBindingBase](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableBindingBase.html)
      * [RunnableEach](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableEach.html)
      * [RunnableEachBase](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableEachBase.html)
      * [RunnableGenerator](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableGenerator.html)
      * [RunnableLambda](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html)
      * [RunnableMap](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableMap.html)
      * [RunnableParallel](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableParallel.html)
      * [RunnableSequence](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSequence.html)
      * [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html)
      * [RunnableBranch](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.branch.RunnableBranch.html)
      * [ContextThreadPoolExecutor](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.ContextThreadPoolExecutor.html)
      * [EmptyDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.EmptyDict.html)
      * [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)
      * [DynamicRunnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.configurable.DynamicRunnable.html)
      * [RunnableConfigurableAlternatives](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.configurable.RunnableConfigurableAlternatives.html)
      * [RunnableConfigurableFields](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.configurable.RunnableConfigurableFields.html)
      * [StrEnum](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.configurable.StrEnum.html)
      * [RunnableWithFallbacks](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.fallbacks.RunnableWithFallbacks.html)
      * [Branch](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Branch.html)
      * [CurveStyle](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.CurveStyle.html)
      * [Edge](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html)
      * [Graph](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html)
      * [LabelsDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.LabelsDict.html)
      * [MermaidDrawMethod](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.MermaidDrawMethod.html)
      * [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html)
      * [NodeStyles](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.NodeStyles.html)
      * [Stringifiable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Stringifiable.html)
      * [AsciiCanvas](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_ascii.AsciiCanvas.html)
      * [VertexViewer](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_ascii.VertexViewer.html)
      * [PngDrawer](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_png.PngDrawer.html)
      * [RunnableWithMessageHistory](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html)
      * [RunnableAssign](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.passthrough.RunnableAssign.html)
      * [RunnablePassthrough](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.passthrough.RunnablePassthrough.html)
      * [RunnablePick](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.passthrough.RunnablePick.html)
      * [ExponentialJitterParams](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.retry.ExponentialJitterParams.html)
      * [RunnableRetry](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.retry.RunnableRetry.html)
      * [RouterInput](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.router.RouterInput.html)
      * [RouterRunnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.router.RouterRunnable.html)
      * [BaseStreamEvent](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html)
      * [CustomStreamEvent](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.CustomStreamEvent.html)
      * [EventData](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.EventData.html)
      * [StandardStreamEvent](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.StandardStreamEvent.html)
      * [AddableDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.AddableDict.html)
      * [ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html)
      * [ConfigurableFieldMultiOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html)
      * [ConfigurableFieldSingleOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html)
      * [ConfigurableFieldSpec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html)
      * [FunctionNonLocals](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.FunctionNonLocals.html)
      * [GetLambdaSource](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.GetLambdaSource.html)
      * [IsFunctionArgDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.IsFunctionArgDict.html)
      * [IsLocalDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.IsLocalDict.html)
      * [NonLocals](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.NonLocals.html)
      * [SupportsAdd](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.SupportsAdd.html)
      * [chain](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.chain.html)
      * [coerce_to_runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.coerce_to_runnable.html)
      * [acall_func_with_variable_args](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.acall_func_with_variable_args.html)
      * [call_func_with_variable_args](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.call_func_with_variable_args.html)
      * [ensure_config](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.ensure_config.html)
      * [get_async_callback_manager_for_config](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.get_async_callback_manager_for_config.html)
      * [get_callback_manager_for_config](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.get_callback_manager_for_config.html)
      * [get_config_list](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.get_config_list.html)
      * [get_executor_for_config](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.get_executor_for_config.html)
      * [merge_configs](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.merge_configs.html)
      * [patch_config](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.patch_config.html)
      * [run_in_executor](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.run_in_executor.html)
      * [set_config_context](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.set_config_context.html)
      * [make_options_spec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.configurable.make_options_spec.html)
      * [prefix_config_spec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.configurable.prefix_config_spec.html)
      * [is_uuid](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.is_uuid.html)
      * [node_data_json](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.node_data_json.html)
      * [node_data_str](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.node_data_str.html)
      * [draw_ascii](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_ascii.draw_ascii.html)
      * [draw_mermaid](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_mermaid.draw_mermaid.html)
      * [draw_mermaid_png](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_mermaid.draw_mermaid_png.html)
      * [aidentity](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.passthrough.aidentity.html)
      * [identity](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.passthrough.identity.html)
      * [aadd](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.aadd.html)
      * [accepts_config](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.accepts_config.html)
      * [accepts_context](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.accepts_context.html)
      * [accepts_run_manager](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.accepts_run_manager.html)
      * [add](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.add.html)
      * [coro_with_context](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.coro_with_context.html)
      * [gated_coro](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.gated_coro.html)
      * [gather_with_concurrency](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.gather_with_concurrency.html)
      * [get_function_first_arg_dict_keys](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.get_function_first_arg_dict_keys.html)
      * [get_lambda_source](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.get_lambda_source.html)
      * [get_unique_config_specs](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.get_unique_config_specs.html)
      * [indent_lines_after_first](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.indent_lines_after_first.html)
      * [is_async_callable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.is_async_callable.html)
      * [is_async_generator](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.is_async_generator.html)
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
  * [`runnables`](https://python.langchain.com/api_reference/core/runnables.html)
  * BaseStreamEvent


# BaseStreamEvent[#](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#basestreamevent "Link to this heading") 

_class_ langchain_core.runnables.schema.BaseStreamEvent[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/schema.html#BaseStreamEvent)[#](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent "Link to this definition")
    
Streaming event.
Schema of a streaming event which is produced from the astream_events method.
Example
```
fromlangchain_core.runnablesimport RunnableLambda
async defreverse(s: str) -> str:
  return s[::-1]
chain = RunnableLambda(func=reverse)
events = [event async for event in chain.astream_events("hello")]
# will produce the following events
# (where some fields have been omitted for brevity):
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

event _: str_[#](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.event "Link to this definition")
    
on_[runnable_type]_(start|stream|end).
Runnable types are one of:
  * **llm** - used by non chat models
  * **chat_model** - used by chat models
  * **prompt** – e.g., ChatPromptTemplate
  * 

**tool** – from tools defined via @tool decorator or inheriting
    
from Tool/BaseTool
  * **chain** - most Runnables are of this type


Further, the events are categorized as one of:
  * **start** - when the Runnable starts
  * **stream** - when the Runnable is streaming
  * [**](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#id1)end* - when the Runnable ends


start, stream and end are associated with slightly different data payload.
Please see the documentation for EventData for more details. 

Type:
    
Event names are of the format 

run_id _: str_[#](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.run_id "Link to this definition")
    
An randomly generated ID to keep track of the execution of the given Runnable.
Each child Runnable that gets invoked as part of the execution of a parent Runnable is assigned its own unique ID. 

tags _: NotRequired[list[str]]_[#](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.tags "Link to this definition")
    
Tags associated with the Runnable that generated this event.
Tags are always inherited from parent Runnables.
Tags can either be bound to a Runnable using .with_config({“tags”: [“hello”]}) or passed at run time using .astream_events(…, {“tags”: [“hello”]}). 

metadata _: NotRequired[dict[str,Any]]_[#](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.metadata "Link to this definition")
    
Metadata associated with the Runnable that generated this event.
Metadata can either be bound to a Runnable using
> .with_config({“metadata”: { “foo”: “bar” }})
or passed at run time using
> .astream_events(…, {“metadata”: {“foo”: “bar”}}). 

parent_ids _: Sequence[str]_[#](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.parent_ids "Link to this definition")
    
A list of the parent IDs associated with this event.
Root Events will have an empty list.
For example, if a Runnable A calls Runnable B, then the event generated by Runnable B will have Runnable A’s ID in the parent_ids field.
The order of the parent IDs is from the root parent to the immediate parent.
Only supported as of v2 of the astream events API. v1 will return an empty list.
On this page 
  * [`BaseStreamEvent`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent)
    * [`event`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.event)
    * [`run_id`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.run_id)
    * [`tags`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.tags)
    * [`metadata`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.metadata)
    * [`parent_ids`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.BaseStreamEvent.html#langchain_core.runnables.schema.BaseStreamEvent.parent_ids)


© Copyright 2025, LangChain Inc. 

