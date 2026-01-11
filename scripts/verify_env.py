import sys
try:
    import beautifulsoup4
    print("beautifulsoup4 OK")
except ImportError:
    print("beautifulsoup4 MISSING")

try:
    import requests
    print("requests OK")
except ImportError:
    print("requests MISSING")

try:
    import openai
    print("openai OK")
except ImportError:
    print("openai MISSING")

try:
    import pytest
    print("pytest OK")
except ImportError:
    print("pytest MISSING")

print(f"Python version: {sys.version}")
