import streamlit as st

def login():
    if "role" not in st.session_state:
        st.session_state.role = "guest"

# -------- Session State Setup --------
if "role" not in st.session_state:
    st.session_state.role = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --------- Login Logic -------------
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Login as", ["Select", "Athlete", "Coach", "Legend"])

    if st.button("Login"):
        if role == "Select":
            st.warning("Please select a role.")
        elif username and password:
            # Simulated authentication check
            st.session_state.role = role.lower()
            st.session_state.logged_in = True
            st.success(f"Welcome, {role}!")
            st.experimental_rerun()
        else:
            st.error("Username and password required.")

# --------- Logout Logic -------------
def logout():
    st.session_state.role = None
    st.session_state.logged_in = False
    st.success("You have been logged out.")
    st.experimental_rerun()

# --------- Athlete Profile Page --------
def athlete_profile():
    st.title("🏃‍♂️ Athlete Profile")
    st.write("Welcome to your Athlete dashboard.")
    # Add athlete-specific widgets here

# --------- Coach Profile Page --------
def coach_profile():
    st.title("📋 Coach Profile")
    st.write("Welcome to your Coach dashboard.")
    # Add coach-specific widgets here

# -------- Main App Routing --------
if not st.session_state.logged_in:
    login()
else:
    st.sidebar.title("Navigation")
    st.sidebar.write(f"Logged in as: **{st.session_state.role.title()}**")

    if st.sidebar.button("Log Out"):
        logout()

    if st.session_state.role == "athlete":
        athlete_profile()
    elif st.session_state.role == "coach":
        coach_profile()
    else:
        st.warning("Unknown role. Please log in again.")
        logout()
