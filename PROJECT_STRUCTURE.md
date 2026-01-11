# DocumentScraper Project Structure

## Directory Layout

```
DocScraper/
├── src/
│   └── docscraper/
│       ├── core/           # Core Logic
│       │   ├── scraper.py         # Advanced Scraper (DocScraper)
│       │   ├── simple.py          # Simple Scraper
│       │   └── processor.py       # Post Processor
│       ├── cleaning/       # Cleaning Utilities
│       │   ├── cleaner.py         # Post Scraper Cleaner
│       │   ├── rules.py           # Regex Rules
│       │   ├── intelligent.py     # AI Cleaner
│       │   └── llm.py             # LLM Validator
│       ├── optimization/   # Optimization Tools
│       │   └── chunker.py         # Chunk Optimizer
│       ├── gui/            # GUI Applications
│       │   ├── scraper_gui.py     # Scraper GUI
│       │   ├── processor_gui.py   # Processor GUI
│       │   └── cleaner_gui.py     # Cleaner GUI
│       ├── cli/            # CLI Tools
│       │   └── vector.py          # Vector DB CLI
│       └── utils/          # Shared Utilities
├── tests/                  # Unit and Integration Tests
├── scripts/                # Utility Scripts & Examples
├── docs/                   # Documentation
└── config/                 # Configuration Templates
```

## Key Modules

- **Core**: Contains the main application logic for scraping and processing.
- **Cleaning**: Specialized modules for document cleaning, including LLM-based and rule-based approaches.
- **GUI**: Tkinter-based graphical interfaces.
- **CLI**: Command-line interface tools.

## Development

- Install in editable mode: `pip install -e .`
- Run tests: `pytest`
- Run GUI: `docscraper-gui` or `python src/docscraper/gui/scraper_gui.py`
