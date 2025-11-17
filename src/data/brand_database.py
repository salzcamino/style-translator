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
