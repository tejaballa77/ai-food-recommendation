import streamlit as st

# -------- IMPORTS --------
from modules.nlp_engine import parse_user_query
from modules.disease_engine import get_diet_rules
from modules.menu_analyzer import analyze_menu, analyze_menu_preferences
from modules.recommender import recommend_items
from modules.reason_engine import get_food_reason
from modules.lifestyle_engine import get_sleep_recommendation
from modules.preference_engine import parse_preferences
from modules.water_engine import get_water_recommendation


# -------- PAGE CONFIG --------
st.set_page_config(page_title="AI Food Assistant", layout="wide")

st.title("🥗 AI Health & Daily Meal Recommendation System")

# -------- MODE SELECTOR --------
mode = st.radio(
    "Select Recommendation Type:",
    ["Disease-Based", "Preference-Based"]
)

# -------- INPUT --------
user_query = st.text_input(
    "Enter your query:",
    placeholder="Example: I have diabetes OR high protein food no rice"
)

budget = st.slider("Select Budget (₹)", 50, 500, 300)

# -------- BUTTON --------
if st.button("Get Recommendations"):

    if not user_query:
        st.warning("Please enter your query.")

    else:
        try:
            # =========================
            # DISEASE MODE
            # =========================
            if mode == "Disease-Based":

                parsed = parse_user_query(user_query)

                if not parsed.get("disease"):
                    st.error("Please mention a health condition.")
                    st.stop()

                rules = get_diet_rules(parsed["disease"])
                analyzed = analyze_menu(rules)
                data = recommend_items(analyzed, budget)

                # -------- HEADER --------
                st.subheader("🩺 Health-Based Daily Meal Plan")

                # -------- DOCTOR NOTE --------
                st.info(rules.get("note", ""))

                sleep = get_sleep_recommendation(parsed["disease"])

            # =========================
            # PREFERENCE MODE
            # =========================
            else:

                preferences = parse_preferences(user_query)

                analyzed = analyze_menu_preferences(preferences)
                data = recommend_items(analyzed, budget)

                # -------- HEADER --------
                st.subheader("🎯 Personalized Daily Meal Plan")

                sleep = None


            # =========================
            # MEAL PLAN DISPLAY
            # =========================
            st.subheader("🍽️ Full Day Meal Plan")

            meal_icons = {
                "breakfast": "🍳 Breakfast",
                "lunch": "🍛 Lunch",
                "dinner": "🍽️ Dinner"
            }

            for meal, items in data.items():

                st.markdown(f"## {meal_icons.get(meal, meal)}")

                if not items:
                    st.info("No suitable items found.")
                    continue

                cols = st.columns(3)

                for i, item in enumerate(items):
                    reason = get_food_reason(
                        item["item"],
                        parsed["disease"] if mode == "Disease-Based" else mode,
                        item["score"]
                    )

                    with cols[i % 3]:
                        st.markdown(f"""
                        ### 🍽️ {item['item']}

                        💰 ₹{item['price']}  
                        🏪 {item['restaurant']}  
                        ⭐ Health Score: **{item['health_score']}/10**

                        ➤ **{reason}**
                        """)

            # =========================
            # LIFESTYLE (ONLY DISEASE MODE)
            # =========================
            if sleep:
                st.subheader("🛌 Lifestyle Recommendation")

                col1, col2 = st.columns(2)

                # WAIT TIME
                with col1:
                    st.markdown(f"""
                    <div style="
                        background-color:#111;
                        padding:20px;
                        border-radius:15px;
                        text-align:center;
                    ">
                        <h1>⏰</h1>
                        <h4>After Food Intake</h4>
                        <p><b>Wait for {sleep['wait_time']} before going to sleep</b></p>
                    </div>
                    """, unsafe_allow_html=True)

                # SLEEP TIME
                with col2:
                    st.markdown(f"""
                    <div style="
                        background-color:#111;
                        padding:20px;
                        border-radius:15px;
                        text-align:center;
                    ">
                        <h1>😴</h1>
                        <h4>Sleep Duration</h4>
                        <p><b>Sleep for at least {sleep['sleep']}</b></p>
                    </div>
                    """, unsafe_allow_html=True)

                        # -------- WATER INTAKE --------
            # -------- WATER INTAKE --------
            if mode == "Disease-Based":

                water = get_water_recommendation(parsed["disease"])

                st.subheader("💧 Daily Water Intake")

                st.markdown(f"""
                <div style="
                    background-color:#111;
                    padding:25px;
                    border-radius:15px;
                    text-align:center;
                ">
                    <h1 style="font-size:50px;">💧</h1>
                    <h3>Water Intake</h3>
                    <p style="font-size:18px;">
                        <b>Drink {water['amount']} per day</b>
                    </p>
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")