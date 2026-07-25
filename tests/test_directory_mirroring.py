#!/usr/bin/env python3
"""
Test Directory Structure Mirroring

Tests the new clean_directory_tree method that mirrors input directory structure
with "_cleaned" suffix appended to subdirectory names.

Example:
    Input:  /input/docs/chroma/file.md
    Output: /output/docs/chroma_cleaned/file.md
"""

import os
from pathlib import Path

from docscraper.cleaning.cleaner import CleaningConfig, PostScraperCleaner


def load_env():
    """Load environment variables from .env file"""
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

load_env()

# Base documentation directory
DOCS_BASE = Path("/Volumes/NvME-Satechi/Documentation/2025_Emanuels_Tech_Stack_Docs")

# Test with a small subset first (only files in root)
TEST_INPUT = DOCS_BASE / "Anthropic_new"
TEST_OUTPUT = DOCS_BASE / "Anthropic_new_TEST"

def test_directory_mirroring():
    """Test directory structure mirroring with '_cleaned' suffix"""

    # Check for OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY environment variable not set")
        return False

    # Configure cleaner with intelligent analysis enabled
    config = CleaningConfig(
        remove_navigation=True,
        remove_headers_footers=True,
        remove_boilerplate=True,
        enable_llm_validation=True,  # This enables intelligent cleaner
        enable_chunk_optimization=False,
        openai_api_key=api_key,
        rate_limit_rpm=500
    )

    cleaner = PostScraperCleaner(config)

    print("="*80)
    print("DIRECTORY STRUCTURE MIRRORING TEST")
    print("="*80)
    print(f"Input:  {TEST_INPUT}")
    print(f"Output: {TEST_OUTPUT}")
    print()
    print("Expected behavior:")
    print("  Input:  en/docs/file.md")
    print("  Output: en_cleaned/docs_cleaned/file.md")
    print()

    # Process directory tree (limit to first 5 files for testing)
    results = cleaner.clean_directory_tree(
        input_root=TEST_INPUT,
        output_root=TEST_OUTPUT,
        pattern="**/*.md"  # Recursive search
    )

    # Print summary
    successful = sum(1 for r in results if r.success)
    failed = len(results) - successful
    total_cost = sum(r.llm_cost for r in results)
    avg_reduction = sum(r.reduction_percentage for r in results if r.success) / successful if successful > 0 else 0

    print("\n" + "="*80)
    print("TEST RESULTS")
    print("="*80)
    print(f"✅ Successful: {successful}/{len(results)}")
    print(f"❌ Failed: {failed}/{len(results)}")
    print(f"💰 Total LLM cost: ${total_cost:.6f}")
    print(f"📉 Average reduction: {avg_reduction:.1f}%")
    print(f"📁 Output directory: {TEST_OUTPUT}")
    print()

    # Verify directory structure
    if TEST_OUTPUT.exists():
        print("Output directory structure:")
        for root, dirs, files in os.walk(TEST_OUTPUT):
            level = root.replace(str(TEST_OUTPUT), '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in sorted(files)[:5]:  # Show first 5 files per directory
                print(f"{subindent}{file}")
            if len(files) > 5:
                print(f"{subindent}... and {len(files) - 5} more files")

    return failed == 0

if __name__ == "__main__":
    import sys
    success = test_directory_mirroring()
    sys.exit(0 if success else 1)
