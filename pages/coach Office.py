# --- DISPLAY SAVED PROFILES ---
st.markdown("---")
st.header("📋 All Saved Athlete Profiles")

if st.session_state.profiles:
    cols = st.columns(2)
    for idx, profile in enumerate(st.session_state.profiles):
        with cols[idx % 2]:
            st.markdown(f"### {profile['sport']} - {profile['name']}")
            st.json(profile)
            st.divider()
else:
    st.info("No profiles added yet.")

import streamlit as st

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")