export enum JobStatus {
  PENDING = 'pending',
  RUNNING = 'running',
  COMPLETED = 'completed',
  FAILED = 'failed',
  CANCELLED = 'cancelled',
}

export interface ScrapeConfig {
  url: string;
  maxPages?: number;
  outputFormat?: string;
  webhookUrl?: string;
}

export interface Job {
  jobId: string;
  status: JobStatus;
  jobType: string;
  progress: number;
  pagesScraped: number;
  pagesFailed: number;
  createdAt?: string;
  startedAt?: string;
  completedAt?: string;
  errorMessage?: string;
  outputFiles: string[];
  summary?: Record<string, unknown>;
}

export class ParsifyError extends Error {
  statusCode?: number;
  code?: string;

  constructor(message: string, statusCode?: number, code?: string) {
    super(message);
    this.name = 'ParsifyError';
    this.statusCode = statusCode;
    this.code = code;
  }
}
