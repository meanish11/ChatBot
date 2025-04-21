# -*- coding: utf-8 -*-
# Import necessary libraries
import google.generativeai as gemini
import streamlit as st

# Set your API key
api_key = "AIzaSyBsKmiBNfOvZDiXVEfyyazb4CeEKBuE27w"  # Replace with your actual API key

# Configure the Gemini API
gemini.configure(api_key=api_key)

# Initialize the Gemini model
model = gemini.GenerativeModel("gemini-2.0-flash")

# Start a persistent chat session
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hi, how are you?"},
        {"role": "model", "parts": "Hello! I'm here to assist you with anything you need. Feel free to ask me anything."},
    ]
)

# Function to handle user input and get model response
def chatbot_response(user_input):
    try:
        response = chat.send_message(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Chatbot"])

# Home Page
if page == "Home":
    st.title("🤖 General-Purpose Chatbot")
    st.markdown("""
        Welcome to the **General-Purpose Chatbot**!  
        This chatbot is designed to assist you with any questions or topics you want to discuss.  
        Simply type your question, and the chatbot will provide you with a response.
    """)
    st.image("https://via.placeholder.com/800x300.png?text=AI+Chatbot", use_column_width=True)

# About Page
elif page == "About":
    st.title("About the Chatbot")
    st.markdown("""
        The **General-Purpose Chatbot** is powered by **Google's Gemini AI**.  
        It uses advanced natural language processing to understand your queries and provide accurate, helpful responses.  
        ### Features:
        - Answer general questions
        - Assist with various topics
        - Provide conversational responses
        - Always ready to chat!
    """)
    st.image("https://via.placeholder.com/800x300.png?text=About+Chatbot", use_column_width=True)

# Chatbot Page
elif page == "Chatbot":
    st.title("Chat with the AI Chatbot")
    st.markdown("Ask anything you'd like!")

    # User input
    user_input = st.text_input("Your Question", placeholder="e.g. What is the meaning of life?")

    # Button to send the query
    if st.button("Ask"):
        if user_input:
            # Get the chatbot response
            response = chatbot_response(user_input)
            # Display the response
            st.text_area("Chatbot Response", value=response, height=150)
        else:
            st.warning("Please enter a question.")