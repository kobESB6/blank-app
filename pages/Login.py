import streamlit as st
import time
from utils.auth import authenticate  # ✅ make sure you're importing from utils/auth.py

st.set_page_config(page_title="Login - ESB", layout="centered")

# --- Custom Title Styling ---
st.markdown("""
    <style>
    .form-title {
        font-size: 2.5em;
        color: #FF6600;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="form-title">Log In to Your Account</div>', unsafe_allow_html=True)

# --- Form Inputs ---
username = st.text_input("Email or Username")
password = st.text_input("Password", type="password")
remember = st.checkbox("Remember me")

# --- Form Submission ---
if st.button("Log In", key="login_button"):
    user = authenticate(username, password)
    
    if user:
        st.success(f"Welcome back, {user['name']}!")
        st.session_state.user = user
        st.session_state.role = user["role"]
        st.session_state.logged_in = True
        if remember:
            st.session_state.remember = True

        with st.spinner("Redirecting..."):
            time.sleep(1.5)

        st.switch_page("pages/RoleRouter.py")  # ✅ clean redirect

    else:
        st.error("Invalid username or password.")
