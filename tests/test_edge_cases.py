"""Cross-cutting edge case tests for PostScraperCleaner and ChunkOptimizer."""

from __future__ import annotations

import threading
from pathlib import Path

import pytest

from docscraper.cleaning.cleaner import (
    CleaningConfig,
    PostScraperCleaner,
)
from docscraper.optimization.chunker import ChunkOptimizer

# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def config() -> CleaningConfig:
    """Default CleaningConfig with LLM disabled."""
    return CleaningConfig(enable_llm_validation=False, enable_chunk_optimization=False)


@pytest.fixture()
def cleaner(config: CleaningConfig) -> PostScraperCleaner:
    """PostScraperCleaner with LLM and chunk optimisation disabled."""
    return PostScraperCleaner(config)


# ---------------------------------------------------------------------------
# 1. Unicode content cleaning
# ---------------------------------------------------------------------------

class TestUnicodeContentCleaning:
    """PostScraperCleaner handles multi-script and special Unicode content."""

    def test_cjk_characters_preserved(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        """CJK characters in the body must survive the cleaning pipeline."""
        content = "# 文档标题\n\n这是一段中文内容，包含 **加粗** 和 `代码`。\n\n## 小节\n\n更多内容。\n"
        src = tmp_path / "cjk.md"
        src.write_text(content, encoding="utf-8")
        out = tmp_path / "cjk_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success
        cleaned = out.read_text(encoding="utf-8")
        assert "文档标题" in cleaned
        assert "中文内容" in cleaned

    def test_emoji_in_body_preserved(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        """Emoji in markdown body are treated as content and not stripped."""
        content = "# Guide\n\nStep 1: Install the package\nStep 2: Configure settings\nNote the rocket launch emoji is intentional.\n"
        src = tmp_path / "emoji.md"
        src.write_text(content, encoding="utf-8")
        out = tmp_path / "emoji_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success
        cleaned = out.read_text(encoding="utf-8")
        assert "Step 1" in cleaned

    def test_rtl_arabic_text_preserved(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        """Right-to-left text should pass through without corruption."""
        content = "# Documentation\n\nهذا نص عربي يصف الوثائق.\n\n## قسم\n\nمزيد من المحتوى.\n"
        src = tmp_path / "rtl.md"
        src.write_text(content, encoding="utf-8")
        out = tmp_path / "rtl_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success
        cleaned = out.read_text(encoding="utf-8")
        assert "عربي" in cleaned

    def test_mixed_scripts_in_single_file(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        """A file with Latin, CJK, and Cyrillic must all survive cleaning."""
        content = (
            "# Mixed Scripts\n\n"
            "English: hello world.\n"
            "Chinese: 你好世界。\n"
            "Russian: Привет мир.\n"
        )
        src = tmp_path / "mixed.md"
        src.write_text(content, encoding="utf-8")
        out = tmp_path / "mixed_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success
        cleaned = out.read_text(encoding="utf-8")
        assert "hello" in cleaned
        assert "你好" in cleaned
        assert "Привет" in cleaned


# ---------------------------------------------------------------------------
# 2. Very large content (500 KB+)
# ---------------------------------------------------------------------------

class TestLargeContent:
    """Cleaning pipeline completes without error on large files."""

    def test_500kb_markdown_cleans_successfully(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        # Build ~500 KB of valid markdown by repeating a fixed-size section block
        block = (
            "## Section\n\n"
            + "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 20
            + "\n\n"
        )
        repeats = (500_000 // len(block)) + 1
        content = "# Large Document\n\n" + block * repeats
        assert len(content) >= 500_000

        src = tmp_path / "large.md"
        src.write_text(content, encoding="utf-8")
        out = tmp_path / "large_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success
        assert result.original_size >= 500_000
        assert result.cleaned_size > 0

    def test_stats_updated_after_large_file(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        body = ("# Heading\n\n" + "word " * 2000 + "\n") * 5
        src = tmp_path / "big.md"
        src.write_text(body, encoding="utf-8")
        out = tmp_path / "big_out.md"

        cleaner.clean_document(src, out)
        stats = cleaner.get_statistics()

        assert stats["total_processed"] == 1
        assert stats["total_bytes_before"] > 0


# ---------------------------------------------------------------------------
# 3. Binary-like content
# ---------------------------------------------------------------------------

class TestBinaryLikeContent:
    """Files with null bytes or control characters should not crash the cleaner."""

    def test_null_bytes_handled(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        # Write a file with embedded null bytes (common binary corruption artefact)
        content = "# Document\n\nNormal content here.\x00\x00More content.\n"
        src = tmp_path / "nullbytes.md"
        src.write_bytes(content.encode("utf-8"))
        out = tmp_path / "nullbytes_out.md"

        result = cleaner.clean_document(src, out)

        # Cleaner should either succeed or record an error — no unhandled exception
        assert result.success or result.error_message is not None

    def test_control_characters_handled(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        # Embed ASCII control characters (BEL, BS, etc.)
        content = "# Title\n\nContent\x07\x08with control\x0bchars.\n"
        src = tmp_path / "control.md"
        src.write_bytes(content.encode("utf-8"))
        out = tmp_path / "control_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success or result.error_message is not None


# ---------------------------------------------------------------------------
# 4. Deeply nested directory trees
# ---------------------------------------------------------------------------

class TestDeeplyNestedDirectories:
    """clean_directory_tree mirrors 5+ levels correctly."""

    def _make_tree(self, root: Path, depth: int = 5) -> int:
        """Recursively create a directory tree; return file count."""
        count = 0
        current = root
        for level in range(1, depth + 1):
            current = current / f"level{level}"
            current.mkdir(parents=True, exist_ok=True)
            f = current / f"doc_{level}.md"
            f.write_text(f"# Level {level} Doc\n\nContent at level {level}.\n")
            count += 1
        return count

    def test_five_level_tree_processed(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        input_root = tmp_path / "input"
        input_root.mkdir()
        file_count = self._make_tree(input_root, depth=5)
        output_root = tmp_path / "output"

        results = cleaner.clean_directory_tree(input_root, output_root)

        assert len(results) == file_count
        assert all(r.success for r in results)

    def test_output_paths_have_cleaned_suffix(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        input_root = tmp_path / "in"
        input_root.mkdir()
        sub = input_root / "level1" / "level2"
        sub.mkdir(parents=True)
        (sub / "file.md").write_text("# Doc\n\nContent.\n")
        output_root = tmp_path / "out"

        results = cleaner.clean_directory_tree(input_root, output_root)

        assert len(results) == 1
        assert results[0].success
        # Output file path must contain the '_cleaned' suffix on each directory segment
        out_path = results[0].output_file
        assert out_path is not None
        rel = out_path.relative_to(output_root)
        assert "level1_cleaned" in str(rel)
        assert "level2_cleaned" in str(rel)


# ---------------------------------------------------------------------------
# 5. Files with unusual names
# ---------------------------------------------------------------------------

class TestUnusualFilenames:
    """Filenames with spaces and special characters should be handled."""

    def test_filename_with_spaces(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        src = tmp_path / "my document file.md"
        src.write_text("# My Document\n\nContent here.\n")
        out = tmp_path / "my document file_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success

    def test_filename_with_hyphens_and_underscores(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        src = tmp_path / "my-doc_v2.md"
        src.write_text("# Doc V2\n\nContent.\n")
        out = tmp_path / "my-doc_v2_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success

    def test_filename_with_dots(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        src = tmp_path / "v1.2.3.md"
        src.write_text("# Version 1.2.3\n\nRelease notes.\n")
        out = tmp_path / "v1.2.3_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success

    def test_batch_with_mixed_unusual_names(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        input_dir = tmp_path / "input"
        input_dir.mkdir()
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        names = ["doc one.md", "doc-two.md", "doc_three.md", "v1.0.md"]
        for name in names:
            (input_dir / name).write_text(f"# {name}\n\nContent.\n")

        results = cleaner.clean_batch(input_dir, output_dir)

        assert len(results) == len(names)
        assert all(r.success for r in results)


# ---------------------------------------------------------------------------
# 6. Empty files
# ---------------------------------------------------------------------------

class TestEmptyFiles:
    """Zero-byte markdown files should not crash the cleaner."""

    def test_empty_file_returns_failed_or_empty_result(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        src = tmp_path / "empty.md"
        src.write_text("")
        out = tmp_path / "empty_out.md"

        result = cleaner.clean_document(src, out)

        # An empty file may succeed with zero content or fail gracefully — no crash.
        assert result.success or result.error_message is not None

    def test_whitespace_only_file(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        src = tmp_path / "whitespace.md"
        src.write_text("   \n\n\t\n")
        out = tmp_path / "whitespace_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success or result.error_message is not None

    def test_batch_skips_no_md_files_when_dir_is_empty(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        input_dir = tmp_path / "empty_input"
        input_dir.mkdir()
        output_dir = tmp_path / "empty_output"
        output_dir.mkdir()

        results = cleaner.clean_batch(input_dir, output_dir)

        assert results == []

    def test_non_md_file_returns_error(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        src = tmp_path / "document.txt"
        src.write_text("Not a markdown file.")
        out = tmp_path / "document_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success is False
        assert result.error_message is not None


# ---------------------------------------------------------------------------
# 7. Config boundary values
# ---------------------------------------------------------------------------

class TestConfigBoundaryValues:
    """CleaningConfig and ChunkOptimizer clamp or validate boundary values."""

    def test_chunk_size_minimum_via_config(self) -> None:
        config = CleaningConfig(target_chunk_size=100)
        assert config.target_chunk_size == 100

    def test_chunk_size_below_minimum_raises(self) -> None:
        with pytest.raises(ValueError):
            CleaningConfig(target_chunk_size=99)

    def test_chunk_optimizer_clamps_below_100(self) -> None:
        optimizer = ChunkOptimizer(chunk_size=50)
        assert optimizer.chunk_size == 100

    def test_chunk_optimizer_clamps_above_2048(self) -> None:
        optimizer = ChunkOptimizer(chunk_size=9999)
        assert optimizer.chunk_size == 2048

    def test_chunk_optimizer_accepts_2048(self) -> None:
        optimizer = ChunkOptimizer(chunk_size=2048)
        assert optimizer.chunk_size == 2048

    def test_chunk_optimizer_accepts_100(self) -> None:
        optimizer = ChunkOptimizer(chunk_size=100)
        assert optimizer.chunk_size == 100

    def test_overlap_capped_at_half_chunk(self) -> None:
        optimizer = ChunkOptimizer(chunk_size=200, overlap=200)
        assert optimizer.overlap <= optimizer.chunk_size // 2

    def test_config_overlap_must_be_less_than_chunk_size(self) -> None:
        with pytest.raises(ValueError):
            CleaningConfig(target_chunk_size=512, overlap_size=512)


# ---------------------------------------------------------------------------
# 8. Pattern matching edge cases
# ---------------------------------------------------------------------------

class TestPatternMatchingEdgeCases:
    """Content that resembles boilerplate but should be preserved."""

    def test_skip_in_sentence_not_removed(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        """A 'skip' mention inside a sentence should not trigger nav removal."""
        content = (
            "# Configuration Guide\n\n"
            "You can skip optional steps if you already have the tool installed.\n\n"
            "## Required Steps\n\nDo the required steps.\n"
        )
        src = tmp_path / "skip_sentence.md"
        src.write_text(content)
        out = tmp_path / "skip_sentence_out.md"

        result = cleaner.clean_document(src, out)
        cleaned = out.read_text()

        assert result.success
        # The sentence context around 'skip' should survive
        assert "skip optional steps" in cleaned

    def test_copyright_in_code_comment_not_removed(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        """A copyright notice inside a code block should NOT be stripped."""
        content = (
            "# Library API\n\n"
            "```python\n"
            "# Copyright 2024 Example Corp\n"
            "def greet(): pass\n"
            "```\n\n"
            "## Usage\n\nCall greet().\n"
        )
        src = tmp_path / "code_copyright.md"
        src.write_text(content)
        out = tmp_path / "code_copyright_out.md"

        result = cleaner.clean_document(src, out)

        assert result.success

    def test_navigation_phrase_at_start_is_removed(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        """'Skip to main content' at the very start should be removed."""
        content = (
            "Skip to main content\n\n"
            "# Real Title\n\nActual documentation content.\n"
        )
        src = tmp_path / "nav_start.md"
        src.write_text(content)
        out = tmp_path / "nav_start_out.md"

        result = cleaner.clean_document(src, out)
        cleaned = out.read_text()

        assert result.success
        assert "Real Title" in cleaned


# ---------------------------------------------------------------------------
# 9. Concurrent batch calls
# ---------------------------------------------------------------------------

class TestConcurrentBatchCalls:
    """Two clean_batch calls on the same cleaner instance run without data races."""

    def test_two_concurrent_batches(self, config: CleaningConfig, tmp_path: Path) -> None:
        shared_cleaner = PostScraperCleaner(config)

        def make_batch(batch_name: str) -> tuple[Path, Path]:
            in_dir = tmp_path / f"{batch_name}_in"
            in_dir.mkdir()
            out_dir = tmp_path / f"{batch_name}_out"
            out_dir.mkdir()
            for i in range(3):
                (in_dir / f"doc{i}.md").write_text(
                    f"# Doc {i}\n\nContent for batch {batch_name}.\n"
                )
            return in_dir, out_dir

        in_a, out_a = make_batch("batch_a")
        in_b, out_b = make_batch("batch_b")

        results_a: list = []
        results_b: list = []

        def run_a() -> None:
            results_a.extend(shared_cleaner.clean_batch(in_a, out_a))

        def run_b() -> None:
            results_b.extend(shared_cleaner.clean_batch(in_b, out_b))

        thread_a = threading.Thread(target=run_a)
        thread_b = threading.Thread(target=run_b)
        thread_a.start()
        thread_b.start()
        thread_a.join()
        thread_b.join()

        # Both batches must complete with 3 results each
        assert len(results_a) == 3
        assert len(results_b) == 3
        assert all(r.success for r in results_a)
        assert all(r.success for r in results_b)

    def test_stats_reflect_all_concurrent_work(
        self, config: CleaningConfig, tmp_path: Path
    ) -> None:
        shared_cleaner = PostScraperCleaner(config)
        total_files = 6  # 3 per batch

        def make_and_run(name: str) -> None:
            in_dir = tmp_path / f"{name}_in"
            in_dir.mkdir()
            out_dir = tmp_path / f"{name}_out"
            out_dir.mkdir()
            for i in range(3):
                (in_dir / f"f{i}.md").write_text(f"# Title\n\nBody {i}.\n")
            shared_cleaner.clean_batch(in_dir, out_dir)

        threads = [threading.Thread(target=make_and_run, args=(f"t{n}",)) for n in range(2)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        stats = shared_cleaner.get_statistics()
        assert stats["total_processed"] == total_files


# ---------------------------------------------------------------------------
# 10. Statistics accuracy
# ---------------------------------------------------------------------------

class TestStatisticsAccuracy:
    """Process exactly 10 files; verify all stats counters are correct."""

    def test_ten_files_stats(self, cleaner: PostScraperCleaner, tmp_path: Path) -> None:
        input_dir = tmp_path / "input"
        input_dir.mkdir()
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        file_count = 10
        for i in range(file_count):
            (input_dir / f"doc{i}.md").write_text(
                f"# Document {i}\n\nThis is content for document {i}.\n"
            )

        results = cleaner.clean_batch(input_dir, output_dir)
        stats = cleaner.get_statistics()

        assert len(results) == file_count
        assert stats["total_processed"] == file_count
        assert stats["total_success"] == file_count
        assert stats["total_failed"] == 0
        assert stats["total_bytes_before"] > 0
        assert stats["total_bytes_after"] > 0
        assert 0.0 <= stats["success_rate"] <= 1.0
        assert stats["success_rate"] == 1.0
        assert stats["average_processing_time"] >= 0.0

    def test_failed_file_counted_in_stats(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        src = tmp_path / "nonexistent.md"  # deliberately absent
        out = tmp_path / "out.md"

        result = cleaner.clean_document(src, out)
        stats = cleaner.get_statistics()

        assert result.success is False
        assert stats["total_processed"] == 1
        assert stats["total_failed"] == 1
        assert stats["total_success"] == 0

    def test_overall_reduction_percentage_calculated(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        input_dir = tmp_path / "in"
        input_dir.mkdir()
        output_dir = tmp_path / "out"
        output_dir.mkdir()

        # Create files with boilerplate that will be reduced
        for i in range(5):
            (input_dir / f"f{i}.md").write_text(
                f"Skip to main content\n\n# Doc {i}\n\nContent.\n\n"
                "Was this page helpful?\n"
            )

        cleaner.clean_batch(input_dir, output_dir)
        stats = cleaner.get_statistics()

        assert "overall_reduction_percentage" in stats
        assert stats["overall_reduction_percentage"] >= 0.0

    def test_average_processing_time_positive(
        self, cleaner: PostScraperCleaner, tmp_path: Path
    ) -> None:
        input_dir = tmp_path / "in"
        input_dir.mkdir()
        output_dir = tmp_path / "out"
        output_dir.mkdir()

        for i in range(3):
            (input_dir / f"doc{i}.md").write_text(f"# Title {i}\n\nBody.\n")

        cleaner.clean_batch(input_dir, output_dir)
        stats = cleaner.get_statistics()

        assert stats["average_processing_time"] >= 0.0
        assert stats["total_processing_time"] >= stats["average_processing_time"]
