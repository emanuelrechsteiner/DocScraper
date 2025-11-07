# PostScraperCleaner: Examples & Recipes

**Version**: 1.0
**Last Updated**: 2025-01-07
**Status**: Production Ready

---

## Table of Contents

1. [Basic Examples](#basic-examples)
2. [Common Recipes](#common-recipes)
3. [Real-World Workflows](#real-world-workflows)
4. [Advanced Patterns](#advanced-patterns)
5. [Integration Examples](#integration-examples)
6. [Error Handling Examples](#error-handling-examples)

---

## Basic Examples

### Example 1: Simplest Usage

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

# Create cleaner with defaults
cleaner = PostScraperCleaner(CleaningConfig())

# Clean one file
result = cleaner.clean_document(
    Path("input.md"),
    Path("output.md")
)

# Check result
if result.success:
    print(f"✓ Cleaned successfully")
    print(f"  Size reduction: {result.reduction_percentage:.1f}%")
else:
    print(f"✗ Failed to clean")
```

---

### Example 2: Batch Processing

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

# Create cleaner
cleaner = PostScraperCleaner(CleaningConfig())

# Process folder
results = cleaner.clean_batch(
    Path("input_docs"),
    Path("output_docs")
)

# Print summary
print(f"Processed: {len(results)} files")
for result in results:
    status = "✓" if result.success else "✗"
    print(f"{status} {result.input_file.name}")

# Show statistics
stats = cleaner.get_statistics()
print(f"\nOverall reduction: {stats['overall_reduction_percentage']:.1f}%")
```

---

### Example 3: With Custom Configuration

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

# Create custom config
config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
    enable_chunk_optimization=True,
    target_chunk_size=512,
)

# Create cleaner with config
cleaner = PostScraperCleaner(config)

# Process
results = cleaner.clean_batch(Path("input"), Path("output"))

# Print results
successful = [r for r in results if r.success]
print(f"Success rate: {len(successful)}/{len(results)}")
```

---

### Example 4: With Progress Tracking

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def on_progress(update):
    """Handle progress updates"""
    if update['type'] == 'progress':
        processed = update['processed']
        total = update['total']
        current_file = update['current_file']
        percent = (processed / total) * 100
        print(f"[{percent:3.0f}%] {processed}/{total} - {current_file}")

# Create cleaner with progress callback
config = CleaningConfig()
cleaner = PostScraperCleaner(config, progress_callback=on_progress)

# Process (progress printed in real-time)
cleaner.clean_batch(Path("input"), Path("output"))
```

---

## Common Recipes

### Recipe 1: Simple CLI Tool

```python
#!/usr/bin/env python3
"""Simple command-line tool to clean markdown files"""

from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python clean.py <input_dir> <output_dir>")
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    if not input_dir.exists():
        print(f"Error: Input directory not found: {input_dir}")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Create cleaner
    config = CleaningConfig()
    cleaner = PostScraperCleaner(config)

    # Process
    results = cleaner.clean_batch(input_dir, output_dir)

    # Report
    successful = [r for r in results if r.success]
    print(f"\n✓ Success: {len(successful)}/{len(results)} files")

    if len(successful) < len(results):
        failed = [r for r in results if not r.success]
        print(f"✗ Failed: {len(failed)} files")
        for failure in failed:
            print(f"  - {failure.input_file.name}")

if __name__ == "__main__":
    main()
```

**Usage**:
```bash
python clean.py input_docs output_docs
```

---

### Recipe 2: Process with Quality Validation

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def process_with_quality_check():
    """Process documents and validate quality"""
    input_dir = Path("docs")
    good_output = Path("output/approved")
    review_output = Path("output/review")

    good_output.mkdir(parents=True, exist_ok=True)
    review_output.mkdir(parents=True, exist_ok=True)

    # First pass: Basic cleaning
    config = CleaningConfig(enable_llm_validation=False)
    cleaner = PostScraperCleaner(config)
    results = cleaner.clean_batch(input_dir, good_output)

    # Second pass: Review low-quality results
    for result in results:
        # Documents with low reduction might need review
        if result.success and result.reduction_percentage < 5:
            # Move to review folder
            output_file = good_output / result.input_file.name
            output_file.rename(review_output / result.input_file.name)
            print(f"Moved to review: {result.input_file.name}")

    print(f"Approved: {len(list(good_output.glob('*.md')))}")
    print(f"Needs review: {len(list(review_output.glob('*.md')))}")

process_with_quality_check()
```

---

### Recipe 3: Cost Estimation

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def estimate_llm_costs():
    """Estimate cost of LLM validation"""
    input_dir = Path("input")
    md_files = list(input_dir.glob("*.md"))

    # Estimate tokens per document
    total_size = sum(f.stat().st_size for f in md_files)
    avg_size = total_size / len(md_files) if md_files else 0

    # Approximate 1 token per 4 characters
    avg_tokens = avg_size / 4

    # OpenAI GPT-4o-mini pricing
    input_price = 0.150 / 1_000_000  # per token
    output_price = 0.600 / 1_000_000  # per token

    # Estimate input and output
    input_cost = avg_tokens * input_price
    output_tokens = 300  # Typical response
    output_cost = output_tokens * output_price

    cost_per_doc = input_cost + output_cost

    print(f"Documents: {len(md_files)}")
    print(f"Avg size: {avg_size/1024:.1f}KB")
    print(f"Avg tokens: {avg_tokens:.0f}")
    print(f"\nCost per document:")
    print(f"  Input: ${input_cost:.6f}")
    print(f"  Output: ${output_cost:.6f}")
    print(f"  Total: ${cost_per_doc:.6f}")
    print(f"\nBatch costs:")
    print(f"  10 docs: ${cost_per_doc * 10:.3f}")
    print(f"  100 docs: ${cost_per_doc * 100:.2f}")
    print(f"  1000 docs: ${cost_per_doc * 1000:.2f}")

estimate_llm_costs()
```

---

### Recipe 4: Save and Load Configuration

```python
import json
from PostScraperCleaner import CleaningConfig, PostScraperCleaner
from pathlib import Path

def save_config(config: CleaningConfig, path: str):
    """Save configuration to JSON"""
    config_dict = {
        "remove_navigation": config.remove_navigation,
        "remove_headers_footers": config.remove_headers_footers,
        "remove_boilerplate": config.remove_boilerplate,
        "enable_llm_validation": config.enable_llm_validation,
        "llm_confidence_threshold": config.llm_confidence_threshold,
        "enable_chunk_optimization": config.enable_chunk_optimization,
        "target_chunk_size": config.target_chunk_size,
        "overlap_size": config.overlap_size,
        "rate_limit_rpm": config.rate_limit_rpm,
    }

    with open(path, "w") as f:
        json.dump(config_dict, f, indent=2)
    print(f"Saved config to {path}")

def load_config(path: str) -> CleaningConfig:
    """Load configuration from JSON"""
    with open(path) as f:
        config_dict = json.load(f)

    return CleaningConfig(**config_dict)

# Save configuration
config = CleaningConfig(
    remove_navigation=True,
    target_chunk_size=512,
)
save_config(config, "my_config.json")

# Later, load and use
config = load_config("my_config.json")
cleaner = PostScraperCleaner(config)
```

---

### Recipe 5: Export Results

```python
import json
import csv
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def export_results(results, output_dir):
    """Export processing results in multiple formats"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Export as JSON
    json_file = output_dir / "results.json"
    json_data = [
        {
            "file": r.input_file.name,
            "success": r.success,
            "original_bytes": r.original_size,
            "cleaned_bytes": r.cleaned_size,
            "reduction_percent": r.reduction_percentage,
        }
        for r in results
    ]
    with open(json_file, "w") as f:
        json.dump(json_data, f, indent=2)
    print(f"Saved JSON: {json_file}")

    # Export as CSV
    csv_file = output_dir / "results.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "success", "original_bytes", "cleaned_bytes", "reduction_percent"])
        for r in results:
            writer.writerow([
                r.input_file.name,
                r.success,
                r.original_size,
                r.cleaned_size,
                f"{r.reduction_percentage:.1f}",
            ])
    print(f"Saved CSV: {csv_file}")

    # Export as plain text summary
    txt_file = output_dir / "summary.txt"
    with open(txt_file, "w") as f:
        f.write("PostScraperCleaner Results\n")
        f.write("=" * 50 + "\n\n")

        successful = [r for r in results if r.success]
        f.write(f"Total: {len(results)}\n")
        f.write(f"Successful: {len(successful)}\n")
        f.write(f"Failed: {len(results) - len(successful)}\n\n")

        if successful:
            avg_reduction = sum(r.reduction_percentage for r in successful) / len(successful)
            f.write(f"Average reduction: {avg_reduction:.1f}%\n")

    print(f"Saved text: {txt_file}")

# Use it
config = CleaningConfig()
cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(Path("input"), Path("output"))

export_results(results, "results_export")
```

---

## Real-World Workflows

### Workflow 1: Documentation Site Preparation

```python
"""
Prepare scraped documentation for knowledge base.
Scrape → Clean → Chunk → Index
"""

from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import json

def prepare_documentation():
    # Directories
    scraped_dir = Path("data/scraped_docs")
    cleaned_dir = Path("data/cleaned_docs")
    chunks_dir = Path("data/chunks")

    # Clean all documents
    print("Step 1: Cleaning documents...")
    config = CleaningConfig(
        remove_navigation=True,
        remove_headers_footers=True,
        remove_boilerplate=True,
        enable_chunk_optimization=True,
        target_chunk_size=512,
    )
    cleaner = PostScraperCleaner(config)
    results = cleaner.clean_batch(scraped_dir, cleaned_dir)

    # Report cleaning
    successful = [r for r in results if r.success]
    print(f"✓ Cleaned {len(successful)}/{len(results)} documents")

    # Chunk documents for embeddings
    print("\nStep 2: Chunking documents...")
    chunks_data = []

    for result in successful:
        cleaned_file = cleaned_dir / result.input_file.name
        chunks = cleaned_file.read_text().split("##")

        for i, chunk in enumerate(chunks):
            if chunk.strip():
                chunks_data.append({
                    "source_file": result.input_file.name,
                    "chunk_id": f"{result.input_file.stem}_{i}",
                    "content": chunk.strip(),
                })

    print(f"✓ Created {len(chunks_data)} chunks")

    # Save chunks
    with open(chunks_dir / "chunks.json", "w") as f:
        json.dump(chunks_data, f, indent=2)

    print(f"\nDocumentation prepared in {cleaned_dir}")

prepare_documentation()
```

---

### Workflow 2: API Documentation Cleaning

```python
"""
Clean API documentation with quality validation
"""

from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import os

def clean_api_docs():
    input_dir = Path("api_docs/raw")
    output_dir = Path("api_docs/cleaned")

    config = CleaningConfig(
        remove_navigation=True,
        remove_headers_footers=True,
        remove_boilerplate=True,
        enable_llm_validation=True,  # Quality check
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        enable_chunk_optimization=True,
    )

    cleaner = PostScraperCleaner(config)
    results = cleaner.clean_batch(input_dir, output_dir)

    # Analyze results
    high_quality = [r for r in results if r.llm_validation]
    standard = [r for r in results if r.success and not r.llm_validation]
    failed = [r for r in results if not r.success]

    print(f"Quality Report:")
    print(f"  High quality (LLM validated): {len(high_quality)}")
    print(f"  Standard quality: {len(standard)}")
    print(f"  Failed: {len(failed)}")

    # Cost analysis
    total_cost = sum(r.llm_cost for r in results)
    print(f"\nCost Analysis:")
    print(f"  Total cost: ${total_cost:.2f}")
    print(f"  Cost per doc: ${total_cost/len(results):.4f}")

clean_api_docs()
```

---

### Workflow 3: Blog Archive Cleaning

```python
"""
Clean and organize blog post archive
"""

from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
from datetime import datetime

def organize_blog_posts():
    input_dir = Path("blog_posts")
    output_base = Path("blog_clean")

    # Create cleaner
    config = CleaningConfig()
    cleaner = PostScraperCleaner(config)

    # Process by date
    current_month = None
    for file in sorted(input_dir.glob("*.md")):
        # Extract date from filename (assuming format: YYYY-MM-DD-title.md)
        try:
            date_str = file.stem.split("-")[0:3]
            month = f"{date_str[0]}-{date_str[1]}"
        except:
            month = "undated"

        # Create monthly directories
        if month != current_month:
            month_dir = output_base / month
            month_dir.mkdir(parents=True, exist_ok=True)
            current_month = month

        # Clean document
        cleaner.clean_document(file, month_dir / file.name)

    # Report
    total = len(list(output_base.glob("**/*.md")))
    print(f"✓ Organized {total} blog posts by month")

organize_blog_posts()
```

---

## Advanced Patterns

### Pattern 1: Conditional Cleaning Based on File Size

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def smart_clean(input_dir: Path, output_dir: Path):
    """Choose cleaning strategy based on file size"""
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in input_dir.glob("*.md"):
        size_kb = file.stat().st_size / 1024

        if size_kb < 10:
            # Small files: High quality
            config = CleaningConfig(
                remove_navigation=True,
                remove_headers_footers=True,
                remove_boilerplate=True,
            )
        elif size_kb < 100:
            # Medium: Balanced
            config = CleaningConfig(
                remove_navigation=True,
                remove_headers_footers=True,
            )
        else:
            # Large: Speed priority
            config = CleaningConfig(
                remove_navigation=True,
            )

        cleaner = PostScraperCleaner(config)
        result = cleaner.clean_document(file, output_dir / file.name)

        status = "✓" if result.success else "✗"
        print(f"{status} {file.name} ({size_kb:.0f}KB)")

smart_clean(Path("input"), Path("output"))
```

---

### Pattern 2: Incremental Processing with Resume

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import json

def resume_capable_processing(input_dir: Path, output_dir: Path):
    """Process with ability to resume from interruption"""
    output_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_file = output_dir / ".checkpoint.json"

    # Load checkpoint
    if checkpoint_file.exists():
        with open(checkpoint_file) as f:
            checkpoint = json.load(f)
        processed = set(checkpoint.get("processed", []))
        print(f"Resuming from checkpoint: {len(processed)} files already done")
    else:
        processed = set()

    # Get all files
    all_files = sorted(input_dir.glob("*.md"))
    remaining = [f for f in all_files if f.stem not in processed]

    print(f"Processing {len(remaining)} remaining files...")

    config = CleaningConfig()
    cleaner = PostScraperCleaner(config)

    for file in remaining:
        try:
            cleaner.clean_document(file, output_dir / file.name)
            processed.add(file.stem)

            # Save checkpoint
            with open(checkpoint_file, "w") as f:
                json.dump({
                    "processed": list(processed),
                    "total": len(all_files),
                }, f)

        except Exception as e:
            print(f"Error processing {file.name}: {e}")

    print(f"✓ Complete: {len(processed)}/{len(all_files)} files")

resume_capable_processing(Path("input"), Path("output"))
```

---

## Integration Examples

### Example: With Existing DocScraper Pipeline

```python
"""Integration with DocScraper"""

from SimpleDocScraper import DocScraper  # Your existing scraper
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def full_pipeline():
    # Directories
    raw_dir = Path("raw_html")
    scraped_dir = Path("scraped_md")
    cleaned_dir = Path("cleaned_md")

    # Step 1: Scrape HTML to Markdown
    print("Step 1: Scraping...")
    scraper = DocScraper()
    scraper.scrape_and_save(raw_dir, scraped_dir)

    # Step 2: Clean Markdown
    print("Step 2: Cleaning...")
    config = CleaningConfig(
        remove_navigation=True,
        remove_headers_footers=True,
        enable_chunk_optimization=True,
    )
    cleaner = PostScraperCleaner(config)
    results = cleaner.clean_batch(scraped_dir, cleaned_dir)

    # Step 3: Report
    successful = [r for r in results if r.success]
    print(f"\n✓ Pipeline complete: {len(successful)}/{len(results)} successful")

    stats = cleaner.get_statistics()
    print(f"Average reduction: {stats['overall_reduction_percentage']:.1f}%")

full_pipeline()
```

---

## Error Handling Examples

### Example: Robust Batch Processing

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("cleaning.log"),
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)

def robust_batch_process():
    """Batch processing with comprehensive error handling"""
    input_dir = Path("input")
    output_dir = Path("output")
    error_dir = Path("errors")

    output_dir.mkdir(parents=True, exist_ok=True)
    error_dir.mkdir(parents=True, exist_ok=True)

    # Basic cleaner
    config = CleaningConfig()
    cleaner = PostScraperCleaner(config)

    results = {"success": [], "failed": []}

    for file in input_dir.glob("*.md"):
        try:
            logger.info(f"Processing {file.name}...")

            result = cleaner.clean_document(file, output_dir / file.name)

            if result.success:
                results["success"].append(file.name)
                logger.info(f"✓ {file.name}")
            else:
                results["failed"].append({
                    "file": file.name,
                    "reason": "Processing failed",
                })
                logger.warning(f"✗ {file.name} - Processing failed")

        except PermissionError as e:
            results["failed"].append({
                "file": file.name,
                "reason": f"Permission denied: {e}",
            })
            logger.error(f"Permission error on {file.name}")

        except MemoryError as e:
            results["failed"].append({
                "file": file.name,
                "reason": "Out of memory",
            })
            logger.error(f"Memory error on {file.name}")

        except Exception as e:
            results["failed"].append({
                "file": file.name,
                "reason": str(e),
            })
            logger.error(f"Unexpected error on {file.name}: {e}")

    # Report
    logger.info(f"\nProcessing complete:")
    logger.info(f"  Successful: {len(results['success'])}")
    logger.info(f"  Failed: {len(results['failed'])}")

    if results["failed"]:
        logger.warning(f"Failed files:")
        for failure in results["failed"]:
            logger.warning(f"  - {failure['file']}: {failure['reason']}")

robust_batch_process()
```

---

## Summary

**Quick Recipe Reference**:

- **Simple**: Use Example 1 (Simplest Usage)
- **Batch**: Use Example 2 (Batch Processing)
- **Custom Config**: Use Example 3 (Custom Configuration)
- **Progress**: Use Example 4 (Progress Tracking)
- **CLI Tool**: Use Recipe 1 (Simple CLI Tool)
- **Quality Control**: Use Recipe 2 (Quality Validation)
- **Cost Estimate**: Use Recipe 3 (Cost Estimation)
- **Config Save/Load**: Use Recipe 4 (Save/Load)
- **Export Results**: Use Recipe 5 (Export Results)

**Real-World Workflows**:

- **Documentation**: Workflow 1 (Documentation Site)
- **API Docs**: Workflow 2 (API Documentation)
- **Blog Posts**: Workflow 3 (Blog Archive)

**Advanced**:

- **Smart Cleaning**: Pattern 1 (Conditional by Size)
- **Resume Processing**: Pattern 2 (Incremental with Resume)
- **Full Pipeline**: Integration Example (with DocScraper)
- **Error Handling**: Example (Robust Batch)

---

**Version**: 1.0 | **Status**: Production Ready | **Last Updated**: 2025-01-07
