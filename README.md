# Documentation Scraper

A web scraper designed to crawl entire documentation websites and convert them to markdown files. Perfect for creating local copies of technical documentation for offline use or LLM context.

## Features

- **Automatic URL Discovery**: Automatically discovers and crawls all documentation pages on a domain
- **Markdown Conversion**: Converts HTML content to clean markdown format
- **Domain Limiting**: Stays within the specified domain to avoid crawling external sites
- **Progress Tracking**: Real-time progress updates and summary statistics
- **Error Handling**: Gracefully handles failed pages and continues crawling
- **Rate Limiting**: Built-in delays to avoid overwhelming servers

## Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

## Usage

### Command Line

Basic usage:
```bash
python SimpleDocScraper.py <documentation_url>
```

With options:
```bash
python SimpleDocScraper.py <documentation_url> <output_dir> <max_pages>
```

Examples:
```bash
# Scrape Anthropic documentation (default: 1000 pages max, saves to 'scraped_docs')
python SimpleDocScraper.py https://docs.anthropic.com

# Scrape with custom output directory and limit
python SimpleDocScraper.py https://docs.anthropic.com anthropic_docs 500

# Scrape other documentation sites
python SimpleDocScraper.py https://docs.python.org python_docs
python SimpleDocScraper.py https://docs.github.com github_docs 200
```

### GUI Version

For a graphical interface:
```bash
python DocScraperGUI.py
```

The GUI allows you to:
- Enter the starting URL
- Choose output directory
- Set maximum pages to crawl
- View real-time progress logs
- Start/stop crawling with buttons

## Output

The scraper creates:
- Individual markdown files for each page
- A `_scrape_summary.json` file with crawl statistics
- Metadata headers in each markdown file with URL, title, and timestamp

### Directory Structure
```
output_dir/
├── index.md
├── getting-started.md
├── api_reference.md
├── guides_tutorial.md
└── _scrape_summary.json
```

## Configuration

The scraper respects:
- Same-domain policy (won't crawl external links)
- Skips non-documentation URLs (login, API endpoints, downloads)
- Adds delays between requests (2 seconds by default)
- Handles common documentation site structures

## Tips

1. **Start Small**: Test with a low `max_pages` value first
2. **Check Robots.txt**: Ensure you're allowed to crawl the target site
3. **Monitor Progress**: Watch the console output for any issues
4. **Review Output**: Check the `_scrape_summary.json` for failed URLs

## Troubleshooting

If you encounter issues:

1. **Import Errors**: Ensure all dependencies are installed in the virtual environment
2. **Network Errors**: Check your internet connection and the target site's availability
3. **Rate Limiting**: If getting 429 errors, increase the delay in the code
4. **No Content**: Some sites may require JavaScript; the scraper handles basic JS rendering

## Limitations

- Requires the target site to have proper HTML structure
- May not work with sites requiring authentication
- JavaScript-heavy SPAs might need additional configuration
- Respects rate limits to avoid being blocked

## License

This tool is for educational and personal use. Always respect website terms of service and robots.txt files.