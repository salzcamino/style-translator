"""
eBay scraper for finding brand items not available elsewhere.

eBay is useful for:
- Discontinued items
- Rare/vintage pieces
- Brands not stocked by major retailers
- Price research

IMPORTANT:
- Respect robots.txt and rate limits
- Use for research/educational purposes only
"""
import re
import uuid
import time
from typing import Generator, Optional, List
from bs4 import BeautifulSoup
import logging

from .base import BaseScraper
from ..models.clothing import ClothingItem, Brand

logger = logging.getLogger(__name__)


class EbayScraper(BaseScraper):
    """
    Scraper for eBay listings.

    Useful for finding brand items that aren't in major retail catalogs.
    """

    BASE_URL = "https://www.ebay.com"

    # Men's clothing categories
    CATEGORIES = {
        'jackets': 'Mens-Coats-Jackets/57988',
        'shirts': 'Mens-Casual-Shirts-Tops/57990',
        'pants': 'Mens-Pants/57989',
        'jeans': 'Mens-Jeans/11483',
        'sweaters': 'Mens-Sweaters/11484',
        'footwear': 'Mens-Shoes/93427',
    }

    def __init__(self, **kwargs):
        super().__init__(delay_seconds=2.0, **kwargs)
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml',
        })

    def search_brand(
        self,
        brand_name: str,
        category: Optional[str] = None,
        max_results: int = 100,
    ) -> Generator[ClothingItem, None, None]:
        """
        Search eBay for items from a specific brand.

        Args:
            brand_name: Brand to search for
            category: Optional category filter
            max_results: Max items to return
        """
        # Build search URL
        search_query = brand_name.replace(' ', '+')
        url = f"{self.BASE_URL}/sch/i.html?_nkw={search_query}&_sacat=1059"  # Men's clothing category

        if category and category in self.CATEGORIES:
            cat_id = self.CATEGORIES[category].split('/')[-1]
            url = f"{self.BASE_URL}/sch/i.html?_nkw={search_query}&_sacat={cat_id}"

        logger.info(f"Searching eBay for {brand_name}")
        count = 0
        page = 1

        while count < max_results:
            page_url = url if page == 1 else f"{url}&_pgn={page}"
            soup = self.fetch_page(page_url)
            if not soup:
                break

            # Find listing items
            listings = soup.select('.s-item, .srp-results .s-item__wrapper')
            if not listings:
                break

            found_on_page = 0
            for listing in listings:
                if count >= max_results:
                    break

                item = self._parse_listing(listing, brand_name)
                if item:
                    yield item
                    count += 1
                    found_on_page += 1

            if found_on_page == 0:
                break

            page += 1
            time.sleep(1)

    def _parse_listing(self, listing, brand_name: str) -> Optional[ClothingItem]:
        """Parse a single eBay listing."""
        try:
            # Title
            title_elem = listing.select_one('.s-item__title, .s-item__info a')
            if not title_elem:
                return None

            title = title_elem.get_text(strip=True)
            if title.lower() == 'shop on ebay':
                return None

            # Skip if brand name not in title
            if brand_name.lower() not in title.lower():
                return None

            # URL
            link = listing.find('a', href=True)
            url = link['href'] if link else ""

            # Price
            price_elem = listing.select_one('.s-item__price')
            price = None
            if price_elem:
                price_text = price_elem.get_text(strip=True)
                # Extract first price if range
                price_match = re.search(r'\$(\d+(?:\.\d{2})?)', price_text)
                if price_match:
                    price = float(price_match.group(1))

            # Parse item details from title
            category = self._infer_category(title)
            attrs = self._parse_attributes(title)

            return ClothingItem(
                id=str(uuid.uuid4()),
                name=title,
                brand=brand_name,
                category=category,
                description=title,
                fit=attrs.get('fit'),
                style_tags=attrs.get('style_tags', []),
                colors=attrs.get('colors', []),
                materials=attrs.get('materials', []),
                source_url=url,
                source_type="ebay",
                price_usd=price,
            )

        except Exception as e:
            logger.debug(f"Error parsing eBay listing: {e}")
            return None

    def _infer_category(self, title: str) -> str:
        """Infer category from title."""
        title_lower = title.lower()

        categories = {
            'jacket': ['jacket', 'coat', 'blazer', 'parka', 'bomber'],
            'pants': ['pants', 'trousers', 'chinos', 'slacks'],
            'jeans': ['jeans', 'denim pants', 'jean'],
            'shirt': ['shirt', 'button up', 'oxford', 'flannel'],
            't-shirt': ['t-shirt', 'tee', 'tshirt'],
            'sweater': ['sweater', 'cardigan', 'knit', 'pullover'],
            'hoodie': ['hoodie', 'hooded', 'sweatshirt'],
            'shorts': ['shorts'],
            'shoes': ['shoes', 'boots', 'sneakers', 'loafers'],
        }

        for cat, keywords in categories.items():
            if any(kw in title_lower for kw in keywords):
                return cat

        return 'other'

    def _parse_attributes(self, title: str) -> dict:
        """Parse style attributes from listing title."""
        title_lower = title.lower()

        # Fit
        fit = None
        if 'slim' in title_lower:
            fit = 'slim'
        elif 'relaxed' in title_lower:
            fit = 'relaxed'
        elif 'oversized' in title_lower:
            fit = 'oversized'
        elif 'tapered' in title_lower:
            fit = 'tapered'

        # Colors
        colors = []
        color_words = ['black', 'navy', 'blue', 'grey', 'olive', 'khaki', 'white', 'brown', 'indigo']
        for color in color_words:
            if color in title_lower:
                colors.append(color)

        # Materials
        materials = []
        material_words = ['cotton', 'wool', 'denim', 'leather', 'nylon', 'linen']
        for mat in material_words:
            if mat in title_lower:
                materials.append(mat)

        # Style tags
        style_tags = []
        if 'vintage' in title_lower:
            style_tags.append('vintage')
        if 'rare' in title_lower:
            style_tags.append('rare')
        if 'japan' in title_lower:
            style_tags.append('japanese')

        return {
            'fit': fit,
            'colors': colors,
            'materials': materials,
            'style_tags': style_tags,
        }

    def find_missing_brands(
        self,
        brand_list: List[str],
        existing_items: List[ClothingItem],
        min_items_per_brand: int = 5,
    ) -> Generator[ClothingItem, None, None]:
        """
        Find items for brands that have less than minimum items in existing data.

        Args:
            brand_list: List of brand names to check
            existing_items: Existing clothing items
            min_items_per_brand: Minimum items needed per brand
        """
        # Count existing items per brand
        brand_counts = {}
        for item in existing_items:
            brand_counts[item.brand] = brand_counts.get(item.brand, 0) + 1

        # Find underrepresented brands
        for brand in brand_list:
            current_count = brand_counts.get(brand, 0)
            if current_count < min_items_per_brand:
                needed = min_items_per_brand - current_count
                logger.info(f"Searching eBay for {brand} (have {current_count}, need {needed} more)")

                for item in self.search_brand(brand, max_results=needed):
                    yield item

    def scrape_products(self, url: str) -> Generator[ClothingItem, None, None]:
        """
        Standard interface for scraping.
        """
        # Parse brand from URL if possible
        if 'nkw=' in url:
            brand_match = re.search(r'nkw=([^&]+)', url)
            if brand_match:
                brand_name = brand_match.group(1).replace('+', ' ')
                for item in self.search_brand(brand_name):
                    yield item

    def scrape_brand_info(self, brand_name: str) -> Optional[Brand]:
        """
        eBay doesn't have brand pages, but we can infer info from listings.
        """
        items = list(self.search_brand(brand_name, max_results=20))
        if not items:
            return None

        # Aggregate info from items
        all_categories = set()
        all_colors = set()
        all_materials = set()
        prices = []

        for item in items:
            all_categories.add(item.category)
            all_colors.update(item.colors)
            all_materials.update(item.materials)
            if item.price_usd:
                prices.append(item.price_usd)

        # Determine price range
        price_range = 'mid'
        if prices:
            avg_price = sum(prices) / len(prices)
            if avg_price > 500:
                price_range = 'luxury'
            elif avg_price > 200:
                price_range = 'premium'
            elif avg_price < 50:
                price_range = 'budget'

        return Brand(
            id=str(uuid.uuid4()),
            name=brand_name,
            description=f"Brand found via eBay listings. Known for {', '.join(list(all_categories)[:3])}.",
            aesthetics=list(all_materials)[:5],
            typical_fits=[],
            price_range=price_range,
            origin_country=None,
            signature_items=list(all_categories),
            similar_brands=[],
        )


def create_ebay_scraper():
    """Create eBay scraper instance."""
    return EbayScraper()
