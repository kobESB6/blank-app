import streamlit as st

def show_athlete_dashboard():
    st.set_page_config(page_title="🏃 Athlete Dashboard", layout="wide")
    st.title("🏃 Athlete Dashboard")
    st.markdown(f"Welcome, **{st.session_state.user['name']}**!")

    st.subheader("📊 Performance Metrics")
    st.write("Track your speed, strength, and GPA here.")

    st.subheader("📸 Upload Game Highlights")
    st.file_uploader("Upload video", type=["mp4", "mov"])

    st.subheader("📝 College Interest Form")
    st.write("Fill out forms from interested colleges.")
