# Project Status — Parsify

> Living progress dashboard. Updated by `/status-sync`, `/issue`, and `/phase-gate`.
> This is a Tier 1 document — always read when starting a session.

---

## Current Status

**Active Phase:** Phase 0 — Codebase Cleanup
**Overall Progress:** 0% complete (0/51 issues)
**Last Updated:** 2026-03-22
**Last Updated By:** decompose-pipeline

---

## Progress by Phase

| Phase | Name | Total | Done | In Progress | Blocked | Available | % |
|-------|------|-------|------|-------------|---------|-----------|---|
| 0 | Codebase Cleanup | 11 | 0 | 0 | 0 | 11 | 0% |
| 1 | FastAPI REST Wrapper | 11 | 0 | 0 | 0 | 0 | 0% |
| 2 | Billing & Usage | 8 | 0 | 0 | 0 | 0 | 0% |
| 3 | CI/CD + Database | 9 | 0 | 0 | 0 | 0 | 0% |
| 4 | Docs + Landing Page | 5 | 0 | 0 | 0 | 0 | 0% |
| 5 | SDK + Launch | 7 | 0 | 0 | 0 | 0 | 0% |
| **Total** | | **51** | **0** | **0** | **0** | **11** | **0%** |

---

## Current Sprint

### Next Available Issues (Phase 0 — all parallel-safe)

| Issue | Title | Type | Area | Labels |
|-------|-------|------|------|--------|
| #2 | Fix DocPostProcessor hardcoded output path | fix | core | `parallel-safe` |
| #3 | Parameterize resume_processing.py paths | fix | core | `parallel-safe` |
| #4 | Update stale pattern count assertions | fix | test | `parallel-safe` |
| #5 | Move script-tests to scripts directory | refactor | test | `parallel-safe` |
| #6 | Add test infrastructure | infrastructure | test | |
| #7 | Fix bare except clauses | fix | core | `parallel-safe` |
| #8 | Remove logging.basicConfig() from library modules | fix | core | `parallel-safe` |
| #9 | Add type hints to public methods | refactor | core | `parallel-safe` |
| #10 | Rename DocumentationScraper class collision | refactor | core | |
| #11 | Fix LLM cost double-counting | fix | core | `parallel-safe` |
| #12 | Fix ONBOARDING.json factual errors | docs | docs | `parallel-safe` |

### Currently In Progress

*No issues in progress yet.*

### Blocked Issues

*No blocked issues.*

---

## Recent Activity

| Date | Agent | Action | Issue | Details |
|------|-------|--------|-------|---------|
| 2026-03-22 | Claude Opus 4.6 | Decompose | — | Created 51 issues across 6 phases, locked scope |
| 2026-03-22 | Claude Opus 4.6 | Brainstorm | — | Generated product foundation (9 documents) |
| 2026-03-22 | Claude Opus 4.6 | Bootstrap | — | Installed Torvaldsen workflow |

---

## Blockers & Risks

### Active Blockers

*No active blockers.*

### Upcoming Risks

| # | Risk | Phase | Mitigation | Status |
|---|------|-------|------------|--------|
| R1 | crawl4ai breaking changes | 1 | Pin version, integration tests | Monitoring |
| R2 | OpenAI API cost spikes | 2 | Usage limits, cost tracking | Monitoring |
| R3 | Playwright + Chromium Docker image size | 3 | Multi-stage build, slim base | Planned |

---

## Scope Health

**Scope Manifest Status:** LOCKED (2026-03-22)
**Total Features:** 6 (F000-F005)
**Features Complete:** 0
**Scope Changes:** 0

---

## Quality Metrics

| Metric | Current | Target |
|--------|---------|--------|
| pytest Errors | TBD | 0 |
| ruff Warnings | TBD | 0 |
| Test Coverage | TBD | 80% |
| mypy Errors | TBD | 0 |
