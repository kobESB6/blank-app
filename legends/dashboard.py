import streamlit as st

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be logged in to access this page.")
    st.stop()

if st.session_state.role != "legend":
    st.error("Access denied.")
    st.stop()

st.set_page_config(page_title="Legend Dashboard", layout="wide")
st.title("🏆 Legend Dashboard")
st.markdown(f"Welcome, **{st.session_state.user['name']}**!")

st.subheader("🎥 Upload Highlights & Stories")
# Placeholder: file uploader

st.subheader("👥 Mentor Athletes (Coming Soon)")
# Placeholder for mentoring feature

st.subheader("🏅 Career Achievements")
# Placeholder: badges, awards
