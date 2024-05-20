import streamlit as st
import pandas as pd
import math

# Sample user data
def load_user_data(file_path, employee_id):
    df = pd.read_excel(file_path)

    # Convert the DataFrame to a dictionary for easier manipulation
    user_data = {row['EmployeeId']: row.to_dict() for _, row in df.iterrows()}
    # Return data for the specified employee_id
    return user_data[int(employee_id)]

def save_user_data(file_path, data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_excel(file_path, index_label='EmployeeId')

# Function to authenticate users
def authenticate(EmployeeId, password):
    user_data = load_user_data("employee_data.xlsx",EmployeeId)
    if user_data["Password"]==int(password):
        return user_data
    else:

        return None


# Main function
def main():
    # Check if user is logged in
    if 'user' not in st.session_state:
        st.session_state.user = None

    st.title('Performance Management System')

    # Login section
    if st.session_state.user is None:
        st.subheader('Login')
        EmployeeId = st.text_input('EmployeeId')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            user = authenticate(EmployeeId, password)
            if user is not None:
                st.session_state.user = user
                st.experimental_rerun()  # Force UI rerender
            else:
                st.error('Invalid EmployeeId or password. Please try again.')
    else:
        st.subheader(f'Welcome, {st.session_state.user["Name"]} ')
        st.write('You have the following options:')
        if st.session_state.user["IsManager"] == 1:
            st.write('hi Manager')

        else:
            st.sidebar.header(f'Welcome, {st.session_state.user["Name"]}')
            page = st.sidebar.radio('Go to', ['Submit Self-Ratings', 'View Manager Feedback', 'Set Goals for Next Year',
                                              'Give Feedback'])

            if page == 'Submit Self-Ratings':
                user_data = load_user_data("HR_DATA.xlsx", st.session_state.user["EmployeeId"])
                if math.isnan(user_data["SelfRating"]):
                    st.header('Submit Self-Ratings')
                    rating = st.slider('Your Self Rating (1-5)', 1, 5, 3)
                    if st.button('Submit Rating'):
                        st.session_state.user['SelfRating'] = rating
                        st.success('Self-rating submitted!')
                else:
                    st.header('You have already Submitted self ratings')

            elif page == 'View Manager Feedback':
                st.header('View Manager Feedback')
                # manager_feedback = st.session_state.user_info.get('ManagerFeedback', 'No feedback available.')
                # st.text_area('Manager Feedback', manager_feedback, height=100, disabled=True)

            elif page == 'Set Goals for Next Year':
                st.header('Set Goals for Next Year')
                # goals = st.text_area('Your Goals', st.session_state.user_info.get('Goals', ''))
                # if st.button('Set Goals'):
                #     st.session_state.user_info['Goals'] = goals
                #     st.success('Goals set for next year!')

            elif page == 'Give Feedback':
                st.header('Give Feedback about Manager and Teammates')
                # manager_feedback = st.text_area('Feedback for Manager',
                #                                 st.session_state.user_info.get('FeedbackForManager', ''))
                # teammates_feedback = st.text_area('Feedback for Teammates',
                #                                   st.session_state.user_info.get('FeedbackForTeammates', ''))
                # if st.button('Submit Feedback'):
                #     st.session_state.user_info['FeedbackForManager'] = manager_feedback
                #     st.session_state.user_info['FeedbackForTeammates'] = teammates_feedback
                #     st.success('Feedback submitted!')

            # Save changes to Excel
            if st.button('Save Changes'):
                st.session_state.user[st.session_state.user['EmployeeId']] = st.session_state.user
                save_user_data('users.xlsx', st.session_state.user)
                st.success('Changes saved to the file!')


        # Logout button
        if st.button('Logout'):
            st.session_state.user = None
            st.info('Logged out successfully.')
            st.experimental_rerun()  # Force UI rerender


if __name__ == '__main__':
    main()
