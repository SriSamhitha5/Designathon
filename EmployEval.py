import streamlit as st
import pandas as pd


def main():
    st.title("Evaluation")

    with st.form(key='evalForm'):
        col1, col2 = st.columns([3, 0.7])

        with col1:
            goal = st.text_input("Write goal")
        with col2:
            rating = st.number_input("Rating", max_value=5, min_value=1)
        with col1:
            explanation = st.text_area("Write Explanation")
        with col2:
            st.text("Save")
            submit = st.form_submit_button(label='Save Goal')

    if submit:
        st.write("Goal saved!")
        with st.expander("Saved Goals"):
            goals_data = st.session_state.get('goals_data', [])
            goals_data.append({'Goal': goal, 'Explanation': explanation, 'Rating': rating})
            st.dataframe(pd.DataFrame(goals_data))

            # Save the data back to the session state
            st.session_state['goals_data'] = goals_data