# DocScraper API Reference

## Table of Contents
- [Overview](#overview)
- [Core Classes](#core-classes)
- [API Methods](#api-methods)
- [Data Models](#data-models)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Examples](#examples)

---

## Overview

DocScraper is a high-performance document processing pipeline that converts raw documents into a structured vector database with intelligent classification and dependency analysis.

### Key Features
- Asynchronous parallel processing
- OpenAI-powered classification
- Checkpoint/recovery system
- Real-time progress tracking
- Automatic dependency graph generation

---

## Core Classes

### DocumentPostProcessor

The main processing engine that orchestrates the document pipeline.

```python
class DocumentPostProcessor:
    """
    High-performance document processor with checkpoint recovery.
    
    Attributes:
        input_dir (Path): Source directory containing documents
        output_dir (Path): Destination for processed documents
        api_key (str): OpenAI API key for classification
        processed_docs (List[ProcessedDocument]): Processed documents
        checkpoint_dir (Path): Directory for checkpoint files
    """
    
    def __init__(
        self,
        input_dir: str,
        output_dir: str,
        api_key: str
    ) -> None:
        """
        Initialize the document processor.
        
        Args:
            input_dir: Path to input documents
            output_dir: Path for output (auto-generates dated subdirectory)
            api_key: OpenAI API key
            
        Raises:
            ValueError: If input_dir doesn't exist
            PermissionError: If output_dir isn't writable
        """
```

#### Methods

##### process_all_documents

```python
async def process_all_documents(
    self,
    recursive: bool = True,
    flatten_output: bool = True
) -> Dict[str, Any]:
    """
    Process all documents in the input directory.
    
    Args:
        recursive: Process subdirectories recursively
        flatten_output: Flatten directory structure in output
        
    Returns:
        Dictionary containing:
            - total_processed: Number of documents processed
            - categories: Document count by category
            - processing_time: Total time in seconds
            - output_dir: Path to output directory
            
    Raises:
        ProcessingError: If processing fails
        
    Example:
        >>> processor = DocumentPostProcessor(input_dir, output_dir, api_key)
        >>> result = await processor.process_all_documents()
        >>> print(f"Processed {result['total_processed']} documents")
    """
```

##### save_checkpoint

```python
def save_checkpoint(
    self,
    phase: str,
    additional_data: Dict = None
) -> Path:
    """
    Save processing state to checkpoint file.
    
    Args:
        phase: Current processing phase ('file_processing', 'pre_classification', 
               'post_classification', 'completed')
        additional_data: Optional additional data to save
        
    Returns:
        Path to saved checkpoint file
        
    Note:
        Checkpoints are saved automatically every 100 documents
        and at critical phase transitions.
    """
```

##### load_checkpoint

```python
def load_checkpoint(
    self,
    checkpoint_file: str
) -> Dict[str, Any]:
    """
    Load processing state from checkpoint.
    
    Args:
        checkpoint_file: Path to checkpoint file
        
    Returns:
        Dictionary containing checkpoint data
        
    Raises:
        FileNotFoundError: If checkpoint doesn't exist
        JSONDecodeError: If checkpoint is corrupted
    """
```

---

### DocumentSorter

Handles document classification and dependency analysis.

```python
class DocumentSorter:
    """
    Intelligent document classifier using OpenAI GPT models.
    
    Attributes:
        use_llm (bool): Whether to use OpenAI for classification
        client (OpenAI): OpenAI client instance
    """
```

#### Methods

##### classify_document

```python
async def classify_document(
    self,
    doc: ProcessedDocument
) -> str:
    """
    Classify a document using AI or rule-based approach.
    
    Args:
        doc: Document to classify
        
    Returns:
        Category string ('tutorials', 'api', 'guides', 'reference', 
        'concepts', 'troubleshooting', 'examples', 'configuration')
        
    Note:
        Falls back to rule-based classification if API fails.
    """
```

##### create_dependency_graph

```python
def create_dependency_graph(
    self,
    documents: List[ProcessedDocument]
) -> nx.DiGraph:
    """
    Create dependency graph between documents.
    
    Args:
        documents: List of processed documents
        
    Returns:
        NetworkX directed graph with documents as nodes
        
    Note:
        Uses sampling for large datasets (>1000 documents)
        to maintain O(n) complexity.
    """
```

---

## Data Models

### ProcessedDocument

```python
@dataclass
class ProcessedDocument:
    """
    Represents a processed document.
    
    Attributes:
        file_path (str): Path to the original file
        original_url (str): Source URL if available
        title (str): Document title
        chunks (List[DocumentChunk]): Document chunks
        category (Optional[str]): Assigned category
        topics (List[str]): Extracted topics
        dependencies (List[str]): Document dependencies
        complexity_score (float): Calculated complexity (0-1)
    """
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'ProcessedDocument':
        """Create instance from dictionary."""
```

### DocumentChunk

```python
@dataclass
class DocumentChunk:
    """
    Represents a chunk of document content.
    
    Attributes:
        content (str): Chunk text content
        metadata (Dict[str, Any]): Chunk metadata
        chunk_id (str): Unique identifier
        parent_doc (str): Parent document path
        position (int): Position in document
        tokens (int): Token count
        embedding (Optional[List[float]]): Vector embedding
    """
```

---

## Configuration

### Environment Variables

```bash
# Required
OPENAI_API_KEY=sk-...  # Your OpenAI API key

# Optional
DOC_PROCESSOR_MAX_WORKERS=25  # Max parallel workers
DOC_PROCESSOR_BATCH_SIZE=50   # Batch size for processing
DOC_PROCESSOR_CHECKPOINT_INTERVAL=100  # Documents between checkpoints
```

### Configuration File

```python
# config.py
CONFIG = {
    "processing": {
        "max_workers": 25,
        "batch_size": 50,
        "checkpoint_interval": 100,
        "timeout_seconds": 15
    },
    "openai": {
        "model": "gpt-4o-mini",
        "max_completion_tokens": 20,
        "temperature": 0.3,
        "timeout": 15
    },
    "output": {
        "base_directory": "/Volumes/NvME-Satechi/VectorDatabase",
        "create_dated_folders": True,
        "flatten_structure": True
    }
}
```

---

## Error Handling

### Exception Hierarchy

```python
class DocScraperError(Exception):
    """Base exception for DocScraper."""

class ProcessingError(DocScraperError):
    """Raised when document processing fails."""

class ClassificationError(DocScraperError):
    """Raised when classification fails."""

class CheckpointError(DocScraperError):
    """Raised when checkpoint operations fail."""

class APIError(DocScraperError):
    """Raised when API calls fail."""
```

### Error Recovery

```python
try:
    result = await processor.process_all_documents()
except ProcessingError as e:
    # Attempt recovery from checkpoint
    checkpoint = processor.load_latest_checkpoint()
    if checkpoint:
        processor.resume_from_checkpoint(checkpoint)
    else:
        raise e
```

---

## Examples

### Basic Usage

```python
import asyncio
from DocPostProcessor import DocumentPostProcessor

async def main():
    # Initialize processor
    processor = DocumentPostProcessor(
        input_dir="/path/to/documents",
        output_dir="/path/to/output",
        api_key="sk-..."
    )
    
    # Process documents
    result = await processor.process_all_documents()
    
    # Print summary
    print(f"Processed {result['total_processed']} documents")
    print(f"Output saved to {result['output_dir']}")

asyncio.run(main())
```

### Resume from Checkpoint

```python
async def resume_processing():
    # Find latest checkpoint
    checkpoint_file = find_latest_checkpoint()
    
    # Create processor
    processor = DocumentPostProcessor(
        input_dir="/path/to/documents",
        output_dir="/path/to/output",
        api_key="sk-..."
    )
    
    # Load checkpoint
    processor.load_checkpoint(checkpoint_file)
    
    # Resume processing
    await processor.resume_processing()
```

### Custom Classification

```python
class CustomSorter(DocumentSorter):
    """Extended sorter with custom categories."""
    
    async def classify_document(self, doc):
        # Custom classification logic
        if "API" in doc.title:
            return "api_reference"
        
        # Fall back to parent implementation
        return await super().classify_document(doc)
```

### Progress Monitoring

```python
async def process_with_progress():
    processor = DocumentPostProcessor(...)
    
    # Set up progress callback
    def progress_callback(current, total, phase):
        percent = (current / total) * 100
        print(f"{phase}: {current}/{total} ({percent:.1f}%)")
    
    processor.set_progress_callback(progress_callback)
    
    await processor.process_all_documents()
```

---

## Performance Considerations

### Optimization Guidelines

1. **Batch Size**: Adjust based on document size
   - Small docs (<1KB): batch_size=100
   - Medium docs (1-10KB): batch_size=50
   - Large docs (>10KB): batch_size=25

2. **Worker Count**: Based on system resources
   - CPU cores * 2 for I/O bound operations
   - CPU cores for CPU bound operations

3. **Memory Management**:
   - Process in batches to avoid memory exhaustion
   - Use gc.collect() after large batches
   - Monitor with memory_profiler

### Benchmarks

| Dataset Size | Processing Time | Throughput | Memory Usage |
|-------------|-----------------|------------|--------------|
| 100 docs    | 5 seconds      | 20 docs/sec | 100 MB      |
| 1,000 docs  | 30 seconds     | 33 docs/sec | 500 MB      |
| 10,000 docs | 5 minutes      | 33 docs/sec | 2 GB        |
| 100,000 docs| 45 minutes     | 37 docs/sec | 4 GB        |

---

## API Rate Limits

### OpenAI Rate Limits

| Model | Requests/min | Tokens/min |
|-------|-------------|------------|
| gpt-4o-mini | 500 | 200,000 |
| gpt-3.5-turbo | 3,500 | 90,000 |

### Handling Rate Limits

```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
async def call_openai_with_retry(prompt):
    return await client.chat.completions.create(...)
```

---

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| GUI Freezes | Blocking operations in main thread | Use threading/async |
| High Memory Usage | Loading all files at once | Process in batches |
| Slow Processing | Sequential operations | Use parallel processing |
| Token Waste | No checkpointing | Implement checkpoints |
| API Errors | Rate limits or timeouts | Add retry logic |

### Debug Mode

```python
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Process with verbose output
processor = DocumentPostProcessor(..., debug=True)
```

---

## Version History

- **v2.0.0** (2024-08-24): Major refactor with async processing
- **v1.5.0**: Added checkpoint system
- **v1.0.0**: Initial release

---

## License

MIT License - See LICENSE file for details

---

## Support

For issues and questions:
- GitHub Issues: [github.com/your-repo/issues](https://github.com)
- Documentation: [docs.your-site.com](https://docs.your-site.com)
- Email: support@your-site.com
