# Changelog

All notable changes to Parsify are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-23

### Added

- **REST API** — Full FastAPI-based API with versioned routes (`/api/v1/`)
- **Documentation scraping** — `POST /api/v1/scrape` submits async scrape jobs via ARQ + Redis
- **Document processing** — `POST /api/v1/process` for post-processing and AI classification
- **Job management** — `GET /api/v1/jobs` for listing, status polling, and result retrieval
- **API key authentication** — SHA-256 hashed keys with prefix-based lookup (ADR-004)
- **Webhook callbacks** — Job completion/failure notifications to user-specified URLs
- **Rate limiting** — Per-key rate limiting via slowapi + Redis (ADR-005)
- **Usage tracking** — Request counting, daily breakdowns, and overage detection (soft/hard limits)
- **Stripe billing** — Subscription checkout, webhook handling, and tier management (Free/Pro/Enterprise)
- **PostgreSQL storage** — SQLAlchemy 2.0 async ORM with Alembic migrations (ADR-002)
- **Docker support** — Multi-stage Dockerfile and docker-compose for local development
- **GitHub Actions CI** — Lint (ruff), type check (mypy), test (pytest), and Docker build pipeline
- **Railway deployment** — Production deployment config with health checks
- **Health endpoints** — `GET /health` (liveness) and `GET /ready` (readiness with DB/Redis checks)
- **Structured logging** — JSON formatter with `X-Request-ID` tracing
- **MkDocs documentation** — API reference, getting started guide, auth and webhook guides
- **Landing page** — Feature overview and pricing comparison
- **Python SDK** — `pip install parsify` — sync and async clients with automatic job polling
- **JavaScript SDK** — `npm install parsify-sdk` — TypeScript client with async/await
- **Sentry monitoring** — Error tracking and performance monitoring

### Fixed (Phase 0 — codebase cleanup)

- `DocPostProcessor` hardcoded output path (#2)
- Hardcoded paths in `resume_processing.py` (#3)
- Stale pattern count assertions in tests (#4)
- Bare `except` clauses replaced with specific exceptions (#7)
- `logging.basicConfig()` removed from library modules (#8)
- LLM cost double-counting in `PostScraperCleaner` (#11)
- Factual errors in `ONBOARDING.json` (#12)

### Changed

- Type hints modernized to Python 3.10+ builtins (#9)
- `DocumentationScraper` class collision resolved (#10)
- Script tests moved to `scripts/` directory (#5)
- Test infrastructure added (`conftest.py`, `pytest.ini`) (#6)

---

## [0.3.0] - 2026-03-22

### Added (Phase 3 — Infrastructure)

- PostgreSQL schema with SQLAlchemy 2.0 async ORM models (#32)
- Alembic async migration framework with initial schema migration (#33)
- Repository pattern for data access layer (#34)
- Multi-stage Dockerfile with optimized layer caching (#35)
- `docker-compose.yml` for local development with PostgreSQL and Redis (#36)
- GitHub Actions CI pipeline (lint, type check, test, Docker build) (#37)
- Railway deployment configuration with environment variable mapping (#38)
- `GET /health` liveness and `GET /ready` readiness endpoints (#39)
- Structured JSON logging middleware with `X-Request-ID` tracing (#40)

---

## [0.2.0] - 2026-03-22

### Added (Phase 2 — Billing)

- Per-key rate limiting middleware via slowapi + Redis (#24)
- Usage tracking middleware recording requests per API key (#25)
- Billing tier structure: Free, Pro, and Enterprise (#26)
- Stripe subscription checkout session creation (#27)
- Stripe webhook handler for subscription lifecycle events (#28)
- Usage dashboard endpoints returning daily breakdowns (#29)
- Overage handling with configurable soft and hard limits (#30)
- Billing integration tests (#31)

---

## [0.1.0] - 2026-03-22

### Added (Phase 1 — REST API)

- FastAPI project structure with app factory pattern (#13)
- Pydantic request and response models for all endpoints (#14)
- `POST /api/v1/scrape` — submit a scrape job (#15)
- `GET /api/v1/jobs/{id}` — poll job status (#16)
- `GET /api/v1/jobs/{id}/result` — retrieve completed job result (#17)
- `POST /api/v1/process` — submit a post-processing job (#18)
- ARQ job queue with Redis backend for async task execution (#19)
- API key authentication middleware with SHA-256 hashing (#20)
- API key CRUD endpoints (`/api/v1/keys`) (#21)
- Webhook callbacks for job completion and failure events (#22)
- API integration tests (#23)

---

## [0.0.1] - 2026-03-22

### Fixed (Phase 0 — codebase cleanup, issues #2–#12)

- All issues identified in the Phase 0 codebase audit resolved
- See [1.0.0 Fixed section](#fixed-phase-0--codebase-cleanup) for the full list

[1.0.0]: https://github.com/parsify/parsify/releases/tag/v1.0.0
[0.3.0]: https://github.com/parsify/parsify/releases/tag/v0.3.0
[0.2.0]: https://github.com/parsify/parsify/releases/tag/v0.2.0
[0.1.0]: https://github.com/parsify/parsify/releases/tag/v0.1.0
[0.0.1]: https://github.com/parsify/parsify/releases/tag/v0.0.1
