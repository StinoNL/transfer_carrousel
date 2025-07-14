import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Create dummy training data
df = pd.DataFrame({
    'age': [20, 24, 30, 28, 22],
    'minutes_played': [1500, 2000, 1800, 1600, 1900],
    'goals': [5, 10, 7, 3, 6],
    'value': [1_000_000, 4_000_000, 3_000_000, 2_000_000, 3_500_000]
})

X = df[['age', 'minutes_played', 'goals']]
y = df['value']

# Train the model
model = RandomForestRegressor()
model.fit(X, y)

# Save the model with pickle
with open('backend/model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Dummy model saved")
