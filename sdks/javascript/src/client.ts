import { Job, JobStatus, ParsifyError, ScrapeConfig } from './types';

const DEFAULT_BASE_URL = 'https://api.parsify.dev';
const DEFAULT_TIMEOUT = 30000;
const DEFAULT_POLL_INTERVAL = 5000;

interface ClientOptions {
  apiKey: string;
  baseUrl?: string;
  timeout?: number;
}

function parseJob(data: Record<string, unknown>): Job {
  return {
    jobId: data.job_id as string,
    status: data.status as JobStatus,
    jobType: (data.job_type as string) || 'scrape',
    progress: (data.progress as number) || 0,
    pagesScraped: (data.pages_scraped as number) || 0,
    pagesFailed: (data.pages_failed as number) || 0,
    createdAt: data.created_at as string | undefined,
    startedAt: data.started_at as string | undefined,
    completedAt: data.completed_at as string | undefined,
    errorMessage: data.error_message as string | undefined,
    outputFiles: (data.output_files as string[]) || [],
    summary: data.summary as Record<string, unknown> | undefined,
  };
}

export class ParsifyClient {
  private apiKey: string;
  private baseUrl: string;
  private timeout: number;

  constructor(options: ClientOptions) {
    this.apiKey = options.apiKey;
    this.baseUrl = (options.baseUrl || DEFAULT_BASE_URL).replace(/\/$/, '');
    this.timeout = options.timeout || DEFAULT_TIMEOUT;
  }

  private async request(method: string, path: string, body?: unknown): Promise<Record<string, unknown>> {
    const url = `${this.baseUrl}${path}`;
    const headers: Record<string, string> = {
      'Authorization': `Bearer ${this.apiKey}`,
      'Content-Type': 'application/json',
    };

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);

    try {
      const response = await fetch(url, {
        method,
        headers,
        body: body ? JSON.stringify(body) : undefined,
        signal: controller.signal,
      });

      const json = await response.json() as Record<string, unknown>;

      if (!response.ok) {
        const error = (json.error || json.detail || {}) as Record<string, unknown>;
        const msg = typeof error === 'object' ? (error.message as string) || JSON.stringify(error) : String(error);
        throw new ParsifyError(msg, response.status, (error as Record<string, unknown>)?.code as string);
      }

      return (json.data || json) as Record<string, unknown>;
    } finally {
      clearTimeout(timeoutId);
    }
  }

  async scrape(config: ScrapeConfig): Promise<Job> {
    const payload: Record<string, unknown> = {
      url: config.url,
      max_pages: config.maxPages || 100,
      output_format: config.outputFormat || 'markdown',
    };
    if (config.webhookUrl) {
      payload.webhook_url = config.webhookUrl;
    }
    const data = await this.request('POST', '/api/v1/scrape', payload);
    return parseJob(data);
  }

  async getJob(jobId: string): Promise<Job> {
    const data = await this.request('GET', `/api/v1/jobs/${jobId}`);
    return parseJob(data);
  }

  async getResult(jobId: string): Promise<Job> {
    const data = await this.request('GET', `/api/v1/jobs/${jobId}/result`);
    return parseJob(data);
  }

  async waitForCompletion(jobId: string, options?: { pollInterval?: number; timeout?: number }): Promise<Job> {
    const pollInterval = options?.pollInterval || DEFAULT_POLL_INTERVAL;
    const timeout = options?.timeout || 1800000;
    const start = Date.now();

    while (true) {
      const job = await this.getJob(jobId);
      if (job.status === JobStatus.COMPLETED) {
        return this.getResult(jobId);
      }
      if (job.status === JobStatus.FAILED) {
        throw new ParsifyError(`Job ${jobId} failed: ${job.errorMessage}`, undefined, 'JOB_FAILED');
      }
      if (Date.now() - start > timeout) {
        throw new ParsifyError(`Job ${jobId} timed out after ${timeout}ms`, undefined, 'TIMEOUT');
      }
      await new Promise(resolve => setTimeout(resolve, pollInterval));
    }
  }

  async listJobs(options?: { status?: string; limit?: number }): Promise<Job[]> {
    const params = new URLSearchParams();
    if (options?.status) params.set('status', options.status);
    if (options?.limit) params.set('limit', String(options.limit));
    const query = params.toString() ? `?${params.toString()}` : '';
    const data = await this.request('GET', `/api/v1/jobs${query}`);
    if (Array.isArray(data)) {
      return data.map(d => parseJob(d as Record<string, unknown>));
    }
    return [];
  }
}
