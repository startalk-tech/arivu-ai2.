import streamlit as st
from google import genai
import os

# 1. പേജ് സെറ്റിംഗ്സ്
st.set_page_config(
    page_title="Star Talk Technologies",
    page_icon="🚀",
    layout="centered"
)

# 2. സൈഡ്‌ബാർ മെനു (ഇതാണ് മെയിൻ വെബ്സൈറ്റ് ആക്കുന്നത്)
with st.sidebar:
    st.markdown("### Star Talk Navigation")
    choice = st.radio("Go to:", ["🏠 Home", "🧠 Arivu AI 2.0", "ℹ️ About Us", "📞 Contact"])

# ലോഗോ ഫയൽ പേര് ശ്രദ്ധിക്കുക
logo_file = "1776486725261.png"

# --- 1. ഹോം പേജ് ---
if choice == "🏠 Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(logo_file):
            st.image(logo_file, use_container_width=True)
        else:
            st.header("Star Talk Technologies")
    
    st.markdown("<h1 style='text-align: center;'>Welcome to Star Talk Technologies</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
    ### ഞങ്ങളെക്കുറിച്ച്
    സാങ്കേതികവിദ്യയുടെ സഹായത്തോടെ നിങ്ങളുടെ പ്രശ്നങ്ങൾ പരിഹരിക്കാൻ ഞങ്ങൾ ശ്രമിക്കുന്നു. 
    ഞങ്ങളുടെ ഏറ്റവും പുതിയ എഐ ടൂളാണ് **Arivu AI 2.0**.
    
    **നിങ്ങൾക്ക് ഇപ്പോൾ ചെയ്യാൻ കഴിയുന്നവ:**
    - ഇടത് വശത്തെ മെനുവിൽ നിന്ന് **Arivu AI 2.0** തിരഞ്ഞെടുത്ത് ചാറ്റ് ചെയ്യാം.
    - ഞങ്ങളുടെ സേവനങ്ങളെക്കുറിച്ച് **About Us** പേജിൽ വായിക്കാം.
    """)

# --- 2. എഐ ചാറ്റ് പേജ് ---
elif choice == "🧠 Arivu AI 2.0":
    st.markdown("<h2 style='text-align: center;'>Arivu AI 2.0</h2>", unsafe_allow_html=True)
    st.write("---")
    
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=api_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ask anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    except:
        st.error("API Key സെറ്റ് ചെയ്തിട്ടില്ല. Streamlit Secrets പരിശോധിക്കുക.")

# --- 3. എബൗട്ട് പേജ് ---
elif choice == "ℹ️ About Us":
    st.header("About Star Talk Technologies")
    st.write("Founder & Developer: **Vyshak Kannur**")
    st.write("Location: **Kannur, Kerala**")
    st.info("സാങ്കേതികവിദ്യ സാധാരണക്കാരിലേക്ക് എത്തിക്കുക എന്നതാണ് ഞങ്ങളുടെ ലക്ഷ്യം.")

# --- 4. കോൺടാക്റ്റ് പേജ് ---
elif choice == "📞 Contact":
    st.header("Contact Us")
    st.write("Email: contact@startalk.tech")
    st.write("ഞങ്ങളെ സോഷ്യൽ മീഡിയയിലൂടെയും ബന്ധപ്പെടാവുന്നതാണ്.")

# ഫൂട്ടർ
st.markdown("<br><hr><p style='text-align: center;'>© 2026 Star Talk Technologies | Developed by Vyshak Kannur</p>", unsafe_allow_html=True)
