"""
Reddit scraper for fashion discussions and recommendations.

Uses PRAW (Python Reddit API Wrapper) for the free Reddit API.
To use this, you'll need to:
1. Create a Reddit account
2. Go to https://www.reddit.com/prefs/apps
3. Create a "script" type application
4. Use the client_id and client_secret in your config
"""
import uuid
import re
from typing import Generator, Optional
import logging

try:
    import praw
    PRAW_AVAILABLE = True
except ImportError:
    PRAW_AVAILABLE = False

from ..models.clothing import StyleDiscussion, Brand

logger = logging.getLogger(__name__)


class RedditScraper:
    """Scraper for fashion-related Reddit content."""

    # Fashion subreddits to scrape
    FASHION_SUBREDDITS = [
        'malefashionadvice',
        'malefashion',
        'rawdenim',
        'goodyearwelt',
        'streetwear',
        'techwearclothing',
        'NavyBlazer',
        'frugalmalefashion',
    ]

    # Keywords that indicate useful style discussions
    STYLE_KEYWORDS = [
        'brand recommendation',
        'what brand',
        'where to buy',
        'similar to',
        'alternative to',
        'looking for',
        'style advice',
        'fit check',
        'fit pics',
    ]

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        user_agent: str = "StyleTranslator/1.0",
    ):
        """
        Initialize Reddit scraper.

        Args:
            client_id: Reddit API client ID (optional for read-only)
            client_secret: Reddit API secret (optional for read-only)
            user_agent: User agent string for API requests
        """
        if not PRAW_AVAILABLE:
            raise ImportError(
                "PRAW not installed. Run: pip install praw"
            )

        self.reddit = praw.Reddit(
            client_id=client_id or "YOUR_CLIENT_ID",
            client_secret=client_secret or "YOUR_CLIENT_SECRET",
            user_agent=user_agent,
        )

    def search_discussions(
        self,
        query: str,
        subreddits: Optional[list[str]] = None,
        limit: int = 25,
        time_filter: str = "year",
    ) -> Generator[StyleDiscussion, None, None]:
        """
        Search for discussions matching a query.

        Args:
            query: Search query (e.g., "japanese workwear brands")
            subreddits: List of subreddits to search (defaults to fashion subs)
            limit: Maximum number of results per subreddit
            time_filter: Time filter (hour, day, week, month, year, all)

        Yields:
            StyleDiscussion objects
        """
        subreddits = subreddits or self.FASHION_SUBREDDITS

        for sub_name in subreddits:
            try:
                subreddit = self.reddit.subreddit(sub_name)

                for submission in subreddit.search(
                    query, limit=limit, time_filter=time_filter
                ):
                    discussion = self._submission_to_discussion(submission)
                    if discussion:
                        yield discussion

            except Exception as e:
                logger.error(f"Error searching {sub_name}: {e}")
                continue

    def get_top_posts(
        self,
        subreddit_name: str,
        limit: int = 50,
        time_filter: str = "year",
    ) -> Generator[StyleDiscussion, None, None]:
        """
        Get top posts from a subreddit.

        Args:
            subreddit_name: Name of subreddit
            limit: Number of posts to fetch
            time_filter: Time filter

        Yields:
            StyleDiscussion objects
        """
        try:
            subreddit = self.reddit.subreddit(subreddit_name)

            for submission in subreddit.top(time_filter=time_filter, limit=limit):
                discussion = self._submission_to_discussion(submission)
                if discussion:
                    yield discussion

        except Exception as e:
            logger.error(f"Error fetching top posts from {subreddit_name}: {e}")

    def _submission_to_discussion(
        self, submission
    ) -> Optional[StyleDiscussion]:
        """
        Convert a Reddit submission to a StyleDiscussion object.

        Args:
            submission: PRAW submission object

        Returns:
            StyleDiscussion or None if not relevant
        """
        # Skip if no text content
        if not submission.selftext and len(submission.title) < 20:
            return None

        content = submission.selftext or ""
        full_text = f"{submission.title} {content}"

        # Extract mentioned brands
        brands = self._extract_brands(full_text)

        # Extract style descriptors
        style_descriptors = self._extract_style_descriptors(full_text)

        # Extract mentioned items
        items = self._extract_item_types(full_text)

        return StyleDiscussion(
            id=str(uuid.uuid4()),
            title=submission.title,
            content=content[:5000],  # Limit content length
            mentioned_brands=brands,
            mentioned_items=items,
            style_descriptors=style_descriptors,
            source_url=f"https://reddit.com{submission.permalink}",
            source_type="reddit",
            subreddit=submission.subreddit.display_name,
            upvotes=submission.score,
            num_comments=submission.num_comments,
        )

    def _extract_brands(self, text: str) -> list[str]:
        """Extract brand names mentioned in text."""
        # Common menswear brands - expand this list
        known_brands = [
            # Japanese
            'Uniqlo', 'Engineered Garments', 'Orslow', 'Kapital', 'Visvim',
            'Needles', 'Comme des Garcons', 'Yohji Yamamoto', 'Issey Miyake',
            'Nanamica', 'And Wander', 'Snow Peak', 'Beams', 'United Arrows',

            # Scandinavian
            'Acne Studios', 'Norse Projects', 'Our Legacy', 'Arket',
            'Filippa K', 'COS', 'Samsoe Samsoe', 'Wood Wood',

            # Heritage/Workwear
            'Carhartt', 'Carhartt WIP', 'Dickies', 'Red Wing', 'Filson',
            'Pendleton', 'Schott', 'Levi\'s', 'Wrangler', 'Lee',

            # Contemporary
            'A.P.C.', 'Acne', 'AMI', 'Sandro', 'The Kooples',
            'AllSaints', 'Theory', 'Vince', 'Rag & Bone',

            # Streetwear
            'Supreme', 'Stussy', 'Palace', 'Bape', 'Kith',
            'Noah', 'Aimé Leon Dore', 'Online Ceramics',

            # Premium Denim
            'Naked & Famous', 'Japan Blue', '3sixteen', 'Rogue Territory',
            'Iron Heart', 'The Flat Head', 'Momotaro', 'Pure Blue Japan',

            # Others
            'Patagonia', 'Arc\'teryx', 'North Face', 'Stone Island',
            'C.P. Company', 'Barbour', 'Baracuta', 'Drake\'s',
        ]

        found_brands = []
        text_lower = text.lower()

        for brand in known_brands:
            if brand.lower() in text_lower:
                found_brands.append(brand)

        return list(set(found_brands))

    def _extract_style_descriptors(self, text: str) -> list[str]:
        """Extract style-related descriptors from text."""
        text_lower = text.lower()

        descriptors = []

        # Aesthetic styles
        style_patterns = {
            'minimalist': ['minimal', 'minimalist', 'clean', 'simple'],
            'workwear': ['workwear', 'work wear', 'utility', 'chore coat'],
            'streetwear': ['streetwear', 'street style', 'hypebeast'],
            'heritage': ['heritage', 'classic', 'timeless', 'traditional'],
            'techwear': ['techwear', 'technical', 'gorpcore'],
            'japanese': ['japanese', 'japan made', 'made in japan'],
            'scandinavian': ['scandinavian', 'nordic', 'scandi'],
            'americana': ['americana', 'ivy style', 'prep'],
            'military': ['military', 'mil-spec', 'field jacket'],
            'oversized': ['oversized', 'boxy', 'loose fit'],
            'slim': ['slim fit', 'skinny', 'tapered'],
            'raw denim': ['raw denim', 'selvedge', 'unsanforized'],
        }

        for style, keywords in style_patterns.items():
            if any(kw in text_lower for kw in keywords):
                descriptors.append(style)

        # Fit descriptors
        fit_patterns = [
            r'\b(relaxed|loose|oversized|slim|tapered|straight|wide)\s+fit\b',
            r'\b(high|mid|low)\s+rise\b',
        ]

        for pattern in fit_patterns:
            matches = re.findall(pattern, text_lower)
            descriptors.extend(matches)

        return list(set(descriptors))

    def _extract_item_types(self, text: str) -> list[str]:
        """Extract clothing item types mentioned."""
        text_lower = text.lower()

        items = []
        item_keywords = [
            'jeans', 'pants', 'trousers', 'chinos',
            'jacket', 'coat', 'blazer', 'cardigan',
            'shirt', 'oxford', 'flannel', 't-shirt',
            'hoodie', 'sweatshirt', 'sweater',
            'boots', 'sneakers', 'shoes',
            'shorts', 'overalls', 'coveralls',
        ]

        for item in item_keywords:
            if item in text_lower:
                items.append(item)

        return list(set(items))


def create_reddit_scraper_without_auth() -> RedditScraper:
    """
    Create a Reddit scraper that works without authentication.
    Limited functionality but good for testing.
    """
    # Note: This will have rate limiting and some features won't work
    # For full functionality, register at https://www.reddit.com/prefs/apps
    return RedditScraper(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="StyleTranslator/1.0 (by /u/YOUR_USERNAME)",
    )
