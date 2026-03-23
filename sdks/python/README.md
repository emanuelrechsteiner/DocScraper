# Parsify Python SDK

Python client for the [Parsify](https://parsify.dev) documentation processing API.

## Installation

```bash
pip install parsify
```

## Quick Start

```python
from parsify import ParsifyClient

with ParsifyClient(api_key="pk_your_api_key") as client:
    # Submit a scrape job
    job = client.scrape("https://docs.example.com", max_pages=50)
    print(f"Job submitted: {job.job_id}")

    # Wait for completion (polls every 5 seconds)
    result = client.wait_for_completion(job.job_id)
    print(f"Scraped {result.pages_scraped} pages")
    print(f"Files: {result.output_files}")
```

## Async Usage

```python
import asyncio
from parsify import AsyncParsifyClient

async def main():
    async with AsyncParsifyClient(api_key="pk_your_key") as client:
        job = await client.scrape("https://docs.example.com")
        result = await client.wait_for_completion(job.job_id)
        print(result.output_files)

asyncio.run(main())
```

## API Reference

### `ParsifyClient` / `AsyncParsifyClient`

| Method | Description |
|---|---|
| `scrape(url, max_pages, output_format, webhook_url)` | Submit a new scrape job |
| `get_job(job_id)` | Fetch current job status |
| `get_result(job_id)` | Fetch completed job result |
| `wait_for_completion(job_id, poll_interval, timeout)` | Block until job finishes |
| `list_jobs(status, limit)` | List jobs with optional filtering |

### Error Handling

```python
from parsify.client import ParsifyError

try:
    result = client.wait_for_completion(job.job_id)
except ParsifyError as e:
    print(f"Error {e.status_code}: {e} (code: {e.code})")
```

## Requirements

- Python 3.10+
- httpx >= 0.27.0
