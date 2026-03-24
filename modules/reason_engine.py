def get_food_reason(item_name, disease, score):
    name = item_name.lower()

    # -------- POSITIVE CASE --------
    if score >= 0:

        # General food logic
        if "grilled" in name:
            return "High protein and low fat."
        if "salad" in name:
            return "Rich in fiber and low in calories."
        if "soup" in name:
            return "Light and easy to digest."
        if "oats" in name:
            return "Low glycemic index and high fiber."
        if "brown rice" in name:
            return "Whole grain with better blood sugar control."
        if "fish" in name:
            return "Rich in omega-3 and heart-friendly."
        if "vegetable" in name:
            return "Rich in vitamins and nutrients."
        if "fruit" in name:
            return "Provides essential vitamins and antioxidants."

        # -------- DISEASE-SPECIFIC --------

        if disease == "diabetes":
            return "Helps maintain stable blood sugar levels."

        if disease == "hypertension":
            return "Low sodium helps control blood pressure."

        if disease == "cholesterol":
            return "Supports heart health and lowers bad cholesterol."

        if disease == "nephrology":
            return "Low sodium and kidney-friendly diet option."

        if disease == "cancer":
            return "Rich in nutrients and supports immunity."

        if disease == "acidity":
            return "Light and non-spicy food reduces acidity."

        if disease == "weight_loss":
            return "Low calorie and helps in weight management."

        if disease == "weight_gain":
            return "High calorie and supports weight gain."

        return "Balanced and suitable for your condition."

    # -------- NEGATIVE CASE --------
    else:

        # General food logic
        if "fried" in name or "pakora" in name or "samosa" in name:
            return "High in unhealthy fats."
        if "cake" in name or "ice cream" in name or "milkshake" in name:
            return "High sugar content."
        if "biryani" in name or "rice" in name:
            return "High in refined carbohydrates."
        if "butter" in name or "cream" in name:
            return "High in saturated fats."
        if "processed" in name:
            return "Contains preservatives and high sodium."

        # -------- DISEASE-SPECIFIC --------

        if disease == "diabetes":
            return "May cause rapid increase in blood sugar."

        if disease == "hypertension":
            return "High salt may increase blood pressure."

        if disease == "cholesterol":
            return "May increase bad cholesterol levels."

        if disease == "nephrology":
            return "High sodium or protein may harm kidney function."

        if disease == "cancer":
            return "Processed or unhealthy food may weaken immunity."

        if disease == "acidity":
            return "Spicy or oily food may worsen acidity."

        if disease == "weight_loss":
            return "High calorie food may slow weight loss."

        if disease == "weight_gain":
            return "Low calorie food may not support weight gain."

        return "Not suitable for your health condition."