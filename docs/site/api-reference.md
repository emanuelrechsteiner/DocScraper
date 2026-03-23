<!--
Status: ACTIVE
Last Updated: 2026-03-23
Purpose: Complete API reference for the Parsify REST API v1
-->

# API Reference

The Parsify API is a REST API for submitting documentation scrape jobs, processing scraped content, and managing API keys and billing. All endpoints return JSON.

**Base URL:** `https://your-host`

**Interactive docs:** `/api/docs` (Swagger UI) · `/api/redoc` (ReDoc) · `/api/openapi.json`

---

## Response Envelope

Every endpoint (except health checks and the Stripe webhook handler) wraps its payload in a standard envelope.

**Success:**

```json
{
  "data": { ... },
  "error": null,
  "meta": {
    "request_id": "req_4a7f2c910b3d",
    "timestamp": "2026-03-23T14:05:00Z",
    "page": null,
    "per_page": null,
    "total": null
  }
}
```

List endpoints populate `page`, `per_page`, and `total` inside `meta`.

**Error:**

```json
{
  "data": null,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable description",
    "details": { ... }
  },
  "meta": {
    "request_id": "req_4a7f2c910b3d",
    "timestamp": "2026-03-23T14:05:00Z"
  }
}
```

---

## Authentication

Protected endpoints require an API key passed as a Bearer token.

```
Authorization: Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Keys are created via [`POST /api/v1/auth/keys`](#post-apiv1authkeys). The full key is shown **only once** at creation — store it securely.

| Condition | Status | Error code |
|-----------|--------|------------|
| Header absent or malformed | 401 | `UNAUTHORIZED` |
| Key is revoked or does not exist | 401 | `UNAUTHORIZED` |

---

## Rate Limiting

Rate limits are enforced per API key (or per IP for unauthenticated requests). Limits reset at the top of each hour.

| Tier | Requests / hour |
|------|----------------|
| Free | 100 |
| Pro | 1,000 |
| Enterprise | 10,000 |

When the limit is exceeded the API returns **429** with a `Retry-After` header.

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again in 42 seconds.",
    "details": {
      "limit": "100/hour",
      "retry_after": 42
    }
  }
}
```

---

## Endpoints

- [Scraping](#scraping)
- [Processing](#processing)
- [Jobs](#jobs)
- [Auth](#auth)
- [Billing](#billing)
- [Usage](#usage)
- [Health](#health)

---

## Scraping

### POST /api/v1/scrape

Submit a documentation website for asynchronous scraping. The job runs in the background — use [`GET /api/v1/jobs/{job_id}`](#get-apiv1jobsjob_id) to poll its status.

**Authentication:** Required

**Status on success:** `202 Accepted`

#### Request body

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `url` | string (URL) | Yes | — | Documentation website URL |
| `max_pages` | integer | No | `100` | Max pages to scrape (1–10,000) |
| `output_format` | string | No | `"markdown"` | Output format (`"markdown"`) |
| `webhook_url` | string (URL) | No | `null` | Callback URL when the job completes |

=== "curl"

    ```bash
    curl -X POST https://your-host/api/v1/scrape \
      -H "Authorization: Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
      -H "Content-Type: application/json" \
      -d '{
        "url": "https://docs.example.com",
        "max_pages": 500,
        "output_format": "markdown",
        "webhook_url": "https://your-app.com/webhooks/parsify"
      }'
    ```

=== "Python"

    ```python
    import httpx

    response = httpx.post(
        "https://your-host/api/v1/scrape",
        headers={"Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"},
        json={
            "url": "https://docs.example.com",
            "max_pages": 500,
            "output_format": "markdown",
            "webhook_url": "https://your-app.com/webhooks/parsify",
        },
    )
    data = response.json()["data"]
    job_id = data["job_id"]
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch("https://your-host/api/v1/scrape", {
      method: "POST",
      headers: {
        "Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        url: "https://docs.example.com",
        max_pages: 500,
        output_format: "markdown",
        webhook_url: "https://your-app.com/webhooks/parsify",
      }),
    });
    const { data } = await response.json();
    const jobId = data.job_id;
    ```

#### Response `202`

```json
{
  "data": {
    "job_id": "job_1a2b3c4d5e6f",
    "status": "pending",
    "message": "Scrape job submitted successfully",
    "created_at": "2026-03-23T14:05:00Z"
  },
  "error": null,
  "meta": {
    "request_id": "req_4a7f2c910b3d",
    "timestamp": "2026-03-23T14:05:00Z"
  }
}
```

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 401 | `UNAUTHORIZED` | Missing or invalid API key |
| 422 | — | Request body validation failed (FastAPI) |
| 429 | `RATE_LIMIT_EXCEEDED` | Hourly limit exceeded |

---

## Processing

### POST /api/v1/process

Submit a batch of previously scraped Markdown files for cleaning and AI classification. The job runs in the background — poll [`GET /api/v1/jobs/{job_id}`](#get-apiv1jobsjob_id) for status.

**Authentication:** Required

**Status on success:** `202 Accepted`

#### Request body

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `input_dir` | string | Yes | — | Path to a directory of scraped Markdown files |
| `use_llm` | boolean | No | `false` | Run AI classification via GPT-4o |
| `output_format` | string | No | `"markdown"` | Output format (`"markdown"`) |
| `webhook_url` | string (URL) | No | `null` | Callback URL when the job completes |

=== "curl"

    ```bash
    curl -X POST https://your-host/api/v1/process \
      -H "Authorization: Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
      -H "Content-Type: application/json" \
      -d '{
        "input_dir": "/data/scraped/docs-example-com",
        "use_llm": true,
        "output_format": "markdown"
      }'
    ```

=== "Python"

    ```python
    response = httpx.post(
        "https://your-host/api/v1/process",
        headers={"Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"},
        json={
            "input_dir": "/data/scraped/docs-example-com",
            "use_llm": True,
            "output_format": "markdown",
        },
    )
    job_id = response.json()["data"]["job_id"]
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch("https://your-host/api/v1/process", {
      method: "POST",
      headers: {
        "Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        input_dir: "/data/scraped/docs-example-com",
        use_llm: true,
        output_format: "markdown",
      }),
    });
    const { data } = await response.json();
    ```

#### Response `202`

```json
{
  "data": {
    "job_id": "job_7g8h9i0j1k2l",
    "status": "pending",
    "message": "Process job submitted successfully",
    "created_at": "2026-03-23T14:10:00Z"
  },
  "error": null,
  "meta": {
    "request_id": "req_9c3e1d820f5a",
    "timestamp": "2026-03-23T14:10:00Z"
  }
}
```

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 401 | `UNAUTHORIZED` | Missing or invalid API key |
| 422 | — | Request body validation failed |
| 429 | `RATE_LIMIT_EXCEEDED` | Hourly limit exceeded |

---

## Jobs

### GET /api/v1/jobs/{job_id}

Retrieve the current status of any job.

**Authentication:** Required

**Status on success:** `200 OK`

#### Path parameters

| Parameter | Description |
|-----------|-------------|
| `job_id` | Job ID returned by `POST /scrape` or `POST /process` |

=== "curl"

    ```bash
    curl https://your-host/api/v1/jobs/job_1a2b3c4d5e6f \
      -H "Authorization: Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

=== "Python"

    ```python
    import time

    job_id = "job_1a2b3c4d5e6f"
    while True:
        r = httpx.get(
            f"https://your-host/api/v1/jobs/{job_id}",
            headers={"Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"},
        )
        status = r.json()["data"]["status"]
        if status in ("completed", "failed", "cancelled"):
            break
        time.sleep(5)
    ```

=== "JavaScript"

    ```javascript
    async function pollJob(jobId) {
      while (true) {
        const r = await fetch(`https://your-host/api/v1/jobs/${jobId}`, {
          headers: { "Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" },
        });
        const { data } = await r.json();
        if (["completed", "failed", "cancelled"].includes(data.status)) return data;
        await new Promise(resolve => setTimeout(resolve, 5000));
      }
    }
    ```

#### Response `200`

```json
{
  "data": {
    "job_id": "job_1a2b3c4d5e6f",
    "status": "running",
    "job_type": "scrape",
    "progress": 42.5,
    "pages_scraped": 212,
    "pages_failed": 3,
    "created_at": "2026-03-23T14:05:00Z",
    "started_at": "2026-03-23T14:05:02Z",
    "completed_at": null,
    "error_message": null
  },
  "error": null,
  "meta": {
    "request_id": "req_f1e2d3c4b5a6",
    "timestamp": "2026-03-23T14:07:30Z"
  }
}
```

**`status` values:**

| Value | Meaning |
|-------|---------|
| `pending` | Job is queued, not yet started |
| `running` | Job is actively executing |
| `completed` | Job finished successfully |
| `failed` | Job terminated with an error |
| `cancelled` | Job was cancelled before completion |

**`progress`** is a float 0.0–100.0 representing percentage completion.

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 401 | `UNAUTHORIZED` | Missing or invalid API key |
| 404 | `JOB_NOT_FOUND` | No job with that ID |

---

### GET /api/v1/jobs/{job_id}/result

Retrieve the output of a completed or failed job. Returns `409` if the job has not yet reached a terminal state.

**Authentication:** Required

**Status on success:** `200 OK`

=== "curl"

    ```bash
    curl https://your-host/api/v1/jobs/job_1a2b3c4d5e6f/result \
      -H "Authorization: Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

=== "Python"

    ```python
    r = httpx.get(
        "https://your-host/api/v1/jobs/job_1a2b3c4d5e6f/result",
        headers={"Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"},
    )
    result = r.json()["data"]
    print(result["output_files"])
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch("https://your-host/api/v1/jobs/job_1a2b3c4d5e6f/result", {
      headers: { "Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" },
    });
    const { data } = await r.json();
    console.log(data.output_files);
    ```

#### Response `200`

```json
{
  "data": {
    "job_id": "job_1a2b3c4d5e6f",
    "status": "completed",
    "total_pages": 498,
    "failed_pages": 2,
    "output_files": [
      "/data/output/job_1a2b3c4d5e6f/getting-started.md",
      "/data/output/job_1a2b3c4d5e6f/api-reference.md"
    ],
    "summary": {
      "avg_page_size_kb": 14.2,
      "total_tokens_estimated": 318400
    },
    "completed_at": "2026-03-23T14:22:11Z"
  },
  "error": null,
  "meta": {
    "request_id": "req_a1b2c3d4e5f6",
    "timestamp": "2026-03-23T14:25:00Z"
  }
}
```

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 401 | `UNAUTHORIZED` | Missing or invalid API key |
| 404 | `JOB_NOT_FOUND` | No job with that ID |
| 409 | `JOB_NOT_COMPLETE` | Job is still `pending` or `running` |

---

### GET /api/v1/jobs

List jobs with optional filtering and pagination.

**Authentication:** Required

**Status on success:** `200 OK`

#### Query parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `status` | string | — | Filter by job status (`pending`, `running`, `completed`, `failed`, `cancelled`) |
| `limit` | integer | `50` | Results per page (1–100) |
| `offset` | integer | `0` | Pagination offset |

=== "curl"

    ```bash
    # All completed jobs, page 2
    curl "https://your-host/api/v1/jobs?status=completed&limit=20&offset=20" \
      -H "Authorization: Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

=== "Python"

    ```python
    r = httpx.get(
        "https://your-host/api/v1/jobs",
        params={"status": "completed", "limit": 20, "offset": 20},
        headers={"Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"},
    )
    payload = r.json()
    jobs = payload["data"]
    total = payload["meta"]["total"]
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch(
      "https://your-host/api/v1/jobs?status=completed&limit=20&offset=20",
      { headers: { "Authorization": "Bearer pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } }
    );
    const payload = await r.json();
    const jobs = payload.data;
    const total = payload.meta.total;
    ```

#### Response `200`

```json
{
  "data": [
    {
      "job_id": "job_1a2b3c4d5e6f",
      "status": "completed",
      "job_type": "scrape",
      "progress": 100.0,
      "pages_scraped": 498,
      "pages_failed": 2,
      "created_at": "2026-03-23T14:05:00Z",
      "started_at": "2026-03-23T14:05:02Z",
      "completed_at": "2026-03-23T14:22:11Z",
      "error_message": null
    }
  ],
  "error": null,
  "meta": {
    "request_id": "req_b2c3d4e5f6a7",
    "timestamp": "2026-03-23T14:25:00Z",
    "page": 2,
    "per_page": 20,
    "total": 34
  }
}
```

---

## Auth

### POST /api/v1/auth/register

Create a new user account. Returns the user ID needed to create API keys.

**Authentication:** Not required

**Status on success:** `201 Created`

#### Request body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `email` | string | Yes | User email address (must be unique) |
| `name` | string | No | Display name |

=== "curl"

    ```bash
    curl -X POST https://your-host/api/v1/auth/register \
      -H "Content-Type: application/json" \
      -d '{"email": "alice@example.com", "name": "Alice"}'
    ```

=== "Python"

    ```python
    r = httpx.post(
        "https://your-host/api/v1/auth/register",
        json={"email": "alice@example.com", "name": "Alice"},
    )
    user_id = r.json()["data"]["user_id"]
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch("https://your-host/api/v1/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: "alice@example.com", name: "Alice" }),
    });
    const { data } = await r.json();
    const userId = data.user_id;
    ```

#### Response `201`

```json
{
  "data": {
    "user_id": "usr_9z8y7x6w5v4u",
    "email": "alice@example.com",
    "name": "Alice",
    "tier": "free",
    "created_at": "2026-03-23T09:00:00Z"
  },
  "error": null,
  "meta": {
    "request_id": "req_c3d4e5f6a7b8",
    "timestamp": "2026-03-23T09:00:00Z"
  }
}
```

**`tier` values:** `free`, `pro`, `enterprise`

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 409 | `EMAIL_EXISTS` | Email already registered |
| 422 | — | Request body validation failed |

---

### POST /api/v1/auth/keys

Create a new API key for a user. The full key (`pk_...`) is included in this response only — it **cannot be retrieved again**. Store it securely immediately.

**Authentication:** Not required (user identified by `user_id` query parameter)

**Status on success:** `201 Created`

#### Query parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User ID from `POST /auth/register` |

#### Request body

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `name` | string | Yes | 1–100 chars | Human-readable label for the key |

=== "curl"

    ```bash
    curl -X POST "https://your-host/api/v1/auth/keys?user_id=usr_9z8y7x6w5v4u" \
      -H "Content-Type: application/json" \
      -d '{"name": "production"}'
    ```

=== "Python"

    ```python
    r = httpx.post(
        "https://your-host/api/v1/auth/keys",
        params={"user_id": "usr_9z8y7x6w5v4u"},
        json={"name": "production"},
    )
    data = r.json()["data"]
    api_key = data["key"]   # Store this — shown only once
    key_id = data["key_id"]
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch(
      "https://your-host/api/v1/auth/keys?user_id=usr_9z8y7x6w5v4u",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: "production" }),
      }
    );
    const { data } = await r.json();
    const apiKey = data.key; // Store this — shown only once
    ```

#### Response `201`

```json
{
  "data": {
    "key_id": "kid_3m4n5o6p7q8r",
    "name": "production",
    "prefix": "pk_a1b2c3d4",
    "key": "pk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
    "created_at": "2026-03-23T09:05:00Z",
    "is_active": true
  },
  "error": null,
  "meta": {
    "request_id": "req_d4e5f6a7b8c9",
    "timestamp": "2026-03-23T09:05:00Z"
  }
}
```

!!! warning "Key shown once"
    The `key` field is only present in the creation response. Subsequent list calls return `null` for this field. Copy the key to a secure secret store before leaving this response.

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 404 | `USER_NOT_FOUND` | No user with that `user_id` |
| 422 | — | Request body validation failed |

---

### GET /api/v1/auth/keys

List all API keys for a user. Full keys are never returned — only the visible prefix and metadata.

**Authentication:** Not required (user identified by `user_id` query parameter)

**Status on success:** `200 OK`

#### Query parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User ID |

=== "curl"

    ```bash
    curl "https://your-host/api/v1/auth/keys?user_id=usr_9z8y7x6w5v4u"
    ```

=== "Python"

    ```python
    r = httpx.get(
        "https://your-host/api/v1/auth/keys",
        params={"user_id": "usr_9z8y7x6w5v4u"},
    )
    keys = r.json()["data"]["keys"]
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch(
      "https://your-host/api/v1/auth/keys?user_id=usr_9z8y7x6w5v4u"
    );
    const { data } = await r.json();
    const keys = data.keys;
    ```

#### Response `200`

```json
{
  "data": {
    "keys": [
      {
        "key_id": "kid_3m4n5o6p7q8r",
        "name": "production",
        "prefix": "pk_a1b2c3d4",
        "key": null,
        "created_at": "2026-03-23T09:05:00Z",
        "is_active": true
      }
    ],
    "total": 1
  },
  "error": null,
  "meta": {
    "request_id": "req_e5f6a7b8c9d0",
    "timestamp": "2026-03-23T14:00:00Z"
  }
}
```

---

### DELETE /api/v1/auth/keys/{key_id}

Revoke an API key. Revoked keys are immediately rejected by the authentication middleware.

**Authentication:** Not required (ownership verified via `user_id` query parameter)

**Status on success:** `200 OK`

#### Path parameters

| Parameter | Description |
|-----------|-------------|
| `key_id` | Key ID from `POST /auth/keys` or `GET /auth/keys` |

#### Query parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | Must match the key owner |

=== "curl"

    ```bash
    curl -X DELETE \
      "https://your-host/api/v1/auth/keys/kid_3m4n5o6p7q8r?user_id=usr_9z8y7x6w5v4u"
    ```

=== "Python"

    ```python
    r = httpx.delete(
        "https://your-host/api/v1/auth/keys/kid_3m4n5o6p7q8r",
        params={"user_id": "usr_9z8y7x6w5v4u"},
    )
    ```

=== "JavaScript"

    ```javascript
    await fetch(
      "https://your-host/api/v1/auth/keys/kid_3m4n5o6p7q8r?user_id=usr_9z8y7x6w5v4u",
      { method: "DELETE" }
    );
    ```

#### Response `200`

```json
{
  "data": {
    "key_id": "kid_3m4n5o6p7q8r",
    "status": "revoked"
  },
  "error": null,
  "meta": {
    "request_id": "req_f6a7b8c9d0e1",
    "timestamp": "2026-03-23T14:30:00Z"
  }
}
```

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 404 | `KEY_NOT_FOUND` | Key not found or `user_id` does not match the key owner |

---

## Billing

### GET /api/v1/billing/plans

List all available billing plans and their limits. No authentication required.

**Authentication:** Not required

**Status on success:** `200 OK`

=== "curl"

    ```bash
    curl https://your-host/api/v1/billing/plans
    ```

=== "Python"

    ```python
    r = httpx.get("https://your-host/api/v1/billing/plans")
    plans = r.json()["data"]
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch("https://your-host/api/v1/billing/plans");
    const { data: plans } = await r.json();
    ```

#### Response `200`

```json
{
  "data": [
    {
      "tier": "free",
      "name": "Free",
      "description": "For evaluation and small projects",
      "requests_per_hour": 100,
      "max_pages_per_request": 100,
      "max_concurrent_jobs": 2,
      "price_monthly_cents": 0
    },
    {
      "tier": "pro",
      "name": "Pro",
      "description": "For production workloads",
      "requests_per_hour": 1000,
      "max_pages_per_request": 5000,
      "max_concurrent_jobs": 10,
      "price_monthly_cents": 4900
    },
    {
      "tier": "enterprise",
      "name": "Enterprise",
      "description": "For high-volume and enterprise use",
      "requests_per_hour": 10000,
      "max_pages_per_request": 10000,
      "max_concurrent_jobs": 50,
      "price_monthly_cents": 29900
    }
  ],
  "error": null,
  "meta": {
    "request_id": "req_g7a8b9c0d1e2",
    "timestamp": "2026-03-23T14:00:00Z"
  }
}
```

`price_monthly_cents` is in USD cents. Divide by 100 for the dollar amount (e.g. `4900` = $49.00/month).

---

### POST /api/v1/billing/checkout

Create a Stripe Checkout session to upgrade a user's subscription. Returns a redirect URL to the Stripe-hosted payment page. Only `pro` and `enterprise` tiers can be purchased — the `free` tier requires no payment.

**Authentication:** Not required (user identified by `user_id` query parameter)

**Status on success:** `200 OK`

#### Query parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User to upgrade |

#### Request body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `tier` | string | Yes | Target tier: `"pro"` or `"enterprise"` |
| `success_url` | string (URL) | Yes | Redirect URL after successful payment |
| `cancel_url` | string (URL) | Yes | Redirect URL if the user cancels |

=== "curl"

    ```bash
    curl -X POST "https://your-host/api/v1/billing/checkout?user_id=usr_9z8y7x6w5v4u" \
      -H "Content-Type: application/json" \
      -d '{
        "tier": "pro",
        "success_url": "https://your-app.com/billing/success",
        "cancel_url": "https://your-app.com/billing/cancel"
      }'
    ```

=== "Python"

    ```python
    r = httpx.post(
        "https://your-host/api/v1/billing/checkout",
        params={"user_id": "usr_9z8y7x6w5v4u"},
        json={
            "tier": "pro",
            "success_url": "https://your-app.com/billing/success",
            "cancel_url": "https://your-app.com/billing/cancel",
        },
    )
    checkout_url = r.json()["data"]["checkout_url"]
    # Redirect the user to checkout_url
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch(
      "https://your-host/api/v1/billing/checkout?user_id=usr_9z8y7x6w5v4u",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          tier: "pro",
          success_url: "https://your-app.com/billing/success",
          cancel_url: "https://your-app.com/billing/cancel",
        }),
      }
    );
    const { data } = await r.json();
    window.location.href = data.checkout_url;
    ```

#### Response `200`

```json
{
  "data": {
    "checkout_url": "https://checkout.stripe.com/c/pay/cs_live_...",
    "session_id": "cs_live_a1b2c3d4e5f6g7h8i9j0"
  },
  "error": null,
  "meta": {
    "request_id": "req_h8b9c0d1e2f3",
    "timestamp": "2026-03-23T10:00:00Z"
  }
}
```

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 400 | `CHECKOUT_ERROR` | `free` tier requested, Stripe not configured, or no price ID for tier |
| 404 | `USER_NOT_FOUND` | No user with that `user_id` |
| 422 | — | Request body validation failed |

---

### POST /api/v1/billing/webhooks

Receive and process Stripe webhook events. This endpoint is called by Stripe, not by your application. It verifies the `Stripe-Signature` header before processing.

**Authentication:** Stripe webhook signature (not a Bearer token)

**Status on success:** `200 OK`

#### Handled Stripe event types

| Event | Effect |
|-------|--------|
| `checkout.session.completed` | Activates the purchased subscription tier for the user |
| `customer.subscription.updated` | Logs the subscription state change |
| `customer.subscription.deleted` | Downgrades the user to the `free` tier |
| `invoice.payment_failed` | Logs a payment failure warning |

#### Required headers

| Header | Description |
|--------|-------------|
| `Stripe-Signature` | HMAC signature provided by Stripe |

#### Response `200`

```json
{
  "status": "ok",
  "event_type": "checkout.session.completed"
}
```

!!! note
    This endpoint does not use the standard response envelope. It returns a plain JSON object for Stripe compatibility.

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 400 | `WEBHOOK_VERIFICATION_FAILED` | Signature verification failed |
| 400 | `WEBHOOK_ERROR` | Stripe webhook secret not configured |

---

### GET /api/v1/billing/subscription

Get the current subscription status for a user.

**Authentication:** Not required (user identified by `user_id` query parameter)

**Status on success:** `200 OK`

#### Query parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User ID |

=== "curl"

    ```bash
    curl "https://your-host/api/v1/billing/subscription?user_id=usr_9z8y7x6w5v4u"
    ```

=== "Python"

    ```python
    r = httpx.get(
        "https://your-host/api/v1/billing/subscription",
        params={"user_id": "usr_9z8y7x6w5v4u"},
    )
    subscription = r.json()["data"]
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch(
      "https://your-host/api/v1/billing/subscription?user_id=usr_9z8y7x6w5v4u"
    );
    const { data: subscription } = await r.json();
    ```

#### Response `200`

```json
{
  "data": {
    "user_id": "usr_9z8y7x6w5v4u",
    "tier": "pro",
    "stripe_subscription_id": "sub_1AbCdEfGhIjKlMnO",
    "is_active": true
  },
  "error": null,
  "meta": {
    "request_id": "req_i9c0d1e2f3g4",
    "timestamp": "2026-03-23T14:00:00Z"
  }
}
```

#### Error responses

| Status | Code | Condition |
|--------|------|-----------|
| 404 | `USER_NOT_FOUND` | No user with that `user_id` |

---

## Usage

### GET /api/v1/usage

Get the usage summary for the current billing hour. Includes overage warnings when usage approaches or exceeds the tier limit.

**Authentication:** Not required (user identified by `user_id` query parameter)

**Status on success:** `200 OK`

#### Query parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User ID |
| `key_id` | string | No | Specific API key ID (defaults to `user_id`) |

=== "curl"

    ```bash
    curl "https://your-host/api/v1/usage?user_id=usr_9z8y7x6w5v4u"
    ```

=== "Python"

    ```python
    r = httpx.get(
        "https://your-host/api/v1/usage",
        params={"user_id": "usr_9z8y7x6w5v4u"},
    )
    summary = r.json()["data"]
    if summary["overage"]["is_over_soft"]:
        print("Warning:", summary["overage"]["message"])
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch(
      "https://your-host/api/v1/usage?user_id=usr_9z8y7x6w5v4u"
    );
    const { data } = await r.json();
    ```

#### Response `200`

```json
{
  "data": {
    "key_id": "usr_9z8y7x6w5v4u",
    "tier": "free",
    "period_start": "2026-03-23T14:00:00+00:00",
    "period_end": "2026-03-23T14:59:59.999999+00:00",
    "total_requests": 73,
    "requests_limit": 100,
    "pages_scraped": 4210,
    "is_over_limit": false,
    "overage_percentage": 0.0,
    "overage": {
      "current_usage": 73,
      "limit": 100,
      "usage_percentage": 73.0,
      "is_over_soft": false,
      "is_over_hard": false,
      "message": "Approaching limit (73.0% of 100/hr)."
    }
  },
  "error": null,
  "meta": {
    "request_id": "req_j0d1e2f3g4h5",
    "timestamp": "2026-03-23T14:45:00Z"
  }
}
```

**Overage thresholds:**

| `usage_percentage` | `message` |
|--------------------|-----------|
| < 80% | `"Within limits"` |
| 80–119% | `"Approaching limit (N% of X/hr)."` |
| 120–149% | `"Soft limit warning (N% of X/hr). Consider upgrading your plan."` |
| ≥ 150% | `"Hard limit exceeded (N% of X/hr). Requests are blocked. Upgrade your plan."` |

---

### GET /api/v1/usage/daily

Get a day-by-day breakdown of request counts, pages scraped, and errors for the past N days (most recent day first).

**Authentication:** Not required (user identified by `user_id` query parameter)

**Status on success:** `200 OK`

#### Query parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `user_id` | string | — | User ID (required) |
| `key_id` | string | — | Specific API key ID (defaults to `user_id`) |
| `days` | integer | `30` | Number of days to return (1–90) |

=== "curl"

    ```bash
    curl "https://your-host/api/v1/usage/daily?user_id=usr_9z8y7x6w5v4u&days=7"
    ```

=== "Python"

    ```python
    r = httpx.get(
        "https://your-host/api/v1/usage/daily",
        params={"user_id": "usr_9z8y7x6w5v4u", "days": 7},
    )
    breakdown = r.json()["data"]
    ```

=== "JavaScript"

    ```javascript
    const r = await fetch(
      "https://your-host/api/v1/usage/daily?user_id=usr_9z8y7x6w5v4u&days=7"
    );
    const { data: breakdown } = await r.json();
    ```

#### Response `200`

```json
{
  "data": [
    {
      "date": "2026-03-23",
      "request_count": 73,
      "pages_scraped": 4210,
      "errors": 2
    },
    {
      "date": "2026-03-22",
      "request_count": 98,
      "pages_scraped": 7830,
      "errors": 0
    }
  ],
  "error": null,
  "meta": {
    "request_id": "req_k1e2f3g4h5i6",
    "timestamp": "2026-03-23T14:45:00Z"
  }
}
```

Days with no activity are still returned with zero counts.

---

## Health

Health endpoints do not use the standard response envelope and do not require authentication. They are intended for load balancers and container orchestrators.

### GET /health

Liveness probe. Always returns `200`. Reports dependency status and process uptime without gating on them.

=== "curl"

    ```bash
    curl https://your-host/health
    ```

#### Response `200`

```json
{
  "status": "healthy",
  "version": "0.3.0",
  "uptime_seconds": 3742.18,
  "checks": {
    "database": "ok",
    "redis": "ok"
  }
}
```

`checks` values are `"ok"` or `"error"`. The overall HTTP status remains `200` even when a dependency shows `"error"` — use `/ready` for traffic gating.

---

### GET /ready

Readiness probe. Returns `200` only when all required dependencies (database and Redis) are reachable. Returns `503` otherwise.

=== "curl"

    ```bash
    curl --fail https://your-host/ready || echo "Not ready"
    ```

#### Response `200` — all dependencies up

```json
{
  "ready": true,
  "database": true,
  "redis": true
}
```

#### Response `503` — one or more dependencies down

```json
{
  "ready": false,
  "database": true,
  "redis": false
}
```

---

## Webhooks

When a `webhook_url` is supplied in a scrape or process request, Parsify sends a `POST` to that URL when the job reaches a terminal state (`completed`, `failed`, or `cancelled`).

### Payload

```json
{
  "event": "job.completed",
  "job_id": "job_1a2b3c4d5e6f",
  "status": "completed",
  "result": {
    "total_pages": 498,
    "failed_pages": 2,
    "output_files": ["/data/output/job_1a2b3c4d5e6f/getting-started.md"]
  },
  "timestamp": "2026-03-23T14:22:11Z"
}
```

| Field | Description |
|-------|-------------|
| `event` | Always `"job.completed"`, `"job.failed"`, or `"job.cancelled"` |
| `job_id` | The job that finished |
| `status` | Final job status |
| `result` | Same payload as `GET /api/v1/jobs/{job_id}/result` (may be `null` for failed jobs) |
| `timestamp` | ISO 8601 UTC timestamp |

Parsify retries delivery up to **3 times** with a **30-second** timeout per attempt. Your endpoint must return a `2xx` response to acknowledge receipt.

---

## Error Code Reference

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `UNAUTHORIZED` | 401 | Missing or invalid Bearer token |
| `RATE_LIMIT_EXCEEDED` | 429 | Hourly request limit reached |
| `JOB_NOT_FOUND` | 404 | No job with the given ID |
| `JOB_NOT_COMPLETE` | 409 | Result requested before job has finished |
| `EMAIL_EXISTS` | 409 | Email already registered |
| `USER_NOT_FOUND` | 404 | No user with the given ID |
| `KEY_NOT_FOUND` | 404 | API key not found or not owned by the user |
| `CHECKOUT_ERROR` | 400 | Stripe checkout could not be created |
| `WEBHOOK_ERROR` | 400 | Stripe webhook secret not configured |
| `WEBHOOK_VERIFICATION_FAILED` | 400 | Stripe signature verification failed |
