---
url: https://python.langchain.com/docs/how_to/debugging/
scraped_at: 2025-05-25T17:56:03.344677
title: How to debug your LLM apps | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/how_to/debugging/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/how_to/debugging/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/how_to/debugging/)
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
    * [v0.2](https://python.langchain.com/docs/how_to/debugging/)
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
  * How to debug your LLM apps


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/how_to/debugging.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/debugging.ipynb)
# How to debug your LLM apps
Like building any type of software, at some point you'll need to debug when building with LLMs. A model call will fail, or model output will be misformatted, or there will be some nested model calls and it won't be clear where along the way an incorrect output was created.
There are three main methods for debugging:
  * Verbose Mode: This adds print statements for "important" events in your chain.
  * Debug Mode: This add logging statements for ALL events in your chain.
  * LangSmith Tracing: This logs events to [LangSmith](https://docs.smith.langchain.com/) to allow for visualization there.

| Verbose Mode| Debug Mode| LangSmith Tracing  
---|---|---|---  
Free| ✅| ✅| ✅  
UI| ❌| ❌| ✅  
Persisted| ❌| ❌| ✅  
See all events| ❌| ✅| ✅  
See "important" events| ✅| ❌| ✅  
Runs Locally| ✅| ✅| ❌  
## Tracing[​](https://python.langchain.com/docs/how_to/debugging/#tracing "Direct link to Tracing")
Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with [LangSmith](https://smith.langchain.com).
After you sign up at the link above, make sure to set your environment variables to start logging traces:
```
export LANGSMITH_TRACING="true"export LANGSMITH_API_KEY="..."
```

Or, if in a notebook, you can set them with:
```
import getpassimport osos.environ["LANGSMITH_TRACING"]="true"os.environ["LANGSMITH_API_KEY"]= getpass.getpass()
```

Let's suppose we have an agent, and want to visualize the actions it takes and tool outputs it receives. Without any debugging, here's what we see:
Select [chat model](https://python.langchain.com/docs/integrations/chat/):
OpenAI▾
* [OpenAI](https://python.langchain.com/docs/how_to/debugging/)
* [Anthropic](https://python.langchain.com/docs/how_to/debugging/)
* [Azure](https://python.langchain.com/docs/how_to/debugging/)
* [Google Gemini](https://python.langchain.com/docs/how_to/debugging/)
* [Google Vertex](https://python.langchain.com/docs/how_to/debugging/)
* [AWS](https://python.langchain.com/docs/how_to/debugging/)
* [Groq](https://python.langchain.com/docs/how_to/debugging/)
* [Cohere](https://python.langchain.com/docs/how_to/debugging/)
* [NVIDIA](https://python.langchain.com/docs/how_to/debugging/)
* [Fireworks AI](https://python.langchain.com/docs/how_to/debugging/)
* [Mistral AI](https://python.langchain.com/docs/how_to/debugging/)
* [Together AI](https://python.langchain.com/docs/how_to/debugging/)
* [IBM watsonx](https://python.langchain.com/docs/how_to/debugging/)
* [Databricks](https://python.langchain.com/docs/how_to/debugging/)
* [xAI](https://python.langchain.com/docs/how_to/debugging/)
* [Perplexity](https://python.langchain.com/docs/how_to/debugging/)
```
pip install -qU "langchain[openai]"
```

```
import getpassimport osifnot os.environ.get("OPENAI_API_KEY"): os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter API key for OpenAI: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("gpt-4o-mini", model_provider="openai")
```

```
from langchain.agents import AgentExecutor, create_tool_calling_agentfrom langchain_community.tools.tavily_search import TavilySearchResultsfrom langchain_core.prompts import ChatPromptTemplatetools =[TavilySearchResults(max_results=1)]prompt = ChatPromptTemplate.from_messages([("system","You are a helpful assistant.",),("placeholder","{chat_history}"),("human","{input}"),("placeholder","{agent_scratchpad}"),])# Construct the Tools agentagent = create_tool_calling_agent(llm, tools, prompt)# Create an agent executor by passing in the agent and toolsagent_executor = AgentExecutor(agent=agent, tools=tools)agent_executor.invoke({"input":"Who directed the 2023 film Oppenheimer and what is their age in days?"})
```

**API Reference:**[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html) | [create_tool_calling_agent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.tool_calling_agent.base.create_tool_calling_agent.html) | [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)
```
{'input': 'Who directed the 2023 film Oppenheimer and what is their age in days?', 'output': 'The 2023 film "Oppenheimer" was directed by Christopher Nolan.\n\nTo calculate Christopher Nolan\'s age in days, we first need his birthdate, which is July 30, 1970. Let\'s calculate his age in days from his birthdate to today\'s date, December 7, 2023.\n\n1. Calculate the total number of days from July 30, 1970, to December 7, 2023.\n2. Nolan was born on July 30, 1970. From July 30, 1970, to July 30, 2023, is 53 years.\n3. From July 30, 2023, to December 7, 2023, is 130 days.\n\nNow, calculate the total days:\n- 53 years = 53 x 365 = 19,345 days\n- Adding leap years from 1970 to 2023: There are 13 leap years (1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020). So, add 13 days.\n- Total days from years and leap years = 19,345 + 13 = 19,358 days\n- Add the days from July 30, 2023, to December 7, 2023 = 130 days\n\nTotal age in days = 19,358 + 130 = 19,488 days\n\nChristopher Nolan is 19,488 days old as of December 7, 2023.'}
```

We don't get much output, but since we set up LangSmith we can easily see what happened under the hood:
<https://smith.langchain.com/public/a89ff88f-9ddc-4757-a395-3a1b365655bf/r>
## `set_debug` and `set_verbose`[​](https://python.langchain.com/docs/how_to/debugging/#set_debug-and-set_verbose "Direct link to set_debug-and-set_verbose")
If you're prototyping in Jupyter Notebooks or running Python scripts, it can be helpful to print out the intermediate steps of a chain run.
There are a number of ways to enable printing at varying degrees of verbosity.
Note: These still work even with LangSmith enabled, so you can have both turned on and running at the same time
### `set_verbose(True)`[​](https://python.langchain.com/docs/how_to/debugging/#set_verbosetrue "Direct link to set_verbosetrue")
Setting the `verbose` flag will print out inputs and outputs in a slightly more readable format and will skip logging certain raw outputs (like the token usage stats for an LLM call) so that you can focus on application logic.
```
from langchain.globalsimport set_verboseset_verbose(True)agent_executor = AgentExecutor(agent=agent, tools=tools)agent_executor.invoke({"input":"Who directed the 2023 film Oppenheimer and what is their age in days?"})
```

**API Reference:**[set_verbose](https://python.langchain.com/api_reference/langchain/globals/langchain.globals.set_verbose.html)
```
[1m> Entering new AgentExecutor chain...[0m[32;1m[1;3mInvoking: `tavily_search_results_json` with `{'query': 'director of the 2023 film Oppenheimer'}`[0m[36;1m[1;3m[{'url': 'https://m.imdb.com/title/tt15398776/', 'content': 'Oppenheimer: Directed by Christopher Nolan. With Cillian Murphy, Emily Blunt, Robert Downey Jr., Alden Ehrenreich. The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb.'}][0m[32;1m[1;3mInvoking: `tavily_search_results_json` with `{'query': 'birth date of Christopher Nolan'}`[0m[36;1m[1;3m[{'url': 'https://m.imdb.com/name/nm0634240/bio/', 'content': 'Christopher Nolan. Writer: Tenet. Best known for his cerebral, often nonlinear, storytelling, acclaimed Academy Award winner writer/director/producer Sir Christopher Nolan CBE was born in London, England. Over the course of more than 25 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made and became one of the most ...'}][0m[32;1m[1;3mInvoking: `tavily_search_results_json` with `{'query': 'Christopher Nolan birth date'}`responded: The 2023 film **Oppenheimer** was directed by **Christopher Nolan**.To calculate Christopher Nolan's age in days, I need his exact birth date. Let me find that information for you.[0m[36;1m[1;3m[{'url': 'https://m.imdb.com/name/nm0634240/bio/', 'content': 'Christopher Nolan. Writer: Tenet. Best known for his cerebral, often nonlinear, storytelling, acclaimed Academy Award winner writer/director/producer Sir Christopher Nolan CBE was born in London, England. Over the course of more than 25 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made and became one of the most ...'}][0m[32;1m[1;3mInvoking: `tavily_search_results_json` with `{'query': 'Christopher Nolan date of birth'}`responded: It appears that I need to refine my search to get the exact birth date of Christopher Nolan. Let me try again to find that specific information.[0m[36;1m[1;3m[{'url': 'https://m.imdb.com/name/nm0634240/bio/', 'content': 'Christopher Nolan. Writer: Tenet. Best known for his cerebral, often nonlinear, storytelling, acclaimed Academy Award winner writer/director/producer Sir Christopher Nolan CBE was born in London, England. Over the course of more than 25 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made and became one of the most ...'}][0m[32;1m[1;3mI am currently unable to retrieve the exact birth date of Christopher Nolan from the sources available. However, it is widely known that he was born on July 30, 1970. Using this date, I can calculate his age in days as of today.Let's calculate:- Christopher Nolan's birth date: July 30, 1970.- Today's date: December 7, 2023.The number of days between these two dates can be calculated as follows:1. From July 30, 1970, to July 30, 2023, is 53 years.2. From July 30, 2023, to December 7, 2023, is 130 days.Calculating the total days for 53 years (considering leap years):- 53 years × 365 days/year = 19,345 days- Adding leap years (1972, 1976, ..., 2020, 2024 - 13 leap years): 13 daysTotal days from birth until July 30, 2023: 19,345 + 13 = 19,358 daysAdding the days from July 30, 2023, to December 7, 2023: 130 daysTotal age in days as of December 7, 2023: 19,358 + 130 = 19,488 days.Therefore, Christopher Nolan is 19,488 days old as of December 7, 2023.[0m[1m> Finished chain.[0m
```

```
{'input': 'Who directed the 2023 film Oppenheimer and what is their age in days?', 'output': "I am currently unable to retrieve the exact birth date of Christopher Nolan from the sources available. However, it is widely known that he was born on July 30, 1970. Using this date, I can calculate his age in days as of today.\n\nLet's calculate:\n\n- Christopher Nolan's birth date: July 30, 1970.\n- Today's date: December 7, 2023.\n\nThe number of days between these two dates can be calculated as follows:\n\n1. From July 30, 1970, to July 30, 2023, is 53 years.\n2. From July 30, 2023, to December 7, 2023, is 130 days.\n\nCalculating the total days for 53 years (considering leap years):\n- 53 years × 365 days/year = 19,345 days\n- Adding leap years (1972, 1976, ..., 2020, 2024 - 13 leap years): 13 days\n\nTotal days from birth until July 30, 2023: 19,345 + 13 = 19,358 days\nAdding the days from July 30, 2023, to December 7, 2023: 130 days\n\nTotal age in days as of December 7, 2023: 19,358 + 130 = 19,488 days.\n\nTherefore, Christopher Nolan is 19,488 days old as of December 7, 2023."}
```

### `set_debug(True)`[​](https://python.langchain.com/docs/how_to/debugging/#set_debugtrue "Direct link to set_debugtrue")
Setting the global `debug` flag will cause all LangChain components with callback support (chains, models, agents, tools, retrievers) to print the inputs they receive and outputs they generate. This is the most verbose setting and will fully log raw inputs and outputs.
```
from langchain.globalsimport set_debugset_debug(True)set_verbose(False)agent_executor = AgentExecutor(agent=agent, tools=tools)agent_executor.invoke({"input":"Who directed the 2023 film Oppenheimer and what is their age in days?"})
```

**API Reference:**[set_debug](https://python.langchain.com/api_reference/langchain/globals/langchain.globals.set_debug.html)
```
[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor] Entering Chain run with input:[0m{ "input": "Who directed the 2023 film Oppenheimer and what is their age in days?"}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence] Entering Chain run with input:[0m{ "input": ""}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 3:chain:RunnableAssign<agent_scratchpad>] Entering Chain run with input:[0m{ "input": ""}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 3:chain:RunnableAssign<agent_scratchpad> > 4:chain:RunnableParallel<agent_scratchpad>] Entering Chain run with input:[0m{ "input": ""}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 3:chain:RunnableAssign<agent_scratchpad> > 4:chain:RunnableParallel<agent_scratchpad> > 5:chain:RunnableLambda] Entering Chain run with input:[0m{ "input": ""}[36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 3:chain:RunnableAssign<agent_scratchpad> > 4:chain:RunnableParallel<agent_scratchpad> > 5:chain:RunnableLambda] [1ms] Exiting Chain run with output:[0m{ "output": []}[36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 3:chain:RunnableAssign<agent_scratchpad> > 4:chain:RunnableParallel<agent_scratchpad>] [2ms] Exiting Chain run with output:[0m{ "agent_scratchpad": []}[36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 3:chain:RunnableAssign<agent_scratchpad>] [5ms] Exiting Chain run with output:[0m{ "input": "Who directed the 2023 film Oppenheimer and what is their age in days?", "intermediate_steps": [], "agent_scratchpad": []}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 6:prompt:ChatPromptTemplate] Entering Prompt run with input:[0m{ "input": "Who directed the 2023 film Oppenheimer and what is their age in days?", "intermediate_steps": [], "agent_scratchpad": []}[36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 6:prompt:ChatPromptTemplate] [1ms] Exiting Prompt run with output:[0m[outputs][32;1m[1;3m[llm/start][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 7:llm:ChatOpenAI] Entering LLM run with input:[0m{ "prompts": [  "System: You are a helpful assistant.\nHuman: Who directed the 2023 film Oppenheimer and what is their age in days?" ]}[36;1m[1;3m[llm/end][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 7:llm:ChatOpenAI] [3.17s] Exiting LLM run with output:[0m{ "generations": [  [   {    "text": "",    "generation_info": {     "finish_reason": "tool_calls"    },    "type": "ChatGenerationChunk",    "message": {     "lc": 1,     "type": "constructor",     "id": [      "langchain",      "schema",      "messages",      "AIMessageChunk"     ],     "kwargs": {      "content": "",      "example": false,      "additional_kwargs": {       "tool_calls": [        {         "index": 0,         "id": "call_fnfq6GjSQED4iF6lo4rxkUup",         "function": {          "arguments": "{\"query\": \"director of the 2023 film Oppenheimer\"}",          "name": "tavily_search_results_json"         },         "type": "function"        },        {         "index": 1,         "id": "call_mwhVi6pk49f4OIo5rOWrr4TD",         "function": {          "arguments": "{\"query\": \"birth date of Christopher Nolan\"}",          "name": "tavily_search_results_json"         },         "type": "function"        }       ]      },      "tool_call_chunks": [       {        "name": "tavily_search_results_json",        "args": "{\"query\": \"director of the 2023 film Oppenheimer\"}",        "id": "call_fnfq6GjSQED4iF6lo4rxkUup",        "index": 0       },       {        "name": "tavily_search_results_json",        "args": "{\"query\": \"birth date of Christopher Nolan\"}",        "id": "call_mwhVi6pk49f4OIo5rOWrr4TD",        "index": 1       }      ],      "response_metadata": {       "finish_reason": "tool_calls"      },      "id": "run-6e160323-15f9-491d-aadf-b5d337e9e2a1",      "tool_calls": [       {        "name": "tavily_search_results_json",        "args": {         "query": "director of the 2023 film Oppenheimer"        },        "id": "call_fnfq6GjSQED4iF6lo4rxkUup"       },       {        "name": "tavily_search_results_json",        "args": {         "query": "birth date of Christopher Nolan"        },        "id": "call_mwhVi6pk49f4OIo5rOWrr4TD"       }      ],      "invalid_tool_calls": []     }    }   }  ] ], "llm_output": null, "run": null}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 8:parser:ToolsAgentOutputParser] Entering Parser run with input:[0m[inputs][36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence > 8:parser:ToolsAgentOutputParser] [1ms] Exiting Parser run with output:[0m[outputs][36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 2:chain:RunnableSequence] [3.18s] Exiting Chain run with output:[0m[outputs][32;1m[1;3m[tool/start][0m [1m[1:chain:AgentExecutor > 9:tool:tavily_search_results_json] Entering Tool run with input:[0m"{'query': 'director of the 2023 film Oppenheimer'}"``````outputError in ConsoleCallbackHandler.on_tool_end callback: AttributeError("'list' object has no attribute 'strip'")``````output[32;1m[1;3m[tool/start][0m [1m[1:chain:AgentExecutor > 10:tool:tavily_search_results_json] Entering Tool run with input:[0m"{'query': 'birth date of Christopher Nolan'}"``````outputError in ConsoleCallbackHandler.on_tool_end callback: AttributeError("'list' object has no attribute 'strip'")``````output[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence] Entering Chain run with input:[0m{ "input": ""}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 12:chain:RunnableAssign<agent_scratchpad>] Entering Chain run with input:[0m{ "input": ""}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 12:chain:RunnableAssign<agent_scratchpad> > 13:chain:RunnableParallel<agent_scratchpad>] Entering Chain run with input:[0m{ "input": ""}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 12:chain:RunnableAssign<agent_scratchpad> > 13:chain:RunnableParallel<agent_scratchpad> > 14:chain:RunnableLambda] Entering Chain run with input:[0m{ "input": ""}[36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 12:chain:RunnableAssign<agent_scratchpad> > 13:chain:RunnableParallel<agent_scratchpad> > 14:chain:RunnableLambda] [1ms] Exiting Chain run with output:[0m[outputs][36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 12:chain:RunnableAssign<agent_scratchpad> > 13:chain:RunnableParallel<agent_scratchpad>] [4ms] Exiting Chain run with output:[0m[outputs][36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 12:chain:RunnableAssign<agent_scratchpad>] [8ms] Exiting Chain run with output:[0m[outputs][32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 15:prompt:ChatPromptTemplate] Entering Prompt run with input:[0m[inputs][36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 15:prompt:ChatPromptTemplate] [1ms] Exiting Prompt run with output:[0m[outputs][32;1m[1;3m[llm/start][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 16:llm:ChatOpenAI] Entering LLM run with input:[0m{ "prompts": [  "System: You are a helpful assistant.\nHuman: Who directed the 2023 film Oppenheimer and what is their age in days?\nAI: \nTool: [{\"url\": \"https://m.imdb.com/title/tt15398776/fullcredits/\", \"content\": \"Oppenheimer (2023) cast and crew credits, including actors, actresses, directors, writers and more. Menu. ... director of photography: behind-the-scenes Jason Gary ... best boy grip ... film loader Luc Poullain ... aerial coordinator\"}]\nTool: [{\"url\": \"https://en.wikipedia.org/wiki/Christopher_Nolan\", \"content\": \"In early 2003, Nolan approached Warner Bros. with the idea of making a new Batman film, based on the character's origin story.[58] Nolan was fascinated by the notion of grounding it in a more realistic world than a comic-book fantasy.[59] He relied heavily on traditional stunts and miniature effects during filming, with minimal use of computer-generated imagery (CGI).[60] Batman Begins (2005), the biggest project Nolan had undertaken to that point,[61] was released to critical acclaim and commercial success.[62][63] Starring Christian Bale as Bruce Wayne / Batman—along with Michael Caine, Gary Oldman, Morgan Freeman and Liam Neeson—Batman Begins revived the franchise.[64][65] Batman Begins was 2005's ninth-highest-grossing film and was praised for its psychological depth and contemporary relevance;[63][66] it is cited as one of the most influential films of the 2000s.[67] Film author Ian Nathan wrote that within five years of his career, Nolan \\\"[went] from unknown to indie darling to gaining creative control over one of the biggest properties in Hollywood, and (perhaps unwittingly) fomenting the genre that would redefine the entire industry\\\".[68]\\nNolan directed, co-wrote and produced The Prestige (2006), an adaptation of the Christopher Priest novel about two rival 19th-century magicians.[69] He directed, wrote and edited the short film Larceny (1996),[19] which was filmed over a weekend in black and white with limited equipment and a small cast and crew.[12][20] Funded by Nolan and shot with the UCL Union Film society's equipment, it appeared at the Cambridge Film Festival in 1996 and is considered one of UCL's best shorts.[21] For unknown reasons, the film has since been removed from public view.[19] Nolan filmed a third short, Doodlebug (1997), about a man seemingly chasing an insect with his shoe, only to discover that it is a miniature of himself.[14][22] Nolan and Thomas first attempted to make a feature in the mid-1990s with Larry Mahoney, which they scrapped.[23] During this period in his career, Nolan had little to no success getting his projects off the ground, facing several rejections; he added, \\\"[T]here's a very limited pool of finance in the UK. Philosophy professor David Kyle Johnson wrote that \\\"Inception became a classic almost as soon as it was projected on silver screens\\\", praising its exploration of philosophical ideas, including leap of faith and allegory of the cave.[97] The film grossed over $836 million worldwide.[98] Nominated for eight Academy Awards—including Best Picture and Best Original Screenplay—it won Best Cinematography, Best Sound Mixing, Best Sound Editing and Best Visual Effects.[99] Nolan was nominated for a BAFTA Award and a Golden Globe Award for Best Director, among other accolades.[40]\\nAround the release of The Dark Knight Rises (2012), Nolan's third and final Batman film, Joseph Bevan of the British Film Institute wrote a profile on him: \\\"In the space of just over a decade, Christopher Nolan has shot from promising British indie director to undisputed master of a new brand of intelligent escapism. He further wrote that Nolan's body of work reflect \\\"a heterogeneity of conditions of products\\\" extending from low-budget films to lucrative blockbusters, \\\"a wide range of genres and settings\\\" and \\\"a diversity of styles that trumpet his versatility\\\".[193]\\nDavid Bordwell, a film theorist, wrote that Nolan has been able to blend his \\\"experimental impulses\\\" with the demands of mainstream entertainment, describing his oeuvre as \\\"experiments with cinematic time by means of techniques of subjective viewpoint and crosscutting\\\".[194] Nolan's use of practical, in-camera effects, miniatures and models, as well as shooting on celluloid film, has been highly influential in early 21st century cinema.[195][196] IndieWire wrote in 2019 that, Nolan \\\"kept a viable alternate model of big-budget filmmaking alive\\\", in an era where blockbuster filmmaking has become \\\"a largely computer-generated art form\\\".[196] Initially reluctant to make a sequel, he agreed after Warner Bros. repeatedly insisted.[78] Nolan wanted to expand on the noir quality of the first film by broadening the canvas and taking on \\\"the dynamic of a story of the city, a large crime story ... where you're looking at the police, the justice system, the vigilante, the poor people, the rich people, the criminals\\\".[79] Continuing to minimalise the use of CGI, Nolan employed high-resolution IMAX cameras, making it the first major motion picture to use this technology.[80][81]\"}]" ]}[36;1m[1;3m[llm/end][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 16:llm:ChatOpenAI] [20.22s] Exiting LLM run with output:[0m{ "generations": [  [   {    "text": "The 2023 film \"Oppenheimer\" was directed by Christopher Nolan.\n\nTo calculate Christopher Nolan's age in days, we first need his birth date, which is July 30, 1970. Let's calculate his age in days from his birth date to today's date, December 7, 2023.\n\n1. Calculate the total number of days from July 30, 1970, to December 7, 2023.\n2. Christopher Nolan was born on July 30, 1970. From July 30, 1970, to July 30, 2023, is 53 years.\n3. From July 30, 2023, to December 7, 2023, is 130 days.\n\nNow, calculate the total days for 53 years:\n- Each year has 365 days, so 53 years × 365 days/year = 19,345 days.\n- Adding the leap years from 1970 to 2023: 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, and 2024 (up to February). This gives us 14 leap years.\n- Total days from leap years: 14 days.\n\nAdding all together:\n- Total days = 19,345 days (from years) + 14 days (from leap years) + 130 days (from July 30, 2023, to December 7, 2023) = 19,489 days.\n\nTherefore, as of December 7, 2023, Christopher Nolan is 19,489 days old.",    "generation_info": {     "finish_reason": "stop"    },    "type": "ChatGenerationChunk",    "message": {     "lc": 1,     "type": "constructor",     "id": [      "langchain",      "schema",      "messages",      "AIMessageChunk"     ],     "kwargs": {      "content": "The 2023 film \"Oppenheimer\" was directed by Christopher Nolan.\n\nTo calculate Christopher Nolan's age in days, we first need his birth date, which is July 30, 1970. Let's calculate his age in days from his birth date to today's date, December 7, 2023.\n\n1. Calculate the total number of days from July 30, 1970, to December 7, 2023.\n2. Christopher Nolan was born on July 30, 1970. From July 30, 1970, to July 30, 2023, is 53 years.\n3. From July 30, 2023, to December 7, 2023, is 130 days.\n\nNow, calculate the total days for 53 years:\n- Each year has 365 days, so 53 years × 365 days/year = 19,345 days.\n- Adding the leap years from 1970 to 2023: 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, and 2024 (up to February). This gives us 14 leap years.\n- Total days from leap years: 14 days.\n\nAdding all together:\n- Total days = 19,345 days (from years) + 14 days (from leap years) + 130 days (from July 30, 2023, to December 7, 2023) = 19,489 days.\n\nTherefore, as of December 7, 2023, Christopher Nolan is 19,489 days old.",      "example": false,      "additional_kwargs": {},      "tool_call_chunks": [],      "response_metadata": {       "finish_reason": "stop"      },      "id": "run-1c08a44f-db70-4836-935b-417caaf422a5",      "tool_calls": [],      "invalid_tool_calls": []     }    }   }  ] ], "llm_output": null, "run": null}[32;1m[1;3m[chain/start][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 17:parser:ToolsAgentOutputParser] Entering Parser run with input:[0m[inputs][36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence > 17:parser:ToolsAgentOutputParser] [2ms] Exiting Parser run with output:[0m[outputs][36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor > 11:chain:RunnableSequence] [20.27s] Exiting Chain run with output:[0m[outputs][36;1m[1;3m[chain/end][0m [1m[1:chain:AgentExecutor] [26.37s] Exiting Chain run with output:[0m{ "output": "The 2023 film \"Oppenheimer\" was directed by Christopher Nolan.\n\nTo calculate Christopher Nolan's age in days, we first need his birth date, which is July 30, 1970. Let's calculate his age in days from his birth date to today's date, December 7, 2023.\n\n1. Calculate the total number of days from July 30, 1970, to December 7, 2023.\n2. Christopher Nolan was born on July 30, 1970. From July 30, 1970, to July 30, 2023, is 53 years.\n3. From July 30, 2023, to December 7, 2023, is 130 days.\n\nNow, calculate the total days for 53 years:\n- Each year has 365 days, so 53 years × 365 days/year = 19,345 days.\n- Adding the leap years from 1970 to 2023: 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, and 2024 (up to February). This gives us 14 leap years.\n- Total days from leap years: 14 days.\n\nAdding all together:\n- Total days = 19,345 days (from years) + 14 days (from leap years) + 130 days (from July 30, 2023, to December 7, 2023) = 19,489 days.\n\nTherefore, as of December 7, 2023, Christopher Nolan is 19,489 days old."}
```

```
{'input': 'Who directed the 2023 film Oppenheimer and what is their age in days?', 'output': 'The 2023 film "Oppenheimer" was directed by Christopher Nolan.\n\nTo calculate Christopher Nolan\'s age in days, we first need his birth date, which is July 30, 1970. Let\'s calculate his age in days from his birth date to today\'s date, December 7, 2023.\n\n1. Calculate the total number of days from July 30, 1970, to December 7, 2023.\n2. Christopher Nolan was born on July 30, 1970. From July 30, 1970, to July 30, 2023, is 53 years.\n3. From July 30, 2023, to December 7, 2023, is 130 days.\n\nNow, calculate the total days for 53 years:\n- Each year has 365 days, so 53 years × 365 days/year = 19,345 days.\n- Adding the leap years from 1970 to 2023: 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, and 2024 (up to February). This gives us 14 leap years.\n- Total days from leap years: 14 days.\n\nAdding all together:\n- Total days = 19,345 days (from years) + 14 days (from leap years) + 130 days (from July 30, 2023, to December 7, 2023) = 19,489 days.\n\nTherefore, as of December 7, 2023, Christopher Nolan is 19,489 days old.'}
```

[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/how_to/debugging.ipynb)
#### Was this page helpful?
  * [Tracing](https://python.langchain.com/docs/how_to/debugging/#tracing)
  * [`set_debug` and `set_verbose`](https://python.langchain.com/docs/how_to/debugging/#set_debug-and-set_verbose)
    * [`set_verbose(True)`](https://python.langchain.com/docs/how_to/debugging/#set_verbosetrue)
    * [`set_debug(True)`](https://python.langchain.com/docs/how_to/debugging/#set_debugtrue)


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

