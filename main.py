import streamlit as st
import os
import json

st.set_page_config(page_title="Eat Sleep Breathe Sports", layout="centered")

# -- Load users from file --
USER_DB = "users.json"

def users_exist():
    return os.path.exists(USER_DB) and os.path.getsize(USER_DB) > 0

# -- UI Elements --
st.image("media/esb_background.png", use_container_width=True)

st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 3em;
        color: #FF6600;
        font-weight: bold;
    }
    .tagline {
        text-align: center;
        font-size: 1.3em;
        color: #003366;
        margin-top: -10px;
    }
    .btn-container {
        text-align: center;
        margin-top: 30px;
    }
    div.stButton > button {
        background-color: #FF6600;
        color: white;
        font-size: 1.1em;
        padding: 0.6em 2em;
        border: none;
        border-radius: 8px;
        transition: 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    div.stButton > button:hover {
        background-color: #e65c00;
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# -- Header --
# -- Header --
st.markdown('<div class="title">EAT SLEEP BREATHE SPORTS</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Providing Knowledge • Cultivating Passion • Advocates for Life</div>', unsafe_allow_html=True)
st.markdown("---")

# -- Button Navigation --
st.markdown('<div class="btn-container">', unsafe_allow_html=True)

# 📌 Single block: Side-by-side buttons only
col1, col2, col3 = st.columns([1, 0.5, 1])  # Adds spacing between buttons
with col1:
    if st.button("Login"):
        st.switch_page("pages/Login.py")
with col3:
    if st.button("Sign Up"):
        st.switch_page("pages/Signup.py")

st.markdown('</div>', unsafe_allow_html=True)
