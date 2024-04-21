import pandas as pd
import pickle
import openai
import streamlit as st
class Employee:
    def __init__(self, name, employee_id, password, manager_id,ismanager):
        self.name = name
        self.employee_id = employee_id
        self.password = password
        self.manager_id = manager_id
        self.is_manager = ismanager
        self.employee_rating = -1
        self.employee_goals = "null"
        self.manager_rating=-1
        self.manager_Feedback ="null"
        self.HOD_rating = -1
        self.Avg_rating = -1



class HRData:
    def __init__(self, employee_id, is_billed, initiative_count, learning_activities, avg_office_time,officedays):
        self.employee_id = employee_id
        self.is_billed = is_billed
        self.initiative_count = initiative_count
        self.learning_activities = learning_activities
        self.avg_office_time = avg_office_time
        self.WFO_days=officedays

# Sample data initialization
employees = [
    Employee("karthick", "E001", "password", "E002", False),
    Employee("Muthu", "E002", "password", "E003", True),
    Employee("Viji", "E003", "password","E004", True),
    Employee("krishna", "E004", "password", "E005", True),
    Employee("bala", "E005", "password","null",True),
    Employee("Nikhil", "E006", "password", "E002", False),
    Employee("kavya", "E007", "password", "E002", False),
    Employee("Samhitha", "E008", "password", "E002", False),
    Employee("pavan", "E009", "password", "E002", False),
]



hr_data = [
    HRData("E001", True, 5, 10, 8,30),
    HRData("E002", True, 3, 8, 7,55),
    HRData("E003", True, 5, 10, 8,65),
    HRData("E004", True, 3, 8, 7,70),
    HRData("E006", True, 5, 10, 8, 65),
    HRData("E007", True, 5, 10, 8, 65),
    HRData("E008", True, 5, 10, 8, 65),
    HRData("E009", True, 5, 10, 8, 65),
]
def display_employee_details(employee):
    print(f"{employee.employee_id:<15} {employee.name}")
# Function to check login credentials
def login():
    employee_id = input("Enter your employee ID: ")
    password = input("Enter your password: ")

    for employee in employees:
        if employee.employee_id == employee_id and employee.password == password:
            return employee
    return None
def generate_response(input_text):
    openai.api_type = "azure"
    openai.api_base = "https://testingkey.openai.azure.com/"
    openai.api_version = "2023-09-15-preview"
    openai.api_key = "35f96eb3ffc04868981139be478f99fa"
    response = openai.Completion.create(
        engine="TestingChatModel",
        prompt=input_text,
        temperature=0.2,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None)
    return response['choices'][0]['text']
def employee_menu(employee):
    print("\nHi " + employee.name + "!")
    print("\nplease select an option..")
    print("1. Submit My Rating/goals")
    print("2. View My feedback")
    print("3. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        if not employee.employee_rating == -1:
            print("You have already submitted your rating.")
            employee_menu(user)
        else:
            employee.employee_rating = int(input("Enter your rating (out of 5): "))
            employee.employee_goals = (input("Enter your comments "))
            print("submitted your rating.")
            employee_menu(user)
    elif choice =="2":
        if not employee.Avg_rating == -1:
            print("PMS is in process")
            employee_menu(user)
        else:
            print(employee.manager_Feedback)
            employee_menu(user)




# Functionality for Employees
def manager_menu(employee):
    isskip=False
    for data in employees:
        for data2 in employees:
            if(data!=employee) and data.manager_id==employee.employee_id:
                if data2.manager_id==data.employee_id:
                    isskip=True

    print("\nHi "+employee.name+"!")
    print("\nplease select an option..")
    print("1. Submit My Rating/goals")
    print("2. View My direct Reportees data and provide feedback")
    if isskip:
        print("3. View My indirect Reportees data and provide feedback")

    print("4. Logout")
    choice = input("Enter your choice: ")

    if choice == "1":
        if not employee.employee_rating==-1:
                print("You have already submitted your rating.")
                manager_menu(user)
        else:
            employee.employee_rating = int(input("Enter your rating (out of 5): "))
            employee.employee_goals=(input("Enter your comments "))
            print("submitted your rating.")
            manager_menu(user)
    elif choice == "2":
        print("employee Data:")
        print("Employee ID    Employee Name")
        for data in employees:
            if data.manager_id == employee.employee_id:
                display_employee_details(data)
        employeeid= (input("Enter employeeid "))
        for data in employees:
            if data.employee_id==employeeid:
                emplo=data
        for data in hr_data:
            if data.employee_id==employeeid:
                HR=data
        print("employee Data")
        print("employee name:"+emplo.name)
        print("employee rating:" + str(emplo.employee_rating))
        print("employee comments:" + emplo.employee_goals)
        print("employee  HR Data")
        print("is employee billed:" + str(HR.is_billed))
        print("employee's average time in office:" +str( HR.avg_office_time))
        print("count of learning activities:" + str(HR.learning_activities))
        print("days worked in last year in office:" + str(HR.WFO_days))
        print("company initiatives participated by employee:" + str(HR.initiative_count))
        input_data = {
            'is_billed': [HR.is_billed],  # Example input values, you can replace them with your own data
            'avg_working_hours': [HR.avg_office_time],
            'learning_activities_completed': [HR.learning_activities],
            'days_worked_last_year': [HR.WFO_days],
            'company_initiatives_taken': [HR.initiative_count],
            'employee_self_rating': [emplo.employee_rating]
        }
        with open('manager_rating_model.pkl', 'rb') as f:
            model = pickle.load(f)
        input_df = pd.DataFrame(input_data)

        # Use the loaded model to make predictions on the input data
        predicted_manager_rating = model.predict(input_df)

        print("Predicted Manager Rating:", predicted_manager_rating[0])
        text="i need you to give short description about employee "+emplo.name+" who is an billed employee worked "+str(HR.WFO_days)+" days in office last year expecting a rating of "+ str(emplo.employee_rating)+" out of 5 company initiatives taken"+str(HR.initiative_count)+", average working hours"+str(HR.avg_office_time)+", learning_activities_completed is"+str(HR.learning_activities)+" give some comments about theis employee within 150 words dont give the data in comment"
        print("description about employee from openai:")
        bot_response = generate_response(text)
        print(bot_response)
        inpu = int(input("Enter your rating (out of 5): "))
        emplo.manager_rating = inpu
        inpu = (input("Enter your comments "))
        emplo.manager_Feedback =inpu
        print("employee rating completed")
        manager_menu(user)
    elif choice == "3":
        print("employee Data:")
        print("Employee ID    Employee Name")
        for data in employees:
            for data2 in employees:
                if (data != employee) and data.manager_id == employee.employee_id:
                    if data2.manager_id == data.employee_id:
                        display_employee_details(data2)
        employeeid= (input("Enter employeeid "))

    elif choice == "4":
        print("Exiting...")
        return

# Main program loop
while True:
    print("\nWelcome to the Performance Management System")
    print("1. Login")
    print("2. Exit")
    option = input("Enter your choice: ")

    if option == "1":
        user = login()
        if user.is_manager:
            manager_menu(user)
        elif not user.is_manager:
            employee_menu(user)

        else:
            print("Invalid credentials. Please try again.")
    elif option == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
