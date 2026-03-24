def get_sleep_recommendation(disease):
    data = {

        # -------- DIABETES --------
        "diabetes": {
            "wait_time": "1.5 - 2 hours",
            "sleep": "7 - 8 hours"
        },

        # -------- HYPERTENSION --------
        "hypertension": {
            "wait_time": "1.5 hours",
            "sleep": "7 - 9 hours"
        },

        # -------- CHOLESTEROL --------
        "cholesterol": {
            "wait_time": "2 hours",
            "sleep": "7 - 8 hours"
        },

        # -------- NEPHROLOGY (KIDNEY) --------
        "nephrology": {
            "wait_time": "2 hours",
            "sleep": "7 - 8 hours"
        },

        # -------- CANCER --------
        "cancer": {
            "wait_time": "2 hours",
            "sleep": "8 - 9 hours"
        },

        # -------- ACIDITY --------
        "acidity": {
            "wait_time": "2 - 3 hours",
            "sleep": "7 - 8 hours"
        },

        # -------- WEIGHT LOSS --------
        "weight_loss": {
            "wait_time": "1.5 hours",
            "sleep": "7 - 8 hours"
        },

        # -------- WEIGHT GAIN --------
        "weight_gain": {
            "wait_time": "2 hours",
            "sleep": "7 - 8 hours"
        }
    }

    return data.get(disease, {
        "wait_time": "1 - 2 hours",
        "sleep": "7 - 8 hours"
    })