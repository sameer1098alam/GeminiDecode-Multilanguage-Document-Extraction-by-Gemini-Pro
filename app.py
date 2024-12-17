### Health Management APP
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini API
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model
    response = model.generate_content([input_text, image])
    return response.text

# Input prompt
input_prompt = """
You are an expert at understanding and extracting details from invoices or documents. 
We will upload an image as a document, and you will answer questions or extract information from the image.
"""

# Streamlit Page Configuration
st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro")
st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

# Description Section
text = "Utilizing Gemini Pro AI, this project effortlessly extracts vital information \n\
from diverse multilingual documents, transcending language barriers with precision \n\
and efficiency for enhanced productivity and decision-making."

styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

# File Upload Section
uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

# Display Uploaded Image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Document", use_container_width=True)  # Fixed deprecated warning

    # Submit Button
    if st.button("Extract Information"):
        try:
            # Get response from Gemini AI
            response = get_gemini_response(input_prompt, image)
            st.subheader("Extracted Information:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
