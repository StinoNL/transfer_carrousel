import streamlit as st
import requests

# Configuration
st.set_page_config(
    page_title="Football Transfer Value Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_BASE_URL = "https://my-api-app-154142035363.europe-west1.run.app"

st.title("⚽ Value Predictor & Player Suggestor")
st.write(
    "Enter player stats in the sidebar and click **Predict Value** to estimate the transfer fee."
)
st.write(
    "Use the **Find Cheaper Alternatives** section below **Predict Value** to discover similar players based on a given name."
)

st.sidebar.header("Player Stats")
age = st.sidebar.number_input("Age", min_value=15, max_value=50, value=25, step=1)
minutes_played = st.sidebar.number_input(
    "Minutes Played", min_value=1, max_value=10000, value=1500, step=50
)
goals = st.sidebar.number_input("Goals", min_value=0, max_value=100, value=10, step=1)
assists = st.sidebar.number_input("Assists", min_value=0, max_value=100, value=5, step=1)
position = st.sidebar.selectbox("Position", ["Defender", "Midfield", "Attack"])
height_in_cm = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=180, step=1)
yellow_cards = st.sidebar.number_input("Yellow Cards", min_value=0, max_value=20, value=0, step=1)
red_cards = st.sidebar.number_input("Red Cards", min_value=0, max_value=10, value=0, step=1)
foot = st.sidebar.selectbox("Foot", ["Right", "Left", "Both"])


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
                "position": position,
                "height_in_cm": height_in_cm,
                "yellow_cards": yellow_cards,
                "red_cards": red_cards,
                "foot": foot
            }
            data = fetch_prediction(params)
            value = data.get("prediction")
            if value is not None:
                col1, col2, col3 = st.columns(3)
                col1.metric("Estimated Value", f"€{value:,.0f}")
                st.success("Prediction successful!")
            else:
                st.error("Unexpected response structure from server.")
        except Exception as e:
            st.error(f"Error fetching prediction: {e}")

# New section to recommend similar players
st.sidebar.markdown("---")
st.sidebar.subheader("Find Cheaper Alternatives")
player_name_input = st.sidebar.text_input("Compare With Player Name", "")

def fetch_recommendations(player_name):
    """
    Call the recommend API and return similar players.
    """
    response = requests.get(f"{API_BASE_URL}/recommend", params={"player_name": player_name})
    response.raise_for_status()
    return response.json()

if st.sidebar.button("Find Similar Players"):
    if not player_name_input.strip():
        st.warning("Please enter a player name.")
    else:
        with st.spinner("Fetching similar players..."):
            try:
                similar_players = fetch_recommendations(player_name_input)
                st.markdown(f"## 🔍 Similar Players to **{player_name_input}**")
                for player in similar_players:
                    with st.container():
                        cols = st.columns([1, 2])
                        with cols[0]:
                            st.image(player["image_url"], width=120)
                        with cols[1]:
                            st.markdown(f"**{player['player_name']}** ({player['age']} yrs, {player['position']})")
                            st.markdown(f"**Club:** {player['club_name']}")
                            st.markdown(f"**Cluster:** _{player['cluster_name']}_")
                            st.markdown(
                                f"📊 Goals: {player['goals']}, Assists: {player['assists']}  \n"
                                f"💸 Market Value (Million): €{player['market_value_million']:,}M"
                            )
                        st.markdown("---")
            except Exception as e:
                st.error(f"Failed to fetch recommendations: {e}")
