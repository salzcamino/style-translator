"""
E-commerce site scrapers for menswear product data.

Note: These scrapers are designed for educational/research purposes.
Always check robots.txt and terms of service before scraping.
Many sites have APIs you should use instead when available.
"""
import re
import uuid
from typing import Generator, Optional
from bs4 import BeautifulSoup

from .base import BaseScraper
from ..models.clothing import ClothingItem, Brand


class GenericEcommerceScraper(BaseScraper):
    """
    Generic scraper that can be adapted for various e-commerce sites.
    Provides templates for common patterns in menswear sites.
    """

    def __init__(self, site_name: str = "generic", **kwargs):
        super().__init__(**kwargs)
        self.site_name = site_name

    def extract_product_from_schema(self, soup: BeautifulSoup) -> dict | None:
        """
        Extract product data from JSON-LD schema markup (common on e-commerce sites).
        This is the most reliable method as it's structured data.
        """
        import json

        schema_script = soup.find('script', type='application/ld+json')
        if schema_script:
            try:
                data = json.loads(schema_script.string)
                if isinstance(data, list):
                    # Find product schema in list
                    for item in data:
                        if item.get('@type') == 'Product':
                            return item
                elif data.get('@type') == 'Product':
                    return data
            except json.JSONDecodeError:
                pass
        return None

    def parse_product_description(self, description: str) -> dict:
        """
        Extract style attributes from product description text.
        Uses pattern matching for common menswear terminology.
        """
        description_lower = description.lower()

        # Fit patterns
        fits = []
        fit_patterns = [
            r'\b(slim|skinny|tapered|straight|relaxed|loose|oversized|regular|wide)\s*(fit|cut|leg)?\b',
            r'\b(high|mid|low)\s*rise\b',
        ]
        for pattern in fit_patterns:
            matches = re.findall(pattern, description_lower)
            fits.extend([' '.join(m).strip() for m in matches])

        # Color patterns
        colors = []
        color_words = [
            'black', 'white', 'navy', 'blue', 'grey', 'gray', 'charcoal',
            'olive', 'green', 'khaki', 'tan', 'brown', 'beige', 'cream',
            'burgundy', 'maroon', 'red', 'orange', 'yellow', 'indigo',
            'earth tone', 'neutral',
        ]
        for color in color_words:
            if color in description_lower:
                colors.append(color)

        # Material patterns
        materials = []
        material_words = [
            'cotton', 'denim', 'wool', 'linen', 'polyester', 'nylon',
            'canvas', 'twill', 'corduroy', 'flannel', 'chambray',
            'selvedge', 'raw denim', 'heavyweight', 'lightweight',
        ]
        for material in material_words:
            if material in description_lower:
                materials.append(material)

        # Style tags
        style_tags = []
        style_keywords = {
            'workwear': ['workwear', 'work wear', 'utility', 'chore'],
            'minimalist': ['minimal', 'clean lines', 'simple'],
            'streetwear': ['streetwear', 'street wear', 'urban'],
            'heritage': ['heritage', 'vintage', 'classic', 'traditional'],
            'techwear': ['technical', 'techwear', 'tech wear', 'waterproof'],
            'japanese': ['japanese', 'japan'],
            'scandinavian': ['scandinavian', 'nordic', 'scandi'],
            'americana': ['americana', 'american', 'western'],
            'military': ['military', 'surplus', 'army', 'cargo'],
        }

        for tag, keywords in style_keywords.items():
            if any(kw in description_lower for kw in keywords):
                style_tags.append(tag)

        return {
            'fits': list(set(fits)),
            'colors': list(set(colors)),
            'materials': list(set(materials)),
            'style_tags': list(set(style_tags)),
        }

    def scrape_products(self, url: str) -> Generator[ClothingItem, None, None]:
        """
        Scrape products from a product listing page.
        This is a template - adjust selectors for specific sites.
        """
        soup = self.fetch_page(url)
        if not soup:
            return

        # Try to find product cards (common patterns)
        product_selectors = [
            '.product-card',
            '.product-item',
            '[data-product]',
            '.product-grid-item',
        ]

        products = []
        for selector in product_selectors:
            products = soup.select(selector)
            if products:
                break

        for product_elem in products:
            try:
                # Extract basic info (adjust selectors as needed)
                name_elem = product_elem.select_one('.product-name, .product-title, h3, h4')
                brand_elem = product_elem.select_one('.product-brand, .brand')
                desc_elem = product_elem.select_one('.product-description, .description')
                price_elem = product_elem.select_one('.price, .product-price')

                if not name_elem:
                    continue

                name = name_elem.get_text(strip=True)
                brand = brand_elem.get_text(strip=True) if brand_elem else "Unknown"
                description = desc_elem.get_text(strip=True) if desc_elem else name

                # Parse description for style attributes
                attrs = self.parse_product_description(description)

                # Determine category from name/description
                category = self._infer_category(name + " " + description)

                # Parse price if available
                price = None
                if price_elem:
                    price_text = price_elem.get_text(strip=True)
                    price_match = re.search(r'[\$£€]?\s*(\d+(?:\.\d{2})?)', price_text)
                    if price_match:
                        price = float(price_match.group(1))

                yield ClothingItem(
                    id=str(uuid.uuid4()),
                    name=name,
                    brand=brand,
                    category=category,
                    description=description,
                    fit=attrs['fits'][0] if attrs['fits'] else None,
                    style_tags=attrs['style_tags'],
                    colors=attrs['colors'],
                    materials=attrs['materials'],
                    source_url=url,
                    source_type="scraped",
                    price_usd=price,
                )

            except Exception as e:
                continue

    def _infer_category(self, text: str) -> str:
        """Infer clothing category from text."""
        text_lower = text.lower()

        category_keywords = {
            'pants': ['pants', 'trousers', 'jeans', 'chinos', 'slacks'],
            'jacket': ['jacket', 'coat', 'blazer', 'outerwear'],
            'shirt': ['shirt', 'button-down', 'oxford', 'flannel shirt'],
            'sweater': ['sweater', 'knit', 'cardigan', 'pullover'],
            't-shirt': ['t-shirt', 'tee', 'tshirt'],
            'hoodie': ['hoodie', 'hooded sweatshirt'],
            'shorts': ['shorts'],
            'shoes': ['shoes', 'boots', 'sneakers', 'footwear'],
        }

        for category, keywords in category_keywords.items():
            if any(kw in text_lower for kw in keywords):
                return category

        return 'other'

    def scrape_brand_info(self, brand_name: str) -> Optional[Brand]:
        """
        Template for scraping brand information.
        This would need to be customized for specific brand pages.
        """
        # This is a placeholder - actual implementation would
        # fetch the brand's about page and extract information
        return None


def create_sample_scraper():
    """Create a scraper instance configured for testing."""
    return GenericEcommerceScraper(site_name="sample", delay_seconds=2.0)
