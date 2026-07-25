"""Pydantic request/response models for the Parsify API."""

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, HttpUrl

# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class JobStatus(str, Enum):
    """Status of a scrape/process job."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class BillingTier(str, Enum):
    """Subscription billing tiers."""

    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


# ---------------------------------------------------------------------------
# Scrape models
# ---------------------------------------------------------------------------

class ScrapeRequest(BaseModel):
    """Request body for POST /api/v1/scrape."""

    url: HttpUrl = Field(..., description="Documentation website URL to scrape")
    max_pages: int = Field(
        default=100, ge=1, le=10000, description="Maximum pages to scrape"
    )
    output_format: str = Field(default="markdown", description="Output format")
    webhook_url: HttpUrl | None = Field(
        default=None, description="URL for job completion callback"
    )


class ScrapeResponse(BaseModel):
    """Response body for POST /api/v1/scrape."""

    job_id: str = Field(..., description="Unique job identifier")
    status: JobStatus = Field(default=JobStatus.PENDING)
    message: str = Field(default="Job submitted successfully")
    created_at: datetime


# ---------------------------------------------------------------------------
# Process models (#18)
# ---------------------------------------------------------------------------

class ProcessRequest(BaseModel):
    """Request body for POST /api/v1/process."""

    input_dir: str = Field(
        ..., description="Path to directory containing scraped markdown files"
    )
    use_llm: bool = Field(
        default=False, description="Whether to use LLM for AI classification"
    )
    output_format: str = Field(default="markdown", description="Output format")
    webhook_url: HttpUrl | None = Field(
        default=None, description="URL for job completion callback"
    )


class ProcessResponse(BaseModel):
    """Response body for POST /api/v1/process."""

    job_id: str = Field(..., description="Unique job identifier")
    status: JobStatus = Field(default=JobStatus.PENDING)
    message: str = Field(default="Process job submitted successfully")
    created_at: datetime


# ---------------------------------------------------------------------------
# Job models (#16, #17)
# ---------------------------------------------------------------------------

class JobStatusResponse(BaseModel):
    """Response body for GET /api/v1/jobs/{id}."""

    job_id: str
    status: JobStatus
    job_type: str = "scrape"
    progress: float = Field(
        default=0.0, ge=0.0, le=100.0, description="Progress percentage"
    )
    pages_scraped: int = Field(default=0)
    pages_failed: int = Field(default=0)
    created_at: datetime
    started_at: datetime | None = None
    completed_at: datetime | None = None
    error_message: str | None = None


class JobResultResponse(BaseModel):
    """Response body for GET /api/v1/jobs/{id}/result."""

    job_id: str
    status: JobStatus
    total_pages: int = Field(default=0)
    failed_pages: int = Field(default=0)
    output_files: list[str] = Field(default_factory=list)
    summary: dict[str, Any] | None = None
    completed_at: datetime | None = None


# ---------------------------------------------------------------------------
# Auth models (#20, #21)
# ---------------------------------------------------------------------------

class UserCreateRequest(BaseModel):
    """Request body for POST /api/v1/auth/register."""

    email: str = Field(..., description="User email address")
    name: str | None = Field(default=None, description="Display name")


class UserResponse(BaseModel):
    """User information (public)."""

    user_id: str
    email: str
    name: str | None = None
    tier: BillingTier = BillingTier.FREE
    created_at: datetime


class APIKeyCreateRequest(BaseModel):
    """Request body for POST /api/v1/auth/keys."""

    name: str = Field(..., min_length=1, max_length=100, description="Key label")


class APIKeyResponse(BaseModel):
    """API key info returned at creation (includes full key ONCE)."""

    key_id: str
    name: str
    prefix: str = Field(description="Visible prefix (pk_xxxxxxxx)")
    key: str | None = Field(
        default=None, description="Full API key — shown only at creation"
    )
    created_at: datetime
    is_active: bool = True


class APIKeyListResponse(BaseModel):
    """List of API keys (no full key exposed)."""

    keys: list[APIKeyResponse]
    total: int


# ---------------------------------------------------------------------------
# Billing models (#26, #27, #28, #29)
# ---------------------------------------------------------------------------

class PlanInfo(BaseModel):
    """Billing plan details."""

    tier: BillingTier
    name: str
    requests_per_hour: int
    max_pages_per_request: int
    max_concurrent_jobs: int
    price_monthly_cents: int
    stripe_price_id: str | None = None


class CheckoutRequest(BaseModel):
    """Request body for POST /api/v1/billing/checkout."""

    tier: BillingTier = Field(..., description="Target billing tier")
    success_url: HttpUrl = Field(..., description="Redirect URL on success")
    cancel_url: HttpUrl = Field(..., description="Redirect URL on cancel")


class CheckoutResponse(BaseModel):
    """Response body for POST /api/v1/billing/checkout."""

    checkout_url: str = Field(description="Stripe checkout session URL")
    session_id: str


class SubscriptionResponse(BaseModel):
    """Current subscription status."""

    user_id: str
    tier: BillingTier
    stripe_subscription_id: str | None = None
    current_period_end: datetime | None = None
    is_active: bool = True


# ---------------------------------------------------------------------------
# Usage models (#25, #29, #30)
# ---------------------------------------------------------------------------

class UsageRecord(BaseModel):
    """Single usage event."""

    timestamp: datetime
    endpoint: str
    method: str
    status_code: int
    response_time_ms: float
    key_id: str | None = None


class UsageSummaryResponse(BaseModel):
    """Aggregated usage summary."""

    key_id: str
    tier: BillingTier
    period_start: datetime
    period_end: datetime
    total_requests: int
    requests_limit: int
    pages_scraped: int
    is_over_limit: bool = False
    overage_percentage: float = 0.0


class DailyUsageResponse(BaseModel):
    """Usage breakdown by day."""

    date: str
    request_count: int
    pages_scraped: int
    errors: int


# ---------------------------------------------------------------------------
# Webhook models (#22)
# ---------------------------------------------------------------------------

class WebhookPayload(BaseModel):
    """Payload sent to webhook URLs on job completion."""

    event: str = Field(description="Event type, e.g. 'job.completed'")
    job_id: str
    status: JobStatus
    result: dict[str, Any] | None = None
    timestamp: datetime


# ---------------------------------------------------------------------------
# Standard response wrappers
# ---------------------------------------------------------------------------

class ErrorResponse(BaseModel):
    """Standard error response."""

    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Human-readable error message")
    details: dict[str, Any] | None = None


class MetaResponse(BaseModel):
    """Metadata included in all API responses."""

    request_id: str
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(__import__("datetime").timezone.utc)
    )
    page: int | None = None
    per_page: int | None = None
    total: int | None = None


class APIResponse(BaseModel):
    """Standard API response wrapper."""

    data: Any | None = None
    error: ErrorResponse | None = None
    meta: MetaResponse
