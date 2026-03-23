# Parsify JavaScript SDK

TypeScript/JavaScript client for the [Parsify](https://parsify.dev) documentation processing API.

## Installation

```bash
npm install parsify-sdk
```

## Quick Start

```typescript
import { ParsifyClient } from 'parsify-sdk';

const client = new ParsifyClient({ apiKey: 'pk_your_api_key' });

// Submit a scrape job
const job = await client.scrape({ url: 'https://docs.example.com', maxPages: 50 });
console.log(`Job submitted: ${job.jobId}`);

// Wait for completion
const result = await client.waitForCompletion(job.jobId);
console.log(`Scraped ${result.pagesScraped} pages`);
console.log(`Files: ${result.outputFiles}`);
```
