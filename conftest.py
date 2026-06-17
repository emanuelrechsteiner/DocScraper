"""Root conftest — ensure the repository root is importable.

The top-level ``api`` package is not pip-installed (only ``src/docscraper`` is),
so ``import api`` relies on the repo root being on ``sys.path``. Pytest loads
this root conftest before any test or ``tests/conftest.py``, so inserting the
path here makes ``api`` importable in every environment (local and CI),
independent of pytest version or invocation cwd.
"""

import os
import sys

_REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
