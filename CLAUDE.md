# DocScraper - Documentation Scraping & Post-Processing Toolkit

A comprehensive Python toolkit for scraping documentation websites and post-processing them for optimal use in vector databases and LLM applications.

## What This Project Does

DocScraper solves the challenge of converting web-based documentation into structured, searchable, and AI-ready formats through a two-phase pipeline:

1. **Scraping Phase**: Crawls documentation websites, converts HTML to clean markdown
2. **Post-Processing Phase**: Cleans content, creates semantic chunks, and prepares for vector databases

## Architecture Overview

```
Web Documentation → Scraper → Raw Markdown → Post-Processor → Vector DB Ready
                     ↓                        ↓
                 GUI/CLI Tools          Chunks + Metadata
```

### Core Components

- **Scraping Engine**: `DocScraper.py` (advanced) and `SimpleDocScraper.py` (basic)
- **Post-Processing Engine**: `DocPostProcessor.py` with AI-powered classification
- **GUI Interfaces**: Tkinter-based tools for both scraping and processing
- **Example Scripts**: Complete workflows for different use cases

### Key Technologies

- **crawl4ai + Playwright**: Advanced web scraping with JavaScript support
- **BeautifulSoup4**: HTML parsing and content extraction
- **OpenAI API**: LLM-powered document classification and sorting
- **NetworkX**: Document dependency analysis
- **scikit-learn**: Text processing and clustering

## Quick Start

### 1. Setup Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
echo "OPENAI_API_KEY=your-key" > .env
```

### 2. Scrape Documentation
```bash
# GUI version (recommended)
python DocScraperGUI.py

# CLI version
python SimpleDocScraper.py https://docs.anthropic.com

# Advanced scraper with parallel processing
python DocScraper.py
```

### 3. Post-Process for Vector DB
```bash
# GUI version (recommended)
python DocPostProcessorGUI.py

# CLI with AI classification
python DocPostProcessor.py scraped_docs processed_docs --use-llm

# Multi-folder processing
python process_multi_folder_example.py
```

## Output Structure

**Scraping Output**: Clean markdown files with metadata
**Processing Output**:
- `cleaned/` - Structured documents
- `chunks/` - Semantic chunks for embeddings
- `vector_db_index.json` - Ready for vector database ingestion
- Metadata and processing summaries

## Claude Code Integration

This project includes specialized agents for different aspects of the system:

- **Scraper Agent**: Web crawling and content extraction expert
- **Processor Agent**: Document post-processing and AI classification specialist
- **GUI Agent**: Tkinter interface development expert

Use `/agents` to activate specialized assistance for specific components.

## Key Features

- **Multi-threaded scraping** with rate limiting and error handling
- **LLM-powered classification** for intelligent document categorization
- **Smart chunking** optimized for embedding models
- **Dependency analysis** between documents
- **GUI interfaces** for non-technical users
- **Batch processing** for large documentation sets
- **Vector database optimization** with metadata enrichment

## Development

- **Language**: Python 3.13+
- **Testing**: Run tests with example scripts
- **GUI**: Tkinter for cross-platform compatibility
- **Async**: AsyncIO for performance
- **AI Integration**: OpenAI API for document intelligence

## File Structure

```
DocScraper/
├── DocScraper.py              # Advanced async scraper
├── SimpleDocScraper.py        # Basic sequential scraper
├── DocScraperGUI.py           # Scraping GUI
├── DocPostProcessor.py        # Core post-processing engine
├── DocPostProcessorGUI.py     # Post-processing GUI
├── process_docs_example.py    # Usage examples
├── process_multi_folder_example.py  # Multi-folder demo
├── docs/                      # Comprehensive documentation
├── requirements.txt           # Dependencies
└── .env.example              # Environment template
```

## Common Use Cases

1. **Documentation Migration**: Convert legacy docs to structured format
2. **AI Training Data**: Prepare documentation for LLM fine-tuning
3. **Vector Database Ingestion**: Create embeddings-ready content
4. **Content Curation**: Clean and organize technical documentation
5. **Knowledge Base Creation**: Build searchable documentation repositories

## Next Steps

1. Review [Architecture Documentation](./docs/architecture.md) for detailed design
2. Follow [Development Setup Guide](./docs/dev-setup.md) for contribution setup
3. Check [API Documentation](./docs/api.md) for integration details
4. Read [Testing Guide](./docs/testing.md) for quality assurance