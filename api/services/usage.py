"""Usage tracking and overage service (#25, #29, #30).

Records API usage per key and enforces soft limits based on billing tier.
In-memory for Phase 1-2; PostgreSQL in Phase 3.
"""

import logging
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, date, datetime

from ..models.schemas import BillingTier

logger = logging.getLogger(__name__)

# Tier limits — centralised definition (#26)
TIER_LIMITS: dict[BillingTier, dict[str, int]] = {
    BillingTier.FREE: {
        "requests_per_hour": 100,
        "max_pages_per_request": 100,
        "max_concurrent_jobs": 2,
        "price_monthly_cents": 0,
    },
    BillingTier.PRO: {
        "requests_per_hour": 1000,
        "max_pages_per_request": 5000,
        "max_concurrent_jobs": 10,
        "price_monthly_cents": 4900,
    },
    BillingTier.ENTERPRISE: {
        "requests_per_hour": 10000,
        "max_pages_per_request": 10000,
        "max_concurrent_jobs": 50,
        "price_monthly_cents": 29900,
    },
}


@dataclass
class UsageEntry:
    """Single API usage record."""

    timestamp: datetime
    endpoint: str
    method: str
    status_code: int
    response_time_ms: float
    key_id: str | None = None
    pages_count: int = 0


class UsageService:
    """Tracks API usage and enforces tier limits."""

    def __init__(self) -> None:
        self._records: list[UsageEntry] = []
        self._hourly_counts: dict[str, int] = defaultdict(int)  # "key_id:hour" -> count
        self._daily_counts: dict[str, dict[str, int]] = defaultdict(
            lambda: {"requests": 0, "pages": 0, "errors": 0}
        )

    def record(
        self,
        endpoint: str,
        method: str,
        status_code: int,
        response_time_ms: float,
        key_id: str | None = None,
        pages_count: int = 0,
    ) -> None:
        """Record a single API usage event."""
        now = datetime.now(UTC)
        entry = UsageEntry(
            timestamp=now,
            endpoint=endpoint,
            method=method,
            status_code=status_code,
            response_time_ms=response_time_ms,
            key_id=key_id,
            pages_count=pages_count,
        )
        self._records.append(entry)

        if key_id:
            hour_key = f"{key_id}:{now.strftime('%Y-%m-%d-%H')}"
            self._hourly_counts[hour_key] += 1

            day_key = f"{key_id}:{now.strftime('%Y-%m-%d')}"
            self._daily_counts[day_key]["requests"] += 1
            self._daily_counts[day_key]["pages"] += pages_count
            if status_code >= 400:
                self._daily_counts[day_key]["errors"] += 1

    def get_hourly_count(self, key_id: str) -> int:
        """Get the request count for the current hour."""
        now = datetime.now(UTC)
        hour_key = f"{key_id}:{now.strftime('%Y-%m-%d-%H')}"
        return self._hourly_counts.get(hour_key, 0)

    def check_rate_limit(self, key_id: str, tier: BillingTier) -> tuple[bool, int]:
        """Check if a key has exceeded its hourly rate limit.

        Returns:
            Tuple of (is_allowed, remaining_requests).
        """
        limit = TIER_LIMITS[tier]["requests_per_hour"]
        current = self.get_hourly_count(key_id)
        remaining = max(0, limit - current)
        return current < limit, remaining

    def check_overage(self, key_id: str, tier: BillingTier) -> dict[str, object]:
        """Check overage status for a key (#30).

        Soft limits: allow requests up to 120% of tier limit with warnings.
        Hard limit: block at 150% of tier limit.

        Returns:
            Dict with is_over_soft, is_over_hard, usage_percentage, message.
        """
        limit = TIER_LIMITS[tier]["requests_per_hour"]
        current = self.get_hourly_count(key_id)
        percentage = (current / limit * 100) if limit > 0 else 0

        soft_threshold = 120.0
        hard_threshold = 150.0

        result: dict[str, object] = {
            "current_usage": current,
            "limit": limit,
            "usage_percentage": round(percentage, 1),
            "is_over_soft": percentage >= soft_threshold,
            "is_over_hard": percentage >= hard_threshold,
            "message": "Within limits",
        }

        if percentage >= hard_threshold:
            result["message"] = (
                f"Hard limit exceeded ({percentage:.0f}% of {limit}/hr). "
                "Requests are blocked. Upgrade your plan."
            )
        elif percentage >= soft_threshold:
            result["message"] = (
                f"Soft limit warning ({percentage:.0f}% of {limit}/hr). "
                "Consider upgrading your plan."
            )
        elif percentage >= 80:
            result["message"] = (
                f"Approaching limit ({percentage:.0f}% of {limit}/hr)."
            )

        return result

    def get_summary(
        self, key_id: str, tier: BillingTier
    ) -> dict[str, object]:
        """Get usage summary for dashboard (#29)."""
        now = datetime.now(UTC)
        hour_key = f"{key_id}:{now.strftime('%Y-%m-%d-%H')}"
        limit = TIER_LIMITS[tier]["requests_per_hour"]
        current = self._hourly_counts.get(hour_key, 0)

        total_pages = sum(
            r.pages_count for r in self._records if r.key_id == key_id
        )

        return {
            "key_id": key_id,
            "tier": tier.value,
            "period_start": now.replace(minute=0, second=0, microsecond=0).isoformat(),
            "period_end": now.replace(minute=59, second=59, microsecond=999999).isoformat(),
            "total_requests": current,
            "requests_limit": limit,
            "pages_scraped": total_pages,
            "is_over_limit": current >= limit,
            "overage_percentage": round((current / limit * 100) - 100, 1) if current > limit else 0,
        }

    def get_daily_breakdown(
        self, key_id: str, days: int = 30
    ) -> list[dict[str, object]]:
        """Get daily usage breakdown for a key."""
        from datetime import timedelta

        today = date.today()
        results: list[dict[str, object]] = []
        for i in range(days):
            day_str = (
                datetime(today.year, today.month, today.day, tzinfo=UTC)
                - timedelta(days=i)
            ).strftime("%Y-%m-%d")
            day_key = f"{key_id}:{day_str}"
            stats = self._daily_counts.get(day_key, {"requests": 0, "pages": 0, "errors": 0})
            results.append({
                "date": day_str,
                "request_count": stats["requests"],
                "pages_scraped": stats["pages"],
                "errors": stats["errors"],
            })
        return results


# Singleton instance
usage_service = UsageService()
