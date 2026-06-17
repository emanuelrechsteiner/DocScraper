#!/usr/bin/env python3
"""
Example: Directory Structure Mirroring

This example demonstrates the new clean_directory_tree() method that mirrors
input directory structure with '_cleaned' suffix appended to subdirectory names.

Transformation Example:
    Input:  /input/docs/chroma/file.md
    Output: /output/docs_cleaned/chroma_cleaned/file.md
"""

import os
from pathlib import Path
from PostScraperCleaner import PostScraperCleaner, CleaningConfig

# Load environment variables from .env
def load_env():
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

load_env()

# Configure cleaner with intelligent analysis
config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
    enable_llm_validation=True,  # Enable intelligent cleaning with GPT-4o
    enable_chunk_optimization=False,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    rate_limit_rpm=500
)

# Initialize cleaner
cleaner = PostScraperCleaner(config)

# Example: Process entire directory tree with mirrored structure
input_root = Path("/path/to/input/docs")
output_root = Path("/path/to/output/docs")

# Process all markdown files recursively
results = cleaner.clean_directory_tree(
    input_root=input_root,
    output_root=output_root,
    pattern="**/*.md"  # Recursive search for all .md files
)

# Print summary
successful = sum(1 for r in results if r.success)
failed = len(results) - successful
total_cost = sum(r.llm_cost for r in results)
avg_reduction = sum(r.reduction_percentage for r in results if r.success) / successful if successful > 0 else 0

print(f"\nProcessing complete:")
print(f"✅ Successful: {successful}/{len(results)}")
print(f"❌ Failed: {failed}/{len(results)}")
print(f"💰 Total LLM cost: ${total_cost:.6f}")
print(f"📉 Average reduction: {avg_reduction:.1f}%")
print(f"📁 Output directory: {output_root}")
