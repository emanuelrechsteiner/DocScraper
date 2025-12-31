# PostScraperCleaner: User Guide

**Version**: 1.0
**Last Updated**: 2025-01-07
**Status**: Production Ready

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [GUI Usage](#gui-usage)
5. [Command-Line Usage](#command-line-usage)
6. [Configuration](#configuration)
7. [Common Workflows](#common-workflows)
8. [Tips & Best Practices](#tips--best-practices)

---

## Introduction

**PostScraperCleaner** is a professional document cleaning and optimization tool designed to transform raw web-scraped markdown into production-ready documentation.

### Key Features

- 🧹 **Rule-Based Cleaning**: Remove navigation, boilerplate, and UI elements
- 🤖 **LLM Validation**: Optional OpenAI API integration for intelligent review
- 📦 **Chunk Optimization**: Prepare content for vector database embeddings
- 🚀 **High Performance**: Process 50-100+ files per second
- 💾 **Zero Dependencies**: Pure Python stdlib implementation
- 🔄 **Batch Processing**: Handle hundreds of documents seamlessly
- 📊 **Detailed Statistics**: Track cleaning metrics and results

### What It Does

```
Raw Scraped Content
    ↓
[Navigation & Boilerplate Removed]
    ↓
[LLM Validation - Optional]
    ↓
[Optimized for Embeddings]
    ↓
Production-Ready Content
```

---

## Installation

### Prerequisites

- Python 3.8+
- No external dependencies (pure Python)

### Setup

1. **Copy Files**
   ```bash
   # Copy these files to your project:
   cp PostScraperCleaner.py your_project/
   cp cleaning_rules.py your_project/
   cp chunk_optimizer.py your_project/
   cp llm_cleaner.py your_project/  # Optional
   cp PostScraperCleanerGUI.py your_project/  # For GUI
   ```

2. **Optional: Install GUI**
   ```bash
   # Tkinter is included with Python on most systems
   # On Linux:
   sudo apt-get install python3-tk
   ```

3. **Optional: Set OpenAI API Key**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

---

## Quick Start

### GUI Mode (Recommended for Most Users)

```bash
python PostScraperCleanerGUI.py
```

**Steps**:
1. Click "Select Input Folder" and choose your folder with markdown files
2. Click "Select Output Folder" for cleaned files
3. Adjust settings if needed (see [Configuration](#configuration))
4. Click "Start Processing"
5. Review results in the Results tabs

**Screenshot Flow**:
- Input folder selection
- Configuration checkboxes (remove navigation, headers, boilerplate)
- Advanced options (chunk size, LLM settings)
- Progress bar during processing
- Results summary, details, and log tabs

### Python Script Mode

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

# Configure
config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
    enable_chunk_optimization=True,
)

# Create cleaner
cleaner = PostScraperCleaner(config)

# Process single file
result = cleaner.clean_document(
    Path("input/document.md"),
    Path("output/document.md")
)

# Or batch process
results = cleaner.clean_batch(
    Path("input_folder"),
    Path("output_folder")
)

# Check results
print(f"Processed: {result.success}")
print(f"Reduction: {result.reduction_percentage:.1f}%")
```

### Command-Line Mode (Minimal)

```bash
python -c "
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

cleaner = PostScraperCleaner(CleaningConfig())
results = cleaner.clean_batch(Path('input'), Path('output'))
print(f'Processed {len(results)} files')
"
```

---

## GUI Usage

### Main Window

**Sections**:
1. **Folder Selection**
   - Select input folder (scraped documents)
   - Select output folder (cleaned results)

2. **Configuration Panel**
   - ☑️ Remove navigation elements
   - ☑️ Remove headers & footers
   - ☑️ Remove boilerplate content
   - ☑️ Enable chunk optimization

3. **Advanced Options** (collapsible)
   - Chunk size: 256-2048 tokens (default: 512)
   - Overlap: 0-500 tokens (default: 50)
   - LLM validation: Enable/disable
   - API key: Enter your OpenAI key
   - Rate limit: 10-1000 RPM

4. **Processing Controls**
   - Start button (begins processing)
   - Stop button (halts processing)
   - Progress bar (visual progress)

5. **Status Bar**
   - Current file being processed
   - Estimated completion time
   - Total cost (if using LLM)
   - Processing statistics

6. **Results Display** (3 tabs)
   - **Summary**: Overall statistics
   - **Details**: File-by-file results table
   - **Log**: Real-time processing log

### Configuration Panel Details

#### Remove Navigation
- Removes: "Skip to content", breadcrumbs, table of contents, site menus
- Impact: 5-10% size reduction
- Risk: Very low (high confidence patterns)

#### Remove Headers & Footers
- Removes: Page headers, navigation bars, copyright notices, footers
- Impact: 3-5% size reduction
- Risk: Very low (clear boundaries)

#### Remove Boilerplate
- Removes: Call-to-action buttons, newsletter signups, cookie notices
- Impact: 2-3% size reduction
- Risk: Low (specific patterns)

#### Enable Chunk Optimization
- Optimizes: Content structure for embeddings
- Impact: Better embedding quality
- Risk: None (improves structure)

### Advanced Options

**Chunk Size** (256-2048 tokens, default 512):
- Smaller (256): Better granularity, more chunks
- Larger (1024): Better context, fewer chunks
- Recommendation: 512 for general use, 256 for fine detail

**Overlap** (0-500 tokens, default 50):
- Higher overlap: Better context preservation
- Lower overlap: Fewer redundant chunks
- Recommendation: 50 tokens (standard)

**LLM Validation**:
- Enable for quality review (costs money)
- Disable for speed (free)
- Recommendation: Disable for bulk processing, enable for important docs

**API Key**:
- Get from: https://platform.openai.com/api-keys
- Format: sk-...
- Security: Stored only in memory during session

**Rate Limit** (10-1000 RPM):
- Default: 500 requests per minute
- Increase if you have high quota
- Decrease if hitting rate limits

### Workflow Example

1. **Setup**
   - Select input folder: `/data/scraped_docs/`
   - Select output folder: `/data/cleaned_docs/`

2. **Configure**
   - ☑️ Remove navigation
   - ☑️ Remove headers/footers
   - ☑️ Remove boilerplate
   - ☑️ Enable chunk optimization
   - Chunk size: 512
   - Leave LLM disabled

3. **Process**
   - Click "Start"
   - Watch progress bar
   - Monitor current file in status bar
   - Wait for completion

4. **Review**
   - Check Summary tab for statistics
   - Review Details tab for per-file metrics
   - Check Log tab for any warnings
   - View output folder for cleaned files

---

## Command-Line Usage

### Basic Cleaning

```bash
python -c "
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

config = CleaningConfig()
cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(Path('input'), Path('output'))

for result in results:
    status = '✓' if result.success else '✗'
    print(f'{status} {result.input_file.name}: {result.reduction_percentage:.1f}% reduction')
"
```

### With Custom Configuration

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
    enable_chunk_optimization=True,
    target_chunk_size=512,
    overlap_size=50,
)

cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(Path('input'), Path('output'))

# Statistics
stats = cleaner.get_statistics()
print(f"Processed: {stats['total_processed']} files")
print(f"Success rate: {stats['success_rate']*100:.1f}%")
print(f"Overall reduction: {stats['overall_reduction_percentage']:.1f}%")
```

### With LLM Validation

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

config = CleaningConfig(
    enable_llm_validation=True,
    openai_api_key="sk-your-key",
    target_chunk_size=512,
)

cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(Path('input'), Path('output'))

for result in results:
    if result.llm_validation:
        confidence = result.llm_validation.get('confidence', 0)
        print(f"{result.input_file.name}: LLM confidence {confidence:.1%}")
```

### Progress Callback

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def show_progress(update):
    if update['type'] == 'progress':
        processed = update['processed']
        total = update['total']
        current = update['current_file']
        print(f"[{processed}/{total}] Processing: {current}")

config = CleaningConfig()
cleaner = PostScraperCleaner(config, progress_callback=show_progress)
results = cleaner.clean_batch(Path('input'), Path('output'))
```

---

## Configuration

### CleaningConfig Options

```python
config = CleaningConfig(
    # Phase 1: Rule-based cleaning (all default True)
    remove_navigation=True,          # Remove nav menus, breadcrumbs
    remove_headers_footers=True,     # Remove page headers/footers
    remove_boilerplate=True,         # Remove CTAs, newsletters, cookies

    # Phase 2: LLM Validation (default False - requires API key)
    enable_llm_validation=False,     # Enable OpenAI API validation
    openai_api_key=None,             # Your OpenAI API key
    llm_confidence_threshold=0.85,   # Confidence requirement (0.0-1.0)

    # Phase 2: Chunk Optimization (default True)
    enable_chunk_optimization=True,  # Optimize for embeddings
    target_chunk_size=512,           # Tokens per chunk (100-2048)
    overlap_size=50,                 # Token overlap between chunks

    # Rate Limiting (for LLM)
    rate_limit_rpm=500,              # Requests per minute
)
```

### Environment Variables

```bash
# OpenAI API Key
export OPENAI_API_KEY="sk-your-key"

# Cache directory (optional)
export POSTCLEANER_CACHE_DIR="~/.cache/postcleaner"
```

### Configuration Files

**Save configuration** (from GUI):
- Format: JSON
- Location: Configurable
- Contents: All settings

**Load configuration** (from GUI):
- Click "Load Config"
- Select JSON file
- Settings applied automatically

---

## Common Workflows

### Workflow 1: Basic Cleaning

**Goal**: Clean scraped documentation, remove boilerplate

**Steps**:
1. Configure: Enable all cleaning options
2. Disable: LLM validation (not needed)
3. Disable: Chunk optimization (not needed)
4. Process: All files

**Expected Result**:
- 10-20% size reduction
- Clean, readable content
- Fast processing

### Workflow 2: Vector Database Preparation

**Goal**: Clean and optimize for embeddings

**Steps**:
1. Configure: Enable all cleaning options
2. Enable: Chunk optimization
3. Set: Chunk size 512, overlap 50
4. Process: All files

**Expected Result**:
- Clean, chunked content
- Optimal for embedding models
- Ready for vector DB ingestion

### Workflow 3: Quality Assurance

**Goal**: High-quality cleaning with validation

**Steps**:
1. Configure: Enable all cleaning options
2. Enable: Chunk optimization
3. Enable: LLM validation
4. Set: OpenAI API key
5. Process: Important documents only

**Expected Result**:
- Highest quality content
- Validated by AI
- Cost: ~$0.002-0.005 per document

### Workflow 4: Batch Processing

**Goal**: Process 100+ documents efficiently

**Steps**:
1. Configure: Enable navigation, headers, boilerplate removal
2. Disable: LLM validation (cost/speed)
3. Enable: Chunk optimization
4. Process: All files
5. Monitor: Progress bar and statistics

**Expected Result**:
- Fast processing (50-100 files/sec)
- Good quality (20-30% reduction)
- Low cost (free)

---

## Tips & Best Practices

### Performance Tips

✅ **Do**:
- Disable LLM validation for batch jobs
- Use chunk optimization for embeddings
- Process multiple files in batch
- Monitor the progress bar

❌ **Don't**:
- Enable LLM for every document
- Use very small chunk sizes (<256)
- Use very large chunk sizes (>2048)
- Stop and restart processing

### Quality Tips

✅ **Do**:
- Review the Log tab for warnings
- Check Details tab for per-file results
- Enable LLM for important documents
- Adjust chunk size for your use case

❌ **Don't**:
- Process untrusted markdown
- Disable all cleaning options
- Ignore reduction warnings
- Skip reviewing output

### Cost Tips

✅ **Do**:
- Disable LLM unless needed (saves 99% cost)
- Use request caching (built-in)
- Batch process (cheaper than individual)
- Monitor API costs in OpenAI dashboard

❌ **Don't**:
- Enable LLM for everything
- Use highest rate limits unnecessarily
- Leave processing running unmonitored
- Ignore API errors

### Integration Tips

✅ **Do**:
- Use in DocScraper pipeline
- Export results to JSON
- Import configurations
- Track statistics over time

❌ **Don't**:
- Manually edit cleaned files
- Mix cleaned and uncleaned content
- Lose configuration files
- Ignore error warnings

---

## Troubleshooting

See [TROUBLESHOOTING_GUIDE.md](TROUBLESHOOTING_GUIDE.md) for:
- Common errors and solutions
- Performance optimization
- API key issues
- File format problems

---

## Support & Resources

- 📖 [API Documentation](API_DOCUMENTATION.md)
- ⚙️ [Configuration Guide](CONFIGURATION_GUIDE.md)
- 🔗 [Integration Guide](INTEGRATION_GUIDE.md)
- 🐛 [Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md)
- 📝 [Examples & Recipes](EXAMPLES.md)
- 🏗️ [Architecture Overview](ARCHITECTURE.md)

---

## Next Steps

1. **Start with GUI**: Most user-friendly
2. **Explore Configuration**: Adjust to your needs
3. **Process Documents**: Clean your content
4. **Review Results**: Check Summary and Details tabs
5. **Integrate**: Add to your pipeline

---

**Version**: 1.0 | **Status**: Production Ready | **Last Updated**: 2025-01-07
