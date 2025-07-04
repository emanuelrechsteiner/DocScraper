---
url: https://python.langchain.com/docs/how_to/sql_prompting/
scraped_at: 2025-05-25T17:54:53.411213
title: How to better prompt when doing SQL question-answering | 🦜️🔗 LangChain
---

[Skip to main content](https://python.langchain.com/docs/how_to/sql_prompting/#__docusaurus_skipToContent_fallback)
**We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith.[ Join our team!](https://www.langchain.com/careers)**
[![🦜️🔗 LangChain](https://python.langchain.com/img/brand/wordmark.png)](https://python.langchain.com/)[Integrations](https://python.langchain.com/docs/integrations/providers/)[API Reference](https://python.langchain.com/api_reference/)
[More](https://python.langchain.com/docs/how_to/sql_prompting/)
  * [Contributing](https://python.langchain.com/docs/contributing/)
  * [People](https://python.langchain.com/docs/people/)
  * [Error reference](https://python.langchain.com/docs/troubleshooting/errors/)
  * [LangSmith](https://docs.smith.langchain.com)
  * [LangGraph](https://langchain-ai.github.io/langgraph/)
  * [LangChain Hub](https://smith.langchain.com/hub)
  * [LangChain JS/TS](https://js.langchain.com)


[v0.3](https://python.langchain.com/docs/how_to/sql_prompting/)
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
    * [v0.2](https://python.langchain.com/docs/how_to/sql_prompting/)
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
  * How to better prompt when doing SQL question-answering


On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/how_to/sql_prompting.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/sql_prompting.ipynb)
# How to better prompt when doing SQL question-answering
In this guide we'll go over prompting strategies to improve SQL query generation using [create_sql_query_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.create_sql_query_chain.html). We'll largely focus on methods for getting relevant database-specific information in your prompt.
We will cover:
  * How the dialect of the LangChain [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html) impacts the prompt of the chain;
  * How to format schema information into the prompt using `SQLDatabase.get_context`;
  * How to build and select [few-shot examples](https://python.langchain.com/docs/concepts/few_shot_prompting/) to assist the model.


## Setup[​](https://python.langchain.com/docs/how_to/sql_prompting/#setup "Direct link to Setup")
First, get required packages and set environment variables:
```
%pip install --upgrade --quiet langchain langchain-community langchain-experimental langchain-openai
```

```
# Uncomment the below to use LangSmith. Not required.# import os# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()# os.environ["LANGSMITH_TRACING"] = "true"
```

The below example will use a SQLite connection with Chinook database. Follow [these installation steps](https://database.guide/2-sample-databases-sqlite/) to create `Chinook.db` in the same directory as this notebook:
  * Save [this file](https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql) as `Chinook_Sqlite.sql`
  * Run `sqlite3 Chinook.db`
  * Run `.read Chinook_Sqlite.sql`
  * Test `SELECT * FROM Artist LIMIT 10;`


Now, `Chinook.db` is in our directory and we can interface with it using the SQLAlchemy-driven `SQLDatabase` class:
```
from langchain_community.utilities import SQLDatabasedb = SQLDatabase.from_uri("sqlite:///Chinook.db", sample_rows_in_table_info=3)print(db.dialect)print(db.get_usable_table_names())print(db.run("SELECT * FROM Artist LIMIT 10;"))
```

**API Reference:**[SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html)
```
sqlite['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track'][(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]
```

## Dialect-specific prompting[​](https://python.langchain.com/docs/how_to/sql_prompting/#dialect-specific-prompting "Direct link to Dialect-specific prompting")
One of the simplest things we can do is make our prompt specific to the SQL dialect we're using. When using the built-in [create_sql_query_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.create_sql_query_chain.html) and [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html), this is handled for you for any of the following dialects:
```
from langchain.chains.sql_database.prompt import SQL_PROMPTSlist(SQL_PROMPTS)
```

```
['crate', 'duckdb', 'googlesql', 'mssql', 'mysql', 'mariadb', 'oracle', 'postgresql', 'sqlite', 'clickhouse', 'prestodb']
```

For example, using our current DB we can see that we'll get a SQLite-specific prompt.
Select [chat model](https://python.langchain.com/docs/integrations/chat/):
OpenAI▾
* [OpenAI](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Anthropic](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Azure](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Google Gemini](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Google Vertex](https://python.langchain.com/docs/how_to/sql_prompting/)
* [AWS](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Groq](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Cohere](https://python.langchain.com/docs/how_to/sql_prompting/)
* [NVIDIA](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Fireworks AI](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Mistral AI](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Together AI](https://python.langchain.com/docs/how_to/sql_prompting/)
* [IBM watsonx](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Databricks](https://python.langchain.com/docs/how_to/sql_prompting/)
* [xAI](https://python.langchain.com/docs/how_to/sql_prompting/)
* [Perplexity](https://python.langchain.com/docs/how_to/sql_prompting/)
```
pip install -qU "langchain[openai]"
```

```
import getpassimport osifnot os.environ.get("OPENAI_API_KEY"): os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter API key for OpenAI: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("gpt-4o-mini", model_provider="openai")
```

```
from langchain.chains import create_sql_query_chainchain = create_sql_query_chain(llm, db)chain.get_prompts()[0].pretty_print()
```

**API Reference:**[create_sql_query_chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.create_sql_query_chain.html)
```
You are a SQLite expert. Given an input question, first create a syntactically correct SQLite query to run, then look at the results of the query and return the answer to the input question.Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per SQLite. You can order the results to return the most informative data in the database.Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.Pay attention to use date('now') function to get the current date, if the question involves "today".Use the following format:Question: Question hereSQLQuery: SQL Query to runSQLResult: Result of the SQLQueryAnswer: Final answer hereOnly use the following tables:[33;1m[1;3m{table_info}[0mQuestion: [33;1m[1;3m{input}[0m
```

## Table definitions and example rows[​](https://python.langchain.com/docs/how_to/sql_prompting/#table-definitions-and-example-rows "Direct link to Table definitions and example rows")
In most SQL chains, we'll need to feed the model at least part of the database schema. Without this it won't be able to write valid queries. Our database comes with some convenience methods to give us the relevant context. Specifically, we can get the table names, their schemas, and a sample of rows from each table.
Here we will use `SQLDatabase.get_context`, which provides available tables and their schemas:
```
context = db.get_context()print(list(context))print(context["table_info"])
```

```
['table_info', 'table_names']CREATE TABLE "Album" (	"AlbumId" INTEGER NOT NULL, 	"Title" NVARCHAR(160) NOT NULL, 	"ArtistId" INTEGER NOT NULL, 	PRIMARY KEY ("AlbumId"), 	FOREIGN KEY("ArtistId") REFERENCES "Artist" ("ArtistId"))/*3 rows from Album table:AlbumId	Title	ArtistId1	For Those About To Rock We Salute You	12	Balls to the Wall	23	Restless and Wild	2*/CREATE TABLE "Artist" (	"ArtistId" INTEGER NOT NULL, 	"Name" NVARCHAR(120), 	PRIMARY KEY ("ArtistId"))/*3 rows from Artist table:ArtistId	Name1	AC/DC2	Accept3	Aerosmith*/CREATE TABLE "Customer" (	"CustomerId" INTEGER NOT NULL, 	"FirstName" NVARCHAR(40) NOT NULL, 	"LastName" NVARCHAR(20) NOT NULL, 	"Company" NVARCHAR(80), 	"Address" NVARCHAR(70), 	"City" NVARCHAR(40), 	"State" NVARCHAR(40), 	"Country" NVARCHAR(40), 	"PostalCode" NVARCHAR(10), 	"Phone" NVARCHAR(24), 	"Fax" NVARCHAR(24), 	"Email" NVARCHAR(60) NOT NULL, 	"SupportRepId" INTEGER, 	PRIMARY KEY ("CustomerId"), 	FOREIGN KEY("SupportRepId") REFERENCES "Employee" ("EmployeeId"))/*3 rows from Customer table:CustomerId	FirstName	LastName	Company	Address	City	State	Country	PostalCode	Phone	Fax	Email	SupportRepId1	Luís	Gonçalves	Embraer - Empresa Brasileira de Aeronáutica S.A.	Av. Brigadeiro Faria Lima, 2170	São José dos Campos	SP	Brazil	12227-000	+55 (12) 3923-5555	+55 (12) 3923-5566	luisg@embraer.com.br	32	Leonie	Köhler	None	Theodor-Heuss-Straße 34	Stuttgart	None	Germany	70174	+49 0711 2842222	None	leonekohler@surfeu.de	53	François	Tremblay	None	1498 rue Bélanger	Montréal	QC	Canada	H2G 1A7	+1 (514) 721-4711	None	ftremblay@gmail.com	3*/CREATE TABLE "Employee" (	"EmployeeId" INTEGER NOT NULL, 	"LastName" NVARCHAR(20) NOT NULL, 	"FirstName" NVARCHAR(20) NOT NULL, 	"Title" NVARCHAR(30), 	"ReportsTo" INTEGER, 	"BirthDate" DATETIME, 	"HireDate" DATETIME, 	"Address" NVARCHAR(70), 	"City" NVARCHAR(40), 	"State" NVARCHAR(40), 	"Country" NVARCHAR(40), 	"PostalCode" NVARCHAR(10), 	"Phone" NVARCHAR(24), 	"Fax" NVARCHAR(24), 	"Email" NVARCHAR(60), 	PRIMARY KEY ("EmployeeId"), 	FOREIGN KEY("ReportsTo") REFERENCES "Employee" ("EmployeeId"))/*3 rows from Employee table:EmployeeId	LastName	FirstName	Title	ReportsTo	BirthDate	HireDate	Address	City	State	Country	PostalCode	Phone	Fax	Email1	Adams	Andrew	General Manager	None	1962-02-18 00:00:00	2002-08-14 00:00:00	11120 Jasper Ave NW	Edmonton	AB	Canada	T5K 2N1	+1 (780) 428-9482	+1 (780) 428-3457	andrew@chinookcorp.com2	Edwards	Nancy	Sales Manager	1	1958-12-08 00:00:00	2002-05-01 00:00:00	825 8 Ave SW	Calgary	AB	Canada	T2P 2T3	+1 (403) 262-3443	+1 (403) 262-3322	nancy@chinookcorp.com3	Peacock	Jane	Sales Support Agent	2	1973-08-29 00:00:00	2002-04-01 00:00:00	1111 6 Ave SW	Calgary	AB	Canada	T2P 5M5	+1 (403) 262-3443	+1 (403) 262-6712	jane@chinookcorp.com*/CREATE TABLE "Genre" (	"GenreId" INTEGER NOT NULL, 	"Name" NVARCHAR(120), 	PRIMARY KEY ("GenreId"))/*3 rows from Genre table:GenreId	Name1	Rock2	Jazz3	Metal*/CREATE TABLE "Invoice" (	"InvoiceId" INTEGER NOT NULL, 	"CustomerId" INTEGER NOT NULL, 	"InvoiceDate" DATETIME NOT NULL, 	"BillingAddress" NVARCHAR(70), 	"BillingCity" NVARCHAR(40), 	"BillingState" NVARCHAR(40), 	"BillingCountry" NVARCHAR(40), 	"BillingPostalCode" NVARCHAR(10), 	"Total" NUMERIC(10, 2) NOT NULL, 	PRIMARY KEY ("InvoiceId"), 	FOREIGN KEY("CustomerId") REFERENCES "Customer" ("CustomerId"))/*3 rows from Invoice table:InvoiceId	CustomerId	InvoiceDate	BillingAddress	BillingCity	BillingState	BillingCountry	BillingPostalCode	Total1	2	2021-01-01 00:00:00	Theodor-Heuss-Straße 34	Stuttgart	None	Germany	70174	1.982	4	2021-01-02 00:00:00	Ullevålsveien 14	Oslo	None	Norway	0171	3.963	8	2021-01-03 00:00:00	Grétrystraat 63	Brussels	None	Belgium	1000	5.94*/CREATE TABLE "InvoiceLine" (	"InvoiceLineId" INTEGER NOT NULL, 	"InvoiceId" INTEGER NOT NULL, 	"TrackId" INTEGER NOT NULL, 	"UnitPrice" NUMERIC(10, 2) NOT NULL, 	"Quantity" INTEGER NOT NULL, 	PRIMARY KEY ("InvoiceLineId"), 	FOREIGN KEY("TrackId") REFERENCES "Track" ("TrackId"), 	FOREIGN KEY("InvoiceId") REFERENCES "Invoice" ("InvoiceId"))/*3 rows from InvoiceLine table:InvoiceLineId	InvoiceId	TrackId	UnitPrice	Quantity1	1	2	0.99	12	1	4	0.99	13	2	6	0.99	1*/CREATE TABLE "MediaType" (	"MediaTypeId" INTEGER NOT NULL, 	"Name" NVARCHAR(120), 	PRIMARY KEY ("MediaTypeId"))/*3 rows from MediaType table:MediaTypeId	Name1	MPEG audio file2	Protected AAC audio file3	Protected MPEG-4 video file*/CREATE TABLE "Playlist" (	"PlaylistId" INTEGER NOT NULL, 	"Name" NVARCHAR(120), 	PRIMARY KEY ("PlaylistId"))/*3 rows from Playlist table:PlaylistId	Name1	Music2	Movies3	TV Shows*/CREATE TABLE "PlaylistTrack" (	"PlaylistId" INTEGER NOT NULL, 	"TrackId" INTEGER NOT NULL, 	PRIMARY KEY ("PlaylistId", "TrackId"), 	FOREIGN KEY("TrackId") REFERENCES "Track" ("TrackId"), 	FOREIGN KEY("PlaylistId") REFERENCES "Playlist" ("PlaylistId"))/*3 rows from PlaylistTrack table:PlaylistId	TrackId1	34021	33891	3390*/CREATE TABLE "Track" (	"TrackId" INTEGER NOT NULL, 	"Name" NVARCHAR(200) NOT NULL, 	"AlbumId" INTEGER, 	"MediaTypeId" INTEGER NOT NULL, 	"GenreId" INTEGER, 	"Composer" NVARCHAR(220), 	"Milliseconds" INTEGER NOT NULL, 	"Bytes" INTEGER, 	"UnitPrice" NUMERIC(10, 2) NOT NULL, 	PRIMARY KEY ("TrackId"), 	FOREIGN KEY("MediaTypeId") REFERENCES "MediaType" ("MediaTypeId"), 	FOREIGN KEY("GenreId") REFERENCES "Genre" ("GenreId"), 	FOREIGN KEY("AlbumId") REFERENCES "Album" ("AlbumId"))/*3 rows from Track table:TrackId	Name	AlbumId	MediaTypeId	GenreId	Composer	Milliseconds	Bytes	UnitPrice1	For Those About To Rock (We Salute You)	1	1	1	Angus Young, Malcolm Young, Brian Johnson	343719	11170334	0.992	Balls to the Wall	2	2	1	U. Dirkschneider, W. Hoffmann, H. Frank, P. Baltes, S. Kaufmann, G. Hoffmann	342562	5510424	0.993	Fast As a Shark	3	2	1	F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman	230619	3990994	0.99*/
```

When we don't have too many, or too wide of, tables, we can just insert the entirety of this information in our prompt:
```
prompt_with_context = chain.get_prompts()[0].partial(table_info=context["table_info"])print(prompt_with_context.pretty_repr()[:1500])
```

```
You are a SQLite expert. Given an input question, first create a syntactically correct SQLite query to run, then look at the results of the query and return the answer to the input question.Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per SQLite. You can order the results to return the most informative data in the database.Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.Pay attention to use date('now') function to get the current date, if the question involves "today".Use the following format:Question: Question hereSQLQuery: SQL Query to runSQLResult: Result of the SQLQueryAnswer: Final answer hereOnly use the following tables:CREATE TABLE "Album" (	"AlbumId" INTEGER NOT NULL, 	"Title" NVARCHAR(160) NOT NULL, 	"ArtistId" INTEGER NOT NULL, 	PRIMARY KEY ("AlbumId"), 	FOREIGN KEY("ArtistId") REFERENCES "Artist" ("ArtistId"))/*3 rows from Album table:AlbumId	Title	ArtistId1	For Those About To Rock We Salute You	12	Balls to the Wall	23	Restless and Wild	2*/CREATE TABLE "Artist" (	"ArtistId" INTEGER NOT NULL, 	"Name" NVARCHAR(120)
```

When we do have database schemas that are too large to fit into our model's context window, we'll need to come up with ways of inserting only the relevant table definitions into the prompt based on the user input. For more on this head to the [Many tables, wide tables, high-cardinality feature](https://python.langchain.com/docs/how_to/sql_large_db/) guide.
## Few-shot examples[​](https://python.langchain.com/docs/how_to/sql_prompting/#few-shot-examples "Direct link to Few-shot examples")
Including examples of natural language questions being converted to valid SQL queries against our database in the prompt will often improve model performance, especially for complex queries.
Let's say we have the following examples:
```
examples =[{"input":"List all artists.","query":"SELECT * FROM Artist;"},{"input":"Find all albums for the artist 'AC/DC'.","query":"SELECT * FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'AC/DC');",},{"input":"List all tracks in the 'Rock' genre.","query":"SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');",},{"input":"Find the total duration of all tracks.","query":"SELECT SUM(Milliseconds) FROM Track;",},{"input":"List all customers from Canada.","query":"SELECT * FROM Customer WHERE Country = 'Canada';",},{"input":"How many tracks are there in the album with ID 5?","query":"SELECT COUNT(*) FROM Track WHERE AlbumId = 5;",},{"input":"Find the total number of invoices.","query":"SELECT COUNT(*) FROM Invoice;",},{"input":"List all tracks that are longer than 5 minutes.","query":"SELECT * FROM Track WHERE Milliseconds > 300000;",},{"input":"Who are the top 5 customers by total purchase?","query":"SELECT CustomerId, SUM(Total) AS TotalPurchase FROM Invoice GROUP BY CustomerId ORDER BY TotalPurchase DESC LIMIT 5;",},{"input":"Which albums are from the year 2000?","query":"SELECT * FROM Album WHERE strftime('%Y', ReleaseDate) = '2000';",},{"input":"How many employees are there","query":'SELECT COUNT(*) FROM "Employee"',},]
```

We can create a few-shot prompt with them like so:
```
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplateexample_prompt = PromptTemplate.from_template("User input: {input}\nSQL query: {query}")prompt = FewShotPromptTemplate(  examples=examples[:5],  example_prompt=example_prompt,  prefix="You are a SQLite expert. Given an input question, create a syntactically correct SQLite query to run. Unless otherwise specificed, do not return more than {top_k} rows.\n\nHere is the relevant table info: {table_info}\n\nBelow are a number of examples of questions and their corresponding SQL queries.",  suffix="User input: {input}\nSQL query: ",  input_variables=["input","top_k","table_info"],)
```

**API Reference:**[FewShotPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.few_shot.FewShotPromptTemplate.html) | [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html)
```
print(prompt.format(input="How many artists are there?", top_k=3, table_info="foo"))
```

```
You are a SQLite expert. Given an input question, create a syntactically correct SQLite query to run. Unless otherwise specificed, do not return more than 3 rows.Here is the relevant table info: fooBelow are a number of examples of questions and their corresponding SQL queries.User input: List all artists.SQL query: SELECT * FROM Artist;User input: Find all albums for the artist 'AC/DC'.SQL query: SELECT * FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'AC/DC');User input: List all tracks in the 'Rock' genre.SQL query: SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');User input: Find the total duration of all tracks.SQL query: SELECT SUM(Milliseconds) FROM Track;User input: List all customers from Canada.SQL query: SELECT * FROM Customer WHERE Country = 'Canada';User input: How many artists are there?SQL query:
```

## Dynamic few-shot examples[​](https://python.langchain.com/docs/how_to/sql_prompting/#dynamic-few-shot-examples "Direct link to Dynamic few-shot examples")
If we have enough examples, we may want to only include the most relevant ones in the prompt, either because they don't fit in the model's context window or because the long tail of examples distracts the model. And specifically, given any input we want to include the examples most relevant to that input.
We can do just this using an ExampleSelector. In this case we'll use a [SemanticSimilarityExampleSelector](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector.html), which will store the examples in the vector database of our choosing. At runtime it will perform a similarity search between the input and our examples, and return the most semantically similar ones.
We default to OpenAI embeddings here, but you can swap them out for the model provider of your choice.
```
from langchain_community.vectorstores import FAISSfrom langchain_core.example_selectors import SemanticSimilarityExampleSelectorfrom langchain_openai import OpenAIEmbeddingsexample_selector = SemanticSimilarityExampleSelector.from_examples(  examples,  OpenAIEmbeddings(),  FAISS,  k=5,  input_keys=["input"],)
```

**API Reference:**[FAISS](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.faiss.FAISS.html) | [SemanticSimilarityExampleSelector](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)
```
example_selector.select_examples({"input":"how many artists are there?"})
```

```
[{'input': 'List all artists.', 'query': 'SELECT * FROM Artist;'}, {'input': 'How many employees are there', 'query': 'SELECT COUNT(*) FROM "Employee"'}, {'input': 'How many tracks are there in the album with ID 5?', 'query': 'SELECT COUNT(*) FROM Track WHERE AlbumId = 5;'}, {'input': 'Which albums are from the year 2000?', 'query': "SELECT * FROM Album WHERE strftime('%Y', ReleaseDate) = '2000';"}, {'input': "List all tracks in the 'Rock' genre.", 'query': "SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');"}]
```

To use it, we can pass the ExampleSelector directly in to our FewShotPromptTemplate:
```
prompt = FewShotPromptTemplate(  example_selector=example_selector,  example_prompt=example_prompt,  prefix="You are a SQLite expert. Given an input question, create a syntactically correct SQLite query to run. Unless otherwise specificed, do not return more than {top_k} rows.\n\nHere is the relevant table info: {table_info}\n\nBelow are a number of examples of questions and their corresponding SQL queries.",  suffix="User input: {input}\nSQL query: ",  input_variables=["input","top_k","table_info"],)
```

```
print(prompt.format(input="how many artists are there?", top_k=3, table_info="foo"))
```

```
You are a SQLite expert. Given an input question, create a syntactically correct SQLite query to run. Unless otherwise specificed, do not return more than 3 rows.Here is the relevant table info: fooBelow are a number of examples of questions and their corresponding SQL queries.User input: List all artists.SQL query: SELECT * FROM Artist;User input: How many employees are thereSQL query: SELECT COUNT(*) FROM "Employee"User input: How many tracks are there in the album with ID 5?SQL query: SELECT COUNT(*) FROM Track WHERE AlbumId = 5;User input: Which albums are from the year 2000?SQL query: SELECT * FROM Album WHERE strftime('%Y', ReleaseDate) = '2000';User input: List all tracks in the 'Rock' genre.SQL query: SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');User input: how many artists are there?SQL query:
```

Trying it out, we see that the model identifies the relevant table:
```
chain = create_sql_query_chain(llm, db, prompt)chain.invoke({"question":"how many artists are there?"})
```

```
'SELECT COUNT(*) FROM Artist;'
```

[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/how_to/sql_prompting.ipynb)
#### Was this page helpful?
  * [Setup](https://python.langchain.com/docs/how_to/sql_prompting/#setup)
  * [Dialect-specific prompting](https://python.langchain.com/docs/how_to/sql_prompting/#dialect-specific-prompting)
  * [Table definitions and example rows](https://python.langchain.com/docs/how_to/sql_prompting/#table-definitions-and-example-rows)
  * [Few-shot examples](https://python.langchain.com/docs/how_to/sql_prompting/#few-shot-examples)
  * [Dynamic few-shot examples](https://python.langchain.com/docs/how_to/sql_prompting/#dynamic-few-shot-examples)


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

