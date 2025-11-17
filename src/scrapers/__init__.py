# Scrapers package for Style Translator
# Import key scrapers for easy access

from .base import BaseScraper
from .ecommerce import GenericEcommerceScraper
from .end_clothing import EndClothingScraper
from .farfetch import FarfetchScraper
from .styleforum import StyleForumScraper
from .ebay import EbayScraper
from .orchestrator import DataPipelineOrchestrator

# Reddit scraper requires PRAW, so import conditionally
try:
    from .reddit import RedditScraper
    REDDIT_AVAILABLE = True
except ImportError:
    RedditScraper = None
    REDDIT_AVAILABLE = False

__all__ = [
    'BaseScraper',
    'GenericEcommerceScraper',
    'EndClothingScraper',
    'FarfetchScraper',
    'RedditScraper',
    'StyleForumScraper',
    'EbayScraper',
    'DataPipelineOrchestrator',
    'REDDIT_AVAILABLE',
]
