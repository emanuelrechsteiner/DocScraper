"""
Unit Tests for ChunkOptimizer and ChunkMetadata

Tests for the chunk optimization module used to prepare content for
vector database ingestion. Covers initialization, chunking logic,
semantic boundary detection, token estimation, and metadata handling.
"""

import pytest
from docscraper.optimization.chunker import ChunkOptimizer, ChunkMetadata


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def optimizer() -> ChunkOptimizer:
    """Default ChunkOptimizer with standard settings."""
    return ChunkOptimizer()


@pytest.fixture
def small_optimizer() -> ChunkOptimizer:
    """ChunkOptimizer with a small chunk size for easier boundary testing."""
    return ChunkOptimizer(chunk_size=150, overlap=20)


@pytest.fixture
def no_overlap_optimizer() -> ChunkOptimizer:
    """ChunkOptimizer with overlap disabled."""
    return ChunkOptimizer(chunk_size=200, overlap=0)


@pytest.fixture
def content_with_headings() -> str:
    return (
        "# Introduction\n\n"
        "This is the introduction section.\n\n"
        "## Background\n\n"
        "Some background information.\n\n"
        "### Details\n\n"
        "More detailed information here.\n\n"
        "## Summary\n\n"
        "Final summary content.\n"
    )


@pytest.fixture
def content_with_code_blocks() -> str:
    return (
        "# API Reference\n\n"
        "Use the following snippet to get started:\n\n"
        "```python\n"
        "from mylib import Client\n"
        "client = Client(api_key='secret')\n"
        "result = client.fetch()\n"
        "```\n\n"
        "Another example in bash:\n\n"
        "```bash\n"
        "pip install mylib\n"
        "```\n"
    )


@pytest.fixture
def content_with_tables() -> str:
    return (
        "# Configuration Options\n\n"
        "| Parameter | Type | Default | Description |\n"
        "| --------- | ---- | ------- | ----------- |\n"
        "| timeout   | int  | 30      | Request timeout in seconds |\n"
        "| retries   | int  | 3       | Number of retry attempts |\n"
        "| verbose   | bool | False   | Enable verbose logging |\n\n"
        "Use these settings wisely.\n"
    )


@pytest.fixture
def content_with_lists() -> str:
    return (
        "# Steps\n\n"
        "- Install the package\n"
        "- Configure credentials\n"
        "- Run the application\n\n"
        "* Another unordered item\n"
        "+ Yet another item\n"
    )


@pytest.fixture
def mixed_content() -> str:
    return (
        "# Getting Started\n\n"
        "Welcome to the documentation.\n\n"
        "## Installation\n\n"
        "```bash\n"
        "pip install mylib\n"
        "```\n\n"
        "## Configuration\n\n"
        "| Option | Default |\n"
        "| ------ | ------- |\n"
        "| debug  | False   |\n\n"
        "## Usage\n\n"
        "- Step one\n"
        "- Step two\n"
        "- Step three\n"
    )


# ---------------------------------------------------------------------------
# TestChunkMetadata
# ---------------------------------------------------------------------------


class TestChunkMetadata:
    """Test the ChunkMetadata dataclass."""

    def test_default_field_values(self):
        """ChunkMetadata is created with sensible zero defaults."""
        meta = ChunkMetadata()
        assert meta.total_chunks == 0
        assert meta.heading_levels == {}
        assert meta.code_blocks == 0
        assert meta.tables == 0
        assert meta.lists == 0
        assert meta.semantic_boundaries == []
        assert meta.avg_chunk_size == 0
        assert meta.optimization_notes == []

    def test_custom_field_values(self):
        """ChunkMetadata stores user-supplied field values correctly."""
        meta = ChunkMetadata(
            total_chunks=5,
            heading_levels={1: 1, 2: 3},
            code_blocks=2,
            tables=1,
            lists=4,
            semantic_boundaries=[0, 100, 200],
            avg_chunk_size=128,
            optimization_notes=["note A", "note B"],
        )
        assert meta.total_chunks == 5
        assert meta.heading_levels == {1: 1, 2: 3}
        assert meta.code_blocks == 2
        assert meta.tables == 1
        assert meta.lists == 4
        assert meta.semantic_boundaries == [0, 100, 200]
        assert meta.avg_chunk_size == 128
        assert meta.optimization_notes == ["note A", "note B"]

    def test_to_dict_keys(self):
        """to_dict returns a dict with all expected top-level keys."""
        meta = ChunkMetadata()
        result = meta.to_dict()

        expected_keys = {
            "total_chunks",
            "heading_levels",
            "code_blocks",
            "tables",
            "lists",
            "avg_chunk_size",
            "optimization_notes",
        }
        assert set(result.keys()) == expected_keys

    def test_to_dict_values_match(self):
        """to_dict serializes field values without modification."""
        meta = ChunkMetadata(
            total_chunks=3,
            heading_levels={2: 4},
            code_blocks=1,
            tables=2,
            lists=5,
            avg_chunk_size=256,
            optimization_notes=["Normalized 1 heading levels"],
        )
        result = meta.to_dict()

        assert result["total_chunks"] == 3
        assert result["heading_levels"] == {2: 4}
        assert result["code_blocks"] == 1
        assert result["tables"] == 2
        assert result["lists"] == 5
        assert result["avg_chunk_size"] == 256
        assert result["optimization_notes"] == ["Normalized 1 heading levels"]

    def test_to_dict_omits_semantic_boundaries(self):
        """semantic_boundaries is intentionally excluded from to_dict output."""
        meta = ChunkMetadata(semantic_boundaries=[0, 50])
        result = meta.to_dict()
        assert "semantic_boundaries" not in result

    def test_mutable_defaults_are_independent(self):
        """Each ChunkMetadata instance has its own mutable containers."""
        meta1 = ChunkMetadata()
        meta2 = ChunkMetadata()
        meta1.optimization_notes.append("only in meta1")
        assert meta2.optimization_notes == []


# ---------------------------------------------------------------------------
# TestChunkOptimizerInit
# ---------------------------------------------------------------------------


class TestChunkOptimizerInit:
    """Test ChunkOptimizer.__init__ with default and custom parameters."""

    def test_default_initialization(self):
        """Default chunk_size and overlap are applied correctly."""
        opt = ChunkOptimizer()
        assert opt.chunk_size == ChunkOptimizer.DEFAULT_CHUNK_SIZE  # 512
        assert opt.overlap == ChunkOptimizer.DEFAULT_OVERLAP  # 50
        assert opt.preserve_structure is True

    def test_custom_valid_parameters(self):
        """Custom chunk_size and overlap within bounds are stored as-is."""
        opt = ChunkOptimizer(chunk_size=1024, overlap=100, preserve_structure=False)
        assert opt.chunk_size == 1024
        assert opt.overlap == 100
        assert opt.preserve_structure is False

    def test_chunk_size_clamped_below_minimum(self):
        """chunk_size below 100 is clamped to 100."""
        opt = ChunkOptimizer(chunk_size=10)
        assert opt.chunk_size == 100

    def test_chunk_size_clamped_above_maximum(self):
        """chunk_size above 2048 is clamped to 2048."""
        opt = ChunkOptimizer(chunk_size=9999)
        assert opt.chunk_size == 2048

    def test_chunk_size_at_minimum_boundary(self):
        """chunk_size exactly at 100 is accepted unchanged."""
        opt = ChunkOptimizer(chunk_size=100)
        assert opt.chunk_size == 100

    def test_chunk_size_at_maximum_boundary(self):
        """chunk_size exactly at 2048 is accepted unchanged."""
        opt = ChunkOptimizer(chunk_size=2048)
        assert opt.chunk_size == 2048

    def test_overlap_clamped_to_half_chunk_size(self):
        """overlap exceeding chunk_size // 2 is clamped."""
        opt = ChunkOptimizer(chunk_size=200, overlap=200)
        assert opt.overlap <= 200 // 2  # 100

    def test_overlap_zero_is_valid(self):
        """overlap of 0 disables overlapping."""
        opt = ChunkOptimizer(chunk_size=512, overlap=0)
        assert opt.overlap == 0

    def test_negative_overlap_clamped_to_zero_or_less(self):
        """Negative overlap is allowed by min() — stays as provided (negative)."""
        opt = ChunkOptimizer(chunk_size=512, overlap=-10)
        # min(-10, 512 // 2) == -10; the implementation does not enforce >= 0
        assert opt.overlap == -10


# ---------------------------------------------------------------------------
# TestTokenEstimation
# ---------------------------------------------------------------------------


class TestTokenEstimation:
    """Test _estimate_tokens and estimate_total_tokens."""

    def test_empty_string_returns_one(self, optimizer):
        """Empty string returns minimum of 1 token."""
        assert optimizer._estimate_tokens("") == 1

    def test_single_char_returns_one(self, optimizer):
        """Single character rounds to 1 token."""
        assert optimizer._estimate_tokens("a") == 1

    def test_four_chars_equals_one_token(self, optimizer):
        """Exactly 4 characters should estimate to 1 token."""
        assert optimizer._estimate_tokens("abcd") == 1

    def test_eight_chars_equals_two_tokens(self, optimizer):
        """8 characters should estimate to 2 tokens."""
        assert optimizer._estimate_tokens("abcdefgh") == 2

    def test_hundred_chars_estimates_correctly(self, optimizer):
        """100 characters should estimate to 25 tokens."""
        text = "a" * 100
        assert optimizer._estimate_tokens(text) == 25

    def test_estimate_total_tokens_delegates_correctly(self, optimizer):
        """estimate_total_tokens returns same result as _estimate_tokens."""
        text = "Hello, world! This is a test sentence."
        assert optimizer.estimate_total_tokens(text) == optimizer._estimate_tokens(text)

    def test_whitespace_only_string(self, optimizer):
        """Whitespace-only string still produces a valid estimate."""
        result = optimizer._estimate_tokens("   ")
        assert result >= 1


# ---------------------------------------------------------------------------
# TestGetChunkInfo
# ---------------------------------------------------------------------------


class TestGetChunkInfo:
    """Test get_chunk_info with various inputs."""

    def test_empty_list(self, optimizer):
        """Empty chunk list returns zeroed stats dict."""
        info = optimizer.get_chunk_info([])
        assert info == {"total_chunks": 0, "avg_size": 0, "min_size": 0, "max_size": 0}

    def test_single_chunk(self, optimizer):
        """Single-element list returns consistent min/max/avg."""
        chunks = ["Hello world, this is exactly one chunk."]
        info = optimizer.get_chunk_info(chunks)
        assert info["total_chunks"] == 1
        assert info["min_size"] == info["max_size"] == info["avg_size"]

    def test_multiple_chunks_stats(self, optimizer):
        """Multiple chunks produce accurate aggregate statistics."""
        chunks = [
            "a" * 400,   # 100 tokens
            "b" * 800,   # 200 tokens
            "c" * 200,   # 50 tokens
        ]
        info = optimizer.get_chunk_info(chunks)
        assert info["total_chunks"] == 3
        assert info["min_size"] == 50
        assert info["max_size"] == 200
        assert info["total_tokens"] == 350
        assert info["avg_size"] == 350 // 3

    def test_chunk_info_contains_total_tokens_key(self, optimizer):
        """Populated list result includes a total_tokens key."""
        info = optimizer.get_chunk_info(["some content"])
        assert "total_tokens" in info


# ---------------------------------------------------------------------------
# TestSplitIntoChunks
# ---------------------------------------------------------------------------


class TestSplitIntoChunks:
    """Test split_into_chunks behavior."""

    def test_empty_string_returns_empty_list(self, optimizer):
        """Empty content produces an empty chunk list."""
        assert optimizer.split_into_chunks("") == []

    def test_whitespace_only_returns_empty_list(self, optimizer):
        """Whitespace-only content produces an empty chunk list."""
        assert optimizer.split_into_chunks("   \n\n   ") == []

    def test_short_content_is_single_chunk(self, optimizer):
        """Content shorter than chunk_size stays in one chunk."""
        content = "Short content.\n"
        chunks = optimizer.split_into_chunks(content)
        assert len(chunks) == 1
        assert chunks[0].strip() == content.strip()

    def test_long_content_produces_multiple_chunks(self, small_optimizer):
        """Content much larger than chunk_size is split into multiple chunks."""
        # ~600 tokens worth of text with 4-char tokens @ chunk_size=150
        content = ("word " * 200 + "\n") * 3  # ~750 lines-worth
        chunks = small_optimizer.split_into_chunks(content)
        assert len(chunks) > 1

    def test_no_overlap_chunks_are_contiguous(self, no_overlap_optimizer):
        """With overlap=0 all content is present across chunks without duplication."""
        # Build known content: lines of 5 chars each (≈1 token)
        lines = [f"line{i:03d}" for i in range(100)]
        content = "\n".join(lines)
        chunks = no_overlap_optimizer.split_into_chunks(content)

        # Reassemble and check all lines appear
        all_text = "\n".join(chunks)
        for line in lines:
            assert line in all_text

    def test_overlap_lines_appear_in_adjacent_chunks(self):
        """With overlap enabled, tail of chunk N appears at head of chunk N+1."""
        # Use a tiny chunk size so overlap is visible quickly
        opt = ChunkOptimizer(chunk_size=100, overlap=20)
        # Create content long enough to force at least 2 chunks
        content = ("This is a sentence that takes up tokens.\n") * 30
        chunks = opt.split_into_chunks(content)
        if len(chunks) < 2:
            pytest.skip("Content too short to produce multiple chunks at this size")

        # Last lines of chunk 0 should appear somewhere in chunk 1
        tail_lines = chunks[0].split("\n")[-3:]
        for line in tail_lines:
            if line.strip():
                assert line in chunks[1], (
                    f"Overlap line '{line}' not found in second chunk"
                )

    def test_chunks_are_stripped_strings(self, small_optimizer):
        """All returned chunks are stripped of leading/trailing whitespace."""
        content = "\n\n" + ("word " * 50 + "\n") * 5 + "\n\n"
        chunks = small_optimizer.split_into_chunks(content)
        for chunk in chunks:
            assert chunk == chunk.strip()

    def test_zero_overlap_produces_multiple_chunks_and_exercises_no_overlap_branch(self):
        """With overlap=0, the zero-overlap branch is executed when a chunk boundary
        is crossed, meaning the new chunk begins with the current line only."""
        # chunk_size=100 tokens => ~400 chars; each distinct line is ~20 tokens
        opt = ChunkOptimizer(chunk_size=100, overlap=0)
        # Use distinct lines so we can track boundaries
        lines = [f"sentence_{i:03d} " + "word " * 15 for i in range(30)]
        content = "\n".join(lines)
        chunks = opt.split_into_chunks(content)
        # Multiple chunks must have been produced for the branch to be reached
        assert len(chunks) > 1
        # Total lines across all chunks should equal input lines (no duplication)
        all_lines_in_chunks = []
        for chunk in chunks:
            all_lines_in_chunks.extend([l for l in chunk.split("\n") if l.strip()])
        unique_lines = set(all_lines_in_chunks)
        # With no overlap, every line appears exactly once
        assert len(all_lines_in_chunks) == len(unique_lines)


# ---------------------------------------------------------------------------
# TestNormalizeHeadings
# ---------------------------------------------------------------------------


class TestNormalizeHeadings:
    """Test _normalize_headings heading counting and hierarchy adjustment."""

    def test_no_headings_returns_empty_dict(self, optimizer):
        """Plain paragraph content yields an empty heading_levels dict."""
        content = "This is plain text without any headings."
        _, heading_stats = optimizer._normalize_headings(content)
        assert heading_stats == {}

    def test_counts_each_level(self, optimizer, content_with_headings):
        """Heading counts per level are tallied correctly."""
        _, heading_stats = optimizer._normalize_headings(content_with_headings)
        assert heading_stats.get(1, 0) == 1  # one H1
        assert heading_stats.get(2, 0) == 2  # two H2
        assert heading_stats.get(3, 0) == 1  # one H3

    def test_minimum_heading_level_pruned(self, optimizer):
        """Heading levels below the minimum present are removed from stats."""
        content = "## Section\n\n### Subsection\n"
        _, heading_stats = optimizer._normalize_headings(content)
        # There is no H1; level 1 should be absent
        assert 1 not in heading_stats

    def test_only_counts_used_levels(self, optimizer):
        """Only heading levels that actually appear have entries."""
        content = "# H1\n\n### H3\n"
        _, heading_stats = optimizer._normalize_headings(content)
        assert 1 in heading_stats
        assert 3 in heading_stats
        assert 2 not in heading_stats

    def test_content_is_returned_unchanged(self, optimizer):
        """The normalized content string is identical to the input."""
        content = "# Title\n\n## Sub\n\nParagraph text.\n"
        normalized, _ = optimizer._normalize_headings(content)
        assert normalized == content


# ---------------------------------------------------------------------------
# TestMarkSemanticBoundaries
# ---------------------------------------------------------------------------


class TestMarkSemanticBoundaries:
    """Test _mark_semantic_boundaries detection logic."""

    def test_no_boundaries_for_plain_text(self, optimizer):
        """Plain paragraph without headings/code/tables yields no boundaries."""
        content = "Just plain text.\nAnother line.\nThird line.\n"
        _, boundaries = optimizer._mark_semantic_boundaries(content, preserve_structure=True)
        assert boundaries == []

    def test_h1_creates_boundary(self, optimizer):
        """An H1 heading line inserts a semantic boundary."""
        content = "# My Title\n\nBody text.\n"
        _, boundaries = optimizer._mark_semantic_boundaries(content, preserve_structure=True)
        assert len(boundaries) >= 1
        assert 0 in boundaries  # H1 is at position 0

    def test_h2_creates_boundary(self, optimizer):
        """An H2 heading line inserts a semantic boundary."""
        content = "Intro text.\n\n## Section\n\nBody.\n"
        _, boundaries = optimizer._mark_semantic_boundaries(content, preserve_structure=True)
        assert len(boundaries) >= 1

    def test_h3_does_not_create_boundary(self, optimizer):
        """H3 and deeper headings do NOT generate semantic boundaries."""
        content = "### Subsection\n\nContent.\n"
        _, boundaries = optimizer._mark_semantic_boundaries(content, preserve_structure=True)
        assert boundaries == []

    def test_code_block_start_creates_boundary(self, optimizer):
        """A ``` delimiter line creates a boundary."""
        content = "Intro.\n\n```python\ncode()\n```\n\nOutro.\n"
        _, boundaries = optimizer._mark_semantic_boundaries(content, preserve_structure=True)
        assert len(boundaries) >= 1

    def test_table_row_creates_boundary(self, optimizer, content_with_tables):
        """Table rows create boundaries."""
        _, boundaries = optimizer._mark_semantic_boundaries(
            content_with_tables, preserve_structure=True
        )
        assert len(boundaries) >= 1

    def test_double_blank_lines_create_boundary(self, optimizer):
        """Two consecutive blank lines are treated as a paragraph boundary."""
        content = "Para 1.\n\n\nPara 2.\n"
        _, boundaries = optimizer._mark_semantic_boundaries(content, preserve_structure=True)
        assert len(boundaries) >= 1

    def test_boundaries_are_sorted(self, optimizer, mixed_content):
        """The returned boundary list is sorted in ascending order."""
        _, boundaries = optimizer._mark_semantic_boundaries(mixed_content, preserve_structure=True)
        assert boundaries == sorted(boundaries)

    def test_boundaries_are_unique(self, optimizer, mixed_content):
        """The returned boundary list contains no duplicate positions."""
        _, boundaries = optimizer._mark_semantic_boundaries(mixed_content, preserve_structure=True)
        assert len(boundaries) == len(set(boundaries))

    def test_content_unchanged(self, optimizer):
        """The content string is returned identical to the input."""
        content = "# Header\n\nSome text.\n"
        returned_content, _ = optimizer._mark_semantic_boundaries(content, True)
        assert returned_content == content


# ---------------------------------------------------------------------------
# TestGetOverlapLines
# ---------------------------------------------------------------------------


class TestGetOverlapLines:
    """Test _get_overlap_lines extraction."""

    def test_returns_string(self, optimizer):
        """_get_overlap_lines always returns a string."""
        result = optimizer._get_overlap_lines("line one\nline two\n")
        assert isinstance(result, str)

    def test_empty_content_returns_empty(self, optimizer):
        """Empty input returns empty string."""
        result = optimizer._get_overlap_lines("")
        assert result == ""

    def test_overlap_respects_max_tokens(self, optimizer):
        """Extracted overlap does not exceed the specified max_tokens budget."""
        content = "word " * 200  # many lines of tokens
        result = optimizer._get_overlap_lines(content, max_tokens=10)
        estimated = optimizer._estimate_tokens(result)
        assert estimated <= 10

    def test_uses_default_overlap_when_none(self, optimizer):
        """When max_tokens is None, the instance overlap attribute is used.

        Build lines that are each ~16 tokens long (64 chars) so that only a
        small number of them fit within the default overlap budget (50 tokens).
        The returned result must therefore be shorter than the full input.
        """
        # Each line is 64 chars => ~16 tokens; default overlap is 50 tokens
        lines = [f"{'word' * 16}_{i}" for i in range(20)]
        content = "\n".join(lines)
        result = optimizer._get_overlap_lines(content)
        # Only a handful of lines should fit; result must be a true sub-set
        assert len(result) < len(content)
        assert len(result) > 0


# ---------------------------------------------------------------------------
# TestOptimize
# ---------------------------------------------------------------------------


class TestOptimize:
    """Test the top-level optimize pipeline method."""

    def test_empty_content_returns_early(self, optimizer):
        """Empty input returns empty string and a metadata note."""
        content, meta = optimizer.optimize("")
        assert content == ""
        assert isinstance(meta, ChunkMetadata)
        assert any("Empty" in note for note in meta.optimization_notes)

    def test_whitespace_only_returns_early(self, optimizer):
        """Whitespace-only input is treated as empty."""
        content, meta = optimizer.optimize("   \n\n   ")
        assert content == ""
        assert any("Empty" in note for note in meta.optimization_notes)

    def test_returns_tuple(self, optimizer, content_with_headings):
        """optimize returns a 2-tuple of (str, ChunkMetadata)."""
        result = optimizer.optimize(content_with_headings)
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], str)
        assert isinstance(result[1], ChunkMetadata)

    def test_heading_levels_populated(self, optimizer, content_with_headings):
        """heading_levels metadata is filled from the content."""
        _, meta = optimizer.optimize(content_with_headings)
        assert len(meta.heading_levels) > 0

    def test_code_blocks_counted(self, optimizer, content_with_code_blocks):
        """code_blocks count reflects actual ``` delimiters in content."""
        _, meta = optimizer.optimize(content_with_code_blocks)
        assert meta.code_blocks == 2

    def test_tables_counted(self, optimizer, content_with_tables):
        """tables count reflects actual | rows in content."""
        _, meta = optimizer.optimize(content_with_tables)
        assert meta.tables >= 4  # header + separator + 3 data rows

    def test_lists_counted(self, optimizer, content_with_lists):
        """lists count reflects actual list items in content."""
        _, meta = optimizer.optimize(content_with_lists)
        assert meta.lists >= 3

    def test_total_chunks_greater_than_zero(self, optimizer, content_with_headings):
        """total_chunks is at least 1 for non-empty content."""
        _, meta = optimizer.optimize(content_with_headings)
        assert meta.total_chunks >= 1

    def test_avg_chunk_size_greater_than_zero(self, optimizer, content_with_headings):
        """avg_chunk_size is a positive integer for non-empty content."""
        _, meta = optimizer.optimize(content_with_headings)
        assert meta.avg_chunk_size > 0

    def test_optimization_notes_present(self, optimizer, content_with_headings):
        """optimization_notes list has at least one entry."""
        _, meta = optimizer.optimize(content_with_headings)
        assert len(meta.optimization_notes) >= 1

    def test_semantic_boundaries_populated(self, optimizer, content_with_headings):
        """semantic_boundaries is filled when headings are present."""
        _, meta = optimizer.optimize(content_with_headings)
        assert len(meta.semantic_boundaries) >= 1

    def test_plain_content_no_structure(self, optimizer):
        """Plain paragraph without any markdown structure is processed without error."""
        content = "This is just plain text. No headings, no code, no tables, no lists.\n"
        optimized, meta = optimizer.optimize(content)
        assert optimized.strip() == content.strip()
        assert meta.code_blocks == 0
        assert meta.tables == 0

    def test_mixed_content_pipeline(self, optimizer, mixed_content):
        """Mixed content (headings + code + tables + lists) processes cleanly."""
        optimized, meta = optimizer.optimize(mixed_content)
        assert len(optimized) > 0
        assert meta.code_blocks >= 1
        assert meta.tables >= 1
        assert meta.lists >= 1
        assert meta.heading_levels


# ---------------------------------------------------------------------------
# TestLargeContent
# ---------------------------------------------------------------------------


class TestLargeContent:
    """Test behavior with very large content (100 KB+)."""

    def test_large_content_does_not_raise(self, optimizer):
        """A 100 KB markdown document is processed without exceptions."""
        block = (
            "# Chapter\n\n"
            "Some paragraph text repeated many times.\n\n"
            "## Section\n\n"
            "```python\nx = 1\n```\n\n"
            "| col1 | col2 |\n"
            "| ---- | ---- |\n"
            "| val1 | val2 |\n\n"
            "- item one\n"
            "- item two\n\n"
        )
        # Repeat to reach ~100 KB
        repeats = (100 * 1024) // len(block) + 1
        content = block * repeats

        optimized, meta = optimizer.optimize(content)
        assert len(optimized) > 0
        assert meta.total_chunks > 1

    def test_large_content_chunk_count_reasonable(self, optimizer):
        """A 100 KB document produces more than 10 chunks with default settings."""
        content = ("word " * 200 + "\n\n") * 50  # ~100 KB
        chunks = optimizer.split_into_chunks(content)
        assert len(chunks) > 10

    def test_large_content_token_estimate_positive(self, optimizer):
        """Token estimate for large content is a positive integer."""
        content = "x" * 100_000
        tokens = optimizer.estimate_total_tokens(content)
        assert tokens > 0
        assert tokens == 100_000 // 4


# ---------------------------------------------------------------------------
# TestEdgeCases
# ---------------------------------------------------------------------------


class TestEdgeCases:
    """Edge-case scenarios: single lines, Unicode, special characters."""

    def test_single_line_no_newline(self, optimizer):
        """Content without any newline produces exactly one chunk."""
        content = "A single line of text without a newline"
        chunks = optimizer.split_into_chunks(content)
        assert len(chunks) == 1

    def test_content_with_only_headings(self, optimizer):
        """Content made entirely of headings is processed without error."""
        content = "# H1\n## H2\n### H3\n"
        optimized, meta = optimizer.optimize(content)
        assert len(meta.heading_levels) > 0

    def test_content_with_only_code_blocks(self, optimizer):
        """Content consisting solely of code fences is handled."""
        content = "```python\nprint('hello')\n```\n"
        optimized, meta = optimizer.optimize(content)
        assert meta.code_blocks == 1

    def test_content_with_only_table(self, optimizer):
        """A standalone markdown table is processed correctly."""
        content = (
            "| A | B |\n"
            "| - | - |\n"
            "| 1 | 2 |\n"
        )
        optimized, meta = optimizer.optimize(content)
        assert meta.tables >= 3  # 3 table rows

    def test_deeply_nested_headings_only_h1_h2_make_boundaries(self, optimizer):
        """Only H1 and H2 headings create semantic boundaries."""
        content = "#### Deep heading\n##### Very deep heading\nContent.\n"
        _, boundaries = optimizer._mark_semantic_boundaries(content, True)
        assert boundaries == []

    def test_repeated_heading_text(self, optimizer):
        """Multiple identical heading texts are each counted individually."""
        content = "## Section\n\nText.\n\n## Section\n\nMore text.\n"
        _, heading_stats = optimizer._normalize_headings(content)
        assert heading_stats.get(2, 0) == 2

    def test_content_with_unicode(self, optimizer):
        """Unicode characters in content do not cause errors."""
        content = "# Ünïcödé Héàdîng\n\n日本語のテキスト。\nArabic: مرحبا\n"
        optimized, meta = optimizer.optimize(content)
        assert len(optimized) > 0

    def test_content_with_crlf_line_endings(self, optimizer):
        """Windows-style CRLF line endings are tolerated."""
        content = "# Title\r\n\r\nParagraph text.\r\n"
        # Should not raise; chunks may differ but no exception expected
        chunks = optimizer.split_into_chunks(content)
        assert isinstance(chunks, list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
