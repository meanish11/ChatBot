# -*- coding: utf-8 -*-
# Import necessary libraries
import google.generativeai as gemini
import gradio as gr

# Set your API key
api_key = "AIzaSyBsKmiBNfOvZDiXVEfyyazb4CeEKBuE27w"  # Replace with your actual API key

# Configure the Gemini API
gemini.configure(api_key=api_key)

# Initialize the Gemini model
model = gemini.GenerativeModel("gemini-2.0-flash")

# Start a persistent chat session
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hi, I want to know about healthy food choices."},
        {"role": "model", "parts": "Sure! Tell me what you usually eat or what you're looking for."},
    ]
)

# Function to handle user input and get model response
def chatbot_response(user_input):
    # Keywords related to nutrients and health
    health_keywords = [
        "nutrition", "healthy", "food", "diet", "protein", "vitamins", 
        "minerals", "calories", "meal", "health", "diabetes", "sugar", 
        "carbs", "fat", "fiber", "cholesterol", "harmful", "beneficial",
        "nutrition", "healthy", "food", "diet", "protein", "vitamins", 
    "minerals", "calories", "meal", "health", "diabetes", "sugar", 
    "carbs", "fat", "fiber", "cholesterol", "harmful", "beneficial",
    "hydration", "exercise", "wellness", "immunity", "antioxidants", 
    "superfoods", "organic", "wholegrain", "metabolism", "fitness",
    "digestion", "sleep", "mentalhealth", "workout", "lifestyle", 
    "bloodpressure", "cardio", "detox", "meditation", "yoga", "stress"
    ]

    # Check if the user input contains any health-related keywords
    if any(keyword in user_input.lower() for keyword in health_keywords):
        try:
            response = chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "This is irrelevant, I can't answer that."

# Create a Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 🥗 Nutrition-Based Chatbot")
    gr.Markdown("Ask about healthy foods, meal suggestions, or best product recommendations!")

    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(label="Your Question", placeholder="e.g. What should I eat for protein?")
            send_btn = gr.Button("Ask")

        with gr.Column():
            chatbot_output = gr.Textbox(label="Chatbot Response", lines=6)

    # Set button click event
    send_btn.click(fn=chatbot_response, inputs=user_input, outputs=chatbot_output)

# Launch the app
demo.launch()