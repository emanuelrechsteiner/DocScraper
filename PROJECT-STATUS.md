# Project Status — Parsify

> Living progress dashboard. Updated by `/status-sync`, `/issue`, and `/phase-gate`.
> This is a Tier 1 document — always read when starting a session.

---

## Current Status

**Active Phase:** Phase 0 — Codebase Cleanup
**Overall Progress:** 0% complete (0/~55 issues)
**Last Updated:** 2026-03-22
**Last Updated By:** brainstorm-pipeline

---

## Progress by Phase

| Phase | Name | Total | Done | In Progress | Blocked | Available | % |
|-------|------|-------|------|-------------|---------|-----------|---|
| 0 | Codebase Cleanup | 12 | 0 | 0 | 0 | 12 | 0% |
| 1 | FastAPI REST Wrapper | 12 | 0 | 0 | 0 | 0 | 0% |
| 2 | Billing & Usage | 8 | 0 | 0 | 0 | 0 | 0% |
| 3 | CI/CD + Database | 10 | 0 | 0 | 0 | 0 | 0% |
| 4 | Docs + Landing Page | 8 | 0 | 0 | 0 | 0 | 0% |
| 5 | SDK + Launch | 7 | 0 | 0 | 0 | 0 | 0% |
| **Total** | | **~57** | **0** | **0** | **0** | **12** | **0%** |

---

## Current Sprint

### Next Available Issues

<!-- Issues that are unblocked and ready to work on — Phase 0 cleanup -->

*Issues will be populated after `/decompose` creates GitHub issues.*

Phase 0 planned issues (all parallel-safe unless noted):
- Fix DocPostProcessor hardcoded output path `fix` `core`
- Parameterize resume_processing.py paths `fix` `core`
- Update stale test assertions `fix` `test`
- Move script-tests to scripts/ `refactor` `test`
- Add test infrastructure `infrastructure` `test`
- Fix bare except clauses `fix` `core`
- Remove logging.basicConfig() from library modules `fix` `core`
- Add type hints to public methods `refactor` `core`
- Rename DocumentationScraper class collision `refactor` `core`
- Fix LLM cost double-counting `fix` `core`
- Fix ONBOARDING.json factual errors `docs` `docs`

### Currently In Progress

*No issues in progress yet.*

### Blocked Issues

*No blocked issues.*

---

## Recent Activity

| Date | Agent | Action | Issue | Details |
|------|-------|--------|-------|---------|
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

**Scope Manifest Status:** Unlocked (will lock after `/decompose`)
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
