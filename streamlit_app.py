import streamlit as st
from google import genai
import os

# 1. പേജ് സെറ്റിംഗ്സ്
st.set_page_config(
    page_title="ARIVU AI 2.0 | Star Talk Technologies",
    page_icon="🧠",
    layout="centered"
)

# 2. ഡിസൈൻ നന്നാക്കാനുള്ള CSS
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    /* ലോഗോയും ടൈറ്റിലും ഭംഗിയാക്കാൻ */
    .header-style { text-align: center; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. ഹെഡർ (ലോഗോയും കമ്പനി പേരും)
# ശ്രദ്ധിക്കുക: GitHub-ൽ 'logo.png' അപ്‌ലോഡ് ചെയ്തിട്ടുണ്ടാകണം
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h2 style='text-align: center;'>ARIVU AI 2.0</h2>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: #555;'>A Product of Star Talk Technologies</h5>", unsafe_allow_html=True)
st.write("---")

# 4. API Key സെറ്റിംഗ്സ്
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error("API Key സെറ്റ് ചെയ്തിട്ടില്ല. Settings-ലെ Secrets പരിശോധിക്കുക.")

# 5. ചാറ്റ് മെസ്സേജുകൾ
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. യൂസർ ചോദ്യം ചോദിക്കുമ്പോൾ
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # AI മറുപടി ജനറേറ്റ് ചെയ്യുന്നു
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        # ലിമിറ്റ് കഴിഞ്ഞാൽ കാണിക്കുന്ന എറർ മെസ്സേജ്
        if "429" in str(e):
            st.warning("Daily Limit കഴിഞ്ഞു. കുറച്ചു സമയം കഴിഞ്ഞ് വീണ്ടും ശ്രമിക്കൂ.")
        else:
            st.error(f"ഒരു ചെറിയ തകരാർ: {e}")

# 7. ഫൂട്ടർ (നിങ്ങളുടെ പേര്)
st.markdown("<br><br><br><hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; padding-bottom: 20px;'>
        <p style='margin: 0; color: #888;'>© 2026 Star Talk Technologies</p>
        <p style='font-weight: bold; color: #1E88E5; font-size: 1.1em;'>Developed by Vyshak Kannur</p>
    </div>
    """,
    unsafe_allow_html=True
)
