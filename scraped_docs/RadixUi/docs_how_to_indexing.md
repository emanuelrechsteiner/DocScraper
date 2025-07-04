---
url: https://python.langchain.com/docs/how_to/indexing/
scraped_at: 2025-05-25T18:08:35.595022
title: How to use the LangChain indexing API | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/how_to/indexing/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/how_to/indexing/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/how_to/indexing/)
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
    * [v0.2](https://python.langchain.com/docs/how_to/indexing/)
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
  * How to use the LangChain indexing API


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/how_to/indexing.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/indexing.ipynb)
# How to use the LangChain indexing API
Here, we will look at a basic indexing workflow using the LangChain indexing API.
The indexing API lets you load and keep in sync documents from any source into a [vector store](https://python.langchain.com/docs/concepts/vectorstores/). Specifically, it helps:
  * Avoid writing duplicated content into the vector store
  * Avoid re-writing unchanged content
  * Avoid re-computing embeddings over unchanged content


All of which should save you time and money, as well as improve your vector search results.
Crucially, the indexing API will work even with documents that have gone through several transformation steps (e.g., via text chunking) with respect to the original source documents.
## How it works[​](https://python.langchain.com/docs/how_to/indexing/#how-it-works "Direct link to How it works")
LangChain indexing makes use of a record manager (`RecordManager`) that keeps track of document writes into the vector store.
When indexing content, hashes are computed for each document, and the following information is stored in the record manager:
  * the document hash (hash of both page content and metadata)
  * write time
  * the source id -- each document should include information in its metadata to allow us to determine the ultimate source of this document


## Deletion modes[​](https://python.langchain.com/docs/how_to/indexing/#deletion-modes "Direct link to Deletion modes")
When indexing documents into a vector store, it's possible that some existing documents in the vector store should be deleted. In certain situations you may want to remove any existing documents that are derived from the same sources as the new documents being indexed. In others you may want to delete all existing documents wholesale. The indexing API deletion modes let you pick the behavior you want:
Cleanup Mode| De-Duplicates Content| Parallelizable| Cleans Up Deleted Source Docs| Cleans Up Mutations of Source Docs and/or Derived Docs| Clean Up Timing  
---|---|---|---|---|---  
None| ✅| ✅| ❌| ❌| -  
Incremental| ✅| ✅| ❌| ✅| Continuously  
Full| ✅| ❌| ✅| ✅| At end of indexing  
Scoped_Full| ✅| ✅| ❌| ✅| At end of indexing  
`None` does not do any automatic clean up, allowing the user to manually do clean up of old content.
`incremental`, `full` and `scoped_full` offer the following automated clean up:
  * If the content of the source document or derived documents has **changed** , all 3 modes will clean up (delete) previous versions of the content.
  * If the source document has been **deleted** (meaning it is not included in the documents currently being indexed), the `full` cleanup mode will delete it from the vector store correctly, but the `incremental` and `scoped_full` mode will not.


When content is mutated (e.g., the source PDF file was revised) there will be a period of time during indexing when both the new and old versions may be returned to the user. This happens after the new content was written, but before the old version was deleted.
  * `incremental` indexing minimizes this period of time as it is able to do clean up continuously, as it writes.
  * `full` and `scoped_full` mode does the clean up after all batches have been written.


## Requirements[​](https://python.langchain.com/docs/how_to/indexing/#requirements "Direct link to Requirements")
  1. Do not use with a store that has been pre-populated with content independently of the indexing API, as the record manager will not know that records have been inserted previously.
  2. Only works with LangChain `vectorstore`'s that support: 
     * document addition by id (`add_documents` method with `ids` argument)
     * delete by id (`delete` method with `ids` argument)


Compatible Vectorstores: `Aerospike`, `AnalyticDB`, `AstraDB`, `AwaDB`, `AzureCosmosDBNoSqlVectorSearch`, `AzureCosmosDBVectorSearch`, `AzureSearch`, `Bagel`, `Cassandra`, `Chroma`, `CouchbaseVectorStore`, `DashVector`, `DatabricksVectorSearch`, `DeepLake`, `Dingo`, `ElasticVectorSearch`, `ElasticsearchStore`, `FAISS`, `HanaDB`, `Milvus`, `MongoDBAtlasVectorSearch`, `MyScale`, `OpenSearchVectorSearch`, `PGVector`, `Pinecone`, `Qdrant`, `Redis`, `Rockset`, `ScaNN`, `SingleStoreDB`, `SupabaseVectorStore`, `SurrealDBStore`, `TimescaleVector`, `Vald`, `VDMS`, `Vearch`, `VespaStore`, `Weaviate`, `Yellowbrick`, `ZepVectorStore`, `TencentVectorDB`, `OpenSearchVectorSearch`.
## Caution[​](https://python.langchain.com/docs/how_to/indexing/#caution "Direct link to Caution")
The record manager relies on a time-based mechanism to determine what content can be cleaned up (when using `full` or `incremental` or `scoped_full` cleanup modes).
If two tasks run back-to-back, and the first task finishes before the clock time changes, then the second task may not be able to clean up content.
This is unlikely to be an issue in actual settings for the following reasons:
  1. The RecordManager uses higher resolution timestamps.
  2. The data would need to change between the first and the second tasks runs, which becomes unlikely if the time interval between the tasks is small.
  3. Indexing tasks typically take more than a few ms.


## Quickstart[​](https://python.langchain.com/docs/how_to/indexing/#quickstart "Direct link to Quickstart")
```
from langchain.indexes import SQLRecordManager, indexfrom langchain_core.documents import Documentfrom langchain_elasticsearch import ElasticsearchStorefrom langchain_openai import OpenAIEmbeddings
```

**API Reference:**[SQLRecordManager](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes._sql_record_manager.SQLRecordManager.html) | [index](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.api.index.html) | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) | [ElasticsearchStore](https://python.langchain.com/api_reference/elasticsearch/vectorstores/langchain_elasticsearch.vectorstores.ElasticsearchStore.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)
Initialize a vector store and set up the embeddings:
```
collection_name ="test_index"embedding = OpenAIEmbeddings()vectorstore = ElasticsearchStore(  es_url="http://localhost:9200", index_name="test_index", embedding=embedding)
```

Initialize a record manager with an appropriate namespace.
**Suggestion:** Use a namespace that takes into account both the vector store and the collection name in the vector store; e.g., 'redis/my_docs', 'chromadb/my_docs' or 'postgres/my_docs'.
```
namespace =f"elasticsearch/{collection_name}"record_manager = SQLRecordManager(  namespace, db_url="sqlite:///record_manager_cache.sql")
```

Create a schema before using the record manager.
```
record_manager.create_schema()
```

Let's index some test documents:
```
doc1 = Document(page_content="kitty", metadata={"source":"kitty.txt"})doc2 = Document(page_content="doggy", metadata={"source":"doggy.txt"})
```

Indexing into an empty vector store:
```
def_clear():"""Hacky helper method to clear content. See the `full` mode section to to understand why it works."""  index([], record_manager, vectorstore, cleanup="full", source_id_key="source")
```

### `None` deletion mode[​](https://python.langchain.com/docs/how_to/indexing/#none-deletion-mode "Direct link to none-deletion-mode")
This mode does not do automatic clean up of old versions of content; however, it still takes care of content de-duplication.
```
_clear()
```

```
index([doc1, doc1, doc1, doc1, doc1],  record_manager,  vectorstore,  cleanup=None,  source_id_key="source",)
```

```
{'num_added': 1, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```

```
_clear()
```

```
index([doc1, doc2], record_manager, vectorstore, cleanup=None, source_id_key="source")
```

```
{'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```

Second time around all content will be skipped:
```
index([doc1, doc2], record_manager, vectorstore, cleanup=None, source_id_key="source")
```

```
{'num_added': 0, 'num_updated': 0, 'num_skipped': 2, 'num_deleted': 0}
```

### `"incremental"` deletion mode[​](https://python.langchain.com/docs/how_to/indexing/#incremental-deletion-mode "Direct link to incremental-deletion-mode")
```
_clear()
```

```
index([doc1, doc2],  record_manager,  vectorstore,  cleanup="incremental",  source_id_key="source",)
```

```
{'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```

Indexing again should result in both documents getting **skipped** -- also skipping the embedding operation!
```
index([doc1, doc2],  record_manager,  vectorstore,  cleanup="incremental",  source_id_key="source",)
```

```
{'num_added': 0, 'num_updated': 0, 'num_skipped': 2, 'num_deleted': 0}
```

If we provide no documents with incremental indexing mode, nothing will change.
```
index([], record_manager, vectorstore, cleanup="incremental", source_id_key="source")
```

```
{'num_added': 0, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```

If we mutate a document, the new version will be written and all old versions sharing the same source will be deleted.
```
changed_doc_2 = Document(page_content="puppy", metadata={"source":"doggy.txt"})
```

```
index([changed_doc_2],  record_manager,  vectorstore,  cleanup="incremental",  source_id_key="source",)
```

```
{'num_added': 1, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 1}
```

### `"full"` deletion mode[​](https://python.langchain.com/docs/how_to/indexing/#full-deletion-mode "Direct link to full-deletion-mode")
In `full` mode the user should pass the `full` universe of content that should be indexed into the indexing function.
Any documents that are not passed into the indexing function and are present in the vectorstore will be deleted!
This behavior is useful to handle deletions of source documents.
```
_clear()
```

```
all_docs =[doc1, doc2]
```

```
index(all_docs, record_manager, vectorstore, cleanup="full", source_id_key="source")
```

```
{'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```

Say someone deleted the first doc:
```
del all_docs[0]
```

```
all_docs
```

```
[Document(page_content='doggy', metadata={'source': 'doggy.txt'})]
```

Using full mode will clean up the deleted content as well.
```
index(all_docs, record_manager, vectorstore, cleanup="full", source_id_key="source")
```

```
{'num_added': 0, 'num_updated': 0, 'num_skipped': 1, 'num_deleted': 1}
```

## Source[​](https://python.langchain.com/docs/how_to/indexing/#source "Direct link to Source")
The metadata attribute contains a field called `source`. This source should be pointing at the _ultimate_ provenance associated with the given document.
For example, if these documents are representing chunks of some parent document, the `source` for both documents should be the same and reference the parent document.
In general, `source` should always be specified. Only use a `None`, if you **never** intend to use `incremental` mode, and for some reason can't specify the `source` field correctly.
```
from langchain_text_splitters import CharacterTextSplitter
```

**API Reference:**[CharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.CharacterTextSplitter.html)
```
doc1 = Document(  page_content="kitty kitty kitty kitty kitty", metadata={"source":"kitty.txt"})doc2 = Document(page_content="doggy doggy the doggy", metadata={"source":"doggy.txt"})
```

```
new_docs = CharacterTextSplitter(  separator="t", keep_separator=True, chunk_size=12, chunk_overlap=2).split_documents([doc1, doc2])new_docs
```

```
[Document(page_content='kitty kit', metadata={'source': 'kitty.txt'}), Document(page_content='tty kitty ki', metadata={'source': 'kitty.txt'}), Document(page_content='tty kitty', metadata={'source': 'kitty.txt'}), Document(page_content='doggy doggy', metadata={'source': 'doggy.txt'}), Document(page_content='the doggy', metadata={'source': 'doggy.txt'})]
```

```
_clear()
```

```
index(  new_docs,  record_manager,  vectorstore,  cleanup="incremental",  source_id_key="source",)
```

```
{'num_added': 5, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```

```
changed_doggy_docs =[  Document(page_content="woof woof", metadata={"source":"doggy.txt"}),  Document(page_content="woof woof woof", metadata={"source":"doggy.txt"}),]
```

This should delete the old versions of documents associated with `doggy.txt` source and replace them with the new versions.
```
index(  changed_doggy_docs,  record_manager,  vectorstore,  cleanup="incremental",  source_id_key="source",)
```

```
{'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 2}
```

```
vectorstore.similarity_search("dog", k=30)
```

```
[Document(page_content='woof woof', metadata={'source': 'doggy.txt'}), Document(page_content='woof woof woof', metadata={'source': 'doggy.txt'}), Document(page_content='tty kitty', metadata={'source': 'kitty.txt'}), Document(page_content='tty kitty ki', metadata={'source': 'kitty.txt'}), Document(page_content='kitty kit', metadata={'source': 'kitty.txt'})]
```

## Using with loaders[​](https://python.langchain.com/docs/how_to/indexing/#using-with-loaders "Direct link to Using with loaders")
Indexing can accept either an iterable of documents or else any loader.
**Attention:** The loader **must** set source keys correctly.
```
from langchain_core.document_loaders import BaseLoaderclassMyCustomLoader(BaseLoader):deflazy_load(self):    text_splitter = CharacterTextSplitter(      separator="t", keep_separator=True, chunk_size=12, chunk_overlap=2)    docs =[      Document(page_content="woof woof", metadata={"source":"doggy.txt"}),      Document(page_content="woof woof woof", metadata={"source":"doggy.txt"}),]yieldfrom text_splitter.split_documents(docs)defload(self):returnlist(self.lazy_load())
```

**API Reference:**[BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html)
```
_clear()
```

```
loader = MyCustomLoader()
```

```
loader.load()
```

```
[Document(page_content='woof woof', metadata={'source': 'doggy.txt'}), Document(page_content='woof woof woof', metadata={'source': 'doggy.txt'})]
```

```
index(loader, record_manager, vectorstore, cleanup="full", source_id_key="source")
```

```
{'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```

```
vectorstore.similarity_search("dog", k=30)
```

```
[Document(page_content='woof woof', metadata={'source': 'doggy.txt'}), Document(page_content='woof woof woof', metadata={'source': 'doggy.txt'})]
```

[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/how_to/indexing.ipynb)
#### Was this page helpful?
  * [How it works](https://python.langchain.com/docs/how_to/indexing/#how-it-works)
  * [Deletion modes](https://python.langchain.com/docs/how_to/indexing/#deletion-modes)
  * [Requirements](https://python.langchain.com/docs/how_to/indexing/#requirements)
  * [Caution](https://python.langchain.com/docs/how_to/indexing/#caution)
  * [Quickstart](https://python.langchain.com/docs/how_to/indexing/#quickstart)
    * [`None` deletion mode](https://python.langchain.com/docs/how_to/indexing/#none-deletion-mode)
    * [`"incremental"` deletion mode](https://python.langchain.com/docs/how_to/indexing/#incremental-deletion-mode)
    * [`"full"` deletion mode](https://python.langchain.com/docs/how_to/indexing/#full-deletion-mode)
  * [Source](https://python.langchain.com/docs/how_to/indexing/#source)
  * [Using with loaders](https://python.langchain.com/docs/how_to/indexing/#using-with-loaders)


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

