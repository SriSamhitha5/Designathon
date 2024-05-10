import streamlit as st
import pandas as pd
import login as login



# Function to submit rating
def submit_rating():
    st.write("Submit your rating here")
    # Add rating submission form here
   # st.title("Text Dropdown with Values 1, 2, 3, 4, 5")

    # Create a text dropdown with values 1, 2, 3, 4, and 5
    selected_value = st.selectbox("Select a value:", ["1", "2", "3", "4", "5"])
    submitted = st.button("Submit")

    # If submit button is clicked, display the feedback
    if submitted:
        st.write("Rating submitted successfully:")
    # Convert the selected value to integer if needed
    selected_value = int(selected_value)

    st.write("You selected:", selected_value)


# Function to view reportees
def view_reportees():
    st.write("Manager Reportees")

    # Hardcoded data
    data = {
        "Name": ["Samhitha", "kavya", "Karthick","Nikhil","Pavan"],
        "Grade": ["G2", "G3", "G3","G2","G2"],
        "Performance": ["Good", "Excellent", "Excellent","Good","Excellent"],
        "Self Rating":["5","5","5","5","4"]
    }

    # Create a DataFrame from the hardcoded data
    df = pd.DataFrame(data)

    # Add a checkbox column
   # df["Select"] = [False] * len(df)

    # Display the table
    st.write(df)



# Boolean to resize the dataframe, stored as a session state variable
#st.checkbox("Use container width", value=False, key="use_container_width")

#df = view_reportees()

#st.dataframe(df, use_container_width=st.session_state.use_container_width)

# Function to provide feedback
def provide_feedback():
    st.write("Provide feedback here")
    # Add feedback form here
    #st.title("Manager Feedback")

    # Text area for manager feedback
    feedback = st.text_area("Manager Feedback", "Enter your feedback here...")
    submitted = st.button("Submit")

    # If submit button is clicked, display the feedback
    if submitted:
        st.write("Feedback submitted successfully:")
       # st.write(feedback)
    # Display the provided feedback
   # st.write("Feedback provided by the manager:")
   # st.write(feedback)
def logout():


    # Logout button

     #   st.title('Redirect Example')

        if st.button('Logout'):
            login.login_page()


if __name__ == "__main__":
    logout()

# Main function
def main():
    st.title("Manager Page")

    # Navigation menu
    menu = ["Submit Rating", "View Reportees", "Provide Feedback"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Display corresponding page based on menu choice
    if choice == "Submit Rating":
        submit_rating()
    elif choice == "View Reportees":
        view_reportees()
    elif choice == "Provide Feedback":
        provide_feedback()



# Run the main function
if __name__ == "__main__":
    main()
