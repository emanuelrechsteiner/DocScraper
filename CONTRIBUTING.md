# Contributing to Parsify

> This project uses the **Torvaldsen Development Workflow** — a strict atomic development process designed for AI-assisted development with comprehensive git traceability.

---

## Getting Started

### Prerequisites

- Python 3.13+
- pip (or uv)
- Git
- GitHub CLI (`gh`) — for issue and PR management
- Claude Code — for AI-assisted development with Torvaldsen commands

### Setup

```bash
# Clone
git clone https://github.com/emanuelgrammenos/DocScraper.git
cd DocScraper

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
pip install -e .                      # Package in editable mode

# Install Playwright
playwright install chromium

# Set up environment
cp .env.example .env
# Edit .env with your OPENAI_API_KEY

# Verify setup
python -m pytest tests/ -v
```

---

## Development Workflow

This project follows the Torvaldsen workflow. Every code change follows this loop:

```
1. Orient          /torvaldsen-onboard (or read START_HERE.md)
2. Pick issue      From PROJECT-STATUS.md
3. Implement       /issue <#>
4. Review          /review <PR#>
5. Clean context   /clear
6. Repeat
```

### Key Commands

| Command | Purpose |
|---------|---------|
| `/issue <#>` | Full development workflow for one issue |
| `/review <PR#>` | Code review before merge |
| `/status-sync` | Update progress dashboard |
| `/phase-gate <N>` | Verify phase completion |
| `/handoff` | Context handoff between sessions |

---

## Code Standards

### Commit Messages

```
<type>(<area>): <description> - closes #<N>

Phase: <N>
Feature: <feature-id>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `style`, `chore`, `perf`

### Branch Naming

```
<type>/issue-<N>-<kebab-description>
```

### Pre-Commit Checklist

- [ ] Tests pass: `python -m pytest tests/ -v`
- [ ] Linting passes: `ruff check .`
- [ ] Type check passes: `mypy src/`
- [ ] No `print()` or `logging.basicConfig()` in library code
- [ ] No bare `except:` clauses
- [ ] All new public methods have type hints and docstrings

---

## Project Structure

See `CONVENTIONS.md` for detailed folder structure and naming conventions.

---

## Architecture

See `ARCHITECTURE.md` for technology decisions and ADRs.

---

## Scope Policy

- Every issue has a defined **scope boundary** (what's in AND what's out)
- No changes outside the scope of the assigned issue
- New ideas → new issues (never add unplanned work to a branch)
- Scope changes require human approval

See `.claude/rules/torvaldsen-scope.md` for full scope discipline rules.

---

## Getting Help

| I need to... | Read this |
|--------------|-----------|
| Understand the project | `START_HERE.md` |
| See current progress | `PROJECT-STATUS.md` |
| Know the coding style | `CONVENTIONS.md` |
| Understand tech choices | `ARCHITECTURE.md` |
| See feature requirements | `SPECIFICATION.md` |
| Read the full plan | `BRAINSTORM.md` |
