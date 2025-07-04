---
url: https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/
scraped_at: 2025-05-25T18:04:20.279657
title: Migrating off ConversationBufferWindowMemory or ConversationTokenBufferMemory | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/)
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
    * [v0.2](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/)
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
  * [Upgrading to LangGraph memory](https://python.langchain.com/docs/versions/migrating_memory/)
  * Migrating off ConversationBufferWindowMemory or ConversationTokenBufferMemory


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/versions/migrating_memory/conversation_buffer_window_memory.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/versions/migrating_memory/conversation_buffer_window_memory.ipynb)
# Migrating off ConversationBufferWindowMemory or ConversationTokenBufferMemory
Follow this guide if you're trying to migrate off one of the old memory classes listed below:
Memory Type| Description  
---|---  
`ConversationBufferWindowMemory`| Keeps the last `n` messages of the conversation. Drops the oldest messages when there are more than `n` messages.  
`ConversationTokenBufferMemory`| Keeps only the most recent messages in the conversation under the constraint that the total number of tokens in the conversation does not exceed a certain limit.  
`ConversationBufferWindowMemory` and `ConversationTokenBufferMemory` apply additional processing on top of the raw conversation history to trim the conversation history to a size that fits inside the context window of a chat model.
This processing functionality can be accomplished using LangChain's built-in [trim_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html) function.
important
We’ll begin by exploring a straightforward method that involves applying processing logic to the entire conversation history.
While this approach is easy to implement, it has a downside: as the conversation grows, so does the latency, since the logic is re-applied to all previous exchanges in the conversation at each turn.
More advanced strategies focus on incrementally updating the conversation history to avoid redundant processing.
For instance, the langgraph [how-to guide on summarization](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/) demonstrates how to maintain a running summary of the conversation while discarding older messages, ensuring they aren't re-processed during later turns.
## Set up[​](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#set-up "Direct link to Set up")
```
%%capture --no-stderr%pip install --upgrade --quiet langchain-openai langchain
```

```
import osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

## Legacy usage with LLMChain / Conversation Chain[​](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#legacy-usage-with-llmchain--conversation-chain "Direct link to Legacy usage with LLMChain / Conversation Chain")
Details
```
from langchain.chains import LLMChainfrom langchain.memory import ConversationBufferWindowMemoryfrom langchain_core.messages import SystemMessagefrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.prompts.chat import(  ChatPromptTemplate,  HumanMessagePromptTemplate,  MessagesPlaceholder,)from langchain_openai import ChatOpenAIprompt = ChatPromptTemplate([    SystemMessage(content="You are a helpful assistant."),    MessagesPlaceholder(variable_name="chat_history"),    HumanMessagePromptTemplate.from_template("{text}"),])memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True)legacy_chain = LLMChain(  llm=ChatOpenAI(),  prompt=prompt,  memory=memory,)legacy_result = legacy_chain.invoke({"text":"my name is bob"})print(legacy_result)legacy_result = legacy_chain.invoke({"text":"what was my name"})print(legacy_result)
```

**API Reference:**[LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html) | [ConversationBufferWindowMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer_window.ConversationBufferWindowMemory.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [HumanMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.HumanMessagePromptTemplate.html) | [MessagesPlaceholder](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
```
{'text': 'Nice to meet you, Bob! How can I assist you today?', 'chat_history': []}{'text': 'Your name is Bob. How can I assist you further, Bob?', 'chat_history': [HumanMessage(content='my name is bob', additional_kwargs={}, response_metadata={}), AIMessage(content='Nice to meet you, Bob! How can I assist you today?', additional_kwargs={}, response_metadata={})]}
```

## Reimplementing ConversationBufferWindowMemory logic[​](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#reimplementing-conversationbufferwindowmemory-logic "Direct link to Reimplementing ConversationBufferWindowMemory logic")
Let's first create appropriate logic to process the conversation history, and then we'll see how to integrate it into an application. You can later replace this basic setup with more advanced logic tailored to your specific needs.
We'll use `trim_messages` to implement logic that keeps the last `n` messages of the conversation. It will drop the oldest messages when the number of messages exceeds `n`.
In addition, we will also keep the system message if it's present -- when present, it's the first message in a conversation that includes instructions for the chat model.
```
from langchain_core.messages import(  AIMessage,  BaseMessage,  HumanMessage,  SystemMessage,  trim_messages,)from langchain_openai import ChatOpenAImessages =[  SystemMessage("you're a good assistant, you always respond with a joke."),  HumanMessage("i wonder why it's called langchain"),  AIMessage('Well, I guess they thought "WordRope" and "SentenceString" just didn\'t have the same ring to it!'),  HumanMessage("and who is harrison chasing anyways"),  AIMessage("Hmmm let me think.\n\nWhy, he's probably chasing after the last cup of coffee in the office!"),  HumanMessage("why is 42 always the answer?"),  AIMessage("Because it’s the only number that’s constantly right, even when it doesn’t add up!"),  HumanMessage("What did the cow say?"),]
```

**API Reference:**[AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [trim_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
```
from langchain_core.messages import trim_messagesselected_messages = trim_messages(  messages,  token_counter=len,# <-- len will simply count the number of messages rather than tokens  max_tokens=5,# <-- allow up to 5 messages.  strategy="last",# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage# start_on="human" makes sure we produce a valid chat history  start_on="human",# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.  include_system=True,  allow_partial=False,)for msg in selected_messages:  msg.pretty_print()
```

**API Reference:**[trim_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html)
```
================================[1m System Message [0m================================you're a good assistant, you always respond with a joke.==================================[1m Ai Message [0m==================================Hmmm let me think.Why, he's probably chasing after the last cup of coffee in the office!================================[1m Human Message [0m=================================why is 42 always the answer?==================================[1m Ai Message [0m==================================Because it’s the only number that’s constantly right, even when it doesn’t add up!================================[1m Human Message [0m=================================What did the cow say?
```

## Reimplementing ConversationTokenBufferMemory logic[​](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#reimplementing-conversationtokenbuffermemory-logic "Direct link to Reimplementing ConversationTokenBufferMemory logic")
Here, we'll use `trim_messages` to keeps the system message and the most recent messages in the conversation under the constraint that the total number of tokens in the conversation does not exceed a certain limit.
```
from langchain_core.messages import trim_messagesselected_messages = trim_messages(  messages,# Please see API reference for trim_messages for other ways to specify a token counter.  token_counter=ChatOpenAI(model="gpt-4o"),  max_tokens=80,# <-- token limit# The start_on is specified# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage# start_on="human" makes sure we produce a valid chat history  start_on="human",# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.  include_system=True,  strategy="last",)for msg in selected_messages:  msg.pretty_print()
```

**API Reference:**[trim_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html)
```
================================[1m System Message [0m================================you're a good assistant, you always respond with a joke.================================[1m Human Message [0m=================================why is 42 always the answer?==================================[1m Ai Message [0m==================================Because it’s the only number that’s constantly right, even when it doesn’t add up!================================[1m Human Message [0m=================================What did the cow say?
```

## Modern usage with LangGraph[​](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#modern-usage-with-langgraph "Direct link to Modern usage with LangGraph")
The example below shows how to use LangGraph to add simple conversation pre-processing logic.
note
If you want to avoid running the computation on the entire conversation history each time, you can follow the [how-to guide on summarization](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/) that demonstrates how to discard older messages, ensuring they aren't re-processed during later turns.
Details
```
import uuidfrom IPython.display import Image, displayfrom langchain_core.messages import HumanMessagefrom langgraph.checkpoint.memory import MemorySaverfrom langgraph.graph import START, MessagesState, StateGraph# Define a new graphworkflow = StateGraph(state_schema=MessagesState)# Define a chat modelmodel = ChatOpenAI()# Define the function that calls the modeldefcall_model(state: MessagesState):  selected_messages = trim_messages(    state["messages"],    token_counter=len,# <-- len will simply count the number of messages rather than tokens    max_tokens=5,# <-- allow up to 5 messages.    strategy="last",# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage# start_on="human" makes sure we produce a valid chat history    start_on="human",# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.    include_system=True,    allow_partial=False,)  response = model.invoke(selected_messages)# We return a list, because this will get added to the existing listreturn{"messages": response}# Define the two nodes we will cycle betweenworkflow.add_edge(START,"model")workflow.add_node("model", call_model)# Adding memory is straight forward in langgraph!memory = MemorySaver()app = workflow.compile(  checkpointer=memory)# The thread id is a unique key that identifies# this particular conversation.# We'll just generate a random uuid here.thread_id = uuid.uuid4()config ={"configurable":{"thread_id": thread_id}}input_message = HumanMessage(content="hi! I'm bob")for event in app.stream({"messages":[input_message]}, config, stream_mode="values"):  event["messages"][-1].pretty_print()# Here, let's confirm that the AI remembers our name!config ={"configurable":{"thread_id": thread_id}}input_message = HumanMessage(content="what was my name?")for event in app.stream({"messages":[input_message]}, config, stream_mode="values"):  event["messages"][-1].pretty_print()
```

**API Reference:**[HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)
```
================================[1m Human Message [0m=================================hi! I'm bob==================================[1m Ai Message [0m==================================Hello Bob! How can I assist you today?================================[1m Human Message [0m=================================what was my name?==================================[1m Ai Message [0m==================================Your name is Bob. How can I help you, Bob?
```

## Usage with a pre-built langgraph agent[​](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#usage-with-a-pre-built-langgraph-agent "Direct link to Usage with a pre-built langgraph agent")
This example shows usage of an Agent Executor with a pre-built agent constructed using the [create_tool_calling_agent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.tool_calling_agent.base.create_tool_calling_agent.html) function.
If you are using one of the [old LangChain pre-built agents](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/), you should be able to replace that code with the new [langgraph pre-built agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/) which leverages native tool calling capabilities of chat models and will likely work better out of the box.
Details
```
import uuidfrom langchain_core.messages import(  AIMessage,  BaseMessage,  HumanMessage,  SystemMessage,  trim_messages,)from langchain_core.tools import toolfrom langchain_openai import ChatOpenAIfrom langgraph.checkpoint.memory import MemorySaverfrom langgraph.prebuilt import create_react_agent@tooldefget_user_age(name:str)->str:"""Use this tool to find the user's age."""# This is a placeholder for the actual implementationif"bob"in name.lower():return"42 years old"return"41 years old"memory = MemorySaver()model = ChatOpenAI()defprompt(state)->list[BaseMessage]:"""Given the agent state, return a list of messages for the chat model."""# We're using the message processor defined above.return trim_messages(    state["messages"],    token_counter=len,# <-- len will simply count the number of messages rather than tokens    max_tokens=5,# <-- allow up to 5 messages.    strategy="last",# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage# start_on="human" makes sure we produce a valid chat history    start_on="human",# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.    include_system=True,    allow_partial=False,)app = create_react_agent(  model,  tools=[get_user_age],  checkpointer=memory,  prompt=prompt,)# The thread id is a unique key that identifies# this particular conversation.# We'll just generate a random uuid here.thread_id = uuid.uuid4()config ={"configurable":{"thread_id": thread_id}}# Tell the AI that our name is Bob, and ask it to use a tool to confirm# that it's capable of working like an agent.input_message = HumanMessage(content="hi! I'm bob. What is my age?")for event in app.stream({"messages":[input_message]}, config, stream_mode="values"):  event["messages"][-1].pretty_print()# Confirm that the chat bot has access to previous conversation# and can respond to the user saying that the user's name is Bob.input_message = HumanMessage(content="do you remember my name?")for event in app.stream({"messages":[input_message]}, config, stream_mode="values"):  event["messages"][-1].pretty_print()
```

**API Reference:**[AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [trim_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)
```
================================[1m Human Message [0m=================================hi! I'm bob. What is my age?==================================[1m Ai Message [0m==================================Tool Calls: get_user_age (call_jsMvoIFv970DhqqLCJDzPKsp) Call ID: call_jsMvoIFv970DhqqLCJDzPKsp Args:  name: bob=================================[1m Tool Message [0m=================================Name: get_user_age42 years old==================================[1m Ai Message [0m==================================Bob, you are 42 years old.================================[1m Human Message [0m=================================do you remember my name?==================================[1m Ai Message [0m==================================Yes, your name is Bob.
```

## LCEL: Add a preprocessing step[​](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#lcel-add-a-preprocessing-step "Direct link to LCEL: Add a preprocessing step")
The simplest way to add complex conversation management is by introducing a pre-processing step in front of the chat model and pass the full conversation history to the pre-processing step.
This approach is conceptually simple and will work in many situations; for example, if using a [RunnableWithMessageHistory](https://python.langchain.com/docs/how_to/message_history/) instead of wrapping the chat model, wrap the chat model with the pre-processor.
The obvious downside of this approach is that latency starts to increase as the conversation history grows because of two reasons:
  1. As the conversation gets longer, more data may need to be fetched from whatever store your'e using to store the conversation history (if not storing it in memory).
  2. The pre-processing logic will end up doing a lot of redundant computation, repeating computation from previous steps of the conversation.


caution
If you want to use a chat model's tool calling capabilities, remember to bind the tools to the model before adding the history pre-processing step to it!
Details
```
from langchain_core.messages import(  AIMessage,  BaseMessage,  HumanMessage,  SystemMessage,  trim_messages,)from langchain_core.tools import toolfrom langchain_openai import ChatOpenAImodel = ChatOpenAI()@tooldefwhat_did_the_cow_say()->str:"""Check to see what the cow said."""return"foo"message_processor = trim_messages(# Returns a Runnable if no messages are provided  token_counter=len,# <-- len will simply count the number of messages rather than tokens  max_tokens=5,# <-- allow up to 5 messages.  strategy="last",# The start_on is specified# to make sure we do not generate a sequence where# a ToolMessage that contains the result of a tool invocation# appears before the AIMessage that requested a tool invocation# as this will cause some chat models to raise an error.  start_on=("human","ai"),  include_system=True,# <-- Keep the system message  allow_partial=False,)# Note that we bind tools to the model first!model_with_tools = model.bind_tools([what_did_the_cow_say])model_with_preprocessor = message_processor | model_with_toolsfull_history =[  SystemMessage("you're a good assistant, you always respond with a joke."),  HumanMessage("i wonder why it's called langchain"),  AIMessage('Well, I guess they thought "WordRope" and "SentenceString" just didn\'t have the same ring to it!'),  HumanMessage("and who is harrison chasing anyways"),  AIMessage("Hmmm let me think.\n\nWhy, he's probably chasing after the last cup of coffee in the office!"),  HumanMessage("why is 42 always the answer?"),  AIMessage("Because it’s the only number that’s constantly right, even when it doesn’t add up!"),  HumanMessage("What did the cow say?"),]# We pass it explicity to the model_with_preprocesor for illustrative purposes.# If you're using `RunnableWithMessageHistory` the history will be automatically# read from the source the you configure.model_with_preprocessor.invoke(full_history).pretty_print()
```

**API Reference:**[AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [trim_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
```
==================================[1m Ai Message [0m==================================Tool Calls: what_did_the_cow_say (call_urHTB5CShhcKz37QiVzNBlIS) Call ID: call_urHTB5CShhcKz37QiVzNBlIS Args:
```

If you need to implement more efficient logic and want to use `RunnableWithMessageHistory` for now the way to achieve this is to subclass from [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html) and define appropriate logic for `add_messages` (that doesn't simply append the history, but instead re-writes it).
Unless you have a good reason to implement this solution, you should instead use LangGraph.
## Next steps[​](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#next-steps "Direct link to Next steps")
Explore persistence with LangGraph:
  * [LangGraph quickstart tutorial](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
  * [How to add persistence ("memory") to your graph](https://langchain-ai.github.io/langgraph/how-tos/persistence/)
  * [How to manage conversation history](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/)
  * [How to add summary of the conversation history](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/)


Add persistence with simple LCEL (favor langgraph for more complex use cases):
  * [How to add message history](https://python.langchain.com/docs/how_to/message_history/)


Working with message history:
  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)
  * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)
  * [How to merge message runs](https://python.langchain.com/docs/how_to/merge_message_runs/)


[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/versions/migrating_memory/conversation_buffer_window_memory.ipynb)
#### Was this page helpful?
[PreviousMigrating off ConversationBufferMemory or ConversationStringBufferMemory](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_memory/)[NextMigrating off ConversationSummaryMemory or ConversationSummaryBufferMemory](https://python.langchain.com/docs/versions/migrating_memory/conversation_summary_memory/)
  * [Set up](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#set-up)
  * [Legacy usage with LLMChain / Conversation Chain](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#legacy-usage-with-llmchain--conversation-chain)
  * [Reimplementing ConversationBufferWindowMemory logic](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#reimplementing-conversationbufferwindowmemory-logic)
  * [Reimplementing ConversationTokenBufferMemory logic](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#reimplementing-conversationtokenbuffermemory-logic)
  * [Modern usage with LangGraph](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#modern-usage-with-langgraph)
  * [Usage with a pre-built langgraph agent](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#usage-with-a-pre-built-langgraph-agent)
  * [LCEL: Add a preprocessing step](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#lcel-add-a-preprocessing-step)
  * [Next steps](https://python.langchain.com/docs/versions/migrating_memory/conversation_buffer_window_memory/#next-steps)


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

