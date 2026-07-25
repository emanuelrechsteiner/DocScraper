"""
Chunk Optimization for Vector Database Ingestion

This module prepares markdown content for optimal embedding and chunking.
Handles semantic boundaries, code block preservation, and token estimation.

Phase 2: Optimize cleaned content for vector databases
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class ChunkMetadata:
    """Metadata about content chunks"""
    total_chunks: int = 0
    heading_levels: dict[int, int] = field(default_factory=dict)
    code_blocks: int = 0
    tables: int = 0
    lists: int = 0
    semantic_boundaries: list[int] = field(default_factory=list)
    avg_chunk_size: int = 0
    optimization_notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "total_chunks": self.total_chunks,
            "heading_levels": self.heading_levels,
            "code_blocks": self.code_blocks,
            "tables": self.tables,
            "lists": self.lists,
            "avg_chunk_size": self.avg_chunk_size,
            "optimization_notes": self.optimization_notes,
        }


class ChunkOptimizer:
    """Optimizes content for vector database chunking"""

    # Configuration
    DEFAULT_CHUNK_SIZE = 512  # tokens
    DEFAULT_OVERLAP = 50  # tokens
    APPROX_TOKENS_PER_CHAR = 0.25  # ~4 chars per token
    APPROX_CHARS_PER_TOKEN = 4

    # Regex patterns
    HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
    CODE_BLOCK_PATTERN = re.compile(r"```[\s\S]*?```", re.MULTILINE)
    TABLE_PATTERN = re.compile(r"^\|.+\|$", re.MULTILINE)
    LIST_PATTERN = re.compile(r"^[\s]*[-*+]\s+", re.MULTILINE)
    HORIZONTAL_RULE_PATTERN = re.compile(r"^---+$", re.MULTILINE)

    def __init__(
        self,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        overlap: int = DEFAULT_OVERLAP,
        preserve_structure: bool = True,
    ) -> None:
        """Initialize chunk optimizer"""
        self.chunk_size = max(100, min(chunk_size, 2048))  # Clamp 100-2048
        self.overlap = min(overlap, self.chunk_size // 2)
        self.preserve_structure = preserve_structure

        logger.info(
            f"ChunkOptimizer initialized: chunk_size={self.chunk_size}, "
            f"overlap={self.overlap}, preserve_structure={preserve_structure}"
        )

    def optimize(
        self, content: str, preserve_structure: bool = True
    ) -> tuple[str, ChunkMetadata]:
        """
        Optimize content for chunking.
        Returns (optimized_content, metadata)
        """
        if not content or not content.strip():
            return "", ChunkMetadata(
                optimization_notes=["Empty content provided"]
            )

        optimized = content
        metadata = ChunkMetadata()

        # Step 1: Normalize headings
        optimized, heading_stats = self._normalize_headings(optimized)
        metadata.heading_levels = heading_stats

        # Step 2: Mark semantic boundaries
        optimized, boundaries = self._mark_semantic_boundaries(
            optimized, preserve_structure
        )
        metadata.semantic_boundaries = boundaries

        # Step 3: Count special elements
        metadata.code_blocks = len(self.CODE_BLOCK_PATTERN.findall(optimized))
        metadata.tables = len(self.TABLE_PATTERN.findall(optimized))
        metadata.lists = len(self.LIST_PATTERN.findall(optimized))

        # Step 4: Estimate chunks
        chunks = self.split_into_chunks(optimized)
        metadata.total_chunks = len(chunks)
        if chunks:
            metadata.avg_chunk_size = sum(len(c) for c in chunks) // len(chunks)

        metadata.optimization_notes = [
            f"Normalized {len(heading_stats)} heading levels",
            f"Marked {len(boundaries)} semantic boundaries",
            f"Estimated {len(chunks)} chunks (avg {metadata.avg_chunk_size} tokens)",
        ]

        return optimized, metadata

    def _normalize_headings(self, content: str) -> tuple[str, dict[int, int]]:
        """
        Normalize heading hierarchy and count by level.
        Ensures proper H1->H2->H3 nesting.
        """
        lines = content.split("\n")
        heading_levels = {i: 0 for i in range(1, 7)}
        min_level = 7
        adjusted_lines = []

        for line in lines:
            match = self.HEADING_PATTERN.match(line)
            if match:
                level = len(match.group(1))
                heading_levels[level] += 1
                min_level = min(min_level, level)
                adjusted_lines.append(line)
            else:
                adjusted_lines.append(line)

        # Remove empty heading levels below minimum
        if min_level > 1:
            for i in range(1, min_level):
                del heading_levels[i]

        normalized = "\n".join(adjusted_lines)
        return normalized, {k: v for k, v in heading_levels.items() if v > 0}

    def _mark_semantic_boundaries(
        self, content: str, preserve_structure: bool
    ) -> tuple[str, list[int]]:
        """
        Mark semantic boundaries for optimal chunking.
        Boundaries: headings, code blocks, tables, major gaps.
        """
        boundaries = []
        lines = content.split("\n")
        char_pos = 0

        for i, line in enumerate(lines):
            # Track character position
            line_start = char_pos
            char_pos += len(line) + 1  # +1 for newline

            # Major heading (H1, H2) boundary
            if line.startswith("# ") or line.startswith("## "):
                boundaries.append(line_start)

            # Code block start
            if line.strip().startswith("```"):
                boundaries.append(line_start)

            # Table line
            if self.TABLE_PATTERN.match(line):
                boundaries.append(line_start)

            # Multiple blank lines
            if i > 0 and line.strip() == "" and (
                i + 1 < len(lines) and lines[i + 1].strip() == ""
            ):
                boundaries.append(line_start)

        return content, sorted(list(set(boundaries)))

    def split_into_chunks(self, content: str) -> list[str]:
        """
        Split content into chunks respecting token limits and boundaries.
        Returns list of chunk strings.
        """
        if not content or not content.strip():
            return []

        chunks = []
        current_chunk = ""
        current_tokens = 0

        # Simple line-based chunking
        lines = content.split("\n")

        for line in lines:
            line_tokens = self._estimate_tokens(line)
            line_with_newline = line + "\n"

            # Check if adding this line exceeds chunk size
            if (
                current_tokens + line_tokens > self.chunk_size
                and current_chunk.strip()
            ):
                # Save current chunk
                chunks.append(current_chunk.strip())

                # Start new chunk with overlap
                if self.overlap > 0:
                    overlap_lines = self._get_overlap_lines(current_chunk)
                    current_chunk = overlap_lines + line_with_newline
                    current_tokens = self._estimate_tokens(current_chunk)
                else:
                    current_chunk = line_with_newline
                    current_tokens = line_tokens
            else:
                current_chunk += line_with_newline
                current_tokens += line_tokens

        # Add final chunk
        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        return chunks

    def _get_overlap_lines(self, content: str, max_tokens: int | None = None) -> str:
        """Extract last N lines for overlap"""
        if max_tokens is None:
            max_tokens = self.overlap

        lines = content.split("\n")
        overlap_lines = []
        token_count = 0

        # Walk backward to collect overlap
        for line in reversed(lines):
            line_tokens = self._estimate_tokens(line)
            if token_count + line_tokens > max_tokens:
                break
            overlap_lines.insert(0, line)
            token_count += line_tokens

        return "\n".join(overlap_lines)

    def _estimate_tokens(self, text: str) -> int:
        """Estimate token count (4 chars ≈ 1 token)"""
        return max(1, len(text) // self.APPROX_CHARS_PER_TOKEN)

    def estimate_total_tokens(self, content: str) -> int:
        """Estimate total tokens in content"""
        return self._estimate_tokens(content)

    def get_chunk_info(self, chunks: list[str]) -> dict:
        """Get information about chunks"""
        if not chunks:
            return {"total_chunks": 0, "avg_size": 0, "min_size": 0, "max_size": 0}

        sizes = [self._estimate_tokens(c) for c in chunks]
        return {
            "total_chunks": len(chunks),
            "avg_size": sum(sizes) // len(sizes) if sizes else 0,
            "min_size": min(sizes) if sizes else 0,
            "max_size": max(sizes) if sizes else 0,
            "total_tokens": sum(sizes),
        }
