"""
Cleaning Rules and Patterns for PostScraperCleaner

This module defines the rule-based patterns used to identify and remove
navigation, UI elements, boilerplate, and redundant content from scraped
documentation markdown files.
"""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Pattern
from enum import Enum


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
CLEANING_PATTERNS: List[CleaningPattern] = [
    # NAVIGATION PATTERNS
    CleaningPattern(
        name="skip_navigation",
        pattern=r'^(?:Skip to (?:main )?content|Jump to content)(?:\s*\n)?',
        replacement="",
        confidence=0.95,
        category=PatternCategory.NAVIGATION,
        description="Remove 'Skip to main content' accessibility links"
    ),

    CleaningPattern(
        name="breadcrumbs",
        pattern=r'(?:^|\n)(?:Home\s*[>»/]\s*|[>»/]\s*)+[^\n]+(?:\n|$)',
        replacement="\n",
        confidence=0.90,
        category=PatternCategory.NAVIGATION,
        description="Remove breadcrumb navigation trails"
    ),

    CleaningPattern(
        name="sidebar_menu",
        pattern=r'(?:^|\n)(?:##?\s*)?(?:Table of Contents|On This Page|In This Section|Navigation|Menu)(?:\s*\n)+(?:[-*+]\s+\[.+?\]\(.+?\)\s*\n)+',
        replacement="\n",
        confidence=0.85,
        category=PatternCategory.NAVIGATION,
        description="Remove sidebar navigation menus"
    ),

    CleaningPattern(
        name="concatenated_nav_links",
        pattern=r'(?:^|\n)\[(?:Home|Docs|Documentation|API|Guide|Overview|Resources|Console|Support)\]\([^\)]+\)(?:\[.+?\]\([^\)]+\)){2,}',
        replacement="\n",
        confidence=0.88,
        category=PatternCategory.NAVIGATION,
        description="Remove concatenated navigation links on single lines"
    ),

    CleaningPattern(
        name="header_nav_section",
        pattern=r'(?:English|Deutsch|Français)\s*\n\s*Search\.\.\.\s*\n.*?(?:\[Console\]|\[Support\]|\[Discord\]|\[Sign up\]|\[Login\]).*?(?:\n\s*\n)',
        replacement="\n",
        confidence=0.85,
        category=PatternCategory.NAVIGATION,
        description="Remove header navigation with language/search/login"
    ),

    CleaningPattern(
        name="footer_company_links",
        pattern=r'Company\s*\n(?:\[.+?\]\(.+?\)\s*\n?){3,}',
        replacement="\n",
        confidence=0.87,
        category=PatternCategory.UI,
        description="Remove footer company link sections"
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

    # Additional Navigation Patterns
    CleaningPattern(
        name="on_this_page_toc",
        pattern=r'(?:^|\n)On this page\s*\n(?:\s*\*\s+\[.+?\]\(.+?\)\s*\n)+',
        replacement="\n",
        confidence=0.92,
        category=PatternCategory.NAVIGATION,
        description="Remove 'On this page' table of contents with anchor links"
    ),

    CleaningPattern(
        name="nested_nav_sections",
        pattern=r'(?:^|\n)#{2,5}\s*(?:First steps|Models? (?:&|and) pricing|Build with|Capabilities|Tools|Agent (?:Skills|SDK)|MCP|Prompt engineering|Test (?:&|and) evaluate|Strengthen guardrails|Administration|Claude on).*?\n(?:\s*\*\s+\[.+?\]\(.+?\)\s*\n)+',
        replacement="\n",
        confidence=0.85,
        category=PatternCategory.NAVIGATION,
        description="Remove nested navigation menu sections with headers"
    ),

    CleaningPattern(
        name="category_breadcrumb",
        pattern=r'(?:^|\n)(?:Capabilities|Features|API Reference|Documentation|Developer Guide|Resources)\s*\n(?=\s*#)',
        replacement="\n",
        confidence=0.80,
        category=PatternCategory.NAVIGATION,
        description="Remove single-word category breadcrumb before main heading"
    ),

    # Additional UI Patterns
    CleaningPattern(
        name="copy_page_button",
        pattern=r'(?:^|\n)Copy page\s*\n?',
        replacement="\n",
        confidence=0.90,
        category=PatternCategory.UI,
        description="Remove 'Copy page' action buttons"
    ),

    CleaningPattern(
        name="banner_announcement",
        pattern=r'(?:^|\n)(?:Agent Skills|New feature|Update|Announcement)[^!]*![^\]]*\]\([^\)]+\)\s*\.',
        replacement="\n",
        confidence=0.75,
        category=PatternCategory.UI,
        description="Remove banner announcements with links"
    ),

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

    CleaningPattern(
        name="footer_terms_section",
        pattern=r'Terms and policies\s*\n(?:\[.+?\]\(.+?\)\s*\n?){2,}',
        replacement="\n",
        confidence=0.90,
        category=PatternCategory.UI,
        description="Remove footer terms and policies section"
    ),
]


class PatternRegistry:
    """Registry for managing cleaning patterns"""

    def __init__(self, patterns: List[CleaningPattern] = None):
        """Initialize registry with patterns"""
        self.patterns = patterns if patterns is not None else CLEANING_PATTERNS.copy()
        self._pattern_map = {p.name: p for p in self.patterns}

    def get_pattern(self, name: str) -> CleaningPattern:
        """Get a specific pattern by name"""
        return self._pattern_map.get(name)

    def get_enabled_patterns(self) -> List[CleaningPattern]:
        """Get all enabled patterns"""
        return [p for p in self.patterns if p.enabled]

    def get_patterns_by_category(self, category: PatternCategory) -> List[CleaningPattern]:
        """Get all patterns in a specific category"""
        return [p for p in self.patterns if p.category == category]

    def get_patterns_by_confidence(self, min_confidence: float) -> List[CleaningPattern]:
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

    def get_statistics(self) -> Dict:
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
