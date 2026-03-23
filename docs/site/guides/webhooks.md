<!--
Status: ACTIVE
Last Updated: 2026-03-23
Purpose: Guide developers through webhook setup, payload format, retry behaviour, and handler implementation
-->

# Webhooks

Webhooks let you receive real-time notifications when an asynchronous job finishes.
Instead of polling `GET /api/v1/jobs/{id}`, you provide a URL and Parsify will POST a
structured payload to it the moment the job completes or fails.

---

## How Webhooks Work

1. You include a `webhook_url` field when submitting a scrape or process job.
2. Parsify runs the job asynchronously in the background.
3. When the job reaches a terminal state (`completed` or `failed`), Parsify sends an
   HTTP `POST` to your URL with a JSON payload.
4. Your endpoint must respond with a `2xx` status code within 30 seconds.
5. If the delivery fails, Parsify retries automatically (see [Retry Logic](#retry-logic)).

!!! note "Webhooks are optional"
    Webhooks are not required. If you omit `webhook_url`, the job runs normally and you
    can poll for status using `GET /api/v1/jobs/{id}`.

---

## Events

| Event | Fired when |
|-------|-----------|
| `job.completed` | The job finished successfully |
| `job.failed` | The job encountered a fatal error and will not be retried |

---

## Setting Up a Webhook

Include `webhook_url` in the request body when submitting a job.

### Scrape Job with Webhook

`POST /api/v1/scrape`

```json
{
  "url": "https://docs.example.com",
  "max_pages": 100,
  "webhook_url": "https://yourapp.example.com/webhooks/parsify"
}
```

### Process Job with Webhook

`POST /api/v1/process`

```json
{
  "input_dir": "/data/scraped/docs-example-com",
  "use_llm": true,
  "webhook_url": "https://yourapp.example.com/webhooks/parsify"
}
```

Both endpoints accept `webhook_url` as an optional `HttpUrl` field. Parsify validates
that the URL is well-formed at submission time — an invalid URL returns `422`.

---

## Payload Format

Parsify sends the same envelope for both event types; the `event` field distinguishes
them.

### job.completed

```json
{
  "event": "job.completed",
  "job_id": "job_abc123def456",
  "status": "completed",
  "result": {
    "pages_scraped": 42,
    "output_files": [
      "output/docs-example-com/index.md",
      "output/docs-example-com/api-reference.md"
    ]
  },
  "timestamp": "2026-03-23T10:30:00Z"
}
```

### job.failed

```json
{
  "event": "job.failed",
  "job_id": "job_abc123def456",
  "status": "failed",
  "result": {
    "error": "Target site returned 403 Forbidden after 3 retries"
  },
  "timestamp": "2026-03-23T10:30:00Z"
}
```

### Field Reference

| Field | Type | Description |
|-------|------|-------------|
| `event` | string | `"job.completed"` or `"job.failed"` |
| `job_id` | string | Unique job identifier matching the submission response |
| `status` | string | Final job status (`completed` or `failed`) |
| `result` | object | Event-specific data; `null` if no result is available |
| `timestamp` | string | ISO 8601 UTC timestamp of the event |

!!! note "Request headers"
    Parsify sends the following headers with every webhook delivery:

    | Header | Value |
    |--------|-------|
    | `Content-Type` | `application/json` |
    | `User-Agent` | `Parsify-Webhook/1.0` |

---

## Retry Logic

If your endpoint does not return a `2xx` response within 30 seconds (configurable via
`PARSIFY_WEBHOOK_TIMEOUT`), Parsify treats the delivery as failed and retries using
**exponential backoff**:

| Attempt | Delay before retry |
|---------|--------------------|
| 1 (initial) | — |
| 2 | ~1 second |
| 3 | ~2 seconds |

After 3 total attempts (1 initial + 2 retries) the delivery is abandoned and the
failure is logged server-side. The job itself is not affected — a webhook delivery
failure does not change the job's status.

!!! warning "Ensure your endpoint is idempotent"
    Because Parsify may deliver the same event more than once on transient failures,
    your handler must be idempotent. Use `job_id` as a deduplication key — if you have
    already processed a given `job_id`, discard the duplicate delivery silently.

---

## Best Practices

**Respond quickly, process asynchronously**

Your endpoint must return `200 OK` within 30 seconds. If your processing logic takes
longer, acknowledge the webhook immediately and push the payload onto a queue or
background task for later processing.

**Verify the payload belongs to you**

Cross-check `job_id` against jobs you actually submitted to avoid processing
deliveries intended for a different account or stray test calls.

**Use HTTPS endpoints**

Parsify will attempt delivery to any valid HTTPS URL. Plain `http://` URLs are
accepted during development but should not be used in production.

**Log raw payloads for debugging**

Store the raw JSON body alongside the parsed result so you can replay deliveries
during debugging without re-running jobs.

---

## Example Webhook Handler

The examples below show a minimal handler that acknowledges the webhook immediately
and dispatches processing to a background task.

=== "FastAPI"

    ```python
    from fastapi import FastAPI, BackgroundTasks, Request, Response
    import logging

    app = FastAPI()
    logger = logging.getLogger(__name__)


    async def process_webhook_event(event: str, job_id: str, payload: dict) -> None:
        """Background task — process after responding 200."""
        if event == "job.completed":
            logger.info("Job %s completed: %s", job_id, payload.get("result"))
            # e.g. update database, notify users, trigger downstream pipeline
        elif event == "job.failed":
            error = payload.get("result", {}).get("error", "unknown error")
            logger.error("Job %s failed: %s", job_id, error)


    @app.post("/webhooks/parsify", status_code=200)
    async def parsify_webhook(request: Request, background_tasks: BackgroundTasks):
        payload = await request.json()

        event = payload.get("event")
        job_id = payload.get("job_id")

        if not event or not job_id:
            # Return 200 anyway — malformed payloads should not trigger retries
            return {"status": "ignored"}

        # Acknowledge immediately, then process in the background
        background_tasks.add_task(process_webhook_event, event, job_id, payload)
        return {"status": "accepted"}
    ```

=== "Flask"

    ```python
    from flask import Flask, request, jsonify
    from threading import Thread
    import logging

    app = Flask(__name__)
    logger = logging.getLogger(__name__)


    def process_webhook_event(event: str, job_id: str, payload: dict) -> None:
        """Background thread — process after responding 200."""
        if event == "job.completed":
            logger.info("Job %s completed: %s", job_id, payload.get("result"))
            # e.g. update database, notify users, trigger downstream pipeline
        elif event == "job.failed":
            error = payload.get("result", {}).get("error", "unknown error")
            logger.error("Job %s failed: %s", job_id, error)


    @app.post("/webhooks/parsify")
    def parsify_webhook():
        payload = request.get_json(silent=True) or {}

        event = payload.get("event")
        job_id = payload.get("job_id")

        if not event or not job_id:
            return jsonify({"status": "ignored"}), 200

        # Acknowledge immediately, then process in a background thread
        Thread(target=process_webhook_event, args=(event, job_id, payload)).start()
        return jsonify({"status": "accepted"}), 200
    ```

!!! tip "Production recommendation: use a task queue"
    For production workloads, replace the inline thread/background task with a proper
    task queue such as Celery, RQ, or Dramatiq. This gives you persistence, visibility,
    and retry semantics for your own processing logic — independent of Parsify's
    delivery retries.

---

## Testing Webhooks Locally

During development, expose your local server using a tunneling tool so Parsify can
reach it:

```bash
# Using ngrok
ngrok http 8000

# The tunnel URL (e.g. https://abc123.ngrok.io) is your webhook_url
```

Then submit a test job with your tunnel URL:

```bash
curl -X POST https://api.parsify.dev/api/v1/scrape \
  -H "Authorization: Bearer $PARSIFY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://docs.example.com",
    "max_pages": 1,
    "webhook_url": "https://abc123.ngrok.io/webhooks/parsify"
  }'
```

!!! note "Local tunnels"
    [ngrok](https://ngrok.com), [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/),
    and [localtunnel](https://theboroer.github.io/localtunnel-www/) all work.
    Choose whichever you already have available.
