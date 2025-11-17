"""
Expanded sample dataset for the Style Translator.
200+ items, 30+ brands, 20+ discussions covering diverse menswear styles.
"""
import json
from datetime import datetime
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.clothing import ClothingItem, Brand, StyleDiscussion


def generate_sample_brands() -> list[Brand]:
    """Generate 30+ brand profiles covering diverse aesthetics."""
    brands = [
        # Japanese Workwear / Heritage
        Brand(
            id="brand_001", name="Orslow",
            description="Japanese brand specializing in vintage American workwear reproductions. Known for meticulous attention to detail and authentic reproduction of military and work garments.",
            aesthetics=["workwear", "military", "heritage", "japanese"],
            typical_fits=["relaxed", "vintage"],
            price_range="premium", origin_country="Japan",
            signature_items=["fatigue pants", "105 jeans", "utility jacket"],
            similar_brands=["Engineered Garments", "Arpenteur", "Nigel Cabourn"],
        ),
        Brand(
            id="brand_002", name="Engineered Garments",
            description="New York based brand with Japanese roots. Combines American workwear with Japanese sensibility. Known for oversized silhouettes and utilitarian details.",
            aesthetics=["workwear", "japanese", "utilitarian", "oversized"],
            typical_fits=["oversized", "boxy", "relaxed"],
            price_range="premium", origin_country="USA/Japan",
            signature_items=["Bedford jacket", "fatigue pants", "coveralls"],
            similar_brands=["Orslow", "Kapital", "Monitaly"],
        ),
        Brand(
            id="brand_003", name="Kapital",
            description="Japanese brand known for eclectic, artisanal clothing. Combines traditional Japanese techniques with Americana and global influences. Famous for indigo dyeing and patchwork.",
            aesthetics=["japanese", "artisanal", "eclectic", "vintage", "indigo"],
            typical_fits=["loose", "oversized"],
            price_range="luxury", origin_country="Japan",
            signature_items=["century denim", "ring coat", "boro patchwork"],
            similar_brands=["Visvim", "Needles", "Blue Blue Japan"],
        ),
        Brand(
            id="brand_004", name="Visvim",
            description="High-end Japanese brand blending traditional craftsmanship with modern design. Known for Americana influences and premium materials.",
            aesthetics=["japanese", "americana", "heritage", "premium"],
            typical_fits=["relaxed", "oversized"],
            price_range="luxury", origin_country="Japan",
            signature_items=["FBT moccasins", "Christo sandals", "Noragi jacket"],
            similar_brands=["Kapital", "Needles", "Orslow"],
        ),
        Brand(
            id="brand_005", name="Needles",
            description="Japanese brand known for bold patterns and vintage sportswear influence. Famous for track pants with side stripes and butterfly embroidery.",
            aesthetics=["japanese", "streetwear", "vintage", "bold"],
            typical_fits=["relaxed", "wide"],
            price_range="premium", origin_country="Japan",
            signature_items=["track pants", "rebuild flannel", "papillon shirt"],
            similar_brands=["Kapital", "Sasquatchfabrix", "Orslow"],
        ),

        # Scandinavian Minimalist
        Brand(
            id="brand_006", name="Norse Projects",
            description="Copenhagen-based brand embodying Scandinavian minimalism. Focus on clean lines, quality materials, and functional simplicity.",
            aesthetics=["minimalist", "scandinavian", "functional", "clean"],
            typical_fits=["regular", "relaxed"],
            price_range="premium", origin_country="Denmark",
            signature_items=["Anton shirt", "Aros chinos", "Sigfred sweater"],
            similar_brands=["Our Legacy", "Arket", "COS", "Wood Wood"],
        ),
        Brand(
            id="brand_007", name="Our Legacy",
            description="Swedish brand known for refined basics with subtle design twists. Combines Scandinavian minimalism with experimental details.",
            aesthetics=["minimalist", "scandinavian", "contemporary", "refined"],
            typical_fits=["relaxed", "oversized"],
            price_range="premium", origin_country="Sweden",
            signature_items=["Box Shirt", "Third Cut jeans", "Borrowed BD shirt"],
            similar_brands=["Norse Projects", "Acne Studios", "Lemaire"],
        ),
        Brand(
            id="brand_008", name="COS",
            description="H&M group brand focusing on architectural, minimalist design. Offers Scandinavian aesthetic at accessible price points.",
            aesthetics=["minimalist", "scandinavian", "architectural", "modern"],
            typical_fits=["oversized", "relaxed", "boxy"],
            price_range="mid", origin_country="Sweden",
            signature_items=["oversized shirts", "structured trousers", "minimal coats"],
            similar_brands=["Arket", "Uniqlo U", "Norse Projects"],
        ),
        Brand(
            id="brand_009", name="Acne Studios",
            description="Swedish fashion house known for minimal Scandinavian design with artistic edge. Famous for denim and clean aesthetic.",
            aesthetics=["minimalist", "scandinavian", "artistic", "contemporary"],
            typical_fits=["slim", "regular", "oversized"],
            price_range="luxury", origin_country="Sweden",
            signature_items=["Ace jeans", "Face logo", "oversized sweaters"],
            similar_brands=["Our Legacy", "Norse Projects", "A.P.C."],
        ),

        # Raw Denim / Americana
        Brand(
            id="brand_010", name="3sixteen",
            description="New York brand focused on premium American-made selvedge denim. Known for quality construction and raw denim that ages beautifully.",
            aesthetics=["americana", "heritage", "raw denim", "workwear"],
            typical_fits=["slim", "tapered", "straight"],
            price_range="premium", origin_country="USA",
            signature_items=["CT-100x jeans", "Type 3s jacket", "heavyweight tees"],
            similar_brands=["Rogue Territory", "Left Field NYC", "Railcar"],
        ),
        Brand(
            id="brand_011", name="Iron Heart",
            description="Japanese brand specializing in heavyweight denim and leather. Known for super heavy fabrics and exceptional construction.",
            aesthetics=["japanese", "heavyweight", "raw denim", "workwear"],
            typical_fits=["slim", "straight", "relaxed"],
            price_range="luxury", origin_country="Japan",
            signature_items=["21oz denim", "leather jackets", "flannel shirts"],
            similar_brands=["The Flat Head", "Samurai Jeans", "Pure Blue Japan"],
        ),
        Brand(
            id="brand_012", name="Pure Blue Japan",
            description="Japanese denim brand known for slubby, textured fabrics and unique indigo dyeing. Creates some of the most character-rich raw denim available.",
            aesthetics=["japanese", "raw denim", "artisanal", "textured"],
            typical_fits=["slim tapered", "relaxed tapered", "straight"],
            price_range="luxury", origin_country="Japan",
            signature_items=["XX-019 jeans", "slubby denim", "indigo knits"],
            similar_brands=["Iron Heart", "Momotaro", "Samurai Jeans"],
        ),
        Brand(
            id="brand_013", name="Rogue Territory",
            description="Los Angeles brand making American-made selvedge denim with Western influences. Known for quality construction and unique fabrics.",
            aesthetics=["americana", "western", "raw denim", "workwear"],
            typical_fits=["slim", "tapered"],
            price_range="premium", origin_country="USA",
            signature_items=["Stanton jeans", "Supply jacket", "Officer trousers"],
            similar_brands=["3sixteen", "Freenote Cloth", "Taylor Stitch"],
        ),

        # Heritage / Classic American
        Brand(
            id="brand_014", name="Red Wing",
            description="American heritage boot manufacturer since 1905. Known for durable work boots with Goodyear welt construction that last for decades.",
            aesthetics=["heritage", "americana", "workwear", "durable"],
            typical_fits=["classic", "traditional"],
            price_range="mid", origin_country="USA",
            signature_items=["Iron Ranger", "Moc Toe", "Beckman"],
            similar_brands=["Wolverine 1000 Mile", "Alden", "Viberg"],
        ),
        Brand(
            id="brand_015", name="Filson",
            description="Pacific Northwest brand making rugged outdoor gear since 1897. Known for heavy tin cloth, wool, and products built to last.",
            aesthetics=["heritage", "outdoor", "rugged", "workwear"],
            typical_fits=["classic", "relaxed"],
            price_range="premium", origin_country="USA",
            signature_items=["Mackinaw Cruiser", "tin cloth jacket", "briefcase"],
            similar_brands=["Pendleton", "L.L.Bean", "Carhartt"],
        ),
        Brand(
            id="brand_016", name="Schott NYC",
            description="American brand famous for leather jackets since 1913. Created the original Perfecto motorcycle jacket.",
            aesthetics=["heritage", "americana", "leather", "rebel"],
            typical_fits=["classic", "fitted"],
            price_range="premium", origin_country="USA",
            signature_items=["Perfecto 618", "peacoat", "leather jackets"],
            similar_brands=["Aero Leather", "Vanson", "Lewis Leathers"],
        ),

        # Techwear / Technical
        Brand(
            id="brand_017", name="Arc'teryx",
            description="Technical outdoor brand from Vancouver. Known for minimalist techwear pieces with exceptional construction and weather protection.",
            aesthetics=["techwear", "technical", "minimalist", "outdoor"],
            typical_fits=["athletic", "technical", "articulated"],
            price_range="premium", origin_country="Canada",
            signature_items=["Alpha SV", "Beta jacket", "Atom hoodie"],
            similar_brands=["Veilance", "Outlier", "Patagonia"],
        ),
        Brand(
            id="brand_018", name="Acronym",
            description="High-end German techwear brand. Known for futuristic designs, exceptional functionality, and premium technical fabrics.",
            aesthetics=["techwear", "futuristic", "technical", "black"],
            typical_fits=["tapered", "articulated"],
            price_range="luxury", origin_country="Germany",
            signature_items=["P30A pants", "J1A jacket", "3A-1 bag"],
            similar_brands=["Veilance", "Stone Island Shadow", "Y-3"],
        ),
        Brand(
            id="brand_019", name="Outlier",
            description="New York brand focused on technical fabrics for everyday wear. Known for stretch pants and merino wool basics.",
            aesthetics=["techwear", "minimalist", "technical", "urban"],
            typical_fits=["slim", "tapered"],
            price_range="premium", origin_country="USA",
            signature_items=["Futureworks pants", "Ultrafine merino", "Slim Dungarees"],
            similar_brands=["Veilance", "Mission Workshop", "Western Rise"],
        ),

        # Streetwear
        Brand(
            id="brand_020", name="Supreme",
            description="New York streetwear brand known for limited releases and collaborations. Iconic box logo and skate culture roots.",
            aesthetics=["streetwear", "hype", "skate", "bold"],
            typical_fits=["relaxed", "oversized"],
            price_range="mid", origin_country="USA",
            signature_items=["box logo hoodie", "camp cap", "skateboard decks"],
            similar_brands=["Palace", "Stussy", "Noah"],
        ),
        Brand(
            id="brand_021", name="Aimé Leon Dore",
            description="New York brand blending streetwear with preppy Americana. Known for refined casual wear with vintage sports influences.",
            aesthetics=["streetwear", "preppy", "vintage", "refined"],
            typical_fits=["relaxed", "regular"],
            price_range="premium", origin_country="USA",
            signature_items=["New Balance collabs", "rugby shirts", "colorful basics"],
            similar_brands=["Noah", "Rowing Blazers", "Kith"],
        ),
        Brand(
            id="brand_022", name="Stussy",
            description="California surf and skate brand from the 80s. Pioneer of streetwear with relaxed California aesthetic.",
            aesthetics=["streetwear", "surf", "skate", "casual"],
            typical_fits=["relaxed", "oversized"],
            price_range="mid", origin_country="USA",
            signature_items=["signature logo tees", "bucket hats", "varsity jackets"],
            similar_brands=["Supreme", "Palace", "Carhartt WIP"],
        ),

        # Contemporary / Designer
        Brand(
            id="brand_023", name="A.P.C.",
            description="French brand known for clean, minimal designs. Particularly famous for their raw denim jeans that develop unique fades over time.",
            aesthetics=["minimalist", "french", "clean", "understated"],
            typical_fits=["slim", "straight"],
            price_range="premium", origin_country="France",
            signature_items=["Petit Standard jeans", "Petit New Standard", "minimalist tees"],
            similar_brands=["Acne Studios", "AMI", "Lemaire"],
        ),
        Brand(
            id="brand_024", name="Lemaire",
            description="French brand known for refined, understated luxury. Architectural silhouettes with soft, draped fabrics.",
            aesthetics=["minimalist", "french", "architectural", "refined"],
            typical_fits=["relaxed", "oversized", "draped"],
            price_range="luxury", origin_country="France",
            signature_items=["Croissant bag", "pleated trousers", "boxy shirts"],
            similar_brands=["Our Legacy", "Auralee", "Studio Nicholson"],
        ),
        Brand(
            id="brand_025", name="Margaret Howell",
            description="British designer focusing on understated, quality clothing. Simple shapes in natural fabrics with excellent tailoring.",
            aesthetics=["british", "understated", "natural", "quality"],
            typical_fits=["relaxed", "classic"],
            price_range="luxury", origin_country="UK",
            signature_items=["linen shirts", "cotton drill trousers", "wool coats"],
            similar_brands=["Lemaire", "Sunspel", "Universal Works"],
        ),

        # British Heritage
        Brand(
            id="brand_026", name="Barbour",
            description="British heritage brand famous for waxed cotton jackets. Classic country clothing with timeless appeal.",
            aesthetics=["british", "heritage", "country", "classic"],
            typical_fits=["classic", "regular"],
            price_range="mid", origin_country="UK",
            signature_items=["Bedale jacket", "Beaufort", "waxed cotton"],
            similar_brands=["Baracuta", "Grenfell", "Private White V.C."],
        ),
        Brand(
            id="brand_027", name="Baracuta",
            description="British brand known for the original Harrington jacket. Classic British style with functional details.",
            aesthetics=["british", "heritage", "classic", "mod"],
            typical_fits=["classic", "fitted"],
            price_range="mid", origin_country="UK",
            signature_items=["G9 Harrington", "Fraser tartan lining", "raincoats"],
            similar_brands=["Barbour", "Fred Perry", "Ben Sherman"],
        ),

        # Budget / Value
        Brand(
            id="brand_028", name="Uniqlo",
            description="Japanese fast fashion brand known for quality basics at affordable prices. Collaborations with designers bring elevated design to accessible price points.",
            aesthetics=["minimalist", "basic", "affordable", "japanese"],
            typical_fits=["regular", "slim", "relaxed"],
            price_range="budget", origin_country="Japan",
            signature_items=["Heattech", "AIRism", "Uniqlo U", "selvedge jeans"],
            similar_brands=["Muji", "COS", "H&M"],
        ),
        Brand(
            id="brand_029", name="Carhartt WIP",
            description="European division of Carhartt focusing on streetwear-influenced workwear. More fitted than mainline Carhartt with contemporary styling.",
            aesthetics=["workwear", "streetwear", "urban", "durable"],
            typical_fits=["relaxed", "regular"],
            price_range="mid", origin_country="Germany",
            signature_items=["Detroit jacket", "Sid pant", "Chase hoodie"],
            similar_brands=["Dickies", "Carhartt", "Stan Ray"],
        ),
        Brand(
            id="brand_030", name="Stan Ray",
            description="American workwear brand making simple, durable clothing. Known for painter pants and fatigue pants at good value.",
            aesthetics=["workwear", "military", "simple", "durable"],
            typical_fits=["relaxed", "loose"],
            price_range="budget", origin_country="USA",
            signature_items=["OG painter pants", "fatigue pants", "shop jacket"],
            similar_brands=["Carhartt WIP", "Dickies", "Universal Works"],
        ),

        # Italian
        Brand(
            id="brand_031", name="Stone Island",
            description="Italian brand known for innovative fabric research and dyeing techniques. Iconic compass badge and technical sportswear.",
            aesthetics=["technical", "italian", "innovative", "sporty"],
            typical_fits=["regular", "fitted"],
            price_range="premium", origin_country="Italy",
            signature_items=["Ghost piece", "compass badge", "nylon metal"],
            similar_brands=["C.P. Company", "Aspesi", "Acronym"],
        ),
        Brand(
            id="brand_032", name="Aspesi",
            description="Italian brand specializing in lightweight outerwear. Known for nylon jackets and shirts with refined Italian casualwear.",
            aesthetics=["italian", "casual", "lightweight", "refined"],
            typical_fits=["regular", "fitted"],
            price_range="premium", origin_country="Italy",
            signature_items=["Minifield jacket", "nylon shirt jacket", "cotton sweaters"],
            similar_brands=["Stone Island", "Herno", "Moncler"],
        ),
    ]
    return brands


def generate_sample_items() -> list[ClothingItem]:
    """Generate 200+ clothing items covering diverse styles and brands."""
    items = []
    item_id = 1

    # Helper to create ID
    def next_id():
        nonlocal item_id
        id_str = f"item_{item_id:04d}"
        item_id += 1
        return id_str

    # === ORSLOW ===
    items.extend([
        ClothingItem(id=next_id(), name="Fatigue Pants", brand="Orslow", category="pants",
            description="Classic US Army fatigue pants in ripstop fabric. Relaxed fit with slight taper. Features utility pockets and adjustable waist tabs. Made in Japan with attention to vintage military details.",
            fit="relaxed tapered", style_tags=["workwear", "military", "japanese", "heritage"],
            colors=["olive", "army green"], materials=["ripstop cotton"], price_usd=295.00),
        ClothingItem(id=next_id(), name="105 Standard Jeans", brand="Orslow", category="pants",
            description="Classic straight leg jeans in Japanese selvedge denim. Regular fit with vintage details. Inspired by 1960s American denim.",
            fit="regular straight", style_tags=["japanese", "heritage", "raw denim"],
            colors=["indigo", "one wash"], materials=["selvedge denim"], price_usd=265.00),
        ClothingItem(id=next_id(), name="107 Ivy Fit Jeans", brand="Orslow", category="pants",
            description="Slim tapered jeans with ivy league inspired fit. Japanese selvedge with vintage details.",
            fit="slim tapered", style_tags=["japanese", "heritage", "raw denim"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=265.00),
        ClothingItem(id=next_id(), name="French Work Jacket", brand="Orslow", category="jacket",
            description="French workwear inspired chore coat in cotton twill. Boxy fit with patch pockets. Classic European workwear silhouette.",
            fit="boxy", style_tags=["workwear", "french", "heritage"],
            colors=["navy", "ecru"], materials=["cotton twill"], price_usd=385.00),
        ClothingItem(id=next_id(), name="Fatigue Shirt", brand="Orslow", category="shirt",
            description="Military-inspired overshirt in earth tone olive green. Relaxed fit with utility pockets. Japanese craftsmanship with vintage workwear aesthetic.",
            fit="relaxed", style_tags=["workwear", "military", "japanese"],
            colors=["olive", "earth tone", "green"], materials=["cotton twill"], price_usd=375.00),
        ClothingItem(id=next_id(), name="US Army Tropical Jacket", brand="Orslow", category="jacket",
            description="Lightweight ripstop jacket based on Vietnam-era military design. Oversized fit with multiple pockets. Perfect for layering.",
            fit="oversized", style_tags=["military", "japanese", "vintage"],
            colors=["olive", "khaki"], materials=["ripstop"], price_usd=495.00),
    ])

    # === ENGINEERED GARMENTS ===
    items.extend([
        ClothingItem(id=next_id(), name="Bedford Jacket", brand="Engineered Garments", category="jacket",
            description="Unstructured cotton jacket with patch pockets. Relaxed tailoring meets workwear utility. Signature EG piece.",
            fit="relaxed", style_tags=["workwear", "japanese", "tailoring"],
            colors=["navy", "olive", "khaki"], materials=["cotton ripstop", "twill"], price_usd=480.00),
        ClothingItem(id=next_id(), name="Coverall Jacket", brand="Engineered Garments", category="jacket",
            description="Oversized coverall jacket in heavyweight cotton canvas. Boxy fit with multiple patch pockets. Japanese-made workwear-inspired piece.",
            fit="oversized boxy", style_tags=["workwear", "japanese", "utilitarian"],
            colors=["navy", "khaki"], materials=["heavyweight cotton", "canvas"], price_usd=450.00),
        ClothingItem(id=next_id(), name="Fatigue Pant", brand="Engineered Garments", category="pants",
            description="Relaxed fatigue pants with back cinch. Multiple utility pockets with vintage military details.",
            fit="relaxed", style_tags=["workwear", "military", "japanese"],
            colors=["olive", "navy", "black"], materials=["cotton twill"], price_usd=340.00),
        ClothingItem(id=next_id(), name="Loiter Jacket", brand="Engineered Garments", category="jacket",
            description="Kimono-inspired jacket with oversized fit and wrap front. Unique EG take on traditional Japanese garment.",
            fit="oversized", style_tags=["japanese", "unique", "layering"],
            colors=["indigo", "black"], materials=["cotton"], price_usd=520.00),
        ClothingItem(id=next_id(), name="Andover Pant", brand="Engineered Garments", category="pants",
            description="Wide leg pleated trousers with high rise. Combines tailoring with relaxed workwear sensibility.",
            fit="wide leg pleated", style_tags=["tailoring", "japanese", "wide"],
            colors=["grey", "navy", "olive"], materials=["wool blend"], price_usd=395.00),
    ])

    # === KAPITAL ===
    items.extend([
        ClothingItem(id=next_id(), name="Ring Coat", brand="Kapital", category="jacket",
            description="Indigo dyed ring coat with patchwork details. Loose fitting Japanese workwear with artisanal touches. Features hand-stitched sashiko embroidery.",
            fit="loose", style_tags=["japanese", "artisanal", "indigo"],
            colors=["indigo", "blue"], materials=["cotton", "denim"], price_usd=625.00),
        ClothingItem(id=next_id(), name="Century Denim", brand="Kapital", category="pants",
            description="Heavily distressed and reconstructed denim with sashiko stitching. Each pair is unique with artisanal repairs.",
            fit="relaxed", style_tags=["japanese", "artisanal", "distressed"],
            colors=["indigo"], materials=["denim"], price_usd=895.00),
        ClothingItem(id=next_id(), name="Kountry Westerner Jacket", brand="Kapital", category="jacket",
            description="Western-inspired denim jacket with decorative stitching and patchwork. Eclectic mix of Americana and Japanese craft.",
            fit="regular", style_tags=["japanese", "western", "artisanal"],
            colors=["indigo", "blue"], materials=["denim"], price_usd=750.00),
        ClothingItem(id=next_id(), name="Smiley Tee", brand="Kapital", category="t-shirt",
            description="Oversized tee with signature smiley face graphic. Relaxed fit in heavyweight cotton.",
            fit="oversized", style_tags=["japanese", "graphic", "casual"],
            colors=["white", "black", "grey"], materials=["heavyweight cotton"], price_usd=195.00),
    ])

    # === NORSE PROJECTS ===
    items.extend([
        ClothingItem(id=next_id(), name="Theo Trouser", brand="Norse Projects", category="pants",
            description="Clean minimal trouser in organic cotton twill. Regular fit with straight leg. Simple Scandinavian design.",
            fit="regular straight", style_tags=["minimalist", "scandinavian", "clean"],
            colors=["black", "navy", "beige"], materials=["organic cotton", "twill"], price_usd=185.00),
        ClothingItem(id=next_id(), name="Aros Chinos", brand="Norse Projects", category="pants",
            description="Slim fit chinos in brushed cotton. Clean minimal design with tapered leg.",
            fit="slim tapered", style_tags=["minimalist", "scandinavian", "casual"],
            colors=["khaki", "navy", "black", "olive"], materials=["brushed cotton"], price_usd=165.00),
        ClothingItem(id=next_id(), name="Kyle Oxford Shirt", brand="Norse Projects", category="shirt",
            description="Relaxed fit oxford shirt in brushed cotton. Clean minimal design with no chest pocket. Button-down collar.",
            fit="relaxed", style_tags=["minimalist", "scandinavian", "casual"],
            colors=["white", "light blue", "pale pink"], materials=["brushed cotton", "oxford cloth"], price_usd=145.00),
        ClothingItem(id=next_id(), name="Anton Button Down", brand="Norse Projects", category="shirt",
            description="Classic button down shirt in lightweight cotton. Clean lines with subtle branding.",
            fit="regular", style_tags=["minimalist", "scandinavian", "classic"],
            colors=["white", "blue", "grey"], materials=["cotton poplin"], price_usd=135.00),
        ClothingItem(id=next_id(), name="Sigfred Merino Sweater", brand="Norse Projects", category="sweater",
            description="Crew neck sweater in fine merino wool. Clean Scandinavian design with minimal details.",
            fit="regular", style_tags=["minimalist", "scandinavian", "classic"],
            colors=["grey", "navy", "black", "burgundy"], materials=["merino wool"], price_usd=195.00),
        ClothingItem(id=next_id(), name="Nunk Down Parka", brand="Norse Projects", category="jacket",
            description="Minimal down parka with clean silhouette. Technical fabric with warm down fill.",
            fit="regular", style_tags=["minimalist", "scandinavian", "technical"],
            colors=["black", "navy"], materials=["nylon", "down"], price_usd=550.00),
    ])

    # === OUR LEGACY ===
    items.extend([
        ClothingItem(id=next_id(), name="Box Shirt", brand="Our Legacy", category="shirt",
            description="Boxy fit shirt with dropped shoulders. Contemporary take on classic shirt in interesting fabrics.",
            fit="boxy", style_tags=["minimalist", "scandinavian", "contemporary"],
            colors=["white", "black", "pink"], materials=["cotton"], price_usd=225.00),
        ClothingItem(id=next_id(), name="Third Cut Jeans", brand="Our Legacy", category="pants",
            description="Wide straight leg jeans with high rise. Modern cut with vintage denim inspiration.",
            fit="wide straight", style_tags=["minimalist", "scandinavian", "contemporary"],
            colors=["indigo", "black"], materials=["denim"], price_usd=285.00),
        ClothingItem(id=next_id(), name="Borrowed BD Shirt", brand="Our Legacy", category="shirt",
            description="Oversized button-down shirt designed to look borrowed. Relaxed contemporary fit.",
            fit="oversized", style_tags=["minimalist", "scandinavian", "relaxed"],
            colors=["white", "blue stripe"], materials=["cotton poplin"], price_usd=245.00),
        ClothingItem(id=next_id(), name="Cardigan Coat", brand="Our Legacy", category="jacket",
            description="Long cardigan-style coat in wool blend. Minimal design with no buttons.",
            fit="relaxed", style_tags=["minimalist", "scandinavian", "layering"],
            colors=["black", "camel", "grey"], materials=["wool blend"], price_usd=595.00),
    ])

    # === COS ===
    items.extend([
        ClothingItem(id=next_id(), name="Relaxed Merino Sweater", brand="COS", category="sweater",
            description="Oversized merino wool sweater with dropped shoulders. Minimal design in neutral tones.",
            fit="oversized", style_tags=["minimalist", "scandinavian", "cozy"],
            colors=["grey", "cream", "charcoal"], materials=["merino wool"], price_usd=135.00),
        ClothingItem(id=next_id(), name="Wide Leg Trousers", brand="COS", category="pants",
            description="High waisted wide leg trousers in cotton blend. Clean architectural silhouette.",
            fit="wide leg", style_tags=["minimalist", "architectural", "modern"],
            colors=["black", "navy", "beige"], materials=["cotton blend"], price_usd=115.00),
        ClothingItem(id=next_id(), name="Oversized Shirt", brand="COS", category="shirt",
            description="Boxy oversized shirt in crisp cotton. Minimal Scandinavian design.",
            fit="oversized boxy", style_tags=["minimalist", "scandinavian", "clean"],
            colors=["white", "light blue", "black"], materials=["cotton"], price_usd=89.00),
        ClothingItem(id=next_id(), name="Hooded Parka", brand="COS", category="jacket",
            description="Minimal parka with clean lines. Water resistant fabric with warm lining.",
            fit="regular", style_tags=["minimalist", "scandinavian", "technical"],
            colors=["black", "navy", "olive"], materials=["cotton blend"], price_usd=195.00),
    ])

    # === 3SIXTEEN ===
    items.extend([
        ClothingItem(id=next_id(), name="CT-100x Classic Tapered", brand="3sixteen", category="pants",
            description="Raw selvedge denim jeans made in USA. Slim tapered fit with high rise. Unsanforized Cone Mills denim that fades beautifully.",
            fit="slim tapered high rise", style_tags=["raw denim", "americana", "heritage"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=265.00),
        ClothingItem(id=next_id(), name="ST-100x Slim Tapered", brand="3sixteen", category="pants",
            description="Classic slim tapered fit in raw selvedge. Perfect balance of slim and comfortable.",
            fit="slim tapered", style_tags=["raw denim", "americana", "heritage"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=265.00),
        ClothingItem(id=next_id(), name="NT-100x Narrow Tapered", brand="3sixteen", category="pants",
            description="Narrower fit raw denim for modern silhouette. Strong taper from knee to hem.",
            fit="narrow tapered", style_tags=["raw denim", "americana", "modern"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=265.00),
        ClothingItem(id=next_id(), name="Type 3s Denim Jacket", brand="3sixteen", category="jacket",
            description="Classic denim jacket in raw selvedge. Type III design with modern proportions.",
            fit="regular", style_tags=["raw denim", "americana", "heritage"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=365.00),
        ClothingItem(id=next_id(), name="Heavyweight Pocket Tee", brand="3sixteen", category="t-shirt",
            description="10oz heavyweight cotton tee made in USA. Substantial fabric that softens with wear.",
            fit="regular", style_tags=["americana", "heavyweight", "basic"],
            colors=["white", "black", "grey"], materials=["heavyweight cotton"], price_usd=75.00),
    ])

    # === PURE BLUE JAPAN ===
    items.extend([
        ClothingItem(id=next_id(), name="XX-019 Relaxed Tapered", brand="Pure Blue Japan", category="pants",
            description="Slubby selvedge denim with relaxed top block and tapered leg. Textured fabric with amazing fading potential.",
            fit="relaxed tapered", style_tags=["japanese", "raw denim", "textured"],
            colors=["indigo"], materials=["slubby selvedge"], price_usd=365.00),
        ClothingItem(id=next_id(), name="18oz High Rise Straight", brand="Pure Blue Japan", category="pants",
            description="Heavyweight raw denim with high rise waist. Straight leg cut with stacks. Exceptional slubby texture.",
            fit="high rise straight", style_tags=["raw denim", "japanese", "heavyweight"],
            colors=["indigo"], materials=["heavyweight denim", "selvedge"], price_usd=395.00),
        ClothingItem(id=next_id(), name="Indigo Dyed Sashiko Jacket", brand="Pure Blue Japan", category="jacket",
            description="Hand-dyed indigo sashiko fabric jacket. Traditional Japanese stitching with workwear design.",
            fit="regular", style_tags=["japanese", "indigo", "artisanal"],
            colors=["indigo"], materials=["sashiko cotton"], price_usd=485.00),
        ClothingItem(id=next_id(), name="Slub Knit Henley", brand="Pure Blue Japan", category="shirt",
            description="Textured cotton henley with indigo dye. Slubby fabric with natural variation.",
            fit="regular", style_tags=["japanese", "indigo", "casual"],
            colors=["indigo"], materials=["slub cotton"], price_usd=165.00),
    ])

    # === IRON HEART ===
    items.extend([
        ClothingItem(id=next_id(), name="21oz Super Slim", brand="Iron Heart", category="pants",
            description="Super heavyweight 21oz selvedge denim in slim fit. For serious denim enthusiasts.",
            fit="slim straight", style_tags=["japanese", "heavyweight", "raw denim"],
            colors=["indigo"], materials=["21oz selvedge"], price_usd=395.00),
        ClothingItem(id=next_id(), name="25oz Monster Denim", brand="Iron Heart", category="pants",
            description="Extremely heavy 25oz denim. Stiff and armour-like when new, softens beautifully with wear.",
            fit="regular straight", style_tags=["japanese", "heavyweight", "raw denim", "extreme"],
            colors=["indigo"], materials=["25oz selvedge"], price_usd=445.00),
        ClothingItem(id=next_id(), name="Ultra Heavy Flannel", brand="Iron Heart", category="shirt",
            description="Super heavyweight flannel shirt at 12oz. Incredibly warm and durable.",
            fit="regular", style_tags=["japanese", "heavyweight", "workwear"],
            colors=["grey", "red", "black"], materials=["heavyweight flannel"], price_usd=295.00),
        ClothingItem(id=next_id(), name="Leather Rider Jacket", brand="Iron Heart", category="jacket",
            description="Heavy horsehide leather jacket. Classic rider style with exceptional quality.",
            fit="fitted", style_tags=["japanese", "leather", "rebel"],
            colors=["black"], materials=["horsehide leather"], price_usd=1495.00),
    ])

    # === RED WING ===
    items.extend([
        ClothingItem(id=next_id(), name="Iron Ranger 8111", brand="Red Wing", category="shoes",
            description="Classic American work boots with Goodyear welt construction. Full grain leather upper with cork midsole.",
            fit="regular", style_tags=["heritage", "americana", "workwear"],
            colors=["amber", "black", "copper"], materials=["full grain leather"], price_usd=350.00),
        ClothingItem(id=next_id(), name="Classic Moc Toe 875", brand="Red Wing", category="shoes",
            description="Iconic moc toe work boot. Traction Tred sole with comfortable wedge design.",
            fit="regular", style_tags=["heritage", "americana", "workwear"],
            colors=["oro legacy"], materials=["leather"], price_usd=320.00),
        ClothingItem(id=next_id(), name="Blacksmith 3343", brand="Red Wing", category="shoes",
            description="Round toe boot inspired by blacksmiths. Rugged yet refined design.",
            fit="regular", style_tags=["heritage", "americana", "workwear"],
            colors=["copper"], materials=["leather"], price_usd=350.00),
        ClothingItem(id=next_id(), name="Postman Oxford", brand="Red Wing", category="shoes",
            description="Classic service oxford from the Heritage line. Dress meets workwear.",
            fit="regular", style_tags=["heritage", "americana", "dress"],
            colors=["black"], materials=["leather"], price_usd=320.00),
    ])

    # === ROGUE TERRITORY ===
    items.extend([
        ClothingItem(id=next_id(), name="Stanton Jeans", brand="Rogue Territory", category="pants",
            description="Slim straight raw selvedge denim. Western-inspired details with clean American construction.",
            fit="slim straight", style_tags=["americana", "raw denim", "western"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=285.00),
        ClothingItem(id=next_id(), name="Officer Trousers", brand="Rogue Territory", category="pants",
            description="Military-inspired trousers with high rise and wide leg. Vintage officer pants silhouette.",
            fit="high rise wide", style_tags=["americana", "military", "vintage"],
            colors=["olive", "navy", "khaki"], materials=["cotton twill"], price_usd=245.00),
        ClothingItem(id=next_id(), name="Supply Jacket", brand="Rogue Territory", category="jacket",
            description="Unlined denim jacket in selvedge. Work jacket silhouette with western details.",
            fit="regular", style_tags=["americana", "raw denim", "workwear"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=285.00),
        ClothingItem(id=next_id(), name="Stealth SK", brand="Rogue Territory", category="pants",
            description="Skinny fit raw selvedge denim with tonal stitching. Modern slim cut.",
            fit="skinny", style_tags=["americana", "raw denim", "modern"],
            colors=["black"], materials=["selvedge denim"], price_usd=265.00),
    ])

    # === ARC'TERYX ===
    items.extend([
        ClothingItem(id=next_id(), name="Gamma LT Jacket", brand="Arc'teryx", category="jacket",
            description="Technical softshell jacket with weather resistance. Articulated fit with underarm gussets. Minimalist techwear.",
            fit="athletic", style_tags=["techwear", "technical", "minimalist"],
            colors=["black", "grey"], materials=["softshell"], price_usd=325.00),
        ClothingItem(id=next_id(), name="Beta AR Jacket", brand="Arc'teryx", category="jacket",
            description="All-round Gore-Tex shell jacket. Complete weather protection with minimal bulk.",
            fit="regular", style_tags=["techwear", "technical", "outdoor"],
            colors=["black", "dynasty"], materials=["gore-tex"], price_usd=599.00),
        ClothingItem(id=next_id(), name="Atom LT Hoodie", brand="Arc'teryx", category="jacket",
            description="Lightweight insulated hoodie with Coreloft. Perfect for layering or standalone use.",
            fit="regular", style_tags=["techwear", "technical", "insulated"],
            colors=["black", "pilot"], materials=["nylon", "coreloft"], price_usd=299.00),
        ClothingItem(id=next_id(), name="Zeta SL Jacket", brand="Arc'teryx", category="jacket",
            description="Super lightweight packable rain shell. Emergency weather protection that fits in a pocket.",
            fit="trim", style_tags=["techwear", "technical", "packable"],
            colors=["black", "labyrinth"], materials=["gore-tex"], price_usd=399.00),
    ])

    # === ACRONYM ===
    items.extend([
        ClothingItem(id=next_id(), name="P30A-DS Pants", brand="Acronym", category="pants",
            description="Technical cargo pants with tapered fit. Water resistant fabric with magnetic closures. High-end techwear.",
            fit="tapered", style_tags=["techwear", "technical", "futuristic"],
            colors=["black"], materials=["gore-tex", "technical fabric"], price_usd=1200.00),
        ClothingItem(id=next_id(), name="J1A-GTPL Jacket", brand="Acronym", category="jacket",
            description="Technical shell jacket with gravity pockets. Futuristic design with exceptional functionality.",
            fit="regular", style_tags=["techwear", "futuristic", "technical"],
            colors=["black", "alpha green"], materials=["gore-tex"], price_usd=1850.00),
        ClothingItem(id=next_id(), name="S24-PR-B Shirt", brand="Acronym", category="shirt",
            description="Technical shirt with articulated construction. Minimalist techwear design.",
            fit="regular", style_tags=["techwear", "technical", "minimalist"],
            colors=["black"], materials=["technical cotton"], price_usd=495.00),
    ])

    # === OUTLIER ===
    items.extend([
        ClothingItem(id=next_id(), name="Futureworks", brand="Outlier", category="pants",
            description="Stretchy technical chinos that look like dress pants. Water resistant with four-way stretch.",
            fit="slim tapered", style_tags=["techwear", "minimalist", "technical"],
            colors=["black", "dark navy", "charcoal"], materials=["f.cloth"], price_usd=198.00),
        ClothingItem(id=next_id(), name="Slim Dungarees", brand="Outlier", category="pants",
            description="Stretchy technical pants in workwear style. Slim fit with technical fabric.",
            fit="slim", style_tags=["techwear", "workwear", "technical"],
            colors=["black", "darkindigo"], materials=["workcloth"], price_usd=228.00),
        ClothingItem(id=next_id(), name="Ultrafine Merino Tee", brand="Outlier", category="t-shirt",
            description="17.5 micron merino wool t-shirt. Odor resistant and temperature regulating.",
            fit="regular", style_tags=["techwear", "minimalist", "merino"],
            colors=["black", "grey", "navy"], materials=["merino wool"], price_usd=120.00),
        ClothingItem(id=next_id(), name="New Way Shorts", brand="Outlier", category="shorts",
            description="Technical shorts that can go from gym to dinner. Stretchy and quick-drying.",
            fit="regular", style_tags=["techwear", "minimalist", "versatile"],
            colors=["black", "charcoal", "navy"], materials=["f.cloth"], price_usd=148.00),
    ])

    # === SUPREME ===
    items.extend([
        ClothingItem(id=next_id(), name="Box Logo Hoodie", brand="Supreme", category="hoodie",
            description="Heavyweight fleece hoodie with embroidered box logo. Classic streetwear piece.",
            fit="relaxed", style_tags=["streetwear", "hype", "iconic"],
            colors=["black", "grey", "navy"], materials=["heavyweight cotton", "fleece"], price_usd=168.00),
        ClothingItem(id=next_id(), name="Box Logo Tee", brand="Supreme", category="t-shirt",
            description="Classic t-shirt with Supreme box logo. Streetwear essential.",
            fit="regular", style_tags=["streetwear", "hype", "iconic"],
            colors=["white", "black", "red"], materials=["cotton"], price_usd=48.00),
        ClothingItem(id=next_id(), name="Work Jacket", brand="Supreme", category="jacket",
            description="Canvas work jacket with multiple pockets. Workwear meets streetwear.",
            fit="regular", style_tags=["streetwear", "workwear", "casual"],
            colors=["black", "stone", "navy"], materials=["canvas"], price_usd=228.00),
    ])

    # === AIME LEON DORE ===
    items.extend([
        ClothingItem(id=next_id(), name="Rugby Shirt", brand="Aimé Leon Dore", category="shirt",
            description="Heavy cotton rugby shirt with stripe pattern. Vintage sports meets refined streetwear.",
            fit="relaxed", style_tags=["streetwear", "preppy", "vintage"],
            colors=["green stripe", "navy stripe", "burgundy stripe"], materials=["heavy cotton"], price_usd=185.00),
        ClothingItem(id=next_id(), name="Uniform Shorts", brand="Aimé Leon Dore", category="shorts",
            description="Tailored shorts in cotton twill. Refined casual wear with preppy influence.",
            fit="regular", style_tags=["streetwear", "preppy", "casual"],
            colors=["khaki", "navy", "olive"], materials=["cotton twill"], price_usd=145.00),
        ClothingItem(id=next_id(), name="Logo Hoodie", brand="Aimé Leon Dore", category="hoodie",
            description="French terry hoodie with embroidered logo. Quality basics with elevated details.",
            fit="relaxed", style_tags=["streetwear", "refined", "casual"],
            colors=["cream", "navy", "green"], materials=["french terry"], price_usd=225.00),
    ])

    # === NEEDLES ===
    items.extend([
        ClothingItem(id=next_id(), name="Track Pants", brand="Needles", category="pants",
            description="Wide leg track pants with side stripe. Japanese streetwear meets vintage sportswear.",
            fit="wide leg", style_tags=["streetwear", "japanese", "vintage"],
            colors=["purple", "green", "navy"], materials=["polyester", "mesh"], price_usd=295.00),
        ClothingItem(id=next_id(), name="Rebuild Flannel", brand="Needles", category="shirt",
            description="Reconstructed vintage flannel shirts. Each piece is unique patchwork.",
            fit="oversized", style_tags=["japanese", "vintage", "unique"],
            colors=["multi"], materials=["cotton flannel"], price_usd=395.00),
        ClothingItem(id=next_id(), name="Papillon Shirt", brand="Needles", category="shirt",
            description="Camp collar shirt with butterfly embroidery. Signature Needles design.",
            fit="relaxed", style_tags=["japanese", "casual", "decorative"],
            colors=["black", "navy", "white"], materials=["rayon"], price_usd=265.00),
        ClothingItem(id=next_id(), name="Narrow Track Pant", brand="Needles", category="pants",
            description="Tapered version of the classic track pants. Modern slim silhouette.",
            fit="tapered", style_tags=["streetwear", "japanese", "sporty"],
            colors=["black", "navy"], materials=["poly smooth"], price_usd=295.00),
    ])

    # === A.P.C. ===
    items.extend([
        ClothingItem(id=next_id(), name="Petit Standard Jeans", brand="A.P.C.", category="pants",
            description="Classic straight leg jeans in raw selvedge denim. Slim straight fit. French minimalism.",
            fit="slim straight", style_tags=["minimalist", "raw denim", "french"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=220.00),
        ClothingItem(id=next_id(), name="Petit New Standard", brand="A.P.C.", category="pants",
            description="Slimmer version of the Petit Standard. Modern tapered silhouette.",
            fit="slim tapered", style_tags=["minimalist", "raw denim", "french"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=220.00),
        ClothingItem(id=next_id(), name="New Standard", brand="A.P.C.", category="pants",
            description="Regular straight fit raw selvedge jeans. Classic fit for all body types.",
            fit="regular straight", style_tags=["minimalist", "raw denim", "french"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=220.00),
        ClothingItem(id=next_id(), name="VPC Logo Tee", brand="A.P.C.", category="t-shirt",
            description="Simple cotton tee with small VPC logo. Understated Parisian style.",
            fit="regular", style_tags=["minimalist", "french", "basic"],
            colors=["white", "black", "navy"], materials=["cotton"], price_usd=95.00),
    ])

    # === LEMAIRE ===
    items.extend([
        ClothingItem(id=next_id(), name="Pleated Trousers", brand="Lemaire", category="pants",
            description="Wide pleated trousers with high rise. Refined architectural silhouette.",
            fit="wide pleated", style_tags=["minimalist", "french", "architectural"],
            colors=["black", "tan", "grey"], materials=["wool blend"], price_usd=495.00),
        ClothingItem(id=next_id(), name="Twisted Shirt", brand="Lemaire", category="shirt",
            description="Shirt with asymmetric twisted seams. Signature Lemaire design detail.",
            fit="relaxed", style_tags=["minimalist", "french", "architectural"],
            colors=["white", "blue"], materials=["cotton poplin"], price_usd=445.00),
        ClothingItem(id=next_id(), name="Soft Coat", brand="Lemaire", category="jacket",
            description="Unstructured wool coat with soft drape. Minimal design with elegant proportions.",
            fit="relaxed", style_tags=["minimalist", "french", "refined"],
            colors=["black", "camel", "grey"], materials=["wool"], price_usd=1295.00),
    ])

    # === BARBOUR ===
    items.extend([
        ClothingItem(id=next_id(), name="Bedale Jacket", brand="Barbour", category="jacket",
            description="Classic waxed cotton jacket. Shorter length country jacket with corduroy collar.",
            fit="regular", style_tags=["british", "heritage", "country"],
            colors=["sage", "navy"], materials=["waxed cotton"], price_usd=425.00),
        ClothingItem(id=next_id(), name="Beaufort Jacket", brand="Barbour", category="jacket",
            description="Longer waxed cotton jacket. Classic British country style.",
            fit="regular", style_tags=["british", "heritage", "country"],
            colors=["olive", "navy"], materials=["waxed cotton"], price_usd=449.00),
        ClothingItem(id=next_id(), name="Ashby Jacket", brand="Barbour", category="jacket",
            description="Slimmer fit waxed jacket. Modern take on classic Barbour style.",
            fit="slim", style_tags=["british", "heritage", "modern"],
            colors=["navy", "olive"], materials=["waxed cotton"], price_usd=399.00),
    ])

    # === BARACUTA ===
    items.extend([
        ClothingItem(id=next_id(), name="G9 Harrington Jacket", brand="Baracuta", category="jacket",
            description="Original G9 Harrington jacket in cotton blend. Classic fit with Fraser tartan lining.",
            fit="classic", style_tags=["heritage", "british", "classic"],
            colors=["navy", "tan", "black"], materials=["cotton blend"], price_usd=395.00),
        ClothingItem(id=next_id(), name="G4 Jacket", brand="Baracuta", category="jacket",
            description="Longer version of the G9. Three-quarter length with same iconic details.",
            fit="regular", style_tags=["heritage", "british", "classic"],
            colors=["navy", "tan"], materials=["cotton blend"], price_usd=425.00),
    ])

    # === UNIQLO ===
    items.extend([
        ClothingItem(id=next_id(), name="Ultra Light Down Jacket", brand="Uniqlo", category="jacket",
            description="Lightweight packable down jacket. Affordable warmth with minimal bulk.",
            fit="regular", style_tags=["minimalist", "affordable", "technical"],
            colors=["black", "navy", "olive"], materials=["nylon", "down"], price_usd=79.90),
        ClothingItem(id=next_id(), name="Selvedge Slim Fit Jeans", brand="Uniqlo", category="pants",
            description="Budget-friendly selvedge denim jeans. Good quality at affordable price.",
            fit="slim", style_tags=["affordable", "japanese", "raw denim"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=49.90),
        ClothingItem(id=next_id(), name="Supima Cotton Tee", brand="Uniqlo", category="t-shirt",
            description="High quality cotton t-shirt at budget price. Soft Supima cotton.",
            fit="regular", style_tags=["affordable", "basic", "minimalist"],
            colors=["white", "black", "grey", "navy"], materials=["supima cotton"], price_usd=14.90),
        ClothingItem(id=next_id(), name="U Crew Neck Tee", brand="Uniqlo", category="t-shirt",
            description="Uniqlo U designer collaboration tee. Elevated basics with interesting cuts.",
            fit="oversized", style_tags=["minimalist", "affordable", "designer"],
            colors=["white", "black", "olive"], materials=["cotton"], price_usd=19.90),
        ClothingItem(id=next_id(), name="Athletic Fit Chinos", brand="Uniqlo", category="pants",
            description="Stretchy cotton chinos with athletic fit. Tapered leg with room in thighs.",
            fit="athletic tapered", style_tags=["casual", "affordable"],
            colors=["navy", "khaki", "olive", "black"], materials=["cotton blend"], price_usd=39.90),
        ClothingItem(id=next_id(), name="EZY Ankle Pants", brand="Uniqlo", category="pants",
            description="Ultra stretch ankle pants. Comfortable with dress pant appearance.",
            fit="slim ankle", style_tags=["affordable", "comfortable", "casual"],
            colors=["black", "navy", "grey"], materials=["stretch polyester"], price_usd=39.90),
    ])

    # === CARHARTT WIP ===
    items.extend([
        ClothingItem(id=next_id(), name="Detroit Jacket", brand="Carhartt WIP", category="jacket",
            description="Classic workwear jacket with blanket lining. Iconic Carhartt silhouette.",
            fit="regular", style_tags=["workwear", "streetwear", "heritage"],
            colors=["black", "hamilton brown", "blue"], materials=["cotton duck"], price_usd=298.00),
        ClothingItem(id=next_id(), name="Sid Pant", brand="Carhartt WIP", category="pants",
            description="Slim fit chino with stretch. Modern workwear-inspired pants.",
            fit="slim", style_tags=["workwear", "streetwear", "casual"],
            colors=["black", "leather", "navy"], materials=["cotton twill"], price_usd=128.00),
        ClothingItem(id=next_id(), name="Chase Hoodie", brand="Carhartt WIP", category="hoodie",
            description="Heavyweight French terry hoodie with embroidered logo. Quality streetwear basic.",
            fit="regular", style_tags=["streetwear", "workwear", "casual"],
            colors=["black", "grey heather", "ash heather"], materials=["french terry"], price_usd=128.00),
        ClothingItem(id=next_id(), name="Double Knee Pant", brand="Carhartt WIP", category="pants",
            description="Classic workwear pants with reinforced knees. Relaxed fit in durable canvas.",
            fit="relaxed", style_tags=["workwear", "heritage", "durable"],
            colors=["brown", "black", "blue"], materials=["canvas"], price_usd=128.00),
        ClothingItem(id=next_id(), name="OG Active Jacket", brand="Carhartt WIP", category="jacket",
            description="Organic cotton duck jacket. Lighter weight version of classic Carhartt.",
            fit="regular", style_tags=["workwear", "streetwear", "casual"],
            colors=["black", "hamilton brown"], materials=["organic cotton"], price_usd=248.00),
    ])

    # === STAN RAY ===
    items.extend([
        ClothingItem(id=next_id(), name="OG Painter Pants", brand="Stan Ray", category="pants",
            description="Classic painter pants with loop for tools. Relaxed fit in durable cotton.",
            fit="relaxed", style_tags=["workwear", "americana", "simple"],
            colors=["white", "natural", "khaki"], materials=["cotton drill"], price_usd=85.00),
        ClothingItem(id=next_id(), name="Slim Fit Fatigue Pants", brand="Stan Ray", category="pants",
            description="Military fatigue pants in slimmer fit. Budget-friendly workwear essential.",
            fit="slim", style_tags=["workwear", "military", "affordable"],
            colors=["olive", "khaki", "black"], materials=["cotton ripstop"], price_usd=95.00),
        ClothingItem(id=next_id(), name="Taper Fit Fatigue", brand="Stan Ray", category="pants",
            description="Tapered version of classic fatigue pants. Modern silhouette with vintage details.",
            fit="tapered", style_tags=["workwear", "military", "modern"],
            colors=["olive", "khaki"], materials=["cotton ripstop"], price_usd=95.00),
        ClothingItem(id=next_id(), name="Shop Jacket", brand="Stan Ray", category="jacket",
            description="Simple cotton twill shop jacket. Clean workwear styling at accessible price.",
            fit="regular", style_tags=["workwear", "simple", "affordable"],
            colors=["navy", "black", "olive"], materials=["cotton twill"], price_usd=115.00),
    ])

    # === STONE ISLAND ===
    items.extend([
        ClothingItem(id=next_id(), name="Nylon Metal Overshirt", brand="Stone Island", category="jacket",
            description="Iconic nylon metal fabric overshirt. Unique iridescent quality from special dyeing process.",
            fit="regular", style_tags=["technical", "italian", "innovative"],
            colors=["black", "blue", "olive"], materials=["nylon metal"], price_usd=495.00),
        ClothingItem(id=next_id(), name="Ghost Piece Smock", brand="Stone Island", category="jacket",
            description="Badge-less Ghost collection piece. Minimal design with tonal branding.",
            fit="relaxed", style_tags=["technical", "minimalist", "innovative"],
            colors=["black", "military green"], materials=["cotton"], price_usd=425.00),
        ClothingItem(id=next_id(), name="Cargo Pants", brand="Stone Island", category="pants",
            description="Technical cargo pants with compass badge. Functional pockets with sporty design.",
            fit="regular", style_tags=["technical", "italian", "sporty"],
            colors=["black", "olive", "navy"], materials=["cotton blend"], price_usd=385.00),
        ClothingItem(id=next_id(), name="Crewneck Sweatshirt", brand="Stone Island", category="sweater",
            description="Classic sweatshirt with arm badge. Heavyweight garment-dyed cotton.",
            fit="regular", style_tags=["italian", "casual", "iconic"],
            colors=["black", "dust grey", "navy"], materials=["cotton fleece"], price_usd=295.00),
    ])

    # === STILL BY HAND (Contemporary Japanese) ===
    items.extend([
        ClothingItem(id=next_id(), name="Pleated Wide Chinos", brand="Still by Hand", category="pants",
            description="Wide leg pleated trousers in tan cotton. Relaxed Japanese contemporary design with earth tone palette.",
            fit="wide pleated", style_tags=["japanese", "contemporary", "relaxed"],
            colors=["tan", "beige", "earth tone"], materials=["cotton"], price_usd=265.00),
        ClothingItem(id=next_id(), name="Boxy Tee", brand="Still by Hand", category="t-shirt",
            description="Oversized boxy t-shirt in premium cotton. Clean contemporary Japanese design.",
            fit="boxy", style_tags=["japanese", "contemporary", "minimalist"],
            colors=["white", "black", "grey"], materials=["cotton"], price_usd=125.00),
        ClothingItem(id=next_id(), name="Relaxed Blazer", brand="Still by Hand", category="jacket",
            description="Unstructured linen cotton blazer. Casual tailoring with relaxed fit.",
            fit="relaxed", style_tags=["japanese", "contemporary", "casual"],
            colors=["navy", "beige"], materials=["linen cotton"], price_usd=385.00),
    ])

    # === VISVIM ===
    items.extend([
        ClothingItem(id=next_id(), name="FBT Moccasins", brand="Visvim", category="shoes",
            description="Signature folk-inspired moccasins. Hand-stitched with premium leather.",
            fit="regular", style_tags=["japanese", "artisanal", "heritage"],
            colors=["brown", "black"], materials=["leather"], price_usd=895.00),
        ClothingItem(id=next_id(), name="Noragi Jacket", brand="Visvim", category="jacket",
            description="Traditional Japanese work jacket. Kimono-inspired with modern construction.",
            fit="relaxed", style_tags=["japanese", "heritage", "artisanal"],
            colors=["indigo", "black"], materials=["cotton"], price_usd=1295.00),
        ClothingItem(id=next_id(), name="Social Sculpture Denim", brand="Visvim", category="pants",
            description="Handcrafted vintage-style denim. Exceptional aging and character.",
            fit="straight", style_tags=["japanese", "heritage", "artisanal"],
            colors=["indigo"], materials=["selvedge denim"], price_usd=895.00),
    ])

    # === ACNE STUDIOS ===
    items.extend([
        ClothingItem(id=next_id(), name="North Jeans", brand="Acne Studios", category="pants",
            description="Mid-rise straight leg jeans. Clean Scandinavian denim with quality construction.",
            fit="straight", style_tags=["minimalist", "scandinavian", "contemporary"],
            colors=["indigo", "black"], materials=["denim"], price_usd=280.00),
        ClothingItem(id=next_id(), name="River Jeans", brand="Acne Studios", category="pants",
            description="Tapered fit jeans with mid rise. Modern slim fit.",
            fit="tapered", style_tags=["minimalist", "scandinavian", "modern"],
            colors=["indigo", "black"], materials=["stretch denim"], price_usd=280.00),
        ClothingItem(id=next_id(), name="Face Patch Hoodie", brand="Acne Studios", category="hoodie",
            description="Oversized hoodie with signature face patch. Premium Scandinavian streetwear.",
            fit="oversized", style_tags=["minimalist", "scandinavian", "iconic"],
            colors=["pale pink", "black", "grey"], materials=["cotton fleece"], price_usd=380.00),
        ClothingItem(id=next_id(), name="Oversized Sweater", brand="Acne Studios", category="sweater",
            description="Chunky oversized wool sweater. Cozy minimalist knitwear.",
            fit="oversized", style_tags=["minimalist", "scandinavian", "cozy"],
            colors=["cream", "black", "grey"], materials=["wool"], price_usd=450.00),
    ])

    return items


def generate_sample_discussions() -> list[StyleDiscussion]:
    """Generate 20+ Reddit-style discussions for style recommendations."""
    discussions = [
        StyleDiscussion(
            id="disc_001",
            title="Best brands for relaxed Japanese workwear aesthetic?",
            content="Looking to build a wardrobe around Japanese workwear. I love the relaxed fits and earth tones. Budget is around $200-400 per piece. Already have some Orslow pieces but looking for alternatives.",
            mentioned_brands=["Orslow", "Engineered Garments", "Kapital", "Stan Ray"],
            mentioned_items=["fatigue pants", "chore coat", "overshirt"],
            style_descriptors=["japanese", "workwear", "relaxed", "earth tones"],
            source_url="https://reddit.com/r/malefashionadvice/comments/example1",
            subreddit="malefashionadvice", upvotes=245, num_comments=89,
        ),
        StyleDiscussion(
            id="disc_002",
            title="Scandinavian minimalism - building a capsule wardrobe",
            content="I'm tired of fast fashion and want to invest in quality minimalist pieces. Love the clean lines of Norse Projects and COS. Looking for neutral colors - black, white, grey, navy.",
            mentioned_brands=["Norse Projects", "COS", "Arket", "Our Legacy", "Acne Studios"],
            mentioned_items=["shirt", "trousers", "sweater"],
            style_descriptors=["minimalist", "scandinavian", "neutral", "capsule", "quality"],
            source_url="https://reddit.com/r/malefashionadvice/comments/example2",
            subreddit="malefashionadvice", upvotes=312, num_comments=124,
        ),
        StyleDiscussion(
            id="disc_003",
            title="Raw denim recommendations for slim tapered fit with high rise?",
            content="My favorite pair of jeans are wearing out. Need something with high rise for comfort but slim tapered for modern look. Prefer unsanforized for the fading journey. Budget around $300.",
            mentioned_brands=["3sixteen", "Pure Blue Japan", "Iron Heart", "Rogue Territory"],
            mentioned_items=["jeans", "raw denim"],
            style_descriptors=["slim tapered", "high rise", "raw denim", "fading"],
            source_url="https://reddit.com/r/rawdenim/comments/example3",
            subreddit="rawdenim", upvotes=156, num_comments=67,
        ),
        StyleDiscussion(
            id="disc_004",
            title="Techwear that doesn't look like you're cosplaying",
            content="I love the functionality of techwear but hate the ninja aesthetic. Looking for subtle technical pieces. Arc'teryx Veilance seems perfect but the price is insane. Any alternatives?",
            mentioned_brands=["Arc'teryx", "Outlier", "Veilance", "Acronym"],
            mentioned_items=["jacket", "pants", "technical"],
            style_descriptors=["techwear", "minimalist", "technical", "functional", "subtle"],
            source_url="https://reddit.com/r/techwearclothing/comments/example4",
            subreddit="techwearclothing", upvotes=423, num_comments=198,
        ),
        StyleDiscussion(
            id="disc_005",
            title="Wide leg pants revolution - recommendations?",
            content="Finally embracing wider fits after years of skinny jeans. Looking for wide leg or straight leg pants that aren't too extreme. Like the silhouette of Lemaire and Still by Hand. Earth tones preferred.",
            mentioned_brands=["Lemaire", "Still by Hand", "Our Legacy", "Engineered Garments"],
            mentioned_items=["wide leg pants", "trousers"],
            style_descriptors=["wide leg", "relaxed", "earth tones", "contemporary"],
            source_url="https://reddit.com/r/malefashion/comments/example5",
            subreddit="malefashion", upvotes=287, num_comments=95,
        ),
        StyleDiscussion(
            id="disc_006",
            title="Best heavyweight flannel shirts?",
            content="Looking for really thick flannel shirts. Talking 10oz+ fabric. Iron Heart seems to be the gold standard but open to alternatives. Want something that will last decades.",
            mentioned_brands=["Iron Heart", "The Flat Head", "3sixteen", "Freenote Cloth"],
            mentioned_items=["flannel shirt", "heavyweight"],
            style_descriptors=["heavyweight", "durable", "workwear", "quality"],
            source_url="https://reddit.com/r/rawdenim/comments/example6",
            subreddit="rawdenim", upvotes=189, num_comments=76,
        ),
        StyleDiscussion(
            id="disc_007",
            title="French minimalist brands besides A.P.C.?",
            content="Love the clean A.P.C. aesthetic but want to explore more French brands. Looking for that effortless Parisian style - simple, well-made basics.",
            mentioned_brands=["A.P.C.", "Lemaire", "AMI", "Sandro"],
            mentioned_items=["jeans", "shirts", "basics"],
            style_descriptors=["minimalist", "french", "clean", "understated"],
            source_url="https://reddit.com/r/malefashionadvice/comments/example7",
            subreddit="malefashionadvice", upvotes=267, num_comments=103,
        ),
        StyleDiscussion(
            id="disc_008",
            title="Heritage boots - Red Wing vs Viberg vs Alden",
            content="Ready to invest in a pair of quality boots that will last 10+ years. Stuck between these three brands. Mostly wearing with jeans and chinos. Which offers best value?",
            mentioned_brands=["Red Wing", "Viberg", "Alden", "Wolverine"],
            mentioned_items=["boots", "heritage footwear"],
            style_descriptors=["heritage", "americana", "durable", "investment"],
            source_url="https://reddit.com/r/goodyearwelt/comments/example8",
            subreddit="goodyearwelt", upvotes=534, num_comments=278,
        ),
        StyleDiscussion(
            id="disc_009",
            title="Oversized streetwear that's not hypebeast?",
            content="Want to try oversized fits but don't want to look like I'm trying too hard. More Japanese streetwear vibe than Supreme hype. Needles and Kapital catch my eye.",
            mentioned_brands=["Needles", "Kapital", "Orslow", "Engineered Garments"],
            mentioned_items=["track pants", "oversized shirts"],
            style_descriptors=["oversized", "japanese", "streetwear", "relaxed"],
            source_url="https://reddit.com/r/streetwear/comments/example9",
            subreddit="streetwear", upvotes=198, num_comments=84,
        ),
        StyleDiscussion(
            id="disc_010",
            title="Best budget raw denim?",
            content="Want to get into raw denim but can't justify $300+ jeans yet. Are Uniqlo selvedge or Brave Star worth it? Or should I just save up for 3sixteen?",
            mentioned_brands=["Uniqlo", "Brave Star", "3sixteen", "Gustin"],
            mentioned_items=["raw denim", "selvedge jeans"],
            style_descriptors=["raw denim", "budget", "affordable", "entry-level"],
            source_url="https://reddit.com/r/rawdenim/comments/example10",
            subreddit="rawdenim", upvotes=445, num_comments=234,
        ),
        StyleDiscussion(
            id="disc_011",
            title="British heritage brands for waxed jackets",
            content="Looking for a quality waxed cotton jacket. Barbour is the obvious choice but are there alternatives? Want something for rainy city weather.",
            mentioned_brands=["Barbour", "Baracuta", "Private White V.C.", "Grenfell"],
            mentioned_items=["waxed jacket", "rain jacket"],
            style_descriptors=["british", "heritage", "waterproof", "classic"],
            source_url="https://reddit.com/r/malefashionadvice/comments/example11",
            subreddit="malefashionadvice", upvotes=178, num_comments=67,
        ),
        StyleDiscussion(
            id="disc_012",
            title="Carhartt WIP vs mainline Carhartt",
            content="What's the actual difference? WIP seems more expensive for similar products. Is it just the fit and fashion cred?",
            mentioned_brands=["Carhartt WIP", "Carhartt", "Dickies", "Stan Ray"],
            mentioned_items=["work jacket", "chore coat"],
            style_descriptors=["workwear", "streetwear", "value"],
            source_url="https://reddit.com/r/malefashionadvice/comments/example12",
            subreddit="malefashionadvice", upvotes=356, num_comments=189,
        ),
        StyleDiscussion(
            id="disc_013",
            title="Stone Island - worth the hype?",
            content="I keep seeing Stone Island everywhere. Is it actually quality or just brand tax? The fabric research seems interesting but prices are steep.",
            mentioned_brands=["Stone Island", "C.P. Company", "Acronym"],
            mentioned_items=["nylon jacket", "overshirt"],
            style_descriptors=["technical", "italian", "innovative"],
            source_url="https://reddit.com/r/malefashion/comments/example13",
            subreddit="malefashion", upvotes=234, num_comments=156,
        ),
        StyleDiscussion(
            id="disc_014",
            title="Alternatives to Outlier pants?",
            content="Love Outlier Futureworks but want to explore other technical pants brands. Something with stretch and water resistance that looks like regular chinos.",
            mentioned_brands=["Outlier", "Western Rise", "Bluffworks", "Mission Workshop"],
            mentioned_items=["technical pants", "stretch chinos"],
            style_descriptors=["techwear", "minimalist", "technical", "versatile"],
            source_url="https://reddit.com/r/onebag/comments/example14",
            subreddit="onebag", upvotes=289, num_comments=134,
        ),
        StyleDiscussion(
            id="disc_015",
            title="Building a workwear wardrobe on a budget",
            content="Love the workwear aesthetic but can't afford Engineered Garments prices. Stan Ray and Dickies seem like good budget options. Any other recommendations?",
            mentioned_brands=["Stan Ray", "Dickies", "Carhartt WIP", "Universal Works"],
            mentioned_items=["fatigue pants", "shop jacket", "chore coat"],
            style_descriptors=["workwear", "budget", "affordable", "military"],
            source_url="https://reddit.com/r/frugalmalefashion/comments/example15",
            subreddit="frugalmalefashion", upvotes=567, num_comments=298,
        ),
        StyleDiscussion(
            id="disc_016",
            title="Best Oxford cloth button down shirts?",
            content="Looking for the perfect OCBD. Tried Uniqlo but want something better quality. Norse Projects Anton looks nice. What about Kamakura or Gitman?",
            mentioned_brands=["Norse Projects", "Kamakura", "Gitman Vintage", "Uniqlo"],
            mentioned_items=["oxford shirt", "button down"],
            style_descriptors=["classic", "minimalist", "quality", "smart casual"],
            source_url="https://reddit.com/r/malefashionadvice/comments/example16",
            subreddit="malefashionadvice", upvotes=423, num_comments=234,
        ),
        StyleDiscussion(
            id="disc_017",
            title="Aimé Leon Dore aesthetic on a budget",
            content="Love ALD's preppy streetwear vibe but can't afford their prices. Looking for rugby shirts, quality basics, vintage sports influence. Any alternatives?",
            mentioned_brands=["Aimé Leon Dore", "Noah", "Rowing Blazers", "J.Crew"],
            mentioned_items=["rugby shirt", "sweatshirts"],
            style_descriptors=["preppy", "streetwear", "vintage", "refined"],
            source_url="https://reddit.com/r/streetwear/comments/example17",
            subreddit="streetwear", upvotes=312, num_comments=145,
        ),
        StyleDiscussion(
            id="disc_018",
            title="Super heavyweight denim - is it worth it?",
            content="Thinking about getting Iron Heart 21oz or 25oz denim. Is super heavy denim actually better or just a flex? Anyone have experience breaking them in?",
            mentioned_brands=["Iron Heart", "Samurai", "The Flat Head"],
            mentioned_items=["heavyweight denim", "jeans"],
            style_descriptors=["heavyweight", "raw denim", "extreme", "japanese"],
            source_url="https://reddit.com/r/rawdenim/comments/example18",
            subreddit="rawdenim", upvotes=278, num_comments=189,
        ),
        StyleDiscussion(
            id="disc_019",
            title="Quiet luxury menswear brands",
            content="Looking for understated luxury. No obvious logos, quality materials, timeless design. Margaret Howell, Lemaire - what else fits this aesthetic?",
            mentioned_brands=["Margaret Howell", "Lemaire", "Auralee", "Studio Nicholson"],
            mentioned_items=["coats", "trousers", "shirts"],
            style_descriptors=["minimalist", "quiet luxury", "understated", "quality"],
            source_url="https://reddit.com/r/malefashion/comments/example19",
            subreddit="malefashion", upvotes=398, num_comments=167,
        ),
        StyleDiscussion(
            id="disc_020",
            title="Indigo dyed everything - recommendations?",
            content="Obsessed with indigo. Want to build wardrobe around natural indigo pieces. Kapital and Pure Blue Japan do amazing indigo work. Any other brands?",
            mentioned_brands=["Kapital", "Pure Blue Japan", "Blue Blue Japan", "Orslow"],
            mentioned_items=["indigo dyed clothing", "sashiko"],
            style_descriptors=["japanese", "indigo", "artisanal", "natural dye"],
            source_url="https://reddit.com/r/rawdenim/comments/example20",
            subreddit="rawdenim", upvotes=234, num_comments=98,
        ),
    ]
    return discussions


def save_sample_data():
    """Save all sample data to JSON files."""
    import os

    samples_dir = os.path.dirname(__file__)

    items = generate_sample_items()
    brands = generate_sample_brands()
    discussions = generate_sample_discussions()

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
