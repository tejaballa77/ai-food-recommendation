import re

def parse_user_query(query):
    query = query.lower()

    result = {
        "disease": None,
        "budget": None
    }

    # -------- Disease Detection --------
    if any(word in query for word in ["diabetes", "sugar"]):
        result["disease"] = "diabetes"

    elif any(word in query for word in ["bp", "blood pressure", "hypertension"]):
        result["disease"] = "hypertension"

    elif "cholesterol" in query:
        result["disease"] = "cholesterol"

    elif any(word in query for word in ["kidney", "renal", "nephro"]):
        result["disease"] = "nephrology"

    elif "cancer" in query:
        result["disease"] = "cancer"

    elif "acidity" in query:
        result["disease"] = "acidity"

    elif "weight loss" in query:
        result["disease"] = "weight_loss"

    elif "weight gain" in query:
        result["disease"] = "weight_gain"

    # -------- Budget --------
    match = re.search(r'\d+', query)
    if match:
        result["budget"] = int(match.group())

    return result