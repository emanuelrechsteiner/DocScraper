# Python SDK

The official Python client for the Parsify API. Supports both synchronous and asynchronous usage, automatic job polling, and full type annotations.

---

## Installation

```bash
pip install parsify
```

Python 3.9+ required.

---

## Quick Start

=== "Sync"

    ```python
    from parsify import ParsifyClient

    client = ParsifyClient(api_key="pk_your_api_key")

    # Submit a scrape job
    job = client.scrape("https://docs.example.com", max_pages=50)
    print(job.job_id)   # job_abc123

    # Block until the job finishes (polls every 2 seconds)
    result = client.wait_for_completion(job.job_id)

    print(f"Scraped {result.total_pages} pages")
    print(f"Output files: {result.output_files}")
    ```

=== "Async"

    ```python
    import asyncio
    from parsify import AsyncParsifyClient

    async def main():
        async with AsyncParsifyClient(api_key="pk_your_api_key") as client:
            # Submit a scrape job
            job = await client.scrape("https://docs.example.com", max_pages=50)
            print(job.job_id)   # job_abc123

            # Await completion
            result = await client.wait_for_completion(job.job_id)

            print(f"Scraped {result.total_pages} pages")
            print(f"Output files: {result.output_files}")

    asyncio.run(main())
    ```

---

## Authentication

Pass your API key at client construction. The client sends it as a `Bearer` token on every request.

```python
client = ParsifyClient(api_key="pk_your_api_key")
```

!!! tip "Environment variable"
    Store your key in an environment variable instead of hard-coding it.

    ```python
    import os
    from parsify import ParsifyClient

    client = ParsifyClient(api_key=os.environ["PARSIFY_API_KEY"])
    ```

---

## Methods Reference

### `scrape`

Submit a documentation scrape job.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `url` | `str` | Yes | — | Documentation site URL to scrape |
| `max_pages` | `int` | No | `100` | Maximum pages to crawl (1–10,000) |
| `output_format` | `str` | No | `"markdown"` | Output format for scraped content |
| `webhook_url` | `str \| None` | No | `None` | URL to notify on job completion |

**Returns:** `Job`

```python
job = client.scrape(
    url="https://docs.example.com",
    max_pages=200,
    webhook_url="https://yourapp.com/webhooks/parsify",
)
```

---

### `get_job`

Fetch the current status of a job.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `job_id` | `str` | Yes | Job identifier returned by `scrape` |

**Returns:** `Job`

```python
job = client.get_job("job_abc123")
print(job.status)    # "pending" | "running" | "completed" | "failed" | "cancelled"
print(job.progress)  # 0.0 – 100.0
```

---

### `get_result`

Retrieve the result of a completed job. Raises `ParsifyError` with code `JOB_NOT_COMPLETE` if the job has not yet finished.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `job_id` | `str` | Yes | Job identifier |

**Returns:** `JobResult`

```python
result = client.get_result("job_abc123")
print(result.total_pages)   # 47
print(result.output_files)  # ["output/vector_db_index.json", ...]
```

---

### `wait_for_completion`

Poll `get_job` until the job reaches a terminal status (`completed`, `failed`, or `cancelled`), then return the result.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `job_id` | `str` | Yes | — | Job identifier |
| `poll_interval` | `float` | No | `2.0` | Seconds between polls |
| `timeout` | `float \| None` | No | `None` | Max seconds to wait before raising `TimeoutError` |

**Returns:** `JobResult`

```python
# Wait up to 5 minutes
result = client.wait_for_completion(
    "job_abc123",
    poll_interval=3.0,
    timeout=300.0,
)
```

---

### `list_jobs`

Return a paginated list of your jobs.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `status` | `str \| None` | No | `None` | Filter: `"pending"`, `"running"`, `"completed"`, `"failed"`, `"cancelled"` |
| `limit` | `int` | No | `50` | Results per page (1–100) |
| `offset` | `int` | No | `0` | Pagination offset |

**Returns:** `list[Job]`

```python
# All running jobs
running = client.list_jobs(status="running")

# Paginate through completed jobs
page_1 = client.list_jobs(status="completed", limit=20, offset=0)
page_2 = client.list_jobs(status="completed", limit=20, offset=20)
```

---

## Error Handling

All API errors raise `ParsifyError`. Inspect `status_code` for the HTTP status and `code` for the machine-readable error identifier.

```python
from parsify import ParsifyClient, ParsifyError

client = ParsifyClient(api_key="pk_your_api_key")

try:
    result = client.get_result("job_abc123")
except ParsifyError as e:
    print(e.status_code)  # e.g. 404
    print(e.code)         # e.g. "JOB_NOT_FOUND"
    print(e.message)      # e.g. "Job job_abc123 not found"
```

### Common error codes

| Code | HTTP | Description |
|------|------|-------------|
| `UNAUTHORIZED` | 401 | Missing or invalid API key |
| `FORBIDDEN` | 403 | Key does not have permission for this resource |
| `JOB_NOT_FOUND` | 404 | No job exists with the given `job_id` |
| `JOB_NOT_COMPLETE` | 409 | `get_result` called before the job finished |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests; respect `Retry-After` header |
| `INTERNAL_ERROR` | 500 | Server-side error; safe to retry with backoff |

---

## Configuration

Pass options directly to the client constructor.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | `str` | — | Your Parsify API key (**required**) |
| `base_url` | `str` | `"https://api.parsify.dev"` | Override for self-hosted or staging |
| `timeout` | `float` | `30.0` | HTTP request timeout in seconds |

```python
from parsify import ParsifyClient

client = ParsifyClient(
    api_key="pk_your_api_key",
    base_url="https://staging.parsify.dev",
    timeout=60.0,
)
```

---

## Full Working Example

This example scrapes a documentation site, waits for the job, and loads the output into ChromaDB.

```python
import os
import json
import chromadb
from parsify import ParsifyClient, ParsifyError

def scrape_and_index(url: str, collection_name: str) -> None:
    """Scrape a documentation site and index it into ChromaDB.

    Args:
        url: Documentation site to scrape.
        collection_name: ChromaDB collection to create.
    """
    client = ParsifyClient(api_key=os.environ["PARSIFY_API_KEY"])

    # 1. Submit the job
    print(f"Submitting scrape job for {url}…")
    job = client.scrape(url, max_pages=200)
    print(f"Job submitted: {job.job_id}")

    # 2. Wait for completion (up to 10 minutes)
    try:
        result = client.wait_for_completion(
            job.job_id,
            poll_interval=5.0,
            timeout=600.0,
        )
    except TimeoutError:
        print("Timed out waiting for job to finish.")
        return
    except ParsifyError as e:
        print(f"Job failed: [{e.code}] {e.message}")
        return

    print(f"Done. Scraped {result.total_pages} pages.")

    # 3. Load vector index and ingest into ChromaDB
    vector_index_path = next(
        (f for f in result.output_files if f.endswith("vector_db_index.json")),
        None,
    )
    if vector_index_path is None:
        print("No vector index in output.")
        return

    with open(vector_index_path) as f:
        chunks = json.load(f)

    chroma = chromadb.Client()
    collection = chroma.create_collection(collection_name)
    collection.add(
        documents=[c["content"] for c in chunks],
        metadatas=[c["metadata"] for c in chunks],
        ids=[c["chunk_id"] for c in chunks],
    )
    print(f"Indexed {len(chunks)} chunks into '{collection_name}'.")


if __name__ == "__main__":
    scrape_and_index(
        url="https://docs.example.com",
        collection_name="example_docs",
    )
```

---

## Async Full Example

```python
import asyncio
import os
from parsify import AsyncParsifyClient, ParsifyError


async def main() -> None:
    async with AsyncParsifyClient(
        api_key=os.environ["PARSIFY_API_KEY"],
        timeout=60.0,
    ) as client:
        # Submit multiple jobs concurrently
        urls = [
            "https://docs.example.com",
            "https://docs.another.com",
        ]
        jobs = await asyncio.gather(
            *[client.scrape(url, max_pages=100) for url in urls]
        )

        job_ids = [job.job_id for job in jobs]
        print(f"Submitted {len(job_ids)} jobs: {job_ids}")

        # Wait for all jobs concurrently
        results = await asyncio.gather(
            *[
                client.wait_for_completion(jid, poll_interval=3.0, timeout=300.0)
                for jid in job_ids
            ],
            return_exceptions=True,
        )

        for url, result in zip(urls, results):
            if isinstance(result, Exception):
                print(f"{url}: FAILED — {result}")
            else:
                print(f"{url}: {result.total_pages} pages scraped")


asyncio.run(main())
```
