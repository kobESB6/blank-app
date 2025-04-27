import streamlit as st
import json
import os

def coach_form():
    st.subheader("🏀 Coach Profile")
    name = st.text_input("Name")
    team = st.text_input("Team / Organization")
    years = st.number_input("Years of Experience", 0, 50, 5)
    philosophy = st.text_area("Coaching Philosophy")
    if st.button("Add Coach Profile"):
        profile = {"role": "coach", "name": name, "team": team,
                   "years": years, "philosophy": philosophy}
        st.session_state.profiles.append(profile)
        save_profiles(st.session_state.profiles)
        st.success(f"Coach {name} profile added.")
# ----- MAIN VIEW -----
if page == "Coach Profiles":
    st.markdown("<h2 class='sub-title'>Create & Manage Coach Profiles</h2>", unsafe_allow_html=True)
    coach_form()
    display_profiles("coach")
