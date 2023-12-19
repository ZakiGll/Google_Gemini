import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import streamlit as st
import os
import PIL.Image


load_dotenv(find_dotenv())

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')

image = st.file_uploader("Enter the radiology image:")
if image != None:
    img = PIL.Image.open(image)
    st.image(img)

if st.button("Generate"):
   response = model.generate_content(["You are a radiology report generator, you will generate two sections based on the radiology image! The first section will be the observation section where you should provided all the details about the radiology test. The second section contains the conclusion of the report where you give the result of this observation.", img], stream=True)
   response.resolve()
   with st.expander("Report"):
        st.write(response.text)