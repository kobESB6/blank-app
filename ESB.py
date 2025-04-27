import streamlit as st
import json
import os

# ----- Load CSS -----
def load_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# ----- JSON Profile Storage -----
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

# ----- Navigation -----
page = st.sidebar.radio("Go to", ["Athlete Profiles", "Coach Profiles"])

# ----- EDIT MODE TRACKER -----
if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

# ----- COMPONENTS -----

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

# Initialize session state list for events
import streamlit as st

# Initialize event list
if "track_events" not in st.session_state:
    st.session_state.track_events = []

# Temporary new event inputs stored in separate keys
if "new_event_temp" not in st.session_state:
    st.session_state.new_event_temp = ""
if "new_pb_temp" not in st.session_state:
    st.session_state.new_pb_temp = ""
if "new_medals_temp" not in st.session_state:
    st.session_state.new_medals_temp = 0

def track_form():
    st.subheader("🏃‍♂️ Track & Field Profile")

    # Basic profile inputs
    name = st.text_input("Name (Track & Field)")
    school = st.text_input("School/Team")

    # Existing Events Section
    st.markdown("### 🎯 Events Added:")
    for i, event_data in enumerate(st.session_state.track_events):
        st.text_input(f"Event {i+1}", value=event_data["event"], key=f"event_{i}", disabled=True)
        st.text_input(f"Personal Best {i+1}", value=event_data["personal_best"], key=f"pb_{i}", disabled=True)
        st.number_input(f"Medals {i+1}", min_value=0, max_value=50, value=event_data["medals"], key=f"medals_{i}", disabled=True)

    # Inputs for adding new event
    st.markdown("### ➕ Add New Event")
    new_event = st.text_input("Event", key="new_event_temp")
    new_pb = st.text_input("Personal Best Time/Distance", key="new_pb_temp")
    new_medals = st.number_input("Number of Medals", 0, 50, 0, key="new_medals_temp")

    if st.button("➕ Add Another Event"):
        if new_event and new_pb:
            st.session_state.track_events.append({
                "event": new_event,
                "personal_best": new_pb,
                "medals": new_medals
            })
            # Reset buffer inputs safely
            st.session_state.new_event_temp = ""
            st.session_state.new_pb_temp = ""
            st.session_state.new_medals_temp = 0
        else:
            st.warning("Please fill out the event and personal best fields.")

    # Uploads
    uploads = st.file_uploader("📹 Upload race footage/articles", accept_multiple_files=True)

    if st.button("✅ Add Track & Field Profile"):
        profile = {
            "sport": "Track & Field",
            "name": name,
            "school": school,
            "events": st.session_state.track_events,
            "uploads": [file.name for file in uploads] if uploads else []
        }
        if "profiles" not in st.session_state:
            st.session_state.profiles = []
        st.session_state.profiles.append(profile)

        save_profiles(st.session_state.profiles)
        st.success(f"Track & Field profile for {name} added!")
        st.session_state.track_events = []

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


#-----COACHES PROFILE------
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

# ----- DISPLAY CARDS -----
def display_profiles(role_type):
    st.markdown("<div class='profile-grid'>", unsafe_allow_html=True)
    for idx, profile in enumerate(st.session_state.profiles):
        if profile.get("role", "athlete") != role_type:
            continue
        with st.container():
            st.markdown("<div class='profile-card'>", unsafe_allow_html=True)
            st.markdown(f"**Name:** {profile.get('name')}")
            if profile.get("sport"):
                st.markdown(f"**Sport:** {profile.get('sport')}")
            if profile.get("school"):
                st.markdown(f"**School/Team:** {profile.get('school')}")
            if profile.get("position"):
                st.markdown(f"**Position:** {profile.get('position')}")
            if profile.get("forty"):
                st.markdown(f"**40 Time:** {profile.get('forty')}s")
            if profile.get("team"):
                st.markdown(f"**Team:** {profile.get('team')}")
            if profile.get("years"):
                st.markdown(f"**Experience:** {profile.get('years')} years")
            if profile.get("philosophy"):
                st.markdown(f"**Philosophy:** {profile.get('philosophy')}")
            if profile.get("uploads"):
                st.write("📂 Uploaded:")
                for f in profile["uploads"]:
                    st.markdown(f"- {f}")

            col1, col2 = st.columns(2)
            if col1.button("📝 Edit", key=f"edit_{idx}"):
                st.session_state.edit_index = idx
            if col2.button("🗑️ Delete", key=f"del_{idx}"):
                st.session_state.profiles.pop(idx)
                save_profiles(st.session_state.profiles)
                st.experimental_rerun()
            st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----- MAIN VIEW -----
if page == "Coach Profiles":
    st.markdown("<h2 class='sub-title'>Create & Manage Coach Profiles</h2>", unsafe_allow_html=True)
    coach_form()
    display_profiles("coach")

# ----- Footer -----
st.markdown("<div class='footer'>© 2025 Eat Sleep Breathe Sports — Built with Streamlit</div>", unsafe_allow_html=True)
