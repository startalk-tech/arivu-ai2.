import streamlit as st
from google import genai
import os

st.title("Arivu AI 2.0")

# API Key സെറ്റിംഗ്സിൽ നിന്ന് എടുക്കുന്നു
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("എന്താണ് അറിയേണ്ടത്?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
  
