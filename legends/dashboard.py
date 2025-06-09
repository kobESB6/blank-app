import streamlit as st

# --- Authentication & Role Guard ---
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("🔒 You must be logged in to access this page.")
    st.stop()

if st.session_state.role != "legend":
    st.error("⛔ Access denied. This dashboard is for Legends only.")
    st.stop()

# --- Page Config & Greeting ---
st.set_page_config(page_title="Legend Dashboard", layout="wide")
st.title("🏆 Legend Dashboard")

user_name = st.session_state.user.get("name", "Legend")
st.markdown(f"Welcome, **{user_name}**! 👋")

# --- Upload Highlights Section ---
st.subheader("🎥 Upload Highlights & Stories")
st.info("This section will allow you to upload video clips, accolades, and personal stories.")
st.file_uploader("Upload your media", type=["mp4", "mov", "jpg", "png"], key="legend_upload")

# --- Mentoring Placeholder ---
st.subheader("👥 Mentor Athletes (Coming Soon)")
st.warning("We're working on a mentoring feature to help you connect with athletes!")

# --- Career Achievements Placeholder ---
st.subheader("🏅 Career Achievements")
st.success("Badges, awards, and legacy highlights will appear here.")
