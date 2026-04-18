import streamlit as st
from google import genai
import os

# 1. പേജ് സെറ്റിംഗ്സ്
st.set_page_config(
    page_title="ARIVU AI 2.0",
    page_icon="🧠",
    layout="centered"
)

# 2. പ്രൊഫഷണൽ ലുക്ക് നൽകാനുള്ള CSS
st.markdown("""
    <style>
    /* ബാക്ക്ഗ്രൗണ്ട് മാറ്റി വൃത്തിയാക്കുന്നു */
    .stApp { background-color: #FFFFFF; }
    
    /* മെസ്സേജ് ബോക്സുകൾക്ക് ഭംഗി നൽകുന്നു */
    .stChatMessage { 
        border: 1px solid #f0f2f6;
        border-radius: 10px;
        padding: 15px;
    }
    
    /* ഇൻപുട്ട് ബോക്സ് സ്റ്റൈൽ */
    .stChatInput {
        border-radius: 20px;
    }

    /* ഫൂട്ടർ സ്റ്റൈൽ */
    .main-footer {
        text-align: center;
        padding: 40px 0;
        color: #333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ഹെഡർ (ലോഗോ മാത്രം)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # നിങ്ങളുടെ അപ്‌ലോഡ് ചെയ്ത ലോഗോ ഫയൽ പേര് ഇവിടെ നൽകി
    logo_file = "1776486725261.png"
    if os.path.exists(logo_file):
        st.image(logo_file, use_container_width=True)
    else:
        st.markdown("<h1 style='text-align: center; color: #1E88E5;'>ARIVU AI 2.0</h1>", unsafe_allow_html=True)

st.write("---")

# 4. API Key ലോജിക്
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except:
    st.error("API Key missing! Please check Streamlit Secrets.")

# 5. ചാറ്റ് ഹിസ്റ്ററി
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. ചാറ്റ് ഇൻപുട്ട്
if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        if "429" in str(e):
            st.warning("Daily limit reached. Please try again later.")
        else:
            st.error("Technical error occurred.")

# 7. ഫ്രൊഫഷണൽ ഫൂട്ടർ (Developed by Vyshak Kannur)
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="main-footer">
        <hr style="border: 0.5px solid #eee;">
        <p style="letter-spacing: 1px; font-size: 14px; margin-bottom: 5px;">STAR TALK TECHNOLOGIES</p>
        <p style="font-weight: 600; font-size: 16px; color: #1E88E5;">Developed by Vyshak Kannur</p>
        <p style="font-size: 12px; color: #999;">© 2026 All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True
)
