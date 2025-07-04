---
url: https://python.langchain.com/docs/how_to/document_loader_custom/
scraped_at: 2025-05-25T17:54:42.711631
title: Custom Document Loader | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/how_to/document_loader_custom/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/how_to/document_loader_custom/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/how_to/document_loader_custom/)
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
    * [v0.2](https://python.langchain.com/docs/how_to/document_loader_custom/)
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
  * Custom Document Loader


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/how_to/document_loader_custom.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/document_loader_custom.ipynb)
# How to create a custom Document Loader
## Overview[​](https://python.langchain.com/docs/how_to/document_loader_custom/#overview "Direct link to Overview")
Applications based on LLMs frequently entail extracting data from databases or files, like PDFs, and converting it into a format that LLMs can utilize. In LangChain, this usually involves creating Document objects, which encapsulate the extracted text (`page_content`) along with metadata—a dictionary containing details about the document, such as the author's name or the date of publication.
`Document` objects are often formatted into prompts that are fed into an LLM, allowing the LLM to use the information in the `Document` to generate a desired response (e.g., summarizing the document). `Documents` can be either used immediately or indexed into a vectorstore for future retrieval and use.
The main abstractions for [Document Loading](https://python.langchain.com/docs/concepts/document_loaders/) are:
Component| Description  
---|---  
Document| Contains `text` and `metadata`  
BaseLoader| Use to convert raw data into `Documents`  
Blob| A representation of binary data that's located either in a file or in memory  
BaseBlobParser| Logic to parse a `Blob` to yield `Document` objects  
This guide will demonstrate how to write custom document loading and file parsing logic; specifically, we'll see how to:
  1. Create a standard document Loader by sub-classing from `BaseLoader`.
  2. Create a parser using `BaseBlobParser` and use it in conjunction with `Blob` and `BlobLoaders`. This is useful primarily when working with files.


## Standard Document Loader[​](https://python.langchain.com/docs/how_to/document_loader_custom/#standard-document-loader "Direct link to Standard Document Loader")
A document loader can be implemented by sub-classing from a `BaseLoader` which provides a standard interface for loading documents.
### Interface[​](https://python.langchain.com/docs/how_to/document_loader_custom/#interface "Direct link to Interface")
Method Name| Explanation  
---|---  
lazy_load| Used to load documents one by one **lazily**. Use for production code.  
alazy_load| Async variant of `lazy_load`  
load| Used to load all the documents into memory **eagerly**. Use for prototyping or interactive work.  
aload| Used to load all the documents into memory **eagerly**. Use for prototyping or interactive work. **Added in 2024-04 to LangChain.**  
  * The `load` methods is a convenience method meant solely for prototyping work -- it just invokes `list(self.lazy_load())`.
  * The `alazy_load` has a default implementation that will delegate to `lazy_load`. If you're using async, we recommend overriding the default implementation and providing a native async implementation.


important
When implementing a document loader do **NOT** provide parameters via the `lazy_load` or `alazy_load` methods.
All configuration is expected to be passed through the initializer (**init**). This was a design choice made by LangChain to make sure that once a document loader has been instantiated it has all the information needed to load documents.
### Installation[​](https://python.langchain.com/docs/how_to/document_loader_custom/#installation "Direct link to Installation")
Install **langchain-core** and **langchain_community**.
```
%pip install -qU langchain_core langchain_community
```

### Implementation[​](https://python.langchain.com/docs/how_to/document_loader_custom/#implementation "Direct link to Implementation")
Let's create an example of a standard document loader that loads a file and creates a document from each line in the file.
```
from typing import AsyncIterator, Iteratorfrom langchain_core.document_loaders import BaseLoaderfrom langchain_core.documents import DocumentclassCustomDocumentLoader(BaseLoader):"""An example document loader that reads a file line by line."""def__init__(self, file_path:str)->None:"""Initialize the loader with a file path.    Args:      file_path: The path to the file to load.    """    self.file_path = file_pathdeflazy_load(self)-> Iterator[Document]:# <-- Does not take any arguments"""A lazy loader that reads a file line by line.    When you're implementing lazy load methods, you should use a generator    to yield documents one by one.    """withopen(self.file_path, encoding="utf-8")as f:      line_number =0for line in f:yield Document(          page_content=line,          metadata={"line_number": line_number,"source": self.file_path},)        line_number +=1# alazy_load is OPTIONAL.# If you leave out the implementation, a default implementation which delegates to lazy_load will be used!asyncdefalazy_load(    self,)-> AsyncIterator[Document]:# <-- Does not take any arguments"""An async lazy loader that reads a file line by line."""# Requires aiofiles# https://github.com/Tinche/aiofilesimport aiofilesasyncwith aiofiles.open(self.file_path, encoding="utf-8")as f:      line_number =0asyncfor line in f:yield Document(          page_content=line,          metadata={"line_number": line_number,"source": self.file_path},)        line_number +=1
```

**API Reference:**[BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html) | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html)
### Test 🧪[​](https://python.langchain.com/docs/how_to/document_loader_custom/#test- "Direct link to Test 🧪")
To test out the document loader, we need a file with some quality content.
```
withopen("./meow.txt","w", encoding="utf-8")as f:  quality_content ="meow meow🐱 \n meow meow🐱 \n meow😻😻"  f.write(quality_content)loader = CustomDocumentLoader("./meow.txt")
```

```
%pip install -q aiofiles
```

```
## Test out the lazy load interfacefor doc in loader.lazy_load():print()print(type(doc))print(doc)
```

```
<class 'langchain_core.documents.base.Document'>page_content='meow meow🐱 ' metadata={'line_number': 0, 'source': './meow.txt'}<class 'langchain_core.documents.base.Document'>page_content=' meow meow🐱 ' metadata={'line_number': 1, 'source': './meow.txt'}<class 'langchain_core.documents.base.Document'>page_content=' meow😻😻' metadata={'line_number': 2, 'source': './meow.txt'}
```

```
## Test out the async implementationasyncfor doc in loader.alazy_load():print()print(type(doc))print(doc)
```

```
<class 'langchain_core.documents.base.Document'>page_content='meow meow🐱 ' metadata={'line_number': 0, 'source': './meow.txt'}<class 'langchain_core.documents.base.Document'>page_content=' meow meow🐱 ' metadata={'line_number': 1, 'source': './meow.txt'}<class 'langchain_core.documents.base.Document'>page_content=' meow😻😻' metadata={'line_number': 2, 'source': './meow.txt'}
```

tip
`load()` can be helpful in an interactive environment such as a jupyter notebook.
Avoid using it for production code since eager loading assumes that all the content can fit into memory, which is not always the case, especially for enterprise data.
```
loader.load()
```

```
[Document(metadata={'line_number': 0, 'source': './meow.txt'}, page_content='meow meow🐱 \n'), Document(metadata={'line_number': 1, 'source': './meow.txt'}, page_content=' meow meow🐱 \n'), Document(metadata={'line_number': 2, 'source': './meow.txt'}, page_content=' meow😻😻')]
```

## Working with Files[​](https://python.langchain.com/docs/how_to/document_loader_custom/#working-with-files "Direct link to Working with Files")
Many document loaders involve parsing files. The difference between such loaders usually stems from how the file is parsed, rather than how the file is loaded. For example, you can use `open` to read the binary content of either a PDF or a markdown file, but you need different parsing logic to convert that binary data into text.
As a result, it can be helpful to decouple the parsing logic from the loading logic, which makes it easier to re-use a given parser regardless of how the data was loaded.
### BaseBlobParser[​](https://python.langchain.com/docs/how_to/document_loader_custom/#baseblobparser "Direct link to BaseBlobParser")
A `BaseBlobParser` is an interface that accepts a `blob` and outputs a list of `Document` objects. A `blob` is a representation of data that lives either in memory or in a file. LangChain python has a `Blob` primitive which is inspired by the [Blob WebAPI spec](https://developer.mozilla.org/en-US/docs/Web/API/Blob).
```
from langchain_core.document_loaders import BaseBlobParser, BlobclassMyParser(BaseBlobParser):"""A simple parser that creates a document from each line."""deflazy_parse(self, blob: Blob)-> Iterator[Document]:"""Parse a blob into a document line by line."""    line_number =0with blob.as_bytes_io()as f:for line in f:        line_number +=1yield Document(          page_content=line,          metadata={"line_number": line_number,"source": blob.source},)
```

**API Reference:**[BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html) | [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html)
```
blob = Blob.from_path("./meow.txt")parser = MyParser()
```

```
list(parser.lazy_parse(blob))
```

```
[Document(metadata={'line_number': 1, 'source': './meow.txt'}, page_content='meow meow🐱 \n'), Document(metadata={'line_number': 2, 'source': './meow.txt'}, page_content=' meow meow🐱 \n'), Document(metadata={'line_number': 3, 'source': './meow.txt'}, page_content=' meow😻😻')]
```

Using the **blob** API also allows one to load content directly from memory without having to read it from a file!
```
blob = Blob(data=b"some data from memory\nmeow")list(parser.lazy_parse(blob))
```

```
[Document(metadata={'line_number': 1, 'source': None}, page_content='some data from memory\n'), Document(metadata={'line_number': 2, 'source': None}, page_content='meow')]
```

### Blob[​](https://python.langchain.com/docs/how_to/document_loader_custom/#blob "Direct link to Blob")
Let's take a quick look through some of the Blob API.
```
blob = Blob.from_path("./meow.txt", metadata={"foo":"bar"})
```

```
blob.encoding
```

```
'utf-8'
```

```
blob.as_bytes()
```

```
b'meow meow\xf0\x9f\x90\xb1 \n meow meow\xf0\x9f\x90\xb1 \n meow\xf0\x9f\x98\xbb\xf0\x9f\x98\xbb'
```

```
blob.as_string()
```

```
'meow meow🐱 \n meow meow🐱 \n meow😻😻'
```

```
blob.as_bytes_io()
```

```
<contextlib._GeneratorContextManager at 0x74b8d42e9940>
```

```
blob.metadata
```

```
{'foo': 'bar'}
```

```
blob.source
```

```
'./meow.txt'
```

### Blob Loaders[​](https://python.langchain.com/docs/how_to/document_loader_custom/#blob-loaders "Direct link to Blob Loaders")
While a parser encapsulates the logic needed to parse binary data into documents, _blob loaders_ encapsulate the logic that's necessary to load blobs from a given storage location.
At the moment, `LangChain` supports `FileSystemBlobLoader` and `CloudBlobLoader`.
You can use the `FileSystemBlobLoader` to load blobs and then use the parser to parse them.
```
from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoaderfilesystem_blob_loader = FileSystemBlobLoader(  path=".", glob="*.mdx", show_progress=True)
```

**API Reference:**[FileSystemBlobLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blob_loaders.file_system.FileSystemBlobLoader.html)
```
%pip install -q tqdm
```

```
parser = MyParser()for blob in filesystem_blob_loader.yield_blobs():for doc in parser.lazy_parse(blob):print(doc)break
```

Or, you can use `CloudBlobLoader` to load blobs from a cloud storage location (Supports s3://, az://, gs://, file:// schemes).
```
%pip install -q 'cloudpathlib[s3]'
```

```
from cloudpathlib import S3Client, S3Pathfrom langchain_community.document_loaders.blob_loaders import CloudBlobLoaderclient = S3Client(no_sign_request=True)client.set_as_default_client()path = S3Path("s3://bucket-01", client=client)# Supports s3://, az://, gs://, file:// schemes.cloud_loader = CloudBlobLoader(path, glob="**/*.pdf", show_progress=True)for blob in cloud_loader.yield_blobs():print(blob)
```

**API Reference:**[CloudBlobLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blob_loaders.cloud_blob_loader.CloudBlobLoader.html)
### Generic Loader[​](https://python.langchain.com/docs/how_to/document_loader_custom/#generic-loader "Direct link to Generic Loader")
LangChain has a `GenericLoader` abstraction which composes a `BlobLoader` with a `BaseBlobParser`.
`GenericLoader` is meant to provide standardized classmethods that make it easy to use existing `BlobLoader` implementations. At the moment, the `FileSystemBlobLoader` and `CloudBlobLoader` are supported. See example below:
```
from langchain_community.document_loaders.generic import GenericLoadergeneric_loader_filesystem = GenericLoader(  blob_loader=filesystem_blob_loader, blob_parser=parser)for idx, doc inenumerate(generic_loader_filesystem.lazy_load()):if idx <5:print(doc)print("... output truncated for demo purposes")
```

**API Reference:**[GenericLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.generic.GenericLoader.html)
```
100%|██████████| 7/7 [00:00<00:00, 1224.82it/s]``````outputpage_content='# Text embedding models' metadata={'line_number': 1, 'source': 'embed_text.mdx'}page_content='' metadata={'line_number': 2, 'source': 'embed_text.mdx'}page_content=':::info' metadata={'line_number': 3, 'source': 'embed_text.mdx'}page_content='Head to [Integrations](/docs/integrations/text_embedding/) for documentation on built-in integrations with text embedding model providers.' metadata={'line_number': 4, 'source': 'embed_text.mdx'}page_content=':::' metadata={'line_number': 5, 'source': 'embed_text.mdx'}... output truncated for demo purposes
```

#### Custom Generic Loader[​](https://python.langchain.com/docs/how_to/document_loader_custom/#custom-generic-loader "Direct link to Custom Generic Loader")
If you really like creating classes, you can sub-class and create a class to encapsulate the logic together.
You can sub-class from this class to load content using an existing loader.
```
from typing import AnyclassMyCustomLoader(GenericLoader):@staticmethoddefget_parser(**kwargs: Any)-> BaseBlobParser:"""Override this method to associate a default parser with the class."""return MyParser()
```

```
loader = MyCustomLoader.from_filesystem(path=".", glob="*.mdx", show_progress=True)for idx, doc inenumerate(loader.lazy_load()):if idx <5:print(doc)print("... output truncated for demo purposes")
```

```
100%|██████████| 7/7 [00:00<00:00, 814.86it/s]``````outputpage_content='# Text embedding models' metadata={'line_number': 1, 'source': 'embed_text.mdx'}page_content='' metadata={'line_number': 2, 'source': 'embed_text.mdx'}page_content=':::info' metadata={'line_number': 3, 'source': 'embed_text.mdx'}page_content='Head to [Integrations](/docs/integrations/text_embedding/) for documentation on built-in integrations with text embedding model providers.' metadata={'line_number': 4, 'source': 'embed_text.mdx'}page_content=':::' metadata={'line_number': 5, 'source': 'embed_text.mdx'}... output truncated for demo purposes
```

[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/how_to/document_loader_custom.ipynb)
#### Was this page helpful?
  * [Overview](https://python.langchain.com/docs/how_to/document_loader_custom/#overview)
  * [Standard Document Loader](https://python.langchain.com/docs/how_to/document_loader_custom/#standard-document-loader)
    * [Interface](https://python.langchain.com/docs/how_to/document_loader_custom/#interface)
    * [Installation](https://python.langchain.com/docs/how_to/document_loader_custom/#installation)
    * [Implementation](https://python.langchain.com/docs/how_to/document_loader_custom/#implementation)
    * [Test 🧪](https://python.langchain.com/docs/how_to/document_loader_custom/#test-)
  * [Working with Files](https://python.langchain.com/docs/how_to/document_loader_custom/#working-with-files)
    * [BaseBlobParser](https://python.langchain.com/docs/how_to/document_loader_custom/#baseblobparser)
    * [Blob](https://python.langchain.com/docs/how_to/document_loader_custom/#blob)
    * [Blob Loaders](https://python.langchain.com/docs/how_to/document_loader_custom/#blob-loaders)
    * [Generic Loader](https://python.langchain.com/docs/how_to/document_loader_custom/#generic-loader)


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

