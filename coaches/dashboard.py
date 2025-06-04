import streamlit as st

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be logged in to access this page.")
    st.stop()

if st.session_state.role != "coach":
    st.error("Access denied.")
    st.stop()

st.set_page_config(page_title="Coach Dashboard", layout="wide")
st.title("🎓 Coach Dashboard")
st.markdown(f"Welcome, **{st.session_state.user['name']}**!")

st.subheader("🔍 Search Athletes")
# Placeholder: filters, search box

st.subheader("📁 View Scouting Reports")
# Placeholder: athlete profiles, downloads

st.subheader("✉️ Messages / Inquiries")
# Placeholder: inbox or contact form
