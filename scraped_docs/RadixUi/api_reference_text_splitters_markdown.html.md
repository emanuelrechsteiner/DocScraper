---
url: https://python.langchain.com/api_reference/text_splitters/markdown.html
scraped_at: 2025-05-25T18:13:45.104545
title: markdown — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/text_splitters/markdown.html#main-content)
Back to top `⌘`+`K`
[ ![🦜🔗 LangChain documentation - Home](https://python.langchain.com/api_reference/_static/wordmark-api.svg) ![🦜🔗 LangChain documentation - Home](https://python.langchain.com/api_reference/_static/wordmark-api-dark.svg) ](https://python.langchain.com/api_reference/index.html)
  * [ Reference ](https://python.langchain.com/api_reference/reference.html)


`⌘`+`K`
[Docs](https://python.langchain.com/)
Light Dark System Settings
  * [ GitHub](https://github.com/langchain-ai/langchain)
  * [ X / Twitter](https://twitter.com/langchainai)


`⌘`+`K`
  * [ Reference ](https://python.langchain.com/api_reference/reference.html)


[Docs](https://python.langchain.com/)
Light Dark System Settings
  * [ GitHub](https://github.com/langchain-ai/langchain)
  * [ X / Twitter](https://twitter.com/langchainai)


Section Navigation
Base packages
  * [Core](https://python.langchain.com/api_reference/core/index.html)
  * [Langchain](https://python.langchain.com/api_reference/langchain/index.html)
  * [Text Splitters](https://python.langchain.com/api_reference/text_splitters/index.html)
    * [`base`](https://python.langchain.com/api_reference/text_splitters/base.html)
    * [`character`](https://python.langchain.com/api_reference/text_splitters/character.html)
    * [`html`](https://python.langchain.com/api_reference/text_splitters/html.html)
    * [`json`](https://python.langchain.com/api_reference/text_splitters/json.html)
    * [`jsx`](https://python.langchain.com/api_reference/text_splitters/jsx.html)
    * [`konlpy`](https://python.langchain.com/api_reference/text_splitters/konlpy.html)
    * [`latex`](https://python.langchain.com/api_reference/text_splitters/latex.html)
    * [`markdown`](https://python.langchain.com/api_reference/text_splitters/markdown.html)
      * [ExperimentalMarkdownSyntaxTextSplitter](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter.html)
      * [HeaderType](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.HeaderType.html)
      * [LineType](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.LineType.html)
      * [MarkdownHeaderTextSplitter](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.MarkdownHeaderTextSplitter.html)
      * [MarkdownTextSplitter](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.MarkdownTextSplitter.html)
    * [`nltk`](https://python.langchain.com/api_reference/text_splitters/nltk.html)
    * [`python`](https://python.langchain.com/api_reference/text_splitters/python.html)
    * [`sentence_transformers`](https://python.langchain.com/api_reference/text_splitters/sentence_transformers.html)
    * [`spacy`](https://python.langchain.com/api_reference/text_splitters/spacy.html)
  * [Community](https://python.langchain.com/api_reference/community/index.html)
  * [Experimental](https://python.langchain.com/api_reference/experimental/index.html)


Integrations
  * [AI21](https://python.langchain.com/api_reference/ai21/index.html)
  * [Anthropic](https://python.langchain.com/api_reference/anthropic/index.html)
  * [AstraDB](https://python.langchain.com/api_reference/astradb/index.html)
  * [AWS](https://python.langchain.com/api_reference/aws/index.html)
  * [Azure Ai](https://python.langchain.com/api_reference/azure_ai/index.html)
  * [Azure Dynamic Sessions](https://python.langchain.com/api_reference/azure_dynamic_sessions/index.html)
  * [Cerebras](https://python.langchain.com/api_reference/cerebras/index.html)
  * [Chroma](https://python.langchain.com/api_reference/chroma/index.html)
  * [Cohere](https://python.langchain.com/api_reference/cohere/index.html)
  * [Deepseek](https://python.langchain.com/api_reference/deepseek/index.html)
  * [Elasticsearch](https://python.langchain.com/api_reference/elasticsearch/index.html)
  * [Exa](https://python.langchain.com/api_reference/exa/index.html)
  * [Fireworks](https://python.langchain.com/api_reference/fireworks/index.html)
  * [Google Community](https://python.langchain.com/api_reference/google_community/index.html)
  * [Google GenAI](https://python.langchain.com/api_reference/google_genai/index.html)
  * [Google VertexAI](https://python.langchain.com/api_reference/google_vertexai/index.html)
  * [Groq](https://python.langchain.com/api_reference/groq/index.html)
  * [Huggingface](https://python.langchain.com/api_reference/huggingface/index.html)
  * [IBM](https://python.langchain.com/api_reference/ibm/index.html)
  * [Milvus](https://python.langchain.com/api_reference/milvus/index.html)
  * [MistralAI](https://python.langchain.com/api_reference/mistralai/index.html)
  * [MongoDB](https://python.langchain.com/api_reference/mongodb/index.html)
  * [Neo4J](https://python.langchain.com/api_reference/neo4j/index.html)
  * [Nomic](https://python.langchain.com/api_reference/nomic/index.html)
  * [Nvidia Ai Endpoints](https://python.langchain.com/api_reference/nvidia_ai_endpoints/index.html)
  * [Ollama](https://python.langchain.com/api_reference/ollama/index.html)
  * [OpenAI](https://python.langchain.com/api_reference/openai/index.html)
  * [Perplexity](https://python.langchain.com/api_reference/perplexity/index.html)
  * [Pinecone](https://python.langchain.com/api_reference/pinecone/index.html)
  * [Postgres](https://python.langchain.com/api_reference/postgres/index.html)
  * [Prompty](https://python.langchain.com/api_reference/prompty/index.html)
  * [Qdrant](https://python.langchain.com/api_reference/qdrant/index.html)
  * [Redis](https://python.langchain.com/api_reference/redis/index.html)
  * [Sema4](https://python.langchain.com/api_reference/sema4/index.html)
  * [Snowflake](https://python.langchain.com/api_reference/snowflake/index.html)
  * [Sqlserver](https://python.langchain.com/api_reference/sqlserver/index.html)
  * [Standard Tests](https://python.langchain.com/api_reference/standard_tests/index.html)
  * [Tavily](https://python.langchain.com/api_reference/tavily/index.html)
  * [Together](https://python.langchain.com/api_reference/together/index.html)
  * [Unstructured](https://python.langchain.com/api_reference/unstructured/index.html)
  * [Upstage](https://python.langchain.com/api_reference/upstage/index.html)
  * [Weaviate](https://python.langchain.com/api_reference/weaviate/index.html)
  * [XAI](https://python.langchain.com/api_reference/xai/index.html)


  * [ ](https://python.langchain.com/api_reference/index.html)
  * [LangChain Python API Reference](https://python.langchain.com/api_reference/reference.html)
  * [langchain-text-splitters: 0.3.8](https://python.langchain.com/api_reference/text_splitters/index.html)
  * `markdown`


# `markdown`[#](https://python.langchain.com/api_reference/text_splitters/markdown.html#module-langchain_text_splitters.markdown "Link to this heading")
**Classes**
[`markdown.ExperimentalMarkdownSyntaxTextSplitter`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter.html#langchain_text_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter "langchain_text_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter")([...]) | An experimental text splitter for handling Markdown syntax.  
---|---  
[`markdown.HeaderType`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.HeaderType.html#langchain_text_splitters.markdown.HeaderType "langchain_text_splitters.markdown.HeaderType") | Header type as typed dict.  
[`markdown.LineType`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.LineType.html#langchain_text_splitters.markdown.LineType "langchain_text_splitters.markdown.LineType") | Line type as typed dict.  
[`markdown.MarkdownHeaderTextSplitter`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.MarkdownHeaderTextSplitter.html#langchain_text_splitters.markdown.MarkdownHeaderTextSplitter "langchain_text_splitters.markdown.MarkdownHeaderTextSplitter")(...[, ...]) | Splitting markdown files based on specified headers.  
[`markdown.MarkdownTextSplitter`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.MarkdownTextSplitter.html#langchain_text_splitters.markdown.MarkdownTextSplitter "langchain_text_splitters.markdown.MarkdownTextSplitter")(**kwargs) | Attempts to split the text along Markdown-formatted headings.  
© Copyright 2025, LangChain Inc. 

