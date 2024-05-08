import pandas as pd
from faker import Faker
import random

# Initialize Faker to generate synthetic data
fake = Faker()

# Define the number of rows in the dataset
num_rows = 1000

# Generate synthetic data
data = {
    'is_billed': [random.choice([0, 1]) for _ in range(num_rows)],
    'avg_working_hours': [random.uniform(6, 8) for _ in range(num_rows)],
    'learning_activities_completed': [random.randint(0, 5) for _ in range(num_rows)],
    'days_worked_last_year': [random.randint(50, 100) for _ in range(num_rows)],
    'company_initiatives_taken': [random.randint(0, 4) for _ in range(num_rows)],
    'employee_self_rating': [random.randint(3, 5) for _ in range(num_rows)]
}

# Generate manager ratings based on employee self ratings
data['manager_rating_given'] = [min(5, max(3, rating + random.randint(-1, 1))) for rating in data['employee_self_rating']]

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Save the data to an Excel file
df.to_excel('synthetic_data.xlsx', index=False)
