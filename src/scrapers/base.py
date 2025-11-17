"""
Base scraper class with common functionality.
"""
import requests
from bs4 import BeautifulSoup
import time
from abc import ABC, abstractmethod
from typing import Generator
import logging
from ratelimit import limits, sleep_and_retry

logger = logging.getLogger(__name__)


class BaseScraper(ABC):
    """Base class for all scrapers."""

    def __init__(self, delay_seconds: float = 1.0):
        """
        Initialize scraper with polite delay between requests.

        Args:
            delay_seconds: Minimum delay between requests to be respectful
        """
        self.delay_seconds = delay_seconds
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'StyleTranslator/1.0 (Educational/Research Purpose)',
        })

    @sleep_and_retry
    @limits(calls=10, period=60)  # Max 10 requests per minute
    def fetch_page(self, url: str) -> BeautifulSoup | None:
        """
        Fetch a page and return BeautifulSoup object.

        Args:
            url: URL to fetch

        Returns:
            BeautifulSoup object or None if failed
        """
        try:
            logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            # Be polite - wait between requests
            time.sleep(self.delay_seconds)

            return BeautifulSoup(response.content, 'lxml')

        except requests.RequestException as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return None

    @abstractmethod
    def scrape_products(self, url: str) -> Generator:
        """
        Scrape products from a given URL.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def scrape_brand_info(self, brand_name: str) -> dict | None:
        """
        Scrape information about a specific brand.
        Must be implemented by subclasses.
        """
        pass
