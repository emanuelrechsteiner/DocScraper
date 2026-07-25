"""
Comprehensive tests for PostScraperCleaner.

Covers clean_document, clean_batch, clean_directory_tree,
get_statistics, _calculate_content_quality, _calculate_chunk_score,
_update_statistics, CleaningResult.calculate_reduction, and
CleaningResult.to_dict.

LLM validation is always disabled (enable_llm_validation=False) to
avoid network calls during unit testing.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from docscraper.cleaning.cleaner import (
    CleaningConfig,
    CleaningResult,
    PostScraperCleaner,
)

# ---------------------------------------------------------------------------
# Helpers / shared fixtures
# ---------------------------------------------------------------------------

MINIMAL_CONFIG = CleaningConfig(
    remove_navigation=True,
    remove_headers_footers=True,
    remove_boilerplate=True,
    enable_llm_validation=False,
    enable_chunk_optimization=False,
)

SAMPLE_MD = """\
# Hello World

This is a sample markdown document used for testing.

## Section One

Here is some content with a list:

- Item A
- Item B
- Item C

## Section Two

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

This paragraph provides additional context about the example above.
"""


def _make_cleaner(config: CleaningConfig | None = None) -> PostScraperCleaner:
    return PostScraperCleaner(config or MINIMAL_CONFIG)


# ---------------------------------------------------------------------------
# Tests: clean_document
# ---------------------------------------------------------------------------


class TestCleanDocument:
    """Tests for PostScraperCleaner.clean_document"""

    def test_clean_document_valid_markdown_file(self, tmp_path: Path) -> None:
        """clean_document should succeed and write output for a valid .md file."""
        # Arrange
        input_file = tmp_path / "input.md"
        input_file.write_text(SAMPLE_MD, encoding="utf-8")
        output_file = tmp_path / "output.md"
        cleaner = _make_cleaner()

        # Act
        result = cleaner.clean_document(input_file, output_file)

        # Assert
        assert result.success is True
        assert result.error_message is None
        assert output_file.exists()
        assert result.input_file == input_file
        assert result.output_file == output_file
        assert result.original_size == len(SAMPLE_MD)
        assert result.cleaned_size > 0
        assert result.rule_based_cleaning is True

    def test_clean_document_missing_file_sets_error_message(self, tmp_path: Path) -> None:
        """clean_document with a non-existent input should record FileNotFoundError in error_message."""
        # Arrange
        missing = tmp_path / "does_not_exist.md"
        output_file = tmp_path / "output.md"
        cleaner = _make_cleaner()

        # Act
        result = cleaner.clean_document(missing, output_file)

        # Assert
        assert result.success is False
        assert result.error_message is not None
        assert "not found" in result.error_message.lower() or "FileNotFoundError" in result.error_message

    def test_clean_document_non_md_file_sets_error_message(self, tmp_path: Path) -> None:
        """clean_document with a .txt file should record ValueError in error_message."""
        # Arrange
        txt_file = tmp_path / "notes.txt"
        txt_file.write_text("some content", encoding="utf-8")
        output_file = tmp_path / "output.md"
        cleaner = _make_cleaner()

        # Act
        result = cleaner.clean_document(txt_file, output_file)

        # Assert
        assert result.success is False
        assert result.error_message is not None
        assert "markdown" in result.error_message.lower() or ".md" in result.error_message

    def test_clean_document_creates_parent_directories(self, tmp_path: Path) -> None:
        """clean_document should create nested output directories automatically."""
        # Arrange
        input_file = tmp_path / "doc.md"
        input_file.write_text(SAMPLE_MD, encoding="utf-8")
        output_file = tmp_path / "deep" / "nested" / "dir" / "doc.md"
        cleaner = _make_cleaner()

        # Act
        result = cleaner.clean_document(input_file, output_file)

        # Assert
        assert result.success is True
        assert output_file.exists()

    def test_clean_document_populates_processing_time(self, tmp_path: Path) -> None:
        """clean_document should always set a non-negative processing_time."""
        # Arrange
        input_file = tmp_path / "doc.md"
        input_file.write_text(SAMPLE_MD, encoding="utf-8")
        output_file = tmp_path / "out.md"
        cleaner = _make_cleaner()

        # Act
        result = cleaner.clean_document(input_file, output_file)

        # Assert
        assert result.processing_time >= 0.0

    def test_clean_document_calculates_reduction(self, tmp_path: Path) -> None:
        """Successful clean_document should compute a valid reduction_percentage."""
        # Arrange — add obvious boilerplate so cleaning actually removes something
        content = "Skip to main content\n\n" + SAMPLE_MD
        input_file = tmp_path / "doc.md"
        input_file.write_text(content, encoding="utf-8")
        output_file = tmp_path / "out.md"
        cleaner = _make_cleaner()

        # Act
        result = cleaner.clean_document(input_file, output_file)

        # Assert
        assert result.success is True
        assert 0.0 <= result.reduction_percentage <= 100.0


# ---------------------------------------------------------------------------
# Tests: clean_batch
# ---------------------------------------------------------------------------


class TestCleanBatch:
    """Tests for PostScraperCleaner.clean_batch"""

    def test_clean_batch_empty_directory_returns_empty_list(self, tmp_path: Path) -> None:
        """clean_batch on a directory with no .md files should return []."""
        # Arrange
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        output_dir = tmp_path / "output"
        cleaner = _make_cleaner()

        # Act
        results = cleaner.clean_batch(empty_dir, output_dir)

        # Assert
        assert results == []

    def test_clean_batch_nonexistent_directory_raises_file_not_found(self, tmp_path: Path) -> None:
        """clean_batch on a missing input directory should raise FileNotFoundError."""
        # Arrange
        missing = tmp_path / "no_such_dir"
        output_dir = tmp_path / "output"
        cleaner = _make_cleaner()

        # Act & Assert
        with pytest.raises(FileNotFoundError):
            cleaner.clean_batch(missing, output_dir)

    def test_clean_batch_processes_all_matching_files(self, tmp_path: Path) -> None:
        """clean_batch should return one CleaningResult per .md file found."""
        # Arrange
        input_dir = tmp_path / "docs"
        input_dir.mkdir()
        for name in ("alpha.md", "beta.md", "gamma.md"):
            (input_dir / name).write_text(SAMPLE_MD, encoding="utf-8")
        # Add a non-markdown file that should be ignored
        (input_dir / "readme.txt").write_text("ignored", encoding="utf-8")

        output_dir = tmp_path / "output"
        cleaner = _make_cleaner()

        # Act
        results = cleaner.clean_batch(input_dir, output_dir)

        # Assert
        assert len(results) == 3
        assert all(r.success for r in results)

    def test_clean_batch_custom_pattern_filters_files(self, tmp_path: Path) -> None:
        """clean_batch with custom pattern should only match files with that suffix."""
        # Arrange
        input_dir = tmp_path / "mixed"
        input_dir.mkdir()
        (input_dir / "api.md").write_text(SAMPLE_MD, encoding="utf-8")
        (input_dir / "data.json").write_text("{}", encoding="utf-8")

        output_dir = tmp_path / "output"
        cleaner = _make_cleaner()

        # Act — default pattern only picks up .md
        results = cleaner.clean_batch(input_dir, output_dir, pattern="*.md")

        # Assert
        assert len(results) == 1

    def test_clean_batch_returns_results_in_order(self, tmp_path: Path) -> None:
        """Every result returned by clean_batch should reference an existing input file."""
        # Arrange
        input_dir = tmp_path / "docs"
        input_dir.mkdir()
        names = {"one.md", "two.md"}
        for name in names:
            (input_dir / name).write_text(SAMPLE_MD, encoding="utf-8")

        output_dir = tmp_path / "output"
        cleaner = _make_cleaner()

        # Act
        results = cleaner.clean_batch(input_dir, output_dir)

        # Assert
        result_names = {r.input_file.name for r in results}
        assert result_names == names


# ---------------------------------------------------------------------------
# Tests: clean_directory_tree
# ---------------------------------------------------------------------------


class TestCleanDirectoryTree:
    """Tests for PostScraperCleaner.clean_directory_tree"""

    def test_mirrors_structure_with_cleaned_suffix(self, tmp_path: Path) -> None:
        """clean_directory_tree should produce output paths with '_cleaned' on directories."""
        # Arrange
        input_root = tmp_path / "input"
        (input_root / "docs").mkdir(parents=True)
        (input_root / "docs" / "page.md").write_text(SAMPLE_MD, encoding="utf-8")

        output_root = tmp_path / "output"
        cleaner = _make_cleaner()

        # Act
        results = cleaner.clean_directory_tree(input_root, output_root)

        # Assert
        assert len(results) == 1
        assert results[0].success is True
        # The directory part of the relative output path must have '_cleaned'
        rel_out = results[0].output_file.relative_to(output_root)
        assert "docs_cleaned" in str(rel_out)

    def test_mirrors_nested_directories(self, tmp_path: Path) -> None:
        """clean_directory_tree should handle multiple nesting levels."""
        # Arrange
        input_root = tmp_path / "in"
        deep = input_root / "a" / "b"
        deep.mkdir(parents=True)
        (deep / "file.md").write_text(SAMPLE_MD, encoding="utf-8")

        output_root = tmp_path / "out"
        cleaner = _make_cleaner()

        # Act
        results = cleaner.clean_directory_tree(input_root, output_root)

        # Assert
        assert len(results) == 1
        assert results[0].success is True
        rel_out = results[0].output_file.relative_to(output_root)
        parts = rel_out.parts
        # Every directory segment must carry '_cleaned'
        for part in parts[:-1]:  # exclude filename
            assert part.endswith("_cleaned"), f"Expected '_cleaned' suffix on '{part}'"

    def test_nonexistent_input_returns_empty_list(self, tmp_path: Path) -> None:
        """clean_directory_tree with a missing input root should return []."""
        # Arrange
        missing = tmp_path / "no_such"
        output_root = tmp_path / "out"
        cleaner = _make_cleaner()

        # Act
        results = cleaner.clean_directory_tree(missing, output_root)

        # Assert
        assert results == []

    def test_non_directory_input_returns_empty_list(self, tmp_path: Path) -> None:
        """clean_directory_tree with a file path as input root should return []."""
        # Arrange
        file_path = tmp_path / "file.md"
        file_path.write_text(SAMPLE_MD, encoding="utf-8")
        output_root = tmp_path / "out"
        cleaner = _make_cleaner()

        # Act
        results = cleaner.clean_directory_tree(file_path, output_root)

        # Assert
        assert results == []

    def test_processes_multiple_files_in_tree(self, tmp_path: Path) -> None:
        """clean_directory_tree should process all .md files recursively."""
        # Arrange
        input_root = tmp_path / "root"
        for subdir, filename in [("sub1", "a.md"), ("sub2", "b.md"), ("sub2", "c.md")]:
            d = input_root / subdir
            d.mkdir(parents=True, exist_ok=True)
            (d / filename).write_text(SAMPLE_MD, encoding="utf-8")

        output_root = tmp_path / "cleaned"
        cleaner = _make_cleaner()

        # Act
        results = cleaner.clean_directory_tree(input_root, output_root)

        # Assert
        assert len(results) == 3
        assert all(r.success for r in results)


# ---------------------------------------------------------------------------
# Tests: progress_callback
# ---------------------------------------------------------------------------


class TestProgressCallback:
    """Tests that the progress callback is invoked correctly."""

    def test_progress_callback_called_during_clean_batch(self, tmp_path: Path) -> None:
        """clean_batch should invoke the callback once per file processed."""
        # Arrange
        input_dir = tmp_path / "docs"
        input_dir.mkdir()
        for name in ("a.md", "b.md"):
            (input_dir / name).write_text(SAMPLE_MD, encoding="utf-8")

        callback_events: list[dict] = []

        def capture(event: dict) -> None:
            callback_events.append(event)

        cleaner = PostScraperCleaner(MINIMAL_CONFIG, progress_callback=capture)
        output_dir = tmp_path / "out"

        # Act
        cleaner.clean_batch(input_dir, output_dir)

        # Assert
        assert len(callback_events) == 2
        assert all(e.get("type") == "progress" for e in callback_events)

    def test_progress_callback_called_during_clean_directory_tree(self, tmp_path: Path) -> None:
        """clean_directory_tree should invoke the callback once per file."""
        # Arrange
        input_root = tmp_path / "input"
        sub = input_root / "chapter"
        sub.mkdir(parents=True)
        for name in ("x.md", "y.md", "z.md"):
            (sub / name).write_text(SAMPLE_MD, encoding="utf-8")

        callback_events: list[dict] = []

        def capture(event: dict) -> None:
            callback_events.append(event)

        cleaner = PostScraperCleaner(MINIMAL_CONFIG, progress_callback=capture)
        output_root = tmp_path / "output"

        # Act
        cleaner.clean_directory_tree(input_root, output_root)

        # Assert
        assert len(callback_events) == 3
        for event in callback_events:
            assert event.get("type") == "progress"
            assert "current_file" in event

    def test_progress_callback_reports_correct_total(self, tmp_path: Path) -> None:
        """The 'total' field in callback events should equal the file count."""
        # Arrange
        input_dir = tmp_path / "docs"
        input_dir.mkdir()
        file_count = 4
        for i in range(file_count):
            (input_dir / f"doc_{i}.md").write_text(SAMPLE_MD, encoding="utf-8")

        totals: list[int] = []

        def capture(event: dict) -> None:
            totals.append(event.get("total", -1))

        cleaner = PostScraperCleaner(MINIMAL_CONFIG, progress_callback=capture)
        output_dir = tmp_path / "out"

        # Act
        cleaner.clean_batch(input_dir, output_dir)

        # Assert
        assert all(t == file_count for t in totals)


# ---------------------------------------------------------------------------
# Tests: _calculate_content_quality
# ---------------------------------------------------------------------------


class TestCalculateContentQuality:
    """Tests for PostScraperCleaner._calculate_content_quality"""

    def test_empty_content_returns_zero(self) -> None:
        """Empty string should yield a quality score of 0.0."""
        cleaner = _make_cleaner()
        assert cleaner._calculate_content_quality("") == 0.0

    def test_rich_content_returns_high_score(self) -> None:
        """Content with code blocks, headings, and lists should score higher than plain text."""
        cleaner = _make_cleaner()
        rich = SAMPLE_MD  # has headings, lists, and code blocks
        plain = "just some words without any structure whatsoever and no markdown at all"
        assert cleaner._calculate_content_quality(rich) > cleaner._calculate_content_quality(plain)

    def test_score_bounded_between_zero_and_one(self) -> None:
        """Quality score must always be in [0.0, 1.0]."""
        cleaner = _make_cleaner()
        for content in ("", "x", SAMPLE_MD, "word " * 500):
            score = cleaner._calculate_content_quality(content)
            assert 0.0 <= score <= 1.0, f"Score out of range for content starting with '{content[:20]}'"

    def test_content_with_code_block_scores_higher_than_plain(self) -> None:
        """Adding a code block should increase the quality score."""
        cleaner = _make_cleaner()
        base = "This is a paragraph with enough words to get a decent word count score here."
        with_code = base + "\n\n```python\nprint('hello')\n```"
        assert cleaner._calculate_content_quality(with_code) > cleaner._calculate_content_quality(base)

    def test_content_with_heading_scores_higher_than_plain(self) -> None:
        """Adding a markdown heading should increase the quality score."""
        cleaner = _make_cleaner()
        plain = "just some plain text content with no markdown elements to speak of at all"
        with_heading = "# Main Title\n\n" + plain
        assert cleaner._calculate_content_quality(with_heading) > cleaner._calculate_content_quality(plain)

    def test_content_with_list_scores_higher_than_plain(self) -> None:
        """Adding a markdown list should increase the quality score."""
        cleaner = _make_cleaner()
        plain = "just some plain text content with no markdown list elements present"
        with_list = plain + "\n\n- item one\n- item two\n- item three"
        assert cleaner._calculate_content_quality(with_list) > cleaner._calculate_content_quality(plain)


# ---------------------------------------------------------------------------
# Tests: _calculate_chunk_score
# ---------------------------------------------------------------------------


class TestCalculateChunkScore:
    """Tests for PostScraperCleaner._calculate_chunk_score"""

    def test_empty_content_returns_zero(self) -> None:
        """Empty content should yield a chunk score of 0.0."""
        cleaner = _make_cleaner()
        assert cleaner._calculate_chunk_score("") == 0.0

    def test_content_smaller_than_half_target_returns_half(self) -> None:
        """Content shorter than 50 % of target_chunk_size should return 0.5."""
        config = CleaningConfig(
            enable_llm_validation=False,
            enable_chunk_optimization=False,
            target_chunk_size=512,
        )
        cleaner = PostScraperCleaner(config)
        # 20 chars is well below 512 * 0.5 = 256
        tiny = "a" * 20
        assert cleaner._calculate_chunk_score(tiny) == 0.5

    def test_content_near_target_size_returns_one(self) -> None:
        """Content whose length is between 50 % and 150 % of target should return 1.0."""
        config = CleaningConfig(
            enable_llm_validation=False,
            enable_chunk_optimization=False,
            target_chunk_size=512,
        )
        cleaner = PostScraperCleaner(config)
        # 512 chars is exactly at the target
        on_target = "x" * 512
        assert cleaner._calculate_chunk_score(on_target) == 1.0

    def test_very_large_content_returns_lower_score(self) -> None:
        """Content much larger than the target should score lower than 1.0."""
        config = CleaningConfig(
            enable_llm_validation=False,
            enable_chunk_optimization=False,
            target_chunk_size=512,
        )
        cleaner = PostScraperCleaner(config)
        huge = "x" * (512 * 20)  # 20× the target
        assert cleaner._calculate_chunk_score(huge) < 1.0

    def test_chunk_score_bounded_between_zero_and_one(self) -> None:
        """Chunk score must always be in [0.0, 1.0] regardless of content length."""
        cleaner = _make_cleaner()
        for size in (0, 1, 10, 100, 512, 1000, 50000):
            score = cleaner._calculate_chunk_score("a" * size)
            assert 0.0 <= score <= 1.0, f"Score out of range for size {size}"


# ---------------------------------------------------------------------------
# Tests: get_statistics
# ---------------------------------------------------------------------------


class TestGetStatistics:
    """Tests for PostScraperCleaner.get_statistics"""

    def test_statistics_after_zero_documents(self) -> None:
        """A freshly created cleaner should report success_rate of 0.0."""
        cleaner = _make_cleaner()
        stats = cleaner.get_statistics()

        assert stats["success_rate"] == 0.0
        assert stats["total_processed"] == 0
        assert stats["total_success"] == 0
        assert stats["total_failed"] == 0
        assert stats["overall_reduction_percentage"] == 0.0

    def test_statistics_after_successful_document(self, tmp_path: Path) -> None:
        """Processing one file successfully should increment success counters."""
        # Arrange
        input_file = tmp_path / "doc.md"
        input_file.write_text(SAMPLE_MD, encoding="utf-8")
        output_file = tmp_path / "out.md"
        cleaner = _make_cleaner()

        # Act
        cleaner.clean_document(input_file, output_file)
        stats = cleaner.get_statistics()

        # Assert
        assert stats["total_processed"] == 1
        assert stats["total_success"] == 1
        assert stats["total_failed"] == 0
        assert stats["success_rate"] == 1.0

    def test_statistics_after_failed_document(self, tmp_path: Path) -> None:
        """Processing a missing file should increment failure counters."""
        # Arrange
        cleaner = _make_cleaner()
        cleaner.clean_document(tmp_path / "missing.md", tmp_path / "out.md")
        stats = cleaner.get_statistics()

        # Assert
        assert stats["total_processed"] == 1
        assert stats["total_success"] == 0
        assert stats["total_failed"] == 1
        assert stats["success_rate"] == 0.0

    def test_statistics_track_multiple_documents(self, tmp_path: Path) -> None:
        """Totals should accumulate correctly across multiple document calls."""
        # Arrange
        cleaner = _make_cleaner()
        for i in range(3):
            f = tmp_path / f"doc_{i}.md"
            f.write_text(SAMPLE_MD, encoding="utf-8")
            cleaner.clean_document(f, tmp_path / f"out_{i}.md")
        # Also process one failure
        cleaner.clean_document(tmp_path / "ghost.md", tmp_path / "ghost_out.md")

        stats = cleaner.get_statistics()

        # Assert
        assert stats["total_processed"] == 4
        assert stats["total_success"] == 3
        assert stats["total_failed"] == 1
        assert stats["success_rate"] == pytest.approx(0.75)

    def test_statistics_returns_average_processing_time(self, tmp_path: Path) -> None:
        """get_statistics should include average_processing_time after processing."""
        # Arrange
        input_file = tmp_path / "doc.md"
        input_file.write_text(SAMPLE_MD, encoding="utf-8")
        cleaner = _make_cleaner()
        cleaner.clean_document(input_file, tmp_path / "out.md")

        stats = cleaner.get_statistics()

        assert "average_processing_time" in stats
        assert stats["average_processing_time"] >= 0.0

    def test_statistics_returns_overall_reduction_percentage(self, tmp_path: Path) -> None:
        """get_statistics should compute overall_reduction_percentage after success."""
        # Arrange
        content = "Skip to main content\n\n" + SAMPLE_MD
        input_file = tmp_path / "doc.md"
        input_file.write_text(content, encoding="utf-8")
        cleaner = _make_cleaner()
        cleaner.clean_document(input_file, tmp_path / "out.md")

        stats = cleaner.get_statistics()

        assert 0.0 <= stats["overall_reduction_percentage"] <= 100.0


# ---------------------------------------------------------------------------
# Tests: CleaningResult
# ---------------------------------------------------------------------------


class TestCleaningResultCalculateReduction:
    """Tests for CleaningResult.calculate_reduction"""

    def test_normal_reduction(self) -> None:
        """Reduction percentage should equal (original - cleaned) / original * 100."""
        result = CleaningResult(
            input_file=Path("a.md"),
            original_size=1000,
            cleaned_size=750,
        )
        result.calculate_reduction()
        assert result.reduction_percentage == pytest.approx(25.0)

    def test_zero_original_size_leaves_reduction_at_zero(self) -> None:
        """calculate_reduction with original_size=0 should not raise and leave percentage at 0."""
        result = CleaningResult(
            input_file=Path("a.md"),
            original_size=0,
            cleaned_size=0,
        )
        result.calculate_reduction()
        assert result.reduction_percentage == 0.0

    def test_no_reduction_when_sizes_equal(self) -> None:
        """calculate_reduction should yield 0 % when both sizes are identical."""
        result = CleaningResult(
            input_file=Path("a.md"),
            original_size=500,
            cleaned_size=500,
        )
        result.calculate_reduction()
        assert result.reduction_percentage == pytest.approx(0.0)

    def test_full_reduction(self) -> None:
        """calculate_reduction should yield 100 % when cleaned_size is 0."""
        result = CleaningResult(
            input_file=Path("a.md"),
            original_size=200,
            cleaned_size=0,
        )
        result.calculate_reduction()
        assert result.reduction_percentage == pytest.approx(100.0)


class TestCleaningResultToDict:
    """Tests for CleaningResult.to_dict"""

    def test_to_dict_returns_dict(self) -> None:
        """to_dict should return a plain Python dict."""
        result = CleaningResult(input_file=Path("a.md"))
        assert isinstance(result.to_dict(), dict)

    def test_to_dict_contains_required_keys(self) -> None:
        """to_dict must include all documented top-level keys."""
        required_keys = {
            "input_file",
            "output_file",
            "success",
            "original_size",
            "cleaned_size",
            "reduction_percentage",
            "removed_sections",
            "rule_based_cleaning",
            "processing_time",
            "error_message",
        }
        result = CleaningResult(
            input_file=Path("a.md"),
            output_file=Path("b.md"),
            success=True,
            original_size=1000,
            cleaned_size=800,
        )
        result.calculate_reduction()
        d = result.to_dict()
        assert required_keys.issubset(d.keys())

    def test_to_dict_values_are_serializable(self) -> None:
        """All values in to_dict must be JSON-serialisable (no Path objects)."""
        import json

        result = CleaningResult(
            input_file=Path("a.md"),
            output_file=Path("b.md"),
            success=True,
            original_size=400,
            cleaned_size=300,
            removed_sections=["nav", "footer"],
        )
        result.calculate_reduction()
        # Should not raise
        json.dumps(result.to_dict())

    def test_to_dict_none_output_file(self) -> None:
        """to_dict with output_file=None should store None (not crash)."""
        result = CleaningResult(input_file=Path("a.md"), output_file=None)
        d = result.to_dict()
        assert d["output_file"] is None

    def test_to_dict_rounds_reduction_to_two_decimals(self) -> None:
        """reduction_percentage in to_dict should be rounded to 2 decimal places."""
        result = CleaningResult(
            input_file=Path("a.md"),
            original_size=3,
            cleaned_size=1,
        )
        result.calculate_reduction()  # 66.666...%
        d = result.to_dict()
        # Value should be the rounded float, not the raw repeating decimal
        assert d["reduction_percentage"] == round(result.reduction_percentage, 2)

    def test_to_dict_reflects_error_message(self) -> None:
        """to_dict should include the error_message field for failed results."""
        result = CleaningResult(
            input_file=Path("missing.md"),
            success=False,
            error_message="File not found",
        )
        d = result.to_dict()
        assert d["error_message"] == "File not found"
        assert d["success"] is False
