# Menswear Style Translator

**Discover clothing items and brands using natural language style descriptions.**

Instead of searching by keywords like "wide pants" (which returns anything with those words), describe what you're actually looking for: "relaxed Japanese workwear vibes with earth tones" or "slim tapered jeans with high rise" — and get semantically relevant results.

## Features

- **Semantic Search**: Understands style concepts, not just keywords. "Relaxed fit" matches "loose cut", "earth tones" includes olive/tan/brown
- **Multiple Data Sources**: Clothing items, brand profiles, and community discussions
- **100% Free & Local**: Uses sentence-transformers and ChromaDB - no paid APIs, runs entirely on your machine
- **Extensible**: Scrape your own data from e-commerce sites and Reddit

## Quick Start

### 1. Installation

```bash
# Clone and enter directory
cd style-translator

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Or install as package
pip install -e .
```

### 2. Load Sample Data

The first time you run this, it will download the embedding model (~90MB):

```bash
python -m src.cli load-samples
```

### 3. Search!

```bash
# Full search (items + brands + discussions)
python -m src.cli search "Japanese workwear vibes with earth tones"

# Just items
python -m src.cli items "wide fitting pants with slight taper"

# Just brands
python -m src.cli brands "minimalist Scandinavian aesthetic"

# More examples
python -m src.cli search "slim tapered jeans with high rise"
python -m src.cli search "oversized Japanese streetwear"
python -m src.cli search "technical techwear black"
python -m src.cli search "vintage Americana heritage workwear"
```

## Example Output

```
Searching for: Japanese workwear vibes with earth tones

═══ MATCHING ITEMS ═══

┌─ 1. Fatigue Pants by Orslow ──────────────────┐
│ Category: pants                                │
│ Fit: relaxed tapered                          │
│ Description: Classic US Army fatigue pants... │
│ Style: workwear, military, japanese, heritage │
│ Colors: olive, army green                     │
│ Materials: ripstop cotton                     │
│ Price: $295.00                                │
│                                               │
│ Match Score: 87.3%                            │
└───────────────────────────────────────────────┘

═══ MATCHING BRANDS ═══

┌─ 1. Orslow ───────────────────────────────────┐
│ Japanese brand specializing in vintage...     │
│ Aesthetics: workwear, military, heritage      │
│ Known For: fatigue pants, 105 jeans           │
│ Origin: Japan                                 │
│ Price Range: premium                          │
│                                               │
│ Match Score: 82.1%                            │
└───────────────────────────────────────────────┘
```

## Architecture

```
style-translator/
├── src/
│   ├── models/          # Data models (ClothingItem, Brand, Discussion)
│   ├── embeddings/      # Semantic search engine (sentence-transformers + ChromaDB)
│   ├── scrapers/        # Web scraping modules (BeautifulSoup, PRAW)
│   └── cli.py           # Command-line interface
├── data/
│   ├── raw/             # Scraped data
│   ├── processed/       # Cleaned data
│   └── vectors/         # ChromaDB vector storage
├── samples/             # Demo dataset (20 items, 10 brands, 5 discussions)
└── requirements.txt
```

### Key Components

1. **Sentence-Transformers** (`all-MiniLM-L6-v2`)
   - Creates semantic embeddings that understand meaning
   - Runs locally, completely free
   - ~90MB model download on first use

2. **ChromaDB**
   - Local vector database for similarity search
   - Persists to disk - fast startup after initial indexing

3. **Data Models**
   - `ClothingItem`: Product with fit, colors, materials, style tags
   - `Brand`: Company profile with aesthetics and signature pieces
   - `StyleDiscussion`: Forum content with recommendations

## CLI Commands

```bash
# Main search commands
python -m src.cli search "query"              # Comprehensive search
python -m src.cli items "query"               # Search only items
python -m src.cli brands "query"              # Search only brands

# Data management
python -m src.cli load-samples                # Load demo data
python -m src.cli stats                       # Show index statistics
python -m src.cli clear                       # Clear all data
python -m src.cli load-json FILE --type items # Load custom JSON data

# Options
--data-dir PATH                               # Custom vector DB location
--items/-i N                                  # Number of items to return (default: 10)
--brands/-b N                                 # Number of brands to return (default: 5)
--discussions/-d N                            # Number of discussions (default: 3)
```

## Adding Your Own Data

### Manual JSON Import

Create a JSON file with your items:

```json
[
  {
    "id": "custom_001",
    "name": "My Favorite Pants",
    "brand": "Some Brand",
    "category": "pants",
    "description": "Detailed description of fit, style, materials...",
    "fit": "relaxed tapered",
    "style_tags": ["workwear", "japanese"],
    "colors": ["olive", "tan"],
    "materials": ["cotton", "canvas"],
    "price_usd": 150.00
  }
]
```

Then load it:

```bash
python -m src.cli load-json my_items.json --type items
```

### Scraping (Advanced)

The `src/scrapers/` directory includes templates for:

- **E-commerce sites**: `ecommerce.py` has a generic scraper that extracts product data
- **Reddit**: `reddit.py` scrapes fashion discussions (requires Reddit API credentials)

Example usage:

```python
from src.scrapers.ecommerce import GenericEcommerceScraper

scraper = GenericEcommerceScraper()
for item in scraper.scrape_products("https://example.com/products"):
    print(item.name, item.brand)
```

**Important**: Always respect robots.txt and terms of service. Use reasonable delays between requests.

## How It Works

1. **Embedding**: Each item/brand is converted to text describing all its attributes:
   ```
   Fatigue Pants | by Orslow | pants | Classic US Army fatigue pants... |
   relaxed tapered fit | Style: workwear, military, japanese |
   Colors: olive, army green | Materials: ripstop cotton
   ```

2. **Vector Encoding**: Sentence-transformers converts this text to a 384-dimensional vector that captures semantic meaning

3. **Similarity Search**: Your query is also converted to a vector, and ChromaDB finds items with the most similar vectors using cosine similarity

4. **Semantic Understanding**: Because the model understands language semantically:
   - "relaxed fit" ≈ "loose cut" ≈ "oversized"
   - "earth tones" ≈ "olive" ≈ "tan" ≈ "brown"
   - "Japanese workwear" ≈ "Orslow" ≈ "military heritage"

## Sample Data Included

The demo dataset includes:

**Items (20)**:
- Japanese workwear (Orslow, Engineered Garments, Kapital)
- Scandinavian minimalist (Norse Projects, COS)
- Raw denim (3sixteen, Pure Blue Japan)
- Techwear (Arc'teryx, Acronym)
- Heritage Americana (Red Wing, Rogue Territory)
- Streetwear (Supreme, Needles)

**Brands (10)**:
- Full profiles with aesthetics, typical fits, signature items
- Price ranges from budget to luxury
- Similar brand recommendations

**Discussions (5)**:
- Reddit-style posts about style recommendations
- Mentioned brands and style descriptors extracted

## Performance Tips

- First query is slow (~2-3 seconds) as model loads into memory
- Subsequent queries are fast (~100ms)
- Index persists to disk - restart is quick after first load
- For large datasets (1000+ items), consider batch indexing

## Extending the System

### Add a new data source

```python
from src.models.clothing import ClothingItem
from src.embeddings.engine import StyleSearchEngine

# Your custom data collection logic
items = [
    ClothingItem(
        id="unique_id",
        name="Product Name",
        brand="Brand",
        category="category",
        description="Full description with style attributes",
        # ... other fields
    )
]

# Index it
engine = StyleSearchEngine()
engine.add_items(items)
```

### Different embedding model

```python
# In src/embeddings/engine.py, change DEFAULT_MODEL:
DEFAULT_MODEL = 'all-mpnet-base-v2'  # Higher quality, slower
# or
DEFAULT_MODEL = 'paraphrase-MiniLM-L3-v2'  # Faster, lower quality
```

## Dependencies

All free and open source:

- **sentence-transformers**: Local semantic embeddings
- **chromadb**: Local vector database
- **click + rich**: CLI framework with pretty output
- **beautifulsoup4**: Web scraping
- **praw**: Reddit API (optional)
- **pandas**: Data processing

## Future Enhancements

- [ ] Web interface (Flask/FastAPI)
- [ ] Image-based search (CLIP model)
- [ ] Price filtering and budget recommendations
- [ ] Outfit combination suggestions
- [ ] More sophisticated style taxonomy
- [ ] Automated daily scraping jobs

## License

MIT License - feel free to modify and use as you like.

---

Built for menswear enthusiasts who want to discover new brands and pieces based on actual style descriptions, not just keyword matching.
