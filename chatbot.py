import os
import openai
import streamlit as st

# Function to generate a response from the chatbot
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


# Streamlit UI
def main():
    st.title("Chatbot")

    # Text input for user input
    user_input = st.text_input("Enter your message:")

    # Button to submit user input
    if st.button("Send"):
        # Display user input
        st.write("You:", user_input)

        # Generate and display chatbot response
        bot_response = generate_response(user_input)
        st.write("Bot:", bot_response)


if __name__ == "__main__":
    main()