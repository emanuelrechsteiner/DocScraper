# JavaScript SDK

The official JavaScript/TypeScript client for the Parsify API. Ships with full TypeScript types, async/await support, and automatic job polling.

---

## Installation

=== "npm"

    ```bash
    npm install parsify-sdk
    ```

=== "pnpm"

    ```bash
    pnpm add parsify-sdk
    ```

=== "yarn"

    ```bash
    yarn add parsify-sdk
    ```

Node.js 18+ required. Works in any TypeScript or JavaScript project including Next.js, Bun, and Deno (via npm compat).

---

## Quick Start

```typescript
import { ParsifyClient } from "parsify-sdk";

const client = new ParsifyClient({ apiKey: "pk_your_api_key" });

// Submit a scrape job
const job = await client.scrape("https://docs.example.com", { maxPages: 50 });
console.log(job.jobId); // "job_abc123"

// Wait until the job finishes (polls every 2 seconds)
const result = await client.waitForCompletion(job.jobId);

console.log(`Scraped ${result.totalPages} pages`);
console.log("Output files:", result.outputFiles);
```

---

## Authentication

Pass your API key in the constructor options. The client sends it as a `Bearer` token on every request.

```typescript
const client = new ParsifyClient({ apiKey: "pk_your_api_key" });
```

!!! tip "Environment variable"
    Read the key from an environment variable instead of hard-coding it.

    ```typescript
    const client = new ParsifyClient({
      apiKey: process.env.PARSIFY_API_KEY!,
    });
    ```

---

## Methods Reference

### `scrape`

Submit a documentation scrape job.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `url` | `string` | Yes | — | Documentation site URL to scrape |
| `options.maxPages` | `number` | No | `100` | Maximum pages to crawl (1–10,000) |
| `options.outputFormat` | `string` | No | `"markdown"` | Output format for scraped content |
| `options.webhookUrl` | `string` | No | `undefined` | URL to notify on job completion |

**Returns:** `Promise<Job>`

```typescript
const job = await client.scrape("https://docs.example.com", {
  maxPages: 200,
  webhookUrl: "https://yourapp.com/webhooks/parsify",
});
```

---

### `getJob`

Fetch the current status of a job.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `jobId` | `string` | Yes | Job identifier returned by `scrape` |

**Returns:** `Promise<Job>`

```typescript
const job = await client.getJob("job_abc123");
console.log(job.status);   // "pending" | "running" | "completed" | "failed" | "cancelled"
console.log(job.progress); // 0 – 100
```

---

### `getResult`

Retrieve the result of a completed job. Throws `ParsifyError` with code `JOB_NOT_COMPLETE` if the job has not finished yet.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `jobId` | `string` | Yes | Job identifier |

**Returns:** `Promise<JobResult>`

```typescript
const result = await client.getResult("job_abc123");
console.log(result.totalPages);   // 47
console.log(result.outputFiles);  // ["output/vector_db_index.json", ...]
```

---

### `waitForCompletion`

Poll `getJob` until the job reaches a terminal status (`completed`, `failed`, or `cancelled`), then return the result.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `jobId` | `string` | Yes | — | Job identifier |
| `options.pollInterval` | `number` | No | `2000` | Milliseconds between polls |
| `options.timeout` | `number` | No | `undefined` | Max milliseconds to wait before throwing |

**Returns:** `Promise<JobResult>`

```typescript
// Wait up to 5 minutes
const result = await client.waitForCompletion("job_abc123", {
  pollInterval: 3000,
  timeout: 300_000,
});
```

---

### `listJobs`

Return a paginated list of your jobs.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `options.status` | `JobStatus` | No | `undefined` | Filter by status |
| `options.limit` | `number` | No | `50` | Results per page (1–100) |
| `options.offset` | `number` | No | `0` | Pagination offset |

**Returns:** `Promise<Job[]>`

```typescript
// All running jobs
const running = await client.listJobs({ status: "running" });

// Paginate through completed jobs
const page1 = await client.listJobs({ status: "completed", limit: 20, offset: 0 });
const page2 = await client.listJobs({ status: "completed", limit: 20, offset: 20 });
```

---

## Error Handling

All API errors throw a `ParsifyError`. Inspect `statusCode` for the HTTP status and `code` for the machine-readable error identifier.

```typescript
import { ParsifyClient, ParsifyError } from "parsify-sdk";

const client = new ParsifyClient({ apiKey: "pk_your_api_key" });

try {
  const result = await client.getResult("job_abc123");
} catch (err) {
  if (err instanceof ParsifyError) {
    console.error(err.statusCode); // e.g. 404
    console.error(err.code);       // e.g. "JOB_NOT_FOUND"
    console.error(err.message);    // e.g. "Job job_abc123 not found"
  } else {
    throw err; // re-throw unexpected errors
  }
}
```

### Common error codes

| Code | HTTP | Description |
|------|------|-------------|
| `UNAUTHORIZED` | 401 | Missing or invalid API key |
| `FORBIDDEN` | 403 | Key does not have permission for this resource |
| `JOB_NOT_FOUND` | 404 | No job exists with the given `jobId` |
| `JOB_NOT_COMPLETE` | 409 | `getResult` called before the job finished |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests; respect `Retry-After` header |
| `INTERNAL_ERROR` | 500 | Server-side error; safe to retry with backoff |

---

## TypeScript Types

The SDK ships complete TypeScript types with no extra `@types` package needed.

### `Job`

Represents a scrape job returned by `scrape`, `getJob`, and `listJobs`.

```typescript
interface Job {
  jobId: string;
  status: JobStatus;
  jobType: "scrape" | "process";
  progress: number;          // 0 – 100
  pagesScraped: number;
  pagesFailed: number;
  createdAt: string;         // ISO 8601
  startedAt: string | null;
  completedAt: string | null;
  errorMessage: string | null;
}
```

### `JobStatus`

```typescript
type JobStatus =
  | "pending"
  | "running"
  | "completed"
  | "failed"
  | "cancelled";
```

### `JobResult`

Returned by `getResult` and `waitForCompletion`.

```typescript
interface JobResult {
  jobId: string;
  status: JobStatus;
  totalPages: number;
  failedPages: number;
  outputFiles: string[];
  summary: Record<string, unknown> | null;
  completedAt: string | null;
}
```

### `ScrapeConfig`

Options accepted by `scrape`.

```typescript
interface ScrapeConfig {
  maxPages?: number;       // default: 100
  outputFormat?: string;   // default: "markdown"
  webhookUrl?: string;
}
```

### `ParsifyClientOptions`

Constructor options for `ParsifyClient`.

```typescript
interface ParsifyClientOptions {
  apiKey: string;
  baseUrl?: string;   // default: "https://api.parsify.dev"
  timeout?: number;   // milliseconds, default: 30_000
}
```

---

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `apiKey` | `string` | — | Your Parsify API key (**required**) |
| `baseUrl` | `string` | `"https://api.parsify.dev"` | Override for self-hosted or staging |
| `timeout` | `number` | `30000` | HTTP request timeout in milliseconds |

```typescript
import { ParsifyClient } from "parsify-sdk";

const client = new ParsifyClient({
  apiKey: process.env.PARSIFY_API_KEY!,
  baseUrl: "https://staging.parsify.dev",
  timeout: 60_000,
});
```

---

## Full Working Example

This example scrapes a documentation site, waits for the job, and loads the output into a Pinecone index.

```typescript
import { ParsifyClient, ParsifyError, type JobResult } from "parsify-sdk";
import { Pinecone } from "@pinecone-database/pinecone";
import { readFile } from "node:fs/promises";

interface VectorChunk {
  chunk_id: string;
  content: string;
  metadata: Record<string, string>;
  embedding: number[];
}

async function scrapeAndIndex(url: string, indexName: string): Promise<void> {
  const client = new ParsifyClient({
    apiKey: process.env.PARSIFY_API_KEY!,
  });

  // 1. Submit the job
  console.log(`Submitting scrape job for ${url}…`);
  const job = await client.scrape(url, { maxPages: 200 });
  console.log(`Job submitted: ${job.jobId}`);

  // 2. Wait for completion (up to 10 minutes)
  let result: JobResult;
  try {
    result = await client.waitForCompletion(job.jobId, {
      pollInterval: 5000,
      timeout: 600_000,
    });
  } catch (err) {
    if (err instanceof ParsifyError) {
      console.error(`Job failed: [${err.code}] ${err.message}`);
    } else {
      console.error("Timed out or unexpected error:", err);
    }
    return;
  }

  console.log(`Done. Scraped ${result.totalPages} pages.`);

  // 3. Load vector index
  const vectorIndexPath = result.outputFiles.find((f) =>
    f.endsWith("vector_db_index.json"),
  );
  if (!vectorIndexPath) {
    console.error("No vector index in output.");
    return;
  }

  const chunks: VectorChunk[] = JSON.parse(
    await readFile(vectorIndexPath, "utf8"),
  );

  // 4. Upsert into Pinecone
  const pinecone = new Pinecone({ apiKey: process.env.PINECONE_API_KEY! });
  const index = pinecone.index(indexName);

  await index.upsert(
    chunks.map((chunk) => ({
      id: chunk.chunk_id,
      values: chunk.embedding,
      metadata: { ...chunk.metadata, content: chunk.content },
    })),
  );

  console.log(`Indexed ${chunks.length} chunks into '${indexName}'.`);
}

await scrapeAndIndex("https://docs.example.com", "example-docs");
```

---

## Usage in Next.js

=== "App Router (Server Component)"

    ```typescript
    // app/docs/page.tsx
    import { ParsifyClient } from "parsify-sdk";

    export default async function DocsPage() {
      const client = new ParsifyClient({
        apiKey: process.env.PARSIFY_API_KEY!,
      });

      const jobs = await client.listJobs({ status: "completed", limit: 5 });

      return (
        <ul>
          {jobs.map((job) => (
            <li key={job.jobId}>
              {job.jobId} — {job.pagesScraped} pages
            </li>
          ))}
        </ul>
      );
    }
    ```

=== "Route Handler"

    ```typescript
    // app/api/scrape/route.ts
    import { NextRequest, NextResponse } from "next/server";
    import { ParsifyClient, ParsifyError } from "parsify-sdk";

    export async function POST(request: NextRequest) {
      const { url } = await request.json();

      const client = new ParsifyClient({
        apiKey: process.env.PARSIFY_API_KEY!,
      });

      try {
        const job = await client.scrape(url, { maxPages: 100 });
        return NextResponse.json({ jobId: job.jobId }, { status: 202 });
      } catch (err) {
        if (err instanceof ParsifyError) {
          return NextResponse.json(
            { error: err.code, message: err.message },
            { status: err.statusCode },
          );
        }
        return NextResponse.json({ error: "INTERNAL_ERROR" }, { status: 500 });
      }
    }
    ```
