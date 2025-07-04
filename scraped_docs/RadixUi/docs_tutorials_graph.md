---
url: https://python.langchain.com/docs/tutorials/graph/
scraped_at: 2025-05-25T17:54:01.452717
title: Build a Question Answering application over a Graph Database | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/tutorials/graph/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/tutorials/graph/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/tutorials/graph/)
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
    * [v0.2](https://python.langchain.com/docs/tutorials/graph/)
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
  * Build a Question Answering application over a Graph Database


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/tutorials/graph.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/tutorials/graph.ipynb)
# Build a Question Answering application over a Graph Database
In this guide we'll go over the basic ways to create a Q&A chain over a graph database. These systems will allow us to ask a question about the data in a graph database and get back a natural language answer. First, we will show a simple out-of-the-box option and then implement a more sophisticated version with LangGraph.
## ⚠️ Security note ⚠️[​](https://python.langchain.com/docs/tutorials/graph/#️-security-note-️ "Direct link to ⚠️ Security note ⚠️")
Building Q&A systems of graph databases requires executing model-generated graph queries. There are inherent risks in doing this. Make sure that your database connection permissions are always scoped as narrowly as possible for your chain/agent's needs. This will mitigate though not eliminate the risks of building a model-driven system. For more on general security best practices, [see here](https://python.langchain.com/docs/security/).
## Architecture[​](https://python.langchain.com/docs/tutorials/graph/#architecture "Direct link to Architecture")
At a high-level, the steps of most graph chains are:
  1. **Convert question to a graph database query** : Model converts user input to a graph database query (e.g. Cypher).
  2. **Execute graph database query** : Execute the graph database query.
  3. **Answer the question** : Model responds to user input using the query results.


![sql_usecase.png](https://python.langchain.com/assets/images/graph_usecase-34d891523e6284bb6230b38c5f8392e5.png)
## Setup[​](https://python.langchain.com/docs/tutorials/graph/#setup "Direct link to Setup")
First, get required packages and set environment variables. In this example, we will be using Neo4j graph database.
```
%pip install --upgrade --quiet langchain langchain-neo4j langchain-openai langgraph
```

We default to OpenAI models in this guide.
```
import getpassimport osif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter your OpenAI API key: ")# Uncomment the below to use LangSmith. Not required.# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()# os.environ["LANGSMITH_TRACING"] = "true"
```

```
Enter your OpenAI API key: ········
```

Next, we need to define Neo4j credentials. Follow [these installation steps](https://neo4j.com/docs/operations-manual/current/installation/) to set up a Neo4j database.
```
os.environ["NEO4J_URI"]="bolt://localhost:7687"os.environ["NEO4J_USERNAME"]="neo4j"os.environ["NEO4J_PASSWORD"]="password"
```

The below example will create a connection with a Neo4j database and will populate it with example data about movies and their actors.
```
from langchain_neo4j import Neo4jGraphgraph = Neo4jGraph()# Import movie informationmovies_query ="""LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/movies/movies_small.csv'AS rowMERGE (m:Movie {id:row.movieId})SET m.released = date(row.released),  m.title = row.title,  m.imdbRating = toFloat(row.imdbRating)FOREACH (director in split(row.director, '|') |   MERGE (p:Person {name:trim(director)})  MERGE (p)-[:DIRECTED]->(m))FOREACH (actor in split(row.actors, '|') |   MERGE (p:Person {name:trim(actor)})  MERGE (p)-[:ACTED_IN]->(m))FOREACH (genre in split(row.genres, '|') |   MERGE (g:Genre {name:trim(genre)})  MERGE (m)-[:IN_GENRE]->(g))"""graph.query(movies_query)
```

**API Reference:**[Neo4jGraph](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.neo4j_graph.Neo4jGraph.html)
```
[]
```

## Graph schema[​](https://python.langchain.com/docs/tutorials/graph/#graph-schema "Direct link to Graph schema")
In order for an LLM to be able to generate a Cypher statement, it needs information about the graph schema. When you instantiate a graph object, it retrieves the information about the graph schema. If you later make any changes to the graph, you can run the `refresh_schema` method to refresh the schema information.
```
graph.refresh_schema()print(graph.schema)
```

```
Node properties:Person {name: STRING}Movie {id: STRING, released: DATE, title: STRING, imdbRating: FLOAT}Genre {name: STRING}Chunk {id: STRING, embedding: LIST, text: STRING, question: STRING, query: STRING}Relationship properties:The relationships:(:Person)-[:DIRECTED]->(:Movie)(:Person)-[:ACTED_IN]->(:Movie)(:Movie)-[:IN_GENRE]->(:Genre)
```

For more involved schema information, you can use `enhanced_schema` option.
```
enhanced_graph = Neo4jGraph(enhanced_schema=True)print(enhanced_graph.schema)
```

```
Received notification from DBMS server: {severity: WARNING} {code: Neo.ClientNotification.Statement.FeatureDeprecationWarning} {category: DEPRECATION} {title: This feature is deprecated and will be removed in future versions.} {description: The procedure has a deprecated field. ('config' used by 'apoc.meta.graphSample' is deprecated.)} {position: line: 1, column: 1, offset: 0} for query: "CALL apoc.meta.graphSample() YIELD nodes, relationships RETURN nodes, [rel in relationships | {name:apoc.any.property(rel, 'type'), count: apoc.any.property(rel, 'count')}] AS relationships"``````outputNode properties:- **Person** - `name`: STRING Example: "John Lasseter"- **Movie** - `id`: STRING Example: "1" - `released`: DATE Min: 1964-12-16, Max: 1996-09-15 - `title`: STRING Example: "Toy Story" - `imdbRating`: FLOAT Min: 2.4, Max: 9.3- **Genre** - `name`: STRING Example: "Adventure"- **Chunk** - `id`: STRING Available options: ['d66006059fd78d63f3df90cc1059639a', '0e3dcb4502853979d12357690a95ec17', 'c438c6bcdcf8e4fab227f29f8e7ff204', '97fe701ec38057594464beaa2df0710e', 'b54f9286e684373498c4504b4edd9910', '5b50a72c3a4954b0ff7a0421be4f99b9', 'fb28d41771e717255f0d8f6c799ede32', '58e6f14dd2e6c6702cf333f2335c499c'] - `text`: STRING Available options: ['How many artists are there?', 'Which actors played in the movie Casino?', 'How many movies has Tom Hanks acted in?', "List all the genres of the movie Schindler's List", 'Which actors have worked in movies from both the c', 'Which directors have made movies with at least thr', 'Identify movies where directors also played a role', 'Find the actor with the highest number of movies i'] - `question`: STRING Available options: ['How many artists are there?', 'Which actors played in the movie Casino?', 'How many movies has Tom Hanks acted in?', "List all the genres of the movie Schindler's List", 'Which actors have worked in movies from both the c', 'Which directors have made movies with at least thr', 'Identify movies where directors also played a role', 'Find the actor with the highest number of movies i'] - `query`: STRING Available options: ['MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN coun', "MATCH (m:Movie {title: 'Casino'})<-[:ACTED_IN]-(a)", "MATCH (a:Person {name: 'Tom Hanks'})-[:ACTED_IN]->", "MATCH (m:Movie {title: 'Schindler's List'})-[:IN_G", 'MATCH (a:Person)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]', 'MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_I', 'MATCH (p:Person)-[:DIRECTED]->(m:Movie), (p)-[:ACT', 'MATCH (a:Actor)-[:ACTED_IN]->(m:Movie) RETURN a.na']Relationship properties:The relationships:(:Person)-[:DIRECTED]->(:Movie)(:Person)-[:ACTED_IN]->(:Movie)(:Movie)-[:IN_GENRE]->(:Genre)
```

The `enhanced_schema` option enriches property information by including details such as minimum and maximum values for floats and dates, as well as example values for string properties. This additional context helps guide the LLM toward generating more accurate and effective queries.
Great! We've got a graph database that we can query. Now let's try hooking it up to an LLM.
## GraphQACypherChain[​](https://python.langchain.com/docs/tutorials/graph/#graphqacypherchain "Direct link to GraphQACypherChain")
Let's use a simple out-of-the-box chain that takes a question, turns it into a Cypher query, executes the query, and uses the result to answer the original question.
![graph_chain.webp](https://python.langchain.com/assets/images/graph_chain-6379941793e0fa985e51e4bda0329403.webp)
LangChain comes with a built-in chain for this workflow that is designed to work with Neo4j: [GraphCypherQAChain](https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/)
```
from langchain_neo4j import GraphCypherQAChainfrom langchain_openai import ChatOpenAIllm = ChatOpenAI(model="gpt-4o", temperature=0)chain = GraphCypherQAChain.from_llm(  graph=enhanced_graph, llm=llm, verbose=True, allow_dangerous_requests=True)response = chain.invoke({"query":"What was the cast of the Casino?"})response
```

**API Reference:**[GraphCypherQAChain](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher.GraphCypherQAChain.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
```
[1m> Entering new GraphCypherQAChain chain...[0mGenerated Cypher:[32;1m[1;3mcypherMATCH (p:Person)-[:ACTED_IN]->(m:Movie {title: "Casino"})RETURN p.name[0mFull Context:[32;1m[1;3m[{'p.name': 'Robert De Niro'}, {'p.name': 'Joe Pesci'}, {'p.name': 'Sharon Stone'}, {'p.name': 'James Woods'}][0m[1m> Finished chain.[0m
```

```
{'query': 'What was the cast of the Casino?', 'result': 'Robert De Niro, Joe Pesci, Sharon Stone, and James Woods were the cast of Casino.'}
```

## Advanced implementation with LangGraph[​](https://python.langchain.com/docs/tutorials/graph/#advanced-implementation-with-langgraph "Direct link to Advanced implementation with LangGraph")
While the GraphCypherQAChain is effective for quick demonstrations, it may face challenges in production environments. Transitioning to LangGraph can enhance the workflow, but implementing natural language to query flows in production remains a complex task. Nevertheless, there are several strategies to significantly improve accuracy and reliability, which we will explore next.
Here is the visualized LangGraph flow we will implement:
![langgraph_text2cypher](https://python.langchain.com/assets/images/langgraph_text2cypher-1414c073e151b391ef08fed77915e3c0.webp)
We will begin by defining the Input, Output, and Overall state of the LangGraph application.
```
from operator import addfrom typing import Annotated, Listfrom typing_extensions import TypedDictclassInputState(TypedDict):  question:strclassOverallState(TypedDict):  question:str  next_action:str  cypher_statement:str  cypher_errors: List[str]  database_records: List[dict]  steps: Annotated[List[str], add]classOutputState(TypedDict):  answer:str  steps: List[str]  cypher_statement:str
```

The first step is a simple `guardrails` step, where we validate whether the question pertains to movies or their cast. If it doesn't, we notify the user that we cannot answer any other questions. Otherwise, we move on to the Cypher generation step.
```
from typing import Literalfrom langchain_core.prompts import ChatPromptTemplatefrom pydantic import BaseModel, Fieldguardrails_system ="""As an intelligent assistant, your primary objective is to decide whether a given question is related to movies or not. If the question is related to movies, output "movie". Otherwise, output "end".To make this decision, assess the content of the question and determine if it refers to any movie, actor, director, film industry, or related topics. Provide only the specified output: "movie" or "end"."""guardrails_prompt = ChatPromptTemplate.from_messages([("system",      guardrails_system,),("human",("{question}"),),])classGuardrailsOutput(BaseModel):  decision: Literal["movie","end"]= Field(    description="Decision on whether the question is related to movies")guardrails_chain = guardrails_prompt | llm.with_structured_output(GuardrailsOutput)defguardrails(state: InputState)-> OverallState:"""  Decides if the question is related to movies or not.  """  guardrails_output = guardrails_chain.invoke({"question": state.get("question")})  database_records =Noneif guardrails_output.decision =="end":    database_records ="This questions is not about movies or their cast. Therefore I cannot answer this question."return{"next_action": guardrails_output.decision,"database_records": database_records,"steps":["guardrail"],}
```

**API Reference:**[ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)
### Few-shot prompting[​](https://python.langchain.com/docs/tutorials/graph/#few-shot-prompting "Direct link to Few-shot prompting")
Converting natural language into accurate queries is challenging. One way to enhance this process is by providing relevant few-shot examples to guide the LLM in query generation. To achieve this, we will use the `SemanticSimilarityExampleSelector` to dynamically select the most relevant examples.
```
from langchain_core.example_selectors import SemanticSimilarityExampleSelectorfrom langchain_neo4j import Neo4jVectorfrom langchain_openai import OpenAIEmbeddingsexamples =[{"question":"How many artists are there?","query":"MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN count(DISTINCT a)",},{"question":"Which actors played in the movie Casino?","query":"MATCH (m:Movie {title: 'Casino'})<-[:ACTED_IN]-(a) RETURN a.name",},{"question":"How many movies has Tom Hanks acted in?","query":"MATCH (a:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)",},{"question":"List all the genres of the movie Schindler's List","query":"MATCH (m:Movie {title: 'Schindler's List'})-[:IN_GENRE]->(g:Genre) RETURN g.name",},{"question":"Which actors have worked in movies from both the comedy and action genres?","query":"MATCH (a:Person)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g1:Genre), (a)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g2:Genre) WHERE g1.name = 'Comedy' AND g2.name = 'Action' RETURN DISTINCT a.name",},{"question":"Which directors have made movies with at least three different actors named 'John'?","query":"MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person) WHERE a.name STARTS WITH 'John' WITH d, COUNT(DISTINCT a) AS JohnsCount WHERE JohnsCount >= 3 RETURN d.name",},{"question":"Identify movies where directors also played a role in the film.","query":"MATCH (p:Person)-[:DIRECTED]->(m:Movie), (p)-[:ACTED_IN]->(m) RETURN m.title, p.name",},{"question":"Find the actor with the highest number of movies in the database.","query":"MATCH (a:Actor)-[:ACTED_IN]->(m:Movie) RETURN a.name, COUNT(m) AS movieCount ORDER BY movieCount DESC LIMIT 1",},]example_selector = SemanticSimilarityExampleSelector.from_examples(  examples, OpenAIEmbeddings(), Neo4jVector, k=5, input_keys=["question"])
```

**API Reference:**[SemanticSimilarityExampleSelector](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector.html) | [Neo4jVector](https://python.langchain.com/api_reference/neo4j/vectorstores/langchain_neo4j.vectorstores.neo4j_vector.Neo4jVector.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)
Next, we implement the Cypher generation chain, also known as **text2cypher**. The prompt includes an enhanced graph schema, dynamically selected few-shot examples, and the user’s question. This combination enables the generation of a Cypher query to retrieve relevant information from the database.
```
from langchain_core.output_parsers import StrOutputParsertext2cypher_prompt = ChatPromptTemplate.from_messages([("system",("Given an input question, convert it to a Cypher query. No pre-amble.""Do not wrap the response in any backticks or anything else. Respond with a Cypher statement only!"),),("human",("""You are a Neo4j expert. Given an input question, create a syntactically correct Cypher query to run.Do not wrap the response in any backticks or anything else. Respond with a Cypher statement only!Here is the schema information{schema}Below are a number of examples of questions and their corresponding Cypher queries.{fewshot_examples}User input: {question}Cypher query:"""),),])text2cypher_chain = text2cypher_prompt | llm | StrOutputParser()defgenerate_cypher(state: OverallState)-> OverallState:"""  Generates a cypher statement based on the provided schema and user input  """  NL ="\n"  fewshot_examples =(NL *2).join([f"Question: {el['question']}{NL}Cypher:{el['query']}"for el in example_selector.select_examples({"question": state.get("question")})])  generated_cypher = text2cypher_chain.invoke({"question": state.get("question"),"fewshot_examples": fewshot_examples,"schema": enhanced_graph.schema,})return{"cypher_statement": generated_cypher,"steps":["generate_cypher"]}
```

**API Reference:**[StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)
### Query validation[​](https://python.langchain.com/docs/tutorials/graph/#query-validation "Direct link to Query validation")
The next step is to validate the generated Cypher statement and ensuring that all property values are accurate. While numbers and dates typically don’t require validation, strings such as movie titles or people’s names do. In this example, we’ll use a basic `CONTAINS` clause for validation, though more advanced mapping and validation techniques can be implemented if needed.
First, we will create a chain that detects any errors in the Cypher statement and extracts the property values it references.
```
from typing import List, Optionalvalidate_cypher_system ="""You are a Cypher expert reviewing a statement written by a junior developer."""validate_cypher_user ="""You must check the following:* Are there any syntax errors in the Cypher statement?* Are there any missing or undefined variables in the Cypher statement?* Are any node labels missing from the schema?* Are any relationship types missing from the schema?* Are any of the properties not included in the schema?* Does the Cypher statement include enough information to answer the question?Examples of good errors:* Label (:Foo) does not exist, did you mean (:Bar)?* Property bar does not exist for label Foo, did you mean baz?* Relationship FOO does not exist, did you mean FOO_BAR?Schema:{schema}The question is:{question}The Cypher statement is:{cypher}Make sure you don't make any mistakes!"""validate_cypher_prompt = ChatPromptTemplate.from_messages([("system",      validate_cypher_system,),("human",(validate_cypher_user),),])classProperty(BaseModel):"""  Represents a filter condition based on a specific node property in a graph in a Cypher statement.  """  node_label:str= Field(    description="The label of the node to which this property belongs.")  property_key:str= Field(description="The key of the property being filtered.")  property_value:str= Field(    description="The value that the property is being matched against.")classValidateCypherOutput(BaseModel):"""  Represents the validation result of a Cypher query's output,  including any errors and applied filters.  """  errors: Optional[List[str]]= Field(    description="A list of syntax or semantical errors in the Cypher statement. Always explain the discrepancy between schema and Cypher statement")  filters: Optional[List[Property]]= Field(    description="A list of property-based filters applied in the Cypher statement.")validate_cypher_chain = validate_cypher_prompt | llm.with_structured_output(  ValidateCypherOutput)
```

LLMs often struggle with correctly determining relationship directions in generated Cypher statements. Since we have access to the schema, we can deterministically correct these directions using the **CypherQueryCorrector**.
_Note: The`CypherQueryCorrector` is an experimental feature and doesn't support all the newest Cypher syntax._
```
from langchain_neo4j.chains.graph_qa.cypher_utils import CypherQueryCorrector, Schema# Cypher query corrector is experimentalcorrector_schema =[  Schema(el["start"], el["type"], el["end"])for el in enhanced_graph.structured_schema.get("relationships")]cypher_query_corrector = CypherQueryCorrector(corrector_schema)
```

**API Reference:**[CypherQueryCorrector](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.CypherQueryCorrector.html) | [Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html)
Now we can implement the Cypher validation step. First, we use the `EXPLAIN` method to detect any syntax errors. Next, we leverage the LLM to identify potential issues and extract the properties used for filtering. For string properties, we validate them against the database using a simple `CONTAINS` clause.
Based on the validation results, the process can take the following paths:
  * If value mapping fails, we end the conversation and inform the user that we couldn't identify a specific property value (e.g., a person or movie title).
  * If errors are found, we route the query for correction.
  * If no issues are detected, we proceed to the Cypher execution step.


```
from neo4j.exceptions import CypherSyntaxErrordefvalidate_cypher(state: OverallState)-> OverallState:"""  Validates the Cypher statements and maps any property values to the database.  """  errors =[]  mapping_errors =[]# Check for syntax errorstry:    enhanced_graph.query(f"EXPLAIN {state.get('cypher_statement')}")except CypherSyntaxError as e:    errors.append(e.message)# Experimental feature for correcting relationship directions  corrected_cypher = cypher_query_corrector(state.get("cypher_statement"))ifnot corrected_cypher:    errors.append("The generated Cypher statement doesn't fit the graph schema")ifnot corrected_cypher == state.get("cypher_statement"):print("Relationship direction was corrected")# Use LLM to find additional potential errors and get the mapping for values  llm_output = validate_cypher_chain.invoke({"question": state.get("question"),"schema": enhanced_graph.schema,"cypher": state.get("cypher_statement"),})if llm_output.errors:    errors.extend(llm_output.errors)if llm_output.filters:forfilterin llm_output.filters:# Do mapping only for string valuesif(not[          propfor prop in enhanced_graph.structured_schema["node_props"][filter.node_label]if prop["property"]==filter.property_key][0]["type"]=="STRING"):continue      mapping = enhanced_graph.query(f"MATCH (n:{filter.node_label}) WHERE toLower(n.`{filter.property_key}`) = toLower($value) RETURN 'yes' LIMIT 1",{"value":filter.property_value},)ifnot mapping:print(f"Missing value mapping for {filter.node_label} on property {filter.property_key} with value {filter.property_value}")        mapping_errors.append(f"Missing value mapping for {filter.node_label} on property {filter.property_key} with value {filter.property_value}")if mapping_errors:    next_action ="end"elif errors:    next_action ="correct_cypher"else:    next_action ="execute_cypher"return{"next_action": next_action,"cypher_statement": corrected_cypher,"cypher_errors": errors,"steps":["validate_cypher"],}
```

The Cypher correction step takes the existing Cypher statement, any identified errors, and the original question to generate a corrected version of the query.
```
correct_cypher_prompt = ChatPromptTemplate.from_messages([("system",("You are a Cypher expert reviewing a statement written by a junior developer. ""You need to correct the Cypher statement based on the provided errors. No pre-amble.""Do not wrap the response in any backticks or anything else. Respond with a Cypher statement only!"),),("human",("""Check for invalid syntax or semantics and return a corrected Cypher statement.Schema:{schema}Note: Do not include any explanations or apologies in your responses.Do not wrap the response in any backticks or anything else.Respond with a Cypher statement only!Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.The question is:{question}The Cypher statement is:{cypher}The errors are:{errors}Corrected Cypher statement: """),),])correct_cypher_chain = correct_cypher_prompt | llm | StrOutputParser()defcorrect_cypher(state: OverallState)-> OverallState:"""  Correct the Cypher statement based on the provided errors.  """  corrected_cypher = correct_cypher_chain.invoke({"question": state.get("question"),"errors": state.get("cypher_errors"),"cypher": state.get("cypher_statement"),"schema": enhanced_graph.schema,})return{"next_action":"validate_cypher","cypher_statement": corrected_cypher,"steps":["correct_cypher"],}
```

We need to add a step that executes the given Cypher statement. If no results are returned, we should explicitly handle this scenario, as leaving the context empty can sometimes lead to LLM hallucinations.
```
no_results ="I couldn't find any relevant information in the database"defexecute_cypher(state: OverallState)-> OverallState:"""  Executes the given Cypher statement.  """  records = enhanced_graph.query(state.get("cypher_statement"))return{"database_records": records if records else no_results,"next_action":"end","steps":["execute_cypher"],}
```

The final step is to generate the answer. This involves combining the initial question with the database output to produce a relevant response.
```
generate_final_prompt = ChatPromptTemplate.from_messages([("system","You are a helpful assistant",),("human",("""Use the following results retrieved from a database to providea succinct, definitive answer to the user's question.Respond as if you are answering the question directly.Results: {results}Question: {question}"""),),])generate_final_chain = generate_final_prompt | llm | StrOutputParser()defgenerate_final_answer(state: OverallState)-> OutputState:"""  Decides if the question is related to movies.  """  final_answer = generate_final_chain.invoke({"question": state.get("question"),"results": state.get("database_records")})return{"answer": final_answer,"steps":["generate_final_answer"]}
```

Next, we will implement the LangGraph workflow, starting with defining the conditional edge functions.
```
defguardrails_condition(  state: OverallState,)-> Literal["generate_cypher","generate_final_answer"]:if state.get("next_action")=="end":return"generate_final_answer"elif state.get("next_action")=="movie":return"generate_cypher"defvalidate_cypher_condition(  state: OverallState,)-> Literal["generate_final_answer","correct_cypher","execute_cypher"]:if state.get("next_action")=="end":return"generate_final_answer"elif state.get("next_action")=="correct_cypher":return"correct_cypher"elif state.get("next_action")=="execute_cypher":return"execute_cypher"
```

Let's put it all together now.
```
from IPython.display import Image, displayfrom langgraph.graph import END, START, StateGraphlanggraph = StateGraph(OverallState,input=InputState, output=OutputState)langgraph.add_node(guardrails)langgraph.add_node(generate_cypher)langgraph.add_node(validate_cypher)langgraph.add_node(correct_cypher)langgraph.add_node(execute_cypher)langgraph.add_node(generate_final_answer)langgraph.add_edge(START,"guardrails")langgraph.add_conditional_edges("guardrails",  guardrails_condition,)langgraph.add_edge("generate_cypher","validate_cypher")langgraph.add_conditional_edges("validate_cypher",  validate_cypher_condition,)langgraph.add_edge("execute_cypher","generate_final_answer")langgraph.add_edge("correct_cypher","validate_cypher")langgraph.add_edge("generate_final_answer", END)langgraph = langgraph.compile()# Viewdisplay(Image(langgraph.get_graph().draw_mermaid_png()))
```

**API Reference:**[StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)
![](https://python.langchain.com/docs/tutorials/graph/)
We can now test the application by asking an irrelevant question.
```
langgraph.invoke({"question":"What's the weather in Spain?"})
```

```
{'answer': "I'm sorry, but I cannot provide current weather information. Please check a reliable weather website or app for the latest updates on the weather in Spain.", 'steps': ['guardrail', 'generate_final_answer']}
```

Let's now ask something relevant about the movies.
```
langgraph.invoke({"question":"What was the cast of the Casino?"})
```

```
{'answer': 'The cast of "Casino" includes Robert De Niro, Joe Pesci, Sharon Stone, and James Woods.', 'steps': ['guardrail', 'generate_cypher', 'validate_cypher', 'execute_cypher', 'generate_final_answer'], 'cypher_statement': "MATCH (m:Movie {title: 'Casino'})<-[:ACTED_IN]-(a:Person) RETURN a.name"}
```

### Next steps[​](https://python.langchain.com/docs/tutorials/graph/#next-steps "Direct link to Next steps")
For other graph techniques like this and more check out:
  * [Semantic layer](https://python.langchain.com/docs/how_to/graph_semantic/): Techniques for implementing semantic layers.
  * [Constructing graphs](https://python.langchain.com/docs/how_to/graph_constructing/): Techniques for constructing knowledge graphs.


[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/tutorials/graph.ipynb)
#### Was this page helpful?
  * [⚠️ Security note ⚠️](https://python.langchain.com/docs/tutorials/graph/#️-security-note-️)
  * [Architecture](https://python.langchain.com/docs/tutorials/graph/#architecture)
  * [Setup](https://python.langchain.com/docs/tutorials/graph/#setup)
  * [Graph schema](https://python.langchain.com/docs/tutorials/graph/#graph-schema)
  * [GraphQACypherChain](https://python.langchain.com/docs/tutorials/graph/#graphqacypherchain)
  * [Advanced implementation with LangGraph](https://python.langchain.com/docs/tutorials/graph/#advanced-implementation-with-langgraph)
    * [Few-shot prompting](https://python.langchain.com/docs/tutorials/graph/#few-shot-prompting)
    * [Query validation](https://python.langchain.com/docs/tutorials/graph/#query-validation)
    * [Next steps](https://python.langchain.com/docs/tutorials/graph/#next-steps)


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

