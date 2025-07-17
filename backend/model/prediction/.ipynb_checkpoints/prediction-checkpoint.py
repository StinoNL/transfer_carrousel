
import pickle
import os

#Takes 3 inputs: age, minutes, goals
def predict_player_value(age: float, minutes_played: float, goals: float):
    """
    Load trained model and return value prediction.
    """
    model_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'model.pkl'
    )

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    #Makes a prediction
    X_pred = [[age, minutes_played, goals]]
    prediction = model.predict(X_pred)

    #Returns a single value (the predicted transfer value)
    return prediction[0]
