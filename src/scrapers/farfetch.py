"""
Farfetch scraper for menswear products.

Farfetch is a global luxury fashion platform with extensive designer inventory.

IMPORTANT:
- Respect robots.txt and rate limits
- Use for research/educational purposes only
- Check Terms of Service before use
"""
import json
import re
import time
import uuid
from typing import Generator, Optional, List, Dict
from bs4 import BeautifulSoup
import logging

from .base import BaseScraper
from ..models.clothing import ClothingItem, Brand

logger = logging.getLogger(__name__)


class FarfetchScraper(BaseScraper):
    """
    Scraper for Farfetch (farfetch.com).

    Farfetch uses React with server-side rendering and has good structured data.
    """

    BASE_URL = "https://www.farfetch.com"

    # Men's categories
    CATEGORIES = {
        'jackets': '/us/shopping/men/coats-jackets/items.aspx',
        'shirts': '/us/shopping/men/shirts/items.aspx',
        't-shirts': '/us/shopping/men/t-shirts/items.aspx',
        'sweaters': '/us/shopping/men/knitwear/items.aspx',
        'pants': '/us/shopping/men/trousers/items.aspx',
        'jeans': '/us/shopping/men/jeans/items.aspx',
        'shorts': '/us/shopping/men/shorts/items.aspx',
        'hoodies': '/us/shopping/men/sweaters/items.aspx',
        'footwear': '/us/shopping/men/shoes/items.aspx',
        'accessories': '/us/shopping/men/accessories/items.aspx',
    }

    def __init__(self, **kwargs):
        super().__init__(delay_seconds=3.0, **kwargs)  # Slower rate for Farfetch
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
        })
        self.discovered_brands = set()

    def get_category_url(self, category: str, page: int = 1) -> str:
        """Build URL for category listing with pagination."""
        base_path = self.CATEGORIES.get(category, category)
        if page > 1:
            return f"{self.BASE_URL}{base_path}?page={page}"
        return f"{self.BASE_URL}{base_path}"

    def scrape_category_listing(self, category: str, max_pages: int = 30) -> Generator[dict, None, None]:
        """
        Scrape product listings from a category page.

        Farfetch pages load products via JavaScript, but initial page load
        contains some products in the HTML.
        """
        page = 1
        consecutive_empty = 0

        while page <= max_pages:
            url = self.get_category_url(category, page)
            logger.info(f"Scraping Farfetch {category} page {page}")

            soup = self.fetch_page(url)
            if not soup:
                consecutive_empty += 1
                if consecutive_empty >= 3:
                    break
                page += 1
                continue

            # Farfetch embeds product data in script tags
            products = self._extract_products_from_page(soup)

            if not products:
                consecutive_empty += 1
                if consecutive_empty >= 2:
                    logger.info(f"No more products for {category}")
                    break
                page += 1
                continue

            consecutive_empty = 0

            for product in products:
                self.discovered_brands.add(product.get('brand', 'Unknown'))
                yield product

            page += 1
            time.sleep(1.5)  # Extra delay between pages

    def _extract_products_from_page(self, soup: BeautifulSoup) -> List[dict]:
        """
        Extract product data from Farfetch page.

        Farfetch often has product data in __NEXT_DATA__ or similar JSON blobs.
        """
        products = []

        # Try to find Next.js data
        next_data = soup.find('script', id='__NEXT_DATA__')
        if next_data:
            try:
                data = json.loads(next_data.string)
                # Navigate the Next.js data structure
                if 'props' in data:
                    products = self._parse_next_data(data['props'])
            except (json.JSONDecodeError, KeyError) as e:
                logger.debug(f"Could not parse __NEXT_DATA__: {e}")

        # Fallback to HTML parsing
        if not products:
            products = self._parse_html_products(soup)

        return products

    def _parse_next_data(self, props: dict) -> List[dict]:
        """Parse products from Next.js props data."""
        products = []

        # Navigate through possible paths in Next.js data
        page_props = props.get('pageProps', {})
        initial_state = page_props.get('initialState', {})

        # Look for products in various possible locations
        listings = (
            initial_state.get('products', {}).get('items', []) or
            page_props.get('products', []) or
            initial_state.get('listing', {}).get('products', [])
        )

        for item in listings:
            if isinstance(item, dict):
                product = {
                    'id': str(item.get('id', uuid.uuid4())),
                    'brand': item.get('brand', {}).get('name', 'Unknown') if isinstance(item.get('brand'), dict) else item.get('brand', 'Unknown'),
                    'name': item.get('shortDescription', item.get('name', 'Unknown')),
                    'url': self._build_product_url(item),
                    'price': self._extract_price(item),
                    'description': item.get('description', ''),
                    'colors': self._extract_colors(item),
                    'category': item.get('category', {}).get('name', 'other'),
                }
                products.append(product)

        return products

    def _parse_html_products(self, soup: BeautifulSoup) -> List[dict]:
        """Fallback: parse products from HTML structure."""
        products = []

        # Common Farfetch product card selectors
        product_cards = soup.select('[data-testid="productCard"], [class*="ProductCard"], .product-card')

        for card in product_cards:
            try:
                # Extract link
                link = card.find('a', href=True)
                if not link:
                    continue

                url = link['href']
                if not url.startswith('http'):
                    url = self.BASE_URL + url

                # Brand
                brand_elem = card.select_one('[data-testid="productDesigner"], [class*="Designer"]')
                brand = brand_elem.get_text(strip=True) if brand_elem else "Unknown"

                # Name
                name_elem = card.select_one('[data-testid="productDescription"], [class*="Description"]')
                name = name_elem.get_text(strip=True) if name_elem else "Unknown"

                # Price
                price_elem = card.select_one('[data-testid="price"], [class*="Price"]')
                price = None
                if price_elem:
                    price_text = price_elem.get_text(strip=True)
                    price_match = re.search(r'\$(\d+(?:,\d{3})*(?:\.\d{2})?)', price_text)
                    if price_match:
                        price = float(price_match.group(1).replace(',', ''))

                products.append({
                    'brand': brand,
                    'name': name,
                    'url': url,
                    'price': price,
                    'description': name,
                    'colors': [],
                    'category': 'other',
                })

            except Exception as e:
                logger.debug(f"Error parsing product card: {e}")
                continue

        return products

    def _build_product_url(self, item: dict) -> str:
        """Build product URL from item data."""
        if 'url' in item:
            url = item['url']
            if not url.startswith('http'):
                return self.BASE_URL + url
            return url

        # Construct from ID/slug
        product_id = item.get('id', '')
        slug = item.get('slug', item.get('shortDescription', '').lower().replace(' ', '-'))
        return f"{self.BASE_URL}/us/shopping/item-{product_id}.aspx"

    def _extract_price(self, item: dict) -> Optional[float]:
        """Extract price from product data."""
        price_info = item.get('priceInfo', item.get('price', {}))
        if isinstance(price_info, dict):
            return price_info.get('finalPrice', price_info.get('current', {}).get('value'))
        elif isinstance(price_info, (int, float)):
            return float(price_info)
        return None

    def _extract_colors(self, item: dict) -> List[str]:
        """Extract colors from product data."""
        colors = []
        color_data = item.get('colors', item.get('availableColors', []))
        if isinstance(color_data, list):
            for c in color_data:
                if isinstance(c, dict):
                    colors.append(c.get('name', c.get('color', '')))
                elif isinstance(c, str):
                    colors.append(c)
        elif isinstance(color_data, str):
            colors.append(color_data)
        return [c.lower() for c in colors if c]

    def scrape_products(self, url: str) -> Generator[ClothingItem, None, None]:
        """
        Main product scraping interface.
        """
        if url == 'all':
            for category in self.CATEGORIES.keys():
                for product in self.scrape_category(category):
                    yield product
        else:
            # Single category
            category = self._infer_category_from_url(url)
            for product_info in self.scrape_category_listing(category):
                item = self._convert_to_clothing_item(product_info)
                if item:
                    yield item

    def scrape_category(self, category: str, max_pages: int = 15, max_products: int = 400) -> Generator[ClothingItem, None, None]:
        """
        Scrape all products in a category.
        """
        count = 0
        for product_info in self.scrape_category_listing(category, max_pages):
            if count >= max_products:
                break

            item = self._convert_to_clothing_item(product_info, category)
            if item:
                yield item
                count += 1
                if count % 50 == 0:
                    logger.info(f"Scraped {count} products from Farfetch {category}")

    def _convert_to_clothing_item(self, product_info: dict, category: str = 'other') -> Optional[ClothingItem]:
        """Convert scraped product info to ClothingItem."""
        try:
            # Parse attributes from description/name
            text = f"{product_info.get('name', '')} {product_info.get('description', '')}"
            attrs = self._parse_style_attributes(text)

            return ClothingItem(
                id=str(product_info.get('id', uuid.uuid4())),
                name=product_info.get('name', 'Unknown'),
                brand=product_info.get('brand', 'Unknown'),
                category=product_info.get('category', category),
                description=product_info.get('description', product_info.get('name', '')),
                fit=attrs.get('fit'),
                style_tags=attrs.get('style_tags', []),
                colors=product_info.get('colors', []) or attrs.get('colors', []),
                materials=attrs.get('materials', []),
                source_url=product_info.get('url', ''),
                source_type="farfetch",
                price_usd=product_info.get('price'),
            )
        except Exception as e:
            logger.debug(f"Error converting product: {e}")
            return None

    def _parse_style_attributes(self, text: str) -> dict:
        """Parse style attributes from text."""
        text_lower = text.lower()

        # Fit
        fit = None
        if 'slim' in text_lower:
            fit = 'slim'
        elif 'oversized' in text_lower or 'oversize' in text_lower:
            fit = 'oversized'
        elif 'relaxed' in text_lower:
            fit = 'relaxed'
        elif 'tapered' in text_lower:
            fit = 'tapered'
        elif 'straight' in text_lower:
            fit = 'straight'
        elif 'wide' in text_lower:
            fit = 'wide'

        # Colors
        colors = []
        color_words = ['black', 'white', 'navy', 'blue', 'grey', 'gray', 'brown', 'green', 'red', 'beige', 'cream']
        for color in color_words:
            if color in text_lower:
                colors.append(color)

        # Materials
        materials = []
        material_words = ['cotton', 'wool', 'silk', 'cashmere', 'leather', 'suede', 'linen', 'denim', 'polyester', 'nylon']
        for mat in material_words:
            if mat in text_lower:
                materials.append(mat)

        # Style tags
        style_tags = []
        if any(word in text_lower for word in ['luxury', 'designer', 'premium']):
            style_tags.append('luxury')
        if any(word in text_lower for word in ['minimal', 'clean', 'simple']):
            style_tags.append('minimalist')
        if any(word in text_lower for word in ['italian', 'italy']):
            style_tags.append('italian')

        return {
            'fit': fit,
            'colors': colors,
            'materials': materials,
            'style_tags': style_tags,
        }

    def _infer_category_from_url(self, url: str) -> str:
        """Infer category from URL."""
        for cat, path in self.CATEGORIES.items():
            if path in url:
                return cat
        return 'other'

    def scrape_brand_info(self, brand_name: str) -> Optional[Brand]:
        """Scrape brand information from Farfetch."""
        # Farfetch has designer pages
        brand_slug = brand_name.lower().replace(' ', '-').replace("'", '')
        url = f"{self.BASE_URL}/us/designers/{brand_slug}"

        soup = self.fetch_page(url)
        if not soup:
            return None

        try:
            desc_elem = soup.select_one('.designer-description, [class*="DesignerDescription"]')
            description = desc_elem.get_text(strip=True) if desc_elem else ""

            return Brand(
                id=str(uuid.uuid4()),
                name=brand_name,
                description=description,
                aesthetics=['luxury'],
                typical_fits=[],
                price_range='luxury',
                origin_country=None,
                signature_items=[],
                similar_brands=[],
            )

        except Exception as e:
            logger.error(f"Error scraping brand {brand_name}: {e}")
            return None

    def get_all_brands(self) -> List[str]:
        """Get list of discovered brands."""
        return list(self.discovered_brands)


def create_farfetch_scraper():
    """Create Farfetch scraper instance."""
    return FarfetchScraper()
