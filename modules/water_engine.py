def get_water_recommendation(disease):

    data = {
        "diabetes": {
            "amount": "3 - 4 liters",
            "reason": "Helps regulate blood sugar and hydration."
        },
        "hypertension": {
            "amount": "3 liters",
            "reason": "Supports blood pressure control."
        },
        "cholesterol": {
            "amount": "3 liters",
            "reason": "Helps maintain heart health."
        },
        "nephrology": {
            "amount": "2 - 2.5 liters",
            "reason": "Controlled intake to avoid kidney strain."
        },
        "cancer": {
            "amount": "3 - 3.5 liters",
            "reason": "Supports recovery and detoxification."
        },
        "acidity": {
            "amount": "3 liters",
            "reason": "Helps reduce acidity levels."
        },
        "weight_loss": {
            "amount": "3 - 4 liters",
            "reason": "Supports metabolism and fat loss."
        },
        "weight_gain": {
            "amount": "2.5 - 3 liters",
            "reason": "Maintains hydration balance."
        }
    }

    return data.get(disease, {
        "amount": "3 liters",
        "reason": "Maintain proper hydration."
    })