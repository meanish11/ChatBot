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
st.sidebar.title("Features")
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
    
    
    st.markdown("### Make a Question Paper for the Test")
    st.markdown("Generate customized question papers for your students using AI.")
  

   

    # User input
    user_input = st.text_input("Your Question", placeholder="e.g. What courses do you offer?")


    if st.button("Ask"):
     if user_input:
        response = chatbot_response(user_input)

        st.markdown(f"<div style='color: black; font-weight: bold;'>{response}</div>", unsafe_allow_html=True)
        if st.button("Copy Response"):
            st.session_state["copied_text"] = response
            st.success("Response copied to clipboard!")
    else:
        st.warning("Please enter a question.")

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
    




    import streamlit as st

def main():
    
    st.title("AI Question Paper Generator")
    st.write("Generate customized question papers for your students using AI")
    st.sidebar.title("Question Paper Settings")
    language = st.sidebar.radio("Select Language:", ["English", "Hindi"])
    class_level = st.sidebar.selectbox("Select Class:", 
                                      ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10", 
                                       "Class 11", "Class 12", "Undergraduate", "Postgraduate"])
    subjects = get_subjects_for_class(class_level)
    subject = st.sidebar.selectbox("Select Subject:", subjects)
    topic = st.sidebar.text_input("Enter Specific Topic (Optional):", "")
    question_type = st.sidebar.multiselect("Select Question Type(s):", 
                                          ["Objective (MCQ)", "Short Answer", "Long Answer", "Fill in the Blanks", 
                                           "True/False", "Match the Following", "Diagram Based"])
    question_counts = {}
    for q_type in question_type:
        question_counts[q_type] = st.sidebar.number_input(f"Number of {q_type} questions:", 
                                                         min_value=1, max_value=50, value=5)
    difficulty = st.sidebar.select_slider("Difficulty Level:", 
                                         options=["Easy", "Moderate", "Difficult", "Mixed"])
    time_limit = st.sidebar.slider("Time Limit (minutes):", 
                                  min_value=15, max_value=180, value=60, step=15)
    total_marks = st.sidebar.number_input("Total Marks:", min_value=10, max_value=100, value=50)
    additional_instructions = st.sidebar.text_area("Additional Instructions (Optional):", "")
    
    if st.sidebar.button("Generate Prompt"):
        prompt = generate_prompt(language, class_level, subject, topic, question_type, 
                               question_counts, difficulty, time_limit, total_marks, 
                               additional_instructions)
        
        # Display the generated prompt
        st.subheader("Generated Prompt")
        st.code(prompt, language="text")
        
        # Copy button
        st.button("Copy to Clipboard", on_click=lambda: st.write("Prompt copied to clipboard!"))
        
    with st.expander("View Sample Prompts"):
        display_sample_prompts(language)

def get_subjects_for_class(class_level):
    """Return appropriate subjects based on class level"""
    if "11" in class_level or "12" in class_level:
        return ["Physics", "Chemistry", "Biology", "Mathematics", "Computer Science", 
                "English", "Hindi", "History", "Geography", "Political Science", 
                "Economics", "Business Studies", "Accountancy", "Psychology", "Sociology"]
    elif "Undergraduate" in class_level or "Postgraduate" in class_level:
        return ["Physics", "Chemistry", "Biology", "Mathematics", "Computer Science", 
                "English Literature", "Hindi Literature", "History", "Geography", 
                "Political Science", "Economics", "Business Administration", 
                "Accounting", "Psychology", "Sociology", "Engineering", "Medicine"]
    else:
        return ["Science", "Mathematics", "English", "Hindi", "Social Studies", 
                "History", "Geography", "Computer Science", "General Knowledge"]

def generate_prompt(language, class_level, subject, topic, question_types, 
                   question_counts, difficulty, time_limit, total_marks, 
                   additional_instructions):
    """Generate a prompt based on the selected parameters"""
    
    # Start with the appropriate language template
    if language == "English":
        prompt = f"Create a {difficulty.lower()} level question paper for {class_level} {subject}"
    else:  # Hindi
        prompt = f"{class_level} के लिए {subject} का {get_hindi_difficulty(difficulty)} स्तर का प्रश्न पत्र बनाएं"
    if topic:
        if language == "English":
            prompt += f" on the topic of '{topic}'"
        else:
            prompt += f" विषय '{topic}' पर"
    if language == "English":
        prompt += ". Include the following types of questions:\n"
    else:
        prompt += "। निम्नलिखित प्रकार के प्रश्न शामिल करें:\n"
    
    for q_type in question_types:
        count = question_counts[q_type]
        if language == "English":
            prompt += f"- {count} {q_type} questions\n"
        else:
            prompt += f"- {count} {get_hindi_question_type(q_type)}\n"
    if language == "English":
        prompt += f"\nThe question paper should be designed for {time_limit} minutes and for a total of {total_marks} marks."
    else:
        prompt += f"\nप्रश्न पत्र {time_limit} मिनट के लिए और कुल {total_marks} अंकों के लिए डिज़ाइन किया जाना चाहिए।"
    if additional_instructions:
        if language == "English":
            prompt += f"\n\nAdditional instructions: {additional_instructions}"
        else:
            prompt += f"\n\nअतिरिक्त निर्देश: {additional_instructions}"
    if language == "English":
        prompt += "\n\nPlease format the question paper properly with sections, question numbers, and marks distribution. Include clear instructions for students at the beginning."
    else:
        prompt += "\n\nकृपया प्रश्न पत्र को खंडों, प्रश्न संख्याओं और अंक वितरण के साथ उचित रूप से प्रारूपित करें। शुरुआत में छात्रों के लिए स्पष्ट निर्देश शामिल करें।"
    
    return prompt

def get_hindi_difficulty(difficulty):
    """Convert difficulty level to Hindi"""
    hindi_difficulty = {
        "Easy": "आसान",
        "Moderate": "मध्यम",
        "Difficult": "कठिन",
        "Mixed": "मिश्रित"
    }
    return hindi_difficulty.get(difficulty, "मध्यम")

def get_hindi_question_type(q_type):
    """Convert question type to Hindi"""
    hindi_types = {
        "Objective (MCQ)": "बहुविकल्पीय प्रश्न",
        "Short Answer": "लघु उत्तरीय प्रश्न",
        "Long Answer": "दीर्घ उत्तरीय प्रश्न",
        "Fill in the Blanks": "रिक्त स्थान भरें",
        "True/False": "सही/गलत",
        "Match the Following": "निम्नलिखित का मिलान करें",
        "Diagram Based": "चित्र आधारित प्रश्न"
    }
    return hindi_types.get(q_type, q_type)

def display_sample_prompts(language):
    """Display sample prompts for reference"""
    if language == "English":
        st.markdown("### Sample English Prompt")
        st.code("""Create a moderate level question paper for Class 10 Science on the topic of 'Light - Reflection and Refraction'. Include the following types of questions:
- 10 Objective (MCQ) questions
- 5 Short Answer questions
- 3 Long Answer questions
- 4 Diagram Based questions

The question paper should be designed for 90 minutes and for a total of 80 marks.

Please format the question paper properly with sections, question numbers, and marks distribution. Include clear instructions for students at the beginning.""")
    else:
        st.markdown("### नमूना हिंदी प्रॉम्प्ट")
        st.code("""कक्षा 10 के लिए विज्ञान का मध्यम स्तर का प्रश्न पत्र बनाएं विषय 'प्रकाश - परावर्तन और अपवर्तन' पर। निम्नलिखित प्रकार के प्रश्न शामिल करें:
- 10 बहुविकल्पीय प्रश्न
- 5 लघु उत्तरीय प्रश्न
- 3 दीर्घ उत्तरीय प्रश्न
- 4 चित्र आधारित प्रश्न

प्रश्न पत्र 90 मिनट के लिए और कुल 80 अंकों के लिए डिज़ाइन किया जाना चाहिए।

कृपया प्रश्न पत्र को खंडों, प्रश्न संख्याओं और अंक वितरण के साथ उचित रूप से प्रारूपित करें। शुरुआत में छात्रों के लिए स्पष्ट निर्देश शामिल करें।""")

if __name__ == "__main__":
    main()