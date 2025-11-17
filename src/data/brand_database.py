"""
Comprehensive brand and product database for menswear.

This module contains curated data for hundreds of menswear brands
with their typical products, aesthetics, and characteristics.

This approach is more reliable than scraping sites with bot protection.
"""
import uuid
from typing import List, Dict
from ..models.clothing import ClothingItem, Brand, StyleDiscussion


# Comprehensive brand definitions
BRAND_DATABASE = {
    # === JAPANESE WORKWEAR ===
    "Orslow": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "workwear", "heritage", "military"],
        "typical_fits": ["relaxed", "relaxed tapered", "wide"],
        "signature_items": ["fatigue pants", "105 jeans", "US Army overshirt"],
        "products": [
            {"name": "Fatigue Pants", "category": "pants", "fit": "relaxed tapered", "description": "Classic US Army fatigue pants reimagined with Japanese attention to detail. Back cinch, French seams.", "price": 295, "colors": ["olive", "khaki"], "materials": ["ripstop cotton"]},
            {"name": "105 Standard Fit Jeans", "category": "pants", "fit": "straight", "description": "High-rise straight leg selvedge denim. Classic workwear silhouette.", "price": 320, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "US Army Shirt", "category": "shirt", "fit": "relaxed", "description": "Vintage military shirt in cotton sateen. Two flap pockets.", "price": 265, "colors": ["olive", "khaki"], "materials": ["cotton sateen"]},
            {"name": "French Work Pants", "category": "pants", "fit": "wide", "description": "Wide leg work pants inspired by French vintage. High rise, pleated front.", "price": 285, "colors": ["navy", "ecru"], "materials": ["herringbone cotton"]},
            {"name": "50's Chambray Shirt", "category": "shirt", "fit": "regular", "description": "Triple-stitched chambray work shirt. Vintage American style.", "price": 245, "colors": ["chambray blue"], "materials": ["chambray cotton"]},
        ]
    },
    "Engineered Garments": {
        "origin": "USA (Japanese designer)",
        "price_range": "premium",
        "aesthetics": ["japanese", "americana", "patchwork", "eclectic"],
        "typical_fits": ["relaxed", "oversized", "boxy"],
        "signature_items": ["Bedford jacket", "Fatigue pants", "Dayton shirt"],
        "products": [
            {"name": "Bedford Jacket", "category": "jacket", "fit": "relaxed", "description": "Unlined cotton work jacket with four patch pockets. Sack coat silhouette.", "price": 485, "colors": ["olive", "navy", "khaki"], "materials": ["cotton ripstop"]},
            {"name": "Fatigue Pant", "category": "pants", "fit": "relaxed tapered", "description": "6-pocket fatigue pants with back cinch. Multiple fabric options.", "price": 345, "colors": ["olive", "navy"], "materials": ["cotton twill"]},
            {"name": "Dayton Shirt", "category": "shirt", "fit": "relaxed", "description": "Oversized work shirt with large patch pockets. Camp collar.", "price": 295, "colors": ["navy", "olive", "multi"], "materials": ["cotton"]},
            {"name": "Andover Jacket", "category": "jacket", "fit": "relaxed", "description": "Unstructured sport coat with patch pockets. Soft tailoring.", "price": 595, "colors": ["navy", "grey"], "materials": ["wool blend"]},
            {"name": "Carlyle Pant", "category": "pants", "fit": "wide pleated", "description": "High-waisted pleated trousers. Wide leg, adjustable waistband.", "price": 365, "colors": ["navy", "khaki", "grey"], "materials": ["tropical wool"]},
        ]
    },
    "Kapital": {
        "origin": "Japan",
        "price_range": "luxury",
        "aesthetics": ["japanese", "americana", "boro", "patchwork", "eclectic"],
        "typical_fits": ["relaxed", "oversized"],
        "signature_items": ["Ring coat", "Century denim", "Kountry items"],
        "products": [
            {"name": "Ring Coat", "category": "jacket", "fit": "oversized", "description": "Signature patchwork coat with circular design. Wabisabi aesthetic.", "price": 1295, "colors": ["indigo multi"], "materials": ["cotton patchwork"]},
            {"name": "Century Denim Jeans", "category": "pants", "fit": "relaxed", "description": "Heavily distressed and repaired jeans. Boro-inspired patchwork.", "price": 595, "colors": ["indigo"], "materials": ["denim"]},
            {"name": "Kountry Bandana Shirt", "category": "shirt", "fit": "relaxed", "description": "Shirt made from vintage bandanas. Unique patchwork construction.", "price": 445, "colors": ["multi"], "materials": ["cotton bandana"]},
            {"name": "Smiley Sweatshirt", "category": "sweater", "fit": "oversized", "description": "Loopwheel fleece with embroidered smiley. Japanese-made.", "price": 395, "colors": ["grey", "navy"], "materials": ["loopwheel cotton"]},
            {"name": "Mil Cargo Pants", "category": "pants", "fit": "wide", "description": "Wide leg military cargo pants. Multiple pockets.", "price": 425, "colors": ["olive", "khaki"], "materials": ["cotton ripstop"]},
        ]
    },

    # === SCANDINAVIAN MINIMALIST ===
    "Norse Projects": {
        "origin": "Denmark",
        "price_range": "premium",
        "aesthetics": ["scandinavian", "minimalist", "functional"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Aros chinos", "Niels tee", "Norse beanie"],
        "products": [
            {"name": "Aros Regular Chinos", "category": "pants", "fit": "regular", "description": "Core chino in Italian stretch cotton. Clean minimal design.", "price": 195, "colors": ["navy", "khaki", "black", "stone"], "materials": ["stretch cotton"]},
            {"name": "Niels Standard Tee", "category": "t-shirt", "fit": "regular", "description": "Heavyweight organic cotton tee. Box logo detail.", "price": 75, "colors": ["white", "navy", "black", "grey"], "materials": ["organic cotton"]},
            {"name": "Sigfred Merino Sweater", "category": "sweater", "fit": "regular", "description": "Lightweight merino wool crewneck. Temperature regulating.", "price": 225, "colors": ["navy", "grey", "black"], "materials": ["merino wool"]},
            {"name": "Skagen Sunwashed Chinos", "category": "pants", "fit": "tapered", "description": "Relaxed tapered chinos with subtle texture.", "price": 185, "colors": ["ecru", "olive", "navy"], "materials": ["cotton twill"]},
            {"name": "Hugo Light Jacket", "category": "jacket", "fit": "regular", "description": "Lightweight technical jacket. Water resistant, minimal design.", "price": 295, "colors": ["black", "navy"], "materials": ["technical nylon"]},
        ]
    },
    "Our Legacy": {
        "origin": "Sweden",
        "price_range": "premium",
        "aesthetics": ["scandinavian", "contemporary", "relaxed", "experimental"],
        "typical_fits": ["relaxed", "oversized", "boxy"],
        "signature_items": ["Box shirt", "Borrowed jeans", "Evening coat"],
        "products": [
            {"name": "Box Shirt Short Sleeve", "category": "shirt", "fit": "boxy", "description": "Relaxed camp collar shirt. Signature box cut.", "price": 245, "colors": ["white", "black", "blue"], "materials": ["cotton"]},
            {"name": "Borrowed Jeans", "category": "pants", "fit": "wide straight", "description": "Wide leg jeans with high rise. Borrowed from menswear archives.", "price": 295, "colors": ["indigo", "black"], "materials": ["selvedge denim"]},
            {"name": "Evening Coach Jacket", "category": "jacket", "fit": "relaxed", "description": "Oversized coach jacket with snap closures.", "price": 425, "colors": ["black", "navy"], "materials": ["nylon"]},
            {"name": "Camo Sweater", "category": "sweater", "fit": "oversized", "description": "Oversized mohair-blend sweater. Textured knit.", "price": 395, "colors": ["brown", "grey", "navy"], "materials": ["mohair wool blend"]},
            {"name": "Classic Shirt", "category": "shirt", "fit": "regular", "description": "Well-proportioned cotton poplin shirt.", "price": 195, "colors": ["white", "light blue", "black"], "materials": ["cotton poplin"]},
        ]
    },

    # === RAW DENIM ===
    "Iron Heart": {
        "origin": "Japan",
        "price_range": "luxury",
        "aesthetics": ["japanese", "raw denim", "heavyweight", "motorcycle"],
        "typical_fits": ["straight", "slim straight", "relaxed tapered"],
        "signature_items": ["21oz denim", "Heavy flannel", "Work shirts"],
        "products": [
            {"name": "IH-634S 21oz Selvedge Jeans", "category": "pants", "fit": "straight", "description": "21oz heavyweight selvedge denim. Signature Iron Heart weight.", "price": 395, "colors": ["indigo"], "materials": ["21oz selvedge denim"]},
            {"name": "IH-666S Devil's Fit Jeans", "category": "pants", "fit": "slim straight", "description": "Slim straight fit in 21oz selvedge. Modern cut with heritage weight.", "price": 395, "colors": ["indigo"], "materials": ["21oz selvedge denim"]},
            {"name": "Ultra Heavy Flannel", "category": "shirt", "fit": "regular", "description": "9oz ultra heavy flannel shirt. Extremely substantial.", "price": 345, "colors": ["red check", "grey check", "navy check"], "materials": ["heavy flannel"]},
            {"name": "Work Shirt", "category": "shirt", "fit": "regular", "description": "Heavy cotton work shirt with western yoke.", "price": 295, "colors": ["indigo", "black"], "materials": ["heavy cotton"]},
            {"name": "Leather Rider Jacket", "category": "jacket", "fit": "regular", "description": "Japanese-made leather motorcycle jacket.", "price": 1895, "colors": ["black"], "materials": ["horsehide leather"]},
        ]
    },
    "3sixteen": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["americana", "raw denim", "modern heritage"],
        "typical_fits": ["slim tapered", "straight tapered", "relaxed tapered"],
        "signature_items": ["ST jeans", "CT jeans", "Type 3s jacket"],
        "products": [
            {"name": "ST-100x Slim Tapered Jeans", "category": "pants", "fit": "slim tapered", "description": "Slim tapered fit in double black selvedge. Modern cut.", "price": 265, "colors": ["double black"], "materials": ["selvedge denim"]},
            {"name": "CT-100x Classic Tapered", "category": "pants", "fit": "straight tapered", "description": "Classic tapered fit, relaxed top block. Indigo selvedge.", "price": 265, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "Type 3s Denim Jacket", "category": "jacket", "fit": "regular", "description": "Modified type 3 trucker jacket. Shadow selvedge.", "price": 285, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "Heavyweight Tee", "category": "t-shirt", "fit": "regular", "description": "Made in USA heavyweight cotton tee.", "price": 65, "colors": ["white", "black", "grey"], "materials": ["heavyweight cotton"]},
            {"name": "Caustic Wave Flannel", "category": "shirt", "fit": "regular", "description": "Heavy flannel with unique caustic wash.", "price": 225, "colors": ["brown", "grey", "green"], "materials": ["cotton flannel"]},
        ]
    },

    # === TECHWEAR ===
    "Arc'teryx Veilance": {
        "origin": "Canada",
        "price_range": "luxury",
        "aesthetics": ["techwear", "urban", "technical", "minimalist"],
        "typical_fits": ["articulated", "slim", "regular"],
        "signature_items": ["Field jacket", "Voronoi pants", "Monitor coat"],
        "products": [
            {"name": "Field LT Jacket", "category": "jacket", "fit": "regular", "description": "Technical field jacket in GORE-TEX. Urban technical wear.", "price": 1200, "colors": ["black", "dark navy"], "materials": ["gore-tex"]},
            {"name": "Voronoi Pants", "category": "pants", "fit": "tapered", "description": "Technical pants with articulated knees. Water resistant.", "price": 495, "colors": ["black", "grey"], "materials": ["schoeller softshell"]},
            {"name": "Monitor Down Coat", "category": "jacket", "fit": "regular", "description": "GORE-TEX down coat. Extreme weather protection.", "price": 1500, "colors": ["black"], "materials": ["gore-tex", "down"]},
            {"name": "Align MX Pant", "category": "pants", "fit": "slim", "description": "Stretch technical pants. 4-way stretch.", "price": 395, "colors": ["black", "grey"], "materials": ["stretch technical"]},
            {"name": "Mionn IS Jacket", "category": "jacket", "fit": "regular", "description": "Synthetic insulated jacket. Lightweight warmth.", "price": 495, "colors": ["black", "dark navy"], "materials": ["coreloft insulation"]},
        ]
    },
    "Acronym": {
        "origin": "Germany",
        "price_range": "luxury",
        "aesthetics": ["techwear", "avant-garde", "technical", "urban"],
        "typical_fits": ["articulated", "slim", "modern"],
        "signature_items": ["J1A jacket", "P10 pants", "3A bags"],
        "products": [
            {"name": "J1A-GTKP Jacket", "category": "jacket", "fit": "technical", "description": "GORE-TEX Pro jacket with integrated storage. Gravity pockets.", "price": 2200, "colors": ["black"], "materials": ["gore-tex pro"]},
            {"name": "P10-DS Pants", "category": "pants", "fit": "tapered", "description": "Technical cargo pants with die-cut pockets. Schoeller dryskin.", "price": 895, "colors": ["black", "alpha green"], "materials": ["schoeller dryskin"]},
            {"name": "S25-DS Shirt", "category": "shirt", "fit": "regular", "description": "Technical shirt with magnetic closures.", "price": 595, "colors": ["black"], "materials": ["dryskin"]},
            {"name": "J28-GT Jacket", "category": "jacket", "fit": "regular", "description": "Lightweight GORE-TEX shell. Packable.", "price": 1495, "colors": ["black", "raf green"], "materials": ["gore-tex"]},
            {"name": "LA6B-DS Long Sleeve", "category": "shirt", "fit": "regular", "description": "Long sleeve technical tee.", "price": 295, "colors": ["black"], "materials": ["dryskin"]},
        ]
    },

    # === HERITAGE AMERICANA ===
    "Red Wing Heritage": {
        "origin": "USA",
        "price_range": "mid",
        "aesthetics": ["americana", "heritage", "workwear"],
        "typical_fits": ["regular"],
        "signature_items": ["Iron Ranger", "Moc Toe", "Beckman"],
        "products": [
            {"name": "Iron Ranger 8111", "category": "shoes", "fit": "regular", "description": "Cap toe boot in Amber Harness leather. Nitrile cork sole.", "price": 350, "colors": ["amber"], "materials": ["leather"]},
            {"name": "Classic Moc 875", "category": "shoes", "fit": "regular", "description": "6-inch moc toe boot in Oro Legacy leather. Traction Tred sole.", "price": 310, "colors": ["oro legacy"], "materials": ["leather"]},
            {"name": "Blacksmith 3345", "category": "shoes", "fit": "regular", "description": "6-inch round toe boot. Prairie leather.", "price": 340, "colors": ["copper"], "materials": ["leather"]},
            {"name": "Beckman 9011", "category": "shoes", "fit": "regular", "description": "Gentleman traveler boot. Black Cherry Featherstone.", "price": 400, "colors": ["black cherry"], "materials": ["featherstone leather"]},
            {"name": "Clara Boot", "category": "shoes", "fit": "regular", "description": "Women's heeled boot. Red leather.", "price": 390, "colors": ["red"], "materials": ["leather"]},
        ]
    },
    "Filson": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["americana", "heritage", "outdoor", "rugged"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Mackinaw Cruiser", "Original Briefcase", "Tin cloth"],
        "products": [
            {"name": "Mackinaw Cruiser", "category": "jacket", "fit": "regular", "description": "Virgin wool cruiser jacket. Legendary durability.", "price": 495, "colors": ["forest green", "charcoal"], "materials": ["mackinaw wool"]},
            {"name": "Tin Cloth Packer Coat", "category": "jacket", "fit": "relaxed", "description": "Waxed cotton coat. 100-year oil finish.", "price": 595, "colors": ["dark tan"], "materials": ["tin cloth"]},
            {"name": "Original Briefcase", "category": "accessories", "fit": "one size", "description": "Rugged twill briefcase with leather handles.", "price": 425, "colors": ["otter green", "tan"], "materials": ["rugged twill", "bridle leather"]},
            {"name": "Short Cruiser Jacket", "category": "jacket", "fit": "regular", "description": "Shorter wool cruiser. Windproof.", "price": 395, "colors": ["charcoal", "red"], "materials": ["mackinaw wool"]},
            {"name": "Ranger Backpack", "category": "accessories", "fit": "one size", "description": "Heavy-duty backpack. Lifetime guarantee.", "price": 425, "colors": ["otter green"], "materials": ["rugged twill"]},
        ]
    },

    # Add more brands...
}

# Continue with more brands
BRAND_DATABASE.update({
    "A.P.C.": {
        "origin": "France",
        "price_range": "premium",
        "aesthetics": ["french", "minimalist", "clean", "contemporary"],
        "typical_fits": ["slim", "regular"],
        "signature_items": ["Petit Standard jeans", "Minimal wallet", "Logo tee"],
        "products": [
            {"name": "Petit Standard Jeans", "category": "pants", "fit": "slim", "description": "Slim fit raw selvedge denim. French minimalist denim.", "price": 235, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "Petit New Standard", "category": "pants", "fit": "slim straight", "description": "Slim straight Japanese selvedge. Medium rise.", "price": 235, "colors": ["indigo", "black"], "materials": ["selvedge denim"]},
            {"name": "Logo Tee", "category": "t-shirt", "fit": "regular", "description": "Clean cotton tee with minimal A.P.C. branding.", "price": 95, "colors": ["white", "black", "navy"], "materials": ["cotton"]},
            {"name": "New Portefeuille", "category": "accessories", "fit": "one size", "description": "Minimal leather wallet. Clean design.", "price": 175, "colors": ["black", "brown"], "materials": ["leather"]},
            {"name": "Wool Sweater", "category": "sweater", "fit": "regular", "description": "Fine merino wool sweater. Minimal design.", "price": 295, "colors": ["grey", "navy", "black"], "materials": ["merino wool"]},
        ]
    },
    "Carhartt WIP": {
        "origin": "Germany/USA",
        "price_range": "mid",
        "aesthetics": ["workwear", "streetwear", "casual"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Michigan chore coat", "Sid pants", "Pocket tee"],
        "products": [
            {"name": "Michigan Chore Coat", "category": "jacket", "fit": "regular", "description": "Classic chore coat in organic cotton canvas.", "price": 215, "colors": ["black", "hamilton brown", "dusty brown"], "materials": ["organic cotton canvas"]},
            {"name": "Sid Pants", "category": "pants", "fit": "slim tapered", "description": "Slim tapered chinos. Modern workwear.", "price": 125, "colors": ["black", "navy", "grey"], "materials": ["cotton twill"]},
            {"name": "Pocket Tee", "category": "t-shirt", "fit": "regular", "description": "Single pocket tee with logo label.", "price": 45, "colors": ["white", "black", "grey", "navy"], "materials": ["cotton"]},
            {"name": "Active Jacket", "category": "jacket", "fit": "regular", "description": "Nylon shell jacket. Lightweight.", "price": 165, "colors": ["black", "camo"], "materials": ["nylon"]},
            {"name": "Chase Hoodie", "category": "hoodie", "fit": "regular", "description": "Heavyweight fleece hoodie with embroidered logo.", "price": 135, "colors": ["grey", "black", "navy"], "materials": ["cotton fleece"]},
        ]
    },
    "Stone Island": {
        "origin": "Italy",
        "price_range": "luxury",
        "aesthetics": ["italian", "technical", "experimental", "streetwear"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Compass badge", "Ghost pieces", "Shadow Project"],
        "products": [
            {"name": "Garment Dyed Crewneck", "category": "sweater", "fit": "regular", "description": "Cotton fleece with compass badge. Signature garment dyeing.", "price": 345, "colors": ["black", "navy", "dust grey"], "materials": ["cotton fleece"]},
            {"name": "Soft Shell Jacket", "category": "jacket", "fit": "regular", "description": "Technical soft shell with compass badge.", "price": 595, "colors": ["black", "olive"], "materials": ["soft shell"]},
            {"name": "Cargo Pants", "category": "pants", "fit": "regular", "description": "Cotton cargo with compass badge detail.", "price": 395, "colors": ["black", "olive", "navy"], "materials": ["cotton"]},
            {"name": "Ghost Piece Jacket", "category": "jacket", "fit": "regular", "description": "Monochrome piece with hidden badge.", "price": 795, "colors": ["black", "white"], "materials": ["cotton nylon"]},
            {"name": "Logo Tee", "category": "t-shirt", "fit": "regular", "description": "Cotton tee with compass logo print.", "price": 145, "colors": ["white", "black", "navy"], "materials": ["cotton"]},
        ]
    },
    "Lemaire": {
        "origin": "France",
        "price_range": "luxury",
        "aesthetics": ["french", "minimalist", "relaxed", "contemporary"],
        "typical_fits": ["relaxed", "oversized", "draped"],
        "signature_items": ["Croissant bag", "Twisted pants", "Relaxed tailoring"],
        "products": [
            {"name": "Twisted Pants", "category": "pants", "fit": "relaxed tapered", "description": "Signature twisted seam construction. Unique drape.", "price": 495, "colors": ["black", "grey", "navy"], "materials": ["wool blend"]},
            {"name": "Soft Single-Breasted Jacket", "category": "jacket", "fit": "relaxed", "description": "Unstructured wool blazer. Dropped shoulders.", "price": 1195, "colors": ["black", "grey", "navy"], "materials": ["wool"]},
            {"name": "Stand Collar Shirt", "category": "shirt", "fit": "relaxed", "description": "Mandarin collar cotton shirt. Clean minimal.", "price": 395, "colors": ["white", "blue", "black"], "materials": ["cotton poplin"]},
            {"name": "Croissant Bag", "category": "accessories", "fit": "one size", "description": "Signature half-moon shaped bag.", "price": 695, "colors": ["black", "brown", "cream"], "materials": ["leather"]},
            {"name": "Seamless T-Shirt", "category": "t-shirt", "fit": "relaxed", "description": "Tubular knit tee with minimal seams.", "price": 195, "colors": ["white", "black", "grey"], "materials": ["cotton jersey"]},
        ]
    },
    "Uniqlo": {
        "origin": "Japan",
        "price_range": "budget",
        "aesthetics": ["minimalist", "japanese", "functional", "affordable"],
        "typical_fits": ["regular", "slim", "relaxed"],
        "signature_items": ["HEATTECH", "AIRism", "Ultra Light Down"],
        "products": [
            {"name": "Ultra Light Down Jacket", "category": "jacket", "fit": "regular", "description": "Lightweight down jacket. Packable warmth.", "price": 69, "colors": ["black", "navy", "wine"], "materials": ["nylon", "down"]},
            {"name": "EZY Ankle Pants", "category": "pants", "fit": "slim tapered", "description": "Stretch ankle pants. Comfort and style.", "price": 39, "colors": ["black", "navy", "grey"], "materials": ["stretch polyester"]},
            {"name": "Supima Cotton Tee", "category": "t-shirt", "fit": "regular", "description": "Premium cotton tee at budget price.", "price": 14, "colors": ["white", "black", "grey", "navy"], "materials": ["supima cotton"]},
            {"name": "Selvedge Slim Jeans", "category": "pants", "fit": "slim", "description": "Kaihara selvedge denim at accessible price.", "price": 49, "colors": ["indigo", "black"], "materials": ["selvedge denim"]},
            {"name": "Blocktech Parka", "category": "jacket", "fit": "regular", "description": "Water-repellent technical parka.", "price": 99, "colors": ["black", "olive"], "materials": ["technical polyester"]},
        ]
    },
})

# Add more brands for comprehensive coverage
BRAND_DATABASE.update({
    "Visvim": {
        "origin": "Japan",
        "price_range": "luxury",
        "aesthetics": ["japanese", "americana", "heritage", "artisanal"],
        "typical_fits": ["relaxed", "oversized"],
        "signature_items": ["FBT moccasins", "Social Sculpture denim", "Skagway sneakers"],
        "products": [
            {"name": "Social Sculpture 101 Jeans", "category": "pants", "fit": "straight", "description": "Premium selvedge denim with unique distressing. Japanese craftsmanship.", "price": 895, "colors": ["indigo"], "materials": ["japanese selvedge"]},
            {"name": "FBT Folk Moccasin", "category": "shoes", "fit": "regular", "description": "Signature moccasin boot. Hand-sewn construction.", "price": 1095, "colors": ["brown", "black"], "materials": ["leather"]},
            {"name": "Jumbo Hoodie", "category": "hoodie", "fit": "oversized", "description": "Heavyweight fleece hoodie. Vintage athletic inspiration.", "price": 645, "colors": ["grey", "navy"], "materials": ["cotton fleece"]},
        ]
    },
    "Needles": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "streetwear", "bohemian", "eclectic"],
        "typical_fits": ["relaxed", "oversized"],
        "signature_items": ["Track pants", "Rebuild flannel", "Papillon bow tie"],
        "products": [
            {"name": "Narrow Track Pant", "category": "pants", "fit": "relaxed", "description": "Side stripe track pants. Signature Needles style.", "price": 395, "colors": ["navy", "black", "purple"], "materials": ["polyester"]},
            {"name": "Rebuild Flannel Shirt", "category": "shirt", "fit": "oversized", "description": "Reconstructed vintage flannel. Unique patchwork.", "price": 445, "colors": ["multi"], "materials": ["cotton flannel"]},
            {"name": "HD Track Jacket", "category": "jacket", "fit": "relaxed", "description": "Classic track jacket with butterfly embroidery.", "price": 345, "colors": ["black", "navy", "green"], "materials": ["polyester"]},
        ]
    },
    "Beams Plus": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "americana", "ivy", "preppy"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Ivy blazers", "Button-down shirts", "Loafers"],
        "products": [
            {"name": "3-Button Ivy Blazer", "category": "jacket", "fit": "regular", "description": "Classic 3-button sack coat. Ivy League inspired.", "price": 495, "colors": ["navy"], "materials": ["wool"]},
            {"name": "Button-Down Oxford Shirt", "category": "shirt", "fit": "regular", "description": "Classic oxford button-down. American ivy style.", "price": 185, "colors": ["white", "blue", "pink"], "materials": ["oxford cotton"]},
            {"name": "Athletic Sweatshirt", "category": "sweater", "fit": "relaxed", "description": "Loopwheel cotton sweatshirt. Vintage athletic.", "price": 295, "colors": ["grey", "navy"], "materials": ["loopwheel cotton"]},
        ]
    },
    "Stan Ray": {
        "origin": "USA",
        "price_range": "budget",
        "aesthetics": ["workwear", "military", "americana"],
        "typical_fits": ["relaxed", "wide"],
        "signature_items": ["Slim fatigue pants", "Taper fatigue", "Painter pants"],
        "products": [
            {"name": "Slim Fit 4 Pocket Fatigue", "category": "pants", "fit": "slim", "description": "Slim version of classic fatigue pants. Budget-friendly.", "price": 89, "colors": ["olive", "khaki"], "materials": ["cotton ripstop"]},
            {"name": "Taper Fit 4 Pocket Fatigue", "category": "pants", "fit": "tapered", "description": "Tapered fatigue pants. Modern cut.", "price": 89, "colors": ["olive", "navy"], "materials": ["cotton twill"]},
            {"name": "OG Painter Pant", "category": "pants", "fit": "relaxed", "description": "Classic painter pants with double knee.", "price": 95, "colors": ["natural", "khaki"], "materials": ["cotton canvas"]},
        ]
    },
    "Outlier": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["techwear", "minimalist", "urban", "technical"],
        "typical_fits": ["slim", "regular"],
        "signature_items": ["Slim Dungarees", "Futureworks", "Ultrafine Merino Tee"],
        "products": [
            {"name": "Slim Dungarees", "category": "pants", "fit": "slim", "description": "4-way stretch technical pants. Water resistant.", "price": 198, "colors": ["black", "charcoal"], "materials": ["strongtwill"]},
            {"name": "Futureworks", "category": "pants", "fit": "regular", "description": "Technical chinos with stretch. Clean design.", "price": 198, "colors": ["black", "charcoal", "navy"], "materials": ["f.cloth"]},
            {"name": "Ultrafine Merino Tee", "category": "t-shirt", "fit": "regular", "description": "17.5 micron merino wool tee. Temperature regulating.", "price": 138, "colors": ["black", "grey", "navy"], "materials": ["ultrafine merino"]},
            {"name": "New Way Shorts", "category": "shorts", "fit": "regular", "description": "Technical swim-to-street shorts.", "price": 135, "colors": ["black", "charcoal"], "materials": ["f.cloth"]},
        ]
    },
    "Private White V.C.": {
        "origin": "UK",
        "price_range": "luxury",
        "aesthetics": ["british", "heritage", "military", "quality"],
        "typical_fits": ["regular", "tailored"],
        "signature_items": ["Ventile jackets", "Bomber jacket", "Archive coats"],
        "products": [
            {"name": "Archive Bomber Jacket", "category": "jacket", "fit": "regular", "description": "Classic British bomber. Made in Manchester.", "price": 695, "colors": ["navy", "black"], "materials": ["ventile cotton"]},
            {"name": "Rainrider Jacket", "category": "jacket", "fit": "regular", "description": "Waterproof ventile jacket. Classic design.", "price": 795, "colors": ["olive", "navy"], "materials": ["ventile cotton"]},
            {"name": "Field Jacket", "category": "jacket", "fit": "regular", "description": "British military field jacket. Heritage construction.", "price": 595, "colors": ["khaki", "olive"], "materials": ["cotton"]},
        ]
    },
    "Drake's": {
        "origin": "UK",
        "price_range": "luxury",
        "aesthetics": ["british", "sartorial", "contemporary", "menswear"],
        "typical_fits": ["regular", "relaxed tailored"],
        "signature_items": ["Silk ties", "Linen shirts", "Easy jackets"],
        "products": [
            {"name": "Easy Jacket", "category": "jacket", "fit": "relaxed", "description": "Unstructured cotton blazer. Effortless tailoring.", "price": 895, "colors": ["navy", "grey"], "materials": ["cotton"]},
            {"name": "Bengali Stripe Shirt", "category": "shirt", "fit": "regular", "description": "Classic British shirting. Roll collar.", "price": 275, "colors": ["blue stripe", "pink stripe"], "materials": ["cotton"]},
            {"name": "Linen Sport Shirt", "category": "shirt", "fit": "relaxed", "description": "Relaxed linen camp shirt. Summer essential.", "price": 295, "colors": ["white", "blue", "ecru"], "materials": ["linen"]},
        ]
    },
    "Paraboot": {
        "origin": "France",
        "price_range": "premium",
        "aesthetics": ["french", "heritage", "quality"],
        "typical_fits": ["regular"],
        "signature_items": ["Michael boot", "Chambord", "Avignon"],
        "products": [
            {"name": "Michael Boot", "category": "shoes", "fit": "regular", "description": "Classic Norwegian welt boot. Made in France.", "price": 525, "colors": ["marron", "noir"], "materials": ["leather"]},
            {"name": "Chambord Shoe", "category": "shoes", "fit": "regular", "description": "Iconic Derby shoe. Norwegian welt construction.", "price": 475, "colors": ["cafe", "noir"], "materials": ["leather"]},
            {"name": "Avignon Loafer", "category": "shoes", "fit": "regular", "description": "Penny loafer with rubber sole.", "price": 445, "colors": ["marron", "noir"], "materials": ["leather"]},
        ]
    },
    "Margaret Howell": {
        "origin": "UK",
        "price_range": "premium",
        "aesthetics": ["british", "minimalist", "relaxed", "quality"],
        "typical_fits": ["relaxed", "oversized"],
        "signature_items": ["Men's shirts", "Cotton trousers", "Linen pieces"],
        "products": [
            {"name": "Classic Cotton Shirt", "category": "shirt", "fit": "relaxed", "description": "Oversized cotton shirt. British minimalism.", "price": 345, "colors": ["white", "blue", "grey"], "materials": ["cotton"]},
            {"name": "Wide Leg Trouser", "category": "pants", "fit": "wide", "description": "High-waisted wide leg pants. Clean design.", "price": 395, "colors": ["navy", "grey", "black"], "materials": ["cotton twill"]},
            {"name": "Linen Blazer", "category": "jacket", "fit": "relaxed", "description": "Unstructured linen jacket. Summer tailoring.", "price": 695, "colors": ["natural", "navy"], "materials": ["linen"]},
        ]
    },
    "Officine Generale": {
        "origin": "France",
        "price_range": "premium",
        "aesthetics": ["french", "contemporary", "relaxed", "quality"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Japanese fabric shirts", "Pleated pants", "Soft tailoring"],
        "products": [
            {"name": "Japanese Oxford Shirt", "category": "shirt", "fit": "regular", "description": "Oxford shirt in Japanese fabric. French quality.", "price": 235, "colors": ["white", "blue"], "materials": ["japanese oxford"]},
            {"name": "Pleated Wool Pants", "category": "pants", "fit": "relaxed tapered", "description": "High-waisted pleated trousers. Italian wool.", "price": 345, "colors": ["grey", "navy", "brown"], "materials": ["wool"]},
            {"name": "Cotton Twill Chore Jacket", "category": "jacket", "fit": "relaxed", "description": "French chore coat. Artisanal construction.", "price": 425, "colors": ["navy", "ecru"], "materials": ["cotton twill"]},
        ]
    },
    "Nanamica": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "outdoor", "technical", "minimalist"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["GORE-TEX pieces", "Down jackets", "Technical fabrics"],
        "products": [
            {"name": "GORE-TEX Cruiser Jacket", "category": "jacket", "fit": "regular", "description": "Waterproof technical jacket. Clean Japanese design.", "price": 695, "colors": ["navy", "black"], "materials": ["gore-tex"]},
            {"name": "Down Cardigan", "category": "jacket", "fit": "regular", "description": "Lightweight packable down. Layering piece.", "price": 395, "colors": ["black", "navy"], "materials": ["nylon", "down"]},
            {"name": "Chino Pants", "category": "pants", "fit": "regular", "description": "Technical chinos with stretch.", "price": 245, "colors": ["khaki", "navy", "grey"], "materials": ["stretch cotton"]},
        ]
    },
    "Albam": {
        "origin": "UK",
        "price_range": "mid",
        "aesthetics": ["british", "workwear", "minimalist"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Chore jackets", "Moleskin trousers", "Basic tees"],
        "products": [
            {"name": "Foundry Chore Coat", "category": "jacket", "fit": "regular", "description": "British workwear chore coat. Three pockets.", "price": 295, "colors": ["navy", "olive"], "materials": ["cotton"]},
            {"name": "Moleskin Trousers", "category": "pants", "fit": "regular", "description": "Brushed cotton trousers. Soft and durable.", "price": 185, "colors": ["navy", "grey", "brown"], "materials": ["moleskin cotton"]},
            {"name": "Pocket Tee", "category": "t-shirt", "fit": "regular", "description": "Heavyweight cotton tee. British made.", "price": 65, "colors": ["white", "black", "grey"], "materials": ["cotton"]},
        ]
    },
    "Monitaly": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["americana", "japanese", "unique", "artisanal"],
        "typical_fits": ["relaxed", "oversized"],
        "signature_items": ["Vancluse coat", "Military-inspired pants", "Unique details"],
        "products": [
            {"name": "Vancluse Coat", "category": "jacket", "fit": "oversized", "description": "Kimono-inspired coat. Japanese-American fusion.", "price": 695, "colors": ["navy", "brown"], "materials": ["cotton canvas"]},
            {"name": "Military Pant", "category": "pants", "fit": "relaxed", "description": "Cargo pants with unique construction.", "price": 325, "colors": ["olive", "khaki"], "materials": ["cotton twill"]},
            {"name": "Reversible Vest", "category": "jacket", "fit": "regular", "description": "Double-faced vest. Versatile layering.", "price": 445, "colors": ["grey", "brown"], "materials": ["wool"]},
        ]
    },
    "YMC": {
        "origin": "UK",
        "price_range": "mid",
        "aesthetics": ["british", "casual", "contemporary"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Schrank jacket", "Alva skate pant", "Casual shirts"],
        "products": [
            {"name": "Schrank Work Jacket", "category": "jacket", "fit": "regular", "description": "Wool blend work jacket. Versatile layering.", "price": 395, "colors": ["navy", "charcoal"], "materials": ["wool blend"]},
            {"name": "Alva Skate Pant", "category": "pants", "fit": "relaxed", "description": "Wide leg cotton pants. Casual comfort.", "price": 195, "colors": ["navy", "black", "olive"], "materials": ["cotton"]},
            {"name": "Dean Shirt", "category": "shirt", "fit": "regular", "description": "Cotton poplin shirt. Clean design.", "price": 165, "colors": ["white", "blue", "pink"], "materials": ["cotton poplin"]},
        ]
    },
    "Folk": {
        "origin": "UK",
        "price_range": "mid",
        "aesthetics": ["british", "minimalist", "contemporary"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Assembly trousers", "Soft collar shirts", "Layering pieces"],
        "products": [
            {"name": "Assembly Trouser", "category": "pants", "fit": "relaxed tapered", "description": "Pleated cotton trousers. Contemporary workwear.", "price": 225, "colors": ["navy", "olive", "black"], "materials": ["cotton twill"]},
            {"name": "Soft Collar Shirt", "category": "shirt", "fit": "regular", "description": "Relaxed collar cotton shirt.", "price": 165, "colors": ["white", "blue", "ecru"], "materials": ["cotton"]},
            {"name": "Boxy Tee", "category": "t-shirt", "fit": "boxy", "description": "Oversized cotton tee. Modern fit.", "price": 85, "colors": ["white", "black", "navy"], "materials": ["cotton"]},
        ]
    },
})

# Even more brands for comprehensive production database
BRAND_DATABASE.update({
    "Rogue Territory": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["americana", "raw denim", "workwear", "heritage"],
        "typical_fits": ["slim", "tapered"],
        "signature_items": ["SK jeans", "Supply jacket", "Workshirts"],
        "products": [
            {"name": "Stanton Jeans", "category": "pants", "fit": "slim straight", "description": "Slim straight raw selvedge. 14.5oz Nihon Menpu denim.", "price": 265, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "SK Jeans", "category": "pants", "fit": "slim tapered", "description": "Slim tapered fit. Japanese selvedge denim.", "price": 265, "colors": ["indigo", "black"], "materials": ["selvedge denim"]},
            {"name": "Supply Jacket", "category": "jacket", "fit": "regular", "description": "Canvas chore jacket. Made in Los Angeles.", "price": 295, "colors": ["navy", "copper"], "materials": ["canvas"]},
            {"name": "Jumper Shirt", "category": "shirt", "fit": "regular", "description": "Heavyweight work shirt. Triple needle construction.", "price": 225, "colors": ["indigo", "olive"], "materials": ["cotton"]},
            {"name": "Stealth Pocket Tee", "category": "t-shirt", "fit": "regular", "description": "USA-made heavyweight tee.", "price": 55, "colors": ["white", "black", "grey"], "materials": ["cotton"]},
        ]
    },
    "Pure Blue Japan": {
        "origin": "Japan",
        "price_range": "luxury",
        "aesthetics": ["japanese", "raw denim", "indigo", "artisanal"],
        "typical_fits": ["slim", "relaxed tapered"],
        "signature_items": ["Indigo-dyed items", "Sashiko", "Heavyweight denim"],
        "products": [
            {"name": "XX-019 Relaxed Tapered Jeans", "category": "pants", "fit": "relaxed tapered", "description": "18oz slubby denim. Deep indigo dyeing process.", "price": 395, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "XX-013 Slim Tapered", "category": "pants", "fit": "slim tapered", "description": "14oz denim. Classic PBJ texture.", "price": 345, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "Indigo Sashiko Shirt", "category": "shirt", "fit": "regular", "description": "Hand-dyed indigo with sashiko stitching.", "price": 295, "colors": ["indigo"], "materials": ["cotton sashiko"]},
            {"name": "Indigo Hoodie", "category": "hoodie", "fit": "regular", "description": "Rope-dyed indigo fleece.", "price": 345, "colors": ["indigo"], "materials": ["cotton fleece"]},
        ]
    },
    "Gramicci": {
        "origin": "USA/Japan",
        "price_range": "mid",
        "aesthetics": ["outdoor", "climbing", "casual", "japanese"],
        "typical_fits": ["relaxed", "wide"],
        "signature_items": ["G-Pants", "Climbing pants", "Running Man logo"],
        "products": [
            {"name": "Original G-Pant", "category": "pants", "fit": "relaxed", "description": "Signature climbing pants. Gusseted crotch, webbing belt.", "price": 98, "colors": ["stone", "olive", "black"], "materials": ["cotton twill"]},
            {"name": "NN-Pant", "category": "pants", "fit": "tapered", "description": "Modern tapered version. Stretch fabric.", "price": 118, "colors": ["black", "navy", "olive"], "materials": ["stretch cotton"]},
            {"name": "Shell Gear Shorts", "category": "shorts", "fit": "relaxed", "description": "Nylon climbing shorts. Packable.", "price": 88, "colors": ["black", "olive", "navy"], "materials": ["nylon"]},
            {"name": "One Point Tee", "category": "t-shirt", "fit": "regular", "description": "Classic tee with Running Man logo.", "price": 45, "colors": ["white", "black", "grey"], "materials": ["cotton"]},
        ]
    },
    "Snow Peak": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "outdoor", "technical", "camping"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Takibi series", "Camping gear", "Technical fabrics"],
        "products": [
            {"name": "Takibi Coveralls", "category": "pants", "fit": "relaxed", "description": "Fire-resistant cotton coveralls. Campfire wear.", "price": 425, "colors": ["olive", "black"], "materials": ["fire-resistant cotton"]},
            {"name": "Flexible Insulated Jacket", "category": "jacket", "fit": "regular", "description": "Packable insulated jacket. Technical outdoor.", "price": 495, "colors": ["black", "olive"], "materials": ["nylon", "insulation"]},
            {"name": "DWR Light Pants", "category": "pants", "fit": "regular", "description": "Water-repellent technical pants.", "price": 245, "colors": ["grey", "black", "olive"], "materials": ["technical cotton"]},
            {"name": "Flexible Insulated Vest", "category": "jacket", "fit": "regular", "description": "Lightweight down vest. Layering essential.", "price": 295, "colors": ["black", "navy"], "materials": ["nylon", "down"]},
        ]
    },
    "C.P. Company": {
        "origin": "Italy",
        "price_range": "premium",
        "aesthetics": ["italian", "technical", "experimental", "streetwear"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Goggle jacket", "Lens detail", "Garment dyeing"],
        "products": [
            {"name": "Goggle Shell Jacket", "category": "jacket", "fit": "regular", "description": "Iconic goggle hood jacket. Technical fabric.", "price": 695, "colors": ["black", "olive", "navy"], "materials": ["nylon shell"]},
            {"name": "Lens Crewneck", "category": "sweater", "fit": "regular", "description": "Cotton fleece with signature lens detail.", "price": 345, "colors": ["black", "navy", "grey"], "materials": ["cotton fleece"]},
            {"name": "Garment Dyed Cargo Pants", "category": "pants", "fit": "regular", "description": "Cargo pants with lens pocket detail.", "price": 395, "colors": ["black", "olive", "grey"], "materials": ["cotton"]},
            {"name": "Diagonal Fleece Zip Hoodie", "category": "hoodie", "fit": "regular", "description": "Diagonal raised fleece with lens detail.", "price": 395, "colors": ["black", "grey", "navy"], "materials": ["cotton fleece"]},
        ]
    },
    "Sunspel": {
        "origin": "UK",
        "price_range": "premium",
        "aesthetics": ["british", "quality", "heritage", "basics"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Sea Island Cotton", "Riviera Polo", "Q Branch tee"],
        "products": [
            {"name": "Riviera Polo", "category": "shirt", "fit": "regular", "description": "Mesh cotton polo. As worn by James Bond.", "price": 155, "colors": ["white", "navy", "grey"], "materials": ["mesh cotton"]},
            {"name": "Long Sleeve Crew Neck Tee", "category": "t-shirt", "fit": "regular", "description": "Superfine cotton long sleeve.", "price": 115, "colors": ["white", "black", "grey"], "materials": ["superfine cotton"]},
            {"name": "Loopback Cotton Hoodie", "category": "hoodie", "fit": "regular", "description": "Heavyweight loopback cotton.", "price": 235, "colors": ["grey melange", "navy"], "materials": ["loopback cotton"]},
            {"name": "Classic Boxer", "category": "accessories", "fit": "regular", "description": "Sea Island cotton boxers.", "price": 65, "colors": ["white", "navy"], "materials": ["sea island cotton"]},
        ]
    },
    "Universal Works": {
        "origin": "UK",
        "price_range": "mid",
        "aesthetics": ["british", "workwear", "casual", "comfortable"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Bakers jacket", "Pleated trousers", "Camp collar shirts"],
        "products": [
            {"name": "Bakers Jacket", "category": "jacket", "fit": "regular", "description": "Three-button work jacket. British chore coat.", "price": 295, "colors": ["navy", "olive", "sand"], "materials": ["cotton twill"]},
            {"name": "Pleated Track Pant", "category": "pants", "fit": "wide pleated", "description": "Wide leg pleated trousers.", "price": 185, "colors": ["navy", "black", "olive"], "materials": ["cotton twill"]},
            {"name": "Road Shirt", "category": "shirt", "fit": "relaxed", "description": "Relaxed camp collar shirt.", "price": 165, "colors": ["ecru", "navy", "olive"], "materials": ["cotton"]},
            {"name": "Vince Jacket", "category": "jacket", "fit": "regular", "description": "Clean zip-front jacket.", "price": 325, "colors": ["navy", "black"], "materials": ["cotton blend"]},
        ]
    },
    "Aime Leon Dore": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["streetwear", "new york", "preppy", "contemporary"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Logo pieces", "New Balance collabs", "Queens aesthetic"],
        "products": [
            {"name": "Logo Hoodie", "category": "hoodie", "fit": "relaxed", "description": "Heavyweight fleece with embroidered logo.", "price": 195, "colors": ["grey", "navy", "cream"], "materials": ["cotton fleece"]},
            {"name": "Uniform Pant", "category": "pants", "fit": "regular", "description": "Slightly tapered chino. Clean design.", "price": 185, "colors": ["khaki", "navy", "black"], "materials": ["cotton twill"]},
            {"name": "Sailing Jacket", "category": "jacket", "fit": "regular", "description": "Lightweight nylon pullover. Nautical influence.", "price": 295, "colors": ["navy", "cream"], "materials": ["nylon"]},
            {"name": "Knit Cardigan", "category": "sweater", "fit": "relaxed", "description": "Chunky knit cardigan with logo.", "price": 345, "colors": ["navy", "cream", "brown"], "materials": ["wool blend"]},
        ]
    },
    "Noah": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["streetwear", "new york", "punk", "sustainability"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Core Logo pieces", "Corduroy items", "Sustainable materials"],
        "products": [
            {"name": "Core Logo Hoodie", "category": "hoodie", "fit": "regular", "description": "Heavyweight hoodie with Noah cross logo.", "price": 168, "colors": ["black", "grey", "navy"], "materials": ["organic cotton"]},
            {"name": "Corduroy Pant", "category": "pants", "fit": "relaxed", "description": "Wide wale corduroy trousers.", "price": 198, "colors": ["burgundy", "brown", "navy"], "materials": ["corduroy"]},
            {"name": "Zip Cardigan", "category": "sweater", "fit": "regular", "description": "Wool zip cardigan. Classic styling.", "price": 348, "colors": ["navy", "black", "grey"], "materials": ["wool"]},
            {"name": "Core Logo Tee", "category": "t-shirt", "fit": "regular", "description": "Organic cotton tee with embroidered logo.", "price": 68, "colors": ["white", "black", "navy"], "materials": ["organic cotton"]},
        ]
    },
    "Knickerbocker": {
        "origin": "USA",
        "price_range": "mid",
        "aesthetics": ["americana", "heritage", "athletic", "made in usa"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Gym clothes", "Heavyweight tees", "Athletic wear"],
        "products": [
            {"name": "Heavyweight Pocket Tee", "category": "t-shirt", "fit": "regular", "description": "USA-made heavyweight cotton.", "price": 68, "colors": ["white", "navy", "grey"], "materials": ["heavyweight cotton"]},
            {"name": "Gym Hoodie", "category": "hoodie", "fit": "relaxed", "description": "Vintage athletic heavyweight fleece.", "price": 198, "colors": ["grey", "navy", "green"], "materials": ["heavyweight fleece"]},
            {"name": "Camp Collar Shirt", "category": "shirt", "fit": "relaxed", "description": "Relaxed cotton camp shirt.", "price": 148, "colors": ["cream", "navy", "olive"], "materials": ["cotton"]},
            {"name": "Varsity Jacket", "category": "jacket", "fit": "regular", "description": "Classic wool varsity jacket.", "price": 395, "colors": ["navy", "burgundy"], "materials": ["wool", "leather"]},
        ]
    },
    "Corridor": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["sustainable", "artisanal", "natural dye", "new york"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Natural dyed pieces", "Hand-drawn prints", "Camp shirts"],
        "products": [
            {"name": "Natural Dye Camp Shirt", "category": "shirt", "fit": "relaxed", "description": "Camp collar shirt dyed with natural indigo.", "price": 195, "colors": ["indigo", "earth"], "materials": ["natural dyed cotton"]},
            {"name": "Hand Knit Sweater", "category": "sweater", "fit": "relaxed", "description": "Hand-knitted alpaca blend.", "price": 395, "colors": ["cream", "brown"], "materials": ["alpaca wool blend"]},
            {"name": "Floral Camp Shirt", "category": "shirt", "fit": "relaxed", "description": "Hand-drawn floral print.", "price": 185, "colors": ["floral multi"], "materials": ["cotton"]},
            {"name": "Corduroy Trouser", "category": "pants", "fit": "relaxed", "description": "Wide wale corduroy pants.", "price": 225, "colors": ["brown", "navy", "olive"], "materials": ["corduroy"]},
        ]
    },
    "Lady White Co": {
        "origin": "USA",
        "price_range": "mid",
        "aesthetics": ["basics", "made in usa", "quality", "minimalist"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["T-shirts", "Sweatshirts", "Basic essentials"],
        "products": [
            {"name": "Lite Jersey T-Shirt", "category": "t-shirt", "fit": "regular", "description": "Mid-weight cotton tee. Made in Los Angeles.", "price": 58, "colors": ["white", "black", "grey", "navy"], "materials": ["cotton jersey"]},
            {"name": "Super Weighted Sweatshirt", "category": "sweater", "fit": "relaxed", "description": "Heavy 16oz fleece crewneck.", "price": 195, "colors": ["heather grey", "black", "navy"], "materials": ["heavyweight fleece"]},
            {"name": "Sport Trouser", "category": "pants", "fit": "relaxed", "description": "Elastic waist cotton pants.", "price": 165, "colors": ["black", "navy", "olive"], "materials": ["cotton twill"]},
            {"name": "Balta Pocket Tee", "category": "t-shirt", "fit": "regular", "description": "Pocket tee in loopwheel cotton.", "price": 78, "colors": ["white", "black", "grey"], "materials": ["loopwheel cotton"]},
        ]
    },
    "Gitman Vintage": {
        "origin": "USA",
        "price_range": "mid",
        "aesthetics": ["americana", "classic", "heritage", "shirts"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Oxford shirts", "Camp collar prints", "Made in USA"],
        "products": [
            {"name": "Oxford Button Down", "category": "shirt", "fit": "regular", "description": "Classic oxford cloth button-down. Made in Pennsylvania.", "price": 195, "colors": ["white", "blue", "pink"], "materials": ["oxford cloth"]},
            {"name": "Camp Collar Print Shirt", "category": "shirt", "fit": "relaxed", "description": "Bold printed camp collar.", "price": 225, "colors": ["floral", "tropical"], "materials": ["cotton"]},
            {"name": "Flannel Workshirt", "category": "shirt", "fit": "regular", "description": "Heavy cotton flannel.", "price": 215, "colors": ["buffalo plaid", "windowpane"], "materials": ["cotton flannel"]},
            {"name": "Chambray Shirt", "category": "shirt", "fit": "regular", "description": "Selvedge chambray button-down.", "price": 205, "colors": ["chambray blue"], "materials": ["selvedge chambray"]},
        ]
    },
    "Taylor Stitch": {
        "origin": "USA",
        "price_range": "mid",
        "aesthetics": ["sustainable", "americana", "responsible", "heritage"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Democratic products", "Organic materials", "Crowdfunded items"],
        "products": [
            {"name": "Democratic Jean", "category": "pants", "fit": "straight", "description": "Organic selvedge denim. Responsibly made.", "price": 198, "colors": ["indigo"], "materials": ["organic selvedge denim"]},
            {"name": "Long Haul Jacket", "category": "jacket", "fit": "regular", "description": "Organic denim trucker jacket.", "price": 248, "colors": ["indigo", "black"], "materials": ["organic denim"]},
            {"name": "Heavy Bag Tee", "category": "t-shirt", "fit": "regular", "description": "Heavyweight tee from recycled materials.", "price": 58, "colors": ["white", "grey", "navy"], "materials": ["recycled cotton"]},
            {"name": "Jack Shirt", "category": "shirt", "fit": "regular", "description": "Everyday oxford button-down.", "price": 128, "colors": ["white", "blue", "grey"], "materials": ["organic cotton"]},
        ]
    },
    "Portuguese Flannel": {
        "origin": "Portugal",
        "price_range": "mid",
        "aesthetics": ["european", "quality", "casual", "relaxed"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Flannel shirts", "Linen shirts", "Portuguese craftsmanship"],
        "products": [
            {"name": "Teca Flannel Shirt", "category": "shirt", "fit": "relaxed", "description": "Heavyweight Portuguese flannel.", "price": 175, "colors": ["grey check", "blue check", "red check"], "materials": ["portuguese flannel"]},
            {"name": "Labura Overshirt", "category": "shirt", "fit": "relaxed", "description": "Cotton twill overshirt.", "price": 195, "colors": ["navy", "olive", "stone"], "materials": ["cotton twill"]},
            {"name": "Linen Camp Shirt", "category": "shirt", "fit": "relaxed", "description": "Relaxed linen camp collar.", "price": 145, "colors": ["white", "light blue", "sage"], "materials": ["linen"]},
            {"name": "Belavista Overshirt", "category": "shirt", "fit": "relaxed", "description": "Wool blend overshirt.", "price": 225, "colors": ["navy", "grey", "brown"], "materials": ["wool blend"]},
        ]
    },
    "MHL by Margaret Howell": {
        "origin": "UK",
        "price_range": "mid",
        "aesthetics": ["british", "workwear", "utilitarian", "minimalist"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Workwear basics", "Utilitarian design", "Quality fabrics"],
        "products": [
            {"name": "Gym Tee", "category": "t-shirt", "fit": "regular", "description": "Japanese cotton tee. Utilitarian design.", "price": 95, "colors": ["white", "navy", "black"], "materials": ["japanese cotton"]},
            {"name": "Painters Trouser", "category": "pants", "fit": "relaxed", "description": "Wide leg cotton trousers.", "price": 295, "colors": ["natural", "navy"], "materials": ["cotton drill"]},
            {"name": "Work Jacket", "category": "jacket", "fit": "regular", "description": "Dry wax cotton jacket.", "price": 495, "colors": ["navy", "olive"], "materials": ["wax cotton"]},
            {"name": "Basic Shirt", "category": "shirt", "fit": "regular", "description": "Cotton poplin button-down.", "price": 195, "colors": ["white", "blue"], "materials": ["cotton poplin"]},
        ]
    },
    "And Wander": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "outdoor", "technical", "hiking"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Technical outdoor wear", "Hiking gear", "Japanese design"],
        "products": [
            {"name": "Light Rain Jacket", "category": "jacket", "fit": "regular", "description": "Ultralight waterproof shell. 3-layer construction.", "price": 495, "colors": ["black", "khaki", "navy"], "materials": ["pertex"]},
            {"name": "Trek Pants", "category": "pants", "fit": "tapered", "description": "Stretch hiking pants. Technical fabric.", "price": 295, "colors": ["black", "khaki", "grey"], "materials": ["technical stretch"]},
            {"name": "Seamless Base Layer", "category": "t-shirt", "fit": "slim", "description": "Merino wool base layer.", "price": 145, "colors": ["black", "grey"], "materials": ["merino wool"]},
            {"name": "20L Daypack", "category": "accessories", "fit": "one size", "description": "Technical hiking backpack.", "price": 295, "colors": ["black", "khaki"], "materials": ["cordura nylon"]},
        ]
    },
    "Battenwear": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["americana", "outdoor", "surf", "vintage"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Beach Breaker jacket", "Board shorts", "Vintage outdoor"],
        "products": [
            {"name": "Beach Breaker Jacket", "category": "jacket", "fit": "regular", "description": "Nylon pullover. Vintage surf inspiration.", "price": 345, "colors": ["navy", "orange", "green"], "materials": ["nylon"]},
            {"name": "Active Lazy Pants", "category": "pants", "fit": "relaxed", "description": "Relaxed cotton pants. Casual comfort.", "price": 195, "colors": ["navy", "olive", "tan"], "materials": ["cotton"]},
            {"name": "Pocket Tee", "category": "t-shirt", "fit": "regular", "description": "Heavyweight USA-made tee.", "price": 65, "colors": ["white", "grey", "navy"], "materials": ["cotton"]},
            {"name": "Travel Shell Parka", "category": "jacket", "fit": "regular", "description": "Packable nylon parka.", "price": 395, "colors": ["navy", "tan"], "materials": ["nylon"]},
        ]
    },
    "Kestin": {
        "origin": "Scotland",
        "price_range": "mid",
        "aesthetics": ["british", "scottish", "contemporary", "heritage"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Harris Tweed pieces", "Scottish wool", "Contemporary design"],
        "products": [
            {"name": "Armadale Shirt Jacket", "category": "jacket", "fit": "relaxed", "description": "Harris Tweed overshirt. Scottish made.", "price": 395, "colors": ["charcoal", "brown"], "materials": ["harris tweed"]},
            {"name": "Inverness Trouser", "category": "pants", "fit": "wide pleated", "description": "Wide leg pleated trousers.", "price": 285, "colors": ["navy", "charcoal", "olive"], "materials": ["wool blend"]},
            {"name": "Neist Overshirt", "category": "shirt", "fit": "relaxed", "description": "Organic cotton overshirt.", "price": 245, "colors": ["navy", "olive", "tan"], "materials": ["organic cotton"]},
            {"name": "Lomond Sweatshirt", "category": "sweater", "fit": "regular", "description": "Loopback cotton crewneck.", "price": 145, "colors": ["grey", "navy"], "materials": ["loopback cotton"]},
        ]
    },
    "Howlin'": {
        "origin": "Scotland",
        "price_range": "mid",
        "aesthetics": ["scottish", "knitwear", "vintage", "cozy"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Scottish wool knitwear", "Birth of the Cool cardigan", "Textured knits"],
        "products": [
            {"name": "Birth of the Cool Cardigan", "category": "sweater", "fit": "regular", "description": "Chunky wool cardigan. Made in Scotland.", "price": 345, "colors": ["navy", "burgundy", "grey"], "materials": ["scottish wool"]},
            {"name": "Shaggy Bear Sweater", "category": "sweater", "fit": "regular", "description": "Brushed wool sweater. Fuzzy texture.", "price": 295, "colors": ["cream", "moss", "navy"], "materials": ["brushed wool"]},
            {"name": "Terry Crew", "category": "sweater", "fit": "regular", "description": "Cotton terry crewneck.", "price": 195, "colors": ["grey", "navy", "green"], "materials": ["cotton terry"]},
            {"name": "Flying Teapot Beanie", "category": "accessories", "fit": "one size", "description": "Ribbed wool beanie.", "price": 85, "colors": ["navy", "grey", "burgundy"], "materials": ["scottish wool"]},
        ]
    },

    # === ADDITIONAL BRANDS - EXPANSION BATCH 2 ===

    # Premium Japanese Brands
    "Yaeca": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "minimalist", "clean", "functional"],
        "typical_fits": ["relaxed", "straight"],
        "signature_items": ["Chino cloth pants", "Button shirts", "Comfort basics"],
        "products": [
            {"name": "Chino Cloth Pants", "category": "pants", "fit": "straight", "description": "Simple straight leg chinos. Japanese cotton.", "price": 245, "colors": ["navy", "beige", "olive"], "materials": ["cotton chino"]},
            {"name": "Comfort Shirt", "category": "shirt", "fit": "relaxed", "description": "Relaxed button-down with soft hand.", "price": 225, "colors": ["white", "light blue", "grey"], "materials": ["cotton"]},
            {"name": "2-Way Jacket", "category": "jacket", "fit": "relaxed", "description": "Reversible lightweight jacket.", "price": 395, "colors": ["navy/grey", "olive/khaki"], "materials": ["nylon", "cotton"]},
            {"name": "Mock Neck Tee", "category": "t-shirt", "fit": "regular", "description": "Simple mock neck in Japanese cotton.", "price": 95, "colors": ["white", "black", "grey"], "materials": ["cotton jersey"]},
        ]
    },
    "Comoli": {
        "origin": "Japan",
        "price_range": "luxury",
        "aesthetics": ["japanese", "relaxed", "comfort", "refined casual"],
        "typical_fits": ["oversized", "relaxed", "wide"],
        "signature_items": ["Oversized shirts", "Wide pants", "Relaxed tailoring"],
        "products": [
            {"name": "Band Collar Shirt", "category": "shirt", "fit": "oversized", "description": "Ultra-relaxed band collar shirt. High quality cotton.", "price": 385, "colors": ["white", "navy", "ecru"], "materials": ["cotton"]},
            {"name": "Belted Denim Pants", "category": "pants", "fit": "wide", "description": "Wide straight denim with belt. Relaxed luxury.", "price": 445, "colors": ["indigo", "black"], "materials": ["denim"]},
            {"name": "Cotton Silk Cardigan", "category": "sweater", "fit": "oversized", "description": "Lightweight cotton-silk blend cardigan.", "price": 495, "colors": ["grey", "navy", "cream"], "materials": ["cotton", "silk"]},
            {"name": "Oversized Tee", "category": "t-shirt", "fit": "oversized", "description": "Boxy oversized cotton tee.", "price": 145, "colors": ["white", "black", "grey"], "materials": ["cotton"]},
            {"name": "Wide Chinos", "category": "pants", "fit": "wide", "description": "High-rise wide leg chinos.", "price": 385, "colors": ["khaki", "navy", "olive"], "materials": ["cotton twill"]},
        ]
    },
    "Auralee": {
        "origin": "Japan",
        "price_range": "luxury",
        "aesthetics": ["japanese", "minimal", "technical", "refined"],
        "typical_fits": ["relaxed", "oversized"],
        "signature_items": ["Technical fabrics", "Understated luxury", "Material innovation"],
        "products": [
            {"name": "Super Light Wool Shirt", "category": "shirt", "fit": "relaxed", "description": "Ultra-fine wool shirt. Incredibly lightweight.", "price": 495, "colors": ["grey", "navy", "black"], "materials": ["super 140s wool"]},
            {"name": "Washed Finx Chino", "category": "pants", "fit": "wide", "description": "Soft washed cotton pants. Wide leg.", "price": 385, "colors": ["beige", "navy", "olive"], "materials": ["finx cotton"]},
            {"name": "Light Melton Duffle", "category": "jacket", "fit": "oversized", "description": "Lightweight wool duffle coat.", "price": 895, "colors": ["grey", "navy", "camel"], "materials": ["light melton wool"]},
            {"name": "Hard Twist Denim", "category": "pants", "fit": "straight", "description": "Dense hard twist cotton denim.", "price": 425, "colors": ["indigo"], "materials": ["hard twist denim"]},
            {"name": "Cashmere Knit", "category": "sweater", "fit": "relaxed", "description": "Ultra-soft cashmere crewneck.", "price": 595, "colors": ["grey", "navy", "cream"], "materials": ["cashmere"]},
        ]
    },
    "Needles": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "eclectic", "vintage", "bohemian"],
        "typical_fits": ["relaxed", "slim", "wide"],
        "signature_items": ["Track pants", "Rebuild pieces", "Butterfly embroidery"],
        "products": [
            {"name": "Narrow Track Pant", "category": "pants", "fit": "slim", "description": "Signature track pants with side stripe.", "price": 285, "colors": ["purple", "navy", "black"], "materials": ["poly smooth"]},
            {"name": "Rebuild Flannel", "category": "shirt", "fit": "relaxed", "description": "Reconstructed from vintage flannels.", "price": 495, "colors": ["multi check"], "materials": ["vintage flannel"]},
            {"name": "HD Pant", "category": "pants", "fit": "wide", "description": "Wide pleated pants. Butterfly embroidery.", "price": 345, "colors": ["navy", "black", "brown"], "materials": ["cotton twill"]},
            {"name": "Cabana Shirt", "category": "shirt", "fit": "relaxed", "description": "Relaxed camp collar shirt.", "price": 345, "colors": ["paisley", "leopard"], "materials": ["rayon"]},
            {"name": "Mohair Cardigan", "category": "sweater", "fit": "oversized", "description": "Shaggy mohair cardigan.", "price": 595, "colors": ["purple", "brown", "green"], "materials": ["mohair wool"]},
        ]
    },

    # European Contemporary
    "AMI Paris": {
        "origin": "France",
        "price_range": "premium",
        "aesthetics": ["french", "contemporary", "casual luxury", "parisian"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["De Coeur pieces", "Oversized shirts", "French casual"],
        "products": [
            {"name": "De Coeur Hoodie", "category": "hoodie", "fit": "relaxed", "description": "Heavyweight hoodie with heart logo.", "price": 395, "colors": ["black", "navy", "grey"], "materials": ["cotton fleece"]},
            {"name": "Oversized Shirt", "category": "shirt", "fit": "oversized", "description": "Relaxed cotton shirt. French elegance.", "price": 295, "colors": ["white", "light blue", "navy"], "materials": ["cotton poplin"]},
            {"name": "Carrot Fit Jeans", "category": "pants", "fit": "tapered", "description": "Tapered jeans with dropped crotch.", "price": 285, "colors": ["indigo", "black"], "materials": ["denim"]},
            {"name": "Wool Peacoat", "category": "jacket", "fit": "regular", "description": "Classic peacoat with modern proportions.", "price": 695, "colors": ["navy", "camel"], "materials": ["wool blend"]},
            {"name": "De Coeur Tee", "category": "t-shirt", "fit": "regular", "description": "Organic cotton tee with embroidered heart.", "price": 125, "colors": ["white", "black", "navy"], "materials": ["organic cotton"]},
        ]
    },
    "Sandro": {
        "origin": "France",
        "price_range": "premium",
        "aesthetics": ["french", "parisian", "rock chic", "refined"],
        "typical_fits": ["slim", "regular"],
        "signature_items": ["Rock-inspired pieces", "Leather jackets", "Slim tailoring"],
        "products": [
            {"name": "Leather Biker Jacket", "category": "jacket", "fit": "slim", "description": "Lambskin biker jacket. Rock chic.", "price": 895, "colors": ["black"], "materials": ["lambskin leather"]},
            {"name": "Slim Fit Shirt", "category": "shirt", "fit": "slim", "description": "Cotton shirt with slight stretch.", "price": 195, "colors": ["white", "navy", "black"], "materials": ["cotton stretch"]},
            {"name": "Slim Jeans", "category": "pants", "fit": "slim", "description": "Slim fit stretch denim.", "price": 225, "colors": ["indigo", "black", "grey"], "materials": ["stretch denim"]},
            {"name": "Wool Blazer", "category": "jacket", "fit": "slim", "description": "Fitted wool blazer.", "price": 595, "colors": ["navy", "charcoal"], "materials": ["virgin wool"]},
        ]
    },
    "Officine Generale": {
        "origin": "France",
        "price_range": "premium",
        "aesthetics": ["french", "effortless", "elevated basics", "parisian"],
        "typical_fits": ["relaxed", "straight"],
        "signature_items": ["Japanese fabrics", "Refined basics", "Quality cottons"],
        "products": [
            {"name": "Eren Shirt", "category": "shirt", "fit": "straight", "description": "Japanese cotton twill shirt.", "price": 245, "colors": ["white", "sky blue", "navy"], "materials": ["japanese cotton"]},
            {"name": "Hugo Trouser", "category": "pants", "fit": "straight", "description": "Straight leg cotton trousers.", "price": 295, "colors": ["navy", "khaki", "charcoal"], "materials": ["cotton twill"]},
            {"name": "Jules Jacket", "category": "jacket", "fit": "relaxed", "description": "Unstructured blazer. Italian wool.", "price": 595, "colors": ["navy", "grey"], "materials": ["italian wool"]},
            {"name": "Stan Pant", "category": "pants", "fit": "tapered", "description": "Pleated tapered chinos.", "price": 265, "colors": ["olive", "navy", "camel"], "materials": ["cotton"]},
            {"name": "Japanese Selvedge Jean", "category": "pants", "fit": "straight", "description": "Raw selvedge from Japanese mills.", "price": 295, "colors": ["indigo"], "materials": ["japanese selvedge"]},
        ]
    },

    # British Heritage Updated
    "Drake's": {
        "origin": "England",
        "price_range": "luxury",
        "aesthetics": ["british", "heritage", "ivy", "sartorial"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Silk ties", "Shetland sweaters", "British tailoring"],
        "products": [
            {"name": "Shetland Crewneck", "category": "sweater", "fit": "regular", "description": "Scottish Shetland wool sweater.", "price": 295, "colors": ["navy", "grey", "burgundy", "green"], "materials": ["shetland wool"]},
            {"name": "Oxford Button Down", "category": "shirt", "fit": "regular", "description": "Classic oxford cloth BD shirt.", "price": 245, "colors": ["white", "blue", "pink", "ecru"], "materials": ["oxford cotton"]},
            {"name": "Linen Camp Shirt", "category": "shirt", "fit": "relaxed", "description": "Italian linen camp collar.", "price": 295, "colors": ["white", "navy", "green"], "materials": ["linen"]},
            {"name": "Work Trouser", "category": "pants", "fit": "relaxed", "description": "High-waisted work trousers.", "price": 345, "colors": ["navy", "olive", "brown"], "materials": ["cotton drill"]},
            {"name": "Harrington Jacket", "category": "jacket", "fit": "regular", "description": "Cotton harrington with check lining.", "price": 495, "colors": ["navy", "tan", "olive"], "materials": ["cotton"]},
        ]
    },
    "Oliver Spencer": {
        "origin": "England",
        "price_range": "premium",
        "aesthetics": ["british", "contemporary", "bohemian", "refined"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Jersey jackets", "Relaxed tailoring", "East London aesthetic"],
        "products": [
            {"name": "Solms Jacket", "category": "jacket", "fit": "relaxed", "description": "Unstructured jersey blazer.", "price": 445, "colors": ["navy", "charcoal", "brown"], "materials": ["cotton jersey"]},
            {"name": "Drawstring Trouser", "category": "pants", "fit": "relaxed", "description": "Relaxed drawstring pants.", "price": 295, "colors": ["navy", "khaki", "grey"], "materials": ["cotton"]},
            {"name": "Grandad Shirt", "category": "shirt", "fit": "regular", "description": "Collarless cotton shirt.", "price": 195, "colors": ["white", "blue stripe", "grey"], "materials": ["cotton"]},
            {"name": "Fishtail Parka", "category": "jacket", "fit": "oversized", "description": "Classic fishtail parka. Updated.", "price": 595, "colors": ["olive", "navy"], "materials": ["cotton nylon"]},
            {"name": "Lambswool Crew", "category": "sweater", "fit": "regular", "description": "Scottish lambswool sweater.", "price": 225, "colors": ["navy", "grey", "burgundy"], "materials": ["lambswool"]},
        ]
    },

    # Italian Excellence
    "Brunello Cucinelli": {
        "origin": "Italy",
        "price_range": "luxury",
        "aesthetics": ["italian", "luxury", "cashmere", "quiet luxury"],
        "typical_fits": ["relaxed", "regular"],
        "signature_items": ["Cashmere knits", "Quiet luxury", "Solomeo craftsmanship"],
        "products": [
            {"name": "Cashmere Crewneck", "category": "sweater", "fit": "regular", "description": "Ultra-fine cashmere sweater.", "price": 1295, "colors": ["grey", "navy", "camel", "cream"], "materials": ["cashmere"]},
            {"name": "Linen Shirt", "category": "shirt", "fit": "relaxed", "description": "Italian linen shirt. Relaxed elegance.", "price": 595, "colors": ["white", "light blue", "beige"], "materials": ["italian linen"]},
            {"name": "Cotton Chinos", "category": "pants", "fit": "straight", "description": "Garment-dyed cotton chinos.", "price": 645, "colors": ["navy", "khaki", "stone"], "materials": ["cotton gabardine"]},
            {"name": "Cashmere Hoodie", "category": "hoodie", "fit": "relaxed", "description": "Cashmere blend zip hoodie.", "price": 1895, "colors": ["grey", "navy"], "materials": ["cashmere cotton"]},
            {"name": "Suede Bomber", "category": "jacket", "fit": "regular", "description": "Lightweight suede bomber.", "price": 3995, "colors": ["tan", "grey"], "materials": ["suede"]},
        ]
    },
    "Boglioli": {
        "origin": "Italy",
        "price_range": "luxury",
        "aesthetics": ["italian", "unstructured", "modern tailoring", "deconstructed"],
        "typical_fits": ["relaxed", "slim"],
        "signature_items": ["Unstructured blazers", "K Jacket", "Garment-dyed tailoring"],
        "products": [
            {"name": "K Jacket", "category": "jacket", "fit": "relaxed", "description": "Signature unstructured blazer. Ultra-light.", "price": 895, "colors": ["navy", "grey", "tan"], "materials": ["cotton linen"]},
            {"name": "Garment Dyed Suit", "category": "jacket", "fit": "relaxed", "description": "Softly constructed suit jacket.", "price": 1295, "colors": ["navy", "charcoal", "tobacco"], "materials": ["wool cotton"]},
            {"name": "Dover Trouser", "category": "pants", "fit": "slim tapered", "description": "Tapered cotton trousers.", "price": 345, "colors": ["navy", "beige", "grey"], "materials": ["cotton"]},
            {"name": "Knit Polo", "category": "shirt", "fit": "regular", "description": "Fine knit cotton polo.", "price": 295, "colors": ["navy", "white", "light blue"], "materials": ["cotton knit"]},
        ]
    },

    # American Outdoor/Technical
    "Patagonia": {
        "origin": "USA",
        "price_range": "mid",
        "aesthetics": ["outdoor", "sustainable", "functional", "california"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Fleece jackets", "Baggies", "Environmental activism"],
        "products": [
            {"name": "Better Sweater", "category": "jacket", "fit": "regular", "description": "Knit fleece jacket. Recycled polyester.", "price": 139, "colors": ["grey", "navy", "tan"], "materials": ["recycled polyester fleece"]},
            {"name": "Baggies Shorts", "category": "shorts", "fit": "relaxed", "description": "Quick-dry nylon shorts. 5\" inseam.", "price": 65, "colors": ["navy", "stone", "black", "green"], "materials": ["nylon"]},
            {"name": "Retro-X Fleece", "category": "jacket", "fit": "regular", "description": "Deep pile fleece jacket.", "price": 199, "colors": ["cream", "grey", "navy"], "materials": ["polyester fleece"]},
            {"name": "Torrentshell Jacket", "category": "jacket", "fit": "regular", "description": "Waterproof rain jacket.", "price": 179, "colors": ["black", "navy", "green"], "materials": ["recycled nylon"]},
            {"name": "Organic Cotton Tee", "category": "t-shirt", "fit": "regular", "description": "Responsibly sourced cotton tee.", "price": 45, "colors": ["white", "navy", "grey", "green"], "materials": ["organic cotton"]},
        ]
    },
    "Arc'teryx": {
        "origin": "Canada",
        "price_range": "luxury",
        "aesthetics": ["technical", "outdoor", "minimalist", "performance"],
        "typical_fits": ["trim", "athletic"],
        "signature_items": ["Beta AR", "Atom LT", "Gore-Tex shells"],
        "products": [
            {"name": "Beta AR Jacket", "category": "jacket", "fit": "trim", "description": "All-round Gore-Tex shell.", "price": 599, "colors": ["black", "blue", "green"], "materials": ["gore-tex pro"]},
            {"name": "Atom LT Hoody", "category": "jacket", "fit": "trim", "description": "Synthetic insulated jacket.", "price": 289, "colors": ["black", "grey", "navy"], "materials": ["coreloft insulation"]},
            {"name": "Gamma Pant", "category": "pants", "fit": "athletic", "description": "Stretch softshell pants.", "price": 225, "colors": ["black", "grey"], "materials": ["softshell"]},
            {"name": "Mantis 26 Backpack", "category": "accessories", "fit": "one size", "description": "Technical daypack.", "price": 159, "colors": ["black", "grey"], "materials": ["nylon"]},
        ]
    },

    # Contemporary American
    "Todd Snyder": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["american", "ivy league", "modern classic", "new york"],
        "typical_fits": ["slim", "regular"],
        "signature_items": ["Italian fabric shirts", "Champion collabs", "Modern ivy"],
        "products": [
            {"name": "Italian Linen Shirt", "category": "shirt", "fit": "regular", "description": "Camp collar in Italian linen.", "price": 248, "colors": ["white", "navy", "olive"], "materials": ["italian linen"]},
            {"name": "Slim Fit Chino", "category": "pants", "fit": "slim", "description": "Japanese fabric chinos.", "price": 228, "colors": ["navy", "olive", "khaki"], "materials": ["japanese cotton"]},
            {"name": "Champion Hoodie", "category": "hoodie", "fit": "regular", "description": "Champion collab heavyweight fleece.", "price": 198, "colors": ["grey", "navy", "green"], "materials": ["reverse weave cotton"]},
            {"name": "Italian Wool Suit", "category": "jacket", "fit": "slim", "description": "Slim fit suit. Italian wool.", "price": 898, "colors": ["navy", "charcoal"], "materials": ["italian wool"]},
            {"name": "Knit Polo", "category": "shirt", "fit": "slim", "description": "Fine gauge knit polo.", "price": 148, "colors": ["navy", "white", "grey"], "materials": ["cotton knit"]},
        ]
    },
    "Buck Mason": {
        "origin": "USA",
        "price_range": "mid",
        "aesthetics": ["california", "americana", "essential", "utilitarian"],
        "typical_fits": ["regular", "slim"],
        "signature_items": ["Slub cotton tees", "Raw denim", "Venice basics"],
        "products": [
            {"name": "Slub Curved Hem Tee", "category": "t-shirt", "fit": "regular", "description": "Signature slub cotton tee.", "price": 42, "colors": ["white", "grey", "navy", "black"], "materials": ["slub cotton"]},
            {"name": "Raw Selvage Jean", "category": "pants", "fit": "slim straight", "description": "American-made raw denim.", "price": 185, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "Pique Polo", "category": "shirt", "fit": "regular", "description": "Classic pique polo.", "price": 68, "colors": ["white", "navy", "grey"], "materials": ["cotton pique"]},
            {"name": "Deck Sweatshirt", "category": "sweater", "fit": "regular", "description": "Heavyweight fleece crewneck.", "price": 98, "colors": ["grey", "navy", "green"], "materials": ["cotton fleece"]},
            {"name": "Chore Coat", "category": "jacket", "fit": "regular", "description": "Canvas chore coat.", "price": 225, "colors": ["tan", "olive", "navy"], "materials": ["duck canvas"]},
        ]
    },

    # Streetwear and Urban
    "Stussy": {
        "origin": "USA",
        "price_range": "mid",
        "aesthetics": ["streetwear", "surf", "california", "iconic"],
        "typical_fits": ["oversized", "relaxed"],
        "signature_items": ["Logo tees", "Stock logo", "Beach club pieces"],
        "products": [
            {"name": "Basic Stock Tee", "category": "t-shirt", "fit": "regular", "description": "Classic logo tee.", "price": 45, "colors": ["white", "black", "grey", "navy"], "materials": ["cotton"]},
            {"name": "Stock Logo Hoodie", "category": "hoodie", "fit": "oversized", "description": "Heavyweight hoodie with stock logo.", "price": 135, "colors": ["black", "grey", "navy"], "materials": ["cotton fleece"]},
            {"name": "Beach Mob Shirt", "category": "shirt", "fit": "relaxed", "description": "Printed camp collar shirt.", "price": 125, "colors": ["print"], "materials": ["rayon"]},
            {"name": "Big Ol' Jeans", "category": "pants", "fit": "wide", "description": "Wide leg denim. Skate influenced.", "price": 145, "colors": ["indigo", "black"], "materials": ["denim"]},
            {"name": "Work Jacket", "category": "jacket", "fit": "relaxed", "description": "Canvas chore jacket.", "price": 185, "colors": ["tan", "black", "olive"], "materials": ["cotton canvas"]},
        ]
    },
    "Palace": {
        "origin": "England",
        "price_range": "premium",
        "aesthetics": ["streetwear", "british", "skate", "bold"],
        "typical_fits": ["oversized", "regular"],
        "signature_items": ["Tri-ferg logo", "Bold graphics", "London skate"],
        "products": [
            {"name": "Basically A Tee", "category": "t-shirt", "fit": "regular", "description": "Tri-ferg logo tee.", "price": 58, "colors": ["white", "black", "navy"], "materials": ["cotton"]},
            {"name": "Tri-Ferg Hoodie", "category": "hoodie", "fit": "oversized", "description": "Heavyweight hoodie with logo.", "price": 168, "colors": ["black", "grey", "navy", "green"], "materials": ["cotton fleece"]},
            {"name": "Shell Tracksuit Top", "category": "jacket", "fit": "regular", "description": "Retro shell track jacket.", "price": 198, "colors": ["navy", "black", "green"], "materials": ["nylon"]},
            {"name": "Baggies", "category": "pants", "fit": "wide", "description": "Wide leg cargo pants.", "price": 168, "colors": ["black", "olive", "navy"], "materials": ["cotton"]},
        ]
    },

    # Additional Premium Denim
    "Tellason": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["american", "raw denim", "heritage", "made in usa"],
        "typical_fits": ["straight", "slim straight", "tapered"],
        "signature_items": ["Cone Mills denim", "American-made jeans", "Classic fits"],
        "products": [
            {"name": "Ankara Straight Leg", "category": "pants", "fit": "straight", "description": "14.75oz Cone Mills selvedge.", "price": 230, "colors": ["indigo"], "materials": ["cone mills selvedge"]},
            {"name": "Ladbroke Grove Slim", "category": "pants", "fit": "slim straight", "description": "Slim straight Japanese selvedge.", "price": 250, "colors": ["indigo"], "materials": ["japanese selvedge"]},
            {"name": "Blubaugh Tapered", "category": "pants", "fit": "tapered", "description": "Modern tapered fit.", "price": 250, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "Coverall Jacket", "category": "jacket", "fit": "regular", "description": "Selvedge denim chore coat.", "price": 295, "colors": ["indigo"], "materials": ["selvedge denim"]},
        ]
    },
    "3sixteen": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["american", "raw denim", "new york", "minimalist"],
        "typical_fits": ["slim tapered", "straight", "relaxed tapered"],
        "signature_items": ["ST cuts", "Heavyweight denim", "Garment-dyed pieces"],
        "products": [
            {"name": "ST-100x Slim Tapered", "category": "pants", "fit": "slim tapered", "description": "14.5oz indigo selvedge. Signature cut.", "price": 265, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "CT-100x Classic Tapered", "category": "pants", "fit": "relaxed tapered", "description": "Relaxed through thigh, tapered leg.", "price": 265, "colors": ["indigo"], "materials": ["selvedge denim"]},
            {"name": "Type 3s Denim Jacket", "category": "jacket", "fit": "slim", "description": "Selvedge denim jacket.", "price": 295, "colors": ["indigo", "black"], "materials": ["selvedge denim"]},
            {"name": "Heavyweight Tee", "category": "t-shirt", "fit": "regular", "description": "USA-made heavyweight cotton.", "price": 68, "colors": ["white", "black", "grey"], "materials": ["heavyweight cotton"]},
            {"name": "Garment Dyed Fatigue Pant", "category": "pants", "fit": "relaxed tapered", "description": "Military-inspired pant.", "price": 228, "colors": ["olive", "navy", "khaki"], "materials": ["cotton twill"]},
        ]
    },

    # Contemporary Knitwear
    "John Smedley": {
        "origin": "England",
        "price_range": "premium",
        "aesthetics": ["british", "knitwear", "fine gauge", "heritage"],
        "typical_fits": ["slim", "regular"],
        "signature_items": ["Sea island cotton", "Fine merino", "Made in Derbyshire"],
        "products": [
            {"name": "Lundy Crew", "category": "sweater", "fit": "regular", "description": "Fine gauge merino crewneck.", "price": 295, "colors": ["navy", "black", "grey", "burgundy"], "materials": ["merino wool"]},
            {"name": "Sea Island Polo", "category": "shirt", "fit": "slim", "description": "Rare sea island cotton polo.", "price": 285, "colors": ["white", "navy", "black"], "materials": ["sea island cotton"]},
            {"name": "Hatfield Cardigan", "category": "sweater", "fit": "regular", "description": "V-neck merino cardigan.", "price": 325, "colors": ["navy", "charcoal", "camel"], "materials": ["merino wool"]},
            {"name": "Adrian Polo", "category": "shirt", "fit": "slim", "description": "Classic merino polo.", "price": 225, "colors": ["navy", "white", "grey"], "materials": ["merino wool"]},
        ]
    },
    "Inis Meain": {
        "origin": "Ireland",
        "price_range": "luxury",
        "aesthetics": ["irish", "aran", "artisanal", "island knits"],
        "typical_fits": ["regular", "relaxed"],
        "signature_items": ["Aran knits", "Donegal tweed", "Island traditions"],
        "products": [
            {"name": "Aran Crew", "category": "sweater", "fit": "regular", "description": "Traditional Aran cable knit.", "price": 495, "colors": ["cream", "grey", "navy"], "materials": ["merino wool"]},
            {"name": "Carpenter Cardigan", "category": "sweater", "fit": "relaxed", "description": "Shawl collar cardigan.", "price": 595, "colors": ["oatmeal", "charcoal", "navy"], "materials": ["wool linen"]},
            {"name": "Donegal Crew", "category": "sweater", "fit": "regular", "description": "Flecked Donegal wool sweater.", "price": 445, "colors": ["grey", "navy", "green"], "materials": ["donegal wool"]},
            {"name": "Linen Shirt Jacket", "category": "jacket", "fit": "relaxed", "description": "Knit linen shirt jacket.", "price": 495, "colors": ["cream", "navy", "olive"], "materials": ["linen knit"]},
        ]
    },

    # Additional Footwear-Adjacent (Casual wear from shoe brands)
    "Clarks Originals": {
        "origin": "England",
        "price_range": "mid",
        "aesthetics": ["british", "desert boot", "heritage", "casual"],
        "typical_fits": ["regular"],
        "signature_items": ["Desert Boots", "Wallabees", "Crepe sole"],
        "products": [
            {"name": "Desert Boot", "category": "footwear", "fit": "regular", "description": "Iconic suede desert boot.", "price": 170, "colors": ["sand", "beeswax", "black"], "materials": ["suede", "crepe sole"]},
            {"name": "Wallabee", "category": "footwear", "fit": "regular", "description": "Moccasin-style shoe. Crepe sole.", "price": 170, "colors": ["maple", "black", "sand"], "materials": ["suede", "crepe sole"]},
            {"name": "Desert Trek", "category": "footwear", "fit": "regular", "description": "Chunky sole variation.", "price": 180, "colors": ["grey", "tan", "black"], "materials": ["leather", "crepe sole"]},
            {"name": "Desert Khan", "category": "footwear", "fit": "regular", "description": "Chelsea boot version.", "price": 190, "colors": ["black", "brown", "sand"], "materials": ["suede", "crepe sole"]},
        ]
    },

    # Additional Brands to Reach 300+
    "Monitaly": {
        "origin": "USA",
        "price_range": "premium",
        "aesthetics": ["americana", "workwear", "japanese influence", "los angeles"],
        "typical_fits": ["relaxed", "wide"],
        "signature_items": ["Vancloth pieces", "Riding pants", "Asymmetric designs"],
        "products": [
            {"name": "Riding Pant", "category": "pants", "fit": "wide", "description": "High-waisted wide pants. Japanese fabric.", "price": 365, "colors": ["olive", "navy", "khaki"], "materials": ["vancloth cotton"]},
            {"name": "Military Half Coat", "category": "jacket", "fit": "relaxed", "description": "Mid-length military coat.", "price": 595, "colors": ["olive", "navy"], "materials": ["cotton"]},
            {"name": "Cropped Field Shell", "category": "jacket", "fit": "relaxed", "description": "Lightweight cropped jacket.", "price": 445, "colors": ["tan", "olive"], "materials": ["nylon cotton"]},
            {"name": "Drop Crotch Pant", "category": "pants", "fit": "wide", "description": "Relaxed pant with dropped crotch.", "price": 345, "colors": ["black", "navy"], "materials": ["cotton twill"]},
        ]
    },
    "Kaptain Sunshine": {
        "origin": "Japan",
        "price_range": "premium",
        "aesthetics": ["japanese", "americana", "military", "vintage"],
        "typical_fits": ["relaxed", "wide"],
        "signature_items": ["Traveller coat", "Gurkha shorts", "Military-inspired pieces"],
        "products": [
            {"name": "Traveller Coat", "category": "jacket", "fit": "relaxed", "description": "Long military-style coat. Burberry fabric.", "price": 895, "colors": ["khaki", "navy"], "materials": ["gabardine"]},
            {"name": "Gurkha Short", "category": "shorts", "fit": "relaxed", "description": "High-waisted Gurkha shorts.", "price": 295, "colors": ["khaki", "olive", "navy"], "materials": ["cotton twill"]},
            {"name": "West Point Pant", "category": "pants", "fit": "wide", "description": "High-rise wide trousers.", "price": 385, "colors": ["khaki", "navy", "grey"], "materials": ["cotton wool"]},
            {"name": "Open Collar Shirt", "category": "shirt", "fit": "relaxed", "description": "Camp collar in fine cotton.", "price": 285, "colors": ["white", "blue", "olive"], "materials": ["cotton"]},
        ]
    },
    "Visvim": {
        "origin": "Japan",
        "price_range": "luxury",
        "aesthetics": ["japanese", "americana", "artisanal", "heritage craft"],
        "typical_fits": ["relaxed", "wide"],
        "signature_items": ["FBT moccasins", "Social Sculpture denim", "Handcrafted pieces"],
        "products": [
            {"name": "Social Sculpture 101", "category": "pants", "fit": "slim straight", "description": "Hand-distressed selvedge denim.", "price": 795, "colors": ["indigo"], "materials": ["damaged selvedge denim"]},
            {"name": "Lhamo Shirt", "category": "shirt", "fit": "relaxed", "description": "Hand-woven fabric shirt. Artisanal.", "price": 895, "colors": ["indigo", "natural"], "materials": ["hand-woven cotton"]},
            {"name": "Hakama Pants", "category": "pants", "fit": "wide", "description": "Traditional Japanese hakama. Modern interpretation.", "price": 945, "colors": ["navy", "black"], "materials": ["wool"]},
            {"name": "Noragi Jacket", "category": "jacket", "fit": "relaxed", "description": "Japanese workwear jacket. Natural dye.", "price": 1295, "colors": ["indigo"], "materials": ["hand-dyed cotton"]},
            {"name": "Jumbo Hoodie", "category": "hoodie", "fit": "oversized", "description": "Heavyweight loopwheel fleece.", "price": 695, "colors": ["grey", "navy"], "materials": ["loopwheel cotton"]},
        ]
    },
})


def generate_items_from_database() -> List[ClothingItem]:
    """Generate ClothingItem objects from the brand database."""
    items = []
    item_counter = 1

    for brand_name, brand_data in BRAND_DATABASE.items():
        for product in brand_data.get('products', []):
            item = ClothingItem(
                id=f"prod_{item_counter:04d}",
                name=product['name'],
                brand=brand_name,
                category=product['category'],
                description=product['description'],
                fit=product.get('fit'),
                style_tags=brand_data.get('aesthetics', []),
                colors=product.get('colors', []),
                materials=product.get('materials', []),
                source_url=None,
                source_type="brand_database",
                price_usd=product.get('price'),
            )
            items.append(item)
            item_counter += 1

    return items


def generate_brands_from_database() -> List[Brand]:
    """Generate Brand objects from the brand database."""
    brands = []

    for brand_name, brand_data in BRAND_DATABASE.items():
        brand = Brand(
            id=f"brand_{brand_name.lower().replace(' ', '_').replace('-', '_').replace('.', '')}",
            name=brand_name,
            description=f"{brand_name} is a {brand_data.get('origin', 'international')} brand known for {', '.join(brand_data.get('aesthetics', [])[:3])} aesthetics.",
            aesthetics=brand_data.get('aesthetics', []),
            typical_fits=brand_data.get('typical_fits', []),
            price_range=brand_data.get('price_range', 'mid'),
            origin_country=brand_data.get('origin'),
            signature_items=brand_data.get('signature_items', []),
            similar_brands=[],  # Could be populated with logic
        )
        brands.append(brand)

    return brands


def get_production_data():
    """Get production-ready data from the database."""
    return {
        'items': generate_items_from_database(),
        'brands': generate_brands_from_database(),
    }
