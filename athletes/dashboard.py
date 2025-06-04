import streamlit as st

# Auth check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be logged in to access this page.")
    st.stop()

if st.session_state.role != "athlete":
    st.error("Access denied.")
    st.stop()

st.set_page_config(page_title="Athlete Dashboard", layout="wide")
st.title("🏋️ Athlete Dashboard")
st.markdown(f"Welcome, **{st.session_state.user['name']}**!")

st.subheader("🏅 Performance Metrics")
# Placeholder: charts, stats

st.subheader("📹 Upload Highlights")
# Placeholder: file upload

st.subheader("📅 Upcoming Events")
# Placeholder: calendar, schedule
