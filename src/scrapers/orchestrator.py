"""
Data Pipeline Orchestrator for Production Dataset.

This module coordinates all scrapers to build a comprehensive menswear database.
It handles:
- Running multiple scrapers
- Deduplication
- Data normalization
- Gap filling with eBay fallback
- Progress tracking
"""
import json
import os
import time
import logging
from typing import List, Dict, Set, Optional
from pathlib import Path
from datetime import datetime

from ..models.clothing import ClothingItem, Brand, StyleDiscussion
from .end_clothing import EndClothingScraper
from .farfetch import FarfetchScraper
from .styleforum import StyleForumScraper
from .ebay import EbayScraper

logger = logging.getLogger(__name__)


class DataPipelineOrchestrator:
    """
    Main orchestrator for building production-level dataset.

    Coordinates scraping from multiple sources and consolidates data.
    """

    def __init__(
        self,
        output_dir: str = "./data/production",
        checkpoint_interval: int = 100,
    ):
        """
        Initialize orchestrator.

        Args:
            output_dir: Directory to save scraped data
            checkpoint_interval: Save checkpoint every N items
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.checkpoint_interval = checkpoint_interval

        # Data storage
        self.items: List[ClothingItem] = []
        self.brands: List[Brand] = []
        self.discussions: List[StyleDiscussion] = []

        # Tracking
        self.discovered_brands: Set[str] = set()
        self.item_hashes: Set[str] = set()  # For deduplication
        self.stats = {
            'items_scraped': 0,
            'brands_discovered': 0,
            'discussions_collected': 0,
            'sources': {},
            'errors': [],
        }

        # Load existing checkpoint if available
        self._load_checkpoint()

    def _item_hash(self, item: ClothingItem) -> str:
        """Generate hash for deduplication."""
        return f"{item.brand}|{item.name}|{item.category}".lower()

    def _load_checkpoint(self):
        """Load existing data from checkpoint."""
        checkpoint_file = self.output_dir / "checkpoint.json"
        if checkpoint_file.exists():
            try:
                with open(checkpoint_file, 'r') as f:
                    data = json.load(f)

                logger.info("Loading checkpoint...")
                self.items = [ClothingItem.from_dict(d) for d in data.get('items', [])]
                self.brands = [Brand.from_dict(d) for d in data.get('brands', [])]
                self.discussions = [StyleDiscussion.from_dict(d) for d in data.get('discussions', [])]
                self.stats = data.get('stats', self.stats)

                # Rebuild hashes
                for item in self.items:
                    self.item_hashes.add(self._item_hash(item))
                for brand in self.brands:
                    self.discovered_brands.add(brand.name)

                logger.info(f"Loaded {len(self.items)} items, {len(self.brands)} brands, {len(self.discussions)} discussions")

            except Exception as e:
                logger.error(f"Error loading checkpoint: {e}")

    def _save_checkpoint(self):
        """Save current state to checkpoint."""
        checkpoint_file = self.output_dir / "checkpoint.json"
        try:
            data = {
                'items': [item.to_dict() for item in self.items],
                'brands': [brand.to_dict() for brand in self.brands],
                'discussions': [disc.to_dict() for disc in self.discussions],
                'stats': self.stats,
                'timestamp': datetime.now().isoformat(),
            }

            with open(checkpoint_file, 'w') as f:
                json.dump(data, f, indent=2)

            logger.info(f"Checkpoint saved: {len(self.items)} items, {len(self.brands)} brands")

        except Exception as e:
            logger.error(f"Error saving checkpoint: {e}")

    def add_item(self, item: ClothingItem) -> bool:
        """
        Add item with deduplication.

        Returns:
            True if item was added, False if duplicate
        """
        item_hash = self._item_hash(item)
        if item_hash in self.item_hashes:
            return False

        self.items.append(item)
        self.item_hashes.add(item_hash)
        self.discovered_brands.add(item.brand)
        self.stats['items_scraped'] += 1

        # Update source stats
        source = item.source_type or 'unknown'
        self.stats['sources'][source] = self.stats['sources'].get(source, 0) + 1

        # Checkpoint
        if len(self.items) % self.checkpoint_interval == 0:
            self._save_checkpoint()

        return True

    def add_brand(self, brand: Brand) -> bool:
        """Add brand if not duplicate."""
        if brand.name in self.discovered_brands:
            return False

        self.brands.append(brand)
        self.discovered_brands.add(brand.name)
        self.stats['brands_discovered'] += 1
        return True

    def add_discussion(self, discussion: StyleDiscussion) -> bool:
        """Add discussion."""
        self.discussions.append(discussion)
        self.stats['discussions_collected'] += 1

        # Extract and track mentioned brands
        for brand in discussion.mentioned_brands:
            self.discovered_brands.add(brand)

        return True

    def scrape_end_clothing(
        self,
        categories: Optional[List[str]] = None,
        max_per_category: int = 200,
    ):
        """
        Scrape End Clothing catalog.

        Args:
            categories: List of categories to scrape (None = all)
            max_per_category: Max items per category
        """
        logger.info("=== Starting End Clothing scrape ===")
        scraper = EndClothingScraper()

        if categories is None:
            categories = list(scraper.CATEGORIES.keys())

        for category in categories:
            logger.info(f"Scraping End: {category}")
            try:
                count = 0
                for item in scraper.scrape_category(category, max_products=max_per_category):
                    if self.add_item(item):
                        count += 1
                        if count % 25 == 0:
                            logger.info(f"End {category}: {count} items")
                logger.info(f"End {category}: Total {count} new items")
            except Exception as e:
                logger.error(f"Error scraping End {category}: {e}")
                self.stats['errors'].append(f"End/{category}: {str(e)}")

        self._save_checkpoint()

    def scrape_farfetch(
        self,
        categories: Optional[List[str]] = None,
        max_per_category: int = 150,
    ):
        """
        Scrape Farfetch catalog.

        Args:
            categories: Categories to scrape
            max_per_category: Max items per category
        """
        logger.info("=== Starting Farfetch scrape ===")
        scraper = FarfetchScraper()

        if categories is None:
            categories = list(scraper.CATEGORIES.keys())

        for category in categories:
            logger.info(f"Scraping Farfetch: {category}")
            try:
                count = 0
                for item in scraper.scrape_category(category, max_products=max_per_category):
                    if self.add_item(item):
                        count += 1
                        if count % 25 == 0:
                            logger.info(f"Farfetch {category}: {count} items")
                logger.info(f"Farfetch {category}: Total {count} new items")
            except Exception as e:
                logger.error(f"Error scraping Farfetch {category}: {e}")
                self.stats['errors'].append(f"Farfetch/{category}: {str(e)}")

        self._save_checkpoint()

    def scrape_reddit(
        self,
        subreddits: Optional[List[str]] = None,
        posts_per_sub: int = 50,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):
        """
        Scrape Reddit discussions.

        Args:
            subreddits: Subreddits to scrape
            posts_per_sub: Posts to fetch per subreddit
            client_id: Reddit API client ID
            client_secret: Reddit API secret
        """
        logger.info("=== Starting Reddit scrape ===")

        try:
            from .reddit import RedditScraper

            scraper = RedditScraper(
                client_id=client_id or os.environ.get('REDDIT_CLIENT_ID', 'YOUR_CLIENT_ID'),
                client_secret=client_secret or os.environ.get('REDDIT_CLIENT_SECRET', 'YOUR_CLIENT_SECRET'),
            )

            if subreddits is None:
                subreddits = scraper.FASHION_SUBREDDITS

            for sub in subreddits:
                logger.info(f"Scraping r/{sub}")
                try:
                    count = 0
                    for discussion in scraper.get_top_posts(sub, limit=posts_per_sub, time_filter='year'):
                        if self.add_discussion(discussion):
                            count += 1
                    logger.info(f"r/{sub}: {count} discussions")
                except Exception as e:
                    logger.error(f"Error scraping r/{sub}: {e}")
                    self.stats['errors'].append(f"Reddit/{sub}: {str(e)}")

        except ImportError:
            logger.warning("PRAW not available - skipping Reddit scrape")
            self.stats['errors'].append("Reddit: PRAW not installed")

        self._save_checkpoint()

    def scrape_styleforum(
        self,
        forums: Optional[List[str]] = None,
        threads_per_forum: int = 30,
    ):
        """
        Scrape StyleForum discussions.

        Args:
            forums: Forums to scrape
            threads_per_forum: Threads to scrape per forum
        """
        logger.info("=== Starting StyleForum scrape ===")
        scraper = StyleForumScraper()

        if forums is None:
            forums = list(scraper.FORUMS.keys())

        for forum in forums:
            logger.info(f"Scraping StyleForum: {forum}")
            try:
                count = 0
                thread_count = 0
                for thread_info in scraper.scrape_forum_threads(forum, max_pages=5):
                    if thread_count >= threads_per_forum:
                        break

                    discussion = scraper.scrape_thread(thread_info)
                    if discussion and self.add_discussion(discussion):
                        count += 1
                    thread_count += 1

                logger.info(f"StyleForum {forum}: {count} discussions")

            except Exception as e:
                logger.error(f"Error scraping StyleForum {forum}: {e}")
                self.stats['errors'].append(f"StyleForum/{forum}: {str(e)}")

        self._save_checkpoint()

    def fill_brand_gaps_ebay(
        self,
        brand_list: Optional[List[str]] = None,
        min_items_per_brand: int = 3,
    ):
        """
        Use eBay to fill in items for underrepresented brands.

        Args:
            brand_list: Brands to check (None = all discovered)
            min_items_per_brand: Min items needed per brand
        """
        logger.info("=== Filling brand gaps via eBay ===")
        scraper = EbayScraper()

        if brand_list is None:
            brand_list = list(self.discovered_brands)

        # Count items per brand
        brand_counts = {}
        for item in self.items:
            brand_counts[item.brand] = brand_counts.get(item.brand, 0) + 1

        # Find underrepresented brands
        for brand in brand_list:
            current = brand_counts.get(brand, 0)
            if current < min_items_per_brand:
                needed = min_items_per_brand - current
                logger.info(f"eBay: Searching {brand} (have {current}, need {needed})")

                try:
                    count = 0
                    for item in scraper.search_brand(brand, max_results=needed):
                        if self.add_item(item):
                            count += 1
                    logger.info(f"eBay: Added {count} items for {brand}")
                except Exception as e:
                    logger.error(f"eBay error for {brand}: {e}")
                    self.stats['errors'].append(f"eBay/{brand}: {str(e)}")

        self._save_checkpoint()

    def build_brand_profiles(self):
        """Build brand profiles from collected items."""
        logger.info("=== Building brand profiles ===")

        # Group items by brand
        brand_items = {}
        for item in self.items:
            if item.brand not in brand_items:
                brand_items[item.brand] = []
            brand_items[item.brand].append(item)

        # Create brand profiles
        for brand_name, items in brand_items.items():
            if brand_name in [b.name for b in self.brands]:
                continue

            # Aggregate data
            all_categories = set()
            all_colors = set()
            all_materials = set()
            all_style_tags = set()
            all_fits = set()
            prices = []

            for item in items:
                all_categories.add(item.category)
                all_colors.update(item.colors)
                all_materials.update(item.materials)
                all_style_tags.update(item.style_tags)
                if item.fit:
                    all_fits.add(item.fit)
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

            brand = Brand(
                id=f"brand_{brand_name.lower().replace(' ', '_')}",
                name=brand_name,
                description=f"{brand_name} brand profile generated from {len(items)} items.",
                aesthetics=list(all_style_tags)[:10],
                typical_fits=list(all_fits)[:5],
                price_range=price_range,
                origin_country=None,
                signature_items=list(all_categories)[:5],
                similar_brands=[],
            )

            self.add_brand(brand)

        self._save_checkpoint()
        logger.info(f"Built {len(self.brands)} brand profiles")

    def run_full_pipeline(
        self,
        end_max_per_cat: int = 200,
        farfetch_max_per_cat: int = 150,
        reddit_posts_per_sub: int = 50,
        styleforum_threads: int = 30,
    ):
        """
        Run the complete data collection pipeline.

        Args:
            end_max_per_cat: Max items per End category
            farfetch_max_per_cat: Max items per Farfetch category
            reddit_posts_per_sub: Reddit posts per subreddit
            styleforum_threads: StyleForum threads per forum
        """
        start_time = time.time()
        logger.info("========== STARTING FULL PIPELINE ==========")
        logger.info(f"Starting with {len(self.items)} items, {len(self.brands)} brands")

        # 1. Scrape major retailers
        self.scrape_end_clothing(max_per_category=end_max_per_cat)
        self.scrape_farfetch(max_per_category=farfetch_max_per_cat)

        # 2. Scrape discussions
        self.scrape_styleforum(threads_per_forum=styleforum_threads)

        # Try Reddit (requires API keys)
        if os.environ.get('REDDIT_CLIENT_ID'):
            self.scrape_reddit(posts_per_sub=reddit_posts_per_sub)
        else:
            logger.warning("REDDIT_CLIENT_ID not set - skipping Reddit")

        # 3. Fill gaps with eBay
        self.fill_brand_gaps_ebay(min_items_per_brand=3)

        # 4. Build brand profiles
        self.build_brand_profiles()

        # 5. Save final data
        self.save_production_data()

        elapsed = time.time() - start_time
        logger.info("========== PIPELINE COMPLETE ==========")
        logger.info(f"Time elapsed: {elapsed/60:.1f} minutes")
        logger.info(f"Total items: {len(self.items)}")
        logger.info(f"Total brands: {len(self.brands)}")
        logger.info(f"Total discussions: {len(self.discussions)}")
        logger.info(f"Errors: {len(self.stats['errors'])}")

    def save_production_data(self):
        """Save final production dataset."""
        logger.info("Saving production dataset...")

        # Save as JSON files
        items_file = self.output_dir / "items.json"
        with open(items_file, 'w') as f:
            json.dump([item.to_dict() for item in self.items], f, indent=2)

        brands_file = self.output_dir / "brands.json"
        with open(brands_file, 'w') as f:
            json.dump([brand.to_dict() for brand in self.brands], f, indent=2)

        discussions_file = self.output_dir / "discussions.json"
        with open(discussions_file, 'w') as f:
            json.dump([disc.to_dict() for disc in self.discussions], f, indent=2)

        # Save stats
        stats_file = self.output_dir / "stats.json"
        with open(stats_file, 'w') as f:
            json.dump(self.stats, f, indent=2)

        logger.info(f"Data saved to {self.output_dir}")
        logger.info(f"  - {len(self.items)} items")
        logger.info(f"  - {len(self.brands)} brands")
        logger.info(f"  - {len(self.discussions)} discussions")

    def get_summary(self) -> dict:
        """Get summary statistics."""
        return {
            'total_items': len(self.items),
            'total_brands': len(self.brands),
            'total_discussions': len(self.discussions),
            'unique_brands': len(self.discovered_brands),
            'sources': self.stats['sources'],
            'errors': len(self.stats['errors']),
        }


def create_orchestrator(output_dir: str = "./data/production"):
    """Create pipeline orchestrator."""
    return DataPipelineOrchestrator(output_dir=output_dir)
