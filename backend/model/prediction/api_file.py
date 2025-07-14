from fastapi import FastAPI
from model.prediction.prediction import predict_player_value

app = FastAPI()

@app.get("/")
def root():
    return {"message": "the football scout is ready to go!"}

@app.get("/predict")
def predict(age: float, minutes_played: float, goals: float):
    prediction = predict_player_value(age, minutes_played, goals)
    return {"predicted_value": prediction}
