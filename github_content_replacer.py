#!/usr/bin/env python3
"""
GitHub Content URL Replacer

This script recursively scans directories for GitHub content URLs and replaces them
with the actual file content. It handles raw.githubusercontent.com URLs that point to file content.

Usage:
    python github_content_replacer.py [directory_path]

If no directory path is provided, it uses the current directory.
"""

import os
import re
import sys
import requests
import argparse
from pathlib import Path
from urllib.parse import urlparse, unquote
from typing import List, Tuple, Optional


class GitHubContentReplacer:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir).resolve()
        # Only look for raw GitHub URLs
        self.raw_github_pattern = re.compile(
            r'https?://raw\.githubusercontent\.com/([^/\s]+/[^/\s]+)(?:/[^/\s]+)*'
        )
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'GitHub-Content-Replacer/1.0'
        })
        
    def find_github_urls(self, content: str) -> List[Tuple[str, str]]:
        """Find all raw GitHub URLs in the content and return (url, replacement_content) tuples."""
        urls = []
        
        # Find raw GitHub URLs
        for match in self.raw_github_pattern.finditer(content):
            url = match.group(0)
            replacement = self.fetch_github_content(url)
            if replacement:
                urls.append((url, replacement))
        
        return urls
    
    def fetch_github_content(self, url: str) -> Optional[str]:
        """Fetch content from a raw GitHub URL."""
        try:
            print(f"Fetching content from: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
            
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error with {url}: {e}")
            return None
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single .md file, replacing GitHub URLs with content and outputting to .mdx."""
        try:
            # Only process .md files
            if file_path.suffix.lower() != '.md':
                return False
            
            # Skip README.md files
            if file_path.name.lower() == 'readme.md':
                return False
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find and replace GitHub URLs
            replacements = self.find_github_urls(content)
            
            # Create output .mdx file path
            output_path = file_path.with_suffix('.mdx')
            
            if replacements:
                print(f"Processing {file_path} - found {len(replacements)} GitHub URLs")
                
                # Apply replacements
                for url, replacement_content in replacements:
                    # Escape special regex characters in the URL
                    escaped_url = re.escape(url)
                    content = re.sub(escaped_url, replacement_content, content)
                
                print(f"Updated content and saved to {output_path}")
            else:
                print(f"Processing {file_path} - no GitHub URLs found, copying to {output_path}")
            
            # Write content to .mdx file (whether replacements were made or not)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False
    
    def scan_directory(self) -> None:
        """Recursively scan directory and process all .md files."""
        print(f"Scanning directory: {self.base_dir}")
        
        total_files = 0
        processed_files = 0
        
        for file_path in self.base_dir.rglob('*.md'):
            if file_path.is_file():
                total_files += 1
                if self.process_file(file_path):
                    processed_files += 1
        
        print(f"\nScan complete!")
        print(f"Total .md files scanned: {total_files}")
        print(f"Files processed and converted to .mdx: {processed_files}")


def main():
    parser = argparse.ArgumentParser(
        description="Replace GitHub content URLs with actual file content in .md files and output to .mdx files"
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to scan (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Validate directory
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory")
        sys.exit(1)
    
    # Create replacer and start scanning
    replacer = GitHubContentReplacer(args.directory)
    
    try:
        replacer.scan_directory()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
