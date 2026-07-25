"""Tests for Pydantic request/response schemas in api/models/schemas.py."""

from __future__ import annotations

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from api.models.schemas import (
    APIKeyCreateRequest,
    APIKeyListResponse,
    APIKeyResponse,
    APIResponse,
    BillingTier,
    CheckoutRequest,
    ErrorResponse,
    JobResultResponse,
    JobStatus,
    JobStatusResponse,
    MetaResponse,
    PlanInfo,
    ProcessRequest,
    ProcessResponse,
    ScrapeRequest,
    ScrapeResponse,
    UsageSummaryResponse,
    UserCreateRequest,
    UserResponse,
    WebhookPayload,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _now() -> datetime:
    return datetime.now(UTC)


# ---------------------------------------------------------------------------
# JobStatus enum
# ---------------------------------------------------------------------------

class TestJobStatus:
    """Tests for JobStatus enum."""

    def test_all_values_exist(self) -> None:
        assert JobStatus.PENDING == "pending"
        assert JobStatus.RUNNING == "running"
        assert JobStatus.COMPLETED == "completed"
        assert JobStatus.FAILED == "failed"
        assert JobStatus.CANCELLED == "cancelled"

    def test_five_members(self) -> None:
        assert len(list(JobStatus)) == 5

    def test_is_str_subclass(self) -> None:
        assert isinstance(JobStatus.PENDING, str)

    def test_accepts_lowercase_string_in_model(self) -> None:
        """Models using JobStatus should accept its string value."""
        response = ScrapeResponse(
            job_id="abc",
            status=JobStatus.RUNNING,
            created_at=_now(),
        )
        assert response.status == JobStatus.RUNNING

    def test_invalid_value_raises(self) -> None:
        with pytest.raises(ValidationError):
            ScrapeResponse(job_id="x", status="unknown", created_at=_now())


# ---------------------------------------------------------------------------
# BillingTier enum
# ---------------------------------------------------------------------------

class TestBillingTier:
    """Tests for BillingTier enum."""

    def test_all_values_exist(self) -> None:
        assert BillingTier.FREE == "free"
        assert BillingTier.PRO == "pro"
        assert BillingTier.ENTERPRISE == "enterprise"

    def test_three_members(self) -> None:
        assert len(list(BillingTier)) == 3

    def test_is_str_subclass(self) -> None:
        assert isinstance(BillingTier.FREE, str)

    def test_invalid_tier_raises(self) -> None:
        with pytest.raises(ValidationError):
            UserResponse(
                user_id="u1",
                email="a@b.com",
                tier="premium",
                created_at=_now(),
            )


# ---------------------------------------------------------------------------
# ScrapeRequest
# ---------------------------------------------------------------------------

class TestScrapeRequest:
    """Tests for ScrapeRequest model."""

    def test_valid_http_url(self) -> None:
        req = ScrapeRequest(url="http://example.com")
        assert str(req.url).startswith("http://")

    def test_valid_https_url(self) -> None:
        req = ScrapeRequest(url="https://docs.example.com/guide")
        assert "https" in str(req.url)

    def test_max_pages_default(self) -> None:
        req = ScrapeRequest(url="https://example.com")
        assert req.max_pages == 100

    def test_output_format_default(self) -> None:
        req = ScrapeRequest(url="https://example.com")
        assert req.output_format == "markdown"

    def test_webhook_url_defaults_to_none(self) -> None:
        req = ScrapeRequest(url="https://example.com")
        assert req.webhook_url is None

    def test_max_pages_lower_boundary(self) -> None:
        req = ScrapeRequest(url="https://example.com", max_pages=1)
        assert req.max_pages == 1

    def test_max_pages_upper_boundary(self) -> None:
        req = ScrapeRequest(url="https://example.com", max_pages=10000)
        assert req.max_pages == 10000

    def test_max_pages_below_minimum_raises(self) -> None:
        with pytest.raises(ValidationError):
            ScrapeRequest(url="https://example.com", max_pages=0)

    def test_max_pages_above_maximum_raises(self) -> None:
        with pytest.raises(ValidationError):
            ScrapeRequest(url="https://example.com", max_pages=10001)

    def test_invalid_url_scheme_raises(self) -> None:
        with pytest.raises(ValidationError):
            ScrapeRequest(url="ftp://example.com")

    def test_bare_string_not_url_raises(self) -> None:
        with pytest.raises(ValidationError):
            ScrapeRequest(url="not-a-url")

    def test_missing_url_raises(self) -> None:
        with pytest.raises(ValidationError):
            ScrapeRequest()  # type: ignore[call-arg]

    def test_optional_webhook_url_accepted(self) -> None:
        req = ScrapeRequest(
            url="https://example.com",
            webhook_url="https://hooks.example.com/callback",
        )
        assert req.webhook_url is not None

    def test_invalid_webhook_url_raises(self) -> None:
        with pytest.raises(ValidationError):
            ScrapeRequest(url="https://example.com", webhook_url="not-a-url")

    def test_custom_output_format(self) -> None:
        req = ScrapeRequest(url="https://example.com", output_format="json")
        assert req.output_format == "json"

    def test_model_serialisation(self) -> None:
        req = ScrapeRequest(url="https://example.com", max_pages=50)
        data = req.model_dump()
        assert data["max_pages"] == 50
        assert data["output_format"] == "markdown"


# ---------------------------------------------------------------------------
# ProcessRequest
# ---------------------------------------------------------------------------

class TestProcessRequest:
    """Tests for ProcessRequest model."""

    def test_valid_input_dir(self) -> None:
        req = ProcessRequest(input_dir="/tmp/docs")
        assert req.input_dir == "/tmp/docs"

    def test_use_llm_defaults_to_false(self) -> None:
        req = ProcessRequest(input_dir="/tmp/docs")
        assert req.use_llm is False

    def test_output_format_defaults_to_markdown(self) -> None:
        req = ProcessRequest(input_dir="/tmp/docs")
        assert req.output_format == "markdown"

    def test_webhook_url_defaults_to_none(self) -> None:
        req = ProcessRequest(input_dir="/tmp/docs")
        assert req.webhook_url is None

    def test_missing_input_dir_raises(self) -> None:
        with pytest.raises(ValidationError):
            ProcessRequest()  # type: ignore[call-arg]

    def test_optional_webhook_accepted(self) -> None:
        req = ProcessRequest(
            input_dir="/tmp",
            webhook_url="https://example.com/cb",
        )
        assert req.webhook_url is not None

    def test_use_llm_true(self) -> None:
        req = ProcessRequest(input_dir="/tmp", use_llm=True)
        assert req.use_llm is True

    def test_model_serialisation(self) -> None:
        req = ProcessRequest(input_dir="/data", output_format="json")
        data = req.model_dump()
        assert data["input_dir"] == "/data"
        assert data["output_format"] == "json"


# ---------------------------------------------------------------------------
# UserCreateRequest
# ---------------------------------------------------------------------------

class TestUserCreateRequest:
    """Tests for UserCreateRequest model."""

    def test_valid_email_only(self) -> None:
        req = UserCreateRequest(email="user@example.com")
        assert req.email == "user@example.com"

    def test_name_defaults_to_none(self) -> None:
        req = UserCreateRequest(email="user@example.com")
        assert req.name is None

    def test_name_provided(self) -> None:
        req = UserCreateRequest(email="user@example.com", name="Alice")
        assert req.name == "Alice"

    def test_missing_email_raises(self) -> None:
        with pytest.raises(ValidationError):
            UserCreateRequest()  # type: ignore[call-arg]

    def test_email_is_plain_string_field(self) -> None:
        """email is declared as str, not EmailStr, so any non-empty string passes."""
        req = UserCreateRequest(email="anything")
        assert req.email == "anything"

    def test_serialisation(self) -> None:
        req = UserCreateRequest(email="a@b.com", name="Bob")
        data = req.model_dump()
        assert data["email"] == "a@b.com"
        assert data["name"] == "Bob"


# ---------------------------------------------------------------------------
# APIKeyCreateRequest
# ---------------------------------------------------------------------------

class TestAPIKeyCreateRequest:
    """Tests for APIKeyCreateRequest model."""

    def test_valid_name(self) -> None:
        req = APIKeyCreateRequest(name="production-key")
        assert req.name == "production-key"

    def test_single_char_name(self) -> None:
        req = APIKeyCreateRequest(name="x")
        assert req.name == "x"

    def test_max_length_name(self) -> None:
        req = APIKeyCreateRequest(name="a" * 100)
        assert len(req.name) == 100

    def test_empty_name_raises(self) -> None:
        with pytest.raises(ValidationError):
            APIKeyCreateRequest(name="")

    def test_name_exceeding_max_length_raises(self) -> None:
        with pytest.raises(ValidationError):
            APIKeyCreateRequest(name="a" * 101)

    def test_missing_name_raises(self) -> None:
        with pytest.raises(ValidationError):
            APIKeyCreateRequest()  # type: ignore[call-arg]

    def test_serialisation(self) -> None:
        req = APIKeyCreateRequest(name="my-key")
        data = req.model_dump()
        assert data["name"] == "my-key"


# ---------------------------------------------------------------------------
# ErrorResponse
# ---------------------------------------------------------------------------

class TestErrorResponse:
    """Tests for ErrorResponse model."""

    def test_valid_error(self) -> None:
        err = ErrorResponse(code="NOT_FOUND", message="Resource not found")
        assert err.code == "NOT_FOUND"
        assert err.message == "Resource not found"

    def test_details_defaults_to_none(self) -> None:
        err = ErrorResponse(code="ERR", message="Something broke")
        assert err.details is None

    def test_details_with_dict(self) -> None:
        err = ErrorResponse(
            code="VALIDATION_ERROR",
            message="Invalid input",
            details={"field": "url", "issue": "invalid format"},
        )
        assert err.details is not None
        assert err.details["field"] == "url"

    def test_missing_code_raises(self) -> None:
        with pytest.raises(ValidationError):
            ErrorResponse(message="oops")  # type: ignore[call-arg]

    def test_missing_message_raises(self) -> None:
        with pytest.raises(ValidationError):
            ErrorResponse(code="ERR")  # type: ignore[call-arg]

    def test_serialisation(self) -> None:
        err = ErrorResponse(code="X", message="Y", details={"k": "v"})
        data = err.model_dump()
        assert data["code"] == "X"
        assert data["details"] == {"k": "v"}


# ---------------------------------------------------------------------------
# APIResponse (generic wrapper)
# ---------------------------------------------------------------------------

class TestAPIResponse:
    """Tests for APIResponse generic wrapper."""

    def _make_meta(self) -> MetaResponse:
        return MetaResponse(request_id="req-123")

    def test_data_field_accepts_any_value(self) -> None:
        resp = APIResponse(data={"key": "value"}, meta=self._make_meta())
        assert resp.data == {"key": "value"}

    def test_data_defaults_to_none(self) -> None:
        resp = APIResponse(meta=self._make_meta())
        assert resp.data is None

    def test_error_defaults_to_none(self) -> None:
        resp = APIResponse(meta=self._make_meta())
        assert resp.error is None

    def test_error_field_accepts_error_response(self) -> None:
        err = ErrorResponse(code="E", message="err")
        resp = APIResponse(error=err, meta=self._make_meta())
        assert resp.error is not None
        assert resp.error.code == "E"

    def test_meta_required(self) -> None:
        with pytest.raises(ValidationError):
            APIResponse(data="something")  # type: ignore[call-arg]

    def test_meta_auto_timestamp(self) -> None:
        meta = MetaResponse(request_id="req-abc")
        assert meta.timestamp is not None
        assert isinstance(meta.timestamp, datetime)

    def test_meta_pagination_fields_default_to_none(self) -> None:
        meta = MetaResponse(request_id="req-xyz")
        assert meta.page is None
        assert meta.per_page is None
        assert meta.total is None

    def test_meta_with_pagination(self) -> None:
        meta = MetaResponse(request_id="r", page=2, per_page=10, total=100)
        assert meta.page == 2
        assert meta.per_page == 10
        assert meta.total == 100

    def test_data_with_list(self) -> None:
        resp = APIResponse(data=[1, 2, 3], meta=self._make_meta())
        assert resp.data == [1, 2, 3]

    def test_data_with_nested_model(self) -> None:
        err_model = ErrorResponse(code="C", message="M")
        resp = APIResponse(data=err_model.model_dump(), meta=self._make_meta())
        assert resp.data["code"] == "C"

    def test_serialisation_round_trip(self) -> None:
        meta = MetaResponse(request_id="req-1")
        resp = APIResponse(data={"result": 42}, meta=meta)
        data = resp.model_dump()
        assert data["data"]["result"] == 42
        assert data["error"] is None
        assert data["meta"]["request_id"] == "req-1"


# ---------------------------------------------------------------------------
# ScrapeResponse
# ---------------------------------------------------------------------------

class TestScrapeResponse:
    """Tests for ScrapeResponse model."""

    def test_valid_creation(self) -> None:
        resp = ScrapeResponse(job_id="job-1", created_at=_now())
        assert resp.job_id == "job-1"
        assert resp.status == JobStatus.PENDING
        assert resp.message == "Job submitted successfully"

    def test_custom_status(self) -> None:
        resp = ScrapeResponse(
            job_id="job-2", status=JobStatus.RUNNING, created_at=_now()
        )
        assert resp.status == JobStatus.RUNNING


# ---------------------------------------------------------------------------
# ProcessResponse
# ---------------------------------------------------------------------------

class TestProcessResponse:
    """Tests for ProcessResponse model."""

    def test_valid_creation(self) -> None:
        resp = ProcessResponse(job_id="pjob-1", created_at=_now())
        assert resp.status == JobStatus.PENDING
        assert resp.message == "Process job submitted successfully"


# ---------------------------------------------------------------------------
# JobStatusResponse
# ---------------------------------------------------------------------------

class TestJobStatusResponse:
    """Tests for JobStatusResponse model."""

    def test_defaults(self) -> None:
        resp = JobStatusResponse(
            job_id="j1",
            status=JobStatus.PENDING,
            created_at=_now(),
        )
        assert resp.progress == 0.0
        assert resp.pages_scraped == 0
        assert resp.pages_failed == 0
        assert resp.started_at is None
        assert resp.completed_at is None
        assert resp.error_message is None

    def test_progress_boundary_zero(self) -> None:
        resp = JobStatusResponse(
            job_id="j", status=JobStatus.RUNNING, progress=0.0, created_at=_now()
        )
        assert resp.progress == 0.0

    def test_progress_boundary_hundred(self) -> None:
        resp = JobStatusResponse(
            job_id="j", status=JobStatus.COMPLETED, progress=100.0, created_at=_now()
        )
        assert resp.progress == 100.0

    def test_progress_above_max_raises(self) -> None:
        with pytest.raises(ValidationError):
            JobStatusResponse(
                job_id="j",
                status=JobStatus.RUNNING,
                progress=100.1,
                created_at=_now(),
            )

    def test_progress_below_min_raises(self) -> None:
        with pytest.raises(ValidationError):
            JobStatusResponse(
                job_id="j",
                status=JobStatus.RUNNING,
                progress=-1.0,
                created_at=_now(),
            )


# ---------------------------------------------------------------------------
# JobResultResponse
# ---------------------------------------------------------------------------

class TestJobResultResponse:
    """Tests for JobResultResponse model."""

    def test_defaults(self) -> None:
        resp = JobResultResponse(job_id="j", status=JobStatus.COMPLETED)
        assert resp.total_pages == 0
        assert resp.failed_pages == 0
        assert resp.output_files == []
        assert resp.summary is None

    def test_output_files_list(self) -> None:
        resp = JobResultResponse(
            job_id="j",
            status=JobStatus.COMPLETED,
            output_files=["file1.md", "file2.md"],
        )
        assert len(resp.output_files) == 2


# ---------------------------------------------------------------------------
# UserResponse
# ---------------------------------------------------------------------------

class TestUserResponse:
    """Tests for UserResponse model."""

    def test_defaults(self) -> None:
        resp = UserResponse(user_id="u1", email="a@b.com", created_at=_now())
        assert resp.tier == BillingTier.FREE
        assert resp.name is None

    def test_pro_tier(self) -> None:
        resp = UserResponse(
            user_id="u2", email="pro@b.com", tier=BillingTier.PRO, created_at=_now()
        )
        assert resp.tier == BillingTier.PRO


# ---------------------------------------------------------------------------
# APIKeyResponse and APIKeyListResponse
# ---------------------------------------------------------------------------

class TestAPIKeyResponse:
    """Tests for APIKeyResponse model."""

    def test_defaults(self) -> None:
        resp = APIKeyResponse(
            key_id="k1",
            name="prod",
            prefix="pk_abcdefgh",
            created_at=_now(),
        )
        assert resp.key is None
        assert resp.is_active is True

    def test_key_included_at_creation(self) -> None:
        resp = APIKeyResponse(
            key_id="k2",
            name="dev",
            prefix="pk_12345678",
            key="pk_12345678_verylongsecret",
            created_at=_now(),
        )
        assert resp.key is not None


class TestAPIKeyListResponse:
    """Tests for APIKeyListResponse model."""

    def test_empty_list(self) -> None:
        resp = APIKeyListResponse(keys=[], total=0)
        assert resp.total == 0
        assert resp.keys == []

    def test_non_empty_list(self) -> None:
        key = APIKeyResponse(
            key_id="k1", name="prod", prefix="pk_x", created_at=_now()
        )
        resp = APIKeyListResponse(keys=[key], total=1)
        assert resp.total == 1
        assert len(resp.keys) == 1


# ---------------------------------------------------------------------------
# CheckoutRequest
# ---------------------------------------------------------------------------

class TestCheckoutRequest:
    """Tests for CheckoutRequest model."""

    def test_valid_request(self) -> None:
        req = CheckoutRequest(
            tier=BillingTier.PRO,
            success_url="https://app.example.com/success",
            cancel_url="https://app.example.com/cancel",
        )
        assert req.tier == BillingTier.PRO

    def test_invalid_success_url_raises(self) -> None:
        with pytest.raises(ValidationError):
            CheckoutRequest(
                tier=BillingTier.PRO,
                success_url="not-a-url",
                cancel_url="https://example.com",
            )

    def test_missing_tier_raises(self) -> None:
        with pytest.raises(ValidationError):
            CheckoutRequest(  # type: ignore[call-arg]
                success_url="https://example.com",
                cancel_url="https://example.com",
            )


# ---------------------------------------------------------------------------
# WebhookPayload
# ---------------------------------------------------------------------------

class TestWebhookPayload:
    """Tests for WebhookPayload model."""

    def test_valid_payload(self) -> None:
        payload = WebhookPayload(
            event="job.completed",
            job_id="j1",
            status=JobStatus.COMPLETED,
            timestamp=_now(),
        )
        assert payload.event == "job.completed"
        assert payload.result is None

    def test_result_optional(self) -> None:
        payload = WebhookPayload(
            event="job.failed",
            job_id="j2",
            status=JobStatus.FAILED,
            result={"error": "timeout"},
            timestamp=_now(),
        )
        assert payload.result == {"error": "timeout"}

    def test_missing_event_raises(self) -> None:
        with pytest.raises(ValidationError):
            WebhookPayload(job_id="j", status=JobStatus.PENDING, timestamp=_now())  # type: ignore[call-arg]


# ---------------------------------------------------------------------------
# UsageSummaryResponse
# ---------------------------------------------------------------------------

class TestUsageSummaryResponse:
    """Tests for UsageSummaryResponse model."""

    def test_defaults(self) -> None:
        resp = UsageSummaryResponse(
            key_id="k1",
            tier=BillingTier.FREE,
            period_start=_now(),
            period_end=_now(),
            total_requests=10,
            requests_limit=1000,
            pages_scraped=50,
        )
        assert resp.is_over_limit is False
        assert resp.overage_percentage == 0.0

    def test_over_limit_flag(self) -> None:
        resp = UsageSummaryResponse(
            key_id="k2",
            tier=BillingTier.FREE,
            period_start=_now(),
            period_end=_now(),
            total_requests=2000,
            requests_limit=1000,
            pages_scraped=200,
            is_over_limit=True,
            overage_percentage=100.0,
        )
        assert resp.is_over_limit is True
        assert resp.overage_percentage == 100.0


# ---------------------------------------------------------------------------
# PlanInfo
# ---------------------------------------------------------------------------

class TestPlanInfo:
    """Tests for PlanInfo model."""

    def test_valid_plan(self) -> None:
        plan = PlanInfo(
            tier=BillingTier.PRO,
            name="Pro Plan",
            requests_per_hour=500,
            max_pages_per_request=1000,
            max_concurrent_jobs=5,
            price_monthly_cents=1999,
        )
        assert plan.tier == BillingTier.PRO
        assert plan.stripe_price_id is None

    def test_with_stripe_price_id(self) -> None:
        plan = PlanInfo(
            tier=BillingTier.ENTERPRISE,
            name="Enterprise",
            requests_per_hour=10000,
            max_pages_per_request=10000,
            max_concurrent_jobs=50,
            price_monthly_cents=49900,
            stripe_price_id="price_abc123",
        )
        assert plan.stripe_price_id == "price_abc123"
