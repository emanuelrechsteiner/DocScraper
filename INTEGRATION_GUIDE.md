# PostScraperCleaner: Integration Guide

**Version**: 1.0
**Last Updated**: 2025-01-07
**Status**: Production Ready

---

## Table of Contents

1. [Integration Overview](#integration-overview)
2. [DocScraper Pipeline Integration](#docscraper-pipeline-integration)
3. [Python Integration Examples](#python-integration-examples)
4. [Error Handling Strategies](#error-handling-strategies)
5. [Monitoring and Logging](#monitoring-and-logging)
6. [Pipeline Workflows](#pipeline-workflows)
7. [Advanced Patterns](#advanced-patterns)
8. [Troubleshooting Integration Issues](#troubleshooting-integration-issues)

---

## Integration Overview

### What PostScraperCleaner Does in Your Pipeline

```
DocScraper (Raw Markdown)
        ↓
PostScraperCleaner (This Tool)
   ├─ Rule-based cleaning (14 patterns)
   ├─ Optional LLM validation
   ├─ Chunk optimization
   └─ Quality metrics
        ↓
Your System (Vector DB, Search, etc.)
```

### Integration Points

1. **Input**: Markdown files from DocScraper
2. **Processing**: 3-phase cleaning pipeline
3. **Output**: Cleaned markdown files
4. **Feedback**: Statistics and metrics
5. **Error Handling**: Graceful recovery

### When to Integrate

- ✅ After scraping documents
- ✅ Before vector database ingestion
- ✅ Before content indexing
- ✅ For quality assurance workflows

---

## DocScraper Pipeline Integration

### Basic DocScraper → PostScraperCleaner Flow

```python
import subprocess
from pathlib import Path
from PostScraperCleaner import PostScraperCleaner, CleaningConfig

# Step 1: Run DocScraper (your existing script)
print("Step 1: Running DocScraper...")
# Your DocScraper command here
# Outputs to: scraped_docs/

# Step 2: Configure PostScraperCleaner
print("Step 2: Configuring PostScraperCleaner...")
config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
    enable_chunk_optimization=True,
    target_chunk_size=512,
)

# Step 3: Clean documents
print("Step 3: Cleaning documents...")
cleaner = PostScraperCleaner(config)

input_dir = Path("scraped_docs")
output_dir = Path("cleaned_docs")

results = cleaner.clean_batch(input_dir, output_dir)

# Step 4: Report results
print(f"Processed: {len(results)} documents")
successful = [r for r in results if r.success]
print(f"Success rate: {len(successful)}/{len(results)}")

stats = cleaner.get_statistics()
print(f"Overall reduction: {stats['overall_reduction_percentage']:.1f}%")
```

### Docker Integration

**Dockerfile**:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy PostScraperCleaner
COPY PostScraperCleaner.py .
COPY cleaning_rules.py .
COPY llm_cleaner.py .
COPY chunk_optimizer.py .

# Copy your input data
COPY ./scraped_docs /data/input

# Run cleaning
RUN python -c "
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

config = CleaningConfig()
cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(Path('/data/input'), Path('/data/output'))
print(f'Cleaned {len(results)} documents')
"

# Output will be in /data/output
```

**Usage**:
```bash
docker build -t postcleaner .
docker run -v $(pwd)/scraped_docs:/data/input \
           -v $(pwd)/cleaned_docs:/data/output \
           postcleaner
```

---

## Python Integration Examples

### Example 1: Simple Integration

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

# Minimal integration
cleaner = PostScraperCleaner(CleaningConfig())
results = cleaner.clean_batch(
    Path("input_docs"),
    Path("output_docs")
)

# Check results
for result in results:
    if result.success:
        print(f"✓ {result.input_file.name}")
    else:
        print(f"✗ {result.input_file.name}")
```

### Example 2: With Progress Tracking

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def progress_callback(update):
    """Handle progress updates"""
    if update['type'] == 'progress':
        processed = update['processed']
        total = update['total']
        current = update['current_file']
        percentage = (processed / total) * 100
        print(f"[{percentage:.0f}%] {current}")
    elif update['type'] == 'error':
        print(f"Error: {update['message']}")

config = CleaningConfig()
cleaner = PostScraperCleaner(config, progress_callback=progress_callback)

results = cleaner.clean_batch(
    Path("input_docs"),
    Path("output_docs")
)
```

### Example 3: With Quality Control

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import json

config = CleaningConfig(
    enable_llm_validation=True,
    openai_api_key="sk-...",
    llm_confidence_threshold=0.90,
)

cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(Path("input"), Path("output"))

# Separate results by quality
high_quality = [r for r in results if r.success and r.llm_validation]
standard_quality = [r for r in results if r.success and not r.llm_validation]
failed = [r for r in results if not r.success]

print(f"High quality (LLM validated): {len(high_quality)}")
print(f"Standard quality: {len(standard_quality)}")
print(f"Failed: {len(failed)}")

# Export statistics
with open("results.json", "w") as f:
    json.dump({
        "total": len(results),
        "high_quality": len(high_quality),
        "standard_quality": len(standard_quality),
        "failed": len(failed),
        "overall_reduction": cleaner.get_statistics()['overall_reduction_percentage'],
    }, f, indent=2)
```

### Example 4: Incremental Integration

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

config = CleaningConfig()
cleaner = PostScraperCleaner(config)

# Process documents in batches
input_dir = Path("scraped_docs")
output_dir = Path("cleaned_docs")

# Only process new files
processed_files = set(f.stem for f in output_dir.glob("*.md"))
new_files = [
    f for f in input_dir.glob("*.md")
    if f.stem not in processed_files
]

if new_files:
    print(f"Processing {len(new_files)} new documents...")

    # Create temp directory for batch
    temp_dir = input_dir / ".temp"
    temp_dir.mkdir(exist_ok=True)

    for file in new_files:
        # Copy to temp
        temp_file = temp_dir / file.name
        temp_file.write_text(file.read_text())

    # Batch process
    results = cleaner.clean_batch(temp_dir, output_dir)

    # Cleanup
    for f in temp_dir.glob("*.md"):
        f.unlink()
    temp_dir.rmdir()
else:
    print("No new documents to process")
```

---

## Error Handling Strategies

### Strategy 1: Graceful Degradation

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def integrate_with_fallback():
    """Integration with fallback to basic cleaning"""
    config = CleaningConfig(
        enable_llm_validation=True,  # Try LLM first
        openai_api_key="sk-...",
    )

    try:
        cleaner = PostScraperCleaner(config)
        results = cleaner.clean_batch(Path("input"), Path("output"))
    except Exception as e:
        # Fallback: Disable LLM, use basic cleaning
        print(f"LLM integration failed: {e}")
        print("Falling back to basic cleaning...")

        config_fallback = CleaningConfig(
            enable_llm_validation=False,
        )
        cleaner = PostScraperCleaner(config_fallback)
        results = cleaner.clean_batch(Path("input"), Path("output"))

    return results
```

### Strategy 2: Per-Document Error Recovery

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def clean_with_recovery():
    """Clean documents, retry failed ones"""
    config = CleaningConfig()
    cleaner = PostScraperCleaner(config)

    input_dir = Path("input")
    output_dir = Path("output")

    # First pass
    results = cleaner.clean_batch(input_dir, output_dir)

    # Identify failures
    failures = [r for r in results if not r.success]

    if failures:
        print(f"Retrying {len(failures)} failed documents...")

        # Retry with simpler config
        retry_config = CleaningConfig(
            remove_navigation=True,  # Keep only essential
            remove_headers_footers=True,
            remove_boilerplate=False,  # Skip this
            enable_chunk_optimization=False,
        )
        retry_cleaner = PostScraperCleaner(retry_config)

        for failure in failures:
            try:
                result = retry_cleaner.clean_document(
                    failure.input_file,
                    output_dir / failure.input_file.name
                )
                if result.success:
                    print(f"✓ Recovered: {failure.input_file.name}")
            except Exception as e:
                print(f"✗ Unrecoverable: {failure.input_file.name}")
```

### Strategy 3: Validation Before Processing

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def validate_and_clean():
    """Validate inputs before processing"""
    input_dir = Path("input")

    # Validate inputs exist
    if not input_dir.exists():
        raise ValueError(f"Input directory not found: {input_dir}")

    md_files = list(input_dir.glob("*.md"))
    if not md_files:
        raise ValueError(f"No markdown files found in {input_dir}")

    # Validate file sizes
    max_size_mb = 10
    oversized = [
        f for f in md_files
        if f.stat().st_size > max_size_mb * 1024 * 1024
    ]
    if oversized:
        print(f"Warning: {len(oversized)} files exceed {max_size_mb}MB:")
        for f in oversized:
            print(f"  {f.name}")

    # Validate configuration
    config = CleaningConfig()
    if not config.remove_navigation and not config.remove_boilerplate:
        raise ValueError("Must enable at least one cleaning option")

    # Safe to process
    cleaner = PostScraperCleaner(config)
    return cleaner.clean_batch(input_dir, Path("output"))
```

---

## Monitoring and Logging

### Strategy 1: Statistics Export

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import json
import csv

config = CleaningConfig()
cleaner = PostScraperCleaner(config)

results = cleaner.clean_batch(Path("input"), Path("output"))
stats = cleaner.get_statistics()

# Export as JSON
with open("stats.json", "w") as f:
    json.dump(stats, f, indent=2)

# Export results as CSV
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "filename", "success", "original_size", "cleaned_size", "reduction_%"
    ])
    for result in results:
        writer.writerow([
            result.input_file.name,
            result.success,
            result.original_size,
            result.cleaned_size,
            result.reduction_percentage,
        ])

print("Statistics exported to stats.json and results.csv")
```

### Strategy 2: Real-time Monitoring

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import time

class MonitoringCallback:
    def __init__(self):
        self.start_time = time.time()
        self.processed = 0
        self.total = 0

    def __call__(self, update):
        if update['type'] == 'progress':
            self.processed = update['processed']
            self.total = update['total']

            elapsed = time.time() - self.start_time
            rate = self.processed / elapsed if elapsed > 0 else 0
            remaining = (self.total - self.processed) / rate if rate > 0 else 0

            print(
                f"[{self.processed}/{self.total}] "
                f"Rate: {rate:.1f} files/sec "
                f"ETA: {remaining:.0f}s"
            )

config = CleaningConfig()
monitor = MonitoringCallback()
cleaner = PostScraperCleaner(config, progress_callback=monitor)

results = cleaner.clean_batch(Path("input"), Path("output"))
```

### Strategy 3: Logging Integration

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('postcleaner.log'),
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)

def log_results(results, stats):
    """Log processing results"""
    logger.info(f"Processing completed: {len(results)} documents")

    successful = [r for r in results if r.success]
    logger.info(f"Success rate: {len(successful)}/{len(results)}")

    logger.info(f"Overall reduction: {stats['overall_reduction_percentage']:.1f}%")

    failures = [r for r in results if not r.success]
    if failures:
        logger.warning(f"Failed documents: {len(failures)}")
        for failure in failures:
            logger.warning(f"  - {failure.input_file.name}")

config = CleaningConfig()
cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(Path("input"), Path("output"))
stats = cleaner.get_statistics()

log_results(results, stats)
```

---

## Pipeline Workflows

### Workflow 1: Scrape → Clean → Index

```python
from pathlib import Path
from PostScraperCleaner import PostScraperCleaner, CleaningConfig

# Setup directories
scraped_dir = Path("data/scraped")
cleaned_dir = Path("data/cleaned")
indexed_dir = Path("data/indexed")

# Step 1: Scrape (your existing DocScraper code)
print("Step 1: Scraping documents...")
# ... your scraping code here ...

# Step 2: Clean
print("Step 2: Cleaning documents...")
config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
    enable_chunk_optimization=True,
)
cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(scraped_dir, cleaned_dir)

# Step 3: Index
print("Step 3: Indexing cleaned documents...")
for result in results:
    if result.success:
        cleaned_file = cleaned_dir / result.input_file.name
        # ... your indexing code here ...

print("Pipeline complete!")
```

### Workflow 2: Incremental with Quality Gates

```python
from pathlib import Path
from PostScraperCleaner import PostScraperCleaner, CleaningConfig

def process_with_quality_gates():
    """Process documents with quality thresholds"""
    input_dir = Path("input")
    output_dir = Path("output")
    rejected_dir = Path("rejected")

    rejected_dir.mkdir(exist_ok=True)

    # First pass: Basic cleaning
    config_basic = CleaningConfig(
        enable_llm_validation=False,
    )
    cleaner = PostScraperCleaner(config_basic)
    results = cleaner.clean_batch(input_dir, output_dir)

    # Second pass: Quality validation
    config_qa = CleaningConfig(
        enable_llm_validation=True,
        openai_api_key="sk-...",
        llm_confidence_threshold=0.90,
    )
    qa_cleaner = PostScraperCleaner(config_qa)

    for result in results:
        if result.reduction_percentage < 5:
            # Low reduction = possibly not cleaned well
            qa_result = qa_cleaner.clean_document(
                result.input_file,
                rejected_dir / result.input_file.name
            )
            if not qa_result.success:
                print(f"Rejected: {result.input_file.name}")

process_with_quality_gates()
```

### Workflow 3: Batch with Checkpoints

```python
from pathlib import Path
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
import json

def batch_with_checkpoints():
    """Process large batches with progress checkpoints"""
    input_dir = Path("input")
    output_dir = Path("output")
    checkpoint_file = Path("checkpoint.json")

    # Load existing checkpoint
    if checkpoint_file.exists():
        with open(checkpoint_file) as f:
            checkpoint = json.load(f)
        processed = set(checkpoint.get('processed', []))
    else:
        processed = set()

    # Get files to process
    all_files = list(input_dir.glob("*.md"))
    files_to_process = [f for f in all_files if f.stem not in processed]

    print(f"Already processed: {len(processed)}")
    print(f"To process: {len(files_to_process)}")

    # Process in batches of 50
    config = CleaningConfig()
    cleaner = PostScraperCleaner(config)

    batch_size = 50
    for i in range(0, len(files_to_process), batch_size):
        batch = files_to_process[i:i+batch_size]

        # Create temp dir for batch
        temp_dir = input_dir / f".batch_{i}"
        temp_dir.mkdir(exist_ok=True)

        for file in batch:
            (temp_dir / file.name).write_text(file.read_text())

        # Process batch
        results = cleaner.clean_batch(temp_dir, output_dir)

        # Update checkpoint
        for result in results:
            if result.success:
                processed.add(result.input_file.stem)

        with open(checkpoint_file, "w") as f:
            json.dump({
                'processed': list(processed),
                'total': len(all_files),
                'timestamp': str(__import__('datetime').datetime.now()),
            }, f)

        print(f"Batch {i//batch_size + 1} complete. Total: {len(processed)}/{len(all_files)}")

        # Cleanup
        for f in temp_dir.glob("*"):
            f.unlink()
        temp_dir.rmdir()

batch_with_checkpoints()
```

---

## Advanced Patterns

### Pattern 1: Conditional Configuration

```python
from PostScraperCleaner import CleaningConfig, PostScraperCleaner
from pathlib import Path
import os

def get_config_from_environment():
    """Build config from environment"""
    return CleaningConfig(
        remove_navigation=os.getenv("REMOVE_NAV", "true").lower() == "true",
        remove_headers_footers=os.getenv("REMOVE_HEADERS", "true").lower() == "true",
        remove_boilerplate=os.getenv("REMOVE_BOILERPLATE", "true").lower() == "true",
        enable_llm_validation=os.getenv("ENABLE_LLM", "false").lower() == "true",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        target_chunk_size=int(os.getenv("CHUNK_SIZE", "512")),
    )

config = get_config_from_environment()
cleaner = PostScraperCleaner(config)
```

### Pattern 2: File-type Based Routing

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def route_by_content_type(input_file: Path, output_dir: Path):
    """Route processing based on content size/type"""
    size_mb = input_file.stat().st_size / (1024 * 1024)

    if size_mb < 0.5:
        # Small files: High quality
        config = CleaningConfig(
            enable_llm_validation=True,
            openai_api_key="sk-...",
        )
    elif size_mb < 5:
        # Medium files: Balanced
        config = CleaningConfig(
            enable_llm_validation=False,
            enable_chunk_optimization=True,
        )
    else:
        # Large files: Speed focused
        config = CleaningConfig(
            enable_llm_validation=False,
            enable_chunk_optimization=False,
        )

    cleaner = PostScraperCleaner(config)
    return cleaner.clean_document(input_file, output_dir / input_file.name)
```

### Pattern 3: Pipeline Composition

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
from typing import Callable

class CleaningPipeline:
    """Composable pipeline for document processing"""

    def __init__(self):
        self.steps = []

    def add_step(self, name: str, func: Callable):
        """Add processing step"""
        self.steps.append((name, func))
        return self

    def execute(self, input_dir: Path, output_dir: Path):
        """Execute pipeline"""
        current_input = input_dir

        for name, func in self.steps:
            print(f"Running: {name}")
            current_output = output_dir / f"step_{name}"
            current_output.mkdir(exist_ok=True)

            func(current_input, current_output)
            current_input = current_output

        print("Pipeline complete")

# Usage
pipeline = CleaningPipeline()
pipeline.add_step("clean", lambda i, o: PostScraperCleaner(CleaningConfig()).clean_batch(i, o))

# Could add more steps here
# pipeline.add_step("validate", validate_func)
# pipeline.add_step("chunk", chunk_func)

pipeline.execute(Path("input"), Path("output"))
```

---

## Troubleshooting Integration Issues

### Issue 1: "Module Not Found: PostScraperCleaner"

**Cause**: Files not in Python path
**Solution**:
```python
import sys
sys.path.insert(0, "/path/to/PostScraperCleaner")

from PostScraperCleaner import PostScraperCleaner
```

### Issue 2: "Permission Denied" on Output

**Cause**: Output directory not writable
**Solution**:
```python
output_dir = Path("output")
output_dir.mkdir(parents=True, exist_ok=True)

# Verify writable
test_file = output_dir / ".test"
test_file.touch()
test_file.unlink()

# Now safe to process
```

### Issue 3: "API Key Invalid" During Integration

**Cause**: API key not set or invalid
**Solution**:
```python
import os

# Check environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not set")

# Validate format
if not api_key.startswith("sk-"):
    raise ValueError("Invalid API key format")
```

### Issue 4: "Out of Memory" on Large Batches

**Cause**: Processing too many large files simultaneously
**Solution**:
```python
# Process in smaller batches
results = []
batch_size = 10

for i in range(0, len(all_files), batch_size):
    batch = all_files[i:i+batch_size]
    batch_results = cleaner.clean_batch(batch_dir, output_dir)
    results.extend(batch_results)

    # Free memory between batches
    import gc
    gc.collect()
```

### Issue 5: "Timeout" During LLM Integration

**Cause**: API requests taking too long
**Solution**:
```python
# Reduce rate limit
config = CleaningConfig(
    enable_llm_validation=True,
    rate_limit_rpm=100,  # More conservative
)

# Or skip LLM
config = CleaningConfig(
    enable_llm_validation=False,
)
```

---

## Summary

**Key Integration Points**:

1. **Input**: Markdown files from DocScraper
2. **Configuration**: Use CleaningConfig for options
3. **Processing**: Call clean_batch() for batch operations
4. **Error Handling**: Implement fallbacks and recovery
5. **Monitoring**: Track progress and export statistics
6. **Output**: Cleaned markdown ready for next stage

**Best Practices**:

- ✅ Always validate inputs before processing
- ✅ Implement error recovery strategies
- ✅ Monitor progress for long operations
- ✅ Export statistics for quality tracking
- ✅ Use checkpoints for large batches
- ✅ Gracefully handle API failures

**Next Steps**:

1. Choose integration pattern (basic, quality-gated, incremental)
2. Implement error handling strategy
3. Add monitoring/logging
4. Test with sample documents
5. Deploy to production

---

**Version**: 1.0 | **Status**: Production Ready | **Last Updated**: 2025-01-07
