---
url: https://python.langchain.com/docs/how_to/qa_sources/
scraped_at: 2025-05-25T17:53:57.747642
title: How to get your RAG application to return sources | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/how_to/qa_sources/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/how_to/qa_sources/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/how_to/qa_sources/)
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
    * [v0.2](https://python.langchain.com/docs/how_to/qa_sources/)
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
  * How to get your RAG application to return sources


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/how_to/qa_sources.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/qa_sources.ipynb)
# How to get your RAG application to return sources
Often in [Q&A](https://python.langchain.com/docs/concepts/rag/) applications it's important to show users the sources that were used to generate the answer. The simplest way to do this is for the chain to return the Documents that were retrieved in each generation.
We'll work off of the Q&A app we built over the [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) blog post by Lilian Weng in the [RAG tutorial](https://python.langchain.com/docs/tutorials/rag/).
We will cover two approaches:
  1. Using the basic RAG chain covered in [Part 1](https://python.langchain.com/docs/tutorials/rag/) of the RAG tutorial;
  2. Using a conversational RAG chain as convered in [Part 2](https://python.langchain.com/docs/tutorials/qa_chat_history/) of the tutorial.


We will also show how to structure sources into the model response, such that a model can report what specific sources it used in generating its answer.
## Setup[​](https://python.langchain.com/docs/how_to/qa_sources/#setup "Direct link to Setup")
### Dependencies[​](https://python.langchain.com/docs/how_to/qa_sources/#dependencies "Direct link to Dependencies")
We'll use the following packages:
```
%pip install --upgrade --quiet langchain langchain-community langchainhub beautifulsoup4
```

### LangSmith[​](https://python.langchain.com/docs/how_to/qa_sources/#langsmith "Direct link to LangSmith")
Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with [LangSmith](https://smith.langchain.com).
Note that LangSmith is not needed, but it is helpful. If you do want to use LangSmith, after you sign up at the link above, make sure to set your environment variables to start logging traces:
```
os.environ["LANGSMITH_TRACING"]="true"os.environ["LANGSMITH_API_KEY"]= getpass.getpass()
```

### Components[​](https://python.langchain.com/docs/how_to/qa_sources/#components "Direct link to Components")
We will need to select three components from LangChain's suite of integrations.
A [chat model](https://python.langchain.com/docs/integrations/chat/):
Select [chat model](https://python.langchain.com/docs/integrations/chat/):
OpenAI▾
* [OpenAI](https://python.langchain.com/docs/how_to/qa_sources/)
* [Anthropic](https://python.langchain.com/docs/how_to/qa_sources/)
* [Azure](https://python.langchain.com/docs/how_to/qa_sources/)
* [Google Gemini](https://python.langchain.com/docs/how_to/qa_sources/)
* [Google Vertex](https://python.langchain.com/docs/how_to/qa_sources/)
* [AWS](https://python.langchain.com/docs/how_to/qa_sources/)
* [Groq](https://python.langchain.com/docs/how_to/qa_sources/)
* [Cohere](https://python.langchain.com/docs/how_to/qa_sources/)
* [NVIDIA](https://python.langchain.com/docs/how_to/qa_sources/)
* [Fireworks AI](https://python.langchain.com/docs/how_to/qa_sources/)
* [Mistral AI](https://python.langchain.com/docs/how_to/qa_sources/)
* [Together AI](https://python.langchain.com/docs/how_to/qa_sources/)
* [IBM watsonx](https://python.langchain.com/docs/how_to/qa_sources/)
* [Databricks](https://python.langchain.com/docs/how_to/qa_sources/)
* [xAI](https://python.langchain.com/docs/how_to/qa_sources/)
* [Perplexity](https://python.langchain.com/docs/how_to/qa_sources/)
```
pip install -qU "langchain[openai]"
```

```
import getpassimport osifnot os.environ.get("OPENAI_API_KEY"): os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter API key for OpenAI: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("gpt-4o-mini", model_provider="openai")
```

An [embedding model](https://python.langchain.com/docs/integrations/text_embedding/):
Select [embeddings model](https://python.langchain.com/docs/integrations/text_embedding/):
OpenAI▾
* [OpenAI](https://python.langchain.com/docs/how_to/qa_sources/)
* [Azure](https://python.langchain.com/docs/how_to/qa_sources/)
* [Google Gemini](https://python.langchain.com/docs/how_to/qa_sources/)
* [Google Vertex](https://python.langchain.com/docs/how_to/qa_sources/)
* [AWS](https://python.langchain.com/docs/how_to/qa_sources/)
* [HuggingFace](https://python.langchain.com/docs/how_to/qa_sources/)
* [Ollama](https://python.langchain.com/docs/how_to/qa_sources/)
* [Cohere](https://python.langchain.com/docs/how_to/qa_sources/)
* [MistralAI](https://python.langchain.com/docs/how_to/qa_sources/)
* [Nomic](https://python.langchain.com/docs/how_to/qa_sources/)
* [NVIDIA](https://python.langchain.com/docs/how_to/qa_sources/)
* [Voyage AI](https://python.langchain.com/docs/how_to/qa_sources/)
* [IBM watsonx](https://python.langchain.com/docs/how_to/qa_sources/)
* [Fake](https://python.langchain.com/docs/how_to/qa_sources/)
```
pip install -qU langchain-openai
```

```
import getpassimport osifnot os.environ.get("OPENAI_API_KEY"): os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter API key for OpenAI: ")from langchain_openai import OpenAIEmbeddingsembeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

And a [vector store](https://python.langchain.com/docs/integrations/vectorstores/):
Select [vector store](https://python.langchain.com/docs/integrations/vectorstores/):
In-memory▾
* [In-memory](https://python.langchain.com/docs/how_to/qa_sources/)
* [AstraDB](https://python.langchain.com/docs/how_to/qa_sources/)
* [Chroma](https://python.langchain.com/docs/how_to/qa_sources/)
* [FAISS](https://python.langchain.com/docs/how_to/qa_sources/)
* [Milvus](https://python.langchain.com/docs/how_to/qa_sources/)
* [MongoDB](https://python.langchain.com/docs/how_to/qa_sources/)
* [PGVector](https://python.langchain.com/docs/how_to/qa_sources/)
* [Pinecone](https://python.langchain.com/docs/how_to/qa_sources/)
* [Qdrant](https://python.langchain.com/docs/how_to/qa_sources/)
```
pip install -qU langchain-core
```

```
from langchain_core.vectorstores import InMemoryVectorStorevector_store = InMemoryVectorStore(embeddings)
```

## RAG application[​](https://python.langchain.com/docs/how_to/qa_sources/#rag-application "Direct link to RAG application")
Let's reconstruct the Q&A app with sources we built over the [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) blog post by Lilian Weng in the [RAG tutorial](https://python.langchain.com/docs/tutorials/rag/).
First we index our documents:
```
import bs4from langchain import hubfrom langchain_community.document_loaders import WebBaseLoaderfrom langchain_core.documents import Documentfrom langchain_text_splitters import RecursiveCharacterTextSplitterfrom typing_extensions import List, TypedDict# Load and chunk contents of the blogloader = WebBaseLoader(  web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),  bs_kwargs=dict(    parse_only=bs4.SoupStrainer(      class_=("post-content","post-title","post-header"))),)docs = loader.load()text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)all_splits = text_splitter.split_documents(docs)
```

**API Reference:**[hub](https://python.langchain.com/api_reference/langchain/hub/langchain.hub.hub.html) | [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) | [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html)
```
# Index chunks_ = vector_store.add_documents(documents=all_splits)
```

Next we build the application:
```
from langchain import hubfrom langchain_core.documents import Documentfrom langgraph.graph import START, StateGraphfrom typing_extensions import List, TypedDict# Define prompt for question-answeringprompt = hub.pull("rlm/rag-prompt")# Define state for applicationclassState(TypedDict):  question:str  context: List[Document]  answer:str# Define application stepsdefretrieve(state: State):  retrieved_docs = vector_store.similarity_search(state["question"])return{"context": retrieved_docs}defgenerate(state: State):  docs_content ="\n\n".join(doc.page_content for doc in state["context"])  messages = prompt.invoke({"question": state["question"],"context": docs_content})  response = llm.invoke(messages)return{"answer": response.content}# Compile application and testgraph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

**API Reference:**[hub](https://python.langchain.com/api_reference/langchain/hub/langchain.hub.hub.html) | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)
```
from IPython.display import Image, displaydisplay(Image(graph.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/how_to/qa_sources/)
Because we're tracking the retrieved context in our application's state, it is accessible after invoking the application:
```
result = graph.invoke({"question":"What is Task Decomposition?"})print(f'Context: {result["context"]}\n\n')print(f'Answer: {result["answer"]}')
```

```
Context: [Document(id='c8471b37-07d8-4d51-856e-4b2c22bca88d', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.'), Document(id='acb7eb6f-f252-4353-aec2-f459135354ba', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.'), Document(id='4fae6668-7fec-4237-9b2d-78132f4f3f3f', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Resources:\n1. Internet access for searches and information gathering.\n2. Long Term memory management.\n3. GPT-3.5 powered Agents for delegation of simple tasks.\n4. File output.\n\nPerformance Evaluation:\n1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.\n2. Constructively self-criticize your big-picture behavior constantly.\n3. Reflect on past decisions and strategies to refine your approach.\n4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.'), Document(id='3c79dd86-595e-42e8-b64d-404780f9e2d9', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content="(3) Task execution: Expert models execute on the specific tasks and log results.\nInstruction:\n\nWith the input and the inference results, the AI assistant needs to describe the process and results. The previous stages can be formed as - User Input: {{ User Input }}, Task Planning: {{ Tasks }}, Model Selection: {{ Model Assignment }}, Task Execution: {{ Predictions }}. You must first answer the user's request in a straightforward manner. Then describe the task process and show your analysis and model inference results to the user in the first person. If inference results contain a file path, must tell the user the complete file path.")]Answer: Task Decomposition is the process of breaking down a complex task into smaller, manageable steps to facilitate execution. This can be achieved through techniques like Chain of Thought, which encourages step-by-step reasoning, or Tree of Thoughts, which explores multiple reasoning paths for each step. It can be implemented using simple prompts, specific instructions, or human input to effectively tackle the original task.
```

Here, `"context"` contains the sources that the LLM used in generating the response in `"answer"`.
## Structure sources in model response[​](https://python.langchain.com/docs/how_to/qa_sources/#structure-sources-in-model-response "Direct link to Structure sources in model response")
Up to this point, we've simply propagated the documents returned from the retrieval step through to the final response. But this may not illustrate what subset of information the model relied on when generating its answer. Below, we show how to structure sources into the model response, allowing the model to report what specific context it relied on for its answer.
It is straightforward to extend the above LangGraph implementation. Below, we make a simple change: we use the model's tool-calling features to generate [structured output](https://python.langchain.com/docs/how_to/structured_output/), consisting of an answer and list of sources. The schema for the response is represented in the `AnswerWithSources` TypedDict, below.
```
from typing import Listfrom typing_extensions import Annotated, TypedDict# Desired schema for responseclassAnswerWithSources(TypedDict):"""An answer to the question, with sources."""  answer:str  sources: Annotated[    List[str],...,"List of sources (author + year) used to answer the question",]classState(TypedDict):  question:str  context: List[Document]  answer: AnswerWithSourcesdefgenerate(state: State):  docs_content ="\n\n".join(doc.page_content for doc in state["context"])  messages = prompt.invoke({"question": state["question"],"context": docs_content})  structured_llm = llm.with_structured_output(AnswerWithSources)  response = structured_llm.invoke(messages)return{"answer": response}graph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

```
import jsonresult = graph.invoke({"question":"What is Chain of Thought?"})print(json.dumps(result["answer"], indent=2))
```

```
{ "answer": "Chain of Thought (CoT) is a prompting technique that enhances model performance by instructing it to think step by step, allowing the decomposition of complex tasks into smaller, manageable steps. This method not only aids in task execution but also provides insights into the model's reasoning process. CoT has become a standard approach in improving how language models handle intricate problem-solving tasks.", "sources": [  "Wei et al. 2022" ]}
```

tip
View [LangSmith trace](https://smith.langchain.com/public/51d543f7-bdf6-4d93-9ecd-2fc09bf6d666/r).
## Conversational RAG[​](https://python.langchain.com/docs/how_to/qa_sources/#conversational-rag "Direct link to Conversational RAG")
[Part 2](https://python.langchain.com/docs/tutorials/qa_chat_history/) of the RAG tutorial implements a different architecture, in which steps in the RAG flow are represented via successive [message](https://python.langchain.com/docs/concepts/messages/) objects. This leverages additional [tool-calling](https://python.langchain.com/docs/concepts/tool_calling/) features of chat models, and more naturally accommodates a "back-and-forth" conversational user experience.
In that tutorial (and below), we propagate the retrieved documents as [artifacts](https://python.langchain.com/docs/how_to/tool_artifacts/) on the tool messages. That makes it easy to pluck out the retrieved documents. Below, we add them as an additional key in the state, for convenience.
Note that we define the response format of the tool as `"content_and_artifact"`:
```
from langchain_core.tools import tool@tool(response_format="content_and_artifact")defretrieve(query:str):"""Retrieve information related to a query."""  retrieved_docs = vector_store.similarity_search(query, k=2)  serialized ="\n\n".join((f"Source: {doc.metadata}\n"f"Content: {doc.page_content}")for doc in retrieved_docs)return serialized, retrieved_docs
```

**API Reference:**[tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)
We can now build and compile the exact same application as in [Part 2](https://python.langchain.com/docs/tutorials/qa_chat_history/) of the RAG tutorial, with two changes:
  1. We add a `context` key of the state to store retrieved documents;
  2. In the `generate` step, we pluck out the retrieved documents and populate them in the state.


These changes are highlighted below.
```
from langchain_core.messages import SystemMessagefrom langgraph.graph import END, MessagesState, StateGraphfrom langgraph.prebuilt import ToolNode, tools_conditionclassState(MessagesState):  context: List[Document]# Step 1: Generate an AIMessage that may include a tool-call to be sent.defquery_or_respond(state: State):"""Generate tool call for retrieval or respond."""  llm_with_tools = llm.bind_tools([retrieve])  response = llm_with_tools.invoke(state["messages"])# MessagesState appends messages to state instead of overwritingreturn{"messages":[response]}# Step 2: Execute the retrieval.tools = ToolNode([retrieve])# Step 3: Generate a response using the retrieved content.defgenerate(state: MessagesState):"""Generate answer."""# Get generated ToolMessages  recent_tool_messages =[]for message inreversed(state["messages"]):if message.type=="tool":      recent_tool_messages.append(message)else:break  tool_messages = recent_tool_messages[::-1]# Format into prompt  docs_content ="\n\n".join(doc.content for doc in tool_messages)  system_message_content =("You are an assistant for question-answering tasks. ""Use the following pieces of retrieved context to answer ""the question. If you don't know the answer, say that you ""don't know. Use three sentences maximum and keep the ""answer concise.""\n\n"f"{docs_content}")  conversation_messages =[    messagefor message in state["messages"]if message.typein("human","system")or(message.type=="ai"andnot message.tool_calls)]  prompt =[SystemMessage(system_message_content)]+ conversation_messages# Run  response = llm.invoke(prompt)  context =[]for tool_message in tool_messages:    context.extend(tool_message.artifact)return{"messages":[response],"context": context}
```

**API Reference:**[SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) | [tools_condition](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.tools_condition)
We can compile the application as before:
```
graph_builder = StateGraph(MessagesState)graph_builder.add_node(query_or_respond)graph_builder.add_node(tools)graph_builder.add_node(generate)graph_builder.set_entry_point("query_or_respond")graph_builder.add_conditional_edges("query_or_respond",  tools_condition,{END: END,"tools":"tools"},)graph_builder.add_edge("tools","generate")graph_builder.add_edge("generate", END)graph = graph_builder.compile()
```

```
display(Image(graph.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/how_to/qa_sources/)
Invoking our application, we see that the retrieved [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) objects are accessible from the application state.
```
input_message ="What is Task Decomposition?"for step in graph.stream({"messages":[{"role":"user","content": input_message}]},  stream_mode="values",):  step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================What is Task Decomposition?==================================[1m Ai Message [0m==================================Tool Calls: retrieve (call_oA0XZ5hF70X0oW4ccNUFCFxX) Call ID: call_oA0XZ5hF70X0oW4ccNUFCFxX Args:  query: Task Decomposition=================================[1m Tool Message [0m=================================Name: retrieveSource: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Fig. 1. Overview of a LLM-powered autonomous agent system.Component One: Planning#A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.Task Decomposition#Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.==================================[1m Ai Message [0m==================================Task Decomposition is the process of breaking down a complicated task into smaller, manageable steps. It often utilizes techniques like Chain of Thought (CoT) prompting, which encourages models to think step by step, enhancing performance on complex tasks. This approach helps clarify the model's reasoning and makes it easier to tackle difficult problems.
```

```
step["context"]
```

```
[Document(id='c8471b37-07d8-4d51-856e-4b2c22bca88d', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.'), Document(id='acb7eb6f-f252-4353-aec2-f459135354ba', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.')]
```

tip
Check out the [LangSmith trace](https://smith.langchain.com/public/cc25515d-2e46-44fa-8bb2-b9cb0f451504/r).
[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/how_to/qa_sources.ipynb)
#### Was this page helpful?
  * [Setup](https://python.langchain.com/docs/how_to/qa_sources/#setup)
    * [Dependencies](https://python.langchain.com/docs/how_to/qa_sources/#dependencies)
    * [LangSmith](https://python.langchain.com/docs/how_to/qa_sources/#langsmith)
    * [Components](https://python.langchain.com/docs/how_to/qa_sources/#components)
  * [RAG application](https://python.langchain.com/docs/how_to/qa_sources/#rag-application)
  * [Structure sources in model response](https://python.langchain.com/docs/how_to/qa_sources/#structure-sources-in-model-response)
  * [Conversational RAG](https://python.langchain.com/docs/how_to/qa_sources/#conversational-rag)


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

