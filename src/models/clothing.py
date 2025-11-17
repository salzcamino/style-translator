"""
Data models for clothing items, brands, and style attributes.
"""
from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime
import json


@dataclass
class ClothingItem:
    """Represents a single clothing item with its attributes."""

    id: str
    name: str
    brand: str
    category: str  # e.g., "pants", "jacket", "shirt"

    # Style descriptors (key for semantic search)
    description: str
    fit: Optional[str] = None  # e.g., "slim", "relaxed", "oversized"
    style_tags: list[str] = field(default_factory=list)  # e.g., ["workwear", "minimalist"]
    colors: list[str] = field(default_factory=list)
    materials: list[str] = field(default_factory=list)

    # Source information
    source_url: Optional[str] = None
    source_type: str = "manual"  # "manual", "scraped", "reddit"
    price_usd: Optional[float] = None

    # Metadata
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_searchable_text(self) -> str:
        """
        Combine all attributes into a single text for semantic embedding.
        This is what gets embedded for similarity search.
        """
        parts = [
            self.name,
            f"by {self.brand}",
            self.category,
            self.description,
        ]

        if self.fit:
            parts.append(f"{self.fit} fit")

        if self.style_tags:
            parts.append(f"Style: {', '.join(self.style_tags)}")

        if self.colors:
            parts.append(f"Colors: {', '.join(self.colors)}")

        if self.materials:
            parts.append(f"Materials: {', '.join(self.materials)}")

        return " | ".join(parts)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "ClothingItem":
        """Create from dictionary."""
        return cls(**data)


@dataclass
class Brand:
    """Represents a clothing brand with its aesthetic profile."""

    id: str
    name: str

    # Brand aesthetic profile
    description: str
    aesthetics: list[str] = field(default_factory=list)  # e.g., ["minimalist", "scandinavian"]
    typical_fits: list[str] = field(default_factory=list)  # e.g., ["relaxed", "oversized"]
    price_range: str = "mid"  # "budget", "mid", "premium", "luxury"
    origin_country: Optional[str] = None

    # Known for
    signature_items: list[str] = field(default_factory=list)
    similar_brands: list[str] = field(default_factory=list)

    # Source
    source_url: Optional[str] = None
    source_type: str = "manual"

    # Metadata
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_searchable_text(self) -> str:
        """Combine all attributes for semantic embedding."""
        parts = [
            self.name,
            self.description,
        ]

        if self.aesthetics:
            parts.append(f"Aesthetic: {', '.join(self.aesthetics)}")

        if self.typical_fits:
            parts.append(f"Typical fits: {', '.join(self.typical_fits)}")

        if self.signature_items:
            parts.append(f"Known for: {', '.join(self.signature_items)}")

        if self.origin_country:
            parts.append(f"From {self.origin_country}")

        parts.append(f"{self.price_range} price range")

        return " | ".join(parts)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Brand":
        """Create from dictionary."""
        return cls(**data)


@dataclass
class StyleDiscussion:
    """
    Represents a style discussion or recommendation from forums/Reddit.
    Useful for capturing community knowledge about style combinations.
    """

    id: str
    title: str
    content: str

    # Extracted style information
    mentioned_brands: list[str] = field(default_factory=list)
    mentioned_items: list[str] = field(default_factory=list)
    style_descriptors: list[str] = field(default_factory=list)

    # Source
    source_url: str = ""
    source_type: str = "reddit"  # "reddit", "blog", "forum"
    subreddit: Optional[str] = None

    # Engagement (helps with relevance)
    upvotes: int = 0
    num_comments: int = 0

    # Metadata
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_searchable_text(self) -> str:
        """Combine all text for semantic embedding."""
        parts = [self.title, self.content]

        if self.style_descriptors:
            parts.append(f"Style: {', '.join(self.style_descriptors)}")

        if self.mentioned_brands:
            parts.append(f"Brands: {', '.join(self.mentioned_brands)}")

        return " | ".join(parts)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "StyleDiscussion":
        """Create from dictionary."""
        return cls(**data)


def save_items_to_json(items: list, filepath: str):
    """Save a list of dataclass items to JSON file."""
    data = [item.to_dict() for item in items]
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def load_items_from_json(filepath: str, item_class):
    """Load items from JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return [item_class.from_dict(item) for item in data]
