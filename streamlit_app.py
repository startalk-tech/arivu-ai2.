import streamlit as st
from google import genai
import os

# 1. പേജ് സെറ്റിംഗ്സ്
st.set_page_config(
    page_title="ARIVU AI 2.0",
    page_icon="🧠",
    layout="centered"
)

# 2. ഡിസൈൻ (CSS)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    footer {visibility: hidden;}
    .stChatMessage { border-radius: 12px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. ഹെഡർ (നിങ്ങളുടെ ആ ഫയൽ പേര് വച്ച്)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # നിങ്ങൾ അപ്‌ലോഡ് ചെയ്ത ആ ഫയൽ പേര് ഇവിടെ നൽകി
    logo_file = "1776486725261.png"
    if os.path.exists(logo_file):
        st.image(logo_file, use_container_width=True)
    else:
        st.markdown("<h1 style='text-align: center;'>ARIVU AI 2.0</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: #666;'>A Product of Star Talk Technologies</h5>", unsafe_allow_html=True)
st.write("---")

# 4. API Key ലോജിക്
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except:
    st.error("API Key സെറ്റ് ചെയ്തിട്ടില്ല! Settings-ലെ Secrets പരിശോധിക്കുക.")

# 5. ചാറ്റ് ഹിസ്റ്ററി
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. ചോദ്യം ചോദിക്കാനുള്ള ഭാഗം
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
        if "429" in str(e):
            st.warning("ഇന്നത്തെ ലിമിറ്റ് കഴിഞ്ഞു. അല്പം കഴിഞ്ഞ് വീണ്ടും ശ്രമിക്കൂ.")
        else:
            st.error("എന്തോ ഒരു സാങ്കേതിക തകരാർ! പിന്നീട് ശ്രമിക്കുക.")

# 7. ഫൂട്ടർ (നിങ്ങളുടെ പേരും കമ്പനിയും)
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; padding-bottom: 30px;'>
        <p style='margin-bottom: 0; color: #555;'>© 2026 <b>Star Talk Technologies</b></p>
        <p style='font-weight: bold; color: #1E88E5; font-size: 1.1em;'>Developed by Vyshak Kannur</p>
    </div>
    """,
    unsafe_allow_html=True
)
