"""
SSENSE scraper - SSENSE has a more accessible API structure.

SSENSE is a major luxury fashion retailer with excellent brand coverage.

IMPORTANT:
- Respect rate limits and robots.txt
- Use for research/educational purposes only
"""
import json
import re
import uuid
import time
from typing import Generator, Optional, List
from bs4 import BeautifulSoup
import logging

from .base import BaseScraper
from ..models.clothing import ClothingItem, Brand

logger = logging.getLogger(__name__)


class SSENSEScraper(BaseScraper):
    """
    Scraper for SSENSE (ssense.com).

    SSENSE often has more accessible product data than End/Farfetch.
    """

    BASE_URL = "https://www.ssense.com"

    # Men's categories
    CATEGORIES = {
        'outerwear': '/en-us/men/clothing/outerwear',
        'jackets': '/en-us/men/clothing/jackets',
        'shirts': '/en-us/men/clothing/shirts',
        't-shirts': '/en-us/men/clothing/t-shirts',
        'sweaters': '/en-us/men/clothing/sweaters',
        'pants': '/en-us/men/clothing/pants',
        'jeans': '/en-us/men/clothing/jeans',
        'shorts': '/en-us/men/clothing/shorts',
        'footwear': '/en-us/men/shoes',
    }

    def __init__(self, **kwargs):
        super().__init__(delay_seconds=3.0, **kwargs)
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
        })
        self.discovered_brands = set()

    def scrape_category(
        self,
        category: str,
        max_pages: int = 10,
        max_products: int = 200,
    ) -> Generator[ClothingItem, None, None]:
        """Scrape products from a category."""
        base_path = self.CATEGORIES.get(category, category)
        page = 1
        count = 0

        while page <= max_pages and count < max_products:
            url = f"{self.BASE_URL}{base_path}?page={page}"
            logger.info(f"Scraping SSENSE {category} page {page}")

            soup = self.fetch_page(url)
            if not soup:
                break

            products = self._extract_products(soup)
            if not products:
                break

            for product in products:
                if count >= max_products:
                    break

                item = self._convert_to_item(product, category)
                if item:
                    yield item
                    count += 1

            page += 1
            time.sleep(1)

    def _extract_products(self, soup: BeautifulSoup) -> List[dict]:
        """Extract product data from SSENSE page."""
        products = []

        # SSENSE often embeds data in script tags
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(script.string)
                if isinstance(data, dict) and data.get('@type') == 'ItemList':
                    for item in data.get('itemListElement', []):
                        if item.get('@type') == 'ListItem':
                            product = item.get('item', {})
                            products.append({
                                'name': product.get('name', ''),
                                'brand': product.get('brand', {}).get('name', 'Unknown'),
                                'url': product.get('url', ''),
                                'price': self._extract_price(product),
                                'description': product.get('description', ''),
                            })
            except (json.JSONDecodeError, TypeError):
                continue

        # Fallback to HTML parsing
        if not products:
            product_cards = soup.select('[data-testid="product-tile"], .product-tile, .plp-products__product')
            for card in product_cards:
                try:
                    brand_elem = card.select_one('.product-brand, [data-testid="product-brand"]')
                    name_elem = card.select_one('.product-name, [data-testid="product-name"]')
                    link = card.find('a', href=True)
                    price_elem = card.select_one('.product-price, [data-testid="price"]')

                    brand = brand_elem.get_text(strip=True) if brand_elem else "Unknown"
                    name = name_elem.get_text(strip=True) if name_elem else "Unknown"
                    url = link['href'] if link else ""
                    if url and not url.startswith('http'):
                        url = self.BASE_URL + url

                    price = None
                    if price_elem:
                        price_text = price_elem.get_text(strip=True)
                        price_match = re.search(r'\$(\d+)', price_text)
                        if price_match:
                            price = float(price_match.group(1))

                    self.discovered_brands.add(brand)
                    products.append({
                        'brand': brand,
                        'name': name,
                        'url': url,
                        'price': price,
                        'description': name,
                    })

                except Exception:
                    continue

        return products

    def _extract_price(self, product: dict) -> Optional[float]:
        """Extract price from product data."""
        offers = product.get('offers', {})
        if isinstance(offers, dict):
            return offers.get('price')
        return None

    def _convert_to_item(self, product: dict, category: str) -> Optional[ClothingItem]:
        """Convert product dict to ClothingItem."""
        try:
            text = f"{product['name']} {product.get('description', '')}".lower()

            # Fit
            fit = None
            if 'slim' in text:
                fit = 'slim'
            elif 'oversized' in text:
                fit = 'oversized'
            elif 'relaxed' in text:
                fit = 'relaxed'
            elif 'tapered' in text:
                fit = 'tapered'

            # Colors
            colors = []
            for color in ['black', 'white', 'navy', 'grey', 'blue', 'brown', 'green']:
                if color in text:
                    colors.append(color)

            # Materials
            materials = []
            for mat in ['cotton', 'wool', 'silk', 'leather', 'denim', 'nylon', 'polyester']:
                if mat in text:
                    materials.append(mat)

            # Style tags
            style_tags = ['luxury', 'designer']  # SSENSE focuses on designer fashion
            if 'japanese' in text or 'japan' in text:
                style_tags.append('japanese')
            if 'minimal' in text:
                style_tags.append('minimalist')

            return ClothingItem(
                id=str(uuid.uuid4()),
                name=product['name'],
                brand=product['brand'],
                category=category,
                description=product.get('description', product['name']),
                fit=fit,
                style_tags=style_tags,
                colors=colors,
                materials=materials,
                source_url=product.get('url', ''),
                source_type="ssense",
                price_usd=product.get('price'),
            )
        except Exception as e:
            logger.debug(f"Error converting product: {e}")
            return None

    def scrape_products(self, url: str) -> Generator[ClothingItem, None, None]:
        """Main scraping interface."""
        if url == 'all':
            for category in self.CATEGORIES.keys():
                for item in self.scrape_category(category):
                    yield item

    def scrape_brand_info(self, brand_name: str) -> Optional[Brand]:
        """Scrape brand info."""
        return None

    def get_all_brands(self) -> List[str]:
        """Get discovered brands."""
        return list(self.discovered_brands)


def create_ssense_scraper():
    """Create SSENSE scraper."""
    return SSENSEScraper()
