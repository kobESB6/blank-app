import streamlit as st

def app():
    st.title("🏃 Athlete Dashboard")
    st.success(f"Welcome {st.session_state.username.title()}!")
    st.write("Track your workouts, view progress, and more.")
