#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="style-translator",
    version="1.0.0",
    description="Menswear Style Translator - Semantic search for clothing based on style descriptions",
    author="Your Name",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "sentence-transformers>=2.2.0",
        "chromadb>=0.4.0",
        "click>=8.1.0",
        "rich>=13.0.0",
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0",
        "pandas>=2.0.0",
        "ratelimit>=2.2.1",
    ],
    extras_require={
        "reddit": ["praw>=7.7.0"],
        "dev": ["pytest", "black", "flake8"],
    },
    entry_points={
        "console_scripts": [
            "style-translator=src.cli:cli",
        ],
    },
)
