# Getting Started

This guide walks you from zero to your first set of scraped, cleaned, and chunked documentation in about five minutes.

**What you will do:**

1. Create a Parsify account
2. Generate an API key
3. Submit a scrape job
4. Poll for completion
5. Download your results

---

## Prerequisites

- A terminal with `curl` available, **or** Python 3.8+ / Node.js 18+
- An email address for registration

---

## Step 1 — Create an account

Send your email address to the registration endpoint. Parsify creates an account and returns a `user_id` you will use in the next step.

=== "curl"

    ```bash
    curl -X POST https://api.parsify.dev/api/v1/auth/register \
      -H "Content-Type: application/json" \
      -d '{
        "email": "ada@example.com",
        "password": "hunter2-but-stronger"
      }'
    ```

=== "Python"

    ```python
    import httpx

    response = httpx.post(
        "https://api.parsify.dev/api/v1/auth/register",
        json={
            "email": "ada@example.com",
            "password": "hunter2-but-stronger",
        },
    )
    response.raise_for_status()
    data = response.json()["data"]
    print(data["user_id"])  # usr_01hx9k2p3e4f5g6h7j8k9l0m
    ```

=== "JavaScript"

    ```js
    const response = await fetch("https://api.parsify.dev/api/v1/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: "ada@example.com",
        password: "hunter2-but-stronger",
      }),
    });

    const { data } = await response.json();
    console.log(data.user_id); // usr_01hx9k2p3e4f5g6h7j8k9l0m
    ```

**Response (201 Created):**

```json
{
  "data": {
    "user_id": "usr_01hx9k2p3e4f5g6h7j8k9l0m",
    "email": "ada@example.com",
    "created_at": "2026-03-23T09:14:02Z"
  }
}
```

Save the `user_id` — you need it in Step 2.

---

## Step 2 — Create an API key

API keys authenticate every subsequent request. A single account can hold multiple keys (useful for separating production and development workloads).

Replace `usr_01hx9k2p3e4f5g6h7j8k9l0m` with the `user_id` from Step 1.

=== "curl"

    ```bash
    curl -X POST https://api.parsify.dev/api/v1/auth/keys \
      -H "Content-Type: application/json" \
      -d '{
        "user_id": "usr_01hx9k2p3e4f5g6h7j8k9l0m",
        "label": "my-first-key"
      }'
    ```

=== "Python"

    ```python
    import httpx

    response = httpx.post(
        "https://api.parsify.dev/api/v1/auth/keys",
        json={
            "user_id": "usr_01hx9k2p3e4f5g6h7j8k9l0m",
            "label": "my-first-key",
        },
    )
    response.raise_for_status()
    api_key = response.json()["data"]["key"]
    print(api_key)  # pk_live_4a8b2c1d9e3f7g5h6i0j
    ```

=== "JavaScript"

    ```js
    const response = await fetch("https://api.parsify.dev/api/v1/auth/keys", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: "usr_01hx9k2p3e4f5g6h7j8k9l0m",
        label: "my-first-key",
      }),
    });

    const { data } = await response.json();
    console.log(data.key); // pk_live_4a8b2c1d9e3f7g5h6i0j
    ```

**Response (201 Created):**

```json
{
  "data": {
    "key_id": "key_9z8y7x6w5v4u3t",
    "key": "pk_live_4a8b2c1d9e3f7g5h6i0j",
    "label": "my-first-key",
    "created_at": "2026-03-23T09:15:44Z"
  }
}
```

!!! warning "Store your key now"
    The full key value is only returned once. Copy it to a secure location such as a password manager or an environment variable before closing this response.

---

## Step 3 — Submit your first scrape

Pass your API key in the `Authorization` header as a Bearer token. The `url` field is the root of the documentation site you want to scrape.

=== "curl"

    ```bash
    curl -X POST https://api.parsify.dev/api/v1/scrape \
      -H "Authorization: Bearer pk_live_4a8b2c1d9e3f7g5h6i0j" \
      -H "Content-Type: application/json" \
      -d '{
        "url": "https://docs.example.com/guides",
        "max_pages": 25,
        "chunk_size": 512,
        "chunk_overlap": 64
      }'
    ```

=== "Python"

    ```python
    import httpx

    API_KEY = "pk_live_4a8b2c1d9e3f7g5h6i0j"

    response = httpx.post(
        "https://api.parsify.dev/api/v1/scrape",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "url": "https://docs.example.com/guides",
            "max_pages": 25,
            "chunk_size": 512,
            "chunk_overlap": 64,
        },
    )
    response.raise_for_status()
    job_id = response.json()["data"]["job_id"]
    print(job_id)  # job_7m6n5o4p3q2r1s
    ```

=== "JavaScript"

    ```js
    const API_KEY = "pk_live_4a8b2c1d9e3f7g5h6i0j";

    const response = await fetch("https://api.parsify.dev/api/v1/scrape", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        url: "https://docs.example.com/guides",
        max_pages: 25,
        chunk_size: 512,
        chunk_overlap: 64,
      }),
    });

    const { data } = await response.json();
    console.log(data.job_id); // job_7m6n5o4p3q2r1s
    ```

**Response (202 Accepted):**

```json
{
  "data": {
    "job_id": "job_7m6n5o4p3q2r1s",
    "status": "pending",
    "url": "https://docs.example.com/guides",
    "max_pages": 25,
    "submitted_at": "2026-03-23T09:17:11Z",
    "message": "Scrape job submitted successfully"
  }
}
```

**Key request fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `url` | string | required | Root URL to scrape |
| `max_pages` | integer | `100` | Maximum pages to crawl |
| `chunk_size` | integer | `512` | Target tokens per chunk |
| `chunk_overlap` | integer | `64` | Overlap tokens between adjacent chunks |
| `follow_links` | boolean | `true` | Recursively follow links within the same domain |

---

## Step 4 — Check job status

Scraping runs asynchronously. Poll the job endpoint until `status` is `completed` or `failed`. For large jobs (500+ pages), polling every 10–30 seconds is appropriate.

=== "curl"

    ```bash
    curl https://api.parsify.dev/api/v1/jobs/job_7m6n5o4p3q2r1s \
      -H "Authorization: Bearer pk_live_4a8b2c1d9e3f7g5h6i0j"
    ```

=== "Python"

    ```python
    import time
    import httpx

    API_KEY = "pk_live_4a8b2c1d9e3f7g5h6i0j"
    JOB_ID = "job_7m6n5o4p3q2r1s"

    with httpx.Client(headers={"Authorization": f"Bearer {API_KEY}"}) as client:
        while True:
            resp = client.get(f"https://api.parsify.dev/api/v1/jobs/{JOB_ID}")
            resp.raise_for_status()
            job = resp.json()["data"]

            print(f"Status: {job['status']}  Pages: {job.get('pages_scraped', 0)}")

            if job["status"] in ("completed", "failed"):
                break

            time.sleep(5)

    if job["status"] == "failed":
        raise RuntimeError(f"Job failed: {job.get('error')}")

    print("Done!", job["result"])
    ```

=== "JavaScript"

    ```js
    const API_KEY = "pk_live_4a8b2c1d9e3f7g5h6i0j";
    const JOB_ID = "job_7m6n5o4p3q2r1s";

    async function pollJob() {
      while (true) {
        const response = await fetch(
          `https://api.parsify.dev/api/v1/jobs/${JOB_ID}`,
          { headers: { Authorization: `Bearer ${API_KEY}` } }
        );
        const { data } = await response.json();

        console.log(`Status: ${data.status}  Pages: ${data.pages_scraped ?? 0}`);

        if (data.status === "completed" || data.status === "failed") {
          return data;
        }

        await new Promise((resolve) => setTimeout(resolve, 5000));
      }
    }

    const job = await pollJob();
    if (job.status === "failed") throw new Error(`Job failed: ${job.error}`);
    console.log("Done!", job.result);
    ```

**Response when running (200 OK):**

```json
{
  "data": {
    "job_id": "job_7m6n5o4p3q2r1s",
    "status": "running",
    "url": "https://docs.example.com/guides",
    "pages_scraped": 12,
    "max_pages": 25,
    "submitted_at": "2026-03-23T09:17:11Z",
    "started_at": "2026-03-23T09:17:14Z"
  }
}
```

**Response when complete (200 OK):**

```json
{
  "data": {
    "job_id": "job_7m6n5o4p3q2r1s",
    "status": "completed",
    "url": "https://docs.example.com/guides",
    "pages_scraped": 25,
    "max_pages": 25,
    "submitted_at": "2026-03-23T09:17:11Z",
    "started_at": "2026-03-23T09:17:14Z",
    "completed_at": "2026-03-23T09:19:03Z",
    "result": {
      "total_pages": 25,
      "total_chunks": 187,
      "result_url": "https://api.parsify.dev/api/v1/jobs/job_7m6n5o4p3q2r1s/result"
    }
  }
}
```

**Job status values:**

| Status | Meaning |
|--------|---------|
| `pending` | Queued, not yet started |
| `running` | Actively crawling and processing |
| `completed` | Finished successfully — results are ready |
| `failed` | Terminated with an error — check the `error` field |

!!! tip "Skip polling with webhooks"
    Pro and Enterprise plans support webhook callbacks. Configure a `webhook_url` in your scrape request and Parsify will POST the completed job to your endpoint automatically. See the [Webhooks guide](guides/webhooks.md).

---

## Step 5 — Download results

Once the job is `completed`, fetch the structured result. The response contains cleaned markdown, semantic chunks, and classification metadata for every scraped page.

=== "curl"

    ```bash
    curl https://api.parsify.dev/api/v1/jobs/job_7m6n5o4p3q2r1s/result \
      -H "Authorization: Bearer pk_live_4a8b2c1d9e3f7g5h6i0j" \
      -o parsify-result.json
    ```

=== "Python"

    ```python
    import json
    import httpx

    API_KEY = "pk_live_4a8b2c1d9e3f7g5h6i0j"
    JOB_ID = "job_7m6n5o4p3q2r1s"

    response = httpx.get(
        f"https://api.parsify.dev/api/v1/jobs/{JOB_ID}/result",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    response.raise_for_status()

    result = response.json()["data"]
    chunks = result["chunks"]

    print(f"Downloaded {len(chunks)} chunks from {result['total_pages']} pages")

    # Load directly into ChromaDB
    import chromadb

    client = chromadb.Client()
    collection = client.create_collection("example-docs")
    collection.add(
        documents=[c["content"] for c in chunks],
        metadatas=[c["metadata"] for c in chunks],
        ids=[c["chunk_id"] for c in chunks],
    )
    print("Loaded into ChromaDB.")
    ```

=== "JavaScript"

    ```js
    import { writeFileSync } from "fs";

    const API_KEY = "pk_live_4a8b2c1d9e3f7g5h6i0j";
    const JOB_ID = "job_7m6n5o4p3q2r1s";

    const response = await fetch(
      `https://api.parsify.dev/api/v1/jobs/${JOB_ID}/result`,
      { headers: { Authorization: `Bearer ${API_KEY}` } }
    );
    const { data } = await response.json();

    console.log(`Downloaded ${data.chunks.length} chunks from ${data.total_pages} pages`);

    // Persist to disk
    writeFileSync("parsify-result.json", JSON.stringify(data, null, 2));
    ```

**Response (200 OK) — truncated for readability:**

```json
{
  "data": {
    "job_id": "job_7m6n5o4p3q2r1s",
    "total_pages": 25,
    "total_chunks": 187,
    "chunks": [
      {
        "chunk_id": "job_7m6n5o4p3q2r1s_chunk_001",
        "content": "# Installation\n\nInstall the package using pip:\n\n```bash\npip install example-sdk\n```\n\nRequires Python 3.8 or higher.",
        "metadata": {
          "source_url": "https://docs.example.com/guides/installation",
          "page_title": "Installation Guide",
          "page_type": "guide",
          "chunk_index": 0,
          "chunk_total": 3,
          "token_count": 48
        }
      },
      {
        "chunk_id": "job_7m6n5o4p3q2r1s_chunk_002",
        "content": "## Configuration\n\nCreate a `.env` file in your project root and set your credentials...",
        "metadata": {
          "source_url": "https://docs.example.com/guides/installation",
          "page_title": "Installation Guide",
          "page_type": "guide",
          "chunk_index": 1,
          "chunk_total": 3,
          "token_count": 61
        }
      }
    ]
  }
}
```

**Chunk metadata fields:**

| Field | Description |
|-------|-------------|
| `chunk_id` | Globally unique chunk identifier |
| `content` | Cleaned markdown content |
| `source_url` | Original page URL |
| `page_title` | Extracted page title |
| `page_type` | GPT-4o classification: `tutorial`, `concept`, `reference`, `guide`, or `changelog` |
| `chunk_index` | Position of this chunk within its source page |
| `chunk_total` | Total chunks produced from this source page |
| `token_count` | Approximate token count for the chunk |

---

## Next Steps

You have scraped your first site and downloaded structured results. Here is where to go next:

- [API Reference](api-reference.md) — Complete endpoint documentation with all request parameters, response schemas, and error codes
- [Authentication Guide](guides/authentication.md) — Manage multiple API keys, rotate credentials, and understand rate limits
- [SDKs](sdks/python.md) — Official Python and JavaScript SDKs with higher-level abstractions over the REST API
