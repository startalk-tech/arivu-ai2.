import streamlit as st
from google import genai
import os

# 1. പേജ് സെറ്റിംഗ്സ്
st.set_page_config(
    page_title="Star Talk Technologies",
    page_icon="🚀",
    layout="centered"
)

# 2. പ്രൊഫഷണൽ ഡിസൈൻ (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .stChatMessage { border-radius: 10px; border: 1px solid #eee; }
    .footer { text-align: center; padding: 30px; color: #666; font-family: sans-serif; }
    .hero-box { 
        padding: 30px; 
        background: #f8f9fa; 
        border-radius: 15px; 
        text-align: center; 
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. സൈഡ്‌ബാർ മെനു
with st.sidebar:
    st.title("Menu")
    choice = st.radio("Go to", ["Home", "Arivu AI 2.0", "About Us", "Contact"])

# നിങ്ങളുടെ ലോഗോ ഫയൽ പേര് (നേരത്തെ കണ്ടത് പോലെ)
logo_file = "1776486725261.png"

# --- പേജ് 1: ഹോം പേജ് ---
if choice == "Home":
    if os.path.exists(logo_file):
        st.image(logo_file, use_container_width=True)
    
    st.markdown("""
        <div class="hero-box">
            <h1 style='color: #1E88E5;'>STAR TALK TECHNOLOGIES</h1>
            <p>നിങ്ങളുടെ ജീവിതം എളുപ്പമാക്കാൻ അത്യാധുനിക AI സാങ്കേതികവിദ്യയുമായി ഞങ്ങൾ വരുന്നു.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("ഞങ്ങളുടെ സേവനങ്ങൾ")
    st.write("- **AI Solutions:** നിങ്ങളുടെ സംശയങ്ങൾക്ക് മറുപടി നൽകുന്ന സ്മാർട്ട് അസിസ്റ്റന്റ്.")
    st.write("- **Web Development:** മികച്ച രീതിയിലുള്ള വെബ്സൈറ്റ് നിർമ്മാണം.")
    
    if st.button("Start Chat with Arivu AI"):
        st.info("സൈഡ് മെനുവിൽ നിന്ന് Arivu AI 2.0 തിരഞ്ഞെടുക്കുക.")

# --- പേജ് 2: എഐ ചാറ്റ് ബോട്ട് ---
elif choice == "Arivu AI 2.0":
    st.markdown("<h2 style='text-align: center;'>🧠 ARIVU AI 2.0</h2>", unsafe_allow_html=True)
    st.write("---")
    
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=api_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("How can I help you?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
    except Exception as e:
        st.error("API Key സെറ്റ് ചെയ്തിട്ടില്ല അല്ലെങ്കിൽ ലിമിറ്റ് കഴിഞ്ഞു.")

# --- പേജ് 3: എബൗട്ട് അസ് ---
elif choice == "About Us":
    st.header("About Star Talk")
    st.write("സാങ്കേതികവിദ്യ സാധാരണക്കാരിലേക്ക് എത്തിക്കുക എന്ന ലക്ഷ്യത്തോടെ കണ്ണൂർ ആസ്ഥാനമായി പ്രവർത്തിക്കുന്ന ഒരു സ്റ്റാർട്ടപ്പാണ് **Star Talk Technologies**.")
    st.info("**Founder & Developer:** Vyshak Kannur")
    st.write("ഞങ്ങളുടെ ഓരോ ടൂളുകളും യൂസർമാർക്ക് ഏറ്റവും എളുപ്പത്തിൽ ഉപയോഗിക്കാൻ സാധിക്കുന്ന രീതിയിലാണ് ഡിസൈൻ ചെയ്തിരിക്കുന്നത്.")

# --- പേജ് 4: കോൺടാക്റ്റ് ---
elif choice == "Contact":
    st.header("Contact Us")
    st.write("നിങ്ങൾക്ക് ഞങ്ങളെ ബന്ധപ്പെടാൻ താഴെ പറയുന്ന വിവരങ്ങൾ ഉപയോഗിക്കാം.")
    st.write("📧 Email: contact@startalk.tech")
    st.write("📍 Location: Kannur, Kerala")
    
    with st.form("contact"):
        name = st.text_input("Name")
        msg = st.text_area("Message")
        if st.form_submit_button("Send"):
            st.success("സന്ദേശം ലഭിച്ചു. ഞങ്ങൾ ഉടനെ ബന്ധപ്പെടാം.")

# 4. പ്രൊഫഷണൽ ഫൂട്ടർ (എല്ലാ പേജിലും വരും)
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="footer">
        <p style='margin-bottom: 0;'><b>STAR TALK TECHNOLOGIES</b></p>
        <p style='color: #1E88E5; font-weight: bold;'>Developed by Vyshak Kannur</p>
        <p style='font-size: 12px;'>© 2026 All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True
)
