import streamlit as st
from athletes import dashboard as athlete_dashboard
from coaches import dashboard as coach_dashboard
from legends import profile as legend_profile

st.set_page_config(page_title="ESB Dashboard", layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must be logged in to access this page.")
    st.stop()

role = st.session_state.role

if role == "athlete":
    athlete_dashboard.show_dashboard()
elif role == "coach":
    coach_dashboard.show_dashboard()
elif role == "legend":
    legend_profile.show_legend_profile()
else:
    st.error("Unknown role.")

