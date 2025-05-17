import streamlit as st

import streamlit as st
import json
import os

# --- Load & Save Functions ---
PROFILES_FILE = "profiles.json"

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

# --- FOOTBALL FORM COMPONENT ---
def football_form():
    st.subheader("Football Player Profile")
    name = st.text_input("Name (Football)")
    dob = st.text_input("Date of Birth")
    school = st.text_input("School/Team")
    height = st.text_input("Height")
    weight = st.text_input("Weight")
    forty_time = st.slider("40-Yard Dash Time", 4.3, 5.8, 4.5)
    gpa = st.text_input("GPA")
    position = st.text_input("Position")
    uploads = st.file_uploader("Upload images/articles/honors", accept_multiple_files=True)

    if st.button("Add Football Profile"):
        profile = {
            "sport": "Football",
            "name": name,
            "dob": dob,
            "school": school,
            "height": height,
            "weight": weight,
            "forty_time": forty_time,
            "gpa": gpa,
            "position": position,
            "uploads": [file.name for file in uploads] if uploads else []
        }
        st.session_state.profiles.append(profile)
        save_profiles(st.session_state.profiles)
        st.success(f"Football profile for {name} added!")

# --- BASKETBALL FORM COMPONENT ---
def basketball_form():
    st.subheader("Basketball Player Profile")
    name = st.text_input("Name (Basketball)")
    school = st.text_input("School/Team")
    height = st.text_input("Height")
    weight = st.text_input("Weight")
    ppg = st.number_input("Points Per Game (PPG)", 0.0, 50.0, 10.0)
    apg = st.number_input("Assists Per Game (APG)", 0.0, 20.0, 5.0)
    rpg = st.number_input("Rebounds Per Game (RPG)", 0.0, 20.0, 7.0)
    position = st.text_input("Position")
    uploads = st.file_uploader("Upload highlights/articles", accept_multiple_files=True)

    if st.button("Add Basketball Profile"):
        profile = {
            "sport": "Basketball",
            "name": name,
            "school": school,
            "height": height,
            "weight": weight,
            "ppg": ppg,
            "apg": apg,
            "rpg": rpg,
            "position": position,
            "uploads": [file.name for file in uploads] if uploads else []
        }
        st.session_state.profiles.append(profile)
        save_profiles(st.session_state.profiles)
        st.success(f"Basketball profile for {name} added!")

# --- SOCCER FORM COMPONENT ---
def soccer_form():
    st.subheader("Soccer Player Profile")
    name = st.text_input("Name (Soccer)")
    school = st.text_input("School/Team")
    position = st.text_input("Position")
    goals = st.number_input("Goals Scored", 0, 100, 0)
    assists = st.number_input("Assists", 0, 100, 0)
    foot = st.selectbox("Dominant Foot", ["Left", "Right", "Both"])
    uploads = st.file_uploader("Upload highlights/articles", accept_multiple_files=True)

    if st.button("Add Soccer Profile"):
        profile = {
            "sport": "Soccer",
            "name": name,
            "school": school,
            "position": position,
            "goals": goals,
            "assists": assists,
            "foot": foot,
            "uploads": [file.name for file in uploads] if uploads else []
        }
        st.session_state.profiles.append(profile)
        save_profiles(st.session_state.profiles)
        st.success(f"Soccer profile for {name} added!")

# --- TRACK & FIELD FORM COMPONENT ---
def track_form():
    st.subheader("Track & Field Profile")
    name = st.text_input("Name (Track & Field)")
    school = st.text_input("School/Team")
    event = st.text_input("Event")
    personal_best = st.text_input("Personal Best Time/Distance")
    medals = st.number_input("Number of Medals", 0, 50, 0)
    uploads = st.file_uploader("Upload race footage/articles", accept_multiple_files=True)

    if st.button("Add Track & Field Profile"):
        profile = {
            "sport": "Track & Field",
            "name": name,
            "school": school,
            "event": event,
            "personal_best": personal_best,
            "medals": medals,
            "uploads": [file.name for file in uploads] if uploads else []
        }
        st.session_state.profiles.append(profile)
        save_profiles(st.session_state.profiles)
        st.success(f"Track & Field profile for {name} added!")

# --- MASTER SPORT SELECTOR ---
st.title("🏆 EAT SLEEP BREATHE SPORTS - Athlete Profile Builder")

sport = st.selectbox("Select Sport to Add Profile", ["Football", "Basketball", "Soccer", "Track & Field"])

if sport == "Football":
    football_form()
elif sport == "Basketball":
    basketball_form()
elif sport == "Soccer":
    soccer_form()
elif sport == "Track & Field":
    track_form()

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