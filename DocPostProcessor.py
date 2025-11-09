#!/usr/bin/env python3
"""
Documentation Post-Processor
Cleans, structures, and sorts scraped markdown files for optimal vector database ingestion.
"""

import re
import json
import asyncio
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
from datetime import datetime
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import yaml
import hashlib

from bs4 import BeautifulSoup
from openai import AsyncOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import networkx as nx

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class DocumentChunk:
    """Represents a chunk of document content."""
    content: str
    metadata: Dict[str, Any]
    chunk_id: str
    parent_doc: str
    position: int
    tokens: int = 0
    embedding: Optional[List[float]] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for storage."""
        return {
            'chunk_id': self.chunk_id,
            'content': self.content,
            'metadata': self.metadata,
            'parent_doc': self.parent_doc,
            'position': self.position,
            'tokens': self.tokens
        }


@dataclass
class ProcessedDocument:
    """Represents a processed document."""
    file_path: str
    original_url: str
    title: str
    chunks: List[DocumentChunk] = field(default_factory=list)
    category: Optional[str] = None
    topics: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    complexity_score: float = 0.0
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for storage."""
        return {
            'file_path': self.file_path,
            'original_url': self.original_url,
            'title': self.title,
            'chunks': [chunk.to_dict() for chunk in self.chunks],
            'category': self.category,
            'topics': self.topics,
            'dependencies': self.dependencies,
            'complexity_score': self.complexity_score
        }


class DocumentCleaner:
    """Cleans markdown documents by removing headers, footers, and navigation elements."""
    
    def __init__(self):
        # Common patterns to remove
        self.header_patterns = [
            r'\[.*?home page.*?\]\(.*?\)',  # Home page links
            r'Search\.\.\.',  # Search placeholders
            r'⌘K',  # Keyboard shortcuts
            r'Navigation',  # Navigation text
            r'\* \[Research\].*?\n',  # Navigation links
            r'\* \[News\].*?\n',
            r'\* \[Go to.*?\].*?\n',
            r'English\n',  # Language selector
            r'!\[.*?logo\]\(.*?\)',  # Logo images
        ]
        
        self.footer_patterns = [
            r'Was this page helpful\?.*?YesNo',
            r'\[x\]\(https://x\.com/.*?\)',  # Social media links
            r'\[linkedin\]\(.*?\)',
            r'On this page\n.*?(?=\n\n|\Z)',  # Table of contents
        ]
        
        self.navigation_patterns = [
            r'\[Welcome\]\(.*?\)',
            r'\[Developer Guide\]\(.*?\)',
            r'\[API Guide\]\(.*?\)',
            r'\[Resources\]\(.*?\)',
            r'\[Release Notes\]\(.*?\)',
            r'\* \[Documentation\]\(.*?\)',
            r'\* \[Developer Console\]\(.*?\)',
            r'\* \[Support\]\(.*?\)',
        ]
    
    def clean_document(self, content: str, preserve_structure: bool = True) -> str:
        """Clean a document by removing unwanted elements."""
        cleaned = content
        
        # Remove header patterns
        for pattern in self.header_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.MULTILINE | re.DOTALL)
        
        # Remove footer patterns
        for pattern in self.footer_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.MULTILINE | re.DOTALL)
        
        # Remove navigation patterns
        for pattern in self.navigation_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.MULTILINE)
        
        # Clean up excessive whitespace
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
        cleaned = re.sub(r' {2,}', ' ', cleaned)
        
        # Remove empty bullet points
        cleaned = re.sub(r'^\* *$', '', cleaned, flags=re.MULTILINE)
        
        # Remove standalone navigation sections
        cleaned = re.sub(r'^#{1,5} *(First steps|Models & pricing|Learn about Claude|Explore features|Agent components|Test & evaluate|Legal center)\n.*?(?=^#|\Z)', 
                         '', cleaned, flags=re.MULTILINE | re.DOTALL)
        
        if preserve_structure:
            # Preserve important markdown structure
            cleaned = self._preserve_important_structure(cleaned)
        
        return cleaned.strip()
    
    def _preserve_important_structure(self, content: str) -> str:
        """Preserve important structural elements like headers and code blocks."""
        # Ensure code blocks are preserved
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        for i, block in enumerate(code_blocks):
            placeholder = f"__CODE_BLOCK_{i}__"
            content = content.replace(block, placeholder, 1)
        
        # Clean content
        content = re.sub(r'^\s*\n', '', content, flags=re.MULTILINE)
        
        # Restore code blocks
        for i, block in enumerate(code_blocks):
            placeholder = f"__CODE_BLOCK_{i}__"
            content = content.replace(placeholder, block)
        
        return content
    
    def extract_metadata(self, content: str) -> Tuple[Dict[str, Any], str]:
        """Extract YAML frontmatter and return metadata and content."""
        if content.startswith('---'):
            try:
                _, frontmatter, rest = content.split('---', 2)
                metadata = yaml.safe_load(frontmatter)
                
                # Convert any datetime objects to strings
                if metadata:
                    for key, value in metadata.items():
                        if hasattr(value, 'isoformat'):  # Check if it's a datetime object
                            metadata[key] = value.isoformat()
                
                return metadata, rest
            except:
                return {}, content
        return {}, content


class DocumentStructurer:
    """Structures documents into hierarchical chunks optimized for embeddings."""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.section_patterns = {
            'h1': r'^# (.+)$',
            'h2': r'^## (.+)$',
            'h3': r'^### (.+)$',
            'h4': r'^#### (.+)$',
            'h5': r'^##### (.+)$',
            'code': r'```[\s\S]*?```',
            'list': r'^\* .+$',
            'numbered_list': r'^\d+\. .+$',
        }
    
    def structure_document(self, content: str, metadata: Dict[str, Any]) -> List[DocumentChunk]:
        """Structure document into semantic chunks."""
        chunks = []
        
        # Parse document structure
        sections = self._parse_sections(content)
        
        # Create chunks based on sections
        for section in sections:
            section_chunks = self._create_semantic_chunks(
                section['content'],
                section['metadata']
            )
            chunks.extend(section_chunks)
        
        # Add document-level metadata to all chunks
        for chunk in chunks:
            chunk.metadata.update({
                'source_url': metadata.get('url', ''),
                'scraped_at': metadata.get('scraped_at', ''),
                'doc_title': metadata.get('title', '')
            })
        
        return chunks
    
    def _parse_sections(self, content: str) -> List[Dict[str, Any]]:
        """Parse document into hierarchical sections."""
        lines = content.split('\n')
        sections = []
        current_section = {
            'level': 0,
            'title': 'Introduction',
            'content': [],
            'metadata': {}
        }
        
        for line in lines:
            # Check for headers
            header_match = None
            header_level = 0
            
            for level in range(1, 6):
                pattern = f'^{"#" * level} (.+)$'
                match = re.match(pattern, line)
                if match:
                    header_match = match
                    header_level = level
                    break
            
            if header_match:
                # Save current section if it has content
                if current_section['content']:
                    current_section['content'] = '\n'.join(current_section['content'])
                    sections.append(current_section)
                
                # Start new section
                current_section = {
                    'level': header_level,
                    'title': header_match.group(1),
                    'content': [],
                    'metadata': {
                        'section_level': header_level,
                        'section_title': header_match.group(1)
                    }
                }
            else:
                current_section['content'].append(line)
        
        # Add final section
        if current_section['content']:
            current_section['content'] = '\n'.join(current_section['content'])
            sections.append(current_section)
        
        return sections
    
    def _create_semantic_chunks(self, content: str, section_metadata: Dict) -> List[DocumentChunk]:
        """Create semantic chunks from section content."""
        chunks = []
        
        # Skip empty content
        if not content.strip():
            return chunks
        
        # Handle code blocks specially
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        for code_block in code_blocks:
            content = content.replace(code_block, f"__CODE_BLOCK_{len(chunks)}__")
            
            # Create chunk for code block
            chunk_id = hashlib.md5(code_block.encode()).hexdigest()[:8]
            chunk = DocumentChunk(
                content=code_block,
                metadata={**section_metadata, 'type': 'code'},
                chunk_id=chunk_id,
                parent_doc='',
                position=len(chunks),
                tokens=len(code_block.split())
            )
            chunks.append(chunk)
        
        # Split remaining content into chunks
        words = content.split()
        current_chunk = []
        current_size = 0
        
        for word in words:
            current_chunk.append(word)
            current_size += 1
            
            if current_size >= self.chunk_size:
                chunk_content = ' '.join(current_chunk)
                
                # Restore code blocks
                for i, code_block in enumerate(code_blocks):
                    chunk_content = chunk_content.replace(f"__CODE_BLOCK_{i}__", code_block)
                
                chunk_id = hashlib.md5(chunk_content.encode()).hexdigest()[:8]
                chunk = DocumentChunk(
                    content=chunk_content,
                    metadata={**section_metadata, 'type': 'text'},
                    chunk_id=chunk_id,
                    parent_doc='',
                    position=len(chunks),
                    tokens=current_size
                )
                chunks.append(chunk)
                
                # Overlap for next chunk
                overlap_size = min(self.chunk_overlap, len(current_chunk))
                current_chunk = current_chunk[-overlap_size:]
                current_size = overlap_size
        
        # Add remaining content as final chunk
        if current_chunk:
            chunk_content = ' '.join(current_chunk)
            
            # Restore code blocks
            for i, code_block in enumerate(code_blocks):
                chunk_content = chunk_content.replace(f"__CODE_BLOCK_{i}__", code_block)
            
            chunk_id = hashlib.md5(chunk_content.encode()).hexdigest()[:8]
            chunk = DocumentChunk(
                content=chunk_content,
                metadata={**section_metadata, 'type': 'text'},
                chunk_id=chunk_id,
                parent_doc='',
                position=len(chunks),
                tokens=current_size
            )
            chunks.append(chunk)
        
        return chunks


class DocumentSorter:
    """Sorts documents using LLM-based classification and clustering."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.client = None
        if api_key:
            self.client = AsyncOpenAI(api_key=api_key)
        
        self.categories = {
            'getting_started': ['introduction', 'quickstart', 'setup', 'installation'],
            'concepts': ['overview', 'concepts', 'architecture', 'principles'],
            'guides': ['guide', 'tutorial', 'how-to', 'walkthrough'],
            'api_reference': ['api', 'reference', 'endpoints', 'methods'],
            'examples': ['example', 'sample', 'demo', 'code'],
            'advanced': ['advanced', 'optimization', 'performance', 'scaling'],
            'troubleshooting': ['troubleshooting', 'errors', 'debugging', 'issues']
        }
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def classify_document(self, doc: ProcessedDocument) -> str:
        """Classify document using LLM."""
        if not self.client:
            return self._rule_based_classification(doc)
        
        prompt = f"""
        Classify the following documentation into one of these categories:
        - getting_started: Introduction, setup, installation guides
        - concepts: Core concepts, architecture, principles
        - guides: How-to guides, tutorials, walkthroughs
        - api_reference: API documentation, method references
        - examples: Code examples, demos, samples
        - advanced: Advanced topics, optimization, scaling
        - troubleshooting: Error handling, debugging, common issues
        
        Document Title: {doc.title}
        Document URL: {doc.original_url}
        First 500 characters: {doc.chunks[0].content[:500] if doc.chunks else ''}
        
        Return only the category name.
        """
        
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",  # 🚀 Fastest and 20x cheaper than gpt-4.1-mini
                messages=[
                    {"role": "system", "content": "You are a documentation classifier."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,  # Low temperature for consistent classification
                max_tokens=20,    # 🚀 Reduced - we only need category name
                timeout=15        # 🚀 Add timeout to prevent hanging
            )
            
            category = response.choices[0].message.content.strip().lower()
            if category in self.categories:
                return category
            else:
                logger.warning(f"LLM returned unknown category '{category}' for '{doc.title}', falling back to rule-based.")
                return self._rule_based_classification(doc)
                
        except Exception as e:
            logger.error(f"LLM classification failed for '{doc.title}': {e}, falling back to rule-based.")
            return self._rule_based_classification(doc)
    
    def _rule_based_classification(self, doc: ProcessedDocument) -> str:
        """Fallback rule-based classification."""
        title_lower = doc.title.lower()
        url_lower = doc.original_url.lower()
        
        # Check each category's keywords
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if keyword in title_lower or keyword in url_lower:
                    return category
        
        return 'guides'  # Default category
    
    def create_dependency_graph(self, documents: List[ProcessedDocument]) -> nx.DiGraph:
        """Create a dependency graph based on document references with progress tracking."""
        import time
        
        graph = nx.DiGraph()
        total_docs = len(documents)
        
        logger.info(f"🔗 Creating dependency graph for {total_docs} documents...")
        
        # Add nodes
        for doc in documents:
            graph.add_node(doc.file_path, doc=doc)
        
        # Add edges based on references with progress tracking
        start_time = time.time()
        for i, doc in enumerate(documents):
            if i % 50 == 0 or i == total_docs - 1:
                elapsed = time.time() - start_time
                progress = (i + 1) / total_docs * 100
                if i > 0:
                    eta = elapsed / (i + 1) * (total_docs - i - 1)
                    logger.info(f"🔗 Dependency analysis: {i+1}/{total_docs} ({progress:.1f}%) | ETA: {eta/60:.1f}min")
                else:
                    logger.info(f"🔗 Dependency analysis: {i+1}/{total_docs} ({progress:.1f}%)")
            
            # Get content from chunks (limit to first 2 chunks for speed)
            content_parts = []
            for chunk in doc.chunks[:2]:  # Only check first 2 chunks for speed
                content_parts.append(chunk.content)
            content = ' '.join(content_parts).lower()  # Convert to lowercase for faster matching
            
            # Only check against a subset of documents for speed (every 10th document)
            step = max(1, total_docs // 1000)  # Adaptive step size
            for other_doc in documents[::step]:
                if doc.file_path != other_doc.file_path:
                    # Check for URL references (if URL exists and is meaningful)
                    if other_doc.original_url and len(other_doc.original_url) > 10 and other_doc.original_url.lower() in content:
                        graph.add_edge(doc.file_path, other_doc.file_path)
                    
                    # Check for title references (simplified - only meaningful titles)
                    title = other_doc.title if isinstance(other_doc.title, str) else str(other_doc.title)
                    title_lower = title.lower()
                    if len(title_lower) > 15 and title_lower in content:  # Only check meaningful titles
                        graph.add_edge(doc.file_path, other_doc.file_path)
        
        logger.info(f"🔗 Dependency graph created with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges")
        return graph
    
    def calculate_complexity_scores(self, documents: List[ProcessedDocument]) -> None:
        """Calculate complexity scores for documents with progress tracking."""
        total_docs = len(documents)
        logger.info(f"📊 Calculating complexity scores for {total_docs} documents...")
        
        for i, doc in enumerate(documents):
            if i % 1000 == 0 or i == total_docs - 1:
                progress = (i + 1) / total_docs * 100
                logger.info(f"📊 Complexity calculation: {i+1}/{total_docs} ({progress:.1f}%)")
            # Factors for complexity
            total_tokens = sum(chunk.tokens for chunk in doc.chunks)
            code_chunks = sum(1 for chunk in doc.chunks if chunk.metadata.get('type') == 'code')
            avg_chunk_size = total_tokens / len(doc.chunks) if doc.chunks else 0
            
            # Calculate complexity score (0-1)
            complexity = min(1.0, (
                (total_tokens / 10000) * 0.3 +  # Document length
                (code_chunks / max(len(doc.chunks), 1)) * 0.3 +  # Code density
                (avg_chunk_size / 1000) * 0.2 +  # Chunk complexity
                (len(doc.dependencies) / 10) * 0.2  # Dependencies
            ))
            
            doc.complexity_score = complexity
    
    async def sort_documents(self, documents: List[ProcessedDocument]) -> List[ProcessedDocument]:
        """Sort documents for optimal learning/embedding order."""
        
        # 🚀 PARALLEL OpenAI classification instead of sequential
        import asyncio
        
        logger.info(f"Classifying {len(documents)} documents with OpenAI (parallel batches)...")
        
        # Classify documents in parallel batches to respect rate limits
        batch_size = 8  # Optimal for OpenAI rate limits
        total_batches = (len(documents) + batch_size - 1) // batch_size
        
        for batch_num in range(total_batches):
            start_idx = batch_num * batch_size
            end_idx = min(start_idx + batch_size, len(documents))
            batch = documents[start_idx:end_idx]
            
            # Create classification tasks for this batch
            batch_tasks = [self.classify_document(doc) for doc in batch]
            
            # Process batch in parallel
            try:
                categories = await asyncio.gather(*batch_tasks, return_exceptions=True)
                
                # Assign results back to documents
                for i, category in enumerate(categories):
                    if not isinstance(category, Exception):
                        batch[i].category = category
                    else:
                        logger.warning(f"Classification failed for {batch[i].title}: {category}")
                        batch[i].category = self._rule_based_classification(batch[i])
                
                # Progress logging
                processed = end_idx
                logger.info(f"Classified batch {batch_num + 1}/{total_batches} ({processed}/{len(documents)} documents)")
                
                # Small delay between batches to respect rate limits
                if batch_num < total_batches - 1:
                    await asyncio.sleep(0.2)
                    
            except Exception as e:
                logger.error(f"Batch {batch_num + 1} failed: {e}")
                # Fallback to rule-based for this batch
                for doc in batch:
                    doc.category = self._rule_based_classification(doc)
        
        # Create dependency graph
        dep_graph = self.create_dependency_graph(documents)
        
        # Extract dependencies
        for doc in documents:
            doc.dependencies = list(dep_graph.predecessors(doc.file_path))
        
        # Calculate complexity scores
        self.calculate_complexity_scores(documents)
        
        # Sort by category order, then complexity
        category_order = [
            'getting_started', 'concepts', 'guides', 
            'api_reference', 'examples', 'advanced', 'troubleshooting'
        ]
        
        def sort_key(doc):
            category_idx = category_order.index(doc.category) if doc.category in category_order else 99
            return (category_idx, doc.complexity_score)
        
        sorted_docs = sorted(documents, key=sort_key)
        
        # Ensure dependencies come before dependents
        sorted_docs = self._topological_sort_with_categories(sorted_docs, dep_graph)
        
        return sorted_docs
    
    def _topological_sort_with_categories(self, documents: List[ProcessedDocument], 
                                        graph: nx.DiGraph) -> List[ProcessedDocument]:
        """Perform topological sort while respecting category ordering."""
        # Create subgraphs for each category
        category_docs = defaultdict(list)
        for doc in documents:
            category_docs[doc.category].append(doc)
        
        # Sort within each category based on dependencies
        sorted_docs = []
        for category in ['getting_started', 'concepts', 'guides', 
                        'api_reference', 'examples', 'advanced', 'troubleshooting']:
            if category in category_docs:
                # Create subgraph for this category
                category_files = [doc.file_path for doc in category_docs[category]]
                subgraph = graph.subgraph(category_files)
                
                # Topological sort within category
                try:
                    sorted_files = list(nx.topological_sort(subgraph))
                    for file_path in sorted_files:
                        doc = next(d for d in category_docs[category] if d.file_path == file_path)
                        sorted_docs.append(doc)
                except nx.NetworkXUnfeasible:
                    # If there are cycles, just use the original order
                    sorted_docs.extend(category_docs[category])
        
        return sorted_docs


class DocumentPostProcessor:
    """Main post-processor that orchestrates cleaning, structuring, and sorting."""
    
    def __init__(self, input_dir: str, output_dir: str, api_key: Optional[str] = None):
        self.input_dir = Path(input_dir)
        
        # 🛡️ SECURITY: Create dated output directory to prevent overwrites
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_output = Path("/Volumes/NvME-Satechi/VectorDatabase")
        
        # Create descriptive directory name with timestamp
        input_name = Path(input_dir).name.replace(" ", "_")
        dated_output_name = f"{timestamp}_{input_name}_VectorDB"
        
        self.output_dir = base_output / dated_output_name
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Also create checkpoint directory
        self.checkpoint_dir = self.output_dir / "checkpoints"
        self.checkpoint_dir.mkdir(exist_ok=True)
        
        logger.info(f"🛡️ Output will be saved to: {self.output_dir}")
        
        self.cleaner = DocumentCleaner()
        self.structurer = DocumentStructurer()
        self.sorter = DocumentSorter(api_key)
        
        self.processed_docs: List[ProcessedDocument] = []
        
        # 🛡️ CHECKPOINT SYSTEM: Track progress to prevent token loss
        self.checkpoint_interval = 100  # Save every 100 processed documents
        self.last_checkpoint = 0
        self.processing_start_time = None
    
    def save_checkpoint(self, phase: str, additional_data: Dict = None):
        """🛡️ Save processing checkpoint to prevent token loss."""
        import time
        
        checkpoint_data = {
            "timestamp": datetime.now().isoformat(),
            "phase": phase,
            "processed_count": len(self.processed_docs),
            "processing_time": time.time() - self.processing_start_time if self.processing_start_time else 0,
            "input_dir": str(self.input_dir),
            "output_dir": str(self.output_dir),
            "processed_docs": [doc.to_dict() for doc in self.processed_docs],
            **(additional_data or {})
        }
        
        checkpoint_file = self.checkpoint_dir / f"checkpoint_{phase}_{len(self.processed_docs)}.json"
        
        with open(checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(checkpoint_data, f, indent=2)
        
        logger.info(f"🛡️ Checkpoint saved: {checkpoint_file} ({len(self.processed_docs)} docs)")
        return checkpoint_file
    
    def should_save_checkpoint(self) -> bool:
        """Check if it's time to save a checkpoint."""
        return len(self.processed_docs) - self.last_checkpoint >= self.checkpoint_interval
    
    def load_checkpoint(self, checkpoint_file: str):
        """🔄 Load processing state from checkpoint."""
        with open(checkpoint_file, 'r', encoding='utf-8') as f:
            checkpoint_data = json.load(f)
        
        # Restore processed documents
        self.processed_docs = []
        for doc_data in checkpoint_data.get('processed_docs', []):
            # Convert chunk data back to DocumentChunk objects
            chunks = []
            for i, chunk_data in enumerate(doc_data.get('chunks', [])):
                chunk = DocumentChunk(
                    content=chunk_data.get('content', ''),
                    metadata=chunk_data.get('metadata', {}),
                    chunk_id=chunk_data.get('chunk_id', ''),
                    parent_doc=doc_data['file_path'],
                    position=i,
                    tokens=chunk_data.get('tokens', 0)
                )
                chunks.append(chunk)
            
            doc = ProcessedDocument(
                file_path=doc_data['file_path'],
                title=doc_data['title'],
                chunks=chunks,
                original_url=doc_data.get('original_url', ''),
                category=doc_data.get('category'),
                complexity_score=doc_data.get('complexity_score', 0.0),
                dependencies=doc_data.get('dependencies', [])
            )
            self.processed_docs.append(doc)
        
        self.last_checkpoint = len(self.processed_docs)
        logger.info(f"🔄 Loaded {len(self.processed_docs)} documents from checkpoint")
        logger.info(f"🔄 Checkpoint phase: {checkpoint_data.get('phase', 'unknown')}")
        
        return checkpoint_data
    
    async def process_all_documents(self, recursive: bool = True, flatten_output: bool = True) -> Dict[str, Any]:
        """Process all documents in the input directory.
        
        Args:
            recursive: If True, process files in all subdirectories
            flatten_output: If True, output all files to a single directory
        """
        logger.info(f"Starting post-processing of documents in {self.input_dir}")
        logger.info(f"Recursive: {recursive}, Flatten output: {flatten_output}")
        
        # 🛡️ Initialize checkpoint system
        import time
        self.processing_start_time = time.time()
        
        # Find all markdown files
        if recursive:
            md_files = list(self.input_dir.rglob("*.md"))  # Recursive glob
        else:
            md_files = list(self.input_dir.glob("*.md"))  # Non-recursive
            
        # Exclude summary files
        md_files = [f for f in md_files if not f.name.startswith('_')]
        
        logger.info(f"Found {len(md_files)} markdown files to process")
        
        # Track source folders for organization
        source_folders = defaultdict(list)
        
        # 🚀 Process files in parallel batches for better performance
        import asyncio
        
        logger.info(f"Processing {len(md_files)} files in parallel batches...")
        
        # 🔥 OPTIMIZED PARALLEL PROCESSING for large datasets
        max_workers = min(25, len(md_files))  # More conservative: 25 concurrent operations
        batch_size = 50  # Smaller batches: 50 files per batch for better stability
        
        logger.info(f"⚡ TURBO MODE: {max_workers} parallel workers, {batch_size} files per batch")
        total_batches = (len(md_files) + batch_size - 1) // batch_size
        
        for batch_num in range(total_batches):
            start_idx = batch_num * batch_size
            end_idx = min(start_idx + batch_size, len(md_files))
            batch_files = md_files[start_idx:end_idx]
            
            # 🚀 Create semaphore to limit concurrent operations and prevent memory overflow
            semaphore = asyncio.Semaphore(max_workers)
            
            async def process_with_semaphore(file_path):
                async with semaphore:
                    return await self.process_document(file_path)
            
            # Create massive parallel tasks
            batch_tasks = [process_with_semaphore(md_file) for md_file in batch_files]
            
            try:
                # Execute massive parallel batch
                results = await asyncio.gather(*batch_tasks, return_exceptions=True)
                
                # Process results and track source folders
                for i, result in enumerate(results):
                    md_file = batch_files[i]
                    
                    if isinstance(result, Exception):
                        logger.error(f"Error processing {md_file}: {result}")
                        continue
                        
                    if result:  # Successfully processed document
                        self.processed_docs.append(result)
                        
                        # Track source folder
                        relative_path = md_file.relative_to(self.input_dir)
                        source_folder = relative_path.parent if relative_path.parent != Path('.') else Path('root')
                        source_folders[str(source_folder)].append(result)
                
                # 🛡️ CHECKPOINT SAVING: Save progress every few batches
                if self.should_save_checkpoint():
                    self.save_checkpoint("file_processing", {
                        "batch_number": batch_num + 1,
                        "total_batches": total_batches,
                        "files_processed": processed_count,
                        "total_files": len(md_files)
                    })
                    self.last_checkpoint = len(self.processed_docs)
                
                # Memory management: Force garbage collection after each mega-batch
                import gc
                gc.collect()
                
                # Enhanced progress logging with speed metrics
                processed_count = end_idx
                if batch_num == 0:
                    import time
                    batch_start_time = time.time()
                else:
                    batch_time = time.time() - batch_start_time
                    files_per_sec = len(batch_files) / batch_time if batch_time > 0 else 0
                    eta_minutes = ((len(md_files) - processed_count) / files_per_sec / 60) if files_per_sec > 0 else 0
                    
                    logger.info(f"🚀 Batch {batch_num + 1}/{total_batches} COMPLETE - {processed_count}/{len(md_files)} files")
                    logger.info(f"⚡ Speed: {files_per_sec:.1f} files/sec | ETA: {eta_minutes:.1f} minutes")
                    batch_start_time = time.time()
                
            except Exception as e:
                logger.error(f"Batch {batch_num + 1} processing failed: {e}")
                # Fallback to sequential processing for this batch
                for md_file in batch_files:
                    try:
                        processed_doc = await self.process_document(md_file)
                        if processed_doc:
                            self.processed_docs.append(processed_doc)
                            relative_path = md_file.relative_to(self.input_dir)
                            source_folder = relative_path.parent if relative_path.parent != Path('.') else Path('root')
                            source_folders[str(source_folder)].append(processed_doc)
                    except Exception as fallback_error:
                        logger.error(f"Error processing {md_file}: {fallback_error}")
        
        # 🛡️ CRITICAL CHECKPOINT: Save before expensive OpenAI processing
        self.save_checkpoint("pre_classification", {
            "total_documents_ready": len(self.processed_docs),
            "message": "About to start OpenAI classification - most expensive phase"
        })
        
        # Sort documents
        logger.info("Sorting documents...")
        self.processed_docs = await self.sorter.sort_documents(self.processed_docs)
        
        # 🛡️ CHECKPOINT: Save after OpenAI classification
        self.save_checkpoint("post_classification", {
            "total_documents_classified": len(self.processed_docs),
            "message": "OpenAI classification complete - safe to proceed"
        })
        
        # Save processed documents
        logger.info("Saving processed documents...")
        summary = self.save_processed_documents(flatten_output=flatten_output, source_folders=dict(source_folders))
        
        # 🛡️ FINAL CHECKPOINT: Mark successful completion
        self.save_checkpoint("completed", {
            "summary": summary,
            "message": "Processing completed successfully - all files saved"
        })
        
        logger.info(f"🛡️ Processing complete! All checkpoints saved in: {self.checkpoint_dir}")
        
        return summary
    
    async def process_document(self, file_path: Path) -> Optional[ProcessedDocument]:
        """🚀 TURBO: Process a single document with optimized I/O and CPU usage."""
        
        try:
            # 🚀 ASYNC FILE READING (non-blocking I/O for better concurrency)
            try:
                import aiofiles
                async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                    content = await f.read()
            except ImportError:
                # Fallback to sync I/O if aiofiles not available
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
        except Exception as e:
            logger.error(f"Failed to read {file_path}: {e}")
            return None
        
        # 🚀 FAST METADATA EXTRACTION
        metadata, raw_content = self.cleaner.extract_metadata(content)
        cleaned_content = self.cleaner.clean_document(raw_content)
        
        # Skip empty documents early (save processing time)
        if not cleaned_content.strip():
            return None
        
        # 🚀 OPTIMIZED DOCUMENT CREATION
        doc = ProcessedDocument(
            file_path=str(file_path),
            original_url=metadata.get('url', ''),
            title=metadata.get('title', file_path.stem)
        )
        
        # 🚀 FAST CHUNKING
        doc.chunks = self.structurer.structure_document(cleaned_content, metadata)
        
        # 🚀 BATCH CHUNK PROCESSING (avoid repeated string conversion)
        parent_doc_str = str(file_path)
        for chunk in doc.chunks:
            chunk.parent_doc = parent_doc_str
        
        return doc
    
    def save_processed_documents(self, flatten_output: bool = True, source_folders: Dict[str, List] = None) -> Dict[str, Any]:
        """Save processed documents to output directory.
        
        Args:
            flatten_output: If True, save all files in a single directory structure
            source_folders: Mapping of source folders to documents (for organization)
        """
        # Create output structure
        (self.output_dir / 'cleaned').mkdir(exist_ok=True)
        (self.output_dir / 'chunks').mkdir(exist_ok=True)
        (self.output_dir / 'metadata').mkdir(exist_ok=True)
        
        summary = {
            'processed_at': datetime.now().isoformat(),
            'total_documents': len(self.processed_docs),
            'total_chunks': 0,
            'categories': dict(),  # Use regular dict instead of defaultdict
            'source_folders': list(source_folders.keys()) if source_folders else [],
            'documents': []
        }
        
        # Save each document
        for i, doc in enumerate(self.processed_docs):
            # Determine output filename
            if flatten_output:
                # Create a unique filename that preserves some path info
                relative_path = Path(doc.file_path).relative_to(self.input_dir) if self.input_dir in Path(doc.file_path).parents else Path(doc.file_path).name
                path_parts = list(relative_path.parts[:-1])  # Exclude filename
                
                if path_parts:
                    # Include folder structure in filename
                    folder_prefix = "_".join(path_parts).replace("/", "_").replace("\\", "_")
                    filename_stem = f"{i:04d}_{folder_prefix}_{Path(doc.file_path).stem}"
                else:
                    filename_stem = f"{i:04d}_{Path(doc.file_path).stem}"
            else:
                # Preserve original folder structure
                filename_stem = f"{i:04d}_{Path(doc.file_path).stem}"
            
            # Save cleaned full document
            cleaned_path = self.output_dir / 'cleaned' / f"{filename_stem}.md"
            full_content = '\n\n'.join([chunk.content for chunk in doc.chunks])
            
            with open(cleaned_path, 'w', encoding='utf-8') as f:
                f.write(f"# {doc.title}\n\n")
                f.write(f"**Category**: {doc.category}\n")
                f.write(f"**Complexity**: {doc.complexity_score:.2f}\n")
                f.write(f"**Original URL**: {doc.original_url}\n")
                f.write(f"**Source File**: {doc.file_path}\n\n")
                f.write(full_content)
            
            # Save chunks
            chunk_dir = self.output_dir / 'chunks' / filename_stem
            chunk_dir.mkdir(exist_ok=True, parents=True)
            
            for j, chunk in enumerate(doc.chunks):
                chunk_path = chunk_dir / f"chunk_{j:03d}.json"
                with open(chunk_path, 'w', encoding='utf-8') as f:
                    json.dump(chunk.to_dict(), f, indent=2)
            
            # Update summary
            summary['total_chunks'] += len(doc.chunks)
            # Use setdefault to ensure category exists in dict
            summary['categories'].setdefault(doc.category, 0)
            summary['categories'][doc.category] += 1
            summary['documents'].append({
                'index': i,
                'file': str(cleaned_path),
                'original': doc.file_path,
                'title': doc.title,
                'category': doc.category,
                'chunks': len(doc.chunks),
                'complexity': doc.complexity_score,
                'dependencies': doc.dependencies,
                'source_folder': str(Path(doc.file_path).parent.relative_to(self.input_dir)) if self.input_dir in Path(doc.file_path).parents else 'root'
            })
        
        # Save summary
        summary_path = self.output_dir / 'processing_summary.json'
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        # Save sorted index for vector DB
        index_path = self.output_dir / 'vector_db_index.json'
        vector_index = []
        
        for doc in self.processed_docs:
            for chunk in doc.chunks:
                vector_index.append({
                    'chunk_id': chunk.chunk_id,
                    'content': chunk.content,
                    'metadata': {
                        **chunk.metadata,
                        'category': doc.category,
                        'complexity': doc.complexity_score,
                        'parent_title': doc.title,
                        'source_file': doc.file_path
                    }
                })
        
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(vector_index, f, indent=2)
        
        logger.info(f"Processing complete! Summary saved to {summary_path}")
        return summary


async def main():
    """Main entry point."""
    import sys
    import os
    from dotenv import load_dotenv
        
    # Always load environment variables from .env file
    load_dotenv()
        
    if len(sys.argv) < 3:
        print("Usage: python DocPostProcessor.py <input_dir> <output_dir> [--use-llm]")
        print("\nExample:")
        print("  python DocPostProcessor.py Documentation/Anthropic processed_docs")
        print("  python DocPostProcessor.py Documentation/Anthropic processed_docs --use-llm")
        sys.exit(1)
        
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    use_llm = '--use-llm' in sys.argv
        
    # Get API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')
    if use_llm and not api_key:
        logger.warning("No OPENAI_API_KEY found in environment, falling back to rule-based classification")
        use_llm = False
        
    # Process documents
    processor = DocumentPostProcessor(input_dir, output_dir, api_key if use_llm else None)
    summary = await processor.process_all_documents()
        
    # Print summary
    print(f"\n✅ Processing Complete!")
    print(f"📁 Total documents: {summary['total_documents']}")
    print(f"📄 Total chunks: {summary['total_chunks']}")
    print(f"\n📊 Categories:")
    for category, count in summary['categories'].items():
        print(f"  - {category}: {count} documents")


if __name__ == "__main__":
    asyncio.run(main()) 