"""Verify that required runtime dependencies are importable."""

import importlib.util
import sys

# Map: human-facing name -> importable module name.
DEPENDENCIES = {
    "beautifulsoup4": "bs4",
    "requests": "requests",
    "openai": "openai",
    "pytest": "pytest",
}


def main() -> int:
    missing = []
    for display_name, module_name in DEPENDENCIES.items():
        if importlib.util.find_spec(module_name) is not None:
            print(f"{display_name} OK")
        else:
            print(f"{display_name} MISSING")
            missing.append(display_name)

    print(f"Python version: {sys.version}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
