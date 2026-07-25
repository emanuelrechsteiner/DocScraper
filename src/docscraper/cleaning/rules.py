"""
Cleaning Rules and Patterns for PostScraperCleaner

This module defines the rule-based patterns used to identify and remove
navigation, UI elements, boilerplate, and redundant content from scraped
documentation markdown files.
"""

import copy
import re
from dataclasses import dataclass, field
from enum import Enum
from re import Pattern


class PatternCategory(Enum):
    """Categories of cleaning patterns"""
    NAVIGATION = "navigation"
    UI = "ui"
    BOILERPLATE = "boilerplate"
    REDUNDANT = "redundant"


@dataclass
class CleaningPattern:
    """Represents a single cleaning pattern with metadata"""
    name: str
    pattern: str
    replacement: str
    confidence: float
    category: PatternCategory
    description: str
    enabled: bool = True
    compiled_pattern: Pattern = field(init=False, repr=False)

    def __post_init__(self):
        """Compile the regex pattern after initialization"""
        try:
            self.compiled_pattern = re.compile(self.pattern, re.MULTILINE | re.DOTALL)
        except re.error as e:
            raise ValueError(f"Invalid regex pattern '{self.name}': {e}")

    def matches(self, content: str) -> int:
        """Count how many matches this pattern finds"""
        return len(self.compiled_pattern.findall(content))

    def apply(self, content: str) -> tuple:
        """Apply this pattern to content. Returns (cleaned_content, number_of_replacements)"""
        result, count = self.compiled_pattern.subn(self.replacement, content)
        return result, count


# Define all cleaning patterns
# NOTE: Patterns updated to be UNIVERSAL, not documentation-specific
# Anthropic-specific patterns removed - intelligent cleaner handles structure
CLEANING_PATTERNS: list[CleaningPattern] = [
    # UNIVERSAL BOILERPLATE PATTERNS (Work on ALL documentation)
    CleaningPattern(
        name="yaml_frontmatter",
        # \A anchors to the document start only — must NOT match body-level
        # '---' horizontal rules (which would devour content between them).
        pattern=r'\A---\s*\n(?:.*?\n)*?---\s*\n',
        replacement="",
        confidence=0.98,
        category=PatternCategory.BOILERPLATE,
        description="Remove YAML frontmatter metadata block"
    ),

    CleaningPattern(
        name="skip_navigation",
        pattern=r'^(?:Skip to (?:main )?content|Jump to content)(?:\s*\n)?',
        replacement="",
        confidence=0.95,
        category=PatternCategory.NAVIGATION,
        description="Remove 'Skip to main content' accessibility links"
    ),

    # GENERIC NAVIGATION PATTERNS (Removed Anthropic-specific ones)
    # NOTE: concatenated_nav_links, header_nav_section removed - too specific to Anthropic
    # Intelligent cleaner will handle navigation menus semantically

    CleaningPattern(
        name="breadcrumbs",
        pattern=r'(?:^|\n)(?:Home\s*[>»/]\s*|[>»/]\s*)+[^\n]+(?:\n|$)',
        replacement="\n",
        confidence=0.85,
        category=PatternCategory.NAVIGATION,
        description="Remove breadcrumb navigation trails (generic pattern)"
    ),

    CleaningPattern(
        name="toc_nav",
        pattern=r'(?:^|\n)(?:##?\s*)?(?:Contents?|TOC)(?:\s*\n)+(?:[-*+]\s+.*\n)+',
        replacement="\n",
        confidence=0.80,
        category=PatternCategory.NAVIGATION,
        description="Remove table of contents sections"
    ),

    # UI ELEMENT PATTERNS
    CleaningPattern(
        name="header_section",
        pattern=r'^(?:---\s*\n)?(?:Header|Top Navigation|Site Header)[\s\S]*?(?:---|\n\n)',
        replacement="",
        confidence=0.88,
        category=PatternCategory.UI,
        description="Remove header sections"
    ),

    CleaningPattern(
        name="footer_section",
        pattern=r'(?:^|\n)(?:---\s*\n)?(?:Footer|Copyright|© \d{4}|All rights reserved)[\s\S]*?(?:$|\n---)',
        replacement="\n",
        confidence=0.90,
        category=PatternCategory.UI,
        description="Remove footer sections and copyright notices"
    ),

    CleaningPattern(
        name="mobile_menu",
        pattern=r'(?:^|\n)(?:☰|≡|Menu)\s*(?:Open|Close)?\s*(?:Menu|Navigation)?(?:\n|$)',
        replacement="\n",
        confidence=0.92,
        category=PatternCategory.UI,
        description="Remove mobile menu toggle buttons"
    ),

    CleaningPattern(
        name="search_widget",
        pattern=r'(?:^|\n)(?:Search|🔍)\s*(?:documentation|site|docs)?\s*\[.*?\]\(.*?\)(?:\n|$)',
        replacement="\n",
        confidence=0.85,
        category=PatternCategory.UI,
        description="Remove search box widgets"
    ),

    CleaningPattern(
        name="language_selector",
        pattern=r'(?:^|\n)(?:Language|🌐):\s*\[.*?\]\(.*?\)(?:\s*\|.*?\(.*?\))*(?:\n|$)',
        replacement="\n",
        confidence=0.88,
        category=PatternCategory.UI,
        description="Remove language selection dropdowns"
    ),

    CleaningPattern(
        name="navigation_link_row",
        pattern=r'(?:^|\n)(?:Navigation|Nav|Menu):[ \t]*(?:\[[^\]]*\]\([^)]*\)[ \t]*)+(?=\n|$)',
        replacement="\n",
        confidence=0.9,
        category=PatternCategory.NAVIGATION,
        description="Remove 'Navigation:'-prefixed rows of inline links"
    ),

    # BOILERPLATE PATTERNS
    CleaningPattern(
        name="boilerplate_cta",
        pattern=r'(?:^|\n)(?:##?\s*)?(?:Get Started|Try (?:it )?Now|Sign Up|Subscribe|Join|Contact Us)(?:\s*\n)+(?:[^\n]+\n)*?\[.+?\]\(.+?\)',
        replacement="\n",
        confidence=0.75,
        category=PatternCategory.BOILERPLATE,
        description="Remove call-to-action sections"
    ),

    CleaningPattern(
        name="newsletter_signup",
        pattern=r'(?:^|\n)(?:##?\s*)?(?:Newsletter|Stay Updated|Email Updates)(?:\s*\n)+(?:[^\n]*(?:subscribe|sign up|email)[^\n]*\n)+',
        replacement="\n",
        confidence=0.82,
        category=PatternCategory.BOILERPLATE,
        description="Remove newsletter signup forms"
    ),

    CleaningPattern(
        name="cookie_banner",
        pattern=r'(?:^|\n)(?:This (?:site|website) uses cookies|Cookie (?:Policy|Notice)|We use cookies)[\s\S]{0,200}?\[.*?(?:Accept|Agree).*?\]',
        replacement="\n",
        confidence=0.93,
        category=PatternCategory.BOILERPLATE,
        description="Remove cookie consent banners"
    ),

    # REDUNDANT CONTENT
    CleaningPattern(
        name="related_links",
        pattern=r'(?:^|\n)(?:##?\s*)?(?:Related|See Also|Further Reading|More Information)(?:\s*\n)+(?:[-*+]\s+\[.+?\]\(.+?\)\s*\n)+',
        replacement="\n",
        confidence=0.70,
        category=PatternCategory.REDUNDANT,
        description="Remove 'Related' or 'See Also' link sections"
    ),

    CleaningPattern(
        name="social_share",
        pattern=r'(?:^|\n)(?:Share(?:\s+this)?|Follow us):\s*(?:\[.*?\]\(.*?\)\s*)+(?:\n|$)',
        replacement="\n",
        confidence=0.87,
        category=PatternCategory.REDUNDANT,
        description="Remove social sharing buttons"
    ),

    # NOTE: "On this page" TOC, category breadcrumbs, copy buttons removed from patterns
    # Intelligent cleaner will decide whether to keep or remove based on semantic analysis

    # NOTE: Banner announcements pattern too specific - let intelligent cleaner handle
    # CleaningPattern(
    #     name="banner_announcement",
    #     pattern=r'(?:^|\n)(?:Agent Skills|New feature|Update|Announcement)[^!]*![^\]]*\]\([^\)]+\)\s*\.',
    #     replacement="\n",
    #     confidence=0.75,
    #     category=PatternCategory.UI,
    #     description="Remove banner announcements with links"
    # ),

    CleaningPattern(
        name="logo_images",
        pattern=r'\[[^\n]{0,100}!\[(?:light|dark) logo\]\([^\)]+\)[^\n]{0,100}\]\([^\)]+\)',
        replacement="",
        confidence=0.95,
        category=PatternCategory.UI,
        description="Remove site logo image links"
    ),

    CleaningPattern(
        name="flag_language_indicator",
        pattern=r'!\[(?:US|UK|EU|[A-Z]{2})\]\([^\)]*flags/[^\)]+\)\s*\n?(?:English|Deutsch|Français|Español|中文)?',
        replacement="\n",
        confidence=0.88,
        category=PatternCategory.UI,
        description="Remove country flag and language indicator"
    ),

    CleaningPattern(
        name="search_placeholder",
        pattern=r'(?:^|\n)Search\.\.\.\s*\n?(?:⌘K)?\s*\n?',
        replacement="\n",
        confidence=0.90,
        category=PatternCategory.UI,
        description="Remove search placeholder text and keyboard shortcuts"
    ),

    CleaningPattern(
        name="helpful_feedback_widget",
        pattern=r'(?:^|\n)Was this page helpful\?\s*\n?(?:Yes)?(?:No)?\s*\n?',
        replacement="\n",
        confidence=0.93,
        category=PatternCategory.UI,
        description="Remove 'Was this page helpful?' feedback widget"
    ),

    CleaningPattern(
        name="prev_next_navigation",
        pattern=r'(?:^|\n)\[(?:Previous|Next|←|→).*?\]\([^\)]+\)\[(?:Previous|Next|←|→).*?\]\([^\)]+\)',
        replacement="\n",
        confidence=0.88,
        category=PatternCategory.NAVIGATION,
        description="Remove previous/next page navigation links"
    ),

    CleaningPattern(
        name="ai_disclaimer",
        pattern=r'(?:^|\n)(?:Assistant|AI|Bot)\s*\n?(?:Responses are generated using AI and may contain mistakes\.|This is an AI assistant\.)',
        replacement="\n",
        confidence=0.90,
        category=PatternCategory.BOILERPLATE,
        description="Remove AI/Assistant disclaimer messages"
    ),

    # Additional Footer Patterns
    CleaningPattern(
        name="social_media_links",
        pattern=r'(?:^|\n)\[(?:x|twitter|linkedin|facebook|github|discord)\]\([^\)]+\)(?:\[(?:x|twitter|linkedin|facebook|github|discord)\]\([^\)]+\))*',
        replacement="\n",
        confidence=0.89,
        category=PatternCategory.UI,
        description="Remove social media icon links"
    ),

    CleaningPattern(
        name="footer_help_section",
        pattern=r'Help and security\s*\n(?:\[.+?\]\(.+?\)\s*)+',
        replacement="\n",
        confidence=0.87,
        category=PatternCategory.UI,
        description="Remove footer help and security links section"
    ),

    CleaningPattern(
        name="footer_learn_section",
        pattern=r'Learn\s*\n(?:\[.+?\]\(.+?\)\s*)+',
        replacement="\n",
        confidence=0.87,
        category=PatternCategory.UI,
        description="Remove footer learn section with links"
    ),

    # NOTE: Removed footer-specific patterns (footer_company_links, footer_help_section,
    # footer_learn_section, footer_terms_section, next_steps_cards, footer_diagram_images)
    # These are too specific to certain documentation structures
    # Intelligent cleaner will identify and remove footer sections semantically

    # Cleanup patterns for leftover fragments (generic)
    CleaningPattern(
        name="broken_link_fragments",
        pattern=r'(?:^|\n)\]\([^\)]+\)\s*\n',
        replacement="\n",
        confidence=0.85,
        category=PatternCategory.NAVIGATION,
        description="Remove broken link fragments like ](url)"
    ),

    # NOTE: Removed orphaned_nav_text and orphaned_list_items - too specific
    # Intelligent cleaner will handle these semantically

    CleaningPattern(
        name="code_comments_in_examples",
        pattern=r'\n//\s+Additional\s+(?:thinking|text)\s+deltas\.\.\.\s*\n',
        replacement="\n",
        confidence=0.90,
        category=PatternCategory.REDUNDANT,
        description="Remove placeholder comments in code examples"
    ),
]


class PatternRegistry:
    """Registry for managing cleaning patterns"""

    def __init__(self, patterns: list[CleaningPattern] = None):
        """Initialize registry with patterns.

        Patterns are deep-copied so each registry owns independent instances.
        Toggling ``pattern.enabled`` on one registry/cleaner must never leak
        into the shared module-level defaults or another instance.
        """
        source = patterns if patterns is not None else CLEANING_PATTERNS
        self.patterns = [copy.deepcopy(p) for p in source]
        self._pattern_map = {p.name: p for p in self.patterns}

    def get_pattern(self, name: str) -> CleaningPattern:
        """Get a specific pattern by name"""
        return self._pattern_map.get(name)

    def get_enabled_patterns(self) -> list[CleaningPattern]:
        """Get all enabled patterns"""
        return [p for p in self.patterns if p.enabled]

    def get_patterns_by_category(self, category: PatternCategory) -> list[CleaningPattern]:
        """Get all patterns in a specific category"""
        return [p for p in self.patterns if p.category == category]

    def get_patterns_by_confidence(self, min_confidence: float) -> list[CleaningPattern]:
        """Get patterns above a confidence threshold"""
        return [p for p in self.patterns if p.confidence >= min_confidence]

    def enable_pattern(self, name: str) -> bool:
        """Enable a specific pattern by name"""
        pattern = self._pattern_map.get(name)
        if pattern:
            pattern.enabled = True
            return True
        return False

    def disable_pattern(self, name: str) -> bool:
        """Disable a specific pattern by name"""
        pattern = self._pattern_map.get(name)
        if pattern:
            pattern.enabled = False
            return True
        return False

    def get_statistics(self) -> dict:
        """Get statistics about patterns in the registry"""
        enabled = len(self.get_enabled_patterns())
        by_category = {}
        for category in PatternCategory:
            by_category[category.value] = len(self.get_patterns_by_category(category))

        return {
            "total_patterns": len(self.patterns),
            "enabled_patterns": enabled,
            "disabled_patterns": len(self.patterns) - enabled,
            "by_category": by_category,
            "average_confidence": sum(p.confidence for p in self.patterns) / len(self.patterns)
        }


# Default pattern registry instance
DEFAULT_REGISTRY = PatternRegistry()
