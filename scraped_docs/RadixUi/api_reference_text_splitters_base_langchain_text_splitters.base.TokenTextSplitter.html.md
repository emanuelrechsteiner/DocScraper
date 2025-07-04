---
url: https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html
scraped_at: 2025-05-25T18:10:32.648926
title: TokenTextSplitter — 🦜🔗 LangChain  documentation
---

[Skip to main content](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#main-content)
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
      * [Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html)
      * [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html)
      * [TokenTextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html)
      * [Tokenizer](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Tokenizer.html)
      * [split_text_on_tokens](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.split_text_on_tokens.html)
    * [`character`](https://python.langchain.com/api_reference/text_splitters/character.html)
    * [`html`](https://python.langchain.com/api_reference/text_splitters/html.html)
    * [`json`](https://python.langchain.com/api_reference/text_splitters/json.html)
    * [`jsx`](https://python.langchain.com/api_reference/text_splitters/jsx.html)
    * [`konlpy`](https://python.langchain.com/api_reference/text_splitters/konlpy.html)
    * [`latex`](https://python.langchain.com/api_reference/text_splitters/latex.html)
    * [`markdown`](https://python.langchain.com/api_reference/text_splitters/markdown.html)
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
  * [`base`](https://python.langchain.com/api_reference/text_splitters/base.html)
  * TokenTextSplitter


# TokenTextSplitter[#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#tokentextsplitter "Link to this heading") 

_class_ langchain_text_splitters.base.TokenTextSplitter( 
    _encoding_name :str='gpt2'_,     _model_name :str|None=None_,     _allowed_special :Literal['all']|AbstractSet[str]={}_,     _disallowed_special :Literal['all']|Collection[str]='all'_,     _** kwargs:Any_, )[[source]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TokenTextSplitter)[#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter "Link to this definition")     
Splitting text to tokens using model tokenizer.
Create a new TextSplitter.
Methods
[`__init__`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.__init__ "langchain_text_splitters.base.TokenTextSplitter.__init__")([encoding_name, model_name, ...]) | Create a new TextSplitter.  
---|---  
[`atransform_documents`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.atransform_documents "langchain_text_splitters.base.TokenTextSplitter.atransform_documents")(documents, **kwargs) | Asynchronously transform a list of documents.  
[`create_documents`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.create_documents "langchain_text_splitters.base.TokenTextSplitter.create_documents")(texts[, metadatas]) | Create documents from a list of texts.  
[`from_huggingface_tokenizer`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.from_huggingface_tokenizer "langchain_text_splitters.base.TokenTextSplitter.from_huggingface_tokenizer")(tokenizer, **kwargs) | Text splitter that uses HuggingFace tokenizer to count length.  
[`from_tiktoken_encoder`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.from_tiktoken_encoder "langchain_text_splitters.base.TokenTextSplitter.from_tiktoken_encoder")([encoding_name, ...]) | Text splitter that uses tiktoken encoder to count length.  
[`split_documents`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.split_documents "langchain_text_splitters.base.TokenTextSplitter.split_documents")(documents) | Split documents.  
[`split_text`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.split_text "langchain_text_splitters.base.TokenTextSplitter.split_text")(text) | Splits the input text into smaller chunks based on tokenization.  
[`transform_documents`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.transform_documents "langchain_text_splitters.base.TokenTextSplitter.transform_documents")(documents, **kwargs) | Transform sequence of documents by splitting them. 

Parameters:
      
  * **encoding_name** (_str_)
  * **model_name** (_Optional_ _[__str_ _]_)
  * **allowed_special** (_Union_ _[__Literal_ _[__'all'__]__,__AbstractSet_ _[__str_ _]__]_)
  * **disallowed_special** (_Union_ _[__Literal_ _[__'all'__]__,__Collection_ _[__str_ _]__]_)
  * **kwargs** (_Any_)



__init__( 
    _encoding_name :str='gpt2'_,     _model_name :str|None=None_,     _allowed_special :Literal['all']|AbstractSet[str]={}_,     _disallowed_special :Literal['all']|Collection[str]='all'_,     _** kwargs:Any_, ) → None[[source]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TokenTextSplitter.__init__)[#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.__init__ "Link to this definition")     
Create a new TextSplitter. 

Parameters:
    
  * **encoding_name** (_str_)
  * **model_name** (_str_ _|__None_)
  * **allowed_special** (_Literal_ _[__'all'__]__|__~typing.AbstractSet_ _[__str_ _]_)
  * **disallowed_special** (_Literal_ _[__'all'__]__|__~typing.Collection_ _[__str_ _]_)
  * **kwargs** (_Any_)



Return type:
    
None 

_async_ atransform_documents( 
    _documents :Sequence[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")]_,     _** kwargs:Any_, ) → Sequence[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.atransform_documents "Link to this definition")     
Asynchronously transform a list of documents. 

Parameters:
    
  * **documents** (_Sequence_ _[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _]_) – A sequence of Documents to be transformed.
  * **kwargs** (_Any_)



Returns:
    
A sequence of transformed Documents. 

Return type:
    
Sequence[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")] 

create_documents( 
    _texts :list[str]_,     _metadatas :list[dict[Any,Any]]|None=None_, ) → List[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.create_documents "Link to this definition")     
Create documents from a list of texts. 

Parameters:
    
  * **texts** (_list_ _[__str_ _]_)
  * **metadatas** (_list_ _[__dict_ _[__Any_ _,__Any_ _]__]__|__None_)



Return type:
    
_List_[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")] 

_classmethod_ from_huggingface_tokenizer( 
    _tokenizer :Any_,     _** kwargs:Any_, ) → [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")[#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.from_huggingface_tokenizer "Link to this definition")     
Text splitter that uses HuggingFace tokenizer to count length. 

Parameters:
    
  * **tokenizer** (_Any_)
  * **kwargs** (_Any_)



Return type:
    
[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") 

_classmethod_ from_tiktoken_encoder( 
    _encoding_name :str='gpt2'_,     _model_name :str|None=None_,     _allowed_special :Literal['all']|AbstractSet[str]={}_,     _disallowed_special :Literal['all']|Collection[str]='all'_,     _** kwargs:Any_, ) → TS[#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.from_tiktoken_encoder "Link to this definition")     
Text splitter that uses tiktoken encoder to count length. 

Parameters:
    
  * **encoding_name** (_str_)
  * **model_name** (_str_ _|__None_)
  * **allowed_special** (_Literal_ _[__'all'__]__|__~typing.AbstractSet_ _[__str_ _]_)
  * **disallowed_special** (_Literal_ _[__'all'__]__|__~typing.Collection_ _[__str_ _]_)
  * **kwargs** (_Any_)



Return type:
    
_TS_ 

split_documents( 
    _documents :Iterable[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")]_, ) → List[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.split_documents "Link to this definition")     
Split documents. 

Parameters:
    
**documents** (_Iterable_ _[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _]_) 

Return type:
    
_List_[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")] 

split_text(_text :str_) → List[str][[source]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TokenTextSplitter.split_text)[#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.split_text "Link to this definition")
    
Splits the input text into smaller chunks based on tokenization.
This method uses a custom tokenizer configuration to encode the input text into tokens, processes the tokens in chunks of a specified size with overlap, and decodes them back into text chunks. The splitting is performed using the split_text_on_tokens function. 

Parameters:
    
**text** (_str_) – The input text to be split into smaller chunks. 

Returns:
    
A list of text chunks, where each chunk is derived from a portion of the input text based on the tokenization and chunking rules. 

Return type:
    
List[str] 

transform_documents( 
    _documents :Sequence[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")]_,     _** kwargs:Any_, ) → Sequence[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")][#](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.transform_documents "Link to this definition")     
Transform sequence of documents by splitting them. 

Parameters:
    
  * **documents** (_Sequence_ _[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _]_)
  * **kwargs** (_Any_)



Return type:
    
_Sequence_[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")]
Examples using TokenTextSplitter
  * [Apache Doris](https://python.langchain.com/docs/integrations/vectorstores/apache_doris/)
  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)
  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)
  * [How to split text by tokens ](https://python.langchain.com/docs/how_to/split_by_token/)
  * [StarRocks](https://python.langchain.com/docs/integrations/vectorstores/starrocks/)


On this page 
  * [`TokenTextSplitter`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter)
    * [`__init__()`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.__init__)
    * [`atransform_documents()`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.atransform_documents)
    * [`create_documents()`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.create_documents)
    * [`from_huggingface_tokenizer()`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.from_huggingface_tokenizer)
    * [`from_tiktoken_encoder()`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.from_tiktoken_encoder)
    * [`split_documents()`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.split_documents)
    * [`split_text()`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.split_text)
    * [`transform_documents()`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter.transform_documents)


© Copyright 2025, LangChain Inc. 

