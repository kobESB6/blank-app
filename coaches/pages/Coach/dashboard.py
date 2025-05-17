import streamlit as st

st.set_page_config(page_title="Coach Dashboard", layout="wide")

st.title("📊 Coach Dashboard")
st.markdown("Track and manage your roster below.")

# --- Sample Data (Fallback) ---
if "profiles" not in st.session_state:
    st.session_state.profiles = [
        {
            "name": "Jordan Allen",
            "sport": "Basketball",
            "position": "Guard",
            "image": "https://via.placeholder.com/150"
        },
        {
            "name": "Skylar Rose",
            "sport": "Swimming",
            "event": "Butterfly",
            "image": "https://via.placeholder.com/150"
        },
        {
            "name": "Taylor Reed",
            "sport": "Track",
            "event": "100m Dash",
            "image": "https://via.placeholder.com/150"
        }
    ]

# --- Display Athlete Grid ---
st.markdown("---")
st.subheader("🏅 Athlete Roster")

cols = st.columns(5)
for idx, profile in enumerate(st.session_state.profiles):
    with cols[idx % 5]:
        with st.container(border=True):
            st.markdown(
                f"""
                <div style='
                    background-color: #f0f0f0;
                    border-radius: 10px;
                    padding: 1em;
                    box-shadow: 2px 2px 8px rgba(0,0,0,0.08);
                    text-align: center;
                '>
                    <img src="{profile.get("image")}" width="100" style="border-radius: 50%; margin-bottom: 0.5em;" />
                    <h4 style="margin-bottom: 0.2em;">{profile.get("name", "Athlete")}</h4>
                    <p style="margin: 0; font-weight: bold;">{profile.get("sport", "Sport")}</p>
                    <p style="font-size: 0.85em; color: gray;">
                        {profile.get("position", profile.get("event", ""))}
                    </p>
                    <form action="">
                        <button style="
                            margin-top: 10px;
                            padding: 5px 12px;
                            background-color: #006699;
                            color: white;
                            border: none;
                            border-radius: 5px;
                            cursor: pointer;
                        ">
                            View Profile
                        </button>
                    </form>
                </div>
                """,
                unsafe_allow_html=True
            )
