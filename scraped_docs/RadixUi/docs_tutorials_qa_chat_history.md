---
url: https://python.langchain.com/docs/tutorials/qa_chat_history/
scraped_at: 2025-05-25T18:03:19.314031
title: Build a Retrieval Augmented Generation (RAG) App: Part 2 | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/tutorials/qa_chat_history/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/tutorials/qa_chat_history/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/tutorials/qa_chat_history/)
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
    * [v0.2](https://python.langchain.com/docs/tutorials/qa_chat_history/)
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
  * [Tutorials](https://python.langchain.com/docs/tutorials/)
  * Build a Retrieval Augmented Generation (RAG) App: Part 2


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/tutorials/qa_chat_history.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/tutorials/qa_chat_history.ipynb)
# Build a Retrieval Augmented Generation (RAG) App: Part 2
In many Q&A applications we want to allow the user to have a back-and-forth conversation, meaning the application needs some sort of "memory" of past questions and answers, and some logic for incorporating those into its current thinking.
This is the second part of a multi-part tutorial:
  * [Part 1](https://python.langchain.com/docs/tutorials/rag/) introduces RAG and walks through a minimal implementation.
  * [Part 2](https://python.langchain.com/docs/tutorials/qa_chat_history/) (this guide) extends the implementation to accommodate conversation-style interactions and multi-step retrieval processes.


Here we focus on **adding logic for incorporating historical messages.** This involves the management of a [chat history](https://python.langchain.com/docs/concepts/chat_history/).
We will cover two approaches:
  1. [Chains](https://python.langchain.com/docs/tutorials/qa_chat_history/#chains), in which we execute at most one retrieval step;
  2. [Agents](https://python.langchain.com/docs/tutorials/qa_chat_history/#agents), in which we give an LLM discretion to execute multiple retrieval steps.


note
The methods presented here leverage [tool-calling](https://python.langchain.com/docs/concepts/tool_calling/) capabilities in modern [chat models](https://python.langchain.com/docs/concepts/chat_models/). See [this page](https://python.langchain.com/docs/integrations/chat/) for a table of models supporting tool calling features.
For the external knowledge source, we will use the same [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) blog post by Lilian Weng from the [Part 1](https://python.langchain.com/docs/tutorials/rag/) of the RAG tutorial.
## Setup[​](https://python.langchain.com/docs/tutorials/qa_chat_history/#setup "Direct link to Setup")
### Components[​](https://python.langchain.com/docs/tutorials/qa_chat_history/#components "Direct link to Components")
We will need to select three components from LangChain's suite of integrations.
Select [chat model](https://python.langchain.com/docs/integrations/chat/):
OpenAI▾
* [OpenAI](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Anthropic](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Azure](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Google Gemini](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Google Vertex](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [AWS](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Groq](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Cohere](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [NVIDIA](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Fireworks AI](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Mistral AI](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Together AI](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [IBM watsonx](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Databricks](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [xAI](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Perplexity](https://python.langchain.com/docs/tutorials/qa_chat_history/)
```
pip install -qU "langchain[openai]"
```

```
import getpassimport osifnot os.environ.get("OPENAI_API_KEY"): os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter API key for OpenAI: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("gpt-4o-mini", model_provider="openai")
```

Select [embeddings model](https://python.langchain.com/docs/integrations/text_embedding/):
OpenAI▾
* [OpenAI](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Azure](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Google Gemini](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Google Vertex](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [AWS](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [HuggingFace](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Ollama](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Cohere](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [MistralAI](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Nomic](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [NVIDIA](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Voyage AI](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [IBM watsonx](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Fake](https://python.langchain.com/docs/tutorials/qa_chat_history/)
```
pip install -qU langchain-openai
```

```
import getpassimport osifnot os.environ.get("OPENAI_API_KEY"): os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter API key for OpenAI: ")from langchain_openai import OpenAIEmbeddingsembeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

Select [vector store](https://python.langchain.com/docs/integrations/vectorstores/):
In-memory▾
* [In-memory](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [AstraDB](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Chroma](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [FAISS](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Milvus](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [MongoDB](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [PGVector](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Pinecone](https://python.langchain.com/docs/tutorials/qa_chat_history/)
* [Qdrant](https://python.langchain.com/docs/tutorials/qa_chat_history/)
```
pip install -qU langchain-core
```

```
from langchain_core.vectorstores import InMemoryVectorStorevector_store = InMemoryVectorStore(embeddings)
```

### Dependencies[​](https://python.langchain.com/docs/tutorials/qa_chat_history/#dependencies "Direct link to Dependencies")
In addition, we'll use the following packages:
```
%%capture --no-stderr%pip install --upgrade --quiet langgraph langchain-community beautifulsoup4
```

### LangSmith[​](https://python.langchain.com/docs/tutorials/qa_chat_history/#langsmith "Direct link to LangSmith")
Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with [LangSmith](https://smith.langchain.com).
Note that LangSmith is not needed, but it is helpful. If you do want to use LangSmith, after you sign up at the link above, make sure to set your environment variables to start logging traces:
```
os.environ["LANGSMITH_TRACING"]="true"ifnot os.environ.get("LANGSMITH_API_KEY"):  os.environ["LANGSMITH_API_KEY"]= getpass.getpass()
```

## Chains[​](https://python.langchain.com/docs/tutorials/qa_chat_history/#chains "Direct link to Chains")
Let's first revisit the vector store we built in [Part 1](https://python.langchain.com/docs/tutorials/rag/), which indexes an [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) blog post by Lilian Weng.
```
import bs4from langchain import hubfrom langchain_community.document_loaders import WebBaseLoaderfrom langchain_core.documents import Documentfrom langchain_text_splitters import RecursiveCharacterTextSplitterfrom typing_extensions import List, TypedDict# Load and chunk contents of the blogloader = WebBaseLoader(  web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),  bs_kwargs=dict(    parse_only=bs4.SoupStrainer(      class_=("post-content","post-title","post-header"))),)docs = loader.load()text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)all_splits = text_splitter.split_documents(docs)
```

**API Reference:**[hub](https://python.langchain.com/api_reference/langchain/hub/langchain.hub.hub.html) | [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) | [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html)
```
# Index chunks_ = vector_store.add_documents(documents=all_splits)
```

In the [Part 1](https://python.langchain.com/docs/tutorials/rag/) of the RAG tutorial, we represented the user input, retrieved context, and generated answer as separate keys in the state. Conversational experiences can be naturally represented using a sequence of [messages](https://python.langchain.com/docs/concepts/messages/). In addition to messages from the user and assistant, retrieved documents and other artifacts can be incorporated into a message sequence via [tool messages](https://python.langchain.com/docs/concepts/messages/#toolmessage). This motivates us to represent the state of our RAG application using a sequence of messages. Specifically, we will have
  1. User input as a `HumanMessage`;
  2. Vector store query as an `AIMessage` with tool calls;
  3. Retrieved documents as a `ToolMessage`;
  4. Final response as a `AIMessage`.


This model for state is so versatile that LangGraph offers a built-in version for convenience:
```
from langgraph.graph import MessagesState, StateGraphgraph_builder = StateGraph(MessagesState)
```

**API Reference:**[StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)
Leveraging [tool-calling](https://python.langchain.com/docs/concepts/tool_calling/) to interact with a retrieval step has another benefit, which is that the query for the retrieval is generated by our model. This is especially important in a conversational setting, where user queries may require contextualization based on the chat history. For instance, consider the following exchange:
> Human: "What is Task Decomposition?"
> AI: "Task decomposition involves breaking down complex tasks into smaller and simpler steps to make them more manageable for an agent or model."
> Human: "What are common ways of doing it?"
In this scenario, a model could generate a query such as `"common approaches to task decomposition"`. Tool-calling facilitates this naturally. As in the [query analysis](https://python.langchain.com/docs/tutorials/rag/#query-analysis) section of the RAG tutorial, this allows a model to rewrite user queries into more effective search queries. It also provides support for direct responses that do not involve a retrieval step (e.g., in response to a generic greeting from the user).
Let's turn our retrieval step into a [tool](https://python.langchain.com/docs/concepts/tools/):
```
from langchain_core.tools import tool@tool(response_format="content_and_artifact")defretrieve(query:str):"""Retrieve information related to a query."""  retrieved_docs = vector_store.similarity_search(query, k=2)  serialized ="\n\n".join((f"Source: {doc.metadata}\n"f"Content: {doc.page_content}")for doc in retrieved_docs)return serialized, retrieved_docs
```

**API Reference:**[tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)
See [this guide](https://python.langchain.com/docs/how_to/custom_tools/) for more detail on creating tools.
Our graph will consist of three nodes:
  1. A node that fields the user input, either generating a query for the retriever or responding directly;
  2. A node for the retriever tool that executes the retrieval step;
  3. A node that generates the final response using the retrieved context.


We build them below. Note that we leverage another pre-built LangGraph component, [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode), that executes the tool and adds the result as a `ToolMessage` to the state.
```
from langchain_core.messages import SystemMessagefrom langgraph.prebuilt import ToolNode# Step 1: Generate an AIMessage that may include a tool-call to be sent.defquery_or_respond(state: MessagesState):"""Generate tool call for retrieval or respond."""  llm_with_tools = llm.bind_tools([retrieve])  response = llm_with_tools.invoke(state["messages"])# MessagesState appends messages to state instead of overwritingreturn{"messages":[response]}# Step 2: Execute the retrieval.tools = ToolNode([retrieve])# Step 3: Generate a response using the retrieved content.defgenerate(state: MessagesState):"""Generate answer."""# Get generated ToolMessages  recent_tool_messages =[]for message inreversed(state["messages"]):if message.type=="tool":      recent_tool_messages.append(message)else:break  tool_messages = recent_tool_messages[::-1]# Format into prompt  docs_content ="\n\n".join(doc.content for doc in tool_messages)  system_message_content =("You are an assistant for question-answering tasks. ""Use the following pieces of retrieved context to answer ""the question. If you don't know the answer, say that you ""don't know. Use three sentences maximum and keep the ""answer concise.""\n\n"f"{docs_content}")  conversation_messages =[    messagefor message in state["messages"]if message.typein("human","system")or(message.type=="ai"andnot message.tool_calls)]  prompt =[SystemMessage(system_message_content)]+ conversation_messages# Run  response = llm.invoke(prompt)return{"messages":[response]}
```

**API Reference:**[SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)
Finally, we compile our application into a single `graph` object. In this case, we are just connecting the steps into a sequence. We also allow the first `query_or_respond` step to "short-circuit" and respond directly to the user if it does not generate a tool call. This allows our application to support conversational experiences-- e.g., responding to generic greetings that may not require a retrieval step
```
from langgraph.graph import ENDfrom langgraph.prebuilt import ToolNode, tools_conditiongraph_builder.add_node(query_or_respond)graph_builder.add_node(tools)graph_builder.add_node(generate)graph_builder.set_entry_point("query_or_respond")graph_builder.add_conditional_edges("query_or_respond",  tools_condition,{END: END,"tools":"tools"},)graph_builder.add_edge("tools","generate")graph_builder.add_edge("generate", END)graph = graph_builder.compile()
```

**API Reference:**[ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) | [tools_condition](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.tools_condition)
```
from IPython.display import Image, displaydisplay(Image(graph.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/tutorials/qa_chat_history/)
Let's test our application.
Note that it responds appropriately to messages that do not require an additional retrieval step:
```
input_message ="Hello"for step in graph.stream({"messages":[{"role":"user","content": input_message}]},  stream_mode="values",):  step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================Hello==================================[1m Ai Message [0m==================================Hello! How can I assist you today?
```

And when executing a search, we can stream the steps to observe the query generation, retrieval, and answer generation:
```
input_message ="What is Task Decomposition?"for step in graph.stream({"messages":[{"role":"user","content": input_message}]},  stream_mode="values",):  step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================What is Task Decomposition?==================================[1m Ai Message [0m==================================Tool Calls: retrieve (call_dLjB3rkMoxZZxwUGXi33UBeh) Call ID: call_dLjB3rkMoxZZxwUGXi33UBeh Args:  query: Task Decomposition=================================[1m Tool Message [0m=================================Name: retrieveSource: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Fig. 1. Overview of a LLM-powered autonomous agent system.Component One: Planning#A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.Task Decomposition#Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.==================================[1m Ai Message [0m==================================Task Decomposition is the process of breaking down a complicated task into smaller, manageable steps. It often involves techniques like Chain of Thought (CoT), which encourages models to think step by step, enhancing performance on complex tasks. This approach allows for a clearer understanding of the task and aids in structuring the problem-solving process.
```

Check out the LangSmith trace [here](https://smith.langchain.com/public/70110399-01d3-4b4b-9139-cbcd4edf9d6d/r).
### Stateful management of chat history[​](https://python.langchain.com/docs/tutorials/qa_chat_history/#stateful-management-of-chat-history "Direct link to Stateful management of chat history")
note
This section of the tutorial previously used the [RunnableWithMessageHistory](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html) abstraction. You can access that version of the documentation in the [v0.2 docs](https://python.langchain.com/v0.2/docs/tutorials/chatbot/).
As of the v0.3 release of LangChain, we recommend that LangChain users take advantage of [LangGraph persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) to incorporate `memory` into new LangChain applications.
If your code is already relying on `RunnableWithMessageHistory` or `BaseChatMessageHistory`, you do **not** need to make any changes. We do not plan on deprecating this functionality in the near future as it works for simple chat applications and any code that uses `RunnableWithMessageHistory` will continue to work as expected.
Please see [How to migrate to LangGraph Memory](https://python.langchain.com/docs/versions/migrating_memory/) for more details.
In production, the Q&A application will usually persist the chat history into a database, and be able to read and update it appropriately.
[LangGraph](https://langchain-ai.github.io/langgraph/) implements a built-in [persistence layer](https://langchain-ai.github.io/langgraph/concepts/persistence/), making it ideal for chat applications that support multiple conversational turns.
To manage multiple conversational turns and threads, all we have to do is specify a [checkpointer](https://langchain-ai.github.io/langgraph/concepts/persistence/) when compiling our application. Because the nodes in our graph are appending messages to the state, we will retain a consistent chat history across invocations.
LangGraph comes with a simple in-memory checkpointer, which we use below. See its [documentation](https://langchain-ai.github.io/langgraph/concepts/persistence/) for more detail, including how to use different persistence backends (e.g., SQLite or Postgres).
For a detailed walkthrough of how to manage message history, head to the [How to add message history (memory)](https://python.langchain.com/docs/how_to/message_history/) guide.
```
from langgraph.checkpoint.memory import MemorySavermemory = MemorySaver()graph = graph_builder.compile(checkpointer=memory)# Specify an ID for the threadconfig ={"configurable":{"thread_id":"abc123"}}
```

**API Reference:**[MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)
We can now invoke similar to before:
```
input_message ="What is Task Decomposition?"for step in graph.stream({"messages":[{"role":"user","content": input_message}]},  stream_mode="values",  config=config,):  step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================What is Task Decomposition?==================================[1m Ai Message [0m==================================Tool Calls: retrieve (call_JZb6GLD812bW2mQsJ5EJQDnN) Call ID: call_JZb6GLD812bW2mQsJ5EJQDnN Args:  query: Task Decomposition=================================[1m Tool Message [0m=================================Name: retrieveSource: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Fig. 1. Overview of a LLM-powered autonomous agent system.Component One: Planning#A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.Task Decomposition#Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.==================================[1m Ai Message [0m==================================Task Decomposition is a technique used to break down complicated tasks into smaller, manageable steps. It involves using methods like Chain of Thought (CoT) prompting, which encourages the model to think step by step, enhancing performance on complex tasks. This process helps to clarify the model's reasoning and makes it easier to tackle difficult problems.
```

```
input_message ="Can you look up some common ways of doing it?"for step in graph.stream({"messages":[{"role":"user","content": input_message}]},  stream_mode="values",  config=config,):  step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================Can you look up some common ways of doing it?==================================[1m Ai Message [0m==================================Tool Calls: retrieve (call_kjRI4Y5cJOiB73yvd7dmb6ux) Call ID: call_kjRI4Y5cJOiB73yvd7dmb6ux Args:  query: common methods of task decomposition=================================[1m Tool Message [0m=================================Name: retrieveSource: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Fig. 1. Overview of a LLM-powered autonomous agent system.Component One: Planning#A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.Task Decomposition#Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.==================================[1m Ai Message [0m==================================Common ways of performing Task Decomposition include: (1) using Large Language Models (LLMs) with simple prompts like "Steps for XYZ" or "What are the subgoals for achieving XYZ?", (2) employing task-specific instructions such as "Write a story outline" for specific tasks, and (3) incorporating human inputs to guide the decomposition process.
```

Note that the query generated by the model in the second question incorporates the conversational context.
The [LangSmith](https://smith.langchain.com/public/28e6179f-fc56-45e1-9028-447d76352c14/r) trace is particularly informative here, as we can see exactly what messages are visible to our chat model at each step.
## Agents[​](https://python.langchain.com/docs/tutorials/qa_chat_history/#agents "Direct link to Agents")
[Agents](https://python.langchain.com/docs/concepts/agents/) leverage the reasoning capabilities of LLMs to make decisions during execution. Using agents allows you to offload additional discretion over the retrieval process. Although their behavior is less predictable than the above "chain", they are able to execute multiple retrieval steps in service of a query, or iterate on a single search.
Below we assemble a minimal RAG agent. Using LangGraph's [pre-built ReAct agent constructor](https://langchain-ai.github.io/langgraph/how-tos/#langgraph.prebuilt.chat_agent_executor.create_react_agent), we can do this in one line.
tip
Check out LangGraph's [Agentic RAG](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) tutorial for more advanced formulations.
```
from langgraph.prebuilt import create_react_agentagent_executor = create_react_agent(llm,[retrieve], checkpointer=memory)
```

**API Reference:**[create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)
Let's inspect the graph:
```
display(Image(agent_executor.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/tutorials/qa_chat_history/)
The key difference from our earlier implementation is that instead of a final generation step that ends the run, here the tool invocation loops back to the original LLM call. The model can then either answer the question using the retrieved context, or generate another tool call to obtain more information.
Let's test this out. We construct a question that would typically require an iterative sequence of retrieval steps to answer:
```
config ={"configurable":{"thread_id":"def234"}}input_message =("What is the standard method for Task Decomposition?\n\n""Once you get the answer, look up common extensions of that method.")for event in agent_executor.stream({"messages":[{"role":"user","content": input_message}]},  stream_mode="values",  config=config,):  event["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================What is the standard method for Task Decomposition?Once you get the answer, look up common extensions of that method.==================================[1m Ai Message [0m==================================Tool Calls: retrieve (call_Y3YaIzL71B83Cjqa8d2G0O8N) Call ID: call_Y3YaIzL71B83Cjqa8d2G0O8N Args:  query: standard method for Task Decomposition=================================[1m Tool Message [0m=================================Name: retrieveSource: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Fig. 1. Overview of a LLM-powered autonomous agent system.Component One: Planning#A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.Task Decomposition#Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.==================================[1m Ai Message [0m==================================Tool Calls: retrieve (call_2JntP1x4XQMWwgVpYurE12ff) Call ID: call_2JntP1x4XQMWwgVpYurE12ff Args:  query: common extensions of Task Decomposition methods=================================[1m Tool Message [0m=================================Name: retrieveSource: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Fig. 1. Overview of a LLM-powered autonomous agent system.Component One: Planning#A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.Task Decomposition#Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.==================================[1m Ai Message [0m==================================The standard method for task decomposition involves using techniques such as Chain of Thought (CoT), where a model is instructed to "think step by step" to break down complex tasks into smaller, more manageable components. This approach enhances model performance by allowing for more thorough reasoning and planning. Task decomposition can be accomplished through various means, including:1. Simple prompting (e.g., asking for steps to achieve a goal).2. Task-specific instructions (e.g., asking for a story outline).3. Human inputs to guide the decomposition process.### Common Extensions of Task Decomposition Methods:1. **Tree of Thoughts**: This extension builds on CoT by not only decomposing the problem into thought steps but also generating multiple thoughts at each step, creating a tree structure. The search process can employ breadth-first search (BFS) or depth-first search (DFS), with each state evaluated by a classifier or through majority voting.These extensions aim to enhance reasoning capabilities and improve the effectiveness of task decomposition in various contexts.
```

Note that the agent:
  1. Generates a query to search for a standard method for task decomposition;
  2. Receiving the answer, generates a second query to search for common extensions of it;
  3. Having received all necessary context, answers the question.


We can see the full sequence of steps, along with latency and other metadata, in the [LangSmith trace](https://smith.langchain.com/public/48cbd35e-9ac1-49ab-8c09-500d54c06b81/r).
## Next steps[​](https://python.langchain.com/docs/tutorials/qa_chat_history/#next-steps "Direct link to Next steps")
We've covered the steps to build a basic conversational Q&A application:
  * We used chains to build a predictable application that generates at most one query per user input;
  * We used agents to build an application that can iterate on a sequence of queries.


To explore different types of retrievers and retrieval strategies, visit the [retrievers](https://python.langchain.com/docs/how_to/#retrievers) section of the how-to guides.
For a detailed walkthrough of LangChain's conversation memory abstractions, visit the [How to add message history (memory)](https://python.langchain.com/docs/how_to/message_history/) guide.
To learn more about agents, check out the [conceptual guide](https://python.langchain.com/docs/concepts/agents/) and LangGraph [agent architectures](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/) page.
[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/tutorials/qa_chat_history.ipynb)
#### Was this page helpful?
  * [Setup](https://python.langchain.com/docs/tutorials/qa_chat_history/#setup)
    * [Components](https://python.langchain.com/docs/tutorials/qa_chat_history/#components)
    * [Dependencies](https://python.langchain.com/docs/tutorials/qa_chat_history/#dependencies)
    * [LangSmith](https://python.langchain.com/docs/tutorials/qa_chat_history/#langsmith)
  * [Chains](https://python.langchain.com/docs/tutorials/qa_chat_history/#chains)
    * [Stateful management of chat history](https://python.langchain.com/docs/tutorials/qa_chat_history/#stateful-management-of-chat-history)
  * [Agents](https://python.langchain.com/docs/tutorials/qa_chat_history/#agents)
  * [Next steps](https://python.langchain.com/docs/tutorials/qa_chat_history/#next-steps)


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

