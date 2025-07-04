---
url: https://python.langchain.com/docs/how_to/function_calling/
scraped_at: 2025-05-25T17:55:10.467386
title: How to do tool/function calling | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/how_to/function_calling/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/how_to/function_calling/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/how_to/function_calling/)
  * [v0.3](https://python.langchain.com/docs/introduction/)
  * [v0.2](https://python.langchain.com/v0.2/docs/introduction)
  * [v0.1](https://python.langchain.com/v0.1/docs/get_started/introduction)


[💬](https://chat.langchain.com)[](https://github.com/langchain-ai/langchain)
Search`⌘``K`
  * [Introduction](https://python.langchain.com/docs/introduction/)
  * [Tutorials](https://python.langchain.com/docs/tutorials/)
    * [Build a Question Answering application over a Graph Database](https://python.langchain.com/docs/tutorials/graph/)
    * [Tutorials](https://python.langchain.com/docs/tutorials/)
    * [Build a simple LLM application with chat models and prompt templates](https://python.langchain.com/docs/tutorials/llm_chain/)
    * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)
    * [Build a Retrieval Augmented Generation (RAG) App: Part 2](https://python.langchain.com/docs/tutorials/qa_chat_history/)
    * [Build an Extraction Chain](https://python.langchain.com/docs/tutorials/extraction/)
    * [Build an Agent](https://python.langchain.com/docs/tutorials/agents/)
    * [Tagging](https://python.langchain.com/docs/tutorials/classification/)
    * [Build a Retrieval Augmented Generation (RAG) App: Part 1](https://python.langchain.com/docs/tutorials/rag/)
    * [Build a semantic search engine](https://python.langchain.com/docs/tutorials/retrievers/)
    * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)
    * [Summarize Text](https://python.langchain.com/docs/tutorials/summarization/)
  * [How-to guides](https://python.langchain.com/docs/how_to/)
    * [How-to guides](https://python.langchain.com/docs/how_to/)
    * [How to use tools in a chain](https://python.langchain.com/docs/how_to/tools_chain/)
    * [How to use a vectorstore as a retriever](https://python.langchain.com/docs/how_to/vectorstore_retriever/)
    * [How to add memory to chatbots](https://python.langchain.com/docs/how_to/chatbots_memory/)
    * [How to use example selectors](https://python.langchain.com/docs/how_to/example_selectors/)
    * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)
    * [How to invoke runnables in parallel](https://python.langchain.com/docs/how_to/parallel/)
    * [How to stream chat model responses](https://python.langchain.com/docs/how_to/chat_streaming/)
    * [How to add default invocation args to a Runnable](https://python.langchain.com/docs/how_to/binding/)
    * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)
    * [How to use few shot examples in chat models](https://python.langchain.com/docs/how_to/few_shot_examples_chat/)
    * [How to do tool/function calling](https://python.langchain.com/docs/how_to/function_calling/)
    * [How to install LangChain packages](https://python.langchain.com/docs/how_to/installation/)
    * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)
    * [How to use few shot examples](https://python.langchain.com/docs/how_to/few_shot_examples/)
    * [How to run custom functions](https://python.langchain.com/docs/how_to/functions/)
    * [How to use output parsers to parse an LLM response into structured format](https://python.langchain.com/docs/how_to/output_parser_structured/)
    * [How to handle cases where no queries are generated](https://python.langchain.com/docs/how_to/query_no_queries/)
    * [How to route between sub-chains](https://python.langchain.com/docs/how_to/routing/)
    * [How to return structured data from a model](https://python.langchain.com/docs/how_to/structured_output/)
    * [How to summarize text through parallelization](https://python.langchain.com/docs/how_to/summarize_map_reduce/)
    * [How to summarize text through iterative refinement](https://python.langchain.com/docs/how_to/summarize_refine/)
    * [How to summarize text in a single LLM call](https://python.langchain.com/docs/how_to/summarize_stuff/)
    * [How to use toolkits](https://python.langchain.com/docs/how_to/toolkits/)
    * [How to add ad-hoc tool calling capability to LLMs and Chat Models](https://python.langchain.com/docs/how_to/tools_prompting/)
    * [Build an Agent with AgentExecutor (Legacy)](https://python.langchain.com/docs/how_to/agent_executor/)
    * [How to construct knowledge graphs](https://python.langchain.com/docs/how_to/graph_constructing/)
    * [How to partially format prompt templates](https://python.langchain.com/docs/how_to/prompts_partial/)
    * [How to handle multiple queries when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_queries/)
    * [How to use built-in tools and toolkits](https://python.langchain.com/docs/how_to/tools_builtin/)
    * [How to pass through arguments from one step to the next](https://python.langchain.com/docs/how_to/passthrough/)
    * [How to compose prompts together](https://python.langchain.com/docs/how_to/prompts_composition/)
    * [How to handle multiple retrievers when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_retrievers/)
    * [How to add values to a chain's state](https://python.langchain.com/docs/how_to/assign/)
    * [How to construct filters for query analysis](https://python.langchain.com/docs/how_to/query_constructing_filters/)
    * [How to configure runtime chain internals](https://python.langchain.com/docs/how_to/configure/)
    * [How deal with high cardinality categoricals when doing query analysis](https://python.langchain.com/docs/how_to/query_high_cardinality/)
    * [Custom Document Loader](https://python.langchain.com/docs/how_to/document_loader_custom/)
    * [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)
    * [How to add scores to retriever results](https://python.langchain.com/docs/how_to/add_scores_retriever/)
    * [Caching](https://python.langchain.com/docs/how_to/caching_embeddings/)
    * [How to use callbacks in async environments](https://python.langchain.com/docs/how_to/callbacks_async/)
    * [How to attach callbacks to a runnable](https://python.langchain.com/docs/how_to/callbacks_attach/)
    * [How to propagate callbacks constructor](https://python.langchain.com/docs/how_to/callbacks_constructor/)
    * [How to dispatch custom callback events](https://python.langchain.com/docs/how_to/callbacks_custom_events/)
    * [How to pass callbacks in at runtime](https://python.langchain.com/docs/how_to/callbacks_runtime/)
    * [How to split by character](https://python.langchain.com/docs/how_to/character_text_splitter/)
    * [How to cache chat model responses](https://python.langchain.com/docs/how_to/chat_model_caching/)
    * [How to handle rate limits](https://python.langchain.com/docs/how_to/chat_model_rate_limiting/)
    * [How to init any model in one line](https://python.langchain.com/docs/how_to/chat_models_universal_init/)
    * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)
    * [How to add tools to chatbots](https://python.langchain.com/docs/how_to/chatbots_tools/)
    * [How to split code](https://python.langchain.com/docs/how_to/code_splitter/)
    * [How to do retrieval with contextual compression](https://python.langchain.com/docs/how_to/contextual_compression/)
    * [How to convert Runnables to Tools](https://python.langchain.com/docs/how_to/convert_runnable_to_tool/)
    * [How to create custom callback handlers](https://python.langchain.com/docs/how_to/custom_callbacks/)
    * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)
    * [Custom Embeddings](https://python.langchain.com/docs/how_to/custom_embeddings/)
    * [How to create a custom LLM class](https://python.langchain.com/docs/how_to/custom_llm/)
    * [Custom Retriever](https://python.langchain.com/docs/how_to/custom_retriever/)
    * [How to create tools](https://python.langchain.com/docs/how_to/custom_tools/)
    * [How to debug your LLM apps](https://python.langchain.com/docs/how_to/debugging/)
    * [How to load CSVs](https://python.langchain.com/docs/how_to/document_loader_csv/)
    * [How to load documents from a directory](https://python.langchain.com/docs/how_to/document_loader_directory/)
    * [How to load HTML](https://python.langchain.com/docs/how_to/document_loader_html/)
    * [How to load JSON](https://python.langchain.com/docs/how_to/document_loader_json/)
    * [How to load Markdown](https://python.langchain.com/docs/how_to/document_loader_markdown/)
    * [How to load Microsoft Office files](https://python.langchain.com/docs/how_to/document_loader_office_file/)
    * [How to load PDFs](https://python.langchain.com/docs/how_to/document_loader_pdf/)
    * [How to load web pages](https://python.langchain.com/docs/how_to/document_loader_web/)
    * [How to create a dynamic (self-constructing) chain](https://python.langchain.com/docs/how_to/dynamic_chain/)
    * [Text embedding models](https://python.langchain.com/docs/how_to/embed_text/)
    * [How to combine results from multiple retrievers](https://python.langchain.com/docs/how_to/ensemble_retriever/)
    * [How to select examples from a LangSmith dataset](https://python.langchain.com/docs/how_to/example_selectors_langsmith/)
    * [How to select examples by length](https://python.langchain.com/docs/how_to/example_selectors_length_based/)
    * [How to select examples by maximal marginal relevance (MMR)](https://python.langchain.com/docs/how_to/example_selectors_mmr/)
    * [How to select examples by n-gram overlap](https://python.langchain.com/docs/how_to/example_selectors_ngram/)
    * [How to select examples by similarity](https://python.langchain.com/docs/how_to/example_selectors_similarity/)
    * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)
    * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)
    * [How to use prompting alone (no tool calling) to do extraction](https://python.langchain.com/docs/how_to/extraction_parse/)
    * [How to add fallbacks to a runnable](https://python.langchain.com/docs/how_to/fallbacks/)
    * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)
    * [Hybrid Search](https://python.langchain.com/docs/how_to/hybrid/)
    * [How to use the LangChain indexing API](https://python.langchain.com/docs/how_to/indexing/)
    * [How to inspect runnables](https://python.langchain.com/docs/how_to/inspect/)
    * [LangChain Expression Language Cheatsheet](https://python.langchain.com/docs/how_to/lcel_cheatsheet/)
    * [How to cache LLM responses](https://python.langchain.com/docs/how_to/llm_caching/)
    * [How to track token usage for LLMs](https://python.langchain.com/docs/how_to/llm_token_usage_tracking/)
    * [Run models locally](https://python.langchain.com/docs/how_to/local_llms/)
    * [How to get log probabilities](https://python.langchain.com/docs/how_to/logprobs/)
    * [How to reorder retrieved results to mitigate the "lost in the middle" effect](https://python.langchain.com/docs/how_to/long_context_reorder/)
    * [How to split Markdown by Headers](https://python.langchain.com/docs/how_to/markdown_header_metadata_splitter/)
    * [How to merge consecutive messages of the same type](https://python.langchain.com/docs/how_to/merge_message_runs/)
    * [How to add message history](https://python.langchain.com/docs/how_to/message_history/)
    * [How to migrate from legacy LangChain agents to LangGraph](https://python.langchain.com/docs/how_to/migrate_agent/)
    * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)
    * [How to pass multimodal data to models](https://python.langchain.com/docs/how_to/multimodal_inputs/)
    * [How to use multimodal prompts](https://python.langchain.com/docs/how_to/multimodal_prompts/)
    * [How to create a custom Output Parser](https://python.langchain.com/docs/how_to/output_parser_custom/)
    * [How to use the output-fixing parser](https://python.langchain.com/docs/how_to/output_parser_fixing/)
    * [How to parse JSON output](https://python.langchain.com/docs/how_to/output_parser_json/)
    * [How to retry when a parsing error occurs](https://python.langchain.com/docs/how_to/output_parser_retry/)
    * [How to parse text from message objects](https://python.langchain.com/docs/how_to/output_parser_string/)
    * [How to parse XML output](https://python.langchain.com/docs/how_to/output_parser_xml/)
    * [How to parse YAML output](https://python.langchain.com/docs/how_to/output_parser_yaml/)
    * [How to use the Parent Document Retriever](https://python.langchain.com/docs/how_to/parent_document_retriever/)
    * [How to use LangChain with different Pydantic versions](https://python.langchain.com/docs/how_to/pydantic_compatibility/)
    * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)
    * [How to get a RAG application to add citations](https://python.langchain.com/docs/how_to/qa_citations/)
    * [How to do per-user retrieval](https://python.langchain.com/docs/how_to/qa_per_user/)
    * [How to get your RAG application to return sources](https://python.langchain.com/docs/how_to/qa_sources/)
    * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)
    * [How to split JSON data](https://python.langchain.com/docs/how_to/recursive_json_splitter/)
    * [How to recursively split text by characters](https://python.langchain.com/docs/how_to/recursive_text_splitter/)
    * [Response metadata](https://python.langchain.com/docs/how_to/response_metadata/)
    * [How to pass runtime secrets to runnables](https://python.langchain.com/docs/how_to/runnable_runtime_secrets/)
    * [How to do "self-querying" retrieval](https://python.langchain.com/docs/how_to/self_query/)
    * [How to split text based on semantic similarity](https://python.langchain.com/docs/how_to/semantic-chunker/)
    * [How to chain runnables](https://python.langchain.com/docs/how_to/sequence/)
    * [How to save and load LangChain objects](https://python.langchain.com/docs/how_to/serialization/)
    * [How to split text by tokens](https://python.langchain.com/docs/how_to/split_by_token/)
    * [How to split HTML](https://python.langchain.com/docs/how_to/split_html/)
    * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)
    * [How to deal with large databases when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_large_db/)
    * [How to better prompt when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_prompting/)
    * [How to do query validation as part of SQL question-answering](https://python.langchain.com/docs/how_to/sql_query_checking/)
    * [How to stream runnables](https://python.langchain.com/docs/how_to/streaming/)
    * [How to stream responses from an LLM](https://python.langchain.com/docs/how_to/streaming_llm/)
    * [How to use a time-weighted vector store retriever](https://python.langchain.com/docs/how_to/time_weighted_vectorstore/)
    * [How to return artifacts from a tool](https://python.langchain.com/docs/how_to/tool_artifacts/)
    * [How to use chat models to call tools](https://python.langchain.com/docs/how_to/tool_calling/)
    * [How to disable parallel tool calling](https://python.langchain.com/docs/how_to/tool_calling_parallel/)
    * [How to force models to call a tool](https://python.langchain.com/docs/how_to/tool_choice/)
    * [How to access the RunnableConfig from a tool](https://python.langchain.com/docs/how_to/tool_configure/)
    * [How to pass tool outputs to chat models](https://python.langchain.com/docs/how_to/tool_results_pass_to_model/)
    * [How to pass run time values to tools](https://python.langchain.com/docs/how_to/tool_runtime/)
    * [How to stream events from a tool](https://python.langchain.com/docs/how_to/tool_stream_events/)
    * [How to stream tool calls](https://python.langchain.com/docs/how_to/tool_streaming/)
    * [How to convert tools to OpenAI Functions](https://python.langchain.com/docs/how_to/tools_as_openai_functions/)
    * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)
    * [How to use few-shot prompting with tool calling](https://python.langchain.com/docs/how_to/tools_few_shot/)
    * [How to add a human-in-the-loop for tools](https://python.langchain.com/docs/how_to/tools_human/)
    * [How to bind model-specific tools](https://python.langchain.com/docs/how_to/tools_model_specific/)
    * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)
    * [How to create and query vector stores](https://python.langchain.com/docs/how_to/vectorstores/)
  * [Conceptual guide](https://python.langchain.com/docs/concepts/)
    * [Agents](https://python.langchain.com/docs/concepts/agents/)
    * [Architecture](https://python.langchain.com/docs/concepts/architecture/)
    * [Async programming with langchain](https://python.langchain.com/docs/concepts/async/)
    * [Callbacks](https://python.langchain.com/docs/concepts/callbacks/)
    * [Chat history](https://python.langchain.com/docs/concepts/chat_history/)
    * [Chat models](https://python.langchain.com/docs/concepts/chat_models/)
    * [Document loaders](https://python.langchain.com/docs/concepts/document_loaders/)
    * [Embedding models](https://python.langchain.com/docs/concepts/embedding_models/)
    * [Evaluation](https://python.langchain.com/docs/concepts/evaluation/)
    * [Example selectors](https://python.langchain.com/docs/concepts/example_selectors/)
    * [Few-shot prompting](https://python.langchain.com/docs/concepts/few_shot_prompting/)
    * [Conceptual guide](https://python.langchain.com/docs/concepts/)
    * [Key-value stores](https://python.langchain.com/docs/concepts/key_value_stores/)
    * [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/concepts/lcel/)
    * [Messages](https://python.langchain.com/docs/concepts/messages/)
    * [Multimodality](https://python.langchain.com/docs/concepts/multimodality/)
    * [Output parsers](https://python.langchain.com/docs/concepts/output_parsers/)
    * [Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/)
    * [Retrieval augmented generation (RAG)](https://python.langchain.com/docs/concepts/rag/)
    * [Retrieval](https://python.langchain.com/docs/concepts/retrieval/)
    * [Retrievers](https://python.langchain.com/docs/concepts/retrievers/)
    * [Runnable interface](https://python.langchain.com/docs/concepts/runnables/)
    * [Streaming](https://python.langchain.com/docs/concepts/streaming/)
    * [Structured outputs](https://python.langchain.com/docs/concepts/structured_outputs/)
    * [Testing](https://python.langchain.com/docs/concepts/testing/)
    * [String-in, string-out llms](https://python.langchain.com/docs/concepts/text_llms/)
    * [Text splitters](https://python.langchain.com/docs/concepts/text_splitters/)
    * [Tokens](https://python.langchain.com/docs/concepts/tokens/)
    * [Tool calling](https://python.langchain.com/docs/concepts/tool_calling/)
    * [Tools](https://python.langchain.com/docs/concepts/tools/)
    * [Tracing](https://python.langchain.com/docs/concepts/tracing/)
    * [Vector stores](https://python.langchain.com/docs/concepts/vectorstores/)
    * [Why LangChain?](https://python.langchain.com/docs/concepts/why_langchain/)
  * Ecosystem
    * [🦜🛠️ LangSmith](https://docs.smith.langchain.com/)
    * [🦜🕸️ LangGraph](https://langchain-ai.github.io/langgraph/)
  * Versions
    * [v0.3](https://python.langchain.com/docs/versions/v0_3/)
    * [v0.2](https://python.langchain.com/docs/how_to/function_calling/)
    * [Pydantic compatibility](https://python.langchain.com/docs/how_to/pydantic_compatibility/)
    * [Migrating from v0.0 chains](https://python.langchain.com/docs/versions/migrating_chains/)
      * [How to migrate from v0.0 chains](https://python.langchain.com/docs/versions/migrating_chains/)
      * [Migrating from ConstitutionalChain](https://python.langchain.com/docs/versions/migrating_chains/constitutional_chain/)
      * [Migrating from ConversationalChain](https://python.langchain.com/docs/versions/migrating_chains/conversation_chain/)
      * [Migrating from ConversationalRetrievalChain](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/)
      * [Migrating from LLMChain](https://python.langchain.com/docs/versions/migrating_chains/llm_chain/)
      * [Migrating from LLMMathChain](https://python.langchain.com/docs/versions/migrating_chains/llm_math_chain/)
      * [Migrating from LLMRouterChain](https://python.langchain.com/docs/versions/migrating_chains/llm_router_chain/)
      * [Migrating from MapReduceDocumentsChain](https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain/)
      * [Migrating from MapRerankDocumentsChain](https://python.langchain.com/docs/versions/migrating_chains/map_rerank_docs_chain/)
      * [Migrating from MultiPromptChain](https://python.langchain.com/docs/versions/migrating_chains/multi_prompt_chain/)
      * [Migrating from RefineDocumentsChain](https://python.langchain.com/docs/versions/migrating_chains/refine_docs_chain/)
      * [Migrating from RetrievalQA](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)
      * [Migrating from StuffDocumentsChain](https://python.langchain.com/docs/versions/migrating_chains/stuff_docs_chain/)
    * [Upgrading to LangGraph memory](https://python.langchain.com/docs/versions/migrating_memory/)
      * [How to migrate to LangGraph memory](https://python.langchain.com/docs/versions/migrating_memory/)
      * [How to use BaseChatMessageHistory with LangGraph](https://python.langchain.com/docs/versions/migrating_memory/chat_history/)
      * [Migrating off ConversationBufferMemory or ConversationStringBufferMemory](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_memory/)
      * [Migrating off ConversationBufferWindowMemory or ConversationTokenBufferMemory](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/)
      * [Migrating off ConversationSummaryMemory or ConversationSummaryBufferMemory](https://python.langchain.com/docs/versions/migrating_memory/conversation_summary_memory/)
      * [A Long-Term Memory Agent](https://python.langchain.com/docs/versions/migrating_memory/long_term_memory_agent/)
    * [Release policy](https://python.langchain.com/docs/versions/release_policy/)
  * [Security Policy](https://python.langchain.com/docs/security/)


  * [](https://python.langchain.com/)
  * [How-to guides](https://python.langchain.com/docs/how_to/)
  * How to do tool/function calling


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/how_to/function_calling.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/function_calling.ipynb)
# How to do tool/function calling
info
We use the term tool calling interchangeably with function calling. Although function calling is sometimes meant to refer to invocations of a single function, we treat all models as though they can return multiple tool or function calls in each message.
Tool calling allows a model to respond to a given prompt by generating output that matches a user-defined schema. While the name implies that the model is performing some action, this is actually not the case! The model is coming up with the arguments to a tool, and actually running the tool (or not) is up to the user - for example, if you want to [extract output matching some schema](https://python.langchain.com/docs/tutorials/extraction/) from unstructured text, you could give the model an "extraction" tool that takes parameters matching the desired schema, then treat the generated output as your final result.
A tool call includes a name, arguments dict, and an optional identifier. The arguments dict is structured `{argument_name: argument_value}`.
Many LLM providers, including [Anthropic](https://www.anthropic.com/), [Cohere](https://cohere.com/), [Google](https://cloud.google.com/vertex-ai), [Mistral](https://mistral.ai/), [OpenAI](https://openai.com/), and others, support variants of a tool calling feature. These features typically allow requests to the LLM to include available tools and their schemas, and for responses to include calls to these tools. For instance, given a search engine tool, an LLM might handle a query by first issuing a call to the search engine. The system calling the LLM can receive the tool call, execute it, and return the output to the LLM to inform its response. LangChain includes a suite of [built-in tools](https://python.langchain.com/docs/integrations/tools/) and supports several methods for defining your own [custom tools](https://python.langchain.com/docs/how_to/custom_tools/). Tool-calling is extremely useful for building [tool-using chains and agents](https://python.langchain.com/docs/how_to/#tools), and for getting structured outputs from models more generally.
Providers adopt different conventions for formatting tool schemas and tool calls. For instance, Anthropic returns tool calls as parsed structures within a larger content block:
```
[{"text":"<thinking>\nI should use a tool.\n</thinking>","type":"text"},{"id":"id_value","input":{"arg_name":"arg_value"},"name":"tool_name","type":"tool_use"}]
```

whereas OpenAI separates tool calls into a distinct parameter, with arguments as JSON strings:
```
{"tool_calls":[{"id":"id_value","function":{"arguments":'{"arg_name": "arg_value"}',"name":"tool_name"},"type":"function"}]}
```

LangChain implements standard interfaces for defining tools, passing them to LLMs, and representing tool calls.
## Passing tools to LLMs[​](https://python.langchain.com/docs/how_to/function_calling/#passing-tools-to-llms "Direct link to Passing tools to LLMs")
Chat models supporting tool calling features implement a `.bind_tools` method, which receives a list of LangChain [tool objects](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.BaseTool.html#langchain_core.tools.BaseTool) and binds them to the chat model in its expected format. Subsequent invocations of the chat model will include tool schemas in its calls to the LLM.
For example, we can define the schema for custom tools using the `@tool` decorator on Python functions:
```
from langchain_core.tools import tool@tooldefadd(a:int, b:int)->int:"""Adds a and b."""return a + b@tooldefmultiply(a:int, b:int)->int:"""Multiplies a and b."""return a * btools =[add, multiply]
```

**API Reference:**[tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)
Or below, we define the schema using Pydantic:
```
from pydantic import BaseModel, Field# Note that the docstrings here are crucial, as they will be passed along# to the model along with the class name.classAdd(BaseModel):"""Add two integers together."""  a:int= Field(..., description="First integer")  b:int= Field(..., description="Second integer")classMultiply(BaseModel):"""Multiply two integers together."""  a:int= Field(..., description="First integer")  b:int= Field(..., description="Second integer")tools =[Add, Multiply]
```

We can bind them to chat models as follows:
Select [chat model](https://python.langchain.com/docs/integrations/chat/):
OpenAI▾
* [OpenAI](https://python.langchain.com/docs/how_to/function_calling/)
* [Anthropic](https://python.langchain.com/docs/how_to/function_calling/)
* [Azure](https://python.langchain.com/docs/how_to/function_calling/)
* [Google Gemini](https://python.langchain.com/docs/how_to/function_calling/)
* [Google Vertex](https://python.langchain.com/docs/how_to/function_calling/)
* [AWS](https://python.langchain.com/docs/how_to/function_calling/)
* [Groq](https://python.langchain.com/docs/how_to/function_calling/)
* [Cohere](https://python.langchain.com/docs/how_to/function_calling/)
* [NVIDIA](https://python.langchain.com/docs/how_to/function_calling/)
* [Fireworks AI](https://python.langchain.com/docs/how_to/function_calling/)
* [Mistral AI](https://python.langchain.com/docs/how_to/function_calling/)
* [Together AI](https://python.langchain.com/docs/how_to/function_calling/)
* [IBM watsonx](https://python.langchain.com/docs/how_to/function_calling/)
* [Databricks](https://python.langchain.com/docs/how_to/function_calling/)
* [xAI](https://python.langchain.com/docs/how_to/function_calling/)
* [Perplexity](https://python.langchain.com/docs/how_to/function_calling/)
```
pip install -qU "langchain[openai]"
```

```
import getpassimport osifnot os.environ.get("OPENAI_API_KEY"): os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter API key for OpenAI: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("gpt-4o-mini", model_provider="openai")
```

We can use the `bind_tools()` method to handle converting `Multiply` to a "tool" and binding it to the model (i.e., passing it in each time the model is invoked).
```
llm_with_tools = llm.bind_tools(tools)
```

## Tool calls[​](https://python.langchain.com/docs/how_to/function_calling/#tool-calls "Direct link to Tool calls")
If tool calls are included in a LLM response, they are attached to the corresponding [message](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage) or [message chunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk) as a list of [tool call](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall) objects in the `.tool_calls` attribute. A `ToolCall` is a typed dict that includes a tool name, dict of argument values, and (optionally) an identifier. Messages with no tool calls default to an empty list for this attribute.
Example:
```
query ="What is 3 * 12? Also, what is 11 + 49?"llm_with_tools.invoke(query).tool_calls
```

```
[{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_1Tdp5wUXbYQzpkBoagGXqUTo'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_k9v09vYioS3X0Qg35zESuUKI'}]
```

The `.tool_calls` attribute should contain valid tool calls. Note that on occasion, model providers may output malformed tool calls (e.g., arguments that are not valid JSON). When parsing fails in these cases, instances of [InvalidToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall) are populated in the `.invalid_tool_calls` attribute. An `InvalidToolCall` can have a name, string arguments, identifier, and error message.
If desired, [output parsers](https://python.langchain.com/docs/how_to/#output-parsers) can further process the output. For example, we can convert back to the original Pydantic class:
```
from langchain_core.output_parsers.openai_tools import PydanticToolsParserchain = llm_with_tools | PydanticToolsParser(tools=[Multiply, Add])chain.invoke(query)
```

**API Reference:**[PydanticToolsParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.PydanticToolsParser.html)
```
[Multiply(a=3, b=12), Add(a=11, b=49)]
```

### Streaming[​](https://python.langchain.com/docs/how_to/function_calling/#streaming "Direct link to Streaming")
When tools are called in a streaming context, [message chunks](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk) will be populated with [tool call chunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCallChunk.html#langchain_core.messages.tool.ToolCallChunk) objects in a list via the `.tool_call_chunks` attribute. A `ToolCallChunk` includes optional string fields for the tool `name`, `args`, and `id`, and includes an optional integer field `index` that can be used to join chunks together. Fields are optional because portions of a tool call may be streamed across different chunks (e.g., a chunk that includes a substring of the arguments may have null values for the tool name and id).
Because message chunks inherit from their parent message class, an [AIMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk) with tool call chunks will also include `.tool_calls` and `.invalid_tool_calls` fields. These fields are parsed best-effort from the message's tool call chunks.
Note that not all providers currently support streaming for tool calls.
Example:
```
asyncfor chunk in llm_with_tools.astream(query):print(chunk.tool_call_chunks)
```

```
[][{'name': 'Multiply', 'args': '', 'id': 'call_d39MsxKM5cmeGJOoYKdGBgzc', 'index': 0}][{'name': None, 'args': '{"a"', 'id': None, 'index': 0}][{'name': None, 'args': ': 3, ', 'id': None, 'index': 0}][{'name': None, 'args': '"b": 1', 'id': None, 'index': 0}][{'name': None, 'args': '2}', 'id': None, 'index': 0}][{'name': 'Add', 'args': '', 'id': 'call_QJpdxD9AehKbdXzMHxgDMMhs', 'index': 1}][{'name': None, 'args': '{"a"', 'id': None, 'index': 1}][{'name': None, 'args': ': 11,', 'id': None, 'index': 1}][{'name': None, 'args': ' "b": ', 'id': None, 'index': 1}][{'name': None, 'args': '49}', 'id': None, 'index': 1}][]
```

Note that adding message chunks will merge their corresponding tool call chunks. This is the principle by which LangChain's various [tool output parsers](https://python.langchain.com/docs/how_to/output_parser_structured/) support streaming.
For example, below we accumulate tool call chunks:
```
first =Trueasyncfor chunk in llm_with_tools.astream(query):if first:    gathered = chunk    first =Falseelse:    gathered = gathered + chunkprint(gathered.tool_call_chunks)
```

```
[][{'name': 'Multiply', 'args': '', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}][{'name': 'Multiply', 'args': '{"a"', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}][{'name': 'Multiply', 'args': '{"a": 3, ', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}][{'name': 'Multiply', 'args': '{"a": 3, "b": 1', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a"', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a": 11,', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": ', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": 49}', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": 49}', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}]
```

```
print(type(gathered.tool_call_chunks[0]["args"]))
```

```
<class 'str'>
```

And below we accumulate tool calls to demonstrate partial parsing:
```
first =Trueasyncfor chunk in llm_with_tools.astream(query):if first:    gathered = chunk    first =Falseelse:    gathered = gathered + chunkprint(gathered.tool_calls)
```

```
[][][{'name': 'Multiply', 'args': {}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}][{'name': 'Multiply', 'args': {'a': 3}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 1}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {'a': 11}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {'a': 11}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}]
```

```
print(type(gathered.tool_calls[0]["args"]))
```

```
<class 'dict'>
```

## Passing tool outputs to model[​](https://python.langchain.com/docs/how_to/function_calling/#passing-tool-outputs-to-model "Direct link to Passing tool outputs to model")
If we're using the model-generated tool invocations to actually call tools and want to pass the tool results back to the model, we can do so using `ToolMessage`s.
```
from langchain_core.messages import HumanMessage, ToolMessagemessages =[HumanMessage(query)]ai_msg = llm_with_tools.invoke(messages)messages.append(ai_msg)for tool_call in ai_msg.tool_calls:  selected_tool ={"add": add,"multiply": multiply}[tool_call["name"].lower()]  tool_output = selected_tool.invoke(tool_call["args"])  messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))messages
```

**API Reference:**[HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html)
```
[HumanMessage(content='What is 3 * 12? Also, what is 11 + 49?'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_K5DsWEmgt6D08EI9AFu9NaL1', 'function': {'arguments': '{"a": 3, "b": 12}', 'name': 'Multiply'}, 'type': 'function'}, {'id': 'call_qywVrsplg0ZMv7LHYYMjyG81', 'function': {'arguments': '{"a": 11, "b": 49}', 'name': 'Add'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 50, 'prompt_tokens': 105, 'total_tokens': 155}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_b28b39ffa8', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-1a0b8cdd-9221-4d94-b2ed-5701f67ce9fe-0', tool_calls=[{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_K5DsWEmgt6D08EI9AFu9NaL1'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_qywVrsplg0ZMv7LHYYMjyG81'}]), ToolMessage(content='36', tool_call_id='call_K5DsWEmgt6D08EI9AFu9NaL1'), ToolMessage(content='60', tool_call_id='call_qywVrsplg0ZMv7LHYYMjyG81')]
```

```
llm_with_tools.invoke(messages)
```

```
AIMessage(content='3 * 12 is 36 and 11 + 49 is 60.', response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 171, 'total_tokens': 189}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_b28b39ffa8', 'finish_reason': 'stop', 'logprobs': None}, id='run-a6c8093c-b16a-4c92-8308-7c9ac998118c-0')
```

## Few-shot prompting[​](https://python.langchain.com/docs/how_to/function_calling/#few-shot-prompting "Direct link to Few-shot prompting")
For more complex tool use it's very useful to add few-shot examples to the prompt. We can do this by adding `AIMessage`s with `ToolCall`s and corresponding `ToolMessage`s to our prompt.
For example, even with some special instructions our model can get tripped up by order of operations:
```
llm_with_tools.invoke("Whats 119 times 8 minus 20. Don't do any math yourself, only use tools for math. Respect order of operations").tool_calls
```

```
[{'name': 'Multiply', 'args': {'a': 119, 'b': 8}, 'id': 'call_Dl3FXRVkQCFW4sUNYOe4rFr7'}, {'name': 'Add', 'args': {'a': 952, 'b': -20}, 'id': 'call_n03l4hmka7VZTCiP387Wud2C'}]
```

The model shouldn't be trying to add anything yet, since it technically can't know the results of 119 * 8 yet.
By adding a prompt with some examples we can correct this behavior:
```
from langchain_core.messages import AIMessagefrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughexamples =[  HumanMessage("What's the product of 317253 and 128472 plus four", name="example_user"),  AIMessage("",    name="example_assistant",    tool_calls=[{"name":"Multiply","args":{"x":317253,"y":128472},"id":"1"}],),  ToolMessage("16505054784", tool_call_id="1"),  AIMessage("",    name="example_assistant",    tool_calls=[{"name":"Add","args":{"x":16505054784,"y":4},"id":"2"}],),  ToolMessage("16505054788", tool_call_id="2"),  AIMessage("The product of 317253 and 128472 plus four is 16505054788",    name="example_assistant",),]system ="""You are bad at math but are an expert at using a calculator. Use past tool usage as an example of how to correctly use the tools."""few_shot_prompt = ChatPromptTemplate.from_messages([("system", system),*examples,("human","{query}"),])chain ={"query": RunnablePassthrough()}| few_shot_prompt | llm_with_toolschain.invoke("Whats 119 times 8 minus 20").tool_calls
```

**API Reference:**[AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [RunnablePassthrough](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.passthrough.RunnablePassthrough.html)
```
[{'name': 'Multiply', 'args': {'a': 119, 'b': 8}, 'id': 'call_MoSgwzIhPxhclfygkYaKIsGZ'}]
```

Seems like we get the correct output this time.
Here's what the [LangSmith trace](https://smith.langchain.com/public/f70550a1-585f-4c9d-a643-13148ab1616f/r) looks like.
## Next steps[​](https://python.langchain.com/docs/how_to/function_calling/#next-steps "Direct link to Next steps")
  * **Output parsing** : See [OpenAI Tools output parsers](https://python.langchain.com/docs/how_to/output_parser_structured/) to learn about extracting the function calling API responses into various formats.
  * **Structured output chains** : [Some models have constructors](https://python.langchain.com/docs/how_to/structured_output/) that handle creating a structured output chain for you.
  * **Tool use** : See how to construct chains and agents that call the invoked tools in [these guides](https://python.langchain.com/docs/how_to/#tools).


[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/how_to/function_calling.ipynb)
#### Was this page helpful?
  * [Passing tools to LLMs](https://python.langchain.com/docs/how_to/function_calling/#passing-tools-to-llms)
  * [Tool calls](https://python.langchain.com/docs/how_to/function_calling/#tool-calls)
    * [Streaming](https://python.langchain.com/docs/how_to/function_calling/#streaming)
  * [Passing tool outputs to model](https://python.langchain.com/docs/how_to/function_calling/#passing-tool-outputs-to-model)
  * [Few-shot prompting](https://python.langchain.com/docs/how_to/function_calling/#few-shot-prompting)
  * [Next steps](https://python.langchain.com/docs/how_to/function_calling/#next-steps)


Community
  * [Twitter](https://twitter.com/LangChainAI)


GitHub
  * [Organization](https://github.com/langchain-ai)
  * [Python](https://github.com/langchain-ai/langchain)
  * [JS/TS](https://github.com/langchain-ai/langchainjs)


More
  * [Homepage](https://langchain.com)
  * [Blog](https://blog.langchain.dev)
  * [YouTube](https://www.youtube.com/@LangChain)


Copyright © 2025 LangChain, Inc.

