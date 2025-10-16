"""
NewsAPI Integration Module

This module provides functionality to fetch real news articles from NewsAPI.org
for analysis with the fake news detector.

API: https://newsapi.org/
"""

import os
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from newsapi import NewsApiClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load NewsAPI key from environment
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", None)


def get_newsapi_client() -> Optional[NewsApiClient]:
    """
    Initialize and return NewsAPI client.
    
    Returns:
        NewsApiClient: Initialized client or None if key not available.
    
    Example:
        >>> client = get_newsapi_client()
        >>> if client:
        >>>     articles = client.get_everything(q='bitcoin')
    """
    if not NEWSAPI_KEY:
        logger.warning("NewsAPI key not found in environment variables")
        return None
    
    try:
        client = NewsApiClient(api_key=NEWSAPI_KEY)
        logger.info("✓ NewsAPI client initialized successfully")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize NewsAPI client: {e}")
        return None


def search_news(
    query: str,
    language: str = "en",
    sort_by: str = "relevancy",
    page_size: int = 10,
    from_date: Optional[str] = None
) -> Dict[str, Any]:
    """
    Search for news articles by query.
    
    Args:
        query (str): Search query (keywords, phrases)
        language (str): Language code (en, es, fr, etc.)
        sort_by (str): Sort by 'relevancy', 'popularity', or 'publishedAt'
        page_size (int): Number of articles to return (max 100)
        from_date (str): Start date (YYYY-MM-DD format)
    
    Returns:
        Dict containing:
            - status: 'ok' or 'error'
            - totalResults: Total number of results
            - articles: List of article dictionaries
    
    Example:
        >>> results = search_news("fake news detection", page_size=5)
        >>> for article in results.get('articles', []):
        >>>     print(article['title'])
    """
    client = get_newsapi_client()
    if not client:
        return {
            "status": "error",
            "message": "NewsAPI client not available",
            "articles": []
        }
    
    try:
        # Default to last 7 days if no date specified
        if not from_date:
            from_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        
        logger.info(f"Searching news for: '{query}'")
        
        response = client.get_everything(
            q=query,
            language=language,
            sort_by=sort_by,
            page_size=page_size,
            from_param=from_date
        )
        
        logger.info(f"✓ Found {response.get('totalResults', 0)} articles")
        return response
        
    except Exception as e:
        logger.error(f"Failed to search news: {e}")
        return {
            "status": "error",
            "message": str(e),
            "articles": []
        }


def get_top_headlines(
    category: Optional[str] = None,
    country: str = "us",
    page_size: int = 10
) -> Dict[str, Any]:
    """
    Get top headlines from NewsAPI.
    
    Args:
        category (str): Category - business, entertainment, general, health,
                       science, sports, technology
        country (str): Country code (us, gb, ca, au, etc.)
        page_size (int): Number of articles to return (max 100)
    
    Returns:
        Dict containing:
            - status: 'ok' or 'error'
            - totalResults: Total number of results
            - articles: List of article dictionaries
    
    Example:
        >>> headlines = get_top_headlines(category="technology", country="us")
        >>> for article in headlines.get('articles', []):
        >>>     print(article['title'])
    """
    client = get_newsapi_client()
    if not client:
        return {
            "status": "error",
            "message": "NewsAPI client not available",
            "articles": []
        }
    
    try:
        logger.info(f"Fetching top headlines: category={category}, country={country}")
        
        response = client.get_top_headlines(
            category=category,
            country=country,
            page_size=page_size
        )
        
        logger.info(f"✓ Found {response.get('totalResults', 0)} headlines")
        return response
        
    except Exception as e:
        logger.error(f"Failed to fetch headlines: {e}")
        return {
            "status": "error",
            "message": str(e),
            "articles": []
        }


def get_sources(
    category: Optional[str] = None,
    language: str = "en",
    country: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get list of news sources available in NewsAPI.
    
    Args:
        category (str): Filter by category
        language (str): Filter by language code
        country (str): Filter by country code
    
    Returns:
        Dict containing:
            - status: 'ok' or 'error'
            - sources: List of source dictionaries
    
    Example:
        >>> sources = get_sources(category="technology", language="en")
        >>> for source in sources.get('sources', []):
        >>>     print(source['name'])
    """
    client = get_newsapi_client()
    if not client:
        return {
            "status": "error",
            "message": "NewsAPI client not available",
            "sources": []
        }
    
    try:
        logger.info("Fetching news sources")
        
        response = client.get_sources(
            category=category,
            language=language,
            country=country
        )
        
        logger.info(f"✓ Found {len(response.get('sources', []))} sources")
        return response
        
    except Exception as e:
        logger.error(f"Failed to fetch sources: {e}")
        return {
            "status": "error",
            "message": str(e),
            "sources": []
        }


def format_article_for_display(article: Dict) -> Dict[str, str]:
    """
    Format article data for clean display in UI.
    
    Args:
        article (Dict): Raw article data from NewsAPI
    
    Returns:
        Dict with formatted fields
    
    Example:
        >>> article = search_news("AI")['articles'][0]
        >>> formatted = format_article_for_display(article)
        >>> print(formatted['title'])
    """
    try:
        return {
            "title": article.get("title", "No title"),
            "description": article.get("description", "No description available"),
            "content": article.get("content", ""),
            "url": article.get("url", ""),
            "source": article.get("source", {}).get("name", "Unknown"),
            "author": article.get("author", "Unknown"),
            "published": article.get("publishedAt", ""),
            "image": article.get("urlToImage", "")
        }
    except Exception as e:
        logger.error(f"Failed to format article: {e}")
        return {
            "title": "Error formatting article",
            "description": str(e),
            "content": "",
            "url": "",
            "source": "Unknown",
            "author": "Unknown",
            "published": "",
            "image": ""
        }


def extract_article_text(article: Dict) -> str:
    """
    Extract full text content from article for analysis.
    
    Args:
        article (Dict): Article data from NewsAPI
    
    Returns:
        str: Combined text from title, description, and content
    
    Example:
        >>> article = search_news("politics")['articles'][0]
        >>> text = extract_article_text(article)
        >>> # Now analyze with fake news detector
    """
    parts = []
    
    # Title
    if article.get("title"):
        parts.append(article["title"])
    
    # Description
    if article.get("description"):
        parts.append(article["description"])
    
    # Content (may be truncated by NewsAPI)
    if article.get("content"):
        parts.append(article["content"])
    
    return " ".join(parts).strip()


def is_newsapi_configured() -> bool:
    """
    Check if NewsAPI is properly configured.
    
    Returns:
        bool: True if API key is available, False otherwise
    
    Example:
        >>> if is_newsapi_configured():
        >>>     articles = search_news("breaking news")
        >>> else:
        >>>     print("Please configure NewsAPI key")
    """
    return NEWSAPI_KEY is not None and len(NEWSAPI_KEY) > 0


# Quick test function
def test_newsapi():
    """
    Test NewsAPI connection and functionality.
    
    Returns:
        bool: True if tests pass, False otherwise
    """
    print("Testing NewsAPI Integration...")
    print("=" * 50)
    
    # Test 1: Check configuration
    print("\n1. Checking API key configuration...")
    if not is_newsapi_configured():
        print("❌ NewsAPI key not configured")
        return False
    print(f"✅ API key found: {NEWSAPI_KEY[:10]}...")
    
    # Test 2: Initialize client
    print("\n2. Initializing NewsAPI client...")
    client = get_newsapi_client()
    if not client:
        print("❌ Failed to initialize client")
        return False
    print("✅ Client initialized successfully")
    
    # Test 3: Search news
    print("\n3. Searching for news articles...")
    results = search_news("technology", page_size=3)
    if results.get("status") != "ok":
        print(f"❌ Search failed: {results.get('message', 'Unknown error')}")
        return False
    articles = results.get("articles", [])
    print(f"✅ Found {len(articles)} articles")
    
    # Display sample articles
    if articles:
        print("\nSample Articles:")
        for i, article in enumerate(articles[:3], 1):
            formatted = format_article_for_display(article)
            print(f"\n  {i}. {formatted['title']}")
            print(f"     Source: {formatted['source']}")
            print(f"     URL: {formatted['url'][:50]}...")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed! NewsAPI is working correctly.")
    return True


if __name__ == "__main__":
    # Run tests when module is executed directly
    test_newsapi()
