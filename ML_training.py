from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the synthetic data
df = pd.read_excel('synthetic_data.xlsx')

# Define features and target
X = df.drop(columns=['manager_rating_given'])
y = df['manager_rating_given']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"Training R^2 score: {train_score:.2f}")
print(f"Test R^2 score: {test_score:.2f}")

# Save the trained model as a pickle file
with open('manager_rating_model.pkl', 'wb') as f:
    pickle.dump(model, f)
