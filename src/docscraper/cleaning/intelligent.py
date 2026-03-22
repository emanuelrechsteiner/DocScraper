"""
Intelligent Content Analysis using LLM Semantic Understanding

This module provides LLM-powered semantic analysis to identify main documentation
content vs. navigation/boilerplate on ANY documentation source.

Unlike rule-based patterns, this uses semantic understanding to work across
different documentation structures (Anthropic, Python, React, Stripe, etc.)
"""

import json
import logging
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from pathlib import Path

from .llm import LLMValidator, LLMConfig

logger = logging.getLogger(__name__)


@dataclass
class ContentSection:
    """Represents a section of content with type and boundaries"""
    section_type: str  # "main_content", "navigation", "header", "footer", "sidebar", "toc"
    start_line: int
    end_line: int
    reason: str
    confidence: float = 1.0

    def line_count(self) -> int:
        """Get number of lines in this section"""
        return self.end_line - self.start_line + 1


@dataclass
class ContentAnalysis:
    """Result of LLM semantic content analysis"""
    main_content_start: int
    main_content_end: int
    sections_to_remove: List[ContentSection] = field(default_factory=list)
    sections_to_keep: List[ContentSection] = field(default_factory=list)
    confidence: float = 0.0
    analysis_cost: float = 0.0

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization"""
        return {
            "main_content_start": self.main_content_start,
            "main_content_end": self.main_content_end,
            "sections_to_remove": [
                {
                    "type": s.section_type,
                    "start": s.start_line,
                    "end": s.end_line,
                    "reason": s.reason,
                    "line_count": s.line_count()
                }
                for s in self.sections_to_remove
            ],
            "sections_to_keep": [
                {
                    "type": s.section_type,
                    "start": s.start_line,
                    "end": s.end_line,
                    "reason": s.reason,
                    "line_count": s.line_count()
                }
                for s in self.sections_to_keep
            ],
            "confidence": round(self.confidence, 3),
            "analysis_cost": round(self.analysis_cost, 6),
        }


class IntelligentContentAnalyzer:
    """
    LLM-powered semantic content analyzer

    Uses GPT-4o-mini to semantically identify main documentation content
    vs. navigation, headers, footers, and boilerplate.

    Works on any documentation source without hardcoded patterns.
    """

    def __init__(self, llm_config: Optional[LLMConfig] = None):
        """Initialize with LLM configuration"""
        self.llm_config = llm_config or LLMConfig(
            model="gpt-4o",
            temperature=0.1,
            max_tokens=1500,
            rate_limit_rpm=500
        )
        self.llm_validator = LLMValidator(self.llm_config)
        self._last_api_cost = 0.0

        self.stats = {
            "analyses_requested": 0,
            "analyses_successful": 0,
            "analyses_failed": 0,
            "total_cost": 0.0,
            "total_lines_analyzed": 0,
            "total_lines_removed": 0,
        }

    def analyze_structure(self, content: str, filename: str = "") -> ContentAnalysis:
        """
        Analyze document structure using LLM semantic understanding.

        Returns ContentAnalysis with identified boundaries and sections.
        """
        self.stats["analyses_requested"] += 1

        lines = content.split('\n')
        total_lines = len(lines)
        self.stats["total_lines_analyzed"] += total_lines

        logger.info(f"Analyzing structure of {filename} ({total_lines} lines)")

        # Build semantic analysis prompt
        prompt = self._build_analysis_prompt(content, total_lines)

        # Call LLM
        try:
            result = self._call_llm_for_analysis(prompt)
            self.stats["analyses_successful"] += 1
            self.stats["total_cost"] += result.analysis_cost

            # Calculate removed lines
            for section in result.sections_to_remove:
                self.stats["total_lines_removed"] += section.line_count()

            logger.info(f"Analysis complete: main content lines {result.main_content_start}-{result.main_content_end}")
            logger.info(f"Identified {len(result.sections_to_remove)} sections to remove")

            return result

        except Exception as e:
            self.stats["analyses_failed"] += 1
            logger.error(f"Analysis failed: {e}")
            return self._fallback_analysis(total_lines)

    def extract_main_content(self, content: str, analysis: ContentAnalysis) -> str:
        """
        Extract main content based on LLM analysis.

        Removes identified navigation, headers, footers, and boilerplate.
        Preserves main content and any sections marked as useful (like TOC).
        """
        lines = content.split('\n')

        # Convert from 1-indexed (LLM) to 0-indexed (Python)
        # LLM sees "  37: # Title" and returns 37, we need index 36
        main_start = max(0, analysis.main_content_start - 1)
        main_end = min(len(lines) - 1, analysis.main_content_end - 1)

        # Get main content lines (inclusive of both start and end)
        result_lines = lines[main_start:main_end + 1]

        # Remove any sections within main content that were identified
        for section in analysis.sections_to_remove:
            # Convert section boundaries from 1-indexed to 0-indexed
            section_start = section.start_line - 1
            section_end = section.end_line - 1

            # Only remove if section is within our extracted range
            if section_start >= main_start and section_end <= main_end:
                # Calculate relative position in result_lines
                rel_start = section_start - main_start
                rel_end = section_end - main_start + 1

                # Mark lines for removal with None
                for i in range(rel_start, rel_end):
                    if 0 <= i < len(result_lines):
                        result_lines[i] = None

        # Filter out removed lines
        result_lines = [line for line in result_lines if line is not None]

        return '\n'.join(result_lines)

    def _build_analysis_prompt(self, content: str, total_lines: int) -> str:
        """Build prompt for LLM semantic analysis"""

        # Get preview with LINE NUMBERS for accuracy
        lines = content.split('\n')

        preview_sections = []

        # First 100 lines WITH LINE NUMBERS
        if len(lines) > 100:
            preview_sections.append("=== BEGINNING (lines 1-100) ===")
            numbered_lines = [f"{i+1:4d}: {line}" for i, line in enumerate(lines[:100])]
            preview_sections.append('\n'.join(numbered_lines))
        else:
            preview_sections.append(f"=== ENTIRE DOCUMENT (lines 1-{len(lines)}) ===")
            numbered_lines = [f"{i+1:4d}: {line}" for i, line in enumerate(lines)]
            preview_sections.append('\n'.join(numbered_lines))

        # Middle section WITH LINE NUMBERS
        if len(lines) > 200:
            mid_start = len(lines) // 2 - 25
            mid_end = mid_start + 50
            preview_sections.append(f"\n=== MIDDLE (lines {mid_start+1}-{mid_end}) ===")
            numbered_lines = [f"{mid_start+i+1:4d}: {line}" for i, line in enumerate(lines[mid_start:mid_end])]
            preview_sections.append('\n'.join(numbered_lines))

        # End section WITH LINE NUMBERS
        if len(lines) > 150:
            start_line = len(lines) - 50
            preview_sections.append(f"\n=== END (lines {start_line+1}-{len(lines)}) ===")
            numbered_lines = [f"{start_line+i+1:4d}: {line}" for i, line in enumerate(lines[-50:])]
            preview_sections.append('\n'.join(numbered_lines))

        preview = '\n'.join(preview_sections)

        prompt = f"""Analyze this scraped documentation markdown and identify content boundaries.

DOCUMENT INFO:
- Total lines: {total_lines}
- Filename: (scraped documentation)

CONTENT PREVIEW (with line numbers):
{preview}

TASK:
Identify where the main documentation content starts and ends by specifying EXACT LINE NUMBERS.

CRITICAL RULES FOR FINDING MAIN CONTENT START:
1. **Look for the FIRST markdown heading (# or ## or ###)** - this is usually where the main content title begins
2. Main content MUST start at or BEFORE the first H1/H2 heading, NEVER after it
3. Lines with just markdown link lists like "[Link Text](url)" are navigation menus, NOT main content
4. Lines with "Search", "Toggle theme", social media icons, "Discord", "GitHub" are header UI elements
5. Multiple consecutive lines of links in a hierarchical structure are sidebar navigation menus
6. YAML frontmatter (between --- markers) is metadata, not content

EXAMPLES:
- "# Package Search MCP Server" ← Main content STARTS HERE (at this line)
- "## Getting Started" ← Main content STARTS HERE if this is the first heading
- "[Overview](link)" repeated many times ← This is NAVIGATION, remove it
- "Search⌘K" or "Toggle theme" ← This is HEADER UI, remove it

DEFINITIONS:
- Main content: Technical documentation, tutorials, API reference, guides, explanations, code examples, INCLUDING THE TITLE HEADING
- NOT main content: Site navigation menus, headers with logos/search/login, footers with company links, sidebars, breadcrumbs, social media links, YAML frontmatter

IMPORTANT:
- INCLUDE the first H1 heading (# Title) as part of main content
- If unsure, err on the side of KEEPING content (set start earlier rather than later)
- "On this page" TOC after the title can be kept if it's useful
- Footer usually starts with links like "Edit this page" or "Previous/Next" navigation

RETURN JSON:
{{
  "main_content_start": <line_number>,
  "main_content_end": <line_number>,
  "sections_to_remove": [
    {{"type": "header", "start": X, "end": Y, "reason": "site logo and top navigation"}},
    {{"type": "sidebar", "start": X, "end": Y, "reason": "hierarchical menu of other docs"}},
    {{"type": "footer", "start": X, "end": Y, "reason": "company links and social media"}}
  ],
  "sections_to_keep": [
    {{"type": "toc", "start": X, "end": Y, "reason": "on this page navigation is useful"}},
    {{"type": "category", "start": X, "end": Y, "reason": "category label before heading"}}
  ],
  "confidence": 0.0-1.0
}}

Only output valid JSON, no other text."""

        return prompt

    def _call_openai_for_analysis(self, prompt: str) -> str:
        """Call OpenAI API and return raw response text"""
        from urllib.request import Request, urlopen
        import json as json_lib

        # Prepare request
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.llm_validator.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.llm_validator.config.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.llm_validator.config.temperature,
            "max_tokens": self.llm_validator.config.max_tokens,
        }

        request = Request(
            url, data=json_lib.dumps(payload).encode(), headers=headers, method="POST"
        )

        try:
            with urlopen(request, timeout=30) as response:
                data = json_lib.loads(response.read().decode())

                # Extract response text
                response_text = data["choices"][0]["message"]["content"]

                # Calculate cost and store it
                usage = data.get("usage", {})
                input_tokens = usage.get("prompt_tokens", 0)
                output_tokens = usage.get("completion_tokens", 0)
                self._last_api_cost = self.llm_validator._calculate_cost(input_tokens, output_tokens)

                return response_text

        except Exception as e:
            raise ValueError(f"API request failed: {e}")

    def _call_llm_for_analysis(self, prompt: str) -> ContentAnalysis:
        """Call LLM and parse structured response"""

        # Call OpenAI API directly (not using the validator's method)
        response_text = self._call_openai_for_analysis(prompt)

        # Parse JSON response
        try:
            # DEBUG: Log the actual response
            logger.debug(f"LLM Response (first 500 chars): {response_text[:500]}")

            # Try to find JSON in response
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1

            if json_start >= 0 and json_end > json_start:
                json_text = response_text[json_start:json_end]
                data = json.loads(json_text)
            else:
                logger.error(f"No JSON found. Response text: {response_text}")
                raise ValueError("No JSON found in response")

            # Parse sections
            sections_to_remove = []
            for section_data in data.get("sections_to_remove", []):
                sections_to_remove.append(ContentSection(
                    section_type=section_data.get("type", "unknown"),
                    start_line=int(section_data.get("start", 0)),
                    end_line=int(section_data.get("end", 0)),
                    reason=section_data.get("reason", "")
                ))

            sections_to_keep = []
            for section_data in data.get("sections_to_keep", []):
                sections_to_keep.append(ContentSection(
                    section_type=section_data.get("type", "unknown"),
                    start_line=int(section_data.get("start", 0)),
                    end_line=int(section_data.get("end", 0)),
                    reason=section_data.get("reason", "")
                ))

            analysis = ContentAnalysis(
                main_content_start=int(data.get("main_content_start", 0)),
                main_content_end=int(data.get("main_content_end", 999999)),
                sections_to_remove=sections_to_remove,
                sections_to_keep=sections_to_keep,
                confidence=float(data.get("confidence", 0.8)),
                analysis_cost=getattr(self, '_last_api_cost', 0.0)
            )

            return analysis

        except (json.JSONDecodeError, ValueError, KeyError) as e:
            logger.error(f"Failed to parse LLM response: {e}")
            logger.debug(f"Response was: {response_text[:500]}")
            raise ValueError(f"Invalid LLM response format: {e}")

    def _fallback_analysis(self, total_lines: int) -> ContentAnalysis:
        """Fallback when LLM analysis fails"""
        logger.warning("Using fallback analysis (no LLM)")

        # Conservative fallback: assume main content is most of the document
        # Skip first 20% (likely headers/nav) and last 10% (likely footer)
        start = int(total_lines * 0.2)
        end = int(total_lines * 0.9)

        return ContentAnalysis(
            main_content_start=start,
            main_content_end=end,
            confidence=0.5,
            sections_to_remove=[
                ContentSection("header", 0, start - 1, "Fallback: assumed header"),
                ContentSection("footer", end + 1, total_lines - 1, "Fallback: assumed footer")
            ]
        )

    def get_statistics(self) -> Dict:
        """Get analyzer statistics"""
        stats = self.stats.copy()

        if stats["analyses_requested"] > 0:
            stats["success_rate"] = stats["analyses_successful"] / stats["analyses_requested"]
            stats["avg_cost_per_doc"] = stats["total_cost"] / stats["analyses_successful"] if stats["analyses_successful"] > 0 else 0
        else:
            stats["success_rate"] = 0.0
            stats["avg_cost_per_doc"] = 0.0

        if stats["total_lines_analyzed"] > 0:
            stats["removal_percentage"] = (stats["total_lines_removed"] / stats["total_lines_analyzed"]) * 100
        else:
            stats["removal_percentage"] = 0.0

        return stats
