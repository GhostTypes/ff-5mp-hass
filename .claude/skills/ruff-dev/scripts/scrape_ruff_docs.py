#!/usr/bin/env python3
"""
Ruff Documentation Scraper
Scrapes Ruff docs and converts to clean markdown, removing navigation and other UI elements.
"""

import sys
import cloudscraper
from bs4 import BeautifulSoup
from markdownify import markdownify as md

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

    if not main_content:
        return None

    return main_content

def clean_content(content_element):
    """Remove navigation, headers, footers, and other UI elements"""
    if not content_element:
        return None

    # Make a copy to avoid modifying the original
    content = BeautifulSoup(str(content_element), 'lxml')

    # Remove common navigation and UI elements
    elements_to_remove = [
        'nav',  # Navigation bars
        'header',  # Headers
        'footer',  # Footers
        '.md-header',  # Material for MkDocs header
        '.md-footer',  # Material for MkDocs footer
        '.md-sidebar',  # Sidebars
        '.md-nav',  # Navigation
        '.md-search',  # Search boxes
        '.md-tabs',  # Tab navigation
        'script',  # JavaScript
        'style',  # Inline styles
        '.md-content__button',  # Edit page buttons
        '.md-source',  # Source links
    ]

    for selector in elements_to_remove:
        for element in content.select(selector):
            element.decompose()

    return content

def scrape_ruff_page(url):
    """
    Scrape a Ruff documentation page and return clean markdown.

    Args:
        url: The URL to scrape

    Returns:
        String containing clean markdown content
    """
    scraper = get_scraper()
    headers = get_headers()

    # Fetch the page
    response = scraper.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}: Status {response.status_code}")

    # Extract main content
    main_content = extract_main_content(response.text)

    if not main_content:
        raise Exception(f"Could not find main content in {url}")

    # Clean the content
    cleaned_content = clean_content(main_content)

    # Convert to markdown
    markdown = md(str(cleaned_content), heading_style="ATX")

    return markdown

def main():
    if len(sys.argv) < 2:
        print("Usage: scrape_ruff_docs.py <url> [output_file]", file=sys.stderr)
        print("\nExamples:", file=sys.stderr)
        print("  scrape_ruff_docs.py https://docs.astral.sh/ruff/linter/", file=sys.stderr)
        print("  scrape_ruff_docs.py https://docs.astral.sh/ruff/linter/ output.md", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        print(f"Scraping {url}...", file=sys.stderr)
        content = scrape_ruff_page(url)

        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Content saved to {output_file}", file=sys.stderr)
        else:
            print(content)

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
