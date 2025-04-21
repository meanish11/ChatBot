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
page = st.sidebar.radio("Go to", ["Home", "About"])

# Home Page
if page == "Home":
    # st.set_page_config(layout="wide")
    st.title("🏫 Aadarsh Coaching Center - Chaksikander, Hajipur")
    st.markdown("""
        Welcome to the **Aadarsh Coaching Center**!  
        We are dedicated to providing quality education and guidance to help students achieve their academic goals.  
        Feel free to ask any questions or get assistance using our chatbot below.
    """)
    st.image("https://via.placeholder.com/800x300.png?text=Aadarsh+Coaching+Center", use_column_width=True)
    
    st.markdown("### Get Assistance from Our AI Chatbot")
    st.markdown("Ask any questions related to our coaching services, courses, or general queries!")

    st.markdown("### Chat with our AI Chatbot")
    st.markdown("Ask anything related to our coaching services, courses, or general queries!")

    # User input
    user_input = st.text_input("Your Question", placeholder="e.g. What courses do you offer?")

    # Button to send the query
    if st.button("Ask"):
     if user_input:
        # Get the chatbot response
        response = chatbot_response(user_input)
        
        # Display the response (non-editable)
        st.text_area("Chatbot Response", value=response, height=250, disabled=True)
        
        # Add a copy button
        if st.button("Copy Response"):
            st.session_state["copied_text"] = response
            st.success("Response copied to clipboard!")
    else:
        st.warning("Please enter a question.")

# About Page
elif page == "About":
    st.title("About Aadarsh Coaching Center")
    st.markdown("""
        **Aadarsh Coaching Center** is located in **Chaksikander, Hajipur**.  
        We specialize in providing top-notch coaching for students from various academic backgrounds.  
        ### Why Choose Us?
        - Experienced and qualified faculty
        - Comprehensive study materials
        - Regular tests and performance analysis
        - Personalized attention to each student
        - Affordable fees
        ### Our Services
    
        - **Personalized Coaching**: Tailored coaching sessions to meet individual student needs.
        - **Online Classes**: Flexible online classes for students who prefer remote learning.
        - **Study Materials**: Comprehensive study materials and resources for all subjects.
        - **Mock Tests**: Regular mock tests to assess student performance and readiness.
        - **Doubt Clearing Sessions**: Dedicated sessions to clear student doubts and queries.
        ### Courses Offered:
        - Class 1 to 5 (All Subjects)
        - Class 6 to 12 (All Subjects)
        - Competitive Exams (JEE, NEET, etc.)
        - Spoken English and Personality Development
        ### Contact Us:
        - **Address**: Chaksikander, Hajipur, Bihar
        - **Phone**: +91-9876543210
        - **Email**: info@aadarshcoaching.com
    """)
    st.image("https://via.placeholder.com/800x300.png?text=About+Aadarsh+Coaching+Center", use_column_width=True)