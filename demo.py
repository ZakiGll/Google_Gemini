import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import streamlit as st
import os


load_dotenv(find_dotenv())

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')



def main():

    st.set_page_config(page_title="Radiology LLM", page_icon="⚕️")
    st.header("Let AI build your conclusions ⚕️")
    prompt_input = st.text_area("Enter the observation section:")
    if prompt_input != "":
        prompt_parts = [
          f"You are a radiology assistant, your role is to provide a conclusion for the radiology report based on the medical observation.\nPatient's Radiology Observation: {prompt_input}"
]
        conclusion =  model.generate_content(prompt_parts)
        with st.expander("Conclusion"):
            st.write(conclusion.text)


if __name__ == '__main__':
    main()


