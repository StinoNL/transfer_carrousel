import streamlit as st
import requests

# Configuration
st.set_page_config(
    page_title="Football Transfer Value Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_BASE_URL = "https://my-api-app-154142035363.europe-west1.run.app"

st.title("⚽ Football Transfer Value Predictor")
st.write(
    "Enter player stats in the sidebar and click **Predict Value** to estimate the transfer fee."
)

st.sidebar.header("Player Stats")
age = st.sidebar.number_input("Age", min_value=15, max_value=50, value=25, step=1)
minutes_played = st.sidebar.number_input(
    "Minutes Played", min_value=1, max_value=5000, value=1500, step=50
)
goals = st.sidebar.number_input("Goals", min_value=0, max_value=100, value=10, step=1)
assists = st.sidebar.number_input("Assists", min_value=0, max_value=100, value=5, step=1)
position = st.sidebar.selectbox("Position", ["Goalkeeper", "Defender", "Midfield", "Attack"])

def fetch_prediction(params):
    """
    Call the backend API and return the predicted value.
    """
    response = requests.get(f"{API_BASE_URL}/prediction", params=params)
    response.raise_for_status()
    return response.json()

if st.sidebar.button("Predict Value"):
    with st.spinner("Calculating prediction..."):
        try:
            params = {
                "age": age,
                "minutes_played": minutes_played,
                "goals": goals,
                "assists": assists,
                "position": position
            }
            data = fetch_prediction(params)
            value = data.get("prediction")
            if value is not None:
                col1, col2, col3 = st.columns(3)
                col1.metric("Estimated Value", f"€{value:,.0f}")
                gpm = goals / minutes_played if minutes_played else 0
                apm = assists / minutes_played if minutes_played else 0
                col2.metric("Goals per Minute", f"{gpm:.3f}")
                col3.metric("Assists per Minute", f"{apm:.3f}")
                st.success("Prediction successful!")
            else:
                st.error("Unexpected response structure from server.")
        except Exception as e:
            st.error(f"Error fetching prediction: {e}")
