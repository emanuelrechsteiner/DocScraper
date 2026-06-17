"""
LLM-Enhanced Content Cleaning and Validation

This module provides intelligent content validation and refinement using OpenAI's API.
Integrates with PostScraperCleaner to validate and improve rule-based cleaning results.

Phase 2: LLM validation with cost optimization and rate limiting
"""

from __future__ import annotations

import json
import os
import hashlib
import time
import logging
from pathlib import Path
from dataclasses import dataclass, field
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import URLError

logger = logging.getLogger(__name__)


@dataclass
class LLMConfig:
    """Configuration for LLM-based validation"""
    api_key: str | None = None
    model: str = "gpt-4o"
    temperature: float = 0.1
    max_tokens: int = 1000
    rate_limit_rpm: int = 500
    retry_attempts: int = 3
    retry_delay: float = 1.0
    cache_enabled: bool = True
    cache_dir: Path | None = None
    input_cost_per_1m: float = 2.50
    output_cost_per_1m: float = 10.00

    def __post_init__(self):
        """Validate configuration"""
        if self.temperature < 0 or self.temperature > 2:
            raise ValueError("temperature must be between 0 and 2")
        if self.max_tokens < 100:
            raise ValueError("max_tokens must be at least 100")
        if self.rate_limit_rpm < 1:
            raise ValueError("rate_limit_rpm must be at least 1")
        if self.cache_dir:
            self.cache_dir = Path(self.cache_dir)
            self.cache_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class ValidationResult:
    """Result of LLM content validation"""
    is_valid: bool = False
    confidence: float = 0.0
    issues: list[str] = field(default_factory=list)
    suggestions: list[str] = field(default_factory=list)
    improved_content: str | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    cost: float = 0.0
    cached: bool = False
    validation_type: str = "structure"

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "is_valid": self.is_valid,
            "confidence": round(self.confidence, 3),
            "issues": self.issues,
            "suggestions": self.suggestions,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cost": round(self.cost, 6),
            "cached": self.cached,
            "validation_type": self.validation_type,
        }


class RateLimiter:
    """Token bucket rate limiter for API requests"""

    def __init__(self, rpm: int = 500):
        """Initialize with requests per minute limit"""
        self.rpm = rpm
        self.tokens = rpm
        self.last_update = time.time()
        self.requests = 0
        self.lock_until = 0.0

    def acquire(self) -> tuple[bool, float]:
        """
        Try to acquire a token. Returns (success, wait_time_seconds).
        Uses token bucket algorithm with exponential backoff.
        """
        now = time.time()

        # Refill tokens based on elapsed time
        elapsed = now - self.last_update
        refill = (elapsed / 60.0) * self.rpm
        self.tokens = min(self.rpm, self.tokens + refill)
        self.last_update = now

        # Check if rate limited
        if now < self.lock_until:
            wait = self.lock_until - now
            return False, wait

        # Check if we have tokens
        if self.tokens >= 1:
            self.tokens -= 1
            self.requests += 1
            return True, 0.0

        # Calculate backoff
        tokens_needed = 1 - self.tokens
        wait_time = (tokens_needed / self.rpm) * 60.0
        return False, wait_time

    def get_statistics(self) -> dict:
        """Get rate limiter statistics"""
        return {
            "requests_made": self.requests,
            "rpm_limit": self.rpm,
            "tokens_available": round(self.tokens, 2),
        }


class LLMValidator:
    """Validates and improves cleaned content using OpenAI API"""

    def __init__(self, config: LLMConfig):
        """Initialize LLM validator"""
        self.config = config
        self.api_key = config.api_key or os.getenv("OPENAI_API_KEY")
        self.rate_limiter = RateLimiter(config.rate_limit_rpm)

        self.stats = {
            "validations_requested": 0,
            "validations_successful": 0,
            "cache_hits": 0,
            "api_errors": 0,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
            "total_cost": 0.0,
        }

        if not self.api_key:
            logger.warning("No OpenAI API key found. LLM validation disabled.")

    def validate_content(
        self, content: str, metadata: dict | None = None
    ) -> ValidationResult:
        """
        Validate cleaned content structure and quality.
        Returns ValidationResult with improvements if available.
        """
        self.stats["validations_requested"] += 1

        if not self.api_key:
            # Graceful degradation: run real local structure validation rather
            # than rubber-stamping everything as valid.
            result = self._fallback_validation(content)
            result.suggestions.append(
                "Configure OPENAI_API_KEY to enable LLM validation"
            )
            return result

        metadata = metadata or {}

        # Check cache
        if self.config.cache_enabled:
            cached = self._get_cached_result(content)
            if cached:
                self.stats["cache_hits"] += 1
                cached.cached = True
                return cached

        # Rate limiting
        success, wait = self.rate_limiter.acquire()
        if not success:
            logger.warning(f"Rate limited, waiting {wait:.2f}s")
            time.sleep(wait)

        # Call API with retries
        for attempt in range(self.config.retry_attempts):
            try:
                result = self._call_openai_api(content, metadata)
                self.stats["validations_successful"] += 1

                # Cache result
                if self.config.cache_enabled:
                    self._cache_result(content, result)

                # Update stats
                self.stats["total_input_tokens"] += result.input_tokens
                self.stats["total_output_tokens"] += result.output_tokens
                self.stats["total_cost"] += result.cost

                return result

            except Exception as e:
                if attempt < self.config.retry_attempts - 1:
                    wait_time = self.config.retry_delay * (2 ** attempt)
                    logger.warning(
                        f"API error (attempt {attempt + 1}), retrying in {wait_time}s: {e}"
                    )
                    time.sleep(wait_time)
                else:
                    self.stats["api_errors"] += 1
                    logger.error(f"LLM validation failed after retries: {e}")
                    return self._fallback_validation(content)

        return self._fallback_validation(content)

    def _call_openai_api(self, content: str, metadata: dict) -> ValidationResult:
        """Call OpenAI API for content validation"""
        import json

        # Build validation prompt
        prompt = self._build_validation_prompt(content, metadata)

        # Prepare request
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.config.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }

        request = Request(
            url, data=json.dumps(payload).encode(), headers=headers, method="POST"
        )

        try:
            with urlopen(request, timeout=30) as response:
                data = json.loads(response.read().decode())

                # Parse response
                response_text = data["choices"][0]["message"]["content"]
                usage = data.get("usage", {})

                input_tokens = usage.get("prompt_tokens", 0)
                output_tokens = usage.get("completion_tokens", 0)
                cost = self._calculate_cost(input_tokens, output_tokens)

                # Parse structured response
                result = self._parse_validation_response(response_text)
                result.input_tokens = input_tokens
                result.output_tokens = output_tokens
                result.cost = cost

                return result

        except URLError as e:
            raise ValueError(f"API request failed: {e}")

    def _build_validation_prompt(self, content: str, metadata: dict) -> str:
        """Build prompt for content validation"""
        # Summarize content for analysis
        lines = content.split("\n")
        preview = "\n".join(lines[:20]) if len(lines) > 20 else content

        prompt = f"""Analyze this cleaned markdown documentation content and provide validation feedback.

CONTENT PREVIEW:
{preview}
{"..." if len(lines) > 20 else ""}

VALIDATION CRITERIA:
1. Structure: Has proper heading hierarchy (H1-H6)
2. Completeness: Contains meaningful content (not mostly empty)
3. Cleanliness: No navigation, boilerplate, or repetitive elements
4. Readability: Good formatting with code blocks, lists, etc.

RESPONSE FORMAT (JSON):
{{
  "is_valid": true/false,
  "confidence": 0.0-1.0,
  "validation_type": "structure|content|quality",
  "issues": ["list", "of", "issues"],
  "suggestions": ["list", "of", "improvements"]
}}

Only output valid JSON, no other text."""

        return prompt

    def _parse_validation_response(self, response_text: str) -> ValidationResult:
        """Parse structured response from LLM"""
        try:
            # Extract JSON from response
            data = json.loads(response_text)

            return ValidationResult(
                is_valid=data.get("is_valid", True),
                confidence=float(data.get("confidence", 0.8)),
                issues=data.get("issues", []),
                suggestions=data.get("suggestions", []),
                validation_type=data.get("validation_type", "structure"),
            )
        except (json.JSONDecodeError, ValueError):
            # Fallback parsing
            return ValidationResult(
                is_valid=True,
                confidence=0.6,
                suggestions=["Response parsing issue, manual review recommended"],
            )

    def _calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Calculate API cost"""
        input_cost = (input_tokens / 1_000_000) * self.config.input_cost_per_1m
        output_cost = (output_tokens / 1_000_000) * self.config.output_cost_per_1m
        return input_cost + output_cost

    def _fallback_validation(self, content: str) -> ValidationResult:
        """Fallback validation without API"""
        # Basic local validation
        lines = content.split("\n")
        has_headers = any(line.startswith("#") for line in lines)
        # Heuristic minimum for "has meaningful content" — enough to reject
        # trivial input (e.g. a single character) without requiring a full
        # document, since this runs as a no-API-key fallback.
        has_content = len(content.strip()) > 20
        has_structure = has_headers and has_content

        issues = []
        if not has_headers:
            issues.append("No header hierarchy detected")
        if not has_content:
            issues.append("Content too short")

        return ValidationResult(
            is_valid=has_structure,
            confidence=0.6 if has_structure else 0.3,
            issues=issues,
            suggestions=["Enable OpenAI API for enhanced validation"],
        )

    def _get_cached_result(self, content: str) -> ValidationResult | None:
        """Retrieve cached validation result"""
        if not self.config.cache_dir:
            return None

        cache_key = self._get_cache_key(content)
        cache_file = self.config.cache_dir / f"{cache_key}.json"

        if cache_file.exists():
            try:
                with open(cache_file, "r") as f:
                    data = json.load(f)
                    return ValidationResult(**data)
            except Exception as e:
                logger.warning(f"Cache read error: {e}")
        return None

    def _cache_result(self, content: str, result: ValidationResult) -> None:
        """Cache validation result"""
        if not self.config.cache_dir:
            return

        try:
            cache_key = self._get_cache_key(content)
            cache_file = self.config.cache_dir / f"{cache_key}.json"

            with open(cache_file, "w") as f:
                json.dump(result.to_dict(), f)
        except Exception as e:
            logger.warning(f"Cache write error: {e}")

    @staticmethod
    def _get_cache_key(content: str) -> str:
        """Generate cache key from content hash"""
        return hashlib.md5(content.encode()).hexdigest()

    def get_statistics(self) -> dict:
        """Get validation statistics"""
        stats = self.stats.copy()
        success_rate = (
            (stats["validations_successful"] / stats["validations_requested"])
            if stats["validations_requested"] > 0
            else 0
        )
        stats["success_rate"] = round(success_rate, 3)
        stats["total_cost"] = round(stats["total_cost"], 6)
        stats.update(self.rate_limiter.get_statistics())
        return stats
