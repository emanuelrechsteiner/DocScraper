<!--
Status: ACTIVE
Last Updated: 2026-03-23
Purpose: Guide developers through API key authentication — creation, usage, and best practices
-->

# Authentication

Parsify uses **API key authentication** with the HTTP Bearer scheme. Every request to a
protected endpoint must include your API key in the `Authorization` header.

---

## How It Works

When you create an API key, Parsify generates a cryptographically random secret and
stores only its **SHA-256 hash** in the database — the raw key is never persisted. The
key has a short visible prefix (`pk_`) so you can identify it in logs and dashboards
without exposing the full value.

```
Authorization: Bearer pk_a1b2c3d4...
                       ^^^^^^^^^^^^^^^^^
                       Full key (prefix + 64 hex chars)
```

On each request the middleware:

1. Extracts the token from the `Authorization: Bearer` header.
2. Hashes the token with SHA-256.
3. Looks up the hash in the database.
4. Rejects the request with `401 Unauthorized` if the key is missing, inactive, or
   not found.

!!! note "Keys are hashed, not encrypted"
    Because only the hash is stored, a database compromise does not expose your raw
    keys. The trade-off is that **Parsify can never show you the full key again** after
    creation — save it immediately.

---

## Creating an API Key

`POST /api/v1/auth/keys`

### Request

**Headers:**

| Header | Required | Value |
|--------|----------|-------|
| `Content-Type` | Yes | `application/json` |

**Body:**

```json
{
  "name": "Production key"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Human-readable label (1–100 characters) |

### Response

**Success (201):**

```json
{
  "data": {
    "key_id": "key_f3a9b2c1d4e5",
    "name": "Production key",
    "prefix": "pk_f3a9b2c1",
    "key": "pk_f3a9b2c1d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1",
    "created_at": "2026-03-23T10:00:00Z",
    "is_active": true
  },
  "meta": {
    "request_id": "req_a1b2c3d4e5f6",
    "timestamp": "2026-03-23T10:00:00Z"
  }
}
```

!!! warning "Copy your key now"
    The `key` field is returned **only in this response**. Subsequent calls to list
    keys return only the `prefix` and metadata. Store the full key securely before
    closing this response.

### Example

=== "curl"

    ```bash
    curl -X POST https://api.parsify.dev/api/v1/auth/keys \
      -H "Content-Type: application/json" \
      -d '{"name": "Production key"}'
    ```

=== "Python"

    ```python
    import httpx

    response = httpx.post(
        "https://api.parsify.dev/api/v1/auth/keys",
        json={"name": "Production key"},
    )
    data = response.json()["data"]
    api_key = data["key"]   # Save this — shown only once
    key_id = data["key_id"]
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch("https://api.parsify.dev/api/v1/auth/keys", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: "Production key" }),
    });
    const { data } = await response.json();
    const apiKey = data.key;   // Save this — shown only once
    const keyId = data.key_id;
    ```

---

## Using an API Key

Include your key in every request using the `Authorization` header:

```http
Authorization: Bearer pk_f3a9b2c1d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1
```

### Example — Authenticated Scrape Request

=== "curl"

    ```bash
    curl -X POST https://api.parsify.dev/api/v1/scrape \
      -H "Authorization: Bearer $PARSIFY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"url": "https://docs.example.com", "max_pages": 50}'
    ```

=== "Python"

    ```python
    import os
    import httpx

    api_key = os.environ["PARSIFY_API_KEY"]

    response = httpx.post(
        "https://api.parsify.dev/api/v1/scrape",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"url": "https://docs.example.com", "max_pages": 50},
    )
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch("https://api.parsify.dev/api/v1/scrape", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.PARSIFY_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url: "https://docs.example.com", max_pages: 50 }),
    });
    ```

---

## Listing API Keys

`GET /api/v1/auth/keys`

Returns all keys for the authenticated account. Full key values are never included —
only the `prefix` and metadata.

### Response

**Success (200):**

```json
{
  "data": {
    "keys": [
      {
        "key_id": "key_f3a9b2c1d4e5",
        "name": "Production key",
        "prefix": "pk_f3a9b2c1",
        "key": null,
        "created_at": "2026-03-23T10:00:00Z",
        "is_active": true
      },
      {
        "key_id": "key_a0b1c2d3e4f5",
        "name": "CI/CD key",
        "prefix": "pk_a0b1c2d3",
        "key": null,
        "created_at": "2026-03-20T08:30:00Z",
        "is_active": true
      }
    ],
    "total": 2
  },
  "meta": {
    "request_id": "req_b2c3d4e5f6a7",
    "timestamp": "2026-03-23T10:01:00Z"
  }
}
```

### Example

=== "curl"

    ```bash
    curl https://api.parsify.dev/api/v1/auth/keys \
      -H "Authorization: Bearer $PARSIFY_API_KEY"
    ```

=== "Python"

    ```python
    response = httpx.get(
        "https://api.parsify.dev/api/v1/auth/keys",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    keys = response.json()["data"]["keys"]
    ```

---

## Revoking an API Key

`DELETE /api/v1/auth/keys/{key_id}`

Immediately deactivates the key. Any subsequent request using the revoked key returns
`401 Unauthorized`. Revocation is permanent — you cannot reactivate a revoked key.

### Path Parameters

| Parameter | Description |
|-----------|-------------|
| `key_id` | The key ID from the listing response (e.g. `key_f3a9b2c1d4e5`) |

### Response

**Success (200):**

```json
{
  "data": {
    "key_id": "key_f3a9b2c1d4e5",
    "status": "revoked"
  },
  "meta": {
    "request_id": "req_c3d4e5f6a7b8",
    "timestamp": "2026-03-23T10:05:00Z"
  }
}
```

**Error (404) — key not found or not owned by caller:**

```json
{
  "error": {
    "code": "KEY_NOT_FOUND",
    "message": "Key key_f3a9b2c1d4e5 not found or not owned by user"
  },
  "meta": {
    "request_id": "req_d4e5f6a7b8c9",
    "timestamp": "2026-03-23T10:05:01Z"
  }
}
```

### Example

=== "curl"

    ```bash
    curl -X DELETE https://api.parsify.dev/api/v1/auth/keys/key_f3a9b2c1d4e5 \
      -H "Authorization: Bearer $PARSIFY_API_KEY"
    ```

=== "Python"

    ```python
    response = httpx.delete(
        f"https://api.parsify.dev/api/v1/auth/keys/{key_id}",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    ```

---

## Error Responses

### 401 Unauthorized

Returned when the `Authorization` header is missing, malformed, or the key is invalid
or revoked.

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Missing or invalid API key. Include: Authorization: Bearer pk_..."
  },
  "meta": {
    "request_id": "req_e5f6a7b8c9d0",
    "timestamp": "2026-03-23T10:06:00Z"
  }
}
```

The response also includes a `WWW-Authenticate: Bearer` header to indicate the
expected scheme.

**Common causes:**

| Symptom | Likely cause |
|---------|-------------|
| No `Authorization` header | Header was not sent |
| `Bearer` prefix missing | Key sent as raw value without `Bearer ` prefix |
| `401` immediately after key creation | Key was copied with leading/trailing whitespace |
| `401` on a previously working key | Key was revoked or the account was suspended |

---

## Best Practices

!!! tip "Use environment variables — never hardcode keys"
    ```bash
    # .env
    PARSIFY_API_KEY=pk_f3a9b2c1...
    ```
    ```python
    import os
    api_key = os.environ["PARSIFY_API_KEY"]
    ```
    Add `.env` to `.gitignore` and use secrets management in CI/CD pipelines
    (e.g. GitHub Actions secrets, AWS Secrets Manager).

**Rotation schedule**

- Rotate keys at least every 90 days, or immediately after any suspected exposure.
- Create the new key first, update all clients, then revoke the old key — this avoids
  downtime.

**Principle of least privilege**

- Create separate keys for each environment (development, staging, production) and
  each service or CI job.
- This limits blast radius: if one key is compromised, you can revoke it without
  disrupting unrelated consumers.

**Audit your keys periodically**

- Use `GET /api/v1/auth/keys` to review active keys.
- Revoke any key that is no longer in use.

!!! warning "Never log your API key"
    HTTP client libraries sometimes log request headers for debugging. Ensure your
    production log configuration redacts `Authorization` headers before writing to
    any log sink.
