"""
Sample dataset for testing the Style Translator.
This provides a rich set of products, brands, and discussions
to demonstrate semantic search capabilities without needing to scrape.
"""
import json
from datetime import datetime
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.clothing import ClothingItem, Brand, StyleDiscussion


def generate_sample_items() -> list[ClothingItem]:
    """Generate sample clothing items representing various styles."""
    items = [
        # Japanese Workwear
        ClothingItem(
            id="item_001",
            name="Fatigue Pants",
            brand="Orslow",
            category="pants",
            description="Classic US Army fatigue pants in ripstop fabric. Relaxed fit with slight taper. Features utility pockets and adjustable waist tabs. Made in Japan with attention to vintage military details.",
            fit="relaxed tapered",
            style_tags=["workwear", "military", "japanese", "heritage"],
            colors=["olive", "army green"],
            materials=["ripstop cotton"],
            price_usd=295.00,
        ),
        ClothingItem(
            id="item_002",
            name="Coverall Jacket",
            brand="Engineered Garments",
            category="jacket",
            description="Oversized coverall jacket in heavyweight cotton canvas. Boxy fit with multiple patch pockets. Japanese-made workwear-inspired piece with utilitarian design.",
            fit="oversized boxy",
            style_tags=["workwear", "japanese", "utilitarian"],
            colors=["navy", "khaki"],
            materials=["heavyweight cotton", "canvas"],
            price_usd=450.00,
        ),
        ClothingItem(
            id="item_003",
            name="Ring Coat",
            brand="Kapital",
            category="jacket",
            description="Indigo dyed ring coat with patchwork details. Loose fitting Japanese workwear with artisanal touches. Features hand-stitched sashiko embroidery.",
            fit="loose",
            style_tags=["japanese", "artisanal", "indigo"],
            colors=["indigo", "blue"],
            materials=["cotton", "denim"],
            price_usd=625.00,
        ),

        # Scandinavian Minimalist
        ClothingItem(
            id="item_004",
            name="Theo Trouser",
            brand="Norse Projects",
            category="pants",
            description="Clean minimal trouser in organic cotton twill. Regular fit with straight leg. Simple Scandinavian design with hidden details. Perfect for minimalist wardrobe.",
            fit="regular straight",
            style_tags=["minimalist", "scandinavian", "clean"],
            colors=["black", "navy", "beige"],
            materials=["organic cotton", "twill"],
            price_usd=185.00,
        ),
        ClothingItem(
            id="item_005",
            name="Kyle Oxford Shirt",
            brand="Norse Projects",
            category="shirt",
            description="Relaxed fit oxford shirt in brushed cotton. Clean minimal design with no chest pocket. Button-down collar with subtle Scandinavian detailing.",
            fit="relaxed",
            style_tags=["minimalist", "scandinavian", "casual"],
            colors=["white", "light blue", "pale pink"],
            materials=["brushed cotton", "oxford cloth"],
            price_usd=145.00,
        ),
        ClothingItem(
            id="item_006",
            name="Relaxed Merino Sweater",
            brand="COS",
            category="sweater",
            description="Oversized merino wool sweater with dropped shoulders. Minimal design in neutral tones. Soft hand feel with clean lines typical of Scandinavian aesthetic.",
            fit="oversized",
            style_tags=["minimalist", "scandinavian", "cozy"],
            colors=["grey", "cream", "charcoal"],
            materials=["merino wool"],
            price_usd=135.00,
        ),

        # Raw Denim / Americana
        ClothingItem(
            id="item_007",
            name="14.5oz Selvedge Denim",
            brand="3sixteen",
            category="pants",
            description="Raw selvedge denim jeans made in USA. Slim tapered fit with high rise. Unsanforized Cone Mills denim that fades beautifully over time.",
            fit="slim tapered high rise",
            style_tags=["raw denim", "americana", "heritage"],
            colors=["indigo"],
            materials=["selvedge denim", "raw denim"],
            price_usd=265.00,
        ),
        ClothingItem(
            id="item_008",
            name="Iron Ranger Boots",
            brand="Red Wing",
            category="shoes",
            description="Classic American work boots with Goodyear welt construction. Full grain leather upper with cork midsole. Heritage workwear boots built to last decades.",
            fit="regular",
            style_tags=["heritage", "americana", "workwear"],
            colors=["amber", "black", "copper"],
            materials=["full grain leather"],
            price_usd=350.00,
        ),
        ClothingItem(
            id="item_009",
            name="Ranch Jacket",
            brand="Rogue Territory",
            category="jacket",
            description="Unlined denim jacket in 15oz selvedge. Slightly relaxed fit with Western-inspired details. American-made heritage piece that develops character with wear.",
            fit="relaxed",
            style_tags=["americana", "raw denim", "heritage"],
            colors=["indigo"],
            materials=["selvedge denim", "heavyweight denim"],
            price_usd=285.00,
        ),

        # Techwear
        ClothingItem(
            id="item_010",
            name="Gamma LT Jacket",
            brand="Arc'teryx",
            category="jacket",
            description="Technical softshell jacket with weather resistance. Articulated fit with underarm gussets. Minimalist techwear piece with hidden pockets and DWR finish.",
            fit="athletic",
            style_tags=["techwear", "technical", "minimalist"],
            colors=["black", "grey"],
            materials=["softshell", "synthetic"],
            price_usd=325.00,
        ),
        ClothingItem(
            id="item_011",
            name="P30A-DS Pants",
            brand="Acronym",
            category="pants",
            description="Technical cargo pants with tapered fit. Water resistant fabric with magnetic closures. Multiple utility pockets with sleek black aesthetic. High-end techwear piece.",
            fit="tapered",
            style_tags=["techwear", "technical", "urban"],
            colors=["black"],
            materials=["gore-tex", "technical fabric"],
            price_usd=1200.00,
        ),

        # Streetwear
        ClothingItem(
            id="item_012",
            name="Box Logo Hoodie",
            brand="Supreme",
            category="hoodie",
            description="Heavyweight fleece hoodie with embroidered box logo. Relaxed streetwear fit. Classic piece in the streetwear canon.",
            fit="relaxed",
            style_tags=["streetwear", "hype"],
            colors=["black", "grey", "navy"],
            materials=["heavyweight cotton", "fleece"],
            price_usd=168.00,
        ),
        ClothingItem(
            id="item_013",
            name="Track Pants",
            brand="Needles",
            category="pants",
            description="Wide leg track pants with side stripe. Japanese streetwear meets vintage sportswear. Relaxed oversized fit with elastic waist.",
            fit="wide leg",
            style_tags=["streetwear", "japanese", "vintage"],
            colors=["purple", "green", "navy"],
            materials=["polyester", "mesh"],
            price_usd=295.00,
        ),

        # Contemporary/Designer
        ClothingItem(
            id="item_014",
            name="Petit Standard Jeans",
            brand="A.P.C.",
            category="pants",
            description="Classic straight leg jeans in raw selvedge denim. Slim straight fit with mid rise. French minimalist design that becomes personalized through wear.",
            fit="slim straight",
            style_tags=["minimalist", "raw denim", "french"],
            colors=["indigo"],
            materials=["selvedge denim"],
            price_usd=220.00,
        ),
        ClothingItem(
            id="item_015",
            name="Harrington Jacket",
            brand="Baracuta",
            category="jacket",
            description="Original G9 Harrington jacket in cotton blend. Classic fit with Fraser tartan lining. British heritage piece with timeless design.",
            fit="classic",
            style_tags=["heritage", "british", "classic"],
            colors=["navy", "tan", "black"],
            materials=["cotton blend"],
            price_usd=395.00,
        ),

        # Earth Tones / Specific Colors
        ClothingItem(
            id="item_016",
            name="Fatigue Shirt",
            brand="Orslow",
            category="shirt",
            description="Military-inspired overshirt in earth tone olive green. Relaxed fit with utility pockets. Japanese craftsmanship with vintage workwear aesthetic.",
            fit="relaxed",
            style_tags=["workwear", "military", "japanese"],
            colors=["olive", "earth tone", "green"],
            materials=["cotton twill"],
            price_usd=375.00,
        ),
        ClothingItem(
            id="item_017",
            name="Pleated Wide Chinos",
            brand="Still by Hand",
            category="pants",
            description="Wide leg pleated trousers in tan cotton. Relaxed Japanese contemporary design. Earth tone palette with refined casual aesthetic.",
            fit="wide pleated",
            style_tags=["japanese", "contemporary", "relaxed"],
            colors=["tan", "beige", "earth tone"],
            materials=["cotton"],
            price_usd=265.00,
        ),

        # Budget Options
        ClothingItem(
            id="item_018",
            name="Athletic Fit Chinos",
            brand="Uniqlo",
            category="pants",
            description="Stretchy cotton chinos with athletic fit. Tapered leg with room in thighs. Affordable everyday pants with quality construction.",
            fit="athletic tapered",
            style_tags=["casual", "affordable"],
            colors=["navy", "khaki", "olive", "black"],
            materials=["cotton blend", "stretch cotton"],
            price_usd=39.90,
        ),
        ClothingItem(
            id="item_019",
            name="Double Knee Work Pant",
            brand="Carhartt WIP",
            category="pants",
            description="Classic workwear pants with reinforced knees. Relaxed fit in durable canvas. Heritage workwear style at accessible price point.",
            fit="relaxed",
            style_tags=["workwear", "heritage", "durable"],
            colors=["brown", "black", "blue"],
            materials=["canvas", "cotton"],
            price_usd=128.00,
        ),

        # High Rise / Specific Fits
        ClothingItem(
            id="item_020",
            name="High Rise Straight Leg Jean",
            brand="Pure Blue Japan",
            category="pants",
            description="18oz heavyweight raw denim with high rise waist. Straight leg cut that stacks slightly. Slubby texture with beautiful fading potential.",
            fit="high rise straight",
            style_tags=["raw denim", "japanese", "heritage"],
            colors=["indigo"],
            materials=["heavyweight denim", "selvedge"],
            price_usd=395.00,
        ),
    ]
    return items


def generate_sample_brands() -> list[Brand]:
    """Generate sample brand profiles."""
    brands = [
        Brand(
            id="brand_001",
            name="Orslow",
            description="Japanese brand specializing in vintage American workwear reproductions. Known for meticulous attention to detail and authentic reproduction of military and work garments.",
            aesthetics=["workwear", "military", "heritage", "japanese"],
            typical_fits=["relaxed", "vintage"],
            price_range="premium",
            origin_country="Japan",
            signature_items=["fatigue pants", "105 jeans", "utility jacket"],
            similar_brands=["Engineered Garments", "Arpenteur", "OrSlow"],
        ),
        Brand(
            id="brand_002",
            name="Norse Projects",
            description="Copenhagen-based brand embodying Scandinavian minimalism. Focus on clean lines, quality materials, and functional simplicity.",
            aesthetics=["minimalist", "scandinavian", "functional"],
            typical_fits=["regular", "relaxed"],
            price_range="premium",
            origin_country="Denmark",
            signature_items=["Anton shirt", "Aros chinos", "Sigfred sweater"],
            similar_brands=["Our Legacy", "Arket", "COS"],
        ),
        Brand(
            id="brand_003",
            name="3sixteen",
            description="New York brand focused on premium American-made selvedge denim. Known for quality construction and raw denim that ages beautifully.",
            aesthetics=["americana", "heritage", "raw denim"],
            typical_fits=["slim", "tapered"],
            price_range="premium",
            origin_country="USA",
            signature_items=["CT-100x jeans", "Type 3s jacket", "heavyweight tees"],
            similar_brands=["Rogue Territory", "Left Field NYC", "Railcar Fine Goods"],
        ),
        Brand(
            id="brand_004",
            name="Engineered Garments",
            description="New York based brand with Japanese roots. Combines American workwear with Japanese sensibility. Known for oversized silhouettes and utilitarian details.",
            aesthetics=["workwear", "japanese", "utilitarian", "oversized"],
            typical_fits=["oversized", "boxy", "relaxed"],
            price_range="premium",
            origin_country="USA/Japan",
            signature_items=["Bedford jacket", "fatigue pants", "coveralls"],
            similar_brands=["Orslow", "Kapital", "Monitaly"],
        ),
        Brand(
            id="brand_005",
            name="Arc'teryx",
            description="Technical outdoor brand from Vancouver. Known for minimalist techwear pieces with exceptional construction and weather protection.",
            aesthetics=["techwear", "technical", "minimalist"],
            typical_fits=["athletic", "technical"],
            price_range="premium",
            origin_country="Canada",
            signature_items=["Alpha SV", "Beta jacket", "Atom hoodie"],
            similar_brands=["Veilance", "Outlier", "Acronym"],
        ),
        Brand(
            id="brand_006",
            name="A.P.C.",
            description="French brand known for clean, minimal designs. Particularly famous for their raw denim jeans that develop unique fades over time.",
            aesthetics=["minimalist", "french", "clean"],
            typical_fits=["slim", "straight"],
            price_range="premium",
            origin_country="France",
            signature_items=["Petit Standard jeans", "Petit New Standard", "minimalist tees"],
            similar_brands=["Acne Studios", "AMI", "Sandro"],
        ),
        Brand(
            id="brand_007",
            name="Kapital",
            description="Japanese brand known for eclectic, artisanal clothing. Combines traditional Japanese techniques with Americana and global influences.",
            aesthetics=["japanese", "artisanal", "eclectic", "vintage"],
            typical_fits=["loose", "oversized"],
            price_range="luxury",
            origin_country="Japan",
            signature_items=["century denim", "ring coat", "boro patchwork"],
            similar_brands=["Visvim", "Needles", "Orslow"],
        ),
        Brand(
            id="brand_008",
            name="Red Wing",
            description="American heritage boot manufacturer since 1905. Known for durable work boots with Goodyear welt construction that last for decades.",
            aesthetics=["heritage", "americana", "workwear"],
            typical_fits=["classic", "traditional"],
            price_range="mid",
            origin_country="USA",
            signature_items=["Iron Ranger", "Moc Toe", "Beckman"],
            similar_brands=["Wolverine 1000 Mile", "Alden", "Viberg"],
        ),
        Brand(
            id="brand_009",
            name="Carhartt WIP",
            description="European division of Carhartt focusing on streetwear-influenced workwear. More fitted than mainline Carhartt with contemporary styling.",
            aesthetics=["workwear", "streetwear", "urban"],
            typical_fits=["relaxed", "regular"],
            price_range="mid",
            origin_country="Germany",
            signature_items=["Detroit jacket", "sid pant", "chase hoodie"],
            similar_brands=["Dickies", "Carhartt", "Stan Ray"],
        ),
        Brand(
            id="brand_010",
            name="COS",
            description="H&M group brand focusing on architectural, minimalist design. Offers Scandinavian aesthetic at accessible price points.",
            aesthetics=["minimalist", "scandinavian", "architectural"],
            typical_fits=["oversized", "relaxed"],
            price_range="mid",
            origin_country="Sweden",
            signature_items=["oversized shirts", "structured trousers", "minimal coats"],
            similar_brands=["Arket", "Uniqlo U", "Norse Projects"],
        ),
    ]
    return brands


def generate_sample_discussions() -> list[StyleDiscussion]:
    """Generate sample Reddit-style discussions."""
    discussions = [
        StyleDiscussion(
            id="disc_001",
            title="Best brands for relaxed Japanese workwear aesthetic?",
            content="Looking to build a wardrobe around Japanese workwear. I love the relaxed fits and earth tones. Budget is around $200-400 per piece. Already have some Orslow pieces but looking for alternatives. Particularly interested in fatigue pants and chore coats.",
            mentioned_brands=["Orslow", "Engineered Garments", "Kapital"],
            mentioned_items=["fatigue pants", "chore coat"],
            style_descriptors=["japanese", "workwear", "relaxed", "earth tones"],
            source_url="https://reddit.com/r/malefashionadvice/example1",
            subreddit="malefashionadvice",
            upvotes=245,
            num_comments=89,
        ),
        StyleDiscussion(
            id="disc_002",
            title="Scandinavian minimalism - building a capsule wardrobe",
            content="I'm tired of fast fashion and want to invest in quality minimalist pieces. Love the clean lines of Norse Projects and COS. Looking for neutral colors - black, white, grey, navy. Focus on versatile pieces that can be dressed up or down.",
            mentioned_brands=["Norse Projects", "COS", "Arket"],
            mentioned_items=["shirt", "trousers", "sweater"],
            style_descriptors=["minimalist", "scandinavian", "neutral", "capsule"],
            source_url="https://reddit.com/r/malefashionadvice/example2",
            subreddit="malefashionadvice",
            upvotes=312,
            num_comments=124,
        ),
        StyleDiscussion(
            id="disc_003",
            title="Raw denim recommendations for slim tapered fit with high rise?",
            content="My favorite pair of jeans are wearing out. Need something with high rise for comfort but slim tapered for modern look. Prefer unsanforized for the fading journey. Budget around $300. 3sixteen and Pure Blue Japan look interesting.",
            mentioned_brands=["3sixteen", "Pure Blue Japan", "Iron Heart"],
            mentioned_items=["jeans", "raw denim"],
            style_descriptors=["slim tapered", "high rise", "raw denim"],
            source_url="https://reddit.com/r/rawdenim/example3",
            subreddit="rawdenim",
            upvotes=156,
            num_comments=67,
        ),
        StyleDiscussion(
            id="disc_004",
            title="Techwear that doesn't look like you're cosplaying",
            content="I love the functionality of techwear but hate the ninja aesthetic. Looking for subtle technical pieces. Arc'teryx Veilance seems perfect but the price is insane. Any alternatives that offer weather resistance and clean design?",
            mentioned_brands=["Arc'teryx", "Outlier", "Veilance"],
            mentioned_items=["jacket", "pants"],
            style_descriptors=["techwear", "minimalist", "technical", "functional"],
            source_url="https://reddit.com/r/techwearclothing/example4",
            subreddit="techwearclothing",
            upvotes=423,
            num_comments=198,
        ),
        StyleDiscussion(
            id="disc_005",
            title="Wide leg pants revolution - recommendations?",
            content="Finally embracing wider fits after years of skinny jeans. Looking for wide leg or straight leg pants that aren't too extreme. Like the silhouette of Lemaire and Still by Hand. Earth tones preferred - olive, tan, brown.",
            mentioned_brands=["Lemaire", "Still by Hand", "Our Legacy"],
            mentioned_items=["wide leg pants", "trousers"],
            style_descriptors=["wide leg", "relaxed", "earth tones", "contemporary"],
            source_url="https://reddit.com/r/malefashion/example5",
            subreddit="malefashion",
            upvotes=287,
            num_comments=95,
        ),
    ]
    return discussions


def save_sample_data():
    """Save all sample data to JSON files."""
    import os

    # Create samples directory if needed
    samples_dir = os.path.join(os.path.dirname(__file__))

    # Generate and save data
    items = generate_sample_items()
    brands = generate_sample_brands()
    discussions = generate_sample_discussions()

    # Save to JSON
    items_path = os.path.join(samples_dir, "sample_items.json")
    with open(items_path, 'w') as f:
        json.dump([item.to_dict() for item in items], f, indent=2)

    brands_path = os.path.join(samples_dir, "sample_brands.json")
    with open(brands_path, 'w') as f:
        json.dump([brand.to_dict() for brand in brands], f, indent=2)

    discussions_path = os.path.join(samples_dir, "sample_discussions.json")
    with open(discussions_path, 'w') as f:
        json.dump([disc.to_dict() for disc in discussions], f, indent=2)

    print(f"Saved {len(items)} items to {items_path}")
    print(f"Saved {len(brands)} brands to {brands_path}")
    print(f"Saved {len(discussions)} discussions to {discussions_path}")


if __name__ == "__main__":
    save_sample_data()
