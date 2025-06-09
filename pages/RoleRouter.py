import streamlit as st

# Import dashboards from folders
from athlete.dashboard import show_athlete_dashboard
from coach.dashboard import show_coach_dashboard
from legend.dashboard import show_legend_dashboard

# --- Ensure session is valid ---
if "role" not in st.session_state or not st.session_state.get("logged_in"):
    st.error("🚫 Access Denied. Please log in first.")
    st.stop()

# --- Role-based Dashboard Routing ---
role = st.session_state.role.lower()

if role == "athlete":
    show_athlete_dashboard()
elif role == "coach":
    show_coach_dashboard()
elif role == "legend":
    show_legend_dashboard()
else:
    st.error("🚫 Unknown role. Please log in again.")
    st.session_state.clear()
