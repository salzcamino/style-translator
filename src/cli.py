#!/usr/bin/env python3
"""
Menswear Style Translator CLI
Find clothing items and brands based on natural language style descriptions.
"""
import click
import json
import os
import sys
from pathlib import Path

# Rich for pretty terminal output
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich import print as rprint
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    rprint = print

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.models.clothing import ClothingItem, Brand, StyleDiscussion
# StyleSearchEngine is imported lazily in get_engine() to avoid slow startup

console = Console() if RICH_AVAILABLE else None


def get_engine(data_dir: str = "./data/vectors", fast: bool = False):
    """Initialize the search engine with lazy import."""
    # Lazy import to avoid loading heavy dependencies at CLI startup
    from src.embeddings.engine import StyleSearchEngine

    if fast:
        return StyleSearchEngine(
            model_name=StyleSearchEngine.FAST_MODEL,
            persist_directory=data_dir
        )
    return StyleSearchEngine(persist_directory=data_dir)


@click.group()
@click.option('--data-dir', default='./data/vectors', help='Vector database directory')
@click.pass_context
def cli(ctx, data_dir):
    """
    Menswear Style Translator - Find clothing by style description.

    Examples:
        style-translator search "Japanese workwear with earth tones"
        style-translator search "slim tapered jeans with high rise"
        style-translator brands "minimalist Scandinavian"
    """
    ctx.ensure_object(dict)
    ctx.obj['data_dir'] = data_dir


@cli.command()
@click.argument('query')
@click.option('--items', '-i', default=10, help='Number of items to return')
@click.option('--brands', '-b', default=5, help='Number of brands to return')
@click.option('--discussions', '-d', default=3, help='Number of discussions to return')
@click.pass_context
def search(ctx, query, items, brands, discussions):
    """
    Search for clothing items matching your style description.

    Examples:
        search "Japanese workwear vibes with earth tones"
        search "wide fitting pants with a slight taper"
        search "minimalist Scandinavian aesthetic, neutral colors"
    """
    data_dir = ctx.obj['data_dir']

    if console:
        console.print(f"\n[bold blue]Searching for:[/bold blue] {query}\n")
    else:
        print(f"\nSearching for: {query}\n")

    try:
        engine = get_engine(data_dir)
        results = engine.comprehensive_search(
            query, n_items=items, n_brands=brands, n_discussions=discussions
        )

        # Display items
        if results['items']:
            display_items(results['items'])

        # Display brands
        if results['brands']:
            display_brands(results['brands'])

        # Display discussions
        if results['discussions']:
            display_discussions(results['discussions'])

        if not any(results.values()):
            if console:
                console.print("[yellow]No results found. Try loading sample data first:[/yellow]")
                console.print("  style-translator load-samples")
            else:
                print("No results found. Try loading sample data first:")
                print("  style-translator load-samples")

    except Exception as e:
        if console:
            console.print(f"[red]Error:[/red] {e}")
        else:
            print(f"Error: {e}")
        sys.exit(1)


@cli.command()
@click.argument('query')
@click.option('--count', '-n', default=10, help='Number of results')
@click.pass_context
def items(ctx, query, count):
    """Search only for clothing items."""
    data_dir = ctx.obj['data_dir']

    try:
        engine = get_engine(data_dir)
        results = engine.search_items(query, n_results=count)

        if results:
            display_items(results)
        else:
            print("No items found.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


@cli.command()
@click.argument('query')
@click.option('--count', '-n', default=5, help='Number of results')
@click.pass_context
def brands(ctx, query, count):
    """Search for brands matching an aesthetic."""
    data_dir = ctx.obj['data_dir']

    try:
        engine = get_engine(data_dir)
        results = engine.search_brands(query, n_results=count)

        if results:
            display_brands(results)
        else:
            print("No brands found.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


@cli.command('load-samples')
@click.pass_context
def load_samples(ctx):
    """Load sample data into the search index."""
    data_dir = ctx.obj['data_dir']

    if console:
        console.print("[bold]Loading sample data...[/bold]\n")
    else:
        print("Loading sample data...\n")

    try:
        # Import sample data generator
        from samples.sample_data import (
            generate_sample_items,
            generate_sample_brands,
            generate_sample_discussions,
        )

        engine = get_engine(data_dir)

        # Check if data already loaded
        stats = engine.get_stats()
        if stats['items_count'] > 0:
            if console:
                console.print(f"[yellow]Data already loaded:[/yellow]")
                console.print(f"  Items: {stats['items_count']}")
                console.print(f"  Brands: {stats['brands_count']}")
                console.print(f"  Discussions: {stats['discussions_count']}")
                console.print("\nTo reload, first run: python -m src.cli clear")
            else:
                print(f"Data already loaded:")
                print(f"  Items: {stats['items_count']}")
                print(f"  Brands: {stats['brands_count']}")
                print(f"  Discussions: {stats['discussions_count']}")
                print("\nTo reload, first run: python -m src.cli clear")
            return

        # Generate and index data
        if console:
            console.print("Generating sample items...")
        items = generate_sample_items()
        engine.add_items(items)

        if console:
            console.print("Generating sample brands...")
        brands = generate_sample_brands()
        engine.add_brands(brands)

        if console:
            console.print("Generating sample discussions...")
        discussions = generate_sample_discussions()
        engine.add_discussions(discussions)

        if console:
            console.print(f"\n[green]Successfully loaded:[/green]")
            console.print(f"  {len(items)} clothing items")
            console.print(f"  {len(brands)} brand profiles")
            console.print(f"  {len(discussions)} style discussions")
            console.print("\n[bold]Try searching:[/bold]")
            console.print('  python -m src.cli search "Japanese workwear earth tones"')
            console.print('  python -m src.cli search "slim tapered high rise jeans"')
            console.print('  python -m src.cli brands "minimalist Scandinavian"')
        else:
            print(f"\nSuccessfully loaded:")
            print(f"  {len(items)} clothing items")
            print(f"  {len(brands)} brand profiles")
            print(f"  {len(discussions)} style discussions")
            print("\nTry searching:")
            print('  python -m src.cli search "Japanese workwear earth tones"')

    except Exception as e:
        if console:
            console.print(f"[red]Error loading samples:[/red] {e}")
        else:
            print(f"Error loading samples: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


@cli.command()
@click.pass_context
def stats(ctx):
    """Show statistics about indexed data."""
    data_dir = ctx.obj['data_dir']

    try:
        engine = get_engine(data_dir)
        stats = engine.get_stats()

        if console:
            console.print("[bold]Index Statistics:[/bold]\n")
            console.print(f"  Clothing Items: {stats['items_count']}")
            console.print(f"  Brands: {stats['brands_count']}")
            console.print(f"  Discussions: {stats['discussions_count']}")
        else:
            print("Index Statistics:\n")
            print(f"  Clothing Items: {stats['items_count']}")
            print(f"  Brands: {stats['brands_count']}")
            print(f"  Discussions: {stats['discussions_count']}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


@cli.command()
@click.confirmation_option(prompt='Are you sure you want to clear all indexed data?')
@click.pass_context
def clear(ctx):
    """Clear all indexed data."""
    data_dir = ctx.obj['data_dir']

    try:
        engine = get_engine(data_dir)
        engine.clear_all()

        if console:
            console.print("[green]All data cleared successfully.[/green]")
        else:
            print("All data cleared successfully.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


@cli.command()
@click.argument('json_file', type=click.Path(exists=True))
@click.option('--type', 'data_type', type=click.Choice(['items', 'brands', 'discussions']),
              required=True, help='Type of data to load')
@click.pass_context
def load_json(ctx, json_file, data_type):
    """Load data from a JSON file."""
    data_dir = ctx.obj['data_dir']

    try:
        engine = get_engine(data_dir)

        with open(json_file, 'r') as f:
            data = json.load(f)

        if data_type == 'items':
            items = [ClothingItem.from_dict(d) for d in data]
            engine.add_items(items)
            print(f"Loaded {len(items)} items")

        elif data_type == 'brands':
            brands = [Brand.from_dict(d) for d in data]
            engine.add_brands(brands)
            print(f"Loaded {len(brands)} brands")

        elif data_type == 'discussions':
            discussions = [StyleDiscussion.from_dict(d) for d in data]
            engine.add_discussions(discussions)
            print(f"Loaded {len(discussions)} discussions")

    except Exception as e:
        print(f"Error loading JSON: {e}")
        sys.exit(1)


@cli.command()
@click.option('--fast', is_flag=True, help='Use faster (but less accurate) model for quicker startup')
@click.pass_context
def interactive(ctx, fast):
    """
    Start interactive mode for fast repeated searches.

    The model stays loaded in memory, so subsequent queries are instant.
    Type 'quit' or 'exit' to leave interactive mode.

    Use --fast flag for faster startup (5-10s instead of 20s), with slightly less accurate results.
    """
    data_dir = ctx.obj['data_dir']

    model_name = "fast model (paraphrase-MiniLM-L3-v2)" if fast else "standard model (all-MiniLM-L6-v2)"
    if console:
        console.print(f"[bold]Loading {model_name}...[/bold]")
        console.print("[dim]This may take 10-30 seconds on first run...[/dim]")
    else:
        print(f"Loading {model_name}...")
        print("This may take 10-30 seconds on first run...")

    try:
        engine = get_engine(data_dir, fast=fast)
        stats = engine.get_stats()

        if stats['items_count'] == 0:
            if console:
                console.print("[yellow]No data loaded. Run 'python -m src.cli load-samples' first.[/yellow]")
            else:
                print("No data loaded. Run 'python -m src.cli load-samples' first.")
            return

        if console:
            console.print(f"[green]Ready![/green] {stats['items_count']} items, {stats['brands_count']} brands indexed.\n")
            console.print("[bold]Interactive Mode[/bold] - Type your style queries (or 'quit' to exit)")
            console.print("Examples:")
            console.print("  Japanese workwear earth tones")
            console.print("  slim tapered high rise jeans")
            console.print("  minimalist Scandinavian\n")
        else:
            print(f"Ready! {stats['items_count']} items, {stats['brands_count']} brands indexed.\n")
            print("Interactive Mode - Type your style queries (or 'quit' to exit)")

        while True:
            try:
                if console:
                    query = console.input("[bold blue]Query>[/bold blue] ").strip()
                else:
                    query = input("Query> ").strip()

                if not query:
                    continue

                if query.lower() in ('quit', 'exit', 'q'):
                    if console:
                        console.print("[dim]Goodbye![/dim]")
                    else:
                        print("Goodbye!")
                    break

                # Check for special commands
                if query.startswith('/'):
                    cmd = query[1:].lower().split()[0]
                    if cmd == 'items':
                        # Search items only
                        rest = query[len(cmd)+1:].strip()
                        if rest:
                            results = engine.search_items(rest, n_results=10)
                            display_items(results)
                    elif cmd == 'brands':
                        # Search brands only
                        rest = query[len(cmd)+1:].strip()
                        if rest:
                            results = engine.search_brands(rest, n_results=5)
                            display_brands(results)
                    elif cmd == 'help':
                        if console:
                            console.print("\n[bold]Commands:[/bold]")
                            console.print("  /items <query>  - Search only items")
                            console.print("  /brands <query> - Search only brands")
                            console.print("  /help           - Show this help")
                            console.print("  quit            - Exit interactive mode\n")
                        else:
                            print("\nCommands:")
                            print("  /items <query>  - Search only items")
                            print("  /brands <query> - Search only brands")
                            print("  /help           - Show this help")
                            print("  quit            - Exit interactive mode\n")
                    else:
                        print(f"Unknown command: {cmd}")
                    continue

                # Default: comprehensive search
                results = engine.comprehensive_search(query, n_items=5, n_brands=3, n_discussions=2)

                if results['items']:
                    display_items(results['items'])
                if results['brands']:
                    display_brands(results['brands'])
                if results['discussions']:
                    display_discussions(results['discussions'])

            except KeyboardInterrupt:
                print("\n")
                continue
            except EOFError:
                break

    except Exception as e:
        if console:
            console.print(f"[red]Error:[/red] {e}")
        else:
            print(f"Error: {e}")
        sys.exit(1)


def display_items(results: list):
    """Display clothing item results."""
    if not results:
        return

    if console and RICH_AVAILABLE:
        console.print("\n[bold green]═══ MATCHING ITEMS ═══[/bold green]\n")

        for i, result in enumerate(results, 1):
            meta = result['metadata']
            similarity = result['similarity']

            # Create item panel
            title = f"{i}. {meta['name']} by {meta['brand']}"

            content = []
            content.append(f"[bold]Category:[/bold] {meta['category']}")
            if meta.get('fit'):
                content.append(f"[bold]Fit:[/bold] {meta['fit']}")
            content.append(f"[bold]Description:[/bold] {meta['description'][:200]}...")

            if meta.get('style_tags'):
                content.append(f"[bold]Style:[/bold] {', '.join(meta['style_tags'])}")
            if meta.get('colors'):
                content.append(f"[bold]Colors:[/bold] {', '.join(meta['colors'])}")
            if meta.get('materials'):
                content.append(f"[bold]Materials:[/bold] {', '.join(meta['materials'])}")
            if meta.get('price_usd'):
                content.append(f"[bold]Price:[/bold] ${meta['price_usd']:.2f}")

            content.append(f"\n[dim]Match Score: {similarity:.1%}[/dim]")

            panel = Panel(
                "\n".join(content),
                title=f"[bold]{title}[/bold]",
                border_style="green"
            )
            console.print(panel)
    else:
        print("\n=== MATCHING ITEMS ===\n")
        for i, result in enumerate(results, 1):
            meta = result['metadata']
            print(f"{i}. {meta['name']} by {meta['brand']}")
            print(f"   Category: {meta['category']}")
            if meta.get('fit'):
                print(f"   Fit: {meta['fit']}")
            print(f"   Description: {meta['description'][:150]}...")
            if meta.get('price_usd'):
                print(f"   Price: ${meta['price_usd']:.2f}")
            print(f"   Match Score: {result['similarity']:.1%}")
            print()


def display_brands(results: list):
    """Display brand results."""
    if not results:
        return

    if console and RICH_AVAILABLE:
        console.print("\n[bold blue]═══ MATCHING BRANDS ═══[/bold blue]\n")

        for i, result in enumerate(results, 1):
            meta = result['metadata']
            similarity = result['similarity']

            content = []
            content.append(f"[bold]Description:[/bold] {meta['description'][:250]}")

            if meta.get('aesthetics'):
                content.append(f"[bold]Aesthetics:[/bold] {', '.join(meta['aesthetics'])}")
            if meta.get('typical_fits'):
                content.append(f"[bold]Typical Fits:[/bold] {', '.join(meta['typical_fits'])}")
            if meta.get('signature_items'):
                content.append(f"[bold]Known For:[/bold] {', '.join(meta['signature_items'])}")
            if meta.get('origin_country'):
                content.append(f"[bold]Origin:[/bold] {meta['origin_country']}")
            if meta.get('price_range'):
                content.append(f"[bold]Price Range:[/bold] {meta['price_range']}")
            if meta.get('similar_brands'):
                content.append(f"[bold]Similar:[/bold] {', '.join(meta['similar_brands'][:3])}")

            content.append(f"\n[dim]Match Score: {similarity:.1%}[/dim]")

            panel = Panel(
                "\n".join(content),
                title=f"[bold]{i}. {meta['name']}[/bold]",
                border_style="blue"
            )
            console.print(panel)
    else:
        print("\n=== MATCHING BRANDS ===\n")
        for i, result in enumerate(results, 1):
            meta = result['metadata']
            print(f"{i}. {meta['name']}")
            print(f"   {meta['description'][:150]}...")
            if meta.get('aesthetics'):
                print(f"   Aesthetics: {', '.join(meta['aesthetics'])}")
            print(f"   Match Score: {result['similarity']:.1%}")
            print()


def display_discussions(results: list):
    """Display discussion results."""
    if not results:
        return

    if console and RICH_AVAILABLE:
        console.print("\n[bold yellow]═══ RELATED DISCUSSIONS ═══[/bold yellow]\n")

        for i, result in enumerate(results, 1):
            meta = result['metadata']
            similarity = result['similarity']

            content = []
            if meta.get('content'):
                content.append(meta['content'][:300] + "...")
            if meta.get('mentioned_brands'):
                content.append(f"\n[bold]Mentioned Brands:[/bold] {', '.join(meta['mentioned_brands'])}")
            if meta.get('style_descriptors'):
                content.append(f"[bold]Style Tags:[/bold] {', '.join(meta['style_descriptors'])}")
            if meta.get('subreddit'):
                content.append(f"[dim]r/{meta['subreddit']} • {meta.get('upvotes', 0)} upvotes[/dim]")
            if meta.get('source_url'):
                content.append(f"[link={meta['source_url']}]{meta['source_url']}[/link]")

            content.append(f"\n[dim]Match Score: {similarity:.1%}[/dim]")

            panel = Panel(
                "\n".join(content),
                title=f"[bold]{i}. {meta['title'][:80]}[/bold]",
                border_style="yellow"
            )
            console.print(panel)
    else:
        print("\n=== RELATED DISCUSSIONS ===\n")
        for i, result in enumerate(results, 1):
            meta = result['metadata']
            print(f"{i}. {meta['title']}")
            if meta.get('content'):
                print(f"   {meta['content'][:150]}...")
            if meta.get('mentioned_brands'):
                print(f"   Brands: {', '.join(meta['mentioned_brands'])}")
            if meta.get('source_url'):
                print(f"   Link: {meta['source_url']}")
            print(f"   Match Score: {result['similarity']:.1%}")
            print()


if __name__ == '__main__':
    cli(obj={})
