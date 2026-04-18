import streamlit as st
from google import genai
import os

# 1. പേജ് കോൺഫിഗറേഷൻ
st.set_page_config(page_title="Arivu AI 2.0", page_icon="🧠", layout="centered")

# 2. സ്റ്റൈലിംഗ് (Custom CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stChatMessage { border-radius: 15px; }
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 3. ലോഗോയും ടൈറ്റിലും
col1, col2, col3 = st.columns([1, 1.5, 1])
with col2:
    try:
        # logo.png എന്ന ഫയൽ GitHub-ൽ ഉണ്ടെന്ന് ഉറപ്പുവരുത്തുക
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h3 style='text-align: center;'>Arivu AI 2.0</h3>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Arivu AI 2.0</h1>", unsafe_allow_html=True)

# 4. API Key സെറ്റിംഗ്സിൽ നിന്ന് എടുക്കുന്നു
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error("API Key error! Please check Streamlit Secrets.")

# 5. ചാറ്റ് ഹിസ്റ്ററി സൂക്ഷിക്കാൻ
if "messages" not in st.session_state:
    st.session_state.messages = []

# പഴയ മെസ്സേജുകൾ കാണിക്കാൻ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. ചാറ്റ് ഇൻപുട്ട്
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Something went wrong: {e}")

# 7. ഫൂട്ടർ (Developed by Vaisakh Kannur)
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; color: #555; font-family: sans-serif; padding-bottom: 20px;'>
        <p style='margin-bottom: 0;'>© 2026 Arivu AI 2.0</p>
        <p style='font-weight: bold; color: #1E88E5; font-size: 1.1em;'>Developed by Vyshak Kannur</p>
    </div>
    """,
    unsafe_allow_html=True
)
