def parse_preferences(query):
    query = query.lower()

    preferences = {
        "include": [],
        "exclude": []
    }

    # -------- INCLUDE --------
    if "protein" in query:
        preferences["include"].append("protein")

    if "light" in query:
        preferences["include"].append("light")

    if "spicy" in query:
        preferences["include"].append("spicy")

    if "healthy" in query:
        preferences["include"].append("fiber")

    # -------- EXCLUDE --------
    if "no rice" in query:
        preferences["exclude"].append("rice")

    if "no oil" in query:
        preferences["exclude"].append("oil")

    if "no sugar" in query:
        preferences["exclude"].append("sugar")

    return preferences