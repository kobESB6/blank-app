import streamlit as st
import json
import os

# --- Config ---
st.set_page_config(page_title="Create Profile", layout="centered")
st.title("👤 Create Your Profile")

PROFILES_FILE = "data/profiles.json"  # Adjust path as needed

# --- Helpers ---
def load_profiles():
    if os.path.exists(PROFILES_FILE):
        with open(PROFILES_FILE, "r") as f:
            return json.load(f)
    return []

def save_profiles(profiles):
    with open(PROFILES_FILE, "w") as f:
        json.dump(profiles, f, indent=4)

# --- Check Session ---
if "user" not in st.session_state or "role" not in st.session_state:
    st.warning("⚠️ You must log in first.")
    st.stop()

current_user = st.session_state.user
profiles = load_profiles()

# --- Check for existing profile ---
existing_profile = next((p for p in profiles if p.get("username") == current_user.get("username")), None)

if existing_profile:
    st.info("👀 You're editing an existing profile.")
    default_data = existing_profile
else:
    default_data = {"username": current_user["username"], "role": st.session_state.role}

# --- Form ---
st.subheader("General Info")
name = st.text_input("Full Name", value=default_data.get("name", ""))
school = st.text_input("School / Team", value=default_data.get("school", ""))
sport = st.selectbox("Sport", ["Football", "Basketball", "Soccer", "Track & Field"], index=["Football", "Basketball", "Soccer", "Track & Field"].index(default_data.get("sport", "Football")))

profile_data = {
    "username": current_user["username"],
    "name": name,
    "school": school,
    "sport": sport,
    "role": st.session_state.role
}

# --- Sport Specific Fields ---
if sport == "Football":
    profile_data["height"] = st.text_input("Height", value=default_data.get("height", ""))
    profile_data["weight"] = st.text_input("Weight", value=default_data.get("weight", ""))
    profile_data["forty_time"] = st.slider("40-Yard Dash Time", 4.3, 5.8, float(default_data.get("forty_time", 4.5)))
    profile_data["gpa"] = st.text_input("GPA", value=default_data.get("gpa", ""))
    profile_data["position"] = st.text_input("Position", value=default_data.get("position", ""))

elif sport == "Basketball":
    profile_data["height"] = st.text_input("Height", value=default_data.get("height", ""))
    profile_data["weight"] = st.text_input("Weight", value=default_data.get("weight", ""))
    profile_data["ppg"] = st.number_input("Points Per Game (PPG)", 0.0, 50.0, float(default_data.get("ppg", 10.0)))
    profile_data["apg"] = st.number_input("Assists Per Game (APG)", 0.0, 20.0, float(default_data.get("apg", 5.0)))
    profile_data["rpg"] = st.number_input("Rebounds Per Game (RPG)", 0.0, 20.0, float(default_data.get("rpg", 7.0)))
    profile_data["position"] = st.text_input("Position", value=default_data.get("position", ""))

elif sport == "Soccer":
    profile_data["position"] = st.text_input("Position", value=default_data.get("position", ""))
    profile_data["goals"] = st.number_input("Goals Scored", 0, 100, int(default_data.get("goals", 0)))
    profile_data["assists"] = st.number_input("Assists", 0, 100, int(default_data.get("assists", 0)))
    profile_data["foot"] = st.selectbox("Dominant Foot", ["Left", "Right", "Both"], index=["Left", "Right", "Both"].index(default_data.get("foot", "Right")))

elif sport == "Track & Field":
    profile_data["events"] = default_data.get("events", [])
    new_event = st.text_input("Event")
    personal_best = st.text_input("Personal Best Time/Distance")
    medals = st.number_input("Number of Medals", 0, 50, 0)
    if st.button("Add Event"):
        profile_data["events"].append({
            "event": new_event,
            "personal_best": personal_best,
            "medals": medals
        })

# --- Save Profile ---
if st.button("Save Profile"):
    # Remove old profile if it exists
    profiles = [p for p in profiles if p.get("username") != current_user.get("username")]
    profiles.append(profile_data)
    save_profiles(profiles)
    st.success("✅ Profile saved!")

    # Redirect to dashboard
    st.switch_page(f"pages/{st.session_state.role.capitalize()}Dashboard.py")
