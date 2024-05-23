import pandas as pd
def saveinhr(employeeid,columnname,value):
    file_path = 'employee_data.xlsx'
    sheet_name = 'Sheet1'  # Change this to your actual sheet name
    employee_id_to_update = employeeid  # Replace with the actual employee ID
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # Locate the employee and update the rating
    df.loc[df['EmployeeId'] == employee_id_to_update, columnname] = value

    # Save the changes back to the Excel file
    df.to_excel(file_path, sheet_name=sheet_name, index=False)

saveinhr('70232','SelfRating',5)