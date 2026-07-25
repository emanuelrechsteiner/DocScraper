"""Shared test fixtures for the Parsify test suite."""

from pathlib import Path

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.db.models import Base


@pytest.fixture
def sample_markdown() -> str:
    """Sample markdown with common documentation patterns."""
    return """---
url: https://docs.example.com/getting-started
scraped_at: 2026-03-01T12:00:00
title: Getting Started
---

Skip to main content

# Getting Started

Welcome to the documentation.

## Installation

```bash
pip install example-lib
```

## Quick Start

- Step 1: Install the package
- Step 2: Configure your settings
- Step 3: Run the application

## API Reference

```python
from example_lib import Client

client = Client(api_key="your-key")
result = client.process("hello")
```

Was this page helpful?

© 2026 Example Inc. All rights reserved.
"""


@pytest.fixture
def sample_markdown_minimal() -> str:
    """Minimal markdown without boilerplate."""
    return """# Simple Document

This is a simple document with no boilerplate.

## Section One

Content here.
"""


@pytest.fixture
def tmp_output_dir(tmp_path: Path) -> Path:
    """Temporary output directory for processing tests."""
    output = tmp_path / "output"
    output.mkdir()
    return output


@pytest.fixture
def tmp_input_dir(tmp_path: Path) -> Path:
    """Temporary input directory with sample markdown files."""
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    sample = input_dir / "sample.md"
    sample.write_text(
        "# Test Document\n\nThis is test content.\n\n## Section\n\nMore content.\n"
    )
    return input_dir


@pytest_asyncio.fixture
async def db_session() -> AsyncSession:
    """Provide an in-memory SQLite session for unit tests.

    Creates all tables before yielding the session, then drops them on
    teardown. Using SQLite avoids requiring a live PostgreSQL instance.

    PostgreSQL-specific JSONB columns are handled by registering a custom
    SQLite compiler visit method for JSONB that renders it as TEXT, which
    SQLite can store and retrieve as JSON strings.

    Yields:
        An ``AsyncSession`` connected to an in-memory SQLite database.
    """
    import json as _json

    from sqlalchemy.dialects import sqlite as _sqlite_dialect

    # Teach SQLite's type compiler to emit "TEXT" when it encounters a JSONB
    # column — this avoids the "CompileError: Unknown type" at DDL time.
    if not hasattr(_sqlite_dialect.base.SQLiteTypeCompiler, "visit_JSONB"):
        _sqlite_dialect.base.SQLiteTypeCompiler.visit_JSONB = (  # type: ignore[attr-defined]
            lambda self, type_, **kw: "TEXT"
        )

    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        echo=False,
        json_serializer=_json.dumps,
        json_deserializer=_json.loads,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with maker() as session:
        yield session
        await session.close()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()
