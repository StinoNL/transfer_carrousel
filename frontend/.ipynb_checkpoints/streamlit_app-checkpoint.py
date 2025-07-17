import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000"

st.title("Football Transfer Value Predictor")
st.markdown(
    "Enter player stats in the sidebar and click **Predict Value** to get the estimated transfer value."
)

st.sidebar.header("Player Stats")
age = st.sidebar.number_input("Age", min_value=15, max_value=50, value=25, step=1)
minutes_played = st.sidebar.number_input(
    "Minutes Played", min_value=0, max_value=5000, value=1500, step=50
)
goals = st.sidebar.number_input("Goals", min_value=0, max_value=100, value=10, step=1)

# Trigger prediction
if st.sidebar.button("Predict Value"):
    try:
        params = {"age": age, "minutes_played": minutes_played, "goals": goals}
        response = requests.get(f"{API_BASE_URL}/predict", params=params)
        response.raise_for_status()
        data = response.json()
        value = data.get("predicted_value", None)
        if value is not None:
            st.success(f"Estimated Transfer Value: €{value:,.0f}")
        else:
            st.error("Unexpected response from server.")
    except Exception as e:
        st.error(f"Error fetching prediction: {e}")
