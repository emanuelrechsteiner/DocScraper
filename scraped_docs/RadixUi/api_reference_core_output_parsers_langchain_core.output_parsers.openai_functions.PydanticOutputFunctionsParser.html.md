---
url: https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html
scraped_at: 2025-05-25T18:09:41.033492
title: PydanticOutputFunctionsParser — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#main-content)
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
      * [BaseGenerationOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html)
      * [BaseLLMOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html)
      * [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html)
      * [JsonOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.JsonOutputParser.html)
      * [SimpleJsonOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.SimpleJsonOutputParser.html)
      * [CommaSeparatedListOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.CommaSeparatedListOutputParser.html)
      * [ListOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.ListOutputParser.html)
      * [MarkdownListOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.MarkdownListOutputParser.html)
      * [NumberedListOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.NumberedListOutputParser.html)
      * [JsonKeyOutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.JsonKeyOutputFunctionsParser.html)
      * [JsonOutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.JsonOutputFunctionsParser.html)
      * [OutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.OutputFunctionsParser.html)
      * [PydanticAttrOutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticAttrOutputFunctionsParser.html)
      * [PydanticOutputFunctionsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html)
      * [JsonOutputKeyToolsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.JsonOutputKeyToolsParser.html)
      * [JsonOutputToolsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.JsonOutputToolsParser.html)
      * [PydanticToolsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.PydanticToolsParser.html)
      * [PydanticOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.pydantic.PydanticOutputParser.html)
      * [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)
      * [BaseCumulativeTransformOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.transform.BaseCumulativeTransformOutputParser.html)
      * [BaseTransformOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.transform.BaseTransformOutputParser.html)
      * [XMLOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.XMLOutputParser.html)
      * [droplastn](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.droplastn.html)
      * [make_invalid_tool_call](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.make_invalid_tool_call.html)
      * [parse_tool_call](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.parse_tool_call.html)
      * [parse_tool_calls](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.parse_tool_calls.html)
      * [nested_element](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.nested_element.html)
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
  * [`output_parsers`](https://python.langchain.com/api_reference/core/output_parsers.html)
  * PydanticOutputFunctionsParser


# PydanticOutputFunctionsParser[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#pydanticoutputfunctionsparser "Link to this heading") 

_class_ langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/openai_functions.html#PydanticOutputFunctionsParser)[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser "Link to this definition")
    
Bases: [`OutputFunctionsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.OutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.OutputFunctionsParser "langchain_core.output_parsers.openai_functions.OutputFunctionsParser")
Parse an output as a pydantic object.
This parser is used to parse the output of a ChatModel that uses OpenAI function format to invoke functions.
The parser extracts the function call invocation and matches them to the pydantic schema provided.
An exception will be raised if the function call does not match the provided schema.
Example
… code-block:: python
> 

message = AIMessage(
    
> content=”This is a test message”, additional_kwargs={
>> 

“function_call”: {
    
>> “name”: “cookie”, “arguments”: json.dumps({“name”: “value”, “age”: 10}),
>> }
> },
> ) chat_generation = ChatGeneration(message=message) 

class Cookie(BaseModel):
    
> name: str age: int 

class Dog(BaseModel):
    
> species: str
> # Full output parser = PydanticOutputFunctionsParser(
>> pydantic_schema={“cookie”: Cookie, “dog”: Dog}
> ) result = parser.parse_result([chat_generation])
Note
PydanticOutputFunctionsParser implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃
The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more. 

_param_ args_only _: bool_ _= True_[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.args_only "Link to this definition")
    
Whether to only return the arguments to the function call. 

_param_ pydantic_schema _: type[BaseModel]|dict[str,type[BaseModel]]__[Required]_[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.pydantic_schema "Link to this definition")
    
The pydantic schema to parse the output with.
If multiple schemas are provided, then the function name will be used to determine which schema to use. 

_async_ abatch( 
    _inputs :list[Input]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|list[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")]|None=None_,     _*_ ,     _return_exceptions :bool=False_,     _** kwargs:Any|None_, ) → list[Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.abatch "Link to this definition")     
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
    _inputs :Sequence[Input]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|Sequence[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")]|None=None_,     _*_ ,     _return_exceptions :bool=False_,     _** kwargs:Any|None_, ) → AsyncIterator[tuple[int,Output|Exception]][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.abatch_as_completed "Link to this definition")     
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

_async_ ainvoke( 
    _input :str|[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any|None_, ) → T[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.ainvoke "Link to this definition")     
Default implementation of ainvoke, calls invoke from a thread.
The default implementation allows usage of async code even if the Runnable did not implement a native async version of invoke.
Subclasses should override this method if they can run asynchronously. 

Parameters:
    
  * **input** (_str_ _|_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage"))
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_)
  * **kwargs** (_Any_ _|__None_)



Return type:
    
_T_ 

_async_ aparse_result( 
    _result :list[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")]_,     _*_ ,     _partial :bool=False_, ) → T[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.aparse_result "Link to this definition")     
Async parse a list of candidate model Generations into a specific format. 

Parameters:
    
  * **result** (_list_ _[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _]_) – A list of Generations to be parsed. The Generations are assumed to be different candidate outputs for a single model input.
  * **partial** (_bool_) – Whether to parse the output as a partial result. This is useful for parsers that can parse partial results. Default is False.



Returns:
    
Structured output. 

Return type:
    
_T_ 

_async_ astream( 
    _input :Input_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any|None_, ) → AsyncIterator[Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.astream "Link to this definition")     
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
    _input :Any_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _*_ ,     _version :Literal['v1','v2']='v2'_,     _include_names :Sequence[str]|None=None_,     _include_types :Sequence[str]|None=None_,     _include_tags :Sequence[str]|None=None_,     _exclude_names :Sequence[str]|None=None_,     _exclude_types :Sequence[str]|None=None_,     _exclude_tags :Sequence[str]|None=None_,     _** kwargs:Any_, ) → AsyncIterator[StreamEvent][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.astream_events "Link to this definition")     
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
    _inputs :list[Input]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|list[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")]|None=None_,     _*_ ,     _return_exceptions :bool=False_,     _** kwargs:Any|None_, ) → list[Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.batch "Link to this definition")     
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
    _inputs :Sequence[Input]_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|Sequence[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")]|None=None_,     _*_ ,     _return_exceptions :bool=False_,     _** kwargs:Any|None_, ) → Iterator[tuple[int,Output|Exception]][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.batch_as_completed "Link to this definition")     
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
    _** kwargs:Any_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.bind "Link to this definition")     
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
    _which :[ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")_,     _*_ ,     _default_key :str='default'_,     _prefix_keys :bool=False_,     _** kwargs:[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output]|Callable[[],[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output]]_, ) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.configurable_alternatives "Link to this definition")     
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
    _** kwargs:[ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")|[ConfigurableFieldSingleOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption")|[ConfigurableFieldMultiOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")_, ) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.configurable_fields "Link to this definition")     
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
    _input :str|[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any_, ) → T[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.invoke "Link to this definition")     
Transform a single input into an output. 

Parameters:
    
  * **input** (_str_ _|_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")) – The input to the Runnable.
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details.
  * **kwargs** (_Any_)



Returns:
    
The output of the Runnable. 

Return type:
    
_T_ 

parse_result( 
    _result :list[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")]_,     _*_ ,     _partial :bool=False_, ) → Any[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/openai_functions.html#PydanticOutputFunctionsParser.parse_result)[#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.parse_result "Link to this definition")     
Parse the result of an LLM call to a JSON object. 

Parameters:
    
  * **result** (_list_ _[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _]_) – The result of the LLM call.
  * **partial** (_bool_) – Whether to parse partial JSON objects. Default is False.



Returns:
    
The parsed JSON object. 

Return type:
    
_Any_ 

stream( 
    _input :Input_,     _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any|None_, ) → Iterator[Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.stream "Link to this definition")     
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
    _*_ ,     _on_start :AsyncListener|None=None_,     _on_end :AsyncListener|None=None_,     _on_error :AsyncListener|None=None_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_alisteners "Link to this definition")     
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
    _config :[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")|None=None_,     _** kwargs:Any_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_config "Link to this definition")     
Bind config to a Runnable, returning a new Runnable. 

Parameters:
    
  * **config** ([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_) – The config to bind to the Runnable.
  * **kwargs** (_Any_) – Additional keyword arguments to pass to the Runnable.



Returns:
    
A new Runnable with the config bound. 

Return type:
    
[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[_Input_ , _Output_] 

with_fallbacks(_fallbacks: Sequence[Runnable[Input, Output]], *, exceptions_to_handle: tuple[type[BaseException], ...] = (<class 'Exception'>,), exception_key: Optional[str] = None_) → RunnableWithFallbacksT[Input,Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_fallbacks "Link to this definition")
    
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
    _*_ ,     _on_start :Callable[[Run],None]|Callable[[Run,[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")],None]|None=None_,     _on_end :Callable[[Run],None]|Callable[[Run,[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")],None]|None=None_,     _on_error :Callable[[Run],None]|Callable[[Run,[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")],None]|None=None_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_listeners "Link to this definition")     
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

with_retry(_*, retry_if_exception_type: tuple[type[BaseException], ...] = (<class 'Exception'>,), wait_exponential_jitter: bool = True, exponential_jitter_params: Optional[ExponentialJitterParams] = None, stop_after_attempt: int = 3_) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_retry "Link to this definition")
    
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
    _*_ ,     _input_type :type[Input]|None=None_,     _output_type :type[Output]|None=None_, ) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[Input,Output][#](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_types "Link to this definition")     
Bind input and output types to a Runnable, returning a new Runnable. 

Parameters:
    
  * **input_type** (_type_ _[__Input_ _]__|__None_) – The input type to bind to the Runnable. Defaults to None.
  * **output_type** (_type_ _[__Output_ _]__|__None_) – The output type to bind to the Runnable. Defaults to None.



Returns:
    
A new Runnable with the types bound. 

Return type:
    
[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[_Input_ , _Output_]
Examples using PydanticOutputFunctionsParser
  * [LangSmith LLM Runs](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_llm_runs/)


On this page 
  * [`PydanticOutputFunctionsParser`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser)
    * [`args_only`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.args_only)
    * [`pydantic_schema`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.pydantic_schema)
    * [`abatch()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.abatch)
    * [`abatch_as_completed()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.abatch_as_completed)
    * [`ainvoke()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.ainvoke)
    * [`aparse_result()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.aparse_result)
    * [`astream()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.astream)
    * [`astream_events()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.astream_events)
    * [`batch()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.batch)
    * [`batch_as_completed()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.batch_as_completed)
    * [`bind()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.bind)
    * [`configurable_alternatives()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.configurable_alternatives)
    * [`configurable_fields()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.configurable_fields)
    * [`invoke()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.invoke)
    * [`parse_result()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.parse_result)
    * [`stream()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.stream)
    * [`with_alisteners()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_alisteners)
    * [`with_config()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_config)
    * [`with_fallbacks()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_fallbacks)
    * [`with_listeners()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_listeners)
    * [`with_retry()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_retry)
    * [`with_types()`](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.with_types)


© Copyright 2025, LangChain Inc. 
  *[*]: Keyword-only parameters separator (PEP 3102)

