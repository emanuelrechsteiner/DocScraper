"""
PostScraperCleaner - Advanced Documentation Cleaning and Optimization

This module provides rule-based and LLM-enhanced cleaning for scraped documentation.
It removes navigation elements, boilerplate, and redundant content while preserving
valuable documentation content.

Phase 1: Rule-based cleaning with pattern matching
Phase 2: LLM validation and intelligent content analysis (future)
"""

import re
import time
import logging
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, Callable, List, Dict, Tuple
from queue import Queue
from threading import Thread

from cleaning_rules import (
    CleaningPattern,
    PatternRegistry,
    DEFAULT_REGISTRY,
    PatternCategory
)

# Phase 2: LLM and Chunk Optimization (optional imports)
try:
    from llm_cleaner import LLMValidator, LLMConfig, ValidationResult
except ImportError:
    LLMValidator = None
    LLMConfig = None
    ValidationResult = None

try:
    from chunk_optimizer import ChunkOptimizer, ChunkMetadata
except ImportError:
    ChunkOptimizer = None
    ChunkMetadata = None

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class CleaningConfig:
    """Configuration for PostScraperCleaner"""
    remove_navigation: bool = True
    remove_headers_footers: bool = True
    remove_boilerplate: bool = True
    enable_llm_validation: bool = False
    llm_confidence_threshold: float = 0.85
    target_chunk_size: int = 512
    overlap_size: int = 50
    max_cost_per_document: float = 0.05
    rate_limit_rpm: int = 500
    openai_api_key: Optional[str] = None
    enable_chunk_optimization: bool = True

    def __post_init__(self):
        """Validate configuration values"""
        if not 0.0 <= self.llm_confidence_threshold <= 1.0:
            raise ValueError("llm_confidence_threshold must be between 0.0 and 1.0")
        if self.target_chunk_size < 100:
            raise ValueError("target_chunk_size must be at least 100")
        if self.overlap_size >= self.target_chunk_size:
            raise ValueError("overlap_size must be less than target_chunk_size")
        if self.max_cost_per_document < 0:
            raise ValueError("max_cost_per_document must be non-negative")
        if self.rate_limit_rpm < 1:
            raise ValueError("rate_limit_rpm must be at least 1")


@dataclass
class CleaningResult:
    """Result of cleaning operation on a single document"""
    input_file: Path
    output_file: Optional[Path] = None
    success: bool = False
    original_size: int = 0
    cleaned_size: int = 0
    reduction_percentage: float = 0.0
    removed_sections: List[str] = field(default_factory=list)
    preserved_sections: List[str] = field(default_factory=list)
    structure_score: float = 0.0
    rule_based_cleaning: bool = False
    llm_validation_used: bool = False
    llm_validation: Optional[Dict] = None
    llm_cost: float = 0.0
    chunk_optimization_used: bool = False
    chunk_metadata: Optional[Dict] = None
    processing_time: float = 0.0
    content_quality_score: float = 0.0
    chunk_optimization_score: float = 0.0
    error_message: Optional[str] = None
    warnings: List[str] = field(default_factory=list)

    def calculate_reduction(self):
        """Calculate reduction percentage from sizes"""
        if self.original_size > 0:
            self.reduction_percentage = (
                (self.original_size - self.cleaned_size) / self.original_size * 100
            )

    def to_dict(self) -> Dict:
        """Convert result to dictionary for serialization"""
        return {
            "input_file": str(self.input_file),
            "output_file": str(self.output_file) if self.output_file else None,
            "success": self.success,
            "original_size": self.original_size,
            "cleaned_size": self.cleaned_size,
            "reduction_percentage": round(self.reduction_percentage, 2),
            "removed_sections": self.removed_sections,
            "rule_based_cleaning": self.rule_based_cleaning,
            "processing_time": round(self.processing_time, 3),
            "error_message": self.error_message,
        }


class RuleBasedCleaner:
    """Rule-based content cleaning using pattern matching"""

    def __init__(self, config: CleaningConfig, pattern_registry: PatternRegistry = None):
        """Initialize rule-based cleaner"""
        self.config = config
        self.registry = pattern_registry or DEFAULT_REGISTRY
        self._filter_patterns_by_config()

    def _filter_patterns_by_config(self):
        """Disable patterns based on config settings"""
        if not self.config.remove_navigation:
            for pattern in self.registry.get_patterns_by_category(PatternCategory.NAVIGATION):
                pattern.enabled = False

        if not self.config.remove_headers_footers:
            for name in ["header_section", "footer_section"]:
                pattern = self.registry.get_pattern(name)
                if pattern:
                    pattern.enabled = False

        if not self.config.remove_boilerplate:
            for pattern in self.registry.get_patterns_by_category(PatternCategory.BOILERPLATE):
                pattern.enabled = False

    def clean(self, content: str) -> Tuple[str, Dict]:
        """Clean content using rule-based patterns"""
        if not content or not content.strip():
            return "", {"patterns_applied": 0, "total_replacements": 0, "removed_sections": [], "confidence_score": 0.0}

        cleaned = content
        metadata = {
            "patterns_applied": 0,
            "total_replacements": 0,
            "removed_sections": [],
            "confidence_scores": []
        }

        for pattern in self.registry.get_enabled_patterns():
            result, count = pattern.apply(cleaned)
            if count > 0:
                cleaned = result
                metadata["patterns_applied"] += 1
                metadata["total_replacements"] += count
                metadata["removed_sections"].append(pattern.name)
                metadata["confidence_scores"].append(pattern.confidence)

        if metadata["confidence_scores"]:
            metadata["confidence_score"] = sum(metadata["confidence_scores"]) / len(metadata["confidence_scores"])
        else:
            metadata["confidence_score"] = 1.0

        cleaned = self._normalize_whitespace(cleaned)
        cleaned = self._extract_main_content(cleaned)
        metadata["structure_score"] = self._calculate_structure_score(cleaned)

        return cleaned, metadata

    def _normalize_whitespace(self, content: str) -> str:
        """Normalize whitespace in content"""
        lines = [line.rstrip() for line in content.split('\n')]
        normalized = []
        blank_count = 0
        for line in lines:
            if not line.strip():
                blank_count += 1
                if blank_count <= 2:
                    normalized.append(line)
            else:
                blank_count = 0
                normalized.append(line)
        return '\n'.join(normalized)

    def _extract_main_content(self, content: str) -> str:
        """Extract main documentation content"""
        lines = content.split('\n')
        start_idx = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped and not stripped.startswith('---') and stripped != '===':
                start_idx = i
                break

        end_idx = len(lines) - 1
        for i in range(len(lines) - 1, -1, -1):
            stripped = lines[i].strip()
            if stripped and not stripped.startswith('---') and stripped != '===':
                end_idx = i + 1
                break

        return '\n'.join(lines[start_idx:end_idx])

    def _calculate_structure_score(self, content: str) -> float:
        """Calculate content structure quality score"""
        if not content:
            return 0.0

        score = 0.0
        max_score = 4.0

        header_count = len(re.findall(r'^#{1,6}\s+\S', content, re.MULTILINE))
        score += min(1.0, header_count / 3)

        code_block_count = len(re.findall(r'```[\s\S]*?```', content))
        score += min(1.0, code_block_count / 2)

        list_item_count = len(re.findall(r'^\s*[-*+]\s+', content, re.MULTILINE))
        score += min(1.0, list_item_count / 5)

        paragraph_count = len([p for p in content.split('\n\n') if p.strip()])
        score += min(1.0, paragraph_count / 3)

        return score / max_score


class PostScraperCleaner:
    """Main orchestrator for document cleaning operations"""

    def __init__(
        self,
        config: CleaningConfig,
        progress_callback: Optional[Callable] = None
    ):
        """Initialize PostScraperCleaner"""
        self.config = config
        self.progress_callback = progress_callback
        self.rule_cleaner = RuleBasedCleaner(config)

        # Phase 2: Initialize LLM validator if enabled
        self.llm_validator = None
        if config.enable_llm_validation and LLMValidator:
            llm_config = LLMConfig(
                api_key=config.openai_api_key,
                rate_limit_rpm=config.rate_limit_rpm
            )
            self.llm_validator = LLMValidator(llm_config)
            logger.info("LLM validator initialized")

        # Phase 2: Initialize chunk optimizer if enabled
        self.chunk_optimizer = None
        if config.enable_chunk_optimization and ChunkOptimizer:
            self.chunk_optimizer = ChunkOptimizer(
                chunk_size=config.target_chunk_size,
                overlap=config.overlap_size
            )
            logger.info("Chunk optimizer initialized")

        self.stats = {
            "total_processed": 0,
            "total_success": 0,
            "total_failed": 0,
            "total_bytes_before": 0,
            "total_bytes_after": 0,
            "total_processing_time": 0.0,
            "total_llm_cost": 0.0,
            "total_chunks_created": 0,
        }

        logger.info("PostScraperCleaner initialized")

    def clean_document(self, input_path: Path, output_path: Path) -> CleaningResult:
        """Clean a single document"""
        result = CleaningResult(
            input_file=input_path,
            output_file=output_path
        )

        start_time = time.time()

        try:
            if not input_path.exists():
                raise FileNotFoundError(f"Input file not found: {input_path}")

            if input_path.suffix.lower() != '.md':
                raise ValueError(f"Input file must be markdown (.md): {input_path}")

            logger.info(f"Processing: {input_path.name}")
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            result.original_size = len(content)
            self.stats["total_bytes_before"] += result.original_size

            cleaned_content, metadata = self.rule_cleaner.clean(content)
            result.rule_based_cleaning = True
            result.removed_sections = metadata["removed_sections"]
            result.structure_score = metadata["structure_score"]

            result.content_quality_score = self._calculate_content_quality(cleaned_content)
            result.chunk_optimization_score = self._calculate_chunk_score(cleaned_content)

            # Phase 2: LLM Validation (optional)
            if self.llm_validator:
                try:
                    llm_result = self.llm_validator.validate_content(
                        cleaned_content,
                        metadata={"original_size": result.original_size}
                    )
                    result.llm_validation_used = True
                    result.llm_validation = llm_result.to_dict() if hasattr(llm_result, 'to_dict') else {"is_valid": True, "confidence": 0.7}
                    result.llm_cost = llm_result.cost if hasattr(llm_result, 'cost') else 0.0
                    self.stats["total_llm_cost"] += result.llm_cost
                except Exception as e:
                    logger.warning(f"LLM validation failed: {e}")
                    result.warnings.append(f"LLM validation error: {e}")

            # Phase 2: Chunk Optimization (optional)
            if self.chunk_optimizer:
                try:
                    optimized_content, chunk_meta = self.chunk_optimizer.optimize(
                        cleaned_content,
                        preserve_structure=True
                    )
                    result.chunk_optimization_used = True
                    result.chunk_metadata = chunk_meta.to_dict() if hasattr(chunk_meta, 'to_dict') else {}
                    self.stats["total_chunks_created"] += chunk_meta.total_chunks if hasattr(chunk_meta, 'total_chunks') else 0
                    cleaned_content = optimized_content
                except Exception as e:
                    logger.warning(f"Chunk optimization failed: {e}")
                    result.warnings.append(f"Chunk optimization error: {e}")

            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)

            result.cleaned_size = len(cleaned_content)
            result.calculate_reduction()
            result.success = True

            logger.info(f"Cleaned {input_path.name}: {result.reduction_percentage:.1f}% reduction")

        except Exception as e:
            result.success = False
            result.error_message = str(e)
            logger.error(f"Error cleaning {input_path.name}: {e}")

        finally:
            result.processing_time = time.time() - start_time
            self._update_statistics(result)

        return result

    def clean_batch(
        self,
        input_folder: Path,
        output_folder: Path,
        pattern: str = "*.md"
    ) -> List[CleaningResult]:
        """Clean multiple documents in batch"""
        if not input_folder.exists():
            raise FileNotFoundError(f"Input folder not found: {input_folder}")

        input_files = list(input_folder.glob(pattern))
        if not input_files:
            logger.warning(f"No files matching '{pattern}' in {input_folder}")
            return []

        logger.info(f"Processing {len(input_files)} files from {input_folder}")

        results = []

        for i, input_path in enumerate(input_files):
            output_path = output_folder / input_path.name
            result = self.clean_document(input_path, output_path)
            results.append(result)

            if self.progress_callback:
                self.progress_callback({
                    "type": "progress",
                    "processed": i + 1,
                    "total": len(input_files),
                    "current_file": input_path.name
                })

        return results

    def _calculate_content_quality(self, content: str) -> float:
        """Calculate overall content quality score"""
        if not content:
            return 0.0

        score = 0.0
        word_count = len(content.split())
        score += min(1.0, word_count / 100)

        if '```' in content:
            score += 0.5

        if re.search(r'^#{1,6}\s+', content, re.MULTILINE):
            score += 0.3

        if re.search(r'^\s*[-*+]\s+', content, re.MULTILINE):
            score += 0.2

        return min(1.0, score / 2.0)

    def _calculate_chunk_score(self, content: str) -> float:
        """Calculate how well content fits chunking strategy"""
        if not content:
            return 0.0

        content_size = len(content)
        target = self.config.target_chunk_size

        if content_size < target * 0.5:
            return 0.5
        elif content_size <= target * 1.5:
            return 1.0
        else:
            chunks_needed = content_size / target
            return max(0.3, 1.0 / chunks_needed)

    def _update_statistics(self, result: CleaningResult):
        """Update running statistics"""
        self.stats["total_processed"] += 1
        if result.success:
            self.stats["total_success"] += 1
            self.stats["total_bytes_after"] += result.cleaned_size
        else:
            self.stats["total_failed"] += 1

        self.stats["total_processing_time"] += result.processing_time
        self.stats["total_llm_cost"] += result.llm_cost

    def get_statistics(self) -> Dict:
        """Get processing statistics"""
        stats = self.stats.copy()

        if stats["total_processed"] > 0:
            stats["success_rate"] = stats["total_success"] / stats["total_processed"]
            stats["average_processing_time"] = (
                stats["total_processing_time"] / stats["total_processed"]
            )
        else:
            stats["success_rate"] = 0.0
            stats["average_processing_time"] = 0.0

        if stats["total_bytes_before"] > 0:
            stats["overall_reduction_percentage"] = (
                (stats["total_bytes_before"] - stats["total_bytes_after"]) /
                stats["total_bytes_before"] * 100
            )
        else:
            stats["overall_reduction_percentage"] = 0.0

        return stats
