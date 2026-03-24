def generate_response(data, disease):
    recommended = data["recommended"]
    avoid = data["avoid"]

    response = f"### 🩺 Condition: {disease.upper()}\n\n"
    response += f"💡 Advice: {data.get('note','Follow a balanced diet.')}\n\n"

    # ----------- Recommended Items -----------
    response += "### ✅ Recommended Items:\n"

    if recommended:
        for item in recommended:
            reason = get_reason(item["item"], disease, positive=True)
            response += f"- ✔️ {item['item']} (₹{item['price']}) - {item['restaurant']}\n"
            response += f"   ➤ {reason}\n"
    else:
        response += "- No strong recommendations available\n"

    # ----------- Avoid Items -----------
    response += "\n### ❌ Avoid Items:\n"

    if avoid:
        for item in avoid:
            reason = get_reason(item["item"], disease, positive=False)
            response += f"- ❌ {item['item']} - {item['restaurant']}\n"
            response += f"   ➤ {reason}\n"
    else:
        response += "- No major restrictions\n"

    response += "\n💡 Suggestions are based on general dietary guidelines."

    return response


# ----------- Reason Generator -----------

def get_reason(item_name, disease, positive=True):
    name = item_name.lower()

    # -------- Diabetes --------
    if disease == "diabetes":
        if positive:
            if "salad" in name:
                return "Low in carbohydrates and helps control blood sugar."
            if "grilled" in name:
                return "High protein and low sugar content."
            if "fruit" in name:
                return "Natural sugars but safe in moderation."
            return "Suitable as it avoids high sugar content."
        else:
            if "rice" in name or "biryani" in name:
                return "High carbs can increase blood sugar levels."
            if "fried" in name:
                return "Contains unhealthy fats and refined carbs."
            return "May raise blood sugar levels."

    # -------- Hypertension --------
    elif disease == "hypertension":
        if positive:
            return "Low sodium helps maintain healthy blood pressure."
        else:
            return "High salt content may increase blood pressure."

    # -------- Cholesterol --------
    elif disease == "cholesterol":
        if positive:
            if "grilled" in name:
                return "Low fat and heart-friendly option."
            return "Helps maintain healthy cholesterol levels."
        else:
            if "fried" in name or "butter" in name:
                return "High in unhealthy fats."
            return "May increase bad cholesterol levels."

    # -------- Fever --------
    elif disease == "fever":
        if positive:
            return "Light and easy-to-digest food helps recovery."
        else:
            return "Heavy or spicy food may worsen condition."

    # -------- Cold --------
    elif disease == "cold":
        if positive:
            return "Warm food helps soothe throat and improves comfort."
        else:
            return "Cold foods may aggravate symptoms."

    # -------- Cough --------
    elif disease == "cough":
        if positive:
            return "Warm liquids help relieve throat irritation."
        else:
            return "Cold or fried food may irritate throat."

    # -------- Weight Loss --------
    elif disease == "weight_loss":
        if positive:
            return "Low calorie and helps in weight management."
        else:
            return "High calorie food may slow weight loss."

    # -------- Weight Gain --------
    elif disease == "weight_gain":
        if positive:
            return "High calorie and helps in gaining weight."
        else:
            return "Low calorie food may not support weight gain."

    # -------- Acidity --------
    elif disease == "acidity":
        if positive:
            return "Mild food helps reduce acidity."
        else:
            return "Spicy or oily food may increase acidity."

    # -------- Anemia --------
    elif disease == "anemia":
        if positive:
            return "Rich in iron and supports healthy blood levels."
        else:
            return "Lacks essential nutrients for recovery."

    # -------- Default --------
    if positive:
        return "Generally suitable for your condition."
    else:
        return "Not recommended for your condition."