
import pickle
import os

#Takes 3 inputs: age, minutes, goals
<<<<<<< HEAD
def predict_player_value(age: float, minutes_played: float, goals: float, assists: float, position: str):

=======
def predict_player_value(age: float, minutes_played: float, goals: float):
>>>>>>> 0f4fa3a6387a3fb825e49ff293d0e3ec162004ee
    """
    Load trained model and return value prediction.
    """
    model_path = os.path.join(
        os.path.dirname(__file__),
        '..',
<<<<<<< HEAD
        'stjin_model.pkl'
=======
        'model.pkl'
>>>>>>> 0f4fa3a6387a3fb825e49ff293d0e3ec162004ee
    )

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    #Makes a prediction
<<<<<<< HEAD
    X_pred = [[age, minutes_played, goals, assists, position]]
=======
    X_pred = [[age, minutes_played, goals]]
>>>>>>> 0f4fa3a6387a3fb825e49ff293d0e3ec162004ee
    prediction = model.predict(X_pred)

    #Returns a single value (the predicted transfer value)
    return prediction[0]
