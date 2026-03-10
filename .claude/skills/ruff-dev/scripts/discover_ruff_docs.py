#!/usr/bin/env python3
"""
Discover all Ruff documentation pages by crawling the docs site.
This script finds all documentation URLs that need to be scraped.
"""

import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import sys
from collections import deque

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

def fetch_page(scraper, url):
    """Fetch and decode a page"""
    try:
        response = scraper.get(url, headers=get_headers(), timeout=30)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Warning: Got status {response.status_code} for {url}", file=sys.stderr)
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def extract_ruff_links(html, base_url):
    """Extract all Ruff documentation links from HTML"""
    soup = BeautifulSoup(html, 'lxml')
    links = set()

    for a in soup.find_all('a', href=True):
        href = a['href']

        # Skip fragment-only links and external links (except ruff docs)
        if href.startswith('#'):
            continue
        if href.startswith('http') and 'docs.astral.sh/ruff/' not in href:
            continue

        # Make absolute URL
        full_url = urljoin(base_url, href)

        # Only include links that are part of the Ruff docs
        if full_url.startswith('https://docs.astral.sh/ruff/'):
            # Remove fragments and query params
            parsed = urlparse(full_url)
            clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            # Normalize trailing slash - keep it for directory-like URLs
            if not clean_url.endswith('/'):
                clean_url = clean_url + '/'
            links.add(clean_url)

    return links

def crawl_ruff_docs(start_url='https://docs.astral.sh/ruff/'):
    """
    Crawl the Ruff documentation site to discover all pages.
    Uses BFS to explore all linked pages.
    """
    scraper = get_scraper()

    # Track visited and to-visit URLs
    visited = set()
    to_visit = deque([start_url])
    all_pages = set()

    print("Starting crawl of Ruff documentation...", file=sys.stderr)
    print(f"Base URL: {start_url}", file=sys.stderr)
    print("", file=sys.stderr)

    while to_visit:
        url = to_visit.popleft()

        # Skip if already visited
        if url in visited:
            continue

        visited.add(url)
        print(f"Crawling: {url}", file=sys.stderr)

        # Fetch the page
        html = fetch_page(scraper, url)
        if html is None:
            continue

        # Add this page to our collection
        all_pages.add(url)

        # Extract links from this page
        links = extract_ruff_links(html, url)
        print(f"  Found {len(links)} links on this page", file=sys.stderr)

        # Add new links to queue
        new_links = 0
        for link in links:
            if link not in visited:
                to_visit.append(link)
                new_links += 1
        print(f"  Added {new_links} new links to queue", file=sys.stderr)

    return sorted(all_pages)

def main():
    """Main entry point"""
    # Get output file from command line or use default
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    else:
        output_file = 'ruff_docs_pages.json'

    print("=" * 70, file=sys.stderr)
    print("Ruff Documentation Page Discovery", file=sys.stderr)
    print("=" * 70, file=sys.stderr)
    print("", file=sys.stderr)

    # Crawl the docs
    pages = crawl_ruff_docs()

    print("", file=sys.stderr)
    print("=" * 70, file=sys.stderr)
    print(f"Discovery complete! Found {len(pages)} documentation pages", file=sys.stderr)
    print("=" * 70, file=sys.stderr)
    print("", file=sys.stderr)

    # Output results
    output = {
        'total_pages': len(pages),
        'pages': pages
    }

    # Save to JSON file
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"Results saved to: {output_file}", file=sys.stderr)
    print("", file=sys.stderr)

    # Also print the list of URLs
    print("All discovered pages:", file=sys.stderr)
    for i, page in enumerate(pages, 1):
        print(f"{i:3d}. {page}", file=sys.stderr)

if __name__ == '__main__':
    main()
