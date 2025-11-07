# PostScraperCleaner: API Documentation

**Version**: 1.0
**Status**: Production Ready
**Last Updated**: 2025-01-07

---

## Table of Contents

1. [Core Classes](#core-classes)
2. [CleaningConfig](#cleaningconfig)
3. [CleaningResult](#cleaningresult)
4. [PostScraperCleaner](#postscrapercleaner)
5. [RuleBasedCleaner](#rulebasedcleaner)
6. [LLM Integration](#llm-integration)
7. [Chunk Optimization](#chunk-optimization)
8. [Examples](#examples)

---

## Core Classes

### Class Hierarchy

```
PostScraperCleaner (Main orchestrator)
├── CleaningConfig (Configuration)
├── RuleBasedCleaner (Pattern-based cleaning)
│   └── PatternRegistry (Pattern management)
├── LLMValidator (Optional LLM validation)
└── ChunkOptimizer (Content optimization)
```

---

## CleaningConfig

Configuration dataclass for cleaning operations.

### Definition

```python
@dataclass
class CleaningConfig:
    # Phase 1: Rule-based cleaning
    remove_navigation: bool = True
    remove_headers_footers: bool = True
    remove_boilerplate: bool = True

    # Phase 2: LLM validation
    enable_llm_validation: bool = False
    llm_confidence_threshold: float = 0.85
    openai_api_key: Optional[str] = None

    # Phase 2: Chunk optimization
    enable_chunk_optimization: bool = True
    target_chunk_size: int = 512
    overlap_size: int = 50

    # Rate limiting
    rate_limit_rpm: int = 500
    max_cost_per_document: float = 0.05
```

### Parameters

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| `remove_navigation` | bool | True | - | Remove navigation elements |
| `remove_headers_footers` | bool | True | - | Remove headers and footers |
| `remove_boilerplate` | bool | True | - | Remove boilerplate content |
| `enable_llm_validation` | bool | False | - | Enable OpenAI validation |
| `llm_confidence_threshold` | float | 0.85 | 0.0-1.0 | Confidence threshold |
| `openai_api_key` | str | None | - | OpenAI API key |
| `enable_chunk_optimization` | bool | True | - | Enable chunking |
| `target_chunk_size` | int | 512 | 100-2048 | Tokens per chunk |
| `overlap_size` | int | 50 | 0-500 | Overlap tokens |
| `rate_limit_rpm` | int | 500 | 1+ | Requests per minute |
| `max_cost_per_document` | float | 0.05 | 0+ | Max cost USD |

### Methods

#### `__post_init__()`

Validates configuration values after initialization.

**Raises**:
- `ValueError`: If threshold not in [0.0, 1.0]
- `ValueError`: If chunk_size < 100
- `ValueError`: If overlap_size >= chunk_size

### Example

```python
from PostScraperCleaner import CleaningConfig

# Minimal config (defaults)
config = CleaningConfig()

# Custom config
config = CleaningConfig(
    remove_navigation=True,
    target_chunk_size=512,
    enable_llm_validation=False,
)

# With LLM
config = CleaningConfig(
    enable_llm_validation=True,
    openai_api_key="sk-your-key",
    llm_confidence_threshold=0.9,
)
```

---

## CleaningResult

Result dataclass from cleaning a single document.

### Definition

```python
@dataclass
class CleaningResult:
    input_file: Path
    output_file: Optional[Path] = None
    success: bool = False
    original_size: int = 0
    cleaned_size: int = 0
    reduction_percentage: float = 0.0
    removed_sections: List[str] = field(default_factory=list)
    structure_score: float = 0.0
    rule_based_cleaning: bool = False
    llm_validation_used: bool = False
    llm_validation: Optional[Dict] = None
    llm_cost: float = 0.0
    chunk_optimization_used: bool = False
    chunk_metadata: Optional[Dict] = None
    processing_time: float = 0.0
    content_quality_score: float = 0.0
    error_message: Optional[str] = None
    warnings: List[str] = field(default_factory=list)
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `input_file` | Path | Input markdown file path |
| `output_file` | Path | Output markdown file path |
| `success` | bool | Processing succeeded |
| `original_size` | int | Original file size (bytes) |
| `cleaned_size` | int | Cleaned file size (bytes) |
| `reduction_percentage` | float | Size reduction % |
| `removed_sections` | List[str] | Patterns that matched |
| `structure_score` | float | Content structure quality (0-1) |
| `rule_based_cleaning` | bool | Rule-based cleaning applied |
| `llm_validation_used` | bool | LLM validation used |
| `llm_validation` | Dict | LLM validation details |
| `llm_cost` | float | LLM API cost (USD) |
| `chunk_optimization_used` | bool | Chunking applied |
| `chunk_metadata` | Dict | Chunking statistics |
| `processing_time` | float | Processing time (seconds) |
| `content_quality_score` | float | Content quality (0-1) |
| `error_message` | str | Error message if failed |
| `warnings` | List[str] | Warning messages |

### Methods

#### `calculate_reduction()`

Calculate reduction percentage from size.

```python
result = CleaningResult(
    input_file=Path("test.md"),
    original_size=1000,
    cleaned_size=800,
)
result.calculate_reduction()
print(result.reduction_percentage)  # 20.0
```

#### `to_dict() -> Dict`

Convert result to dictionary for JSON serialization.

```python
result_dict = result.to_dict()
# {
#   "input_file": "path/to/file.md",
#   "success": True,
#   "original_size": 1000,
#   "cleaned_size": 800,
#   "reduction_percentage": 20.0,
#   ...
# }
```

---

## PostScraperCleaner

Main orchestrator class for document cleaning.

### Definition

```python
class PostScraperCleaner:
    def __init__(
        self,
        config: CleaningConfig,
        progress_callback: Optional[Callable] = None
    )

    def clean_document(
        self,
        input_path: Path,
        output_path: Path
    ) -> CleaningResult

    def clean_batch(
        self,
        input_folder: Path,
        output_folder: Path,
        pattern: str = "*.md"
    ) -> List[CleaningResult]

    def get_statistics(self) -> Dict
```

### Methods

#### `__init__(config, progress_callback=None)`

Initialize PostScraperCleaner.

**Parameters**:
- `config` (CleaningConfig): Configuration
- `progress_callback` (Callable, optional): Progress callback function

**Progress Callback Format**:
```python
def progress_callback(update: Dict):
    # update = {
    #   "type": "progress",
    #   "processed": 5,
    #   "total": 10,
    #   "current_file": "doc5.md"
    # }
    pass
```

#### `clean_document(input_path, output_path) -> CleaningResult`

Clean a single document.

**Parameters**:
- `input_path` (Path): Input markdown file
- `output_path` (Path): Output markdown file

**Returns**:
- `CleaningResult`: Result object with metadata

**Raises**:
- `FileNotFoundError`: If input file doesn't exist
- `ValueError`: If input is not `.md` file

**Example**:
```python
from pathlib import Path

cleaner = PostScraperCleaner(config)
result = cleaner.clean_document(
    Path("input.md"),
    Path("output.md")
)

if result.success:
    print(f"Reduction: {result.reduction_percentage:.1f}%")
else:
    print(f"Error: {result.error_message}")
```

#### `clean_batch(input_folder, output_folder, pattern="*.md") -> List[CleaningResult]`

Process multiple documents in batch.

**Parameters**:
- `input_folder` (Path): Input folder
- `output_folder` (Path): Output folder
- `pattern` (str): Glob pattern (default: "*.md")

**Returns**:
- `List[CleaningResult]`: Results for all files

**Features**:
- Creates output folder if missing
- Continues on individual file errors
- Calls progress callback for each file
- Updates statistics automatically

**Example**:
```python
results = cleaner.clean_batch(
    Path("input_docs"),
    Path("output_docs")
)

for result in results:
    status = "✓" if result.success else "✗"
    print(f"{status} {result.input_file.name}: {result.reduction_percentage:.1f}%")
```

#### `get_statistics() -> Dict`

Get aggregated processing statistics.

**Returns** (Dict):
```python
{
    "total_processed": 10,
    "total_success": 10,
    "total_failed": 0,
    "success_rate": 1.0,
    "total_bytes_before": 100000,
    "total_bytes_after": 80000,
    "overall_reduction_percentage": 20.0,
    "total_processing_time": 0.5,
    "average_processing_time": 0.05,
    "total_llm_cost": 0.02,
    "total_chunks_created": 50,
}
```

**Example**:
```python
stats = cleaner.get_statistics()
print(f"Processed: {stats['total_processed']}")
print(f"Success rate: {stats['success_rate']*100:.1f}%")
print(f"Overall reduction: {stats['overall_reduction_percentage']:.1f}%")
print(f"Total cost: ${stats['total_llm_cost']:.2f}")
```

---

## RuleBasedCleaner

Pattern-based content cleaning engine.

### Definition

```python
class RuleBasedCleaner:
    def __init__(
        self,
        config: CleaningConfig,
        pattern_registry: PatternRegistry = None
    )

    def clean(self, content: str) -> Tuple[str, Dict]
```

### Methods

#### `clean(content) -> Tuple[str, Dict]`

Clean content using rule-based patterns.

**Parameters**:
- `content` (str): Markdown content

**Returns**:
- Tuple of:
  - `str`: Cleaned content
  - `Dict`: Cleaning metadata

**Metadata** (Dict):
```python
{
    "patterns_applied": 5,           # Number of patterns matched
    "total_replacements": 8,         # Total replacements made
    "removed_sections": [            # Pattern names that matched
        "skip_navigation",
        "footer_section",
        ...
    ],
    "confidence_score": 0.88,        # Average confidence
    "structure_score": 0.85,         # Content structure score (0-1)
}
```

**Example**:
```python
cleaner = RuleBasedCleaner(config)
cleaned, metadata = cleaner.clean(content)

print(f"Patterns applied: {metadata['patterns_applied']}")
print(f"Confidence: {metadata['confidence_score']:.1%}")
print(f"Structure: {metadata['structure_score']:.1%}")
```

---

## LLM Integration

Optional OpenAI API integration for content validation.

### LLMValidator

```python
from llm_cleaner import LLMValidator, LLMConfig

config = LLMConfig(
    api_key="sk-your-key",
    model="gpt-4o-mini",
    temperature=0.1,
    max_tokens=1000,
    rate_limit_rpm=500,
)

validator = LLMValidator(config)
result = validator.validate_content(content)
```

### ValidationResult

```python
@dataclass
class ValidationResult:
    is_valid: bool                   # Content is valid
    confidence: float                # Confidence 0.0-1.0
    issues: List[str]               # Detected issues
    suggestions: List[str]           # Improvement suggestions
    improved_content: Optional[str]  # Improved content (if available)
    input_tokens: int                # Input tokens used
    output_tokens: int               # Output tokens used
    cost: float                      # Cost in USD
    cached: bool                     # Result from cache
```

### Cost Calculation

- **Input**: $0.150 per 1M tokens (GPT-4o-mini)
- **Output**: $0.600 per 1M tokens (GPT-4o-mini)

**Example**:
```python
# 1000 input tokens, 200 output tokens
# Cost = (1000/1M * $0.150) + (200/1M * $0.600)
# Cost ≈ $0.00015 + $0.00012 = $0.00027
```

---

## Chunk Optimization

Prepares content for vector database embedding.

### ChunkOptimizer

```python
from chunk_optimizer import ChunkOptimizer

optimizer = ChunkOptimizer(
    chunk_size=512,          # tokens
    overlap=50,              # tokens
    preserve_structure=True  # preserve heading hierarchy
)

optimized, metadata = optimizer.optimize(content)
```

### ChunkMetadata

```python
@dataclass
class ChunkMetadata:
    total_chunks: int                      # Number of chunks
    heading_levels: Dict[int, int]        # Heading distribution H1-H6
    code_blocks: int                      # Number of code blocks
    tables: int                           # Number of tables
    lists: int                            # Number of lists
    semantic_boundaries: List[int]        # Boundary positions
    avg_chunk_size: int                   # Average chunk size (tokens)
    optimization_notes: List[str]         # Notes about optimization
```

### Token Estimation

Approximate: 1 token ≈ 4 characters

```python
# 4000 characters ≈ 1000 tokens
text = "..." * 1000  # 4000 chars
tokens = optimizer._estimate_tokens(text)  # ~1000
```

---

## Examples

### Example 1: Basic Cleaning

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

# Configure
config = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
)

# Process
cleaner = PostScraperCleaner(config)
result = cleaner.clean_document(
    Path("scraped.md"),
    Path("cleaned.md")
)

# Check result
print(f"Success: {result.success}")
print(f"Reduction: {result.reduction_percentage:.1f}%")
print(f"Removed: {', '.join(result.removed_sections)}")
```

### Example 2: Batch Processing with Progress

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

def show_progress(update):
    if update['type'] == 'progress':
        print(f"[{update['processed']}/{update['total']}] {update['current_file']}")

config = CleaningConfig()
cleaner = PostScraperCleaner(config, progress_callback=show_progress)

results = cleaner.clean_batch(
    Path("input_folder"),
    Path("output_folder")
)

stats = cleaner.get_statistics()
print(f"\nProcessed: {stats['total_processed']} files")
print(f"Success rate: {stats['success_rate']*100:.1f}%")
print(f"Overall reduction: {stats['overall_reduction_percentage']:.1f}%")
```

### Example 3: With LLM Validation

```python
import os
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

config = CleaningConfig(
    enable_llm_validation=True,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    llm_confidence_threshold=0.85,
)

cleaner = PostScraperCleaner(config)
result = cleaner.clean_document(Path("input.md"), Path("output.md"))

if result.llm_validation:
    validation = result.llm_validation
    print(f"Valid: {validation['is_valid']}")
    print(f"Confidence: {validation['confidence']:.1%}")
    print(f"Cost: ${validation['cost']:.4f}")
```

### Example 4: Vector DB Preparation

```python
from PostScraperCleaner import PostScraperCleaner, CleaningConfig
from pathlib import Path

config = CleaningConfig(
    enable_chunk_optimization=True,
    target_chunk_size=512,    # OpenAI embedding size
    overlap_size=50,
)

cleaner = PostScraperCleaner(config)
results = cleaner.clean_batch(
    Path("scraped_docs"),
    Path("ready_for_embeddings")
)

for result in results:
    if result.chunk_metadata:
        meta = result.chunk_metadata
        print(f"{result.input_file.name}:")
        print(f"  Chunks: {meta['total_chunks']}")
        print(f"  Avg size: {meta['avg_chunk_size']} tokens")
        print(f"  Code blocks: {meta['code_blocks']}")
```

---

## Error Handling

### Exception Types

```python
# FileNotFoundError - Input file not found
try:
    result = cleaner.clean_document(Path("missing.md"), Path("out.md"))
except FileNotFoundError as e:
    print(f"File error: {e}")

# ValueError - Invalid configuration or file format
try:
    result = cleaner.clean_document(Path("file.txt"), Path("out.md"))
except ValueError as e:
    print(f"Format error: {e}")

# Generic Exception - LLM or other errors
try:
    result = cleaner.clean_document(Path("in.md"), Path("out.md"))
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Result Error Handling

```python
result = cleaner.clean_document(Path("in.md"), Path("out.md"))

if not result.success:
    print(f"Error: {result.error_message}")

if result.warnings:
    for warning in result.warnings:
        print(f"Warning: {warning}")
```

---

## Performance Characteristics

| Operation | Time | Memory |
|-----------|------|--------|
| Single file (50KB) | 10-50ms | O(n) |
| Single file (1MB) | 50-100ms | O(n) |
| Pattern lookup | <100µs | ~1KB |
| Registry creation | <10ms | ~100KB |
| Chunk optimization (100KB) | <100ms | O(n) |

---

## Backward Compatibility

All new features (Phases 2-3) are backward compatible:

```python
# Old code still works
config = CleaningConfig()  # Uses defaults
cleaner = PostScraperCleaner(config)
result = cleaner.clean_document(in_path, out_path)

# New features optional
assert result.llm_cost == 0.0  # Not used
assert result.chunk_metadata is not None  # Optimization enabled by default
```

---

## See Also

- [User Guide](USER_GUIDE.md)
- [Configuration Guide](CONFIGURATION_GUIDE.md)
- [Integration Guide](INTEGRATION_GUIDE.md)
- [Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md)

---

**Version**: 1.0 | **Status**: Production Ready | **Last Updated**: 2025-01-07
