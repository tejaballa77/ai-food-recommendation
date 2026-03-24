def get_diet_rules(disease):
    rules_db = {

        # ---------------- DIABETES ----------------
        "diabetes": {
            "avoid": ["sugar", "refined_carbs", "fried", "sweet"],
            "prefer": ["low_glycemic", "fiber", "protein", "whole_grain"],
            "note": "Control blood sugar by avoiding sugary and refined foods."
        },

        # ---------------- HYPERTENSION ----------------
        "hypertension": {
            "avoid": ["high_sodium", "processed", "fried"],
            "prefer": ["low_sodium", "vegetables", "fruits"],
            "note": "Reduce salt intake to manage blood pressure."
        },

        # ---------------- CHOLESTEROL ----------------
        "cholesterol": {
            "avoid": ["saturated_fat", "fried", "butter"],
            "prefer": ["lean_protein", "fiber", "omega3"],
            "note": "Avoid unhealthy fats and choose heart-friendly foods."
        },

        # ---------------- NEPHROLOGY (KIDNEY) ----------------
        "nephrology": {
            "avoid": ["high_sodium", "processed", "protein_excess"],
            "prefer": ["low_sodium", "light", "controlled_protein"],
            "note": "Limit salt and protein intake to protect kidney function."
        },

        # ---------------- CANCER ----------------
        "cancer": {
            "avoid": ["processed", "fried", "sugar"],
            "prefer": ["antioxidant", "fiber", "nutrient_dense"],
            "note": "Focus on nutrient-rich and antioxidant foods to support recovery."
        },

        # ---------------- ACIDITY ----------------
        "acidity": {
            "avoid": ["spicy", "fried", "citrus"],
            "prefer": ["low_spice", "light", "alkaline"],
            "note": "Avoid spicy foods to reduce acidity."
        },

        # ---------------- WEIGHT LOSS ----------------
        "weight_loss": {
            "avoid": ["high_calorie", "sugar", "fried"],
            "prefer": ["low_calorie", "protein", "fiber"],
            "note": "Maintain calorie deficit with healthy foods."
        },

        # ---------------- WEIGHT GAIN ----------------
        "weight_gain": {
            "avoid": ["low_calorie"],
            "prefer": ["high_calorie", "protein", "healthy_fats"],
            "note": "Increase calorie intake with nutritious foods."
        }
    }

    return rules_db.get(disease, {"avoid": [], "prefer": [], "note": ""})