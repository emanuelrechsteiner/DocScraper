---
# Archived: 2025-11-09

**Reason**: This file was archived during documentation consolidation.
**Replacement**: Content has been consolidated into standard docs structure.
**See**: ../.. for current documentation.

---


# DocScraper - Implementation Patterns & Best Practices

## 1. SCRAPER USAGE PATTERNS

### Pattern 1.1: Basic Sequential Scraping

**Use Case**: Small documentation sites, testing, debugging

```python
#!/usr/bin/env python3
import asyncio
from SimpleDocScraper import DocumentationScraper

async def scrape_docs():
    scraper = DocumentationScraper(output_dir="my_docs")
    await scraper.scrape_documentation(
        start_url="https://docs.example.com",
        max_pages=100
    )

if __name__ == "__main__":
    asyncio.run(scrape_docs())
```

**Characteristics**:
- One URL at a time
- Built-in 2-second delays
- Simple, predictable
- Good for development

### Pattern 1.2: Advanced Parallel Scraping

**Use Case**: Large documentation sites, production deployment

```python
#!/usr/bin/env python3
import asyncio
from DocScraper import DocumentationScraper

async def scrape_large_docs():
    scraper = DocumentationScraper(output_dir="large_docs")
    
    # Parallel processing with rate limiting
    await scraper.scrape_documentation(
        start_url="https://docs.anthropic.com",
        max_pages=5000  # Can handle large sites
    )

if __name__ == "__main__":
    asyncio.run(scrape_large_docs())
```

**Characteristics**:
- Batch processing (10 URLs per batch)
- 5 concurrent crawls
- Adaptive memory management
- Rate limiting with exponential backoff

### Pattern 1.3: Controlled Stop Mechanism

**Use Case**: User-initiated stops, resource management

```python
#!/usr/bin/env python3
import asyncio
from DocScraper import DocumentationScraper

async def scrape_with_timeout():
    scraper = DocumentationScraper(output_dir="timeout_docs")
    
    # Start scraping in background task
    scrape_task = asyncio.create_task(
        scraper.scrape_documentation(
            start_url="https://docs.example.com",
            max_pages=10000
        )
    )
    
    try:
        # Let it run for max 5 minutes
        await asyncio.wait_for(scrape_task, timeout=300)
    except asyncio.TimeoutError:
        print("Timeout reached, stopping scraper...")
        scraper.should_stop = True
        await scrape_task
    
    print(f"Scraped {len(scraper.visited_urls)} pages")
    print(f"Failed: {len(scraper.failed_urls)} pages")

if __name__ == "__main__":
    asyncio.run(scrape_with_timeout())
```

**Characteristics**:
- Graceful stop signal handling
- Clean shutdown
- Progress tracking during stop

### Pattern 1.4: Multi-Site Scraping

**Use Case**: Scraping multiple documentation sites

```python
#!/usr/bin/env python3
import asyncio
from DocScraper import DocumentationScraper
from pathlib import Path

async def scrape_multiple_sites():
    sites = {
        "anthropic": "https://docs.anthropic.com",
        "react": "https://react.dev",
        "fastapi": "https://fastapi.tiangolo.com"
    }
    
    for name, url in sites.items():
        output_dir = f"docs/{name}"
        print(f"\nScraping {name}...")
        
        scraper = DocumentationScraper(output_dir=output_dir)
        await scraper.scrape_documentation(url, max_pages=500)
        
        print(f"  ✓ {len(scraper.visited_urls)} pages")
        print(f"  ✗ {len(scraper.failed_urls)} failed")

if __name__ == "__main__":
    asyncio.run(scrape_multiple_sites())
```

---

## 2. POST-PROCESSOR USAGE PATTERNS

### Pattern 2.1: Basic Single-Folder Processing

**Use Case**: Process documents from a single folder

```python
#!/usr/bin/env python3
import asyncio
from DocPostProcessor import DocumentPostProcessor
import os
from dotenv import load_dotenv

async def process_docs():
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    processor = DocumentPostProcessor(
        input_dir="Documentation/Anthropic",
        output_dir="processed_docs"
    )
    
    summary = await processor.process_all_documents()
    
    print(f"Processed: {summary['total_documents']} documents")
    print(f"Created: {summary['total_chunks']} chunks")
    print(f"Categories: {summary['categories']}")

if __name__ == "__main__":
    asyncio.run(process_docs())
```

### Pattern 2.2: Multi-Folder Recursive Processing

**Use Case**: Process multiple documentation folders with flattened output

```python
#!/usr/bin/env python3
import asyncio
from DocPostProcessor import DocumentPostProcessor

async def process_all_docs():
    processor = DocumentPostProcessor(
        input_dir="Documentation",      # Root folder
        output_dir="processed_all"
    )
    
    summary = await processor.process_all_documents(
        recursive=True,      # Process all subfolders
        flatten_output=True  # Consolidate in single directory
    )
    
    print("\n✅ Processing Complete!")
    print(f"Folders processed: {summary['source_folders']}")
    print(f"Total documents: {summary['total_documents']}")
    print(f"Total chunks: {summary['total_chunks']}")
    
    print("\nCategory breakdown:")
    for category, count in summary['categories'].items():
        print(f"  - {category}: {count}")

if __name__ == "__main__":
    asyncio.run(process_all_docs())
```

### Pattern 2.3: Custom Chunk Size Configuration

**Use Case**: Optimize chunk size for specific embedding model

```python
#!/usr/bin/env python3
import asyncio
from DocPostProcessor import (
    DocumentPostProcessor, 
    DocumentStructurer,
    DocumentCleaner,
    DocumentSorter
)

async def process_with_custom_chunks():
    # Create custom structurer for small embeddings
    class SmallChunkStructurer(DocumentStructurer):
        def __init__(self):
            # Smaller chunks for models like MiniLM
            super().__init__(chunk_size=300, chunk_overlap=50)
    
    # Instantiate processor
    processor = DocumentPostProcessor(
        input_dir="Documentation",
        output_dir="processed_small_chunks"
    )
    
    # Replace structurer
    processor.structurer = SmallChunkStructurer()
    
    summary = await processor.process_all_documents()
    print(f"Processed with custom chunk size")

if __name__ == "__main__":
    asyncio.run(process_with_custom_chunks())
```

### Pattern 2.4: Custom Cleaning Patterns

**Use Case**: Remove domain-specific elements

```python
#!/usr/bin/env python3
import asyncio
from DocPostProcessor import DocumentPostProcessor, DocumentCleaner

async def process_with_custom_cleaning():
    processor = DocumentPostProcessor(
        input_dir="Documentation",
        output_dir="processed_custom_clean"
    )
    
    # Add custom patterns
    processor.cleaner.header_patterns.extend([
        r'\[Sponsored\].*?\n',
        r'Ads:.*?\n',
        r'© \d+ Company Name\n'
    ])
    
    processor.cleaner.footer_patterns.extend([
        r'Follow us on.*?\n',
        r'Newsletter signup.*?(?=\n\n|\Z)'
    ])
    
    summary = await processor.process_all_documents()
    print("Processing complete with custom patterns")

if __name__ == "__main__":
    asyncio.run(process_with_custom_cleaning())
```

### Pattern 2.5: Rule-Based Classification Only

**Use Case**: Process without LLM (no API costs, offline)

```python
#!/usr/bin/env python3
import asyncio
from DocPostProcessor import DocumentPostProcessor, DocumentSorter

async def process_without_llm():
    # Create sorter without API key
    sorter = DocumentSorter(api_key=None)  # Forces rule-based
    
    processor = DocumentPostProcessor(
        input_dir="Documentation",
        output_dir="processed_no_llm"
    )
    
    # Override sorter
    processor.sorter = sorter
    
    summary = await processor.process_all_documents()
    print("Processing complete with rule-based classification")

if __name__ == "__main__":
    asyncio.run(process_without_llm())
```

---

## 3. VECTOR DATABASE INTEGRATION PATTERNS

### Pattern 3.1: OpenAI Embeddings with Pinecone

**Prerequisites**: `pip install pinecone-client openai`

```python
#!/usr/bin/env python3
import json
from pathlib import Path
from openai import OpenAI
from pinecone import Pinecone

def load_and_embed_for_pinecone():
    # Load processed chunks
    vector_index_file = Path("processed_docs/vector_db_index.json")
    with open(vector_index_file) as f:
        chunks = json.load(f)
    
    # Initialize clients
    openai_client = OpenAI(api_key="sk-...")
    pc = Pinecone(api_key="pc-...")
    index = pc.Index("documentation")
    
    # Generate embeddings in batches
    batch_size = 100
    vectors_to_upsert = []
    
    for i, chunk in enumerate(chunks):
        # Generate embedding
        response = openai_client.embeddings.create(
            input=chunk['content'],
            model="text-embedding-3-small"
        )
        
        embedding = response.data[0].embedding
        
        # Prepare for Pinecone
        vectors_to_upsert.append((
            chunk['chunk_id'],
            embedding,
            chunk['metadata']
        ))
        
        # Upsert in batches
        if (i + 1) % batch_size == 0:
            index.upsert(vectors=vectors_to_upsert)
            vectors_to_upsert = []
            print(f"Upserted {i+1}/{len(chunks)} chunks")
    
    # Upsert remaining
    if vectors_to_upsert:
        index.upsert(vectors=vectors_to_upsert)
    
    print(f"✓ All {len(chunks)} chunks embedded and stored!")

if __name__ == "__main__":
    load_and_embed_for_pinecone()
```

### Pattern 3.2: Sentence Transformers with ChromaDB

**Prerequisites**: `pip install chromadb sentence-transformers`

```python
#!/usr/bin/env python3
import json
from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

def load_and_embed_for_chroma():
    # Load processed chunks
    vector_index_file = Path("processed_docs/vector_db_index.json")
    with open(vector_index_file) as f:
        chunks = json.load(f)
    
    # Initialize ChromaDB client and model
    chroma_client = chromadb.Client()
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Create collection
    collection = chroma_client.create_collection(
        name="documentation",
        metadata={"hnsw:space": "cosine"}
    )
    
    # Embed and add to collection
    ids = []
    documents = []
    metadatas = []
    embeddings = []
    
    for chunk in chunks:
        embedding = model.encode(chunk['content']).tolist()
        
        ids.append(chunk['chunk_id'])
        documents.append(chunk['content'])
        metadatas.append(chunk['metadata'])
        embeddings.append(embedding)
    
    # Batch add
    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )
    
    print(f"✓ Added {len(chunks)} chunks to ChromaDB!")

if __name__ == "__main__":
    load_and_embed_for_chroma()
```

### Pattern 3.3: Semantic Search Implementation

**Works with any vector database**

```python
#!/usr/bin/env python3
from sentence_transformers import SentenceTransformer
from openai import OpenAI

class DocumentationSearcher:
    def __init__(self, vector_db_client, embedding_model="all-MiniLM-L6-v2"):
        self.db = vector_db_client
        self.model = SentenceTransformer(embedding_model)
    
    def search(self, query: str, k: int = 5) -> list:
        """Search documentation using semantic similarity."""
        # Embed query
        query_embedding = self.model.encode(query).tolist()
        
        # Search vector DB
        results = self.db.query(
            vector=query_embedding,
            top_k=k,
            include_metadata=True
        )
        
        return results
    
    def search_with_reranking(self, query: str, k: int = 5):
        """Search with LLM reranking for better relevance."""
        # Get more candidates
        candidates = self.search(query, k=k*3)
        
        # Rerank with LLM
        client = OpenAI()
        
        rerank_prompt = f"""
        Given the query: "{query}"
        
        Rank these documents by relevance (1 = most relevant):
        
        """
        
        for i, result in enumerate(candidates):
            rerank_prompt += f"\n{i+1}. {result['metadata']['title']}: {result['content'][:200]}..."
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a relevance ranking expert."},
                {"role": "user", "content": rerank_prompt}
            ],
            max_tokens=500
        )
        
        # Return top k after reranking
        return response.choices[0].message.content

# Usage
if __name__ == "__main__":
    # Initialize with your vector DB
    # searcher = DocumentationSearcher(db_client)
    # results = searcher.search("How do I use Claude API?")
    pass
```

---

## 4. CUSTOM EXTENSION PATTERNS

### Pattern 4.1: Custom Cleaner Plugin

**Use Case**: Add domain-specific cleaning logic**

```python
from DocPostProcessor import DocumentCleaner

class CustomCleaner(DocumentCleaner):
    """Cleaner with additional patterns for specific documentation."""
    
    def __init__(self):
        super().__init__()
        
        # Add custom patterns
        self.header_patterns.extend([
            r'\[deprecated\].*?\n',
            r'Migration guide:.*?\n',
            r'⚠️ Warning:.*?\n'
        ])
        
        # Custom preprocessing
        self.custom_replacements = {
            'OLD_API': 'NEW_API',
            'Legacy': 'Current'
        }
    
    def clean_document(self, content, preserve_structure=True):
        # Apply custom replacements
        for old, new in self.custom_replacements.items():
            content = content.replace(old, new)
        
        # Apply parent cleaning
        cleaned = super().clean_document(content, preserve_structure)
        
        # Post-clean custom logic
        cleaned = self._apply_custom_filters(cleaned)
        
        return cleaned
    
    def _apply_custom_filters(self, content):
        """Apply domain-specific filters."""
        # Example: Remove code comments
        import re
        content = re.sub(r'// TODO:.*?\n', '', content)
        return content
```

### Pattern 4.2: Custom Structurer Plugin

**Use Case**: Smart chunking based on document structure**

```python
from DocPostProcessor import DocumentStructurer

class SmartStructurer(DocumentStructurer):
    """Structurer that adapts chunk size based on content."""
    
    def structure_document(self, content, metadata):
        # Detect if content is API reference
        if 'api' in metadata.get('url', '').lower():
            self.chunk_size = 500      # Smaller chunks for API docs
            self.chunk_overlap = 100
        # Detect if content is tutorial
        elif 'guide' in metadata.get('url', '').lower():
            self.chunk_size = 1500     # Larger chunks for guides
            self.chunk_overlap = 300
        
        return super().structure_document(content, metadata)
```

### Pattern 4.3: Custom Sorter Plugin

**Use Case**: Custom document classification logic**

```python
from DocPostProcessor import DocumentSorter, ProcessedDocument

class CustomSorter(DocumentSorter):
    """Sorter with custom categories."""
    
    def __init__(self, api_key=None):
        super().__init__(api_key)
        
        # Override categories
        self.categories = {
            'quick_start': ['5-minute', 'quick', 'start'],
            'deep_dive': ['comprehensive', 'detailed', 'full'],
            'faq': ['frequently', 'asked', 'common'],
            'troubleshoot': ['problem', 'issue', 'error'],
            'reference': ['api', 'reference', 'documentation']
        }
    
    def _rule_based_classification(self, doc: ProcessedDocument) -> str:
        """Custom rule-based classification."""
        content = ' '.join([c.content for c in doc.chunks]).lower()
        
        # Custom scoring logic
        scores = {}
        for category, keywords in self.categories.items():
            score = sum(content.count(kw) for kw in keywords)
            scores[category] = score
        
        # Return highest scoring category
        return max(scores, key=scores.get) if scores else 'reference'
```

---

## 5. ERROR RECOVERY PATTERNS

### Pattern 5.1: Retry with Exponential Backoff

**Use Case**: Handle transient network failures**

```python
#!/usr/bin/env python3
import asyncio
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=30),
    retry=retry_if_exception_type((ConnectionError, TimeoutError))
)
async def fetch_with_retry(url):
    """Fetch URL with automatic retry."""
    # Your fetch logic here
    pass
```

### Pattern 5.2: Batch Processing with Error Recovery

**Use Case**: Process files with per-item error handling**

```python
#!/usr/bin/env python3
import asyncio
from pathlib import Path
from typing import List

async def process_files_with_recovery(input_dir: str) -> dict:
    """Process all files with comprehensive error tracking."""
    
    results = {
        'succeeded': [],
        'failed': [],
        'errors': {}
    }
    
    md_files = list(Path(input_dir).glob('*.md'))
    
    for file_path in md_files:
        try:
            # Your processing logic
            result = await process_file(file_path)
            results['succeeded'].append(str(file_path))
            
        except ValueError as e:
            # Validation errors
            results['failed'].append(str(file_path))
            results['errors'][str(file_path)] = f"Validation: {str(e)}"
            continue
            
        except Exception as e:
            # Unexpected errors
            results['failed'].append(str(file_path))
            results['errors'][str(file_path)] = f"Unexpected: {str(e)}"
            continue
    
    # Summary report
    print(f"\n✓ Succeeded: {len(results['succeeded'])}")
    print(f"✗ Failed: {len(results['failed'])}")
    
    if results['errors']:
        print(f"\nErrors:")
        for file, error in results['errors'].items():
            print(f"  - {file}: {error}")
    
    return results

async def process_file(file_path):
    """Process a single file."""
    # Implement your processing logic
    pass
```

---

## 6. PERFORMANCE OPTIMIZATION PATTERNS

### Pattern 6.1: Parallel LLM Classification

**Use Case**: Speed up document classification with concurrent API calls**

```python
#!/usr/bin/env python3
import asyncio
from typing import List
from DocPostProcessor import ProcessedDocument, DocumentSorter

async def classify_in_parallel(
    documents: List[ProcessedDocument],
    max_concurrent: int = 5
):
    """Classify documents with rate limiting."""
    
    sorter = DocumentSorter(api_key="sk-...")
    
    # Semaphore to limit concurrent API calls
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def classify_with_limit(doc):
        async with semaphore:
            return await sorter.classify_document(doc)
    
    # Classify all in parallel
    tasks = [classify_with_limit(doc) for doc in documents]
    categories = await asyncio.gather(*tasks)
    
    # Assign categories
    for doc, category in zip(documents, categories):
        doc.category = category
    
    return documents
```

### Pattern 6.2: Batch Processing with Progress Tracking

**Use Case**: Process large document sets with progress updates**

```python
#!/usr/bin/env python3
from pathlib import Path
from tqdm import tqdm

def process_documents_with_progress(input_dir: str):
    """Process documents with progress bar."""
    
    md_files = list(Path(input_dir).rglob('*.md'))
    
    processed = []
    failed = []
    
    # Progress bar
    for file_path in tqdm(md_files, desc="Processing"):
        try:
            # Process file
            doc = process_file(file_path)
            processed.append(doc)
        except Exception as e:
            failed.append((file_path, e))
    
    print(f"\n✓ Processed: {len(processed)}")
    print(f"✗ Failed: {len(failed)}")
    
    return processed, failed

def process_file(file_path):
    # Implement your logic
    pass
```

### Pattern 6.3: Memory-Efficient Batch Loading

**Use Case**: Process very large document sets without memory overflow**

```python
#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Generator

def load_chunks_lazily(vector_db_index_file: str) -> Generator:
    """Load chunks one at a time instead of loading all into memory."""
    
    with open(vector_db_index_file) as f:
        for line in f:
            if line.strip():
                chunk = json.loads(line)
                yield chunk

# Usage
for chunk in load_chunks_lazily("processed_docs/vector_db_index.json"):
    # Process each chunk
    embedding = generate_embedding(chunk['content'])
    store_in_db(chunk['chunk_id'], embedding, chunk['metadata'])
```

---

## 7. TESTING PATTERNS

### Pattern 7.1: Unit Testing Cleaner

**Use Case**: Test custom cleaning patterns**

```python
#!/usr/bin/env python3
import unittest
from DocPostProcessor import DocumentCleaner

class TestDocumentCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = DocumentCleaner()
    
    def test_remove_header_patterns(self):
        """Test header pattern removal."""
        content = "Navigation\nSome content"
        cleaned = self.cleaner.clean_document(content)
        self.assertNotIn("Navigation", cleaned)
    
    def test_preserve_code_blocks(self):
        """Test code block preservation."""
        content = "```python\nprint('hello')\n```\nOther text"
        cleaned = self.cleaner.clean_document(content)
        self.assertIn("print('hello')", cleaned)
    
    def test_extract_metadata(self):
        """Test YAML metadata extraction."""
        content = """---
url: https://example.com
title: Example
---
Content here"""
        metadata, body = self.cleaner.extract_metadata(content)
        self.assertEqual(metadata['url'], 'https://example.com')
        self.assertIn("Content here", body)

if __name__ == "__main__":
    unittest.main()
```

### Pattern 7.2: Integration Testing Pipeline

**Use Case**: Test end-to-end processing**

```python
#!/usr/bin/env python3
import asyncio
import unittest
import tempfile
from pathlib import Path
from DocPostProcessor import DocumentPostProcessor

class TestPostProcessingPipeline(unittest.TestCase):
    async def test_full_pipeline(self):
        """Test complete post-processing pipeline."""
        
        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = Path(tmpdir) / "input"
            output_dir = Path(tmpdir) / "output"
            input_dir.mkdir()
            
            # Create test markdown file
            test_file = input_dir / "test.md"
            test_file.write_text("""---
url: https://example.com
title: Test Document
---

# Introduction

This is a test document.

## Section 1

Content here.

```python
code = "example"
```
""")
            
            # Process
            processor = DocumentPostProcessor(str(input_dir), str(output_dir))
            summary = await processor.process_all_documents()
            
            # Assertions
            self.assertEqual(summary['total_documents'], 1)
            self.assertGreater(summary['total_chunks'], 0)
            
            # Check output files
            self.assertTrue((output_dir / 'cleaned').exists())
            self.assertTrue((output_dir / 'chunks').exists())
            self.assertTrue((output_dir / 'vector_db_index.json').exists())

if __name__ == "__main__":
    # Run async test
    unittest.main()
```

---

## 8. DEPLOYMENT PATTERNS

### Pattern 8.1: Docker Containerization

**Use Case**: Deploy in containerized environment**

```dockerfile
# Dockerfile
FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    chromium-browser \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN python -m playwright install chromium

# Copy application
COPY . .

# Create volumes for input/output
VOLUME ["/data/input", "/data/output"]

# Default command
CMD ["python", "DocPostProcessor.py", "/data/input", "/data/output"]
```

### Pattern 8.2: Environment Configuration

**Use Case**: Manage configuration across environments**

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration."""
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 1000))
    CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP', 200))
    MAX_PAGES = int(os.getenv('MAX_PAGES', 1000))
    RATE_LIMIT = float(os.getenv('RATE_LIMIT', 2.0))

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    MAX_PAGES = 100
    RATE_LIMIT = 0.5  # Faster for testing

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    MAX_PAGES = 5000
    RATE_LIMIT = 2.0

# Usage
config = ProductionConfig if os.getenv('ENV') == 'production' else DevelopmentConfig()
```

This comprehensive guide covers the main usage patterns and best practices for DocScraper!
