import streamlit as st
import google.generativeai as genai

# Configure API key
google_api_key = 'AIzaSyAX1lkXIWTStVNYj74wRZ0_wE8-p6k4yBM'
genai.configure(api_key=google_api_key)

# Initialize the model
model_name = 'gemini-pro'  # Replace with the correct model name
try:
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Error initializing the model: {e}")

# Streamlit UI for Chatbot
st.title("Chatbot with Gemini Text Model made by Damodar Bhawsar")
st.write("Welcome to the chatbot! Ask me anything.")

# User input box
user_input = st.text_input("Your Message:", key="user_input")

# Chatbot response logic
if st.button("Send") and user_input.strip():
    try:
        # Generate response from the model
        response = model.generate_content(user_input)
        bot_response = response.text

        # Display the response
        st.write(f"*You:* {user_input}")
        st.write(f"*Bot:* {bot_response}")
    except Exception as e:
        st.error(f"Error generating chatbot response: {e}")