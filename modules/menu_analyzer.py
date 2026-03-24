import json
import os


# -------- LOAD MENU --------
def load_menus():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "data", "sample_menus.json")

    with open(file_path) as f:
        return json.load(f)


# -------- COMMON FOOD TAGS --------
food_tags = {
    # Negative
    "sugar": ["cake", "ice cream", "milkshake", "dessert"],
    "refined_carbs": ["white bread", "biryani", "rice"],
    "fried": ["fried", "samosa", "pakora", "vada"],
    "high_sodium": ["salt", "chips", "processed"],
    "processed": ["processed", "packaged"],
    "saturated_fat": ["butter", "cream"],
    "spicy": ["masala", "chilli"],
    "cold_food": ["ice cream", "cold coffee"],

    # Positive
    "protein": ["chicken", "fish", "egg", "paneer"],
    "fiber": ["salad", "vegetable"],
    "low_glycemic": ["oats", "brown rice"],
    "whole_grain": ["brown rice", "oats"],
    "lean_protein": ["grilled chicken", "fish"],
    "omega3": ["fish"],
    "liquid": ["soup"],
    "soft": ["khichdi", "upma"],
    "easy_digest": ["soup", "khichdi"],
    "warm": ["soup", "tea"],
    "herbal": ["herbal tea"],
    "low_calorie": ["salad"],
    "high_calorie": ["milkshake", "cake"],
    "healthy_fats": ["nuts"],

    # New medical tags
    "protein_excess": ["red meat"],
    "controlled_protein": ["paneer"],
    "antioxidant": ["vegetable", "fruit"],
    "nutrient_dense": ["salad", "vegetable"]
}


# -------- DISEASE-BASED ANALYSIS --------
def analyze_menu(diet_rules):
    menus = load_menus()
    results = []

    for restaurant in menus:
        for item in restaurant["items"]:
            name = item["name"].lower()
            score = 0

            # -------- AVOID --------
            for avoid in diet_rules.get("avoid", []):
                for keyword in food_tags.get(avoid, []):
                    if keyword in name:
                        score -= 2

            # -------- PREFER --------
            for prefer in diet_rules.get("prefer", []):
                for keyword in food_tags.get(prefer, []):
                    if keyword in name:
                        score += 2

            # -------- HEALTH SCORE --------
            health_score = max(0, min(10, score + 5))

            results.append({
                "restaurant": restaurant["restaurant"],
                "item": item["name"],
                "price": item["price"],
                "meal": item.get("meal", "lunch"),  # DEFAULT LUNCH
                "score": score,
                "health_score": health_score
            })

    return results


# -------- PREFERENCE-BASED ANALYSIS --------
def analyze_menu_preferences(preferences):
    menus = load_menus()
    results = []

    for restaurant in menus:
        for item in restaurant["items"]:
            name = item["name"].lower()
            score = 0

            # -------- INCLUDE --------
            for inc in preferences.get("include", []):
                for keyword in food_tags.get(inc, []):
                    if keyword in name:
                        score += 2

            # -------- EXCLUDE --------
            for exc in preferences.get("exclude", []):
                for keyword in food_tags.get(exc, []):
                    if keyword in name:
                        score -= 3

            # -------- HEALTH SCORE --------
            health_score = max(0, min(10, score + 5))

            results.append({
                "restaurant": restaurant["restaurant"],
                "item": item["name"],
                "price": item["price"],
                "meal": item.get("meal", "lunch"),
                "score": score,
                "health_score": health_score
            })

    return results