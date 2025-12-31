#!/usr/bin/env python3
"""
Test Intelligent Content Cleaning System

Tests the LLM-powered intelligent cleaner on diverse documentation sources:
- Anthropic (AI API docs)
- Chroma (database docs)
- Python (language docs)
- Convex/Clerk (backend/auth docs)
- Langchain (AI framework docs)

Verifies that the system can identify and extract main content from
any documentation structure without hardcoded patterns.
"""

import os
import sys
from pathlib import Path
from PostScraperCleaner import PostScraperCleaner, CleaningConfig


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


# Load .env file
load_env()

# Base documentation directory
DOCS_BASE = Path("/Volumes/NvME-Satechi/Documentation/2025_Emanuels_Tech_Stack_Docs")

# Test output directory
TEST_OUTPUT = Path("/Volumes/NvME-Satechi/Development/Apps/DocScraper/test_results")
TEST_OUTPUT.mkdir(exist_ok=True)

# Test files from diverse documentation sources
TEST_FILES = [
    {
        "name": "Anthropic",
        "input": DOCS_BASE / "Anthropic_new/en_docs_build-with-claude_extended-thinking.md",
        "description": "AI API docs with language selector, Console/Support/Discord links"
    },
    {
        "name": "Chroma",
        "input": DOCS_BASE / "Chroma/docs_run-chroma_persistent-client.md",
        "description": "Database docs with Discord/GitHub/X links, Toggle theme button"
    },
    {
        "name": "Python",
        "input": DOCS_BASE / "Python_Documentation",  # Will find a file
        "description": "Language docs with index|modules|next|previous nav, permalink anchors"
    },
    {
        "name": "Convex",
        "input": DOCS_BASE / "Convex_Documentation",  # Will find a file
        "description": "Backend docs"
    },
    {
        "name": "Langchain",
        "input": DOCS_BASE / "Langchain",  # Will find a file
        "description": "AI framework docs"
    },
]


def find_sample_file(directory: Path) -> Path:
    """Find a representative markdown file in directory"""
    if directory.is_file():
        return directory

    # Find markdown files
    md_files = list(directory.glob("*.md"))

    if not md_files:
        raise FileNotFoundError(f"No markdown files found in {directory}")

    # Prefer files that are not too small or too large
    suitable_files = [
        f for f in md_files
        if 10000 < f.stat().st_size < 200000  # 10KB - 200KB
    ]

    if suitable_files:
        return suitable_files[0]
    else:
        return md_files[0]


def test_intelligent_cleaning():
    """Test intelligent cleaning on diverse documentation sources"""

    # Check for OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY environment variable not set")
        print("Please set it to enable intelligent content analysis:")
        print("  export OPENAI_API_KEY='your-key-here'")
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
    print("INTELLIGENT CONTENT CLEANING SYSTEM - TEST SUITE")
    print("="*80)
    print(f"Testing on {len(TEST_FILES)} diverse documentation sources")
    print(f"Output directory: {TEST_OUTPUT}")
    print("="*80)
    print()

    results = []

    for test_case in TEST_FILES:
        print(f"\n{'─'*80}")
        print(f"Testing: {test_case['name']}")
        print(f"Description: {test_case['description']}")
        print(f"{'─'*80}")

        try:
            # Find input file
            input_file = find_sample_file(test_case['input'])
            print(f"Input file: {input_file.name}")
            print(f"Input size: {input_file.stat().st_size:,} bytes")

            # Set output file
            output_file = TEST_OUTPUT / f"CLEANED_{test_case['name']}_{input_file.name}"

            # Clean the document
            print(f"\n🔄 Processing with intelligent content analysis...")
            result = cleaner.clean_document(input_file, output_file)

            # Display results
            if result.success:
                print(f"\n✅ SUCCESS")
                print(f"   Original: {result.original_size:,} bytes")
                print(f"   Cleaned:  {result.cleaned_size:,} bytes")
                print(f"   Reduction: {result.reduction_percentage:.1f}%")
                print(f"   Processing time: {result.processing_time:.2f}s")
                print(f"   LLM cost: ${result.llm_cost:.6f}")

                if result.removed_sections:
                    print(f"\n   Sections removed ({len(result.removed_sections)}):")
                    for section in result.removed_sections[:10]:  # Show first 10
                        print(f"     - {section}")
                    if len(result.removed_sections) > 10:
                        print(f"     ... and {len(result.removed_sections) - 10} more")

                if result.warnings:
                    print(f"\n   ⚠️  Warnings:")
                    for warning in result.warnings:
                        print(f"     - {warning}")

                print(f"\n   📄 Output saved to: {output_file.name}")

                results.append({
                    "name": test_case['name'],
                    "success": True,
                    "input_size": result.original_size,
                    "output_size": result.cleaned_size,
                    "reduction": result.reduction_percentage,
                    "cost": result.llm_cost,
                    "processing_time": result.processing_time,
                    "output_file": output_file
                })

            else:
                print(f"\n❌ FAILED")
                print(f"   Error: {result.error_message}")

                results.append({
                    "name": test_case['name'],
                    "success": False,
                    "error": result.error_message
                })

        except Exception as e:
            print(f"\n❌ EXCEPTION")
            print(f"   Error: {e}")

            results.append({
                "name": test_case['name'],
                "success": False,
                "error": str(e)
            })

    # Print summary
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")

    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    print(f"\n📊 Results: {len(successful)}/{len(results)} successful")

    if successful:
        total_cost = sum(r["cost"] for r in successful)
        avg_reduction = sum(r["reduction"] for r in successful) / len(successful)
        avg_time = sum(r["processing_time"] for r in successful) / len(successful)

        print(f"\n💰 Total LLM cost: ${total_cost:.6f}")
        print(f"📉 Average reduction: {avg_reduction:.1f}%")
        print(f"⏱️  Average processing time: {avg_time:.2f}s")

        print(f"\n✅ Successful cleanings:")
        for r in successful:
            print(f"   {r['name']:12} - {r['reduction']:5.1f}% reduction, ${r['cost']:.6f}")

    if failed:
        print(f"\n❌ Failed cleanings:")
        for r in failed:
            print(f"   {r['name']:12} - {r.get('error', 'Unknown error')}")

    print(f"\n\n{'='*80}")
    print("NEXT STEPS")
    print(f"{'='*80}")
    print(f"\n1. Manually verify cleaned files in: {TEST_OUTPUT}")
    print(f"2. Check that only main documentation content remains")
    print(f"3. Verify no important content was removed")
    print(f"4. Compare with original files to see what was removed")
    print()
    print("Manual verification commands:")
    for r in successful:
        print(f"  open '{r['output_file']}'")

    return len(failed) == 0


if __name__ == "__main__":
    success = test_intelligent_cleaning()
    sys.exit(0 if success else 1)
