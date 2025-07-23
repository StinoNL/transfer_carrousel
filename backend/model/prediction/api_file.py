<<<<<<< HEAD

import pickle
import os

#Takes 3 inputs: age, minutes, goals
def predict_player_value(age: float, minutes_played: float, goals: float, assists: float, position: str):

    """
    Load trained model and return value prediction.
    """
    model_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'stjin_model.pkl'
    )

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    #Makes a prediction
    X_pred = [[age, minutes_played, goals, assists, position]]
    prediction = model.predict(X_pred)

    #Returns a single value (the predicted transfer value)
    return prediction[0]
=======
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
>>>>>>> 0f4fa3a6387a3fb825e49ff293d0e3ec162004ee
