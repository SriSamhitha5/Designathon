from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the synthetic data
df = pd.read_excel('synthetic_data.xlsx')


