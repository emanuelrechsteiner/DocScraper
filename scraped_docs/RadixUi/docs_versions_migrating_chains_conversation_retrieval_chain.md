---
url: https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/
scraped_at: 2025-05-25T18:04:27.275785
title: Migrating from ConversationalRetrievalChain | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/)
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
    * [v0.2](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/)
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
  * Versions
  * [Migrating from v0.0 chains](https://python.langchain.com/docs/versions/migrating_chains/)
  * Migrating from ConversationalRetrievalChain


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/versions/migrating_chains/conversation_retrieval_chain.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/versions/migrating_chains/conversation_retrieval_chain.ipynb)
# Migrating from ConversationalRetrievalChain
The [`ConversationalRetrievalChain`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.ConversationalRetrievalChain.html) was an all-in one way that combined retrieval-augmented generation with chat history, allowing you to "chat with" your documents.
Advantages of switching to the LCEL implementation are similar to the [`RetrievalQA` migration guide](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/):
  * Clearer internals. The `ConversationalRetrievalChain` chain hides an entire question rephrasing step which dereferences the initial query against the chat history. 
    * This means the class contains two sets of configurable prompts, LLMs, etc.
  * More easily return source documents.
  * Support for runnable methods like streaming and async operations.


Here are equivalent implementations with custom prompts. We'll use the following ingestion code to load a [blog post by Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent/) on autonomous agents into a local vector store:
## Shared setup[​](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#shared-setup "Direct link to Shared setup")
For both versions, we'll need to load the data with the `WebBaseLoader` document loader, split it with `RecursiveCharacterTextSplitter`, and add it to an in-memory `FAISS` vector store.
We will also instantiate a chat model to use.
```
%pip install --upgrade --quiet langchain-community langchain langchain-openai faiss-cpu beautifulsoup4
```

```
import osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

```
# Load docsfrom langchain_community.document_loaders import WebBaseLoaderfrom langchain_community.vectorstores import FAISSfrom langchain_openai.chat_models import ChatOpenAIfrom langchain_openai.embeddings import OpenAIEmbeddingsfrom langchain_text_splitters import RecursiveCharacterTextSplitterloader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")data = loader.load()# Splittext_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)all_splits = text_splitter.split_documents(data)# Store splitsvectorstore = FAISS.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())# LLMllm = ChatOpenAI()
```

**API Reference:**[WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [FAISS](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.faiss.FAISS.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html) | [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html)
## Legacy[​](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#legacy "Direct link to Legacy")
Details
```
from langchain.chains import ConversationalRetrievalChainfrom langchain_core.prompts import ChatPromptTemplatecondense_question_template ="""Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.Chat History:{chat_history}Follow Up Input: {question}Standalone question:"""condense_question_prompt = ChatPromptTemplate.from_template(condense_question_template)qa_template ="""You are an assistant for question-answering tasks.Use the following pieces of retrieved context to answerthe question. If you don't know the answer, say that youdon't know. Use three sentences maximum and keep theanswer concise.Chat History:{chat_history}Other context:{context}Question: {question}"""qa_prompt = ChatPromptTemplate.from_template(qa_template)convo_qa_chain = ConversationalRetrievalChain.from_llm(  llm,  vectorstore.as_retriever(),  condense_question_prompt=condense_question_prompt,  combine_docs_chain_kwargs={"prompt": qa_prompt,},)convo_qa_chain({"question":"What are autonomous agents?","chat_history":"",})
```

**API Reference:**[ConversationalRetrievalChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.ConversationalRetrievalChain.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)
```
{'question': 'What are autonomous agents?', 'chat_history': '', 'answer': 'Autonomous agents are entities empowered with capabilities like planning, task decomposition, and memory to perform complex tasks independently. These agents can leverage tools like browsing the internet, reading documentation, executing code, and calling APIs to achieve their objectives. They are designed to handle tasks like scientific discovery and experimentation autonomously.'}
```

## LCEL[​](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#lcel "Direct link to LCEL")
Details
```
from langchain.chains import create_history_aware_retriever, create_retrieval_chainfrom langchain.chains.combine_documents import create_stuff_documents_chaincondense_question_system_template =("Given a chat history and the latest user question ""which might reference context in the chat history, ""formulate a standalone question which can be understood ""without the chat history. Do NOT answer the question, ""just reformulate it if needed and otherwise return it as is.")condense_question_prompt = ChatPromptTemplate.from_messages([("system", condense_question_system_template),("placeholder","{chat_history}"),("human","{input}"),])history_aware_retriever = create_history_aware_retriever(  llm, vectorstore.as_retriever(), condense_question_prompt)system_prompt =("You are an assistant for question-answering tasks. ""Use the following pieces of retrieved context to answer ""the question. If you don't know the answer, say that you ""don't know. Use three sentences maximum and keep the ""answer concise.""\n\n""{context}")qa_prompt = ChatPromptTemplate.from_messages([("system", system_prompt),("placeholder","{chat_history}"),("human","{input}"),])qa_chain = create_stuff_documents_chain(llm, qa_prompt)convo_qa_chain = create_retrieval_chain(history_aware_retriever, qa_chain)convo_qa_chain.invoke({"input":"What are autonomous agents?","chat_history":[],})
```

**API Reference:**[create_history_aware_retriever](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.history_aware_retriever.create_history_aware_retriever.html) | [create_retrieval_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval.create_retrieval_chain.html) | [create_stuff_documents_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.stuff.create_stuff_documents_chain.html)
```
{'input': 'What are autonomous agents?', 'chat_history': [], 'context': [Document(metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'title': "LLM Powered Autonomous Agents | Lil'Log", 'description': 'Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.\nAgent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:', 'language': 'en'}, page_content='Boiko et al. (2023) also looked into LLM-empowered agents for scientific discovery, to handle autonomous design, planning, and performance of complex scientific experiments. This agent can use tools to browse the Internet, read documentation, execute code, call robotics experimentation APIs and leverage other LLMs.\nFor example, when requested to "develop a novel anticancer drug", the model came up with the following reasoning steps:'), Document(metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'title': "LLM Powered Autonomous Agents | Lil'Log", 'description': 'Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.\nAgent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:', 'language': 'en'}, page_content='Weng, Lilian. (Jun 2023). “LLM-powered Autonomous Agents”. Lil’Log. https://lilianweng.github.io/posts/2023-06-23-agent/.'), Document(metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'title': "LLM Powered Autonomous Agents | Lil'Log", 'description': 'Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.\nAgent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:', 'language': 'en'}, page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#'), Document(metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'title': "LLM Powered Autonomous Agents | Lil'Log", 'description': 'Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.\nAgent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:', 'language': 'en'}, page_content="LLM Powered Autonomous Agents | Lil'Log\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLil'Log\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPosts\n\n\n\n\nArchive\n\n\n\n\nSearch\n\n\n\n\nTags\n\n\n\n\nFAQ\n\n\n\n\nemojisearch.app\n\n\n\n\n\n\n\n\n\n   LLM Powered Autonomous Agents\n  \nDate: June 23, 2023 | Estimated Reading Time: 31 min | Author: Lilian Weng\n\n\n \n\n\nTable of Contents\n\n\n\nAgent System Overview\n\nComponent One: Planning\n\nTask Decomposition\n\nSelf-Reflection\n\n\nComponent Two: Memory\n\nTypes of Memory\n\nMaximum Inner Product Search (MIPS)")], 'answer': 'Autonomous agents are entities that can act independently to achieve specific goals or tasks without direct human intervention. These agents have the ability to perceive their environment, make decisions, and take actions based on their programming or learning. They can perform tasks such as planning, execution, and problem-solving autonomously.'}
```

## Next steps[​](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#next-steps "Direct link to Next steps")
You've now seen how to migrate existing usage of some legacy chains to LCEL.
Next, check out the [LCEL conceptual docs](https://python.langchain.com/docs/concepts/lcel/) for more background information.
[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/versions/migrating_chains/conversation_retrieval_chain.ipynb)
#### Was this page helpful?
[PreviousMigrating from ConversationalChain](https://python.langchain.com/docs/versions/migrating_chains/conversation_chain/)[NextMigrating from LLMChain](https://python.langchain.com/docs/versions/migrating_chains/llm_chain/)
  * [Shared setup](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#shared-setup)
  * [Legacy](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#legacy)
  * [LCEL](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#lcel)
  * [Next steps](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/#next-steps)


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

