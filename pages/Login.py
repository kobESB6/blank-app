import streamlit as st
import time
from utils.auth import authenticate  # your own logic

# --- Form UI ---
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

username = st.text_input("Email or Username")
password = st.text_input("Password", type="password")
remember = st.checkbox("Remember me")

if st.button("Log In", key="login_button"):
    user = authenticate(username, password)
    if user:
        st.success(f"Welcome back, {user['name']}!")

        # Save session state
        st.session_state.user = user
        st.session_state.role = user["role"]
        st.session_state.logged_in = True
        if remember:
            st.session_state.remember = True

        # Redirect to proper dashboard
        with st.spinner("Redirecting..."):
            time.sleep(1.5)

        role = user["role"].lower()
        if role == "athlete":
            st.switch_page("pages/AthleteDashboard.py")
        elif role == "coach":
            st.switch_page("pages/CoachDashboard.py")
        elif role == "legend":
            st.switch_page("pages/LegendDashboard.py")
        else:
            st.error("Unknown role. Cannot continue.")
    else:
        st.error("Invalid username or password.")

st.markdown('</div>', unsafe_allow_html=True)
