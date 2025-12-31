# DocScraper Architecture - Detailed Visual Guide

## 1. SYSTEM COMPONENT DIAGRAM

```
┌──────────────────────────────────────────────────────────────────────┐
│                     DOCSCRAPER SYSTEM ARCHITECTURE                   │
└──────────────────────────────────────────────────────────────────────┘

┌─ PHASE 1: WEB SCRAPING ──────────────────┬─ PHASE 2: POST-PROCESSING ─┐
│                                          │                            │
│  Documentation Website                  │ Raw Markdown Files         │
│  (HTML pages)                          │ (with YAML metadata)       │
│        │                                │        │                   │
│        ▼                                │        ▼                   │
│  ┌─────────────────────────┐           │  ┌──────────────────────┐  │
│  │ AsyncWebCrawler         │           │  │ DocumentCleaner      │  │
│  │ + Playwright            │           │  │                      │  │
│  │ (crawl4ai)              │           │  │ • Remove headers     │  │
│  │                         │           │  │ • Remove footers     │  │
│  │ Features:              │           │  │ • Remove nav         │  │
│  │ • JS rendering         │           │  │ • Normalize spacing  │  │
│  │ • Cookie handling      │           │  │ • Extract metadata   │  │
│  │ • Rate limiting        │           │  │                      │  │
│  │ • Error recovery       │           │  │ Output: Clean text   │  │
│  └────────┬────────────────┘           │  └──────────┬───────────┘  │
│           │                            │             │               │
│     ┌─────▼──────────────┐             │      ┌──────▼──────────┐   │
│     │ DocumentationScraper│             │      │ DocumentStructurer
│     │                    │             │      │                  │   │
│     │ • URL discovery    │             │      │ • Parse headers  │   │
│     │ • Link extraction  │             │      │ • Create chunks  │   │
│     │ • BFS crawling     │             │      │ • Handle code    │   │
│     │ • Stop signal      │             │      │ • Token counting │   │
│     │ • Batch processing │             │      │ • Overlap chunks │   │
│     │                    │             │      │                  │   │
│     │ Output:            │             │      │ Output: Chunks   │   │
│     │ • .md files        │             │      │ with metadata    │   │
│     │ • Metadata         │             │      └──────┬───────────┘   │
│     │ • Summary JSON     │             │             │               │
│     └────────┬───────────┘             │      ┌──────▼────────────┐  │
│              │                         │      │ DocumentSorter    │  │
│              │                         │      │                   │  │
│              │                         │      │ • LLM classify    │  │
│              │                         │      │ • Build dep graph │  │
│              │                         │      │ • Score complexity
│              │                         │      │ • Topological sort
│              │                         │      │                   │  │
│              │                         │      │ Output: Sorted    │  │
│              │                         │      │ documents with    │  │
│              │                         │      │ metadata          │  │
│              │                         │      └──────┬────────────┘  │
│              │                         │             │               │
│              ▼                         │             ▼               │
│  ┌──────────────────────┐             │  ┌─────────────────────┐   │
│  │ Scraped Docs Dir     │             │  │ DocumentPostProcessor
│  │                      │             │  │                     │   │
│  │ ├─ index.md          │             │  │ • Orchestrate       │   │
│  │ ├─ getting_started.md│             │  │ • Process all docs  │   │
│  │ ├─ api_reference.md  │             │  │ • Generate index    │   │
│  │ └─ _scrape_summary   │             │  │ • Save output       │   │
│  │    .json             │             │  │                     │   │
│  └──────────────────────┘             │  └──────┬──────────────┘   │
│                                        │         │                   │
│                                        │         ▼                   │
│                                        │  ┌─────────────────────┐   │
│                                        │  │ Processed Docs Dir  │   │
│                                        │  │                     │   │
│                                        │  │ ├─ cleaned/         │   │
│                                        │  │ │  ├─ 0000_*.md     │   │
│                                        │  │ │  ├─ 0001_*.md     │   │
│                                        │  │ ├─ chunks/          │   │
│                                        │  │ │  ├─ 0000_*/       │   │
│                                        │  │ │  │  ├─ chunk_*.json
│                                        │  │ │  ├─ 0001_*/       │   │
│                                        │  │ ├─ metadata/        │   │
│                                        │  │ ├─ processing_     │   │
│                                        │  │ │  summary.json    │   │
│                                        │  │ └─ vector_db_      │   │
│                                        │  │    index.json      │   │
│                                        │  └─────────────────────┘   │
│                                        │                            │
└────────────────────────────────────────┴────────────────────────────┘
```

## 2. DATA STRUCTURE HIERARCHY

```
DocumentationScraper
├── output_dir: Path
├── visited_urls: Set[str]
├── failed_urls: Set[str]
├── domain: str
├── should_stop: bool
└── Methods:
    ├── scrape_documentation(start_url, max_pages)
    ├── scrape_page(crawler, url)
    ├── _is_valid_doc_url(url)
    ├── _extract_internal_links(html, url)
    ├── _clean_filename(url)
    └── _save_content(url, content, metadata)

ProcessedDocument
├── file_path: str
├── original_url: str
├── title: str
├── chunks: List[DocumentChunk]
├── category: str (from DocumentSorter)
├── topics: List[str]
├── dependencies: List[str] (file paths)
├── complexity_score: float (0.0-1.0)
└── to_dict() → Dict

DocumentChunk
├── content: str
├── metadata: Dict[str, Any]
├── chunk_id: str (MD5[:8])
├── parent_doc: str (file path)
├── position: int
├── tokens: int
├── embedding: Optional[List[float]]
└── to_dict() → Dict

DocumentCleaner
├── header_patterns: List[str] (regex)
├── footer_patterns: List[str] (regex)
├── navigation_patterns: List[str] (regex)
└── Methods:
    ├── clean_document(content, preserve_structure)
    ├── extract_metadata(content)
    └── _preserve_important_structure(content)

DocumentStructurer
├── chunk_size: int (default 1000)
├── chunk_overlap: int (default 200)
├── section_patterns: Dict[str, str]
└── Methods:
    ├── structure_document(content, metadata)
    ├── _parse_sections(content)
    └── _create_semantic_chunks(content, metadata)

DocumentSorter
├── api_key: Optional[str]
├── client: Optional[AsyncOpenAI]
├── categories: Dict[str, List[str]]
└── Methods:
    ├── classify_document(doc)
    ├── _rule_based_classification(doc)
    ├── create_dependency_graph(documents)
    ├── calculate_complexity_scores(documents)
    ├── sort_documents(documents)
    └── _topological_sort_with_categories(docs, graph)

DocumentPostProcessor
├── input_dir: Path
├── output_dir: Path
├── cleaner: DocumentCleaner
├── structurer: DocumentStructurer
├── sorter: DocumentSorter
├── processed_docs: List[ProcessedDocument]
└── Methods:
    ├── process_all_documents(recursive, flatten_output)
    ├── process_document(file_path)
    └── save_processed_documents(flatten_output, source_folders)
```

## 3. ASYNC CONTROL FLOW DIAGRAM

### Scraping Flow

```
main() [async]
  │
  └─▶ asyncio.run(scraper.scrape_documentation(url, max_pages))
       │
       └─▶ scrape_documentation() [async]
            │
            ├─ Parse domain from start_url
            ├─ Create rate_limiter
            ├─ Create dispatcher with monitor
            ├─ Initialize urls_to_crawl = {start_url}
            │
            ├─ WHILE urls_to_crawl AND visited < max_pages AND NOT should_stop:
            │   │
            │   ├─ Extract batch_size = min(10, len(urls_to_crawl))
            │   ├─ Get current_batch from urls_to_crawl
            │   ├─ Filter visited URLs
            │   │
            │   ├─ tasks = [scrape_page(crawler, url) for url in batch]
            │   │
            │   ├─ results = await asyncio.gather(*tasks)
            │   │   │
            │   │   └─ scrape_page(url) [async] ×N (parallel)
            │   │       ├─ await asyncio.sleep(2)  // Rate limit
            │   │       ├─ result = await crawler.arun(url, config)
            │   │       ├─ Extract links (BeautifulSoup)
            │   │       ├─ Get title from <title> tag
            │   │       ├─ _save_content() → .md file
            │   │       └─ RETURN {url, links, filepath}
            │   │
            │   ├─ FOR result in results:
            │   │   ├─ visited_urls.add(result['url'])
            │   │   └─ FOR link in result['links']:
            │   │       └─ urls_to_crawl.add(link)
            │   │
            │   ├─ Check should_stop flag
            │   ├─ await asyncio.sleep(1)  // Delay between batches
            │   └─ Progress logging
            │
            └─ Save _scrape_summary.json
```

### Post-Processing Flow

```
main() [async]
  │
  └─▶ asyncio.run(processor.process_all_documents())
       │
       └─▶ process_all_documents() [async]
            │
            ├─ Find all markdown files (recursive or flat)
            ├─ Filter out summary files (starting with _)
            │
            ├─ FOR each md_file:
            │   │
            │   └─▶ process_document(file_path) [async]
            │       ├─ Read file content
            │       ├─ extract_metadata() → (metadata, raw_content)
            │       ├─ clean_document(raw_content) → cleaned
            │       ├─ Create ProcessedDocument
            │       │   └─ structure_document(cleaned) → chunks
            │       └─ RETURN ProcessedDocument
            │
            ├─ sorter.sort_documents(processed_docs) [async]
            │   │
            │   ├─ FOR each document:
            │   │   └─▶ classify_document(doc) [async]
            │   │       ├─ Construct LLM prompt
            │   │       ├─ await client.chat.completions.create()
            │   │       └─ Parse category from response
            │   │           (with 3-attempt retry & exponential backoff)
            │   │
            │   ├─ create_dependency_graph() → nx.DiGraph
            │   │   ├─ Add nodes (documents)
            │   │   └─ Add edges (URL references)
            │   │
            │   ├─ calculate_complexity_scores()
            │   │   ├─ FOR each document:
            │   │   │   ├─ Calculate tokens
            │   │   │   ├─ Count code chunks
            │   │   │   └─ Compute complexity
            │   │   
            │   └─ Topological sort by category
            │       └─ RETURN sorted documents
            │
            └─ save_processed_documents(flatten=True)
                ├─ Create output directories
                ├─ FOR each document (with index i):
                │   ├─ Generate filename (with folder prefix if flatten)
                │   ├─ Save cleaned full doc
                │   │   └─ output_dir/cleaned/{filename}.md
                │   │
                │   ├─ Save chunks
                │   │   ├─ Create output_dir/chunks/{filename}/
                │   │   └─ FOR each chunk:
                │   │       └─ Save chunk_{j:03d}.json
                │   │
                │   └─ Update summary stats
                │
                ├─ Save processing_summary.json
                ├─ Save vector_db_index.json
                └─ RETURN summary
```

## 4. CLASS INHERITANCE & COMPOSITION

```
GUI Classes (Tkinter-based)
├── DocScraperGUI
│   ├── Uses: DocumentationScraper (imported from DocScraper)
│   ├── Has: GUIScraper (extends DocumentationScraper)
│   ├── Uses: threading.Thread
│   ├── Has: queue.Queue (messages to main thread)
│   └── Controls: Tk window, widgets
│
└── DocPostProcessorGUI
    ├── Uses: DocumentPostProcessor (imported from DocPostProcessor)
    ├── Uses: threading.Thread
    ├── Has: queue.Queue (messages to main thread)
    └── Controls: Tk window, widgets

Scraper Classes
├── DocumentationScraper
│   ├── Uses: AsyncWebCrawler (crawl4ai)
│   ├── Uses: BeautifulSoup (HTML parsing)
│   ├── Has: visited_urls, failed_urls, domain, should_stop
│   └── Methods: async scrape_page, scrape_documentation
│
└── GUIScraper (extends DocumentationScraper)
    ├── Overrides: scrape_page (adds GUI logging)
    └── Has: gui reference

Post-Processor Classes
├── DocumentCleaner
│   ├── Uses: regex patterns
│   ├── Uses: yaml.safe_load
│   └── Standalone utility
│
├── DocumentStructurer
│   ├── Uses: hashlib for chunk IDs
│   ├── Standalone utility
│   └── Produces: List[DocumentChunk]
│
├── DocumentSorter
│   ├── Uses: AsyncOpenAI (optional)
│   ├── Uses: NetworkX for graph analysis
│   ├── Produces: sorted documents with metadata
│   └── Methods: async classify_document, sort_documents
│
└── DocumentPostProcessor
    ├── Composes: DocumentCleaner
    ├── Composes: DocumentStructurer
    ├── Composes: DocumentSorter
    ├── Orchestrates: full pipeline
    ├── Methods: async process_all_documents, process_document
    └── Produces: processed output directories
```

## 5. MESSAGE QUEUE PROTOCOL (GUI Threading)

```
Main Thread (Tkinter)
┌──────────────────────────────────┐
│ GUI Window                       │
├──────────────────────────────────┤
│ • Input widgets                  │
│ • Output widgets                 │
│ • Check messages every 100ms     │◄─────┐
│   └─ check_messages()            │      │
│       ├─ Get all from queue      │      │
│       └─ Update GUI widgets      │      │
└──────────────────────────────────┘      │
                                          │
                    ┌─────────────────────┴────────────────────┐
                    │                                          │
Worker Thread       │    queue.Queue[Tuple[str, Any]]         │
(Async scraper)     │                                          │
┌──────────────────────────────────┐                          │
│ run_scraper()                    │                          │
├──────────────────────────────────┤                          │
│ • Create event loop              │                          │
│ • Run async scraper              │                          │
│ • Put messages in queue:         ├─────────────────────────┘
│   ├─ ("log", {...})              │
│   ├─ ("status", str)             │
│   ├─ ("complete", output_dir)    │
│   └─ ("error", error_msg)        │
└──────────────────────────────────┘

Message Formats:
{
  "log": {
    "message": str,
    "level": "INFO" | "WARNING" | "ERROR" | "SUCCESS"
  },
  "status": str,
  "complete": str (output_dir),
  "error": str (error_message)
}
```

## 6. CHUNK STRUCTURE EXAMPLE

```
ProcessedDocument
├── file_path: "Documentation/Anthropic/claude.md"
├── original_url: "https://docs.anthropic.com/claude"
├── title: "Claude Documentation"
├── category: "api_reference"
├── complexity_score: 0.62
├── dependencies: ["Documentation/Anthropic/getting-started.md"]
└── chunks: [
    {
      "chunk_id": "a1b2c3d4",
      "content": "Claude is an AI assistant...",
      "parent_doc": "Documentation/Anthropic/claude.md",
      "position": 0,
      "tokens": 1200,
      "metadata": {
        "section_level": 2,
        "section_title": "Introduction",
        "type": "text",
        "source_url": "https://docs.anthropic.com/claude",
        "doc_title": "Claude Documentation",
        "category": "api_reference",
        "complexity": 0.62
      }
    },
    {
      "chunk_id": "e5f6g7h8",
      "content": "```python\nimport anthropic\nclient = anthropic.Anthropic()\n```",
      "parent_doc": "Documentation/Anthropic/claude.md",
      "position": 1,
      "tokens": 25,
      "metadata": {
        "section_level": 3,
        "section_title": "Usage Example",
        "type": "code",
        "source_url": "https://docs.anthropic.com/claude",
        "doc_title": "Claude Documentation",
        "category": "api_reference",
        "complexity": 0.62
      }
    }
  ]
```

## 7. VECTOR DATABASE INTEGRATION FLOW

```
Processed Documents
    │
    ├─ DocumentPostProcessor.save_processed_documents()
    │   │
    │   └─▶ Generate vector_db_index.json
    │       [
    │         {
    │           "chunk_id": "a1b2c3d4",
    │           "content": "...",
    │           "metadata": {...}
    │         },
    │         ...
    │       ]
    │
    ▼
Vector Database Pipeline
    │
    ├─ Load vector_db_index.json
    │   └─ List[Dict] with 'chunk_id', 'content', 'metadata'
    │
    ├─ Generate Embeddings
    │   ├─ Model: OpenAI API / sentence-transformers / other
    │   ├─ Input: chunk['content'] for each chunk
    │   └─ Output: List[List[float]] (768-1536 dimensions)
    │
    ├─ Prepare Upsert Data
    │   ├─ IDs: chunk_id
    │   ├─ Vectors: embeddings
    │   └─ Metadata: chunk['metadata']
    │
    ├─ Upsert to Vector DB
    │   └─ VectorDB.upsert(ids, vectors, metadata)
    │
    └─ Enable Semantic Search
        ├─ Query: "How do I use Claude API?"
        ├─ Query embedding: model.embed_query(query)
        ├─ Search: db.similarity_search(query_embedding, k=5)
        └─ Results: Top 5 most relevant chunks
```

## 8. ERROR HANDLING HIERARCHY

```
DocumentationScraper
├─ scrape_documentation()
│   ├─ Failed to parse domain → Log error, return summary
│   ├─ Failed to create crawler → Exception handling
│   └─ should_stop flag checked every 100ms
│
└─ scrape_page()
    ├─ Network error → self.failed_urls.add(url)
    ├─ Parsing error → logger.error, return None
    └─ No content extracted → logger.warning

DocumentPostProcessor
├─ process_all_documents()
│   └─ Per-document exception
│       └─ Log error, continue with next file
│
├─ process_document()
│   ├─ File read error → Exception handling
│   ├─ Metadata parsing error → Return empty metadata
│   └─ Cleaning produces no output → Skip document
│
└─ DocumentSorter.classify_document()
    ├─ LLM API error
    │   └─ Retry (3 attempts)
    │       ├─ Exponential backoff (4-10s)
    │       └─ Fallback: rule-based classification
    │
    └─ Rule-based classification
        └─ Default: 'guides' category
```

## 9. Configuration Layers

```
Environment Variables
├─ OPENAI_API_KEY (optional)
│   └─ Enables LLM classification
│
└─ Loaded via: load_dotenv()

CLI Arguments
├─ DocScraper.py
│   ├─ documentation_url (required)
│   ├─ output_dir (default: "scraped_docs")
│   └─ max_pages (default: 1000)
│
└─ DocPostProcessor.py
    ├─ input_dir (required)
    ├─ output_dir (required)
    └─ --use-llm (flag, optional)

GUI Configuration
├─ DocScraperGUI
│   ├─ Starting URL (text input)
│   ├─ Output Directory (text + browse)
│   └─ Max Pages (spinbox 1-10000)
│
└─ DocPostProcessorGUI
    ├─ Input Directory
    ├─ Output Directory
    ├─ Chunk Size (100-5000)
    ├─ Chunk Overlap (0-1000)
    ├─ Process Subfolders (checkbox)
    ├─ Flatten Output (checkbox)
    ├─ Use LLM (checkbox)
    └─ API Key (text, if LLM enabled)

Hardcoded Constants
├─ DocumentStructurer
│   ├─ chunk_size = 1000
│   └─ chunk_overlap = 200
│
├─ DocumentCleaner
│   ├─ header_patterns (9 patterns)
│   ├─ footer_patterns (4 patterns)
│   └─ navigation_patterns (8 patterns)
│
└─ DocumentSorter
    ├─ categories (7 types with keywords)
    └─ category_order (processing order)
```

This comprehensive visual guide maps out every major aspect of the DocScraper architecture!
