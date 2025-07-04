---
url: https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html
scraped_at: 2025-05-25T17:55:41.988132
title: MessagesPlaceholder — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#main-content)
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
      * [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html)
      * [AIMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.AIMessagePromptTemplate.html)
      * [BaseChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.BaseChatPromptTemplate.html)
      * [BaseStringMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.BaseStringMessagePromptTemplate.html)
      * [ChatMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatMessagePromptTemplate.html)
      * [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)
      * [HumanMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.HumanMessagePromptTemplate.html)
      * [MessagesPlaceholder](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html)
      * [SystemMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.SystemMessagePromptTemplate.html)
      * [DictPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.dict.DictPromptTemplate.html)
      * [FewShotChatMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.few_shot.FewShotChatMessagePromptTemplate.html)
      * [FewShotPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.few_shot.FewShotPromptTemplate.html)
      * [FewShotPromptWithTemplates](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.few_shot_with_templates.FewShotPromptWithTemplates.html)
      * [ImagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.image.ImagePromptTemplate.html)
      * [BaseMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html)
      * [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html)
      * [StringPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.StringPromptTemplate.html)
      * [StructuredPrompt](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.structured.StructuredPrompt.html)
      * [aformat_document](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.aformat_document.html)
      * [format_document](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.format_document.html)
      * [load_prompt](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.loading.load_prompt.html)
      * [load_prompt_from_config](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.loading.load_prompt_from_config.html)
      * [check_valid_template](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.check_valid_template.html)
      * [get_template_variables](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.get_template_variables.html)
      * [jinja2_formatter](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.jinja2_formatter.html)
      * [mustache_formatter](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.mustache_formatter.html)
      * [mustache_schema](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.mustache_schema.html)
      * [mustache_template_vars](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.mustache_template_vars.html)
      * [validate_jinja2](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.validate_jinja2.html)
      * [PipelinePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.pipeline.PipelinePromptTemplate.html)
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
  * [`prompts`](https://python.langchain.com/api_reference/core/prompts.html)
  * MessagesPlaceholder


# MessagesPlaceholder[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#messagesplaceholder "Link to this heading") 

_class_ langchain_core.prompts.chat.MessagesPlaceholder[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#MessagesPlaceholder)[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder "Link to this definition")
    
Bases: [`BaseMessagePromptTemplate`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate")
Prompt template that assumes variable is already list of messages.
A placeholder which can be used to pass in a list of messages.
Direct usage:
> ```
fromlangchain_core.promptsimport MessagesPlaceholder
prompt = MessagesPlaceholder("history")
prompt.format_messages() # raises KeyError
prompt = MessagesPlaceholder("history", optional=True)
prompt.format_messages() # returns empty list []
prompt.format_messages(
  history=[
    ("system", "You are an AI assistant."),
    ("human", "Hello!"),
  ]
)
# -> [
#   SystemMessage(content="You are an AI assistant."),
#   HumanMessage(content="Hello!"),
# ]

```
Copy to clipboard
Building a prompt with chat history:
> ```
fromlangchain_core.promptsimport ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages(
  [
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
  ]
)
prompt.invoke(
  {
    "history": [("human", "what's 5 + 2"), ("ai", "5 + 2 is 7")],
    "question": "now multiply that by 4"
  }
)
# -> ChatPromptValue(messages=[
#   SystemMessage(content="You are a helpful assistant."),
#   HumanMessage(content="what's 5 + 2"),
#   AIMessage(content="5 + 2 is 7"),
#   HumanMessage(content="now multiply that by 4"),
# ])

```
Copy to clipboard
Limiting the number of messages:
> ```
fromlangchain_core.promptsimport MessagesPlaceholder
prompt = MessagesPlaceholder("history", n_messages=1)
prompt.format_messages(
  history=[
    ("system", "You are an AI assistant."),
    ("human", "Hello!"),
  ]
)
# -> [
#   HumanMessage(content="Hello!"),
# ]

```
Copy to clipboard
Create a messages placeholder. 

Parameters:
    
  * **variable_name** – Name of variable to use as messages.
  * **optional** – If True format_messages can be called with no arguments and will return an empty list. If False then a named argument with name variable_name must be passed in, even if the value is an empty list. Defaults to False.]



_param_ n_messages _: PositiveInt|None_ _= None_[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.n_messages "Link to this definition")
    
Maximum number of messages to include. If None, then will include all. Defaults to None. 

_param_ optional _: bool_ _= False_[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.optional "Link to this definition")
    
If True format_messages can be called with no arguments and will return an empty list. If False then a named argument with name variable_name must be passed in, even if the value is an empty list. 

_param_ variable_name _: str_ _[Required]_[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.variable_name "Link to this definition")
    
Name of variable to use as messages. 

_async_ aformat_messages( 
    _** kwargs:Any_, ) → list[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")][#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.aformat_messages "Link to this definition")     
Async format messages from kwargs. 

Parameters:
    
****kwargs** (_Any_) – Keyword arguments to use for formatting. 

Returns:
    
List of BaseMessages. 

Return type:
    
list[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")] 

format_messages( 
    _** kwargs:Any_, ) → list[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")][[source]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#MessagesPlaceholder.format_messages)[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.format_messages "Link to this definition")     
Format messages from kwargs. 

Parameters:
    
****kwargs** (_Any_) – Keyword arguments to use for formatting. 

Returns:
    
List of BaseMessage. 

Raises:
    
**ValueError** – If variable is not a list of messages. 

Return type:
    
list[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")] 

pretty_print() → None[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.pretty_print "Link to this definition")
    
Print a human-readable representation. 

Return type:
    
None 

pretty_repr(_html :bool=False_) → str[[source]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#MessagesPlaceholder.pretty_repr)[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.pretty_repr "Link to this definition")
    
Human-readable representation. 

Parameters:
    
**html** (_bool_) – Whether to format as HTML. Defaults to False. 

Returns:
    
Human-readable representation. 

Return type:
    
str 

_property_ input_variables _: list[str]_[#](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.input_variables "Link to this definition")
    
Input variables for this prompt template. 

Returns:
    
List of input variable names.
Examples using MessagesPlaceholder
  * [AWS DynamoDB](https://python.langchain.com/docs/integrations/memory/aws_dynamodb/)
  * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)
  * [Build an Extraction Chain](https://python.langchain.com/docs/tutorials/extraction/)
  * [Conceptual guide](https://python.langchain.com/docs/concepts/)
  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)
  * [Couchbase](https://python.langchain.com/docs/integrations/memory/couchbase_chat_message_history/)
  * [Google AlloyDB for PostgreSQL](https://python.langchain.com/docs/integrations/memory/google_alloydb/)
  * [Google El Carro Oracle](https://python.langchain.com/docs/integrations/memory/google_el_carro/)
  * [Google SQL for MySQL](https://python.langchain.com/docs/integrations/memory/google_sql_mysql/)
  * [Google SQL for PostgreSQL](https://python.langchain.com/docs/integrations/memory/google_sql_pg/)
  * [Google SQL for SQL Server](https://python.langchain.com/docs/integrations/memory/google_sql_mssql/)
  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)
  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)
  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)
  * [How to add message history](https://python.langchain.com/docs/how_to/message_history/)
  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)
  * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)
  * [How to get a RAG application to add citations](https://python.langchain.com/docs/how_to/qa_citations/)
  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)
  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)
  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)
  * [Llama2Chat](https://python.langchain.com/docs/integrations/chat/llama2_chat/)
  * [MongoDB](https://python.langchain.com/docs/integrations/memory/mongodb_chat_message_history/)
  * [Redis](https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/)
  * [SQL (SQLAlchemy)](https://python.langchain.com/docs/integrations/memory/sql_chat_message_history/)
  * [SQLite](https://python.langchain.com/docs/integrations/memory/sqlite/)
  * [Streamlit](https://python.langchain.com/docs/integrations/memory/streamlit_chat_message_history/)
  * [TiDB](https://python.langchain.com/docs/integrations/memory/tidb_chat_message_history/)
  * [ZepCloudChatMessageHistory](https://python.langchain.com/docs/integrations/memory/zep_cloud_chat_message_history/)


On this page 
  * [`MessagesPlaceholder`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder)
    * [`n_messages`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.n_messages)
    * [`optional`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.optional)
    * [`variable_name`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.variable_name)
    * [`aformat_messages()`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.aformat_messages)
    * [`format_messages()`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.format_messages)
    * [`pretty_print()`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.pretty_print)
    * [`pretty_repr()`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.pretty_repr)
    * [`input_variables`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder.input_variables)


© Copyright 2025, LangChain Inc. 

