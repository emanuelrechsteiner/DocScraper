"""Shared test fixtures for the Parsify test suite."""

import pytest
from pathlib import Path


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
