import os
import pickle
from fastapi import FastAPI
import pandas as pd
from prediction.recommender import recommend_similar_players_by_name

df_clean = pd.read_csv(
     '../clean_data/clean_players_clustered.csv',
    encoding="utf-8")

app = FastAPI()

@app.get("/")
def root():
    return {'greeting': "hello"}

@app.get("/recommend")
def recommend(player_name: str):
    results = recommend_similar_players_by_name(df_clean, player_name)
    return results

@app.get("/prediction")
def predict_player_value(
    age: float,
    minutes_played: float,
    goals: float,
    assists: float,
    position: str,
):
    model_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'stjin_model.pkl'
    )

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    #CALCULATE THE GOALS AND ASSISTS PER MINUTE
    goals_per_minute_calculate = goals / minutes_played
    assists_per_minute_calculate = assists / minutes_played
    print(goals_per_minute_calculate, assists_per_minute_calculate)

    input_df = pd.DataFrame([{
        "age": age,
        "minutes_played": minutes_played,
        "goals": goals,
        "assists": assists,
        "position": position,
        "goals_per_minute": goals_per_minute_calculate,
        "assists_per_minute": assists_per_minute_calculate
    }])

    prediction = model.predict(input_df)

    return {'prediction': prediction[0]}
    #return {'prediction': prediction[0], 'goals_per_minute_calculate': goals_per_minute_calculate, 'assists_per_minute_calculate': assists_per_minute_calculate}
