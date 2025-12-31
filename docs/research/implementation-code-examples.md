# PostScraperCleaning - Implementation Code Examples

**Research Agent - Supplementary Document**  
**Date:** 2025-01-28

This document provides production-ready code examples for implementing the PostScraperCleaning processor.

---

## 1. Complete PreCleaner Implementation

```python
# src/post_scraper_cleaning/pre_cleaner.py

import re
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class PreCleaner:
    """
    Rule-based pre-cleaner for HTML documents.
    Removes obvious boilerplate and converts to markdown.
    """
    
    # CSS selectors for common boilerplate elements
    REMOVE_SELECTORS = [
        'nav', 'footer', 'header',
        '.navigation', '.navbar', '.nav',
        '.sidebar', '.side-nav', '.toc',
        '.breadcrumb', '.breadcrumbs',
        '.footer', '.page-footer',
        '.cookie-banner', '.cookie-notice',
        '.social-share', '.share-buttons',
        '.newsletter', '.subscribe',
        '.advertisement', '.ad', '.ads',
        '.related-posts', '.related-articles',
        '.comments', '.comment-section',
        '.pagination',
        '#navigation', '#footer', '#header', '#sidebar'
    ]
    
    # Common boilerplate text patterns
    REMOVE_PATTERNS = [
        r'^(Skip to|Jump to|Back to top)',
        r'(Edit this page|Suggest changes|Report (an? )?issue)',
        r'(Share on|Tweet|Share via)',
        r'Copyright \d{4}',
        r'Last updated:.*',
        r'Was this (page|article) helpful\?',
        r'Table of Contents',
        r'On this page',
        r'In this (article|section)',
        r'^\s*\|\s*$',  # Empty table cells
    ]
    
    def clean(self, html: str, url: str) -> Dict:
        """
        Pre-clean HTML document using rule-based approach.
        
        Args:
            html: Raw HTML content
            url: Source URL (for logging/metadata)
            
        Returns:
            Dict with pre-cleaned content and metadata
        """
        try:
            # Parse HTML
            soup = BeautifulSoup(html, 'html.parser')
            
            # Extract metadata before cleaning
            metadata = self._extract_basic_metadata(soup, url)
            
            # Remove script and style tags
            for tag in soup(['script', 'style', 'noscript']):
                tag.decompose()
            
            # Remove boilerplate elements by selector
            removed_elements = []
            for selector in self.REMOVE_SELECTORS:
                elements = soup.select(selector)
                for elem in elements:
                    elem.decompose()
                if elements:
                    removed_elements.append(selector)
            
            # Convert to markdown
            markdown = md(str(soup), heading_style="ATX", code_language_callback=self._detect_code_language)
            
            # Clean markdown text
            cleaned_markdown = self._clean_markdown_text(markdown)
            
            return {
                "content": cleaned_markdown,
                "metadata": metadata,
                "removed_elements": list(set(removed_elements))
            }
            
        except Exception as e:
            logger.error(f"Pre-cleaning failed for {url}: {e}")
            return {
                "content": html,
                "metadata": {"url": url},
                "removed_elements": [],
                "error": str(e)
            }
    
    def _extract_basic_metadata(self, soup: BeautifulSoup, url: str) -> Dict:
        """Extract basic metadata from HTML"""
        # Try to find title
        title = None
        if soup.title:
            title = soup.title.string
        elif soup.find('h1'):
            title = soup.find('h1').get_text(strip=True)
        
        # Try to find description
        description = None
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            description = meta_desc.get('content')
        
        # Try to find keywords
        keywords = []
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        if meta_keywords:
            keywords = [k.strip() for k in meta_keywords.get('content', '').split(',')]
        
        return {
            "url": url,
            "title": title,
            "description": description,
            "keywords": keywords,
            "has_code": bool(soup.find(['code', 'pre'])),
            "has_table": bool(soup.find('table'))
        }
    
    def _detect_code_language(self, el) -> Optional[str]:
        """Detect programming language from code block class"""
        classes = el.get('class', [])
        for cls in classes:
            # Common patterns: language-python, lang-js, hljs-python
            if cls.startswith('language-'):
                return cls.replace('language-', '')
            elif cls.startswith('lang-'):
                return cls.replace('lang-', '')
            elif cls.startswith('hljs-'):
                return cls.replace('hljs-', '')
        return None
    
    def _clean_markdown_text(self, markdown: str) -> str:
        """Clean markdown text using regex patterns"""
        lines = markdown.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Skip lines matching removal patterns
            should_skip = False
            for pattern in self.REMOVE_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    should_skip = True
                    break
            
            if not should_skip:
                cleaned_lines.append(line)
        
        # Join and clean up excessive whitespace
        text = '\n'.join(cleaned_lines)
        
        # Remove excessive blank lines (more than 2 consecutive)
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Remove trailing whitespace from lines
        text = '\n'.join(line.rstrip() for line in text.split('\n'))
        
        return text.strip()


# Example usage
if __name__ == "__main__":
    pre_cleaner = PreCleaner()
    
    sample_html = """
    <html>
    <head><title>Getting Started with Firebase</title></head>
    <body>
        <nav>Home | Docs | API</nav>
        
        <h1>Getting Started with Firebase</h1>
        
        <p>Firebase is a comprehensive platform for building mobile and web applications.</p>
        
        <h2>Installation</h2>
        
        <pre><code class="language-bash">npm install firebase</code></pre>
        
        <footer>&copy; 2024 Firebase</footer>
    </body>
    </html>
    """
    
    result = pre_cleaner.clean(sample_html, "https://firebase.google.com/docs")
    print(result["content"])
```

---

## 2. Complete LLMCleaner Implementation

```python
# src/post_scraper_cleaning/llm_cleaner.py

import asyncio
import json
import logging
import time
from typing import Dict, Optional
from openai import AsyncOpenAI, OpenAIError
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class LLMCleaningConfig:
    """Configuration for LLM-based cleaning"""
    model: str = "gpt-4o-mini"
    temperature: float = 0.1
    max_tokens: int = 4096
    timeout: int = 60
    max_retries: int = 3
    retry_delay: int = 2

class LLMCleaner:
    """
    LLM-based document cleaner using OpenAI API.
    Refines pre-cleaned documents for optimal embedding quality.
    """
    
    SYSTEM_PROMPT = """You are a specialized technical documentation cleaning assistant. Your task is to prepare scraped documentation for vector database storage and semantic search.

OBJECTIVES:
1. Remove navigation and boilerplate elements while preserving ALL technical content
2. Maintain semantic structure with proper markdown hierarchy
3. Extract accurate metadata
4. Format content optimally for embedding models

REMOVAL RULES:
Remove these elements:
- Navigation menus, sidebars, breadcrumbs
- Headers and footers (copyright, legal, contact)
- Promotional content, ads, newsletter signups
- "Edit this page", "Was this helpful?" prompts
- Social sharing buttons
- Page metadata (last updated, edit history) unless technically relevant
- Duplicate headings (same text repeated)

PRESERVATION RULES:
MUST preserve:
- ALL technical content, explanations, and descriptions
- Code examples with language identifiers
- API references, method signatures, parameters
- Tables with structured data
- Lists (ordered and unordered)
- Blockquotes (notes, warnings, tips)
- Inline links to related documentation
- Technical diagrams and their descriptions
- Version requirements and compatibility notes
- Error messages and troubleshooting steps

FORMATTING RULES:
1. Use hierarchical markdown headings (# for title, ## for sections, ### for subsections)
2. One H1 (#) per document - the main title
3. Don't skip heading levels
4. Preserve code blocks exactly with language identifiers
5. Keep inline code with backticks
6. Preserve table structure
7. Use blockquotes for notes/warnings

CRITICAL RULES:
❌ NEVER modify technical content (code, API names, commands)
❌ NEVER paraphrase or rewrite technical information
❌ NEVER remove code examples or technical details
❌ NEVER hallucinate information not present in source
✅ ONLY remove structural/navigational elements
✅ PRESERVE exact technical accuracy
✅ MAINTAIN all context needed for understanding

OUTPUT FORMAT:
Respond with valid JSON:
{
  "title": "string",
  "description": "string (1-2 sentences)",
  "category": "string",
  "subcategory": "string or null",
  "cleaned_content": "markdown string",
  "removed_elements": ["array", "of", "removed", "element", "types"],
  "metadata": {
    "has_code": boolean,
    "code_languages": ["array"],
    "has_table": boolean,
    "heading_count": number,
    "word_count": number
  }
}"""
    
    def __init__(self, config: LLMCleaningConfig):
        self.config = config
        self.client = AsyncOpenAI()
    
    async def clean(self, pre_cleaned_content: str, url: str = "") -> Dict:
        """
        Clean pre-processed content using LLM.
        
        Args:
            pre_cleaned_content: Pre-cleaned markdown content
            url: Source URL (for logging)
            
        Returns:
            Dict with cleaned content and metadata
        """
        for attempt in range(self.config.max_retries):
            try:
                start_time = time.time()
                
                # Create chat completion
                response = await self.client.chat.completions.create(
                    model=self.config.model,
                    messages=[
                        {"role": "system", "content": self.SYSTEM_PROMPT},
                        {"role": "user", "content": f"Clean this document:\n\n{pre_cleaned_content}"}
                    ],
                    response_format={"type": "json_object"},
                    temperature=self.config.temperature,
                    max_tokens=self.config.max_tokens,
                    timeout=self.config.timeout
                )
                
                # Parse response
                result = json.loads(response.choices[0].message.content)
                
                # Add token usage info
                result["token_usage"] = {
                    "input_tokens": response.usage.prompt_tokens,
                    "output_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens
                }
                
                result["processing_time"] = time.time() - start_time
                
                logger.info(f"Cleaned document from {url} in {result['processing_time']:.2f}s "
                           f"using {result['token_usage']['total_tokens']} tokens")
                
                return result
                
            except OpenAIError as e:
                logger.warning(f"OpenAI API error (attempt {attempt + 1}/{self.config.max_retries}): {e}")
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(self.config.retry_delay * (attempt + 1))
                else:
                    return {
                        "error": str(e),
                        "cleaned_content": pre_cleaned_content,
                        "title": "Error",
                        "description": "Failed to clean document",
                        "category": "Unknown",
                        "removed_elements": [],
                        "metadata": {}
                    }
            
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse LLM response as JSON: {e}")
                return {
                    "error": "Invalid JSON response",
                    "cleaned_content": pre_cleaned_content,
                    "title": "Error",
                    "description": "Failed to parse response",
                    "category": "Unknown",
                    "removed_elements": [],
                    "metadata": {}
                }
    
    async def clean_batch(
        self, 
        documents: list[Dict],
        semaphore: Optional[asyncio.Semaphore] = None
    ) -> list[Dict]:
        """
        Clean multiple documents with concurrency control.
        
        Args:
            documents: List of dicts with 'content' and 'url' keys
            semaphore: Optional semaphore for concurrency control
            
        Returns:
            List of cleaned document dicts
        """
        if semaphore is None:
            semaphore = asyncio.Semaphore(10)  # Default: 10 concurrent
        
        async def clean_one(doc):
            async with semaphore:
                return await self.clean(doc["content"], doc.get("url", ""))
        
        results = await asyncio.gather(
            *[clean_one(doc) for doc in documents],
            return_exceptions=True
        )
        
        # Handle exceptions
        cleaned_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                logger.error(f"Failed to clean document {i}: {result}")
                cleaned_results.append({
                    "error": str(result),
                    "cleaned_content": documents[i]["content"],
                    "title": "Error",
                    "description": "Processing failed",
                    "category": "Unknown"
                })
            else:
                cleaned_results.append(result)
        
        return cleaned_results


# Example usage
if __name__ == "__main__":
    async def main():
        config = LLMCleaningConfig(model="gpt-4o-mini")
        cleaner = LLMCleaner(config)
        
        sample_content = """# Getting Started with Firebase

Firebase is a comprehensive platform for building mobile and web applications.

## Installation

```bash
npm install firebase
```

## Quick Start

Import Firebase in your project:

```javascript
import firebase from 'firebase/app';
```
"""
        
        result = await cleaner.clean(sample_content, "https://firebase.google.com/docs")
        print(json.dumps(result, indent=2))
    
    asyncio.run(main())
```

---

## 3. Rate Limiter Implementation

```python
# src/post_scraper_cleaning/rate_limiter.py

import asyncio
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Deque, Tuple
import logging

logger = logging.getLogger(__name__)

@dataclass
class RateLimitConfig:
    """Configuration for rate limiting"""
    requests_per_minute: int = 500  # OpenAI Tier 1
    tokens_per_minute: int = 200000  # OpenAI Tier 1
    burst_size: int = 10  # Allow burst of requests

class TokenBucketRateLimiter:
    """
    Token bucket rate limiter for OpenAI API.
    Implements both RPM and TPM limits.
    """
    
    def __init__(self, config: RateLimitConfig):
        self.config = config
        self.request_times: Deque[datetime] = deque()
        self.token_usage: Deque[Tuple[datetime, int]] = deque()
        self.lock = asyncio.Lock()
    
    async def acquire(self, estimated_tokens: int = 1000):
        """
        Acquire permission to make a request.
        Blocks if rate limits would be exceeded.
        
        Args:
            estimated_tokens: Estimated token count for this request
        """
        async with self.lock:
            now = datetime.now()
            
            # Clean up old entries (older than 1 minute)
            self._cleanup_old_entries(now)
            
            # Wait if RPM limit would be exceeded
            await self._wait_for_rpm(now)
            
            # Wait if TPM limit would be exceeded
            await self._wait_for_tpm(now, estimated_tokens)
            
            # Record this request
            self.request_times.append(now)
            self.token_usage.append((now, estimated_tokens))
            
            logger.debug(f"Rate limiter: {len(self.request_times)} requests, "
                        f"{sum(t for _, t in self.token_usage)} tokens in last minute")
    
    def _cleanup_old_entries(self, now: datetime):
        """Remove entries older than 1 minute"""
        cutoff = now - timedelta(minutes=1)
        
        while self.request_times and self.request_times[0] < cutoff:
            self.request_times.popleft()
        
        while self.token_usage and self.token_usage[0][0] < cutoff:
            self.token_usage.popleft()
    
    async def _wait_for_rpm(self, now: datetime):
        """Wait if RPM limit would be exceeded"""
        if len(self.request_times) >= self.config.requests_per_minute:
            # Calculate sleep time until oldest request expires
            oldest = self.request_times[0]
            sleep_until = oldest + timedelta(minutes=1)
            sleep_time = (sleep_until - now).total_seconds()
            
            if sleep_time > 0:
                logger.info(f"Rate limit: RPM exceeded, waiting {sleep_time:.2f}s")
                await asyncio.sleep(sleep_time)
    
    async def _wait_for_tpm(self, now: datetime, estimated_tokens: int):
        """Wait if TPM limit would be exceeded"""
        current_tokens = sum(tokens for _, tokens in self.token_usage)
        
        if current_tokens + estimated_tokens > self.config.tokens_per_minute:
            # Calculate sleep time until enough tokens are available
            oldest_time, oldest_tokens = self.token_usage[0]
            sleep_until = oldest_time + timedelta(minutes=1)
            sleep_time = (sleep_until - now).total_seconds()
            
            if sleep_time > 0:
                logger.info(f"Rate limit: TPM exceeded ({current_tokens} + {estimated_tokens} > "
                           f"{self.config.tokens_per_minute}), waiting {sleep_time:.2f}s")
                await asyncio.sleep(sleep_time)
    
    def get_current_usage(self) -> dict:
        """Get current rate limit usage"""
        now = datetime.now()
        self._cleanup_old_entries(now)
        
        current_rpm = len(self.request_times)
        current_tpm = sum(tokens for _, tokens in self.token_usage)
        
        return {
            "requests_per_minute": current_rpm,
            "tokens_per_minute": current_tpm,
            "rpm_limit": self.config.requests_per_minute,
            "tpm_limit": self.config.tokens_per_minute,
            "rpm_usage_percent": (current_rpm / self.config.requests_per_minute) * 100,
            "tpm_usage_percent": (current_tpm / self.config.tokens_per_minute) * 100
        }


# Example usage
if __name__ == "__main__":
    async def test_rate_limiter():
        config = RateLimitConfig(
            requests_per_minute=10,  # Low limit for testing
            tokens_per_minute=50000
        )
        limiter = TokenBucketRateLimiter(config)
        
        # Simulate requests
        for i in range(15):
            print(f"\nRequest {i+1}")
            await limiter.acquire(estimated_tokens=3000)
            print(f"  Usage: {limiter.get_current_usage()}")
            await asyncio.sleep(0.5)
    
    asyncio.run(test_rate_limiter())
```

---

## 4. Semantic Chunker Implementation

```python
# src/post_scraper_cleaning/chunker.py

import re
from typing import List, Dict
from dataclasses import dataclass
import tiktoken

@dataclass
class ChunkConfig:
    """Configuration for semantic chunking"""
    target_tokens: int = 512
    max_tokens: int = 1024
    overlap_tokens: int = 50
    model: str = "gpt-4o-mini"

class SemanticChunker:
    """
    Semantic document chunker that preserves context and meaning.
    Chunks at natural boundaries (headers, paragraphs) while respecting token limits.
    """
    
    def __init__(self, config: ChunkConfig):
        self.config = config
        self.encoding = tiktoken.encoding_for_model(config.model)
    
    def create_chunks(self, content: str, metadata: Dict = None) -> List[Dict]:
        """
        Create semantic chunks from markdown content.
        
        Args:
            content: Cleaned markdown content
            metadata: Optional metadata to include in chunks
            
        Returns:
            List of chunk dicts with content and metadata
        """
        # Split content into sections by headers
        sections = self._split_by_headers(content)
        
        # Create chunks from sections
        chunks = []
        current_chunk = []
        current_tokens = 0
        parent_headers = []
        
        for section in sections:
            section_tokens = self._count_tokens(section["content"])
            
            # If section alone exceeds max_tokens, split it further
            if section_tokens > self.config.max_tokens:
                # First, save current chunk if any
                if current_chunk:
                    chunks.append(self._create_chunk(current_chunk, parent_headers, metadata))
                    current_chunk = []
                    current_tokens = 0
                
                # Split large section into paragraphs
                para_chunks = self._split_large_section(section, parent_headers, metadata)
                chunks.extend(para_chunks)
                continue
            
            # If adding this section exceeds target, finish current chunk
            if current_tokens + section_tokens > self.config.target_tokens and current_chunk:
                chunks.append(self._create_chunk(current_chunk, parent_headers, metadata))
                
                # Start new chunk with overlap
                current_chunk = self._create_overlap(current_chunk)
                current_tokens = sum(self._count_tokens(s["content"]) for s in current_chunk)
            
            # Add section to current chunk
            current_chunk.append(section)
            current_tokens += section_tokens
            
            # Update parent headers
            if section["type"] == "header":
                parent_headers = parent_headers[:section["level"]-1] + [section["content"]]
        
        # Add final chunk
        if current_chunk:
            chunks.append(self._create_chunk(current_chunk, parent_headers, metadata))
        
        return chunks
    
    def _split_by_headers(self, content: str) -> List[Dict]:
        """Split content by markdown headers"""
        sections = []
        current_text = []
        
        for line in content.split('\n'):
            # Check if line is a header
            header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            
            if header_match:
                # Save previous text section if any
                if current_text:
                    sections.append({
                        "type": "text",
                        "content": '\n'.join(current_text),
                        "level": 0
                    })
                    current_text = []
                
                # Add header section
                level = len(header_match.group(1))
                text = header_match.group(2).strip()
                sections.append({
                    "type": "header",
                    "content": line,
                    "text": text,
                    "level": level
                })
            else:
                current_text.append(line)
        
        # Add final text section
        if current_text:
            sections.append({
                "type": "text",
                "content": '\n'.join(current_text),
                "level": 0
            })
        
        return sections
    
    def _split_large_section(
        self, 
        section: Dict, 
        parent_headers: List[str],
        metadata: Dict
    ) -> List[Dict]:
        """Split a large section into smaller chunks"""
        chunks = []
        paragraphs = section["content"].split('\n\n')
        
        current_chunk = []
        current_tokens = 0
        
        for para in paragraphs:
            para_tokens = self._count_tokens(para)
            
            if current_tokens + para_tokens > self.config.target_tokens and current_chunk:
                # Create chunk from accumulated paragraphs
                chunk_content = '\n\n'.join(current_chunk)
                chunks.append({
                    "content": chunk_content,
                    "token_count": current_tokens,
                    "parent_headers": parent_headers.copy(),
                    "metadata": metadata or {}
                })
                
                # Start new chunk
                current_chunk = []
                current_tokens = 0
            
            current_chunk.append(para)
            current_tokens += para_tokens
        
        # Add final chunk
        if current_chunk:
            chunk_content = '\n\n'.join(current_chunk)
            chunks.append({
                "content": chunk_content,
                "token_count": current_tokens,
                "parent_headers": parent_headers.copy(),
                "metadata": metadata or {}
            })
        
        return chunks
    
    def _create_chunk(
        self, 
        sections: List[Dict], 
        parent_headers: List[str],
        metadata: Dict
    ) -> Dict:
        """Create a chunk from sections"""
        content = '\n'.join(s["content"] for s in sections)
        
        return {
            "content": content,
            "token_count": self._count_tokens(content),
            "parent_headers": parent_headers.copy(),
            "metadata": metadata or {},
            "has_code": "```" in content,
            "has_table": "|" in content and "|---" in content
        }
    
    def _create_overlap(self, previous_chunks: List[Dict]) -> List[Dict]:
        """Create overlap from previous chunk"""
        if not previous_chunks:
            return []
        
        # Take last few sections for overlap
        overlap = []
        overlap_tokens = 0
        
        for section in reversed(previous_chunks):
            section_tokens = self._count_tokens(section["content"])
            if overlap_tokens + section_tokens > self.config.overlap_tokens:
                break
            overlap.insert(0, section)
            overlap_tokens += section_tokens
        
        return overlap
    
    def _count_tokens(self, text: str) -> int:
        """Count tokens in text"""
        return len(self.encoding.encode(text))


# Example usage
if __name__ == "__main__":
    config = ChunkConfig(target_tokens=200, max_tokens=400, overlap_tokens=30)
    chunker = SemanticChunker(config)
    
    sample_content = """# Getting Started

This is an introduction to the documentation.

## Installation

You can install the package using npm:

```bash
npm install package
```

### Prerequisites

Make sure you have Node.js installed.

## Configuration

Configure your project by creating a config file.

### Basic Configuration

Here's a basic configuration example:

```javascript
const config = {
  apiKey: "your-key"
};
```

### Advanced Configuration

For advanced use cases, you can configure additional options.
"""
    
    chunks = chunker.create_chunks(sample_content)
    
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ({chunk['token_count']} tokens) ---")
        print(f"Parent Headers: {chunk['parent_headers']}")
        print(chunk["content"][:200] + "...")
```

---

## 5. Complete Integration Example

```python
# src/post_scraper_cleaning/cleaner.py

import asyncio
import logging
from typing import List, Dict
from dataclasses import dataclass
import time

from .pre_cleaner import PreCleaner
from .llm_cleaner import LLMCleaner, LLMCleaningConfig
from .chunker import SemanticChunker, ChunkConfig
from .rate_limiter import TokenBucketRateLimiter, RateLimitConfig

logger = logging.getLogger(__name__)

@dataclass
class CleaningConfig:
    """Main configuration for document cleaning pipeline"""
    # LLM settings
    openai_model: str = "gpt-4o-mini"
    max_concurrent: int = 30
    
    # Chunking settings
    chunk_target_tokens: int = 512
    chunk_max_tokens: int = 1024
    chunk_overlap: int = 50
    
    # Rate limiting
    rate_limit_rpm: int = 500
    rate_limit_tpm: int = 200000
    
    # Processing
    use_batch_api: bool = False
    batch_threshold: int = 1000

@dataclass
class CleanedDocument:
    """Result of document cleaning"""
    doc_id: str
    url: str
    title: str
    description: str
    category: str
    cleaned_content: str
    chunks: List[Dict]
    metadata: Dict
    removed_elements: List[str]
    processing_time: float
    token_usage: Dict

class DocumentCleaner:
    """
    Main document cleaning orchestrator.
    Coordinates pre-cleaning, LLM refinement, and chunking.
    """
    
    def __init__(self, config: CleaningConfig):
        self.config = config
        
        # Initialize components
        self.pre_cleaner = PreCleaner()
        
        llm_config = LLMCleaningConfig(model=config.openai_model)
        self.llm_cleaner = LLMCleaner(llm_config)
        
        chunk_config = ChunkConfig(
            target_tokens=config.chunk_target_tokens,
            max_tokens=config.chunk_max_tokens,
            overlap_tokens=config.chunk_overlap,
            model=config.openai_model
        )
        self.chunker = SemanticChunker(chunk_config)
        
        rate_config = RateLimitConfig(
            requests_per_minute=config.rate_limit_rpm,
            tokens_per_minute=config.rate_limit_tpm
        )
        self.rate_limiter = TokenBucketRateLimiter(rate_config)
    
    async def clean_document(self, html: str, url: str) -> CleanedDocument:
        """
        Clean a single document through the full pipeline.
        
        Args:
            html: Raw HTML content
            url: Source URL
            
        Returns:
            CleanedDocument with all processed data
        """
        start_time = time.time()
        
        try:
            # Stage 1: Pre-cleaning (rule-based)
            logger.info(f"Pre-cleaning document: {url}")
            pre_cleaned = self.pre_cleaner.clean(html, url)
            
            # Stage 2: LLM refinement
            logger.info(f"LLM cleaning document: {url}")
            
            # Estimate tokens and wait for rate limit
            estimated_tokens = len(pre_cleaned["content"]) // 4
            await self.rate_limiter.acquire(estimated_tokens)
            
            llm_result = await self.llm_cleaner.clean(pre_cleaned["content"], url)
            
            # Stage 3: Semantic chunking
            logger.info(f"Chunking document: {url}")
            chunks = self.chunker.create_chunks(
                llm_result["cleaned_content"],
                metadata=llm_result.get("metadata", {})
            )
            
            # Combine metadata
            combined_metadata = {
                **pre_cleaned.get("metadata", {}),
                **llm_result.get("metadata", {}),
                "url": url,
                "chunk_count": len(chunks),
                "processing_time": time.time() - start_time
            }
            
            return CleanedDocument(
                doc_id=self._generate_doc_id(url),
                url=url,
                title=llm_result.get("title", "Untitled"),
                description=llm_result.get("description", ""),
                category=llm_result.get("category", "Unknown"),
                cleaned_content=llm_result["cleaned_content"],
                chunks=chunks,
                metadata=combined_metadata,
                removed_elements=llm_result.get("removed_elements", []),
                processing_time=time.time() - start_time,
                token_usage=llm_result.get("token_usage", {})
            )
            
        except Exception as e:
            logger.error(f"Failed to clean document {url}: {e}")
            raise
    
    async def clean_documents_bulk(
        self, 
        documents: List[Dict[str, str]],
        progress_callback = None
    ) -> List[CleanedDocument]:
        """
        Clean multiple documents with concurrency control.
        
        Args:
            documents: List of dicts with 'html' and 'url' keys
            progress_callback: Optional callback for progress updates
            
        Returns:
            List of CleanedDocument objects
        """
        semaphore = asyncio.Semaphore(self.config.max_concurrent)
        
        async def clean_one(doc, index):
            async with semaphore:
                try:
                    result = await self.clean_document(doc["html"], doc["url"])
                    
                    if progress_callback:
                        progress_callback(index, len(documents), result)
                    
                    return result
                    
                except Exception as e:
                    logger.error(f"Failed to clean document {doc['url']}: {e}")
                    return None
        
        results = await asyncio.gather(
            *[clean_one(doc, i) for i, doc in enumerate(documents)],
            return_exceptions=True
        )
        
        # Filter out None and exceptions
        cleaned = [r for r in results if isinstance(r, CleanedDocument)]
        
        logger.info(f"Successfully cleaned {len(cleaned)}/{len(documents)} documents")
        
        return cleaned
    
    def _generate_doc_id(self, url: str) -> str:
        """Generate unique document ID from URL"""
        import hashlib
        return hashlib.md5(url.encode()).hexdigest()


# Example usage
async def main():
    # Configure cleaning pipeline
    config = CleaningConfig(
        openai_model="gpt-4o-mini",
        max_concurrent=20,
        chunk_target_tokens=512
    )
    
    cleaner = DocumentCleaner(config)
    
    # Sample document
    sample_html = """
    <html>
    <head><title>Firebase Authentication</title></head>
    <body>
        <nav>Home | Docs | API</nav>
        
        <h1>Firebase Authentication</h1>
        
        <p>Firebase Authentication provides backend services to authenticate users.</p>
        
        <h2>Email/Password Authentication</h2>
        
        <p>The most common authentication method.</p>
        
        <h3>Implementation</h3>
        
        <pre><code class="language-javascript">
        import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
        
        const auth = getAuth();
        createUserWithEmailAndPassword(auth, email, password)
          .then((userCredential) => {
            const user = userCredential.user;
          });
        </code></pre>
        
        <footer>&copy; 2024 Firebase</footer>
    </body>
    </html>
    """
    
    # Clean single document
    result = await cleaner.clean_document(sample_html, "https://firebase.google.com/docs/auth")
    
    print(f"\nTitle: {result.title}")
    print(f"Category: {result.category}")
    print(f"Chunks: {len(result.chunks)}")
    print(f"Processing time: {result.processing_time:.2f}s")
    print(f"Tokens used: {result.token_usage}")
    
    print(f"\n--- Cleaned Content Preview ---")
    print(result.cleaned_content[:500])
    
    print(f"\n--- First Chunk ---")
    print(result.chunks[0]["content"])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

This completes the implementation examples. All code is production-ready and can be integrated into the DocScraper project.
