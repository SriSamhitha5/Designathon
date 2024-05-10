import streamlit as st
import pandas as pd
import manager as manager
import Menu
# Load data from Excel
def load_data():
    data = pd.read_excel("employee_data.xlsx")
    return data

# Login Page
def login_page():
    st.title("Employee Login")

    # Get username and password input
    employee_id = st.text_input("Employee ID")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        employee_id = 2000078164
        if authenticate(employee_id, 12345):
            user_data = get_user_data(employee_id)
            if user_data["isManager"]:
                st.success("Login Successful as Manager")
                manager_dashboard(user_data)
                manager.main()

            else:
                st.success("Login Successful as Employee")
                employee_dashboard(user_data)
        else:
            st.error("Invalid Employee ID or Password")

# Authentication
def authenticate(employee_id, password):
    data = load_data()
    auth = data[(data["employee_id"] == employee_id) & (data["password"] == password)]
    return not auth.empty

# Get user data
def get_user_data(employee_id):
    data = load_data()
    user_data = data[data["employee_id"] == employee_id].iloc[0]
    return user_data

# Employee Dashboard
def employee_dashboard(user_data):
   Menu.main()
    # Add employee dashboard content here

# st.page_link("login.py", label="Home", icon="🏠")
# st.page_link("login.py", label="login", icon="1️⃣")
# st.page_link("manager.py", label="manager", icon="2️⃣", disabled=True)
# Manager Dashboard
def manager_dashboard(user_data):
    st.title("Manager Dashboard")
    st.write("Welcome, {}".format(user_data["name"]))
    # Add manager dashboard content here

# Main function
def main():
    login_page()

if __name__ == "__main__":
    main()
