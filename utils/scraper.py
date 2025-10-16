"""
Web Scraper Module

This module provides functionality to extract text content from news article URLs
using the newspaper3k library.
"""

import logging
from typing import Optional
from newspaper import Article

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_text_from_url(url: str) -> str:
    """
    Extract article text from a given URL.
    
    Uses newspaper3k to parse and extract the main text content from news articles.
    
    Args:
        url (str): The URL of the news article to fetch
    
    Returns:
        str: Extracted article text (title + body)
    
    Raises:
        ValueError: If URL is invalid or empty
        Exception: If article cannot be downloaded or parsed
    
    Example:
        >>> text = get_text_from_url("https://example.com/news/article")
        >>> print(f"Extracted {len(text)} characters")
    """
    # Validate URL
    if not url or not url.strip():
        raise ValueError("URL cannot be empty")
    
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with http:// or https://")
    
    try:
        logger.info(f"Fetching article from: {url}")
        
        # Create Article object
        article = Article(url)
        
        # Download and parse
        article.download()
        article.parse()
        
        # Extract title and text
        title = article.title or ""
        text = article.text or ""
        
        # Combine title and text
        full_text = f"{title}\n\n{text}".strip()
        
        if not full_text:
            raise Exception("No text content could be extracted from the URL")
        
        logger.info(f"✓ Extracted {len(full_text)} characters from article")
        
        return full_text
        
    except Exception as e:
        logger.error(f"Failed to fetch article: {e}")
        raise Exception(f"Could not extract text from URL: {str(e)}")


# Demo code
if __name__ == "__main__":
    print("=" * 60)
    print("Web Scraper - Demo")
    print("=" * 60)
    
    # Test URLs (use real news sites for testing)
    test_urls = [
        "https://www.bbc.com/news",  # Example - replace with actual article URLs
    ]
    
    print("\n⚠️  Note: Replace test URLs with actual article URLs for testing")
    print("\nExample usage:")
    print("-" * 60)
    
    example_url = "https://example.com/news/article-title"
    print(f"url = '{example_url}'")
    print("text = get_text_from_url(url)")
    print("print(f'Extracted {len(text)} characters')")
    
    print("\n" + "=" * 60)
