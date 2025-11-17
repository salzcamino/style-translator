"""
End Clothing scraper for menswear products.

End Clothing is a major UK-based retailer carrying premium and designer menswear.
This scraper extracts product data including style attributes.

IMPORTANT:
- Respect robots.txt and rate limits
- Use for research/educational purposes only
- Check Terms of Service before use
"""
import json
import re
import time
import uuid
from typing import Generator, Optional, List
from bs4 import BeautifulSoup
import logging

from .base import BaseScraper
from ..models.clothing import ClothingItem, Brand

logger = logging.getLogger(__name__)


class EndClothingScraper(BaseScraper):
    """
    Scraper for End Clothing (endclothing.com).

    End has a well-structured site with JSON-LD product data.
    """

    BASE_URL = "https://www.endclothing.com"

    # Categories to scrape with their URL paths
    # Updated URLs based on current End site structure
    CATEGORIES = {
        'jackets': '/us/men/clothing/coats-and-jackets',
        'shirts': '/us/men/clothing/shirts',
        't-shirts': '/us/men/clothing/t-shirts',
        'sweaters': '/us/men/clothing/knitwear',
        'pants': '/us/men/clothing/trousers',
        'jeans': '/us/men/clothing/jeans',
        'shorts': '/us/men/clothing/shorts',
        'hoodies': '/us/men/clothing/sweatshirts',
        'footwear': '/us/men/footwear',
    }

    def __init__(self, **kwargs):
        super().__init__(delay_seconds=3.0, **kwargs)  # Slower to avoid detection
        # More browser-like headers
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        })
        self.scraped_products = []
        self.discovered_brands = set()

    def get_category_url(self, category: str, page: int = 1) -> str:
        """Build URL for category listing with pagination."""
        base_path = self.CATEGORIES.get(category, category)
        if page > 1:
            return f"{self.BASE_URL}{base_path}?p={page}"
        return f"{self.BASE_URL}{base_path}"

    def scrape_category_listing(self, category: str, max_pages: int = 50) -> Generator[dict, None, None]:
        """
        Scrape product listings from a category page.

        Args:
            category: Category key from CATEGORIES
            max_pages: Maximum number of pages to scrape

        Yields:
            Dictionary with product URLs and basic info
        """
        page = 1
        consecutive_empty = 0

        while page <= max_pages:
            url = self.get_category_url(category, page)
            logger.info(f"Scraping {category} page {page}: {url}")

            soup = self.fetch_page(url)
            if not soup:
                consecutive_empty += 1
                if consecutive_empty >= 3:
                    break
                page += 1
                continue

            # Find product cards
            products = soup.select('[data-test-id="ProductCard"]')
            if not products:
                # Try alternative selectors
                products = soup.select('.product-card, .ProductCard, [class*="ProductCard"]')

            if not products:
                consecutive_empty += 1
                if consecutive_empty >= 2:
                    logger.info(f"No more products found for {category}")
                    break
                page += 1
                continue

            consecutive_empty = 0

            for product in products:
                try:
                    # Extract product link
                    link = product.find('a', href=True)
                    if not link:
                        continue

                    product_url = link['href']
                    if not product_url.startswith('http'):
                        product_url = self.BASE_URL + product_url

                    # Extract brand from listing
                    brand_elem = product.select_one('[data-test-id="ProductCard__brand"], .brand, [class*="brand"]')
                    brand = brand_elem.get_text(strip=True) if brand_elem else "Unknown"

                    # Extract name
                    name_elem = product.select_one('[data-test-id="ProductCard__name"], .product-name, h3')
                    name = name_elem.get_text(strip=True) if name_elem else "Unknown"

                    # Extract price
                    price_elem = product.select_one('[data-test-id="ProductCard__price"], .price')
                    price = None
                    if price_elem:
                        price_text = price_elem.get_text(strip=True)
                        price_match = re.search(r'\$(\d+(?:\.\d{2})?)', price_text)
                        if price_match:
                            price = float(price_match.group(1))

                    self.discovered_brands.add(brand)

                    yield {
                        'url': product_url,
                        'brand': brand,
                        'name': name,
                        'price': price,
                        'category': category,
                    }

                except Exception as e:
                    logger.debug(f"Error parsing product card: {e}")
                    continue

            page += 1
            # Additional delay between pages
            time.sleep(1)

    def scrape_product_detail(self, product_info: dict) -> Optional[ClothingItem]:
        """
        Scrape detailed product information from a product page.

        Args:
            product_info: Basic product info from listing

        Returns:
            ClothingItem or None if scraping fails
        """
        url = product_info['url']
        soup = self.fetch_page(url)
        if not soup:
            return None

        try:
            # Try to extract from JSON-LD schema (most reliable)
            schema_data = self._extract_schema_data(soup)

            # Get description
            description = ""
            desc_elem = soup.select_one('[data-test-id="product-description"], .product-description, [class*="description"]')
            if desc_elem:
                description = desc_elem.get_text(strip=True)
            elif schema_data and 'description' in schema_data:
                description = schema_data['description']

            # Parse style attributes from description
            attrs = self._parse_style_attributes(description, product_info['name'])

            # Extract additional details
            details = self._extract_product_details(soup)

            # Combine materials
            materials = attrs['materials']
            if details.get('composition'):
                materials.extend(details['composition'])
            materials = list(set(materials))

            # Build ClothingItem
            item = ClothingItem(
                id=str(uuid.uuid4()),
                name=product_info['name'],
                brand=product_info['brand'],
                category=product_info['category'],
                description=description or product_info['name'],
                fit=attrs['fit'],
                style_tags=attrs['style_tags'],
                colors=attrs['colors'],
                materials=materials,
                source_url=url,
                source_type="end_clothing",
                price_usd=product_info.get('price'),
            )

            return item

        except Exception as e:
            logger.error(f"Error scraping product detail {url}: {e}")
            return None

    def _extract_schema_data(self, soup: BeautifulSoup) -> dict:
        """Extract product data from JSON-LD schema."""
        scripts = soup.find_all('script', type='application/ld+json')
        for script in scripts:
            try:
                data = json.loads(script.string)
                if isinstance(data, list):
                    for item in data:
                        if item.get('@type') == 'Product':
                            return item
                elif data.get('@type') == 'Product':
                    return data
            except (json.JSONDecodeError, TypeError):
                continue
        return {}

    def _parse_style_attributes(self, description: str, name: str) -> dict:
        """Parse style attributes from product description."""
        text = f"{name} {description}".lower()

        # Fit detection
        fit = None
        fit_patterns = [
            (r'\bslim\s*(?:fit|tapered?)\b', 'slim tapered'),
            (r'\bslim\s*fit\b', 'slim'),
            (r'\btapered?\s*(?:fit|leg)?\b', 'tapered'),
            (r'\brelaxed\s*(?:fit|tapered?)?\b', 'relaxed'),
            (r'\boversized?\b', 'oversized'),
            (r'\bwide\s*(?:leg|fit)?\b', 'wide'),
            (r'\bstraight\s*(?:leg|fit)?\b', 'straight'),
            (r'\bregular\s*fit\b', 'regular'),
            (r'\bhigh\s*rise\b', 'high rise'),
            (r'\bmid\s*rise\b', 'mid rise'),
            (r'\blow\s*rise\b', 'low rise'),
        ]
        for pattern, fit_name in fit_patterns:
            if re.search(pattern, text):
                fit = fit_name
                break

        # Color detection
        colors = []
        color_words = [
            'black', 'white', 'navy', 'blue', 'grey', 'gray', 'charcoal',
            'olive', 'green', 'khaki', 'tan', 'brown', 'beige', 'cream',
            'burgundy', 'red', 'indigo', 'ecru', 'stone', 'camel',
        ]
        for color in color_words:
            if re.search(rf'\b{color}\b', text):
                colors.append(color)

        # Material detection
        materials = []
        material_words = [
            'cotton', 'denim', 'wool', 'linen', 'polyester', 'nylon',
            'canvas', 'twill', 'corduroy', 'flannel', 'chambray',
            'selvedge', 'silk', 'cashmere', 'leather', 'suede',
            'gore-tex', 'ripstop', 'fleece', 'jersey',
        ]
        for material in material_words:
            if material in text:
                materials.append(material)

        # Style tags
        style_tags = []
        style_mappings = {
            'workwear': ['workwear', 'work wear', 'utility', 'chore', 'fatigue'],
            'minimalist': ['minimal', 'clean', 'simple'],
            'streetwear': ['streetwear', 'street', 'urban'],
            'heritage': ['heritage', 'vintage', 'classic', 'traditional'],
            'techwear': ['technical', 'techwear', 'tech', 'waterproof', 'gore-tex'],
            'japanese': ['japanese', 'japan', 'tokyo'],
            'scandinavian': ['scandinavian', 'nordic', 'danish', 'swedish'],
            'americana': ['americana', 'american', 'western', 'usa'],
            'military': ['military', 'army', 'cargo', 'fatigue'],
            'contemporary': ['contemporary', 'modern'],
            'luxury': ['luxury', 'premium', 'designer'],
        }

        for tag, keywords in style_mappings.items():
            if any(kw in text for kw in keywords):
                style_tags.append(tag)

        return {
            'fit': fit,
            'colors': list(set(colors)),
            'materials': list(set(materials)),
            'style_tags': list(set(style_tags)),
        }

    def _extract_product_details(self, soup: BeautifulSoup) -> dict:
        """Extract additional product details from the page."""
        details = {
            'composition': [],
            'care': [],
            'made_in': None,
        }

        # Look for composition/materials info
        comp_elem = soup.select_one('[data-test-id="composition"], .composition, [class*="composition"]')
        if comp_elem:
            comp_text = comp_elem.get_text().lower()
            if 'cotton' in comp_text:
                details['composition'].append('cotton')
            if 'wool' in comp_text:
                details['composition'].append('wool')
            if 'polyester' in comp_text:
                details['composition'].append('polyester')

        return details

    def scrape_products(self, url: str) -> Generator[ClothingItem, None, None]:
        """
        Main product scraping interface.

        Args:
            url: Category URL or 'all' to scrape all categories
        """
        if url == 'all':
            for category in self.CATEGORIES.keys():
                for product in self.scrape_category(category):
                    yield product
        else:
            # Determine category from URL
            category = 'other'
            for cat, path in self.CATEGORIES.items():
                if path in url:
                    category = cat
                    break

            for product_info in self.scrape_category_listing(category):
                item = self.scrape_product_detail(product_info)
                if item:
                    yield item

    def scrape_category(self, category: str, max_pages: int = 20, max_products: int = 500) -> Generator[ClothingItem, None, None]:
        """
        Scrape all products in a category.

        Args:
            category: Category key
            max_pages: Max pages to scrape
            max_products: Max products to return
        """
        count = 0
        for product_info in self.scrape_category_listing(category, max_pages):
            if count >= max_products:
                break

            item = self.scrape_product_detail(product_info)
            if item:
                yield item
                count += 1
                logger.info(f"Scraped {count} products from {category}")

    def scrape_brand_info(self, brand_name: str) -> Optional[Brand]:
        """
        Scrape brand information from End's brand page.
        """
        # End has brand pages at /us/brands/[brand-name]
        brand_slug = brand_name.lower().replace(' ', '-').replace("'", '')
        url = f"{self.BASE_URL}/us/brands/{brand_slug}"

        soup = self.fetch_page(url)
        if not soup:
            return None

        try:
            # Extract brand description
            desc_elem = soup.select_one('.brand-description, [class*="brand-description"]')
            description = desc_elem.get_text(strip=True) if desc_elem else ""

            # Extract brand origin
            origin = None
            if 'japan' in description.lower():
                origin = 'Japan'
            elif 'uk' in description.lower() or 'british' in description.lower():
                origin = 'UK'
            # etc.

            return Brand(
                id=str(uuid.uuid4()),
                name=brand_name,
                description=description,
                aesthetics=[],  # Would need more parsing
                typical_fits=[],
                price_range='premium',  # End focuses on premium
                origin_country=origin,
                signature_items=[],
                similar_brands=[],
            )

        except Exception as e:
            logger.error(f"Error scraping brand {brand_name}: {e}")
            return None

    def get_all_brands(self) -> List[str]:
        """Get list of all brands available on End."""
        url = f"{self.BASE_URL}/us/brands"
        soup = self.fetch_page(url)
        if not soup:
            return list(self.discovered_brands)

        brands = []
        brand_links = soup.select('.brand-list a, [class*="brand"] a')
        for link in brand_links:
            brand_name = link.get_text(strip=True)
            if brand_name:
                brands.append(brand_name)

        return brands or list(self.discovered_brands)


def create_end_scraper():
    """Create End Clothing scraper instance."""
    return EndClothingScraper()
