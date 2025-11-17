"""
Semantic embedding and search engine using sentence-transformers and ChromaDB.
This is the core of the Style Translator - it understands the meaning behind style descriptions.
"""
import os
from typing import Any, Optional
import logging

try:
    from sentence_transformers import SentenceTransformer
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False

try:
    import chromadb
    from chromadb.config import Settings
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False

from ..models.clothing import ClothingItem, Brand, StyleDiscussion

logger = logging.getLogger(__name__)


def _serialize_metadata(metadata: dict) -> dict:
    """
    Convert metadata dict to ChromaDB-compatible format.
    ChromaDB only supports str, int, float, bool, or None values.
    Lists are converted to JSON strings.
    """
    import json
    serialized = {}
    for key, value in metadata.items():
        if isinstance(value, list):
            # Convert lists to JSON strings
            serialized[key] = json.dumps(value)
        else:
            serialized[key] = value
    return serialized


def _deserialize_metadata(metadata: dict) -> dict:
    """
    Convert ChromaDB metadata back to original format.
    JSON strings that represent lists are converted back.
    """
    import json
    deserialized = {}
    for key, value in metadata.items():
        if isinstance(value, str) and value.startswith('['):
            try:
                deserialized[key] = json.loads(value)
            except json.JSONDecodeError:
                deserialized[key] = value
        else:
            deserialized[key] = value
    return deserialized


class StyleSearchEngine:
    """
    Semantic search engine for finding clothing items based on style descriptions.

    Uses sentence-transformers to create embeddings that capture the semantic meaning
    of style descriptions, not just keywords. For example, "relaxed fit" and "loose cut"
    will be understood as similar concepts.
    """

    # Recommended model - good balance of quality and speed
    # Other options:
    # - 'all-mpnet-base-v2': Higher quality but slower
    # - 'paraphrase-MiniLM-L6-v2': Faster but lower quality
    DEFAULT_MODEL = 'all-MiniLM-L6-v2'

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL,
        persist_directory: str = "./data/vectors",
    ):
        """
        Initialize the search engine.

        Args:
            model_name: Name of the sentence-transformers model to use
            persist_directory: Directory to store the vector database
        """
        if not SENTENCE_TRANSFORMERS_AVAILABLE:
            raise ImportError(
                "sentence-transformers not installed. "
                "Run: pip install sentence-transformers"
            )

        if not CHROMADB_AVAILABLE:
            raise ImportError(
                "chromadb not installed. "
                "Run: pip install chromadb"
            )

        logger.info(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

        # Create persist directory if it doesn't exist
        os.makedirs(persist_directory, exist_ok=True)

        # Initialize ChromaDB with persistence
        logger.info(f"Initializing vector database at: {persist_directory}")
        self.client = chromadb.PersistentClient(path=persist_directory)

        # Create collections for different data types
        self.items_collection = self.client.get_or_create_collection(
            name="clothing_items",
            metadata={"description": "Clothing items with style attributes"}
        )

        self.brands_collection = self.client.get_or_create_collection(
            name="brands",
            metadata={"description": "Brand profiles and aesthetics"}
        )

        self.discussions_collection = self.client.get_or_create_collection(
            name="discussions",
            metadata={"description": "Style discussions and recommendations"}
        )

        logger.info("Search engine initialized successfully")

    def add_items(self, items: list[ClothingItem]):
        """
        Add clothing items to the search index.

        Args:
            items: List of ClothingItem objects to index
        """
        if not items:
            return

        logger.info(f"Indexing {len(items)} clothing items...")

        # Prepare data for ChromaDB
        ids = [item.id for item in items]
        documents = [item.to_searchable_text() for item in items]
        # Serialize metadata (convert lists to JSON strings for ChromaDB)
        metadatas = [_serialize_metadata(item.to_dict()) for item in items]

        # Generate embeddings
        embeddings = self.model.encode(documents).tolist()

        # Add to collection
        self.items_collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        logger.info(f"Indexed {len(items)} items successfully")

    def add_brands(self, brands: list[Brand]):
        """
        Add brand profiles to the search index.

        Args:
            brands: List of Brand objects to index
        """
        if not brands:
            return

        logger.info(f"Indexing {len(brands)} brands...")

        ids = [brand.id for brand in brands]
        documents = [brand.to_searchable_text() for brand in brands]
        metadatas = [_serialize_metadata(brand.to_dict()) for brand in brands]

        embeddings = self.model.encode(documents).tolist()

        self.brands_collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        logger.info(f"Indexed {len(brands)} brands successfully")

    def add_discussions(self, discussions: list[StyleDiscussion]):
        """
        Add style discussions to the search index.

        Args:
            discussions: List of StyleDiscussion objects to index
        """
        if not discussions:
            return

        logger.info(f"Indexing {len(discussions)} discussions...")

        ids = [disc.id for disc in discussions]
        documents = [disc.to_searchable_text() for disc in discussions]
        metadatas = [_serialize_metadata(disc.to_dict()) for disc in discussions]

        embeddings = self.model.encode(documents).tolist()

        self.discussions_collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        logger.info(f"Indexed {len(discussions)} discussions successfully")

    def search_items(
        self,
        query: str,
        n_results: int = 10,
        filters: Optional[dict] = None,
    ) -> list[dict[str, Any]]:
        """
        Search for clothing items matching a style description.

        Args:
            query: Natural language style description
                   e.g., "Japanese workwear with relaxed fit"
            n_results: Number of results to return
            filters: Optional metadata filters (e.g., {"brand": "Orslow"})

        Returns:
            List of matching items with similarity scores
        """
        logger.info(f"Searching items for: {query}")

        # Generate query embedding
        query_embedding = self.model.encode([query]).tolist()[0]

        # Search in ChromaDB
        results = self.items_collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            where=filters,
            include=["documents", "metadatas", "distances"]
        )

        # Format results
        formatted_results = []
        if results['ids'][0]:
            for i in range(len(results['ids'][0])):
                # Convert distance to similarity score (ChromaDB uses L2 distance)
                # Lower distance = higher similarity
                distance = results['distances'][0][i]
                similarity = 1 / (1 + distance)  # Convert to 0-1 scale

                formatted_results.append({
                    'id': results['ids'][0][i],
                    'metadata': _deserialize_metadata(results['metadatas'][0][i]),
                    'similarity': round(similarity, 3),
                    'matched_text': results['documents'][0][i],
                })

        return formatted_results

    def search_brands(
        self,
        query: str,
        n_results: int = 5,
    ) -> list[dict[str, Any]]:
        """
        Search for brands matching a style aesthetic.

        Args:
            query: Style description or aesthetic
            n_results: Number of results to return

        Returns:
            List of matching brands with similarity scores
        """
        logger.info(f"Searching brands for: {query}")

        query_embedding = self.model.encode([query]).tolist()[0]

        results = self.brands_collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )

        formatted_results = []
        if results['ids'][0]:
            for i in range(len(results['ids'][0])):
                distance = results['distances'][0][i]
                similarity = 1 / (1 + distance)

                formatted_results.append({
                    'id': results['ids'][0][i],
                    'metadata': _deserialize_metadata(results['metadatas'][0][i]),
                    'similarity': round(similarity, 3),
                    'matched_text': results['documents'][0][i],
                })

        return formatted_results

    def search_discussions(
        self,
        query: str,
        n_results: int = 5,
    ) -> list[dict[str, Any]]:
        """
        Search for relevant style discussions.

        Args:
            query: Style-related question or topic
            n_results: Number of results to return

        Returns:
            List of matching discussions
        """
        logger.info(f"Searching discussions for: {query}")

        query_embedding = self.model.encode([query]).tolist()[0]

        results = self.discussions_collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )

        formatted_results = []
        if results['ids'][0]:
            for i in range(len(results['ids'][0])):
                distance = results['distances'][0][i]
                similarity = 1 / (1 + distance)

                formatted_results.append({
                    'id': results['ids'][0][i],
                    'metadata': _deserialize_metadata(results['metadatas'][0][i]),
                    'similarity': round(similarity, 3),
                    'matched_text': results['documents'][0][i],
                })

        return formatted_results

    def comprehensive_search(
        self,
        query: str,
        n_items: int = 10,
        n_brands: int = 5,
        n_discussions: int = 3,
    ) -> dict[str, list]:
        """
        Perform a comprehensive search across all collections.

        Args:
            query: Natural language style description
            n_items: Number of items to return
            n_brands: Number of brands to return
            n_discussions: Number of discussions to return

        Returns:
            Dictionary with results from all collections
        """
        return {
            'items': self.search_items(query, n_items),
            'brands': self.search_brands(query, n_brands),
            'discussions': self.search_discussions(query, n_discussions),
        }

    def get_stats(self) -> dict:
        """Get statistics about indexed data."""
        return {
            'items_count': self.items_collection.count(),
            'brands_count': self.brands_collection.count(),
            'discussions_count': self.discussions_collection.count(),
        }

    def clear_all(self):
        """Clear all indexed data. Use with caution!"""
        logger.warning("Clearing all indexed data...")
        self.client.delete_collection("clothing_items")
        self.client.delete_collection("brands")
        self.client.delete_collection("discussions")

        # Recreate empty collections
        self.items_collection = self.client.get_or_create_collection(
            name="clothing_items"
        )
        self.brands_collection = self.client.get_or_create_collection(
            name="brands"
        )
        self.discussions_collection = self.client.get_or_create_collection(
            name="discussions"
        )
        logger.info("All data cleared")
