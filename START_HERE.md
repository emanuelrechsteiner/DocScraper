# Start Here — Parsify

> Onboarding entry point for new agents and contributors.
> Read this FIRST. Time to orient: ~2 minutes.

---

## What Is This?

Parsify (formerly DocScraper) is a Python toolkit for scraping documentation websites and post-processing them into AI-ready formats (cleaned markdown, semantic chunks, vector DB indices). It's evolving into a production REST API service so developers can access these capabilities via HTTP instead of running Python scripts.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.13+ |
| Scraping | crawl4ai + Playwright |
| AI | OpenAI API (GPT-4o) |
| Analysis | NetworkX, scikit-learn |
| GUI | Tkinter |
| API (planned) | FastAPI |
| Database (planned) | PostgreSQL + SQLAlchemy |
| Queue (planned) | ARQ + Redis |
| Billing (planned) | Stripe |
| Deployment (planned) | Docker + Railway |

---

## Current Status

**Baseline complete** — legacy project, 47/51 issues delivered (92%) + dashboard (SC001) — **ready for future Torvaldsen development**

> The 6-phase build is done and merged to `main`. Remaining: #42–#45 (landing/docs)
> as future work, plus baseline quality cleanup. For detailed progress, see `PROJECT-STATUS.md`.

---

## Key Documents

| Document | Purpose | When to Read |
|----------|---------|--------------|
| `START_HERE.md` | You are here | Always first |
| `PROJECT-STATUS.md` | Progress dashboard, next issue | Every session start |
| `CONVENTIONS.md` | Code patterns, naming, structure | Before writing code |
| `ARCHITECTURE.md` | Tech decisions, ADRs, system design | When making tech choices |
| `SPECIFICATION.md` | Features, design system, brand | When implementing features |
| `BRAINSTORM.md` | Master plan, all phases and issues | Reference only |
| `RESEARCH_FINDINGS.md` | Technology evaluation | Reference only |
| `CLAUDE.md` | Agent-specific instructions | Auto-loaded |

---

## Environment Setup

```bash
# 1. Clone the repository
git clone https://github.com/emanuelgrammenos/DocScraper.git
cd DocScraper

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -e .  # Install package in editable mode

# 4. Install Playwright browser
playwright install chromium

# 5. Set up environment variables
cp .env.example .env
# Edit .env with your OPENAI_API_KEY

# 6. Run tests
python -m pytest tests/ -v
```

---

## Contribution Flow

```
1. /torvaldsen-onboard     <- Orient yourself (you're doing this now)
2. Pick an issue            <- From PROJECT-STATUS.md "Next Available"
3. /issue <#>              <- Full development workflow
4. /review <PR#>           <- Code review before merge
5. /clear                  <- Clean context between issues
6. Repeat from step 2
```

---

## Quick Reference

- **Commit format:** `<type>(<area>): <description> - closes #<N>`
- **Branch format:** `<type>/issue-<N>-<description>`
- **Before commit:** `python -m pytest tests/ -v && ruff check .`
- **Scope rules:** See `.claude/rules/torvaldsen-scope.md`
- **Phase gate:** Run `/phase-gate <N>` when all phase issues are closed

---

## Need Help?

| I need to... | Do this |
|--------------|---------|
| Understand the architecture | Read `ARCHITECTURE.md` |
| Know the code conventions | Read `CONVENTIONS.md` |
| See the full plan | Read `BRAINSTORM.md` |
| Check feature requirements | Read `SPECIFICATION.md` |
| See what happened before | Read `.torvaldsen/phase-summaries/` |
| See what the last agent did | Read `.torvaldsen/agent-log.md` (last entry) |
