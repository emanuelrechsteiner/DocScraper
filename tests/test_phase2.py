"""
Phase 2 Component Tests

Tests for LLM cleaner, chunk optimizer, and integration with PostScraperCleaner.
All tests verify Phase 2 functionality without external API calls.
"""

import pytest
import json
from pathlib import Path
from docscraper.cleaning.llm import LLMConfig, LLMValidator, ValidationResult, RateLimiter
from docscraper.optimization.chunker import ChunkOptimizer, ChunkMetadata
from docscraper.cleaning.cleaner import PostScraperCleaner, CleaningConfig


class TestLLMConfig:
    """Test LLM configuration"""

    def test_valid_config(self):
        """Test creating valid LLMConfig"""
        config = LLMConfig(
            api_key="test-key",
            model="gpt-4o-mini",
            temperature=0.1
        )
        assert config.api_key == "test-key"
        assert config.model == "gpt-4o-mini"
        assert config.temperature == 0.1

    def test_invalid_temperature(self):
        """Test temperature validation"""
        with pytest.raises(ValueError):
            LLMConfig(temperature=-1)

    def test_invalid_max_tokens(self):
        """Test max_tokens validation"""
        with pytest.raises(ValueError):
            LLMConfig(max_tokens=50)


class TestRateLimiter:
    """Test rate limiting functionality"""

    def test_acquire_success(self):
        """Test successful token acquisition"""
        limiter = RateLimiter(rpm=60)
        success, wait = limiter.acquire()
        assert success is True
        assert wait == 0.0

    def test_rate_limiting(self):
        """Test rate limiter blocking"""
        limiter = RateLimiter(rpm=1)  # 1 request per minute
        # First request succeeds
        success1, _ = limiter.acquire()
        assert success1 is True

        # Second request blocked
        success2, wait = limiter.acquire()
        assert success2 is False
        assert wait > 0

    def test_statistics(self):
        """Test rate limiter statistics"""
        limiter = RateLimiter(rpm=100)
        limiter.acquire()
        stats = limiter.get_statistics()
        assert stats["requests_made"] == 1
        assert stats["rpm_limit"] == 100


class TestLLMValidator:
    """Test LLM validator without API calls"""

    def test_validator_initialization(self):
        """Test validator initialization"""
        config = LLMConfig(api_key=None)
        validator = LLMValidator(config)
        assert validator.api_key is None
        assert validator.stats["validations_requested"] == 0

    def test_validation_without_api_key(self):
        """Test validation gracefully handles missing API key"""
        config = LLMConfig(api_key=None)
        validator = LLMValidator(config)

        result = validator.validate_content("# Test Content\nSome text here")
        assert result.is_valid is True
        assert result.confidence >= 0.0

    def test_fallback_validation_good_content(self):
        """Test fallback validation with good content"""
        config = LLMConfig(api_key=None)
        validator = LLMValidator(config)

        content = "# Heading\n\nSome documentation text content here."
        result = validator.validate_content(content)
        assert result.is_valid is True

    def test_fallback_validation_poor_content(self):
        """Test fallback validation with poor content"""
        config = LLMConfig(api_key=None)
        validator = LLMValidator(config)

        content = "x"  # Too short
        result = validator.validate_content(content)
        assert result.is_valid is False

    def test_statistics(self):
        """Test validator statistics"""
        config = LLMConfig(api_key=None)
        validator = LLMValidator(config)

        validator.validate_content("# Test\n\nContent here")
        validator.validate_content("# Test 2\n\nMore content")

        stats = validator.get_statistics()
        assert stats["validations_requested"] == 2


class TestChunkOptimizer:
    """Test chunk optimization functionality"""

    def test_optimizer_initialization(self):
        """Test optimizer initialization"""
        optimizer = ChunkOptimizer(chunk_size=512, overlap=50)
        assert optimizer.chunk_size == 512
        assert optimizer.overlap == 50

    def test_chunk_size_clamping(self):
        """Test chunk size limits"""
        # Too small
        opt1 = ChunkOptimizer(chunk_size=50)
        assert opt1.chunk_size == 100

        # Too large
        opt2 = ChunkOptimizer(chunk_size=3000)
        assert opt2.chunk_size == 2048

    def test_empty_content(self):
        """Test with empty content"""
        optimizer = ChunkOptimizer()
        content = ""
        optimized, metadata = optimizer.optimize(content)
        assert optimized == ""
        assert metadata.total_chunks == 0

    def test_simple_optimization(self):
        """Test basic content optimization"""
        optimizer = ChunkOptimizer()
        content = "# Heading\n\nParagraph text.\n\nMore text."
        optimized, metadata = optimizer.optimize(content)
        assert len(optimized) > 0
        assert metadata.heading_levels[1] == 1

    def test_heading_count(self):
        """Test heading detection"""
        optimizer = ChunkOptimizer()
        content = "# H1\n## H2\n### H3\n\nContent"
        optimized, metadata = optimizer.optimize(content)
        assert metadata.heading_levels.get(1, 0) == 1
        assert metadata.heading_levels.get(2, 0) == 1
        assert metadata.heading_levels.get(3, 0) == 1

    def test_code_block_detection(self):
        """Test code block detection"""
        optimizer = ChunkOptimizer()
        content = """# Code Example

```python
def hello():
    print("world")
```

More content"""
        optimized, metadata = optimizer.optimize(content)
        assert metadata.code_blocks >= 1

    def test_chunk_splitting(self):
        """Test content splitting into chunks"""
        optimizer = ChunkOptimizer(chunk_size=100)
        content = "# Header\n\n" + "Text line.\n" * 50
        chunks = optimizer.split_into_chunks(content)
        assert len(chunks) > 1

    def test_chunk_info(self):
        """Test chunk information gathering"""
        optimizer = ChunkOptimizer()
        chunks = ["Short content", "Much longer content here" * 10, "Medium"]
        info = optimizer.get_chunk_info(chunks)
        assert info["total_chunks"] == 3
        assert info["avg_size"] > 0
        assert info["max_size"] > info["min_size"]

    def test_token_estimation(self):
        """Test token estimation"""
        optimizer = ChunkOptimizer()
        # Approx 1 token per 4 chars
        text = "A" * 100  # ~25 tokens
        tokens = optimizer._estimate_tokens(text)
        assert tokens == 25


class TestPhase2Integration:
    """Test Phase 2 integration with PostScraperCleaner"""

    def test_config_with_chunk_optimization(self):
        """Test config with chunk optimization enabled"""
        config = CleaningConfig(
            enable_chunk_optimization=True,
            target_chunk_size=512,
            overlap_size=50
        )
        assert config.enable_chunk_optimization is True
        assert config.target_chunk_size == 512

    def test_config_with_llm_disabled(self):
        """Test config with LLM disabled by default"""
        config = CleaningConfig()
        assert config.enable_llm_validation is False

    def test_cleaner_initialization_phase2(self):
        """Test PostScraperCleaner initializes Phase 2 components"""
        config = CleaningConfig(
            enable_chunk_optimization=True,
            enable_llm_validation=False
        )
        cleaner = PostScraperCleaner(config)
        # Chunk optimizer should be initialized
        assert cleaner.chunk_optimizer is not None
        # LLM validator should not be initialized (no API key)
        assert cleaner.llm_validator is None

    def test_validation_result_dict_conversion(self):
        """Test ValidationResult to dict conversion"""
        result = ValidationResult(
            is_valid=True,
            confidence=0.95,
            issues=[],
            suggestions=["Good content"]
        )
        result_dict = result.to_dict()
        assert result_dict["is_valid"] is True
        assert result_dict["confidence"] == 0.95

    def test_chunk_metadata_dict_conversion(self):
        """Test ChunkMetadata to dict conversion"""
        metadata = ChunkMetadata(
            total_chunks=5,
            code_blocks=2,
            heading_levels={1: 1, 2: 3},
            avg_chunk_size=450
        )
        meta_dict = metadata.to_dict()
        assert meta_dict["total_chunks"] == 5
        assert meta_dict["code_blocks"] == 2


if __name__ == "__main__":
    # Run tests: pytest test_phase2.py -v
    pytest.main([__file__, "-v"])
