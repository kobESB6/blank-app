import streamlit as st
import time
from utils.auth import create_user

st.set_page_config(page_title="Join ESB", layout="centered")

# --- UI: Branding ---
st.image("media/esb_background.png", use_container_width=True)

# --- Custom Styling ---
st.markdown("""
    <style>
    .form-container {
        background-color: #ffffffdd;
        padding: 3rem;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
        max-width: 600px;
        margin: 2rem auto;
        text-align: center;
    }
    .form-title {
        font-size: 2.5em;
        color: #FF6600;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .form-button {
        background-color: #FF6600;
        color: white;
        padding: 0.8rem 2rem;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .form-button:hover {
        background-color: #cc5200;
        transform: scale(1.05);
    }
    .login-link {
        display: block;
        margin-top: 1.5rem;
        font-size: 0.95rem;
        color: #003366;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Signup Form UI ---
st.markdown('<div class="form-container">', unsafe_allow_html=True)
st.markdown('<div class="form-title">Create Your ESB Account</div>', unsafe_allow_html=True)

name = st.text_input("Full Name")
username = st.text_input("Email or Username")
role = st.selectbox("Choose a Role", ["Athlete", "Coach", "Legend"])
password = st.text_input("Password", type="password")

if st.button("Sign Up", key="signup_button"):
    if not name or not username or not password or role not in ["Athlete", "Coach", "Legend"]:
        st.warning("Please fill in all fields and select a role.")
    else:
        success = create_user(username, password, name, role.lower())
        if success:
            st.session_state.user = {
                "name": name,
                "role": role.lower(),
            }
            st.session_state.logged_in = True
            st.session_state.role = role.lower()

            st.success(f"Welcome to ESB, {name}!")

            with st.spinner("Redirecting..."):
                time.sleep(1.5)
            st.switch_page("pages/RoleRouter.py")  # ✅ Use central router
        else:
            st.error("An account with this username already exists.")

st.markdown('</div>', unsafe_allow_html=True)

# --- Login redirect button ---
if st.button("Already have an account? Log in here"):
    st.switch_page("pages/Login.py")

