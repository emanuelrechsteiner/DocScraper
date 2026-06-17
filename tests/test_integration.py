"""
Phase 2 Integration Tests

End-to-end tests for PostScraperCleaner with Phase 2 features enabled.
Tests verify chunk optimization works seamlessly with cleaning.
"""

import shutil
import tempfile
import pytest
from pathlib import Path
from docscraper.cleaning.cleaner import PostScraperCleaner, CleaningConfig


@pytest.fixture
def temp_markdown_file():
    """Create a temporary markdown file for testing"""
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.md',
        delete=False,
        encoding='utf-8'
    ) as f:
        content = """# Main Document

This is a test document for integration testing.

## Section 1

Some introduction text here that explains the concept.

```python
def example():
    return "Hello, World!"
```

More content after code block.

## Section 2

Additional information goes here.

### Subsection 2.1

Deep content in subsection.

- Item 1
- Item 2
- Item 3

## Section 3

Final section with content.

Navigation: [Back](#) [Next](#)

---

Copyright 2024. All rights reserved.
"""
        f.write(content)
        f.flush()
        yield Path(f.name)

    # Cleanup
    Path(f.name).unlink(missing_ok=True)


@pytest.fixture
def temp_output_dir():
    """Create temporary output directory"""
    temp_dir = Path(tempfile.mkdtemp())
    yield temp_dir
    # Cleanup — rmtree handles nested subdirectories (a plain unlink loop
    # raises PermissionError on directory entries).
    shutil.rmtree(temp_dir, ignore_errors=True)


class TestPhase2CleaningIntegration:
    """Integration tests for Phase 2 with full pipeline"""

    def test_cleaning_with_chunk_optimization(
        self, temp_markdown_file, temp_output_dir
    ):
        """Test full cleaning pipeline with chunk optimization"""
        config = CleaningConfig(
            enable_chunk_optimization=True,
            target_chunk_size=256,
            overlap_size=30,
            enable_llm_validation=False
        )

        cleaner = PostScraperCleaner(config)
        output_path = temp_output_dir / "output.md"

        result = cleaner.clean_document(temp_markdown_file, output_path)

        # Verify result
        assert result.success is True
        assert result.chunk_optimization_used is True
        assert result.chunk_metadata is not None
        assert result.chunk_metadata.get("total_chunks", 0) > 0

        # Verify output file exists and has content
        assert output_path.exists()
        with open(output_path, 'r', encoding='utf-8') as f:
            cleaned_content = f.read()
        assert len(cleaned_content) > 0

    def test_cleaning_without_chunk_optimization(
        self, temp_markdown_file, temp_output_dir
    ):
        """Test cleaning without chunk optimization (backward compatibility)"""
        config = CleaningConfig(
            enable_chunk_optimization=False,
            enable_llm_validation=False
        )

        cleaner = PostScraperCleaner(config)
        output_path = temp_output_dir / "output.md"

        result = cleaner.clean_document(temp_markdown_file, output_path)

        # Verify backward compatibility
        assert result.success is True
        assert result.chunk_optimization_used is False
        assert result.chunk_metadata is None
        assert output_path.exists()

    def test_size_reduction(self, temp_markdown_file, temp_output_dir):
        """Test that cleaning reduces file size"""
        config = CleaningConfig(
            remove_navigation=True,
            remove_headers_footers=True,
            enable_chunk_optimization=True
        )

        cleaner = PostScraperCleaner(config)
        output_path = temp_output_dir / "output.md"

        result = cleaner.clean_document(temp_markdown_file, output_path)

        # Should reduce size by removing navigation/footer
        assert result.reduction_percentage > 0
        assert result.cleaned_size < result.original_size

    def test_batch_processing_with_phase2(self, temp_output_dir):
        """Test batch processing with Phase 2 features"""
        # Create test files
        input_dir = Path(tempfile.mkdtemp())
        try:
            for i in range(3):
                file_path = input_dir / f"doc{i}.md"
                file_path.write_text(
                    f"# Document {i}\n\nContent for doc {i}.\n\n"
                    f"Navigation: [Home](#) [Next](#)\n\n"
                    f"Footer content here."
                )

            config = CleaningConfig(
                enable_chunk_optimization=True,
                target_chunk_size=300
            )
            cleaner = PostScraperCleaner(config)
            results = cleaner.clean_batch(input_dir, temp_output_dir)

            # Verify batch results
            assert len(results) == 3
            assert all(r.success for r in results)
            assert all(r.chunk_optimization_used for r in results)
            assert len(list(temp_output_dir.glob("*.md"))) == 3

        finally:
            # Cleanup input files
            for file in input_dir.glob("*.md"):
                file.unlink()
            input_dir.rmdir()

    def test_statistics_tracking(self, temp_markdown_file, temp_output_dir):
        """Test Phase 2 statistics tracking"""
        config = CleaningConfig(enable_chunk_optimization=True)
        cleaner = PostScraperCleaner(config)

        output_path = temp_output_dir / "output.md"
        _result = cleaner.clean_document(temp_markdown_file, output_path)

        stats = cleaner.get_statistics()

        assert stats["total_processed"] == 1
        assert stats["total_success"] == 1
        assert stats["total_chunks_created"] > 0

    def test_error_handling_on_chunk_error(
        self, temp_markdown_file, temp_output_dir
    ):
        """Test graceful error handling if chunk optimization fails"""
        config = CleaningConfig(
            enable_chunk_optimization=True,
            target_chunk_size=256
        )

        cleaner = PostScraperCleaner(config)
        # Create output path in non-existent directory
        output_path = temp_output_dir / "subdir" / "output.md"

        result = cleaner.clean_document(temp_markdown_file, output_path)

        # Should succeed (directories created)
        assert result.success is True
        assert output_path.exists()

    def test_config_validation(self):
        """Test config validation for Phase 2 parameters"""
        # Valid config
        config = CleaningConfig(
            target_chunk_size=512,
            overlap_size=50,
            enable_chunk_optimization=True
        )
        assert config.target_chunk_size == 512

        # Test validation in cleaner
        cleaner = PostScraperCleaner(config)
        assert cleaner.config.target_chunk_size == 512
        assert cleaner.chunk_optimizer is not None


class TestChunkMetadataTracking:
    """Test chunk metadata is properly tracked"""

    def test_metadata_fields(self, temp_markdown_file, temp_output_dir):
        """Test all chunk metadata fields are populated"""
        config = CleaningConfig(enable_chunk_optimization=True)
        cleaner = PostScraperCleaner(config)

        output_path = temp_output_dir / "output.md"
        result = cleaner.clean_document(temp_markdown_file, output_path)

        metadata = result.chunk_metadata
        assert metadata is not None
        assert "total_chunks" in metadata
        assert "heading_levels" in metadata
        assert "code_blocks" in metadata
        assert "avg_chunk_size" in metadata


if __name__ == "__main__":
    # Run tests: pytest test_integration.py -v
    pytest.main([__file__, "-v"])
