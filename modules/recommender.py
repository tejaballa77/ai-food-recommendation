def recommend_items(analyzed_items, budget):
    if budget:
        analyzed_items = [
            item for item in analyzed_items
            if item["price"] <= budget
        ]

    meals = {
        "breakfast": [],
        "lunch": [],
        "dinner": []
    }

    for item in analyzed_items:
        meals[item["meal"]].append(item)

    # Sort each meal
    for meal in meals:
        meals[meal] = sorted(
            meals[meal],
            key=lambda x: x["score"],
            reverse=True
        )[:3]

    return meals