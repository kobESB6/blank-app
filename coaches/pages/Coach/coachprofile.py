import streamlit as st

st.set_page_config(page_title="Coach Dashboard", layout="wide")

st.title("🏈 Coach Dashboard")
st.markdown("Welcome, Coach! Here's a grid view of all your athletes.")

# Sample fallback data
if "profiles" not in st.session_state:
    st.session_state.profiles = [
        {"name": "Jordan Allen", "sport": "Basketball", "position": "Guard"},
        {"name": "Taylor Reed", "sport": "Track", "event": "100m Dash"},
        {"name": "Chris Moore", "sport": "Soccer", "position": "Midfielder"},
        {"name": "Avery Green", "sport": "Football", "position": "QB"},
        {"name": "Morgan Lee", "sport": "Tennis", "rank": "State 5"},
        {"name": "Skylar Rose", "sport": "Swimming", "event": "Butterfly"},
        {"name": "Dakota West", "sport": "Baseball", "position": "Catcher"},
        {"name": "Kai Woods", "sport": "Wrestling", "weight": "145 lbs"},
        {"name": "Remy Fox", "sport": "Volleyball", "position": "Setter"},
    ]

# --- Grid Layout with 5 Columns ---
st.markdown("---")
st.header("📋 Athlete Profiles")

if st.session_state.profiles:
    cols = st.columns(5)  # 5-column layout
    for idx, profile in enumerate(st.session_state.profiles):
        with cols[idx % 5]:
            with st.container(border=True):
                st.markdown(f"**{profile.get('sport', 'Sport')}**")
                st.markdown(f"**{profile.get('name', 'Name')}**")
                st.json(profile)
else:
    st.info("No athlete profiles added yet.")

