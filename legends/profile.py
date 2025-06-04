import streamlit as st

def show_legend_profile():
    st.title("🏆 Legend Profile")
    st.markdown(f"Welcome, **{st.session_state.user['name']}**!")

    st.subheader("🎥 Upload Legacy Content")
    # Add file uploader

    st.subheader("👥 Mentoring Opportunities")
    st.info("Mentor features coming soon!")

    st.subheader("🏅 Achievements")
    # List or showcase career achievements

