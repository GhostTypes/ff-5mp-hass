#!/usr/bin/env python3
"""
Bulk Ruff Documentation Scraper
Scrapes all Ruff documentation pages and saves them as clean markdown files.
"""

import json
import os
import sys
import time
import cloudscraper
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urlparse
from pathlib import Path

def get_scraper():
    """Initialize cloudscraper with proper settings"""
    return cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        },
        delay=1
    )

def get_headers():
    """Get headers for requests"""
    return {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

def extract_main_content(html):
    """Extract the main documentation content from the HTML"""
    soup = BeautifulSoup(html, 'lxml')

    # Find the main content area - Ruff docs use <article> tag for main content
    main_content = soup.find('article')

    if not main_content:
        # Fallback: try to find main tag
        main_content = soup.find('main')

    if not main_content:
        # Last resort: return the whole body
        main_content = soup.find('body')

    return main_content

def clean_content(content_element):
    """Remove navigation, headers, footers, and other UI elements"""
    if not content_element:
        return None

    # Make a copy to avoid modifying the original
    content = BeautifulSoup(str(content_element), 'lxml')

    # Remove common navigation and UI elements
    elements_to_remove = [
        'nav',
        'header',
        'footer',
        '.md-header',
        '.md-footer',
        '.md-sidebar',
        '.md-nav',
        '.md-search',
        '.md-tabs',
        'script',
        'style',
        '.md-content__button',
        '.md-source',
    ]

    for selector in elements_to_remove:
        for element in content.select(selector):
            element.decompose()

    return content

def scrape_ruff_page(scraper, url):
    """
    Scrape a Ruff documentation page and return clean markdown.

    Args:
        scraper: The cloudscraper instance to use
        url: The URL to scrape

    Returns:
        String containing clean markdown content, or None on error
    """
    headers = get_headers()

    try:
        # Fetch the page
        response = scraper.get(url, headers=headers, timeout=30)

        if response.status_code != 200:
            print(f"  [WARNING] Failed to fetch (status {response.status_code})", file=sys.stderr)
            return None

        # Extract main content
        main_content = extract_main_content(response.text)

        if not main_content:
            print(f"  [WARNING] Could not find main content", file=sys.stderr)
            return None

        # Clean the content
        cleaned_content = clean_content(main_content)

        # Convert to markdown
        markdown = md(str(cleaned_content), heading_style="ATX")

        return markdown

    except Exception as e:
        print(f"  [ERROR] {str(e)}", file=sys.stderr)
        return None

def url_to_filename(url):
    """
    Convert a URL to a safe filename.

    Example:
        https://docs.astral.sh/ruff/linter/ -> linter.md
        https://docs.astral.sh/ruff/rules/unused-import/ -> rules__unused-import.md
    """
    parsed = urlparse(url)
    path = parsed.path.strip('/')

    # Remove the 'ruff/' prefix if present
    if path.startswith('ruff/'):
        path = path[5:]

    if not path:
        return 'index.md'

    # Replace slashes with double underscores
    filename = path.replace('/', '__') + '.md'

    return filename

def load_page_list(json_file):
    """Load the list of pages to scrape from JSON file"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data['pages']

def bulk_scrape(json_file, output_dir, delay=0.5, resume_from=0):
    """
    Scrape all Ruff documentation pages.

    Args:
        json_file: Path to the JSON file containing page URLs
        output_dir: Directory to save the markdown files
        delay: Delay between requests in seconds
        resume_from: Index to resume from (0 = start from beginning)
    """
    # Load page list
    pages = load_page_list(json_file)
    total = len(pages)

    print(f"Found {total} pages to scrape", file=sys.stderr)
    print(f"Output directory: {output_dir}", file=sys.stderr)
    print(f"Delay between requests: {delay}s", file=sys.stderr)

    if resume_from > 0:
        print(f"Resuming from index {resume_from}", file=sys.stderr)

    print("", file=sys.stderr)

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Initialize scraper
    scraper = get_scraper()

    # Track statistics
    success_count = 0
    error_count = 0
    skipped_count = 0

    # Scrape each page
    for i, url in enumerate(pages):
        if i < resume_from:
            skipped_count += 1
            continue

        # Generate filename
        filename = url_to_filename(url)
        filepath = os.path.join(output_dir, filename)

        # Progress indicator
        progress = f"[{i+1}/{total}]"
        short_url = url.replace('https://docs.astral.sh/ruff/', '')
        print(f"{progress} {short_url}", file=sys.stderr, end=' ... ')
        sys.stderr.flush()

        # Check if file already exists
        if os.path.exists(filepath):
            print("[SKIP] Already exists", file=sys.stderr)
            skipped_count += 1
            continue

        # Scrape the page
        markdown = scrape_ruff_page(scraper, url)

        if markdown:
            # Save to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"[SUCCESS] Saved to {filename}", file=sys.stderr)
            success_count += 1
        else:
            print(f"[FAILED]", file=sys.stderr)
            error_count += 1

        # Delay between requests to avoid rate limiting
        if i < total - 1:  # Don't delay after the last request
            time.sleep(delay)

    # Print summary
    print("", file=sys.stderr)
    print("=" * 70, file=sys.stderr)
    print("Scraping complete!", file=sys.stderr)
    print(f"  Success: {success_count}", file=sys.stderr)
    print(f"  Errors:  {error_count}", file=sys.stderr)
    print(f"  Skipped: {skipped_count}", file=sys.stderr)
    print(f"  Total:   {total}", file=sys.stderr)
    print("=" * 70, file=sys.stderr)

def main():
    if len(sys.argv) < 3:
        print("Usage: bulk_scrape_ruff.py <pages_json> <output_dir> [delay] [resume_from]", file=sys.stderr)
        print("\nArguments:", file=sys.stderr)
        print("  pages_json   - JSON file containing list of page URLs", file=sys.stderr)
        print("  output_dir   - Directory to save markdown files", file=sys.stderr)
        print("  delay        - Delay between requests in seconds (default: 0.5)", file=sys.stderr)
        print("  resume_from  - Index to resume from (default: 0)", file=sys.stderr)
        print("\nExample:", file=sys.stderr)
        print("  bulk_scrape_ruff.py pages.json ./output 0.5 0", file=sys.stderr)
        sys.exit(1)

    json_file = sys.argv[1]
    output_dir = sys.argv[2]
    delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
    resume_from = int(sys.argv[4]) if len(sys.argv) > 4 else 0

    try:
        bulk_scrape(json_file, output_dir, delay, resume_from)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. You can resume by running:", file=sys.stderr)
        print(f"  {sys.argv[0]} {json_file} {output_dir} {delay} <last_index>", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
