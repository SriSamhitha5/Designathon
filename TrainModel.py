#region headers
import pickle

import joblib
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)
#endregion
#region Global declarations
modeln=''
#endregion
#region plotting graph based on trained model
# developed and tested by Nikhil shravan khobragade,

#region Helper Functions for graphs
def drawgraph(uploaded_file,model):
    #region preparing data
    data = pd.read_excel(uploaded_file, sheet_name=0)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    #endregion
    st.write("Feature Importances:")
    data = pd.read_excel(uploaded_file)
    st.write("Pie Chart:")
    plot_feature_importances_pie(model, data.iloc[:, :-1])
    st.write("Bar Chart:")
    plot_feature_importances_bar(model, data.iloc[:, :-1])

def plot_feature_importances_pie(model, feature_names):
    if isinstance(feature_names, pd.DataFrame):
        feature_names = feature_names.columns

    feature_importances = model.feature_importances_
    sorted_idx = feature_importances.argsort()

    # Create a DataFrame for Plotly Express
    data = {
        "Feature": [feature_names[i] for i in sorted_idx],
        "Importance": feature_importances[sorted_idx]
    }
    df = pd.DataFrame(data)

    # Create a pie chart using Plotly Express
    fig = px.pie(df, values='Importance', names='Feature', title='Feature Importances')

    # Display the plot
    st.plotly_chart(fig)

def plot_feature_importances_bar(model, feature_names):
    if isinstance(feature_names, pd.DataFrame):
        feature_names = feature_names.columns

    feature_importances = model.feature_importances_
    sorted_idx = feature_importances.argsort()

    plt.figure(figsize=(10, 8))
    plt.barh(range(len(sorted_idx)), feature_importances[sorted_idx], align='center')
    plt.yticks(range(len(sorted_idx)), [feature_names[i] for i in sorted_idx])
    plt.xlabel('Feature Importance')
    plt.title('Feature Importances')
    st.pyplot()
#endregion

#region method to choose most efficient algorithm (GNB,Randomforest,kNN)
# developed and tested by Karthick C
#endregion
#endregion

#region for  UI to get input file train model
# developed and tested by  kavya
st.title("ML Model trainer for PMS")

uploaded_file = st.file_uploader("Choose a xlsx file with required data")
st.text('please Make sure that the data is in the format:')
st.info('is_billed	avg_working_hours,learning_activities_completed, days_worked_last_year, company_initiatives_taken, employee_self_rating, manager_rating_given')
if uploaded_file is not None and st.button('Train'):
        df = pd.read_excel(uploaded_file)
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
        st.write(f"Training R^2 score: {train_score:.2f}")
        st.write(f"Test R^2 score: {test_score:.2f}")

        # Save the trained model as a pickle file
        with open('manager_rating_model.pkl', 'wb') as f:
            pickle.dump(model, f)
        drawgraph(uploaded_file,model)










