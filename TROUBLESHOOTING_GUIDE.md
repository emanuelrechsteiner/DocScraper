# PostScraperCleaner: Troubleshooting Guide

**Version**: 1.0
**Last Updated**: 2025-01-07
**Status**: Production Ready

---

## Table of Contents

1. [Quick Diagnosis](#quick-diagnosis)
2. [Common Errors](#common-errors)
3. [Performance Issues](#performance-issues)
4. [API Integration Issues](#api-integration-issues)
5. [File and Format Issues](#file-and-format-issues)
6. [Memory and Resource Issues](#memory-and-resource-issues)
7. [GUI Issues](#gui-issues)
8. [Debugging Techniques](#debugging-techniques)
9. [Getting Help](#getting-help)

---

## Quick Diagnosis

### Symptom Checker

**Processing is slow?**
→ See [Performance Issues](#performance-issues)

**Getting error messages?**
→ Search [Common Errors](#common-errors)

**API key problems?**
→ See [API Integration Issues](#api-integration-issues)

**Files not being processed?**
→ See [File and Format Issues](#file-and-format-issues)

**Out of memory?**
→ See [Memory and Resource Issues](#memory-and-resource-issues)

**GUI not responding?**
→ See [GUI Issues](#gui-issues)

---

## Common Errors

### Error 1: "ModuleNotFoundError: No module named 'PostScraperCleaner'"

**Symptoms**:
```
ModuleNotFoundError: No module named 'PostScraperCleaner'
```

**Causes**:
1. PostScraperCleaner.py not in Python path
2. File not in same directory as script
3. Working directory different

**Solutions**:

**Option 1: Copy files to project directory**
```bash
cp PostScraperCleaner.py /your/project/
cp cleaning_rules.py /your/project/
cp llm_cleaner.py /your/project/
cp chunk_optimizer.py /your/project/
```

**Option 2: Add to Python path**
```python
import sys
sys.path.insert(0, "/path/to/PostScraperCleaner/files")

from PostScraperCleaner import PostScraperCleaner
```

**Option 3: Install to site-packages (if using virtual env)**
```bash
# Create symlink or copy
cp *.py ~/.virtualenvs/myenv/lib/python3.9/site-packages/
```

---

### Error 2: "FileNotFoundError: [Errno 2] No such file or directory"

**Symptoms**:
```
FileNotFoundError: [Errno 2] No such file or directory: 'input_folder'
```

**Causes**:
1. Input folder doesn't exist
2. Wrong path provided
3. Path uses backslashes on Linux/Mac
4. Output folder doesn't exist

**Solutions**:

```python
from pathlib import Path

# Verify input exists
input_dir = Path("input")
if not input_dir.exists():
    raise FileNotFoundError(f"Input directory not found: {input_dir}")

# Create output if needed
output_dir = Path("output")
output_dir.mkdir(parents=True, exist_ok=True)

# Always use Path for cross-platform compatibility
from PostScraperCleaner import PostScraperCleaner, CleaningConfig

cleaner = PostScraperCleaner(CleaningConfig())
results = cleaner.clean_batch(input_dir, output_dir)
```

**Or from command line**:
```bash
# Verify directory exists
ls -la input_folder/

# Create if needed
mkdir -p input_folder/
mkdir -p output_folder/
```

---

### Error 3: "PermissionError: [Errno 13] Permission denied"

**Symptoms**:
```
PermissionError: [Errno 13] Permission denied: 'output_folder'
```

**Causes**:
1. Output directory not writable
2. Input files not readable
3. Insufficient user permissions

**Solutions**:

**Check permissions**:
```bash
# Check if directory is writable
touch output_folder/.test && rm output_folder/.test

# If not, fix permissions
chmod 755 output_folder/
chmod 644 input_folder/*.md
```

**In Python**:
```python
from pathlib import Path
import os

output_dir = Path("output")

# Check if writable
if not os.access(output_dir, os.W_OK):
    raise PermissionError(f"Output directory not writable: {output_dir}")

# Create if doesn't exist
output_dir.mkdir(parents=True, exist_ok=True)
```

---

### Error 4: "ValueError: No markdown files found"

**Symptoms**:
```
ValueError: No markdown files found in input directory
```

**Causes**:
1. No .md files in input folder
2. Files have different extension (.markdown, .txt)
3. Files are in subdirectories

**Solutions**:

**Check files exist**:
```bash
ls -la input_folder/*.md

# If none found, check other extensions
ls -la input_folder/
```

**In Python**:
```python
from pathlib import Path

input_dir = Path("input")

# Check markdown files
md_files = list(input_dir.glob("*.md"))
print(f"Found {len(md_files)} markdown files")

# Check other extensions
txt_files = list(input_dir.glob("*.txt"))
markdown_files = list(input_dir.glob("*.markdown"))

print(f"Also found: {len(txt_files)} .txt, {len(markdown_files)} .markdown")
```

**Convert files to .md**:
```bash
# If files have different extension
for file in input_folder/*.txt; do
    mv "$file" "${file%.txt}.md"
done
```

---

### Error 5: "API Error: Invalid API Key"

**Symptoms**:
```
OpenAI API Error: Invalid API key provided
```

**Causes**:
1. API key incorrect or expired
2. API key not set in environment
3. API key not passed to config
4. Typo in key

**Solutions**:

**Verify API key**:
```bash
# Check if environment variable set
echo $OPENAI_API_KEY

# If empty, set it
export OPENAI_API_KEY="sk-your-actual-key"
```

**In Python**:
```python
import os
from PostScraperCleaner import CleaningConfig, PostScraperCleaner

# Get from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Verify format
if not api_key.startswith("sk-"):
    raise ValueError("API key should start with 'sk-'")

# Use in config
config = CleaningConfig(
    enable_llm_validation=True,
    openai_api_key=api_key,
)

cleaner = PostScraperCleaner(config)
```

**Get valid API key**:
1. Go to https://platform.openai.com/api-keys
2. Create new secret key
3. Copy entire key (starts with sk-)
4. Set in environment or pass to config
5. Don't share or commit to version control

---

### Error 6: "API Error: Rate limit exceeded"

**Symptoms**:
```
OpenAI API Error: Rate limit exceeded. Please retry after X seconds.
```

**Causes**:
1. Hitting OpenAI rate limits
2. `rate_limit_rpm` set too high
3. Multiple processes using same key

**Solutions**:

**Reduce rate limit**:
```python
from PostScraperCleaner import CleaningConfig

# More conservative rate limit
config = CleaningConfig(
    enable_llm_validation=True,
    rate_limit_rpm=100,  # Instead of 500
)
```

**Check OpenAI limits**:
1. Login to https://platform.openai.com
2. Check account limits
3. Verify you have API access
4. Check for billing issues

**Process in smaller batches**:
```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import time

config = CleaningConfig(
    enable_llm_validation=True,
    rate_limit_rpm=100,  # Conservative
)

cleaner = PostScraperCleaner(config)
input_dir = Path("input")
output_dir = Path("output")

# Process in small batches with delays
for file in input_dir.glob("*.md"):
    cleaner.clean_document(file, output_dir / file.name)
    time.sleep(1)  # 1 second between files
```

---

### Error 7: "ValueError: Invalid chunk size"

**Symptoms**:
```
ValueError: target_chunk_size must be between 100 and 2048
```

**Causes**:
1. Chunk size out of valid range
2. Chunk size is 0 or negative
3. Chunk size not an integer

**Solutions**:

```python
from PostScraperCleaner import CleaningConfig

# Valid range: 100-2048 tokens
config = CleaningConfig(
    target_chunk_size=512,  # Good default
)

# Too small
config = CleaningConfig(target_chunk_size=50)  # ✗ Error

# Too large
config = CleaningConfig(target_chunk_size=5000)  # ✗ Error

# Recommendations by use case
configs = {
    "search": CleaningConfig(target_chunk_size=256),
    "general": CleaningConfig(target_chunk_size=512),
    "summary": CleaningConfig(target_chunk_size=1024),
}
```

---

### Error 8: "UnicodeDecodeError: 'utf-8' codec can't decode byte"

**Symptoms**:
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xXX in position Y
```

**Causes**:
1. File not UTF-8 encoded
2. File has BOM (Byte Order Mark)
3. File contains invalid characters

**Solutions**:

**Convert file encoding**:
```bash
# Mac/Linux
iconv -f ISO-8859-1 -t UTF-8 input.md > input_utf8.md
mv input_utf8.md input.md

# Or using Python
python3 -c "
import sys
with open('input.md', 'r', encoding='latin-1') as f:
    content = f.read()
with open('input.md', 'w', encoding='utf-8') as f:
    f.write(content)
"
```

**In PostScraperCleaner** (if files are malformed):
```python
from pathlib import Path

input_dir = Path("input")

# Try to fix encoding issues
for file in input_dir.glob("*.md"):
    try:
        content = file.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback to latin-1
        content = file.read_text(encoding='latin-1')
        file.write_text(content, encoding='utf-8')
```

---

## Performance Issues

### Issue 1: "Processing is very slow"

**Symptoms**:
- Single file takes 5+ seconds
- Batch processing takes hours
- CPU usage low

**Causes**:
1. LLM validation enabled (expected slowdown)
2. Too many files being processed
3. Network latency (LLM API)
4. Chunk optimization disabled

**Solutions**:

**Check configuration**:
```python
from PostScraperCleaner import CleaningConfig

# Slowest (with LLM)
config = CleaningConfig(enable_llm_validation=True)
# Expected: 200-500ms per document

# Fast (no LLM)
config = CleaningConfig(enable_llm_validation=False)
# Expected: 10-50ms per document
```

**Benchmark your setup**:
```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import time

config = CleaningConfig()
cleaner = PostScraperCleaner(config)

input_file = Path("test.md")
output_file = Path("test_output.md")

# Time single document
start = time.time()
result = cleaner.clean_document(input_file, output_file)
elapsed = time.time() - start

print(f"Processed in {elapsed*1000:.0f}ms")
print(f"Expected for single: 10-50ms")
print(f"Expected with LLM: 200-500ms")
```

**Disable slow features**:
```python
# Fastest configuration
fast_config = CleaningConfig(
    enable_llm_validation=False,
    enable_chunk_optimization=False,
)
```

---

### Issue 2: "Batch processing slower after first file"

**Symptoms**:
- First file: 20ms
- After first file: 100-200ms each
- CPU usage increases over time

**Causes**:
1. Memory not being freed
2. Too many files in memory
3. Garbage collection kicking in

**Solutions**:

**Process in smaller batches**:
```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import gc

config = CleaningConfig()
cleaner = PostScraperCleaner(config)

input_dir = Path("input")
output_dir = Path("output")

# Process in batches of 50
batch_size = 50
all_files = list(input_dir.glob("*.md"))

for i in range(0, len(all_files), batch_size):
    batch = all_files[i:i+batch_size]

    for file in batch:
        cleaner.clean_document(file, output_dir / file.name)

    # Force garbage collection between batches
    gc.collect()
```

**Monitor memory**:
```python
import psutil
import os

process = psutil.Process(os.getpid())

before = process.memory_info().rss / 1024 / 1024  # MB
print(f"Memory before: {before:.1f}MB")

# ... processing ...

after = process.memory_info().rss / 1024 / 1024  # MB
print(f"Memory after: {after:.1f}MB")
print(f"Growth: {after - before:.1f}MB")
```

---

### Issue 3: "CPU usage stuck at 50%"

**Symptoms**:
- Single CPU core maxed
- Python process shows high CPU
- Other processes not affected

**Causes**:
1. Regex patterns are complex
2. Large files require intensive processing
3. No multiprocessing (current design single-threaded)

**Solutions**:

**Use simpler configuration**:
```python
# Skip intensive cleaning
config = CleaningConfig(
    remove_navigation=True,  # Keep essential only
    remove_headers_footers=False,
    remove_boilerplate=False,
)
```

**Check file sizes**:
```bash
# Find large files
find input_folder -name "*.md" -size +1M -exec ls -lh {} \;

# Process large files separately with simpler config
```

**Reduce batch size**:
```python
# Process fewer files at once
batch_size = 5  # Instead of default
```

---

## API Integration Issues

### Issue 1: "API key keeps getting rejected"

**Symptoms**:
- Every request: "Invalid API key"
- Key works in OpenAI dashboard
- Other tools accept the key

**Causes**:
1. Environment variable not set correctly
2. Key passed with extra spaces
3. Key variable overridden elsewhere

**Debug**:
```python
import os
from PostScraperCleaner import CleaningConfig

# Check environment
raw_key = os.environ.get("OPENAI_API_KEY", "NOT SET")
print(f"Raw from env: '{raw_key}'")
print(f"Length: {len(raw_key)}")

# Check if spaces
if raw_key != raw_key.strip():
    print("WARNING: Key has leading/trailing spaces!")

# Check prefix
if not raw_key.startswith("sk-"):
    print("WARNING: Key should start with 'sk-'")

# Use in config
config = CleaningConfig(
    enable_llm_validation=True,
    openai_api_key=raw_key.strip(),
)
```

---

### Issue 2: "API calls are very expensive"

**Symptoms**:
- Billing higher than expected
- Cost per document > $0.01
- OpenAI dashboard shows many requests

**Causes**:
1. LLM validation enabled for all documents
2. Retry loop causing duplicate requests
3. High input token count

**Solutions**:

**Disable LLM for bulk**:
```python
from PostScraperCleaner import CleaningConfig, PostScraperCleaner
from pathlib import Path

# Two-tier approach
config_fast = CleaningConfig(enable_llm_validation=False)
config_qa = CleaningConfig(
    enable_llm_validation=True,
    openai_api_key="sk-...",
)

cleaner_fast = PostScraperCleaner(config_fast)
cleaner_qa = PostScraperCleaner(config_qa)

input_dir = Path("input")
output_dir = Path("output")

# Fast clean everything
results = cleaner_fast.clean_batch(input_dir, output_dir)

# QA only important documents
important = [r for r in results if r.reduction_percentage < 5]
for result in important:
    cleaner_qa.clean_document(result.input_file, output_dir / result.input_file.name)
```

**Monitor costs**:
```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig

config = CleaningConfig(
    enable_llm_validation=True,
    openai_api_key="sk-...",
)

cleaner = PostScraperCleaner(config)

# Process and check cost
result = cleaner.clean_document(input_file, output_file)

print(f"Cost for this document: ${result.llm_cost:.6f}")

# For batch
results = cleaner.clean_batch(input_dir, output_dir)
total_cost = sum(r.llm_cost for r in results)
print(f"Total cost: ${total_cost:.2f}")
```

---

## File and Format Issues

### Issue 1: "Files are not being processed"

**Symptoms**:
- Input folder has files
- Output folder is empty
- No error messages

**Causes**:
1. Files don't have .md extension
2. Glob pattern not matching
3. Empty input folder

**Debug**:
```python
from pathlib import Path

input_dir = Path("input")

# Check what's in directory
all_files = list(input_dir.glob("*"))
print(f"All files: {[f.name for f in all_files]}")

# Check markdown files specifically
md_files = list(input_dir.glob("*.md"))
print(f"Markdown files: {[f.name for f in md_files]}")

# Check other extensions
other = [f for f in all_files if f.suffix != ".md"]
print(f"Other extensions: {[f.suffix for f in other]}")
```

---

### Issue 2: "Cleaned files are corrupted or empty"

**Symptoms**:
- Output files exist but are empty
- Output files are corrupted
- Can't open cleaned files

**Causes**:
1. Cleaning removed all content
2. File write failed silently
3. Encoding issue

**Debug**:
```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

config = CleaningConfig()
cleaner = PostScraperCleaner(config)

input_file = Path("test.md")
output_file = Path("test_output.md")

result = cleaner.clean_document(input_file, output_file)

# Check result
print(f"Success: {result.success}")
print(f"Original size: {result.original_size}")
print(f"Cleaned size: {result.cleaned_size}")
print(f"Reduction: {result.reduction_percentage:.1f}%")

# Check output file
if output_file.exists():
    content = output_file.read_text()
    print(f"Output file size: {len(content)}")
    print(f"First 100 chars: {content[:100]}")
else:
    print("Output file was not created!")
```

---

### Issue 3: "Markdown formatting lost"

**Symptoms**:
- Headers become plain text
- Code blocks become plain text
- Bold/italic not preserved

**Causes**:
1. Too aggressive cleaning patterns
2. Pattern regex too broad
3. Configuration removing too much

**Solutions**:

**Use conservative configuration**:
```python
from PostScraperCleaner import CleaningConfig

# Conservative: Only remove obvious boilerplate
config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
)
```

**Check which patterns are aggressive**:
```python
from cleaning_rules import CLEANING_PATTERNS

# List patterns and their confidence
for pattern in CLEANING_PATTERNS:
    print(f"{pattern.name}: {pattern.confidence:.2f} confidence")

# High confidence patterns are safer
safe_patterns = [p for p in CLEANING_PATTERNS if p.confidence >= 0.85]
print(f"Safe patterns: {len(safe_patterns)}")
```

---

## Memory and Resource Issues

### Issue 1: "Out of Memory error on large files"

**Symptoms**:
```
MemoryError: Unable to allocate X bytes
```

**Causes**:
1. File too large for RAM
2. Memory leak in processing
3. Loading entire file into memory

**Solutions**:

**Split large files**:
```python
from pathlib import Path

def split_large_file(file_path: Path, chunk_size_mb: int = 5):
    """Split file into smaller chunks"""
    file_size_mb = file_path.stat().st_size / (1024 * 1024)

    if file_size_mb <= chunk_size_mb:
        return [file_path]

    print(f"File {file_path.name} is {file_size_mb:.1f}MB, splitting...")

    with open(file_path) as f:
        content = f.read()

    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    chunks = []

    for i in range(0, len(content), chunk_size_bytes):
        chunk = content[i:i+chunk_size_bytes]
        chunk_file = file_path.with_stem(f"{file_path.stem}_chunk_{i//chunk_size_bytes}")
        chunk_file.write_text(chunk)
        chunks.append(chunk_file)

    return chunks
```

**Process with generator**:
```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def process_large_directory(input_dir: Path, output_dir: Path):
    """Process files one at a time to avoid memory buildup"""
    config = CleaningConfig()
    cleaner = PostScraperCleaner(config)

    for file in input_dir.glob("*.md"):
        try:
            cleaner.clean_document(file, output_dir / file.name)
            print(f"✓ {file.name}")
        except MemoryError:
            print(f"✗ {file.name} - Out of memory")
```

---

### Issue 2: "Disk space exceeded"

**Symptoms**:
- "No space left on device"
- Output folder growing too large
- Temporary files not cleaned up

**Solutions**:

**Monitor disk space**:
```python
import shutil
from pathlib import Path

output_dir = Path("output")
stat = shutil.disk_usage(output_dir)

free_gb = stat.free / (1024 ** 3)
print(f"Free disk space: {free_gb:.1f}GB")

if free_gb < 1:
    print("WARNING: Less than 1GB free!")
```

**Clean up old files**:
```python
from pathlib import Path
import time

output_dir = Path("output")

# Remove files older than 7 days
cutoff = time.time() - (7 * 24 * 60 * 60)

for file in output_dir.glob("*.md"):
    if file.stat().st_mtime < cutoff:
        file.unlink()
        print(f"Deleted old file: {file.name}")
```

---

## GUI Issues

### Issue 1: "GUI not responding / Frozen"

**Symptoms**:
- Button clicks don't work
- Window says "Not Responding"
- Close button doesn't work

**Causes**:
1. Processing blocks GUI thread
2. Large file being processed
3. Network timeout in API call

**Solutions**:

**Force quit**:
```bash
# Mac/Linux
pkill -f "python.*PostScraperCleanerGUI"

# Windows
taskkill /IM python.exe /F
```

**Run in terminal to see errors**:
```bash
python PostScraperCleanerGUI.py
# Look for error messages
```

**Try with simpler configuration**:
1. Disable LLM validation
2. Select smaller input folder
3. Try single file first

---

### Issue 2: "Progress bar stuck or not updating"

**Symptoms**:
- Progress bar doesn't move
- Status bar doesn't update
- No indication of progress

**Causes**:
1. Processing but GUI not getting updates
2. Progress callback not implemented
3. Threading issue

**Solutions**:

**Check the log tab**:
1. Click "Log" tab in GUI
2. Look for processing messages
3. Check for errors

**Try command line instead**:
```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def progress_callback(update):
    if update['type'] == 'progress':
        print(f"[{update['processed']}/{update['total']}] {update['current_file']}")

config = CleaningConfig()
cleaner = PostScraperCleaner(config, progress_callback=progress_callback)
results = cleaner.clean_batch(Path("input"), Path("output"))
```

---

## Debugging Techniques

### Technique 1: Enable Verbose Logging

```python
import logging

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('postcleaner_debug.log'),
        logging.StreamHandler(),
    ]
)

# Use in your code
from PostScraperCleaner import PostScraperCleaner, CleaningConfig

config = CleaningConfig()
cleaner = PostScraperCleaner(config)

# Processing will now log detailed information
results = cleaner.clean_batch(Path("input"), Path("output"))
```

---

### Technique 2: Add Checkpoints

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path
import json

config = CleaningConfig()
cleaner = PostScraperCleaner(config)

input_dir = Path("input")
output_dir = Path("output")
checkpoint_file = Path("checkpoint.json")

# Load checkpoint
if checkpoint_file.exists():
    with open(checkpoint_file) as f:
        processed = set(json.load(f)['processed'])
else:
    processed = set()

# Process with checkpoints
for i, file in enumerate(input_dir.glob("*.md")):
    if file.stem in processed:
        continue

    try:
        cleaner.clean_document(file, output_dir / file.name)
        processed.add(file.stem)

        # Save checkpoint every 10 files
        if (i + 1) % 10 == 0:
            with open(checkpoint_file, "w") as f:
                json.dump({"processed": list(processed)}, f)
            print(f"Checkpoint saved at {i + 1} files")

    except Exception as e:
        print(f"Error processing {file.name}: {e}")
```

---

### Technique 3: Test Single File First

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

# Pick one problematic file
test_file = Path("input/problematic_file.md")

# Test with minimal config
config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=False,
    remove_boilerplate=False,
)

cleaner = PostScraperCleaner(config)

# Process with detailed output
result = cleaner.clean_document(
    test_file,
    Path("test_output.md")
)

print(f"Success: {result.success}")
print(f"Original: {result.original_size} bytes")
print(f"Cleaned: {result.cleaned_size} bytes")
print(f"Reduction: {result.reduction_percentage:.1f}%")

# Examine the output
output = Path("test_output.md").read_text()
print(f"\nOutput preview:\n{output[:500]}")
```

---

## Getting Help

### Resources

1. **User Guide**: [USER_GUIDE.md](USER_GUIDE.md)
2. **API Documentation**: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
3. **Configuration Guide**: [CONFIGURATION_GUIDE.md](CONFIGURATION_GUIDE.md)
4. **Integration Guide**: [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)
5. **Examples**: [EXAMPLES.md](EXAMPLES.md)

### Report an Issue

When reporting an issue, include:

1. **What you tried**:
   ```python
   config = CleaningConfig(...)
   cleaner = PostScraperCleaner(config)
   ```

2. **What happened**:
   ```
   Error message or unexpected behavior
   ```

3. **What you expected**:
   ```
   Expected behavior or output
   ```

4. **System information**:
   ```
   Python version: python --version
   Platform: mac/linux/windows
   ```

5. **Input file size** (if relevant):
   ```bash
   ls -lh input_file.md
   ```

---

## Summary

**Quick Fix Checklist**:

- [ ] Verify file exists and is readable
- [ ] Check Python path includes PostScraperCleaner files
- [ ] Verify output directory is writable
- [ ] Check API key format (starts with sk-)
- [ ] Try with LLM disabled first
- [ ] Check file encoding (should be UTF-8)
- [ ] Test single file before batch
- [ ] Monitor memory and disk space
- [ ] Check logs for detailed errors
- [ ] Try simpler configuration

---

**Version**: 1.0 | **Status**: Production Ready | **Last Updated**: 2025-01-07
