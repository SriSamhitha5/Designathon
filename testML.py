import pandas as pd
import pickle

# Load the trained model from the pickle file
with open('manager_rating_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Prepare input data (features) for testing
input_data = {
    'is_billed': [0],  # Example input values, you can replace them with your own data
    'avg_working_hours': [7.5],
    'learning_activities_completed': [3.5],
    'days_worked_last_year': [100],
    'company_initiatives_taken': [2],
    'employee_self_rating': [4.2]
}

# Create a DataFrame from the input data
input_df = pd.DataFrame(input_data)

# Use the loaded model to make predictions on the input data
predicted_manager_rating = model.predict(input_df)

print("Predicted Manager Rating:", predicted_manager_rating[0])
