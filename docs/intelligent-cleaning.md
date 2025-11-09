# Intelligent Content Cleaning

## Overview

The Intelligent Content Cleaning system uses GPT-4o to semantically analyze scraped documentation and identify main content vs. navigation/headers/footers. Unlike pattern-based cleaning, this works on **any** documentation source without hardcoded rules.

## How It Works

### 3-Pass Architecture

```
Original Doc → Pass 1: LLM Analysis → Pass 2: Rule-Based Cleanup → Clean Output
```

**Pass 1 - LLM Semantic Analysis** (on original content):
- Analyzes document structure with line-numbered preview
- Identifies main content start/end boundaries
- Detects navigation menus, headers, footers, sidebars
- Returns structured analysis with line numbers

**Pass 2 - Rule-Based Cleanup**:
- Applies universal patterns (YAML frontmatter, social links, etc.)
- Cleans up remaining boilerplate
- Normalizes whitespace

### LLM Analysis Process

1. **Document Preview** - First 100 lines, middle 50 lines, last 50 lines (with line numbers)
2. **Prompt Engineering** - Explicit rules for identifying markdown headings and content boundaries
3. **JSON Response** - Structured output with:
   - `main_content_start`: Line number where main content begins
   - `main_content_end`: Line number where main content ends
   - `sections_to_remove`: Array of sections to strip out
   - `sections_to_keep`: Array of useful sections to preserve
   - `confidence`: 0.0-1.0 confidence score

4. **Content Extraction** - Apply boundaries and remove identified sections

### Critical Implementation Details

**Indexing Conversion** (Bug Fix - 2025-11-09):
- LLM sees `"  37: # Title"` and returns line `37` (1-indexed)
- Python arrays are 0-indexed, so line 37 = index 36
- **Fix**: `main_start = analysis.main_content_start - 1`

**Line-Numbered Preview**:
```python
numbered_lines = [f"{i+1:4d}: {line}" for i, line in enumerate(lines)]
```
This ensures the LLM can accurately reference exact line numbers.

## When to Use

### Use Intelligent Cleaning When:
- Processing diverse documentation sources (Anthropic, Python, React, Stripe, etc.)
- Documentation has complex/nested navigation structures
- You need to preserve important headings (H1/H2 titles)
- Content structure varies significantly between files
- Cost is acceptable (~$0.002 per document)

### Use Rule-Based Only When:
- Documentation has consistent, simple structure
- Budget is very tight
- Processing millions of documents
- Speed is critical (5-15ms vs ~3-8s per doc)

## Model Comparison

### GPT-4o (Current - Recommended)
- **Accuracy**: Excellent - correctly identifies H1 titles and complex boundaries
- **Cost**: $2.50/1M input, $10.00/1M output (~$0.002/document)
- **Speed**: ~3-8 seconds per document
- **Use Case**: Production use, diverse documentation

### GPT-4o-mini (Legacy)
- **Accuracy**: Good - sometimes misses titles or over-cleans
- **Cost**: $0.150/1M input, $0.600/1M output (~$0.0003/document)
- **Speed**: ~2-5 seconds per document
- **Use Case**: Budget-constrained scenarios, simple documentation

**Upgrade Rationale** (See ADR 0002):
- 7x more expensive but prevents data loss (missing titles)
- Still extremely affordable at $0.002/doc ($2/1000 docs)
- Observed 20-30% better boundary detection accuracy

## Configuration

### Enable in Code

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig

config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
    enable_llm_validation=True,  # Enables intelligent cleaner
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    rate_limit_rpm=500
)

cleaner = PostScraperCleaner(config)
result = cleaner.clean_document(input_file, output_file)
```

### Enable in GUI

1. Create `.env` file with OpenAI API key (see `ENV_SETUP.md`)
2. Launch GUI: `python3 PostScraperCleanerGUI.py`
3. Check "🧠 Intelligent Analysis (LLM-Powered)" checkbox
4. Process files normally

### Environment Setup

Required `.env` file:
```bash
OPENAI_API_KEY=sk-proj-your-key-here
```

See [ENV_SETUP.md](../ENV_SETUP.md) for detailed setup instructions.

## Performance & Cost

### Typical Performance (GPT-4o)
- **Processing Time**: 3-8 seconds per document
- **Reduction**: 20-80% (average 55%)
- **Cost**: $0.001-$0.004 per document (depends on length)
- **Rate Limit**: 500 RPM (default)

### Batch Processing Example

Processing 107 Chroma docs:
```
✅ Successful: 107/107 (100%)
💰 Total Cost: $0.223 (~$0.002/doc)
📉 Average Reduction: 55%
⏱️ Total Time: ~12 minutes
```

### Cost Scaling

| Documents | Cost (GPT-4o) | Cost (gpt-4o-mini) |
|-----------|---------------|-------------------|
| 100       | $0.20         | $0.03             |
| 1,000     | $2.00         | $0.30             |
| 10,000    | $20.00        | $3.00             |
| 100,000   | $200.00       | $30.00            |

## Troubleshooting

### Issue: API Key Not Found
```
ERROR: OPENAI_API_KEY environment variable not set
```

**Solution**: Create `.env` file in project root with your API key. See [ENV_SETUP.md](../ENV_SETUP.md).

### Issue: HTTP 401 Unauthorized
```
ERROR: API request failed: HTTP Error 401: Unauthorized
```

**Solution**: API key is invalid or expired. Generate new key at https://platform.openai.com/api-keys.

### Issue: Titles Being Removed
```
Expected first line: # Package Search MCP Server
Actual first line: The Package Search MCP Server is an...
```

**Solution**: This was a bug fixed on 2025-11-09. Update to latest version. The fix converts 1-indexed LLM line numbers to 0-indexed Python arrays.

### Issue: Over-Cleaning (97%+ reduction)
```
Original: 104,555 bytes
Cleaned: 2,270 bytes (97.8% reduction)
```

**Solution**:
1. Manually verify the output - LLM may have identified a very small main content section
2. Check if document has unusual structure (e.g., mostly navigation)
3. Consider adjusting prompt or using rule-based cleaning for this specific source

### Issue: Rate Limit Exceeded
```
WARNING: Rate limit exceeded
```

**Solution**: Reduce `rate_limit_rpm` in config or add delays between requests:
```python
config = CleaningConfig(
    ...
    rate_limit_rpm=200  # Reduce from 500
)
```

## Testing

### Test Suite

Run the comprehensive test suite on diverse documentation:
```bash
python3 test_intelligent_cleaning.py
```

This tests on 5 different documentation sources:
- Anthropic (AI API docs)
- Chroma (database docs)
- Python (language docs)
- Convex (backend docs)
- Langchain (AI framework docs)

### Manual Verification

After cleaning, always spot-check results:
1. Open cleaned file: `open test_results/CLEANED_*.md`
2. Verify first line is the main H1 title
3. Check that navigation menus are removed
4. Confirm main content is preserved
5. Look for any missing sections

## Architecture

### Key Components

**intelligent_cleaner.py**:
- `IntelligentContentAnalyzer` - Main orchestrator
- `ContentAnalysis` - Result dataclass with boundaries
- `ContentSection` - Individual section to remove/keep

**llm_cleaner.py**:
- `LLMValidator` - API calling infrastructure
- `LLMConfig` - Configuration with model/pricing

**PostScraperCleaner.py**:
- Integrates intelligent cleaner in Pass 1
- Applies rule-based cleanup in Pass 2
- Tracks costs and statistics

### Prompt Engineering

The LLM prompt includes:
1. **Line-numbered preview** for accurate boundary detection
2. **Explicit rules** for identifying markdown headings
3. **Examples** of what constitutes main content vs. navigation
4. **JSON schema** for structured output
5. **Conservative bias** - err on side of keeping content

Key prompt excerpts:
```
CRITICAL RULES FOR FINDING MAIN CONTENT START:
1. Look for the FIRST markdown heading (# or ## or ###)
2. Main content MUST start at or BEFORE the first H1/H2 heading
3. Lines with just markdown link lists are navigation menus
4. INCLUDE the first H1 heading as part of main content
```

## Best Practices

1. **Always use `.env`** - Never hardcode API keys
2. **Test first** - Run `test_intelligent_cleaning.py` before batch processing
3. **Spot-check results** - Manually verify 5-10 files from each source
4. **Monitor costs** - Check `result.llm_cost` to track spending
5. **Start small** - Process 10-20 files first, then scale up
6. **Use GPT-4o** - Worth the extra cost for better accuracy
7. **Enable rate limiting** - Respect OpenAI's API limits
8. **Archive originals** - Keep backups before mass processing

## Future Improvements

Potential enhancements:
- **Caching**: Cache LLM responses for identical documents
- **Batch API**: Use OpenAI batch API for 50% cost savings
- **Fine-tuning**: Train custom model on our cleaning decisions
- **Multi-model**: Fall back to gpt-4o-mini for simple documents
- **Confidence threshold**: Only use LLM when confidence > 0.8
- **Streaming**: Process results as they arrive for faster feedback

## Related Documentation

- [ENV_SETUP.md](../ENV_SETUP.md) - API key setup instructions
- [Architecture](architecture.md) - System architecture overview
- [API Reference](api.md) - PostScraperCleaner API documentation
- [ADR 0002](decisions/0002-gpt4o-upgrade.md) - GPT-4o upgrade decision
