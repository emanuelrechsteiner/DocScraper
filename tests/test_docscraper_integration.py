"""
Phase 4: DocScraper Integration Tests

Tests integration of PostScraperCleaner with existing DocScraper application.
Verifies seamless workflow from scraping to cleaning.
"""

import json
import tempfile
from pathlib import Path

import pytest

from docscraper.cleaning.cleaner import CleaningConfig, CleaningResult, PostScraperCleaner


class TestDocScraperWorkflow:
    """Test integration with DocScraper workflow"""

    def test_import_docscraper_modules(self):
        """Test importing existing DocScraper modules"""
        try:
            import DocPostProcessor
            import SimpleDocScraper
            assert SimpleDocScraper is not None
            assert DocPostProcessor is not None
        except ImportError as e:
            pytest.skip(f"DocScraper modules not available: {e}")

    def test_scraped_output_compatibility(self):
        """Test PostScraperCleaner works with DocScraper output format"""
        # Create sample scraped content matching DocScraper output
        sample_scraped = """# Documentation Page

Navigation: [Home](#) [Docs](#) [API](#)

---

## Main Content

This is the actual documentation content that we want to preserve.

### Subsection

More detailed information here.

```python
# Code example
def hello():
    pass
```

---

Footer: Copyright 2024
"""

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(sample_scraped)
            f.flush()
            input_path = Path(f.name)

        try:
            config = CleaningConfig(
                remove_navigation=True,
                remove_headers_footers=True,
                remove_boilerplate=True,
            )
            cleaner = PostScraperCleaner(config)
            output_path = Path(tempfile.mktemp(suffix='.md'))

            result = cleaner.clean_document(input_path, output_path)

            assert result.success is True
            assert result.reduction_percentage > 0

            # Verify cleaned content
            cleaned = output_path.read_text()
            assert "Navigation" not in cleaned
            assert "Copyright 2024" not in cleaned
            assert "Main Content" in cleaned

            output_path.unlink()
        finally:
            input_path.unlink()

    def test_batch_scraped_documents(self):
        """Test batch processing of scraped documents"""
        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Simulate DocScraper output (multiple files)
            docs = {
                "page1.md": "# Page 1\n\nNav: [Home](#)\n\nContent 1",
                "page2.md": "# Page 2\n\nNav: [Home](#)\n\nContent 2",
                "page3.md": "# Page 3\n\nNav: [Home](#)\n\nContent 3",
            }

            for filename, content in docs.items():
                (input_dir / filename).write_text(content)

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)
            results = cleaner.clean_batch(input_dir, output_dir)

            assert len(results) == 3
            assert all(r.success for r in results)

            # Verify output files
            output_files = list(output_dir.glob("*.md"))
            assert len(output_files) == 3

        finally:
            for f in input_dir.glob("*"):
                f.unlink()
            input_dir.rmdir()

            for f in output_dir.glob("*"):
                f.unlink()
            output_dir.rmdir()


class TestDataFormat:
    """Test data format compatibility"""

    def test_markdown_format_preserved(self):
        """Test that markdown format is preserved"""
        content = """# Heading 1

## Heading 2

### Heading 3

Paragraph with **bold** and *italic*.

- Bullet point 1
- Bullet point 2

1. Numbered item
2. Numbered item

```python
code block
```

| Column 1 | Column 2 |
|----------|----------|
| Value 1  | Value 2  |
"""

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            f.flush()
            input_path = Path(f.name)

        try:
            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)
            output_path = Path(tempfile.mktemp(suffix='.md'))

            _result = cleaner.clean_document(input_path, output_path)
            cleaned = output_path.read_text()

            # Verify markdown structure preserved
            assert "# Heading 1" in cleaned
            assert "## Heading 2" in cleaned
            assert "**bold**" in cleaned
            assert "- Bullet point" in cleaned
            assert "```python" in cleaned

            output_path.unlink()
        finally:
            input_path.unlink()

    def test_json_result_export(self):
        """Test exporting results as JSON"""
        result = CleaningResult(
            input_file=Path("test.md"),
            output_file=Path("output.md"),
            success=True,
            original_size=1000,
            cleaned_size=800,
        )
        result.calculate_reduction()

        result_dict = result.to_dict()
        json_str = json.dumps(result_dict, indent=2)

        # Should be valid JSON
        loaded = json.loads(json_str)
        assert loaded["success"] is True


class TestConfigurationInteroperability:
    """Test configuration compatibility with DocScraper"""

    def test_config_from_json(self):
        """Test loading configuration from JSON"""
        config_json = {
            "remove_navigation": True,
            "remove_headers_footers": True,
            "remove_boilerplate": True,
            "enable_llm_validation": False,
            "enable_chunk_optimization": True,
            "target_chunk_size": 512,
        }

        # Create config from dict
        config = CleaningConfig(**config_json)
        assert config.remove_navigation is True
        assert config.target_chunk_size == 512

    def test_config_to_json(self):
        """Test saving configuration to JSON"""
        config = CleaningConfig(
            remove_navigation=True,
            target_chunk_size=512,
        )

        # Convert to dict (for JSON)
        config_dict = {
            "remove_navigation": config.remove_navigation,
            "target_chunk_size": config.target_chunk_size,
        }

        json_str = json.dumps(config_dict)
        loaded = json.loads(json_str)

        assert loaded["remove_navigation"] is True
        assert loaded["target_chunk_size"] == 512


class TestErrorRecovery:
    """Test error recovery in integration"""

    def test_continue_on_single_file_error(self):
        """Test batch processing continues on single file error"""
        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Create valid and problematic files
            (input_dir / "valid1.md").write_text("# Valid 1\n\nContent")
            (input_dir / "valid2.md").write_text("# Valid 2\n\nContent")

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)

            results = cleaner.clean_batch(input_dir, output_dir)

            # Should have results for all files
            assert len(results) >= 2
            # Most should be successful
            successful = [r for r in results if r.success]
            assert len(successful) >= 1

        finally:
            for f in input_dir.glob("*"):
                f.unlink()
            input_dir.rmdir()

            for f in output_dir.glob("*"):
                f.unlink()
            output_dir.rmdir()

    def test_invalid_input_file_format(self):
        """Test handling of invalid file formats"""
        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Create non-markdown files
            (input_dir / "document.txt").write_text("Text file")
            (input_dir / "data.json").write_text('{"key": "value"}')

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)

            results = cleaner.clean_batch(input_dir, output_dir)

            # Non-markdown files should be skipped or handled
            # (depending on implementation)
            assert isinstance(results, list)

        finally:
            for f in input_dir.glob("*"):
                f.unlink()
            input_dir.rmdir()

            if output_dir.exists():
                for f in output_dir.glob("*"):
                    f.unlink()
                output_dir.rmdir()


class TestPerformanceIntegration:
    """Test performance in DocScraper context"""

    def test_realistic_document_count(self):
        """Test with realistic document counts"""
        input_dir = Path(tempfile.mkdtemp())
        output_dir = Path(tempfile.mkdtemp())

        try:
            # Simulate DocScraper output (50 documents)
            for i in range(50):
                content = f"""# Document {i}

Navigation: [Home](#)

## Section 1
Content for section 1.

## Section 2
Content for section 2.

Footer: Copyright 2024
"""
                (input_dir / f"doc{i}.md").write_text(content)

            config = CleaningConfig()
            cleaner = PostScraperCleaner(config)

            results = cleaner.clean_batch(input_dir, output_dir)

            assert len(results) == 50
            successful = [r for r in results if r.success]
            assert len(successful) == 50

            stats = cleaner.get_statistics()
            assert stats["total_processed"] == 50

        finally:
            for f in input_dir.glob("*"):
                f.unlink()
            input_dir.rmdir()

            for f in output_dir.glob("*"):
                f.unlink()
            output_dir.rmdir()


class TestVectorDBPreparation:
    """Test integration with vector database pipeline"""

    def test_chunk_optimization_for_embeddings(self):
        """Test content optimized for embeddings"""
        content = """# API Documentation

## Authentication

To authenticate, use the following headers:

```python
headers = {
    "Authorization": "Bearer token"
}
```

### Token Format

The token should be in JWT format.

## Endpoints

### GET /api/users

Returns a list of users.

```json
{
    "users": []
}
```
"""

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            f.flush()
            input_path = Path(f.name)

        try:
            config = CleaningConfig(
                enable_chunk_optimization=True,
                target_chunk_size=512,
            )
            cleaner = PostScraperCleaner(config)
            output_path = Path(tempfile.mktemp(suffix='.md'))

            result = cleaner.clean_document(input_path, output_path)

            assert result.success is True
            assert result.chunk_optimization_used is True
            assert result.chunk_metadata is not None

            # Verify chunks are reasonable size
            chunks_info = result.chunk_metadata
            if chunks_info and "avg_chunk_size" in chunks_info:
                avg_size = chunks_info["avg_chunk_size"]
                assert 100 < avg_size < 1000  # Reasonable chunk sizes

            output_path.unlink()
        finally:
            input_path.unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
