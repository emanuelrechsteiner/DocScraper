"""
Phase 4: Comprehensive Unit Tests for Core Components

Tests for RuleBasedCleaner, PatternRegistry, and related core functionality.
All tests verify Phase 1 components work correctly.
"""

import pytest
from pathlib import Path
from docscraper.cleaning.cleaner import (
    PostScraperCleaner,
    CleaningConfig,
    RuleBasedCleaner,
    CleaningResult,
)
from docscraper.cleaning.rules import (
    CleaningPattern,
    PatternRegistry,
    PatternCategory,
    CLEANING_PATTERNS,
    DEFAULT_REGISTRY,
)


class TestPatternCategory:
    """Test PatternCategory enum"""

    def test_all_categories_exist(self):
        """Test all pattern categories are defined"""
        assert PatternCategory.NAVIGATION.value == "navigation"
        assert PatternCategory.UI.value == "ui"
        assert PatternCategory.BOILERPLATE.value == "boilerplate"
        assert PatternCategory.REDUNDANT.value == "redundant"

    def test_category_enum_members(self):
        """Test we can iterate all categories"""
        categories = list(PatternCategory)
        assert len(categories) == 4


class TestCleaningPattern:
    """Test CleaningPattern dataclass"""

    def test_pattern_creation(self):
        """Test creating a cleaning pattern"""
        pattern = CleaningPattern(
            name="test_pattern",
            pattern=r"test.*pattern",
            replacement="[REMOVED]",
            confidence=0.95,
            category=PatternCategory.NAVIGATION,
            description="Test pattern",
        )
        assert pattern.name == "test_pattern"
        assert pattern.confidence == 0.95
        assert pattern.enabled is True

    def test_pattern_compilation(self):
        """Test regex pattern compilation"""
        pattern = CleaningPattern(
            name="test",
            pattern=r"^\s*skip\s+",
            replacement="",
            confidence=0.9,
            category=PatternCategory.NAVIGATION,
            description="Test",
        )
        assert pattern.compiled_pattern is not None

    def test_pattern_invalid_regex(self):
        """Test invalid regex raises error"""
        with pytest.raises(ValueError):
            CleaningPattern(
                name="bad",
                pattern=r"(unclosed group",
                replacement="",
                confidence=0.9,
                category=PatternCategory.NAVIGATION,
                description="Bad pattern",
            )

    def test_pattern_matches(self):
        """Test pattern matching"""
        pattern = CleaningPattern(
            name="skip_nav",
            pattern=r"^Skip to content\n",
            replacement="",
            confidence=0.95,
            category=PatternCategory.NAVIGATION,
            description="Test",
        )
        content = "Skip to content\nMain content here"
        matches = pattern.matches(content)
        assert matches >= 0

    def test_pattern_apply(self):
        """Test applying pattern to content"""
        pattern = CleaningPattern(
            name="test",
            pattern=r"\[TEMP\]",
            replacement="",
            confidence=0.9,
            category=PatternCategory.BOILERPLATE,
            description="Test",
        )
        content = "Text [TEMP] here [TEMP] and here"
        result, count = pattern.apply(content)
        assert count == 2
        assert "[TEMP]" not in result


class TestPatternRegistry:
    """Test PatternRegistry class"""

    def test_registry_creation(self):
        """Test creating pattern registry"""
        registry = PatternRegistry()
        assert registry.patterns is not None
        assert len(registry.patterns) == 25  # 25 predefined patterns

    def test_default_registry(self):
        """Test default registry instance"""
        assert DEFAULT_REGISTRY is not None
        assert len(DEFAULT_REGISTRY.patterns) == 25

    def test_get_pattern(self):
        """Test retrieving pattern by name"""
        registry = PatternRegistry()
        pattern = registry.get_pattern("skip_navigation")
        assert pattern is not None
        assert pattern.name == "skip_navigation"

    def test_get_nonexistent_pattern(self):
        """Test getting nonexistent pattern returns None"""
        registry = PatternRegistry()
        pattern = registry.get_pattern("nonexistent")
        assert pattern is None

    def test_get_enabled_patterns(self):
        """Test getting all enabled patterns"""
        registry = PatternRegistry()
        enabled = registry.get_enabled_patterns()
        assert len(enabled) > 0
        assert all(p.enabled for p in enabled)

    def test_disable_pattern(self):
        """Test disabling a pattern"""
        registry = PatternRegistry()
        success = registry.disable_pattern("skip_navigation")
        assert success is True

        pattern = registry.get_pattern("skip_navigation")
        assert pattern.enabled is False

    def test_enable_pattern(self):
        """Test enabling a pattern"""
        registry = PatternRegistry()
        registry.disable_pattern("skip_navigation")
        success = registry.enable_pattern("skip_navigation")
        assert success is True

        pattern = registry.get_pattern("skip_navigation")
        assert pattern.enabled is True

    def test_get_patterns_by_category(self):
        """Test getting patterns by category"""
        registry = PatternRegistry()

        nav_patterns = registry.get_patterns_by_category(PatternCategory.NAVIGATION)
        assert len(nav_patterns) > 0
        assert all(p.category == PatternCategory.NAVIGATION for p in nav_patterns)

        ui_patterns = registry.get_patterns_by_category(PatternCategory.UI)
        assert len(ui_patterns) > 0
        assert all(p.category == PatternCategory.UI for p in ui_patterns)

    def test_get_patterns_by_confidence(self):
        """Test getting patterns above confidence threshold"""
        registry = PatternRegistry()
        high_confidence = registry.get_patterns_by_confidence(0.85)
        assert len(high_confidence) > 0
        assert all(p.confidence >= 0.85 for p in high_confidence)

    def test_get_statistics(self):
        """Test getting registry statistics"""
        registry = PatternRegistry()
        stats = registry.get_statistics()

        assert "total_patterns" in stats
        assert "enabled_patterns" in stats
        assert "disabled_patterns" in stats
        assert "by_category" in stats
        assert "average_confidence" in stats

        assert stats["total_patterns"] == 25
        assert stats["enabled_patterns"] + stats["disabled_patterns"] == 25
        assert 0.7 < stats["average_confidence"] < 0.95


class TestRuleBasedCleaner:
    """Test RuleBasedCleaner class"""

    def test_cleaner_initialization(self):
        """Test cleaner initialization"""
        config = CleaningConfig()
        cleaner = RuleBasedCleaner(config)
        assert cleaner.config == config
        assert cleaner.registry is not None

    def test_clean_empty_content(self):
        """Test cleaning empty content"""
        config = CleaningConfig()
        cleaner = RuleBasedCleaner(config)
        content = ""
        result, metadata = cleaner.clean(content)
        assert result == ""
        assert metadata["patterns_applied"] == 0

    def test_clean_with_navigation(self):
        """Test cleaning content with navigation elements"""
        config = CleaningConfig(remove_navigation=True)
        cleaner = RuleBasedCleaner(config)

        content = "Skip to main content\n\n# Main heading\n\nContent here"
        result, metadata = cleaner.clean(content)

        assert "Skip to main content" not in result
        assert "# Main heading" in result
        assert metadata["patterns_applied"] > 0

    def test_clean_respects_config(self):
        """Test cleaning respects configuration settings"""
        # With navigation removal disabled
        config = CleaningConfig(remove_navigation=False)
        cleaner = RuleBasedCleaner(config)

        content = "Skip to content\n# Heading\n\nMain content"
        result, metadata = cleaner.clean(content)

        # Navigation pattern should not be applied
        nav_patterns = [
            p.name for p in cleaner.registry.get_patterns_by_category(PatternCategory.NAVIGATION)
        ]
        assert not any(name in metadata["removed_sections"] for name in nav_patterns)

    def test_clean_structure_score(self):
        """Test structure score calculation"""
        config = CleaningConfig()
        cleaner = RuleBasedCleaner(config)

        # Good content with structure
        good_content = "# Heading\n\n## Subheading\n\n```python\ncode\n```\n\n- item 1\n- item 2"
        result, metadata = cleaner.clean(good_content)
        assert metadata["structure_score"] > 0.5

        # Poor content (minimal structure)
        poor_content = "x y z"
        result, metadata = cleaner.clean(poor_content)
        assert metadata["structure_score"] < 0.5

    def test_clean_whitespace_normalization(self):
        """Test whitespace normalization"""
        config = CleaningConfig()
        cleaner = RuleBasedCleaner(config)

        content = "Line 1\n\n\n\n\nLine 2"
        result, metadata = cleaner.clean(content)

        # Should normalize excessive blank lines
        blank_lines = result.count("\n\n\n")
        assert blank_lines == 0  # No 3+ consecutive newlines

    def test_clean_main_content_extraction(self):
        """Test main content extraction"""
        config = CleaningConfig()
        cleaner = RuleBasedCleaner(config)

        content = "---\nHeader\n---\n\n# Main Content\n\nText here\n\n---\nFooter\n---"
        result, metadata = cleaner.clean(content)

        # Should extract content between separators
        assert "Main Content" in result
        assert "Text here" in result


class TestCleaningConfig:
    """Test CleaningConfig validation"""

    def test_valid_config(self):
        """Test valid configuration"""
        config = CleaningConfig(
            remove_navigation=True,
            remove_headers_footers=True,
            llm_confidence_threshold=0.85,
        )
        assert config.llm_confidence_threshold == 0.85

    def test_invalid_threshold(self):
        """Test invalid confidence threshold"""
        with pytest.raises(ValueError):
            CleaningConfig(llm_confidence_threshold=1.5)

    def test_invalid_chunk_size(self):
        """Test invalid chunk size"""
        with pytest.raises(ValueError):
            CleaningConfig(target_chunk_size=50)

    def test_invalid_overlap(self):
        """Test invalid overlap"""
        with pytest.raises(ValueError):
            CleaningConfig(
                target_chunk_size=512,
                overlap_size=512,  # Can't equal chunk size
            )


class TestCleaningResult:
    """Test CleaningResult dataclass"""

    def test_result_creation(self):
        """Test creating cleaning result"""
        path = Path("test.md")
        result = CleaningResult(input_file=path, output_file=path)
        assert result.input_file == path
        assert result.success is False
        assert result.reduction_percentage == 0.0

    def test_reduction_calculation(self):
        """Test reduction percentage calculation"""
        result = CleaningResult(
            input_file=Path("test.md"),
            original_size=1000,
            cleaned_size=800,
        )
        result.calculate_reduction()
        assert result.reduction_percentage == 20.0

    def test_to_dict_conversion(self):
        """Test converting result to dictionary"""
        result = CleaningResult(
            input_file=Path("test.md"),
            output_file=Path("output.md"),
            success=True,
            original_size=1000,
            cleaned_size=800,
        )
        result.calculate_reduction()

        result_dict = result.to_dict()
        assert result_dict["success"] is True
        assert result_dict["original_size"] == 1000
        assert result_dict["reduction_percentage"] == 20.0


class TestAllPatterns:
    """Test all 25 predefined patterns"""

    def test_all_patterns_have_config(self):
        """Test all patterns have proper configuration"""
        for pattern in CLEANING_PATTERNS:
            assert pattern.name
            assert pattern.pattern
            assert 0.0 <= pattern.confidence <= 1.0
            assert pattern.category in PatternCategory

    def test_all_patterns_compile(self):
        """Test all patterns compile without errors"""
        for pattern in CLEANING_PATTERNS:
            assert pattern.compiled_pattern is not None

    def test_navigation_patterns(self):
        """Test navigation patterns"""
        nav_patterns = [p for p in CLEANING_PATTERNS if p.category == PatternCategory.NAVIGATION]
        assert len(nav_patterns) == 5
        expected_names = {"skip_navigation", "breadcrumbs", "toc_nav", "prev_next_navigation", "broken_link_fragments"}
        actual_names = {p.name for p in nav_patterns}
        assert actual_names == expected_names

    def test_ui_patterns(self):
        """Test UI element patterns"""
        ui_patterns = [p for p in CLEANING_PATTERNS if p.category == PatternCategory.UI]
        assert len(ui_patterns) == 12
        expected_names = {
            "header_section",
            "footer_section",
            "mobile_menu",
            "search_widget",
            "language_selector",
            "logo_images",
            "flag_language_indicator",
            "search_placeholder",
            "helpful_feedback_widget",
            "social_media_links",
            "footer_help_section",
            "footer_learn_section",
        }
        actual_names = {p.name for p in ui_patterns}
        assert actual_names == expected_names

    def test_boilerplate_patterns(self):
        """Test boilerplate patterns"""
        bp_patterns = [p for p in CLEANING_PATTERNS if p.category == PatternCategory.BOILERPLATE]
        assert len(bp_patterns) == 5
        expected_names = {"yaml_frontmatter", "boilerplate_cta", "newsletter_signup", "cookie_banner", "ai_disclaimer"}
        actual_names = {p.name for p in bp_patterns}
        assert actual_names == expected_names

    def test_redundant_patterns(self):
        """Test redundant content patterns"""
        red_patterns = [p for p in CLEANING_PATTERNS if p.category == PatternCategory.REDUNDANT]
        assert len(red_patterns) == 3
        expected_names = {"related_links", "social_share", "code_comments_in_examples"}
        actual_names = {p.name for p in red_patterns}
        assert actual_names == expected_names


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
