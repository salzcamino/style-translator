"""
StyleForum scraper for menswear discussions.

StyleForum is one of the most comprehensive menswear forums with deep discussions
on brands, fit, and style.

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
from ..models.clothing import StyleDiscussion

logger = logging.getLogger(__name__)


class StyleForumScraper(BaseScraper):
    """
    Scraper for StyleForum (styleforum.net).

    StyleForum has extensive discussions on menswear brands and styles.
    """

    BASE_URL = "https://www.styleforum.net"

    # Key forums/subforums to scrape
    FORUMS = {
        'classic_menswear': '/forums/classic-menswear.2/',
        'streetwear_denim': '/forums/streetwear-and-denim.10/',
        'buying_selling': '/forums/buying-and-selling.28/',
        'buying_advice': '/forums/buying-advice.163/',
        'tailors': '/forums/tailors-and-retailers.3/',
    }

    # Popular threads to monitor
    POPULAR_THREADS = [
        'What are you wearing today',
        'Recent purchases',
        'Brand recommendations',
        'WAYWT',
    ]

    def __init__(self, **kwargs):
        super().__init__(delay_seconds=3.0, **kwargs)
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'en-US,en;q=0.9',
        })

    def scrape_forum_threads(
        self,
        forum_name: str,
        max_pages: int = 10,
    ) -> Generator[dict, None, None]:
        """
        Scrape thread listings from a forum.

        Args:
            forum_name: Key from FORUMS dict
            max_pages: Max pages to scrape

        Yields:
            Thread info dicts
        """
        base_path = self.FORUMS.get(forum_name, forum_name)

        for page in range(1, max_pages + 1):
            url = f"{self.BASE_URL}{base_path}"
            if page > 1:
                url = f"{url}page-{page}"

            logger.info(f"Scraping StyleForum {forum_name} page {page}")
            soup = self.fetch_page(url)
            if not soup:
                break

            # Find thread listings
            threads = soup.select('.structItem--thread, .discussionListItem')
            if not threads:
                break

            for thread in threads:
                try:
                    # Extract thread info
                    title_elem = thread.select_one('.structItem-title a, .title a')
                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    thread_url = title_elem.get('href', '')
                    if not thread_url.startswith('http'):
                        thread_url = self.BASE_URL + thread_url

                    # Reply count
                    replies_elem = thread.select_one('.structItem-cell--meta dd, .stats .major')
                    replies = 0
                    if replies_elem:
                        try:
                            replies = int(replies_elem.get_text(strip=True).replace(',', ''))
                        except ValueError:
                            pass

                    yield {
                        'title': title,
                        'url': thread_url,
                        'replies': replies,
                        'forum': forum_name,
                    }

                except Exception as e:
                    logger.debug(f"Error parsing thread: {e}")
                    continue

            time.sleep(1)

    def scrape_thread(self, thread_info: dict, max_posts: int = 50) -> Optional[StyleDiscussion]:
        """
        Scrape a thread and convert to StyleDiscussion.

        Args:
            thread_info: Dict with thread URL and metadata
            max_posts: Max posts to read from thread

        Returns:
            StyleDiscussion or None
        """
        soup = self.fetch_page(thread_info['url'])
        if not soup:
            return None

        try:
            # Get all post content
            posts = soup.select('.message-body, .messageContent, .bbWrapper')
            if not posts:
                return None

            # Combine post text (first post + top replies)
            all_text = []
            for i, post in enumerate(posts[:max_posts]):
                text = post.get_text(strip=True)
                if len(text) > 50:  # Skip very short posts
                    all_text.append(text)

            combined_content = "\n\n".join(all_text[:10])  # First 10 substantial posts

            # Extract brands, styles, items
            brands = self._extract_brands(combined_content)
            style_descriptors = self._extract_style_descriptors(combined_content)
            items = self._extract_items(combined_content)

            # Only create discussion if it has relevant content
            if not brands and not style_descriptors:
                return None

            return StyleDiscussion(
                id=str(uuid.uuid4()),
                title=thread_info['title'],
                content=combined_content[:5000],
                mentioned_brands=brands,
                mentioned_items=items,
                style_descriptors=style_descriptors,
                source_url=thread_info['url'],
                source_type="styleforum",
                subreddit=f"StyleForum/{thread_info['forum']}",
                upvotes=thread_info.get('replies', 0),  # Use replies as engagement metric
                num_comments=thread_info.get('replies', 0),
            )

        except Exception as e:
            logger.error(f"Error scraping thread {thread_info['url']}: {e}")
            return None

    def _extract_brands(self, text: str) -> List[str]:
        """Extract brand mentions from text."""
        # Comprehensive list of menswear brands
        brands = [
            # Japanese
            'Orslow', 'Engineered Garments', 'Kapital', 'Visvim', 'Needles',
            'Beams', 'United Arrows', 'Nanamica', 'Snow Peak', 'And Wander',
            'Comme des Garcons', 'Yohji Yamamoto', 'Issey Miyake', 'Sacai',
            'White Mountaineering', 'Porter', 'Master-Piece', 'Momotaro',
            'Pure Blue Japan', 'Iron Heart', 'The Flat Head', 'Samurai',
            'Studio D\'Artisan', 'Oni', 'Tanuki', 'Japan Blue', 'Graph Zero',

            # Italian/European Luxury
            'Brunello Cucinelli', 'Loro Piana', 'Kiton', 'Attolini', 'Isaia',
            'Boglioli', 'LBM 1911', 'Barena', 'Lardini', 'Caruso', 'Stile Latino',
            'Borrelli', 'Finamore', 'Marol', 'Mattabisch', 'Sartoria Partenopea',

            # British
            'Drake\'s', 'Private White VC', 'Sunspel', 'John Smedley', 'Mackintosh',
            'Barbour', 'Baracuta', 'Grenfell', 'Burberry', 'Aquascutum', 'Fox Brothers',
            'Holland & Holland', 'Cordings', 'Anderson & Sheppard', 'Henry Poole',

            # American Heritage
            'Alden', 'Allen Edmonds', 'Florsheim', 'Johnston & Murphy',
            'Rancourt', 'Quoddy', 'Yuketen', 'Easymoc', 'Oak Street Bootmakers',
            'Wolverine', 'White\'s Boots', 'Wesco', 'Nick\'s Boots', 'Dayton',
            'Filson', 'Pendleton', 'Schott', 'Golden Bear', 'Vanson',
            'Real McCoys', 'Buzz Rickson', 'Toys McCoy',

            # Scandinavian
            'Acne Studios', 'Our Legacy', 'Norse Projects', 'Wood Wood',
            'Arket', 'COS', 'Filippa K', 'Tiger of Sweden', 'Samsoe Samsoe',
            'Hope Stockholm', 'Elvine',

            # French
            'A.P.C.', 'Ami', 'Lemaire', 'Isabel Marant', 'Officine Generale',
            'De Bonne Facture', 'Editions M.R.', 'Arpenteur', 'Vetra',
            'Bleu de Paname', 'Paraboot',

            # Contemporary/Designer
            'Rick Owens', 'Undercover', 'Number (N)ine', 'Raf Simons',
            'Dries Van Noten', 'Maison Margiela', 'Lanvin', 'Givenchy',
            'Balenciaga', 'Vetements', 'Off-White', 'Fear of God',

            # Premium Denim
            '3sixteen', 'Rogue Territory', 'Taylor Stitch', 'Freenote Cloth',
            'Left Field NYC', 'Naked & Famous', 'N&F', 'Nudie Jeans',
            'A.G.', 'Citizens of Humanity', 'Paige',

            # Workwear/Streetwear
            'Carhartt', 'Carhartt WIP', 'Dickies', 'Stan Ray', 'Universal Works',
            'Albam', 'Folk', 'YMC', 'Nigel Cabourn', 'Monitaly', 'Arpenteur',

            # Technical
            'Arc\'teryx', 'Veilance', 'Outlier', 'Mission Workshop', 'Acronym',
            'Stone Island', 'C.P. Company',
        ]

        found = []
        text_lower = text.lower()
        for brand in brands:
            if brand.lower() in text_lower:
                found.append(brand)

        return list(set(found))

    def _extract_style_descriptors(self, text: str) -> List[str]:
        """Extract style and fit descriptors."""
        text_lower = text.lower()
        descriptors = []

        patterns = {
            'sprezzatura': ['sprezzatura', 'nonchalant', 'effortless'],
            'ivy': ['ivy', 'ivy style', 'prep', 'preppy', 'trad'],
            'sartorial': ['sartorial', 'tailoring', 'bespoke', 'MTM', 'made to measure'],
            'workwear': ['workwear', 'heritage', 'utilitarian'],
            'minimalist': ['minimalist', 'minimal', 'clean lines'],
            'slim fit': ['slim', 'slim cut', 'narrow'],
            'relaxed': ['relaxed', 'easy fit', 'loose'],
            'high rise': ['high rise', 'high waist'],
            'neapolitan': ['neapolitan', 'napoli', 'italian tailoring'],
            'british': ['british', 'savile row', 'english cut'],
            'streetwear': ['streetwear', 'street', 'urban'],
            'raw denim': ['raw denim', 'selvedge', 'selvage', 'unsanforized'],
            'goodyear welt': ['goodyear', 'blake', 'welted'],
        }

        for style, keywords in patterns.items():
            if any(kw in text_lower for kw in keywords):
                descriptors.append(style)

        return list(set(descriptors))

    def _extract_items(self, text: str) -> List[str]:
        """Extract clothing item types."""
        text_lower = text.lower()
        items = []

        item_keywords = [
            'suit', 'sport coat', 'blazer', 'odd jacket',
            'trousers', 'pants', 'chinos', 'jeans', 'denim',
            'shirt', 'dress shirt', 'ocbd', 'oxford',
            'tie', 'pocket square', 'grenadine',
            'shoes', 'boots', 'loafers', 'oxfords', 'derbies',
            'overcoat', 'topcoat', 'parka', 'jacket',
            'sweater', 'cardigan', 'knitwear',
        ]

        for item in item_keywords:
            if item in text_lower:
                items.append(item)

        return list(set(items))

    def search_threads(
        self,
        query: str,
        max_results: int = 50,
    ) -> Generator[StyleDiscussion, None, None]:
        """
        Search StyleForum for threads matching query.

        Args:
            query: Search terms
            max_results: Max results to return
        """
        # StyleForum search URL
        search_url = f"{self.BASE_URL}/search/?q={query.replace(' ', '+')}&t=thread"

        soup = self.fetch_page(search_url)
        if not soup:
            return

        # Find search results
        results = soup.select('.contentRow--thread, .searchResult')
        count = 0

        for result in results:
            if count >= max_results:
                break

            try:
                link = result.find('a', href=True)
                if not link:
                    continue

                thread_info = {
                    'title': link.get_text(strip=True),
                    'url': self.BASE_URL + link['href'] if not link['href'].startswith('http') else link['href'],
                    'replies': 0,
                    'forum': 'search',
                }

                discussion = self.scrape_thread(thread_info)
                if discussion:
                    yield discussion
                    count += 1

            except Exception as e:
                logger.debug(f"Error parsing search result: {e}")
                continue

    def scrape_products(self, url: str):
        """Not applicable for StyleForum - it's a discussion site."""
        raise NotImplementedError("StyleForum is a discussion site, not e-commerce")

    def scrape_brand_info(self, brand_name: str):
        """Search for brand discussions."""
        # Could search for brand-specific threads
        pass


def create_styleforum_scraper():
    """Create StyleForum scraper instance."""
    return StyleForumScraper()
