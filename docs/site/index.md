# Parsify

**Documentation scraping and processing REST API**

Parsify transforms web documentation into AI-ready formats — cleaned markdown, semantic chunks, and classified content — through a simple REST API. Stop writing one-off scraping scripts. Ship your RAG pipeline faster.

---

## Features

### Scrape any documentation site
Submit a URL and Parsify handles JavaScript rendering, link discovery, and recursive crawling. Supports up to 10,000 pages per request on Enterprise plans.

### Intelligent content cleaning
25+ pattern-based rules strip navigation, footers, duplicate boilerplate, and cookie banners — leaving only the content your model needs.

### AI-powered classification
GPT-4o categorizes every page by type: tutorial, concept, API reference, guide, or changelog. Your retrieval pipeline gets structured metadata out of the box.

### Semantic chunking
Content is split into embedding-optimized chunks with configurable size and overlap. Each chunk carries full source metadata so you can link back to the original page.

### Async job processing
Scraping large documentation sets takes time. Submit a job, get a `job_id`, and poll or receive a webhook when results are ready.

### Vector database ready
Every job produces a `vector_db_index.json` you can load directly into Pinecone, Weaviate, ChromaDB, or Qdrant.

---

## Quick Start

### 1. Submit a scrape job

```bash
curl -X POST https://api.parsify.dev/api/v1/scrape \
  -H "Authorization: Bearer pk_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://docs.example.com",
    "max_pages": 50
  }'
```

```json
{
  "data": {
    "job_id": "job_abc123",
    "status": "pending",
    "message": "Scrape job submitted successfully"
  }
}
```

### 2. Poll for results

```bash
curl https://api.parsify.dev/api/v1/jobs/job_abc123 \
  -H "Authorization: Bearer pk_your_api_key"
```

```json
{
  "data": {
    "job_id": "job_abc123",
    "status": "completed",
    "result": {
      "total_pages": 47,
      "total_chunks": 312,
      "download_url": "https://api.parsify.dev/api/v1/jobs/job_abc123/download"
    }
  }
}
```

### 3. Load into your vector database

```python
import json
import chromadb

# Download and unpack the result archive, then:
with open("vector_db_index.json") as f:
    chunks = json.load(f)

client = chromadb.Client()
collection = client.create_collection("my_docs")

collection.add(
    documents=[c["content"] for c in chunks],
    metadatas=[c["metadata"] for c in chunks],
    ids=[c["chunk_id"] for c in chunks],
)
```

---

## Plans

| | Free | Pro | Enterprise |
|---|---|---|---|
| Requests per hour | 100 | 1,000 | 10,000 |
| Max pages per request | 100 | 5,000 | 10,000 |
| Concurrent jobs | 2 | 10 | 50 |
| Webhook callbacks | No | Yes | Yes |
| Usage analytics | No | Yes | Yes |
| SLA | No | No | 99.9% uptime |
| Support | Community | Email 24h | Dedicated 4h |
| Price | $0/mo | $49/mo | $299/mo |

[See full pricing details](pricing.md){ .md-button .md-button--primary }
[Get Started Free](getting-started.md){ .md-button }

---

## Documentation

- [Getting Started](getting-started.md) — Create an account and make your first API call
- [API Reference](api-reference.md) — Full endpoint documentation
- [Authentication](guides/authentication.md) — API key management
- [Pricing](pricing.md) — Plans and usage limits
