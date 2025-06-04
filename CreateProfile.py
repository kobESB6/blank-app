# pages/CreateProfile.py
import streamlit as st
import json
import os

# ----- Setup -----
st.set_page_config(page_title="Create Profile", layout="centered")
st.title("👤 Create Your Profile")

PROFILES_FILE = "profiles.json"

# ----- Load / Save Profiles -----
def load_profiles():
    if os.path.exists(PROFILES_FILE):
        with open(PROFILES_FILE, "r") as f:
            return json.load(f)
    return []

def save_profiles(profiles):
    with open(PROFILES_FILE, "w") as f:
        json.dump(profiles, f, indent=4)

if "profiles" not in st.session_state:
    st.session_state.profiles = load_profiles()

# ----- General Info -----
st.subheader("General Information")
name = st.text_input("Full Name")
school = st.text_input("School / Team")
sport = st.selectbox("Sport", ["Football", "Basketball", "Soccer", "Track & Field"])

# ----- Sport-Specific Fields -----
profile_data = {
    "name": name,
    "school": school,
    "sport": sport,
}

if sport == "Football":
    profile_data["height"] = st.text_input("Height")
    profile_data["weight"] = st.text_input("Weight")
    profile_data["forty_time"] = st.slider("40-Yard Dash Time", 4.3, 5.8, 4.5)
    profile_data["gpa"] = st.text_input("GPA")
    profile_data["position"] = st.text_input("Position")

elif sport == "Basketball":
    profile_data["height"] = st.text_input("Height")
    profile_data["weight"] = st.text_input("Weight")
    profile_data["ppg"] = st.number_input("Points Per Game (PPG)", 0.0, 50.0, 10.0)
    profile_data["apg"] = st.number_input("Assists Per Game (APG)", 0.0, 20.0, 5.0)
    profile_data["rpg"] = st.number_input("Rebounds Per Game (RPG)", 0.0, 20.0, 7.0)
    profile_data["position"] = st.text_input("Position")

elif sport == "Soccer":
    profile_data["position"] = st.text_input("Position")
    profile_data["goals"] = st.number_input("Goals Scored", 0, 100, 0)
    profile_data["assists"] = st.number_input("Assists", 0, 100, 0)
    profile_data["foot"] = st.selectbox("Dominant Foot", ["Left", "Right", "Both"])

elif sport == "Track & Field":
    profile_data["events"] = []
    st.markdown("### Add Events")
    event = st.text_input("Event")
    personal_best = st.text_input("Personal Best Time/Distance")
    medals = st.number_input("Number of Medals", 0, 50, 0)
    if st.button("Add Event"):
        profile_data["events"].append({
            "event": event,
            "personal_best": personal_best,
            "medals": medals
        })

# ----- Submit -----
if st.button("Save Profile"):
    st.session_state.profiles.append(profile_data)
    save_profiles(st.session_state.profiles)
    st.success("✅ Profile saved successfully!")
    st.switch_page(f"pages/{st.session_state.role.capitalize()}Dashboard.py")
