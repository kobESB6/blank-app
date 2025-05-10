import streamlit as st

def app():
    st.title('Welcome to :blue[EAT SLEEP BREATHE SPORTS]')

    # ---------- Session Setup ----------
    if "role" not in st.session_state:
        st.session_state.role = None
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # ---------- If already logged in, show relevant dashboard ----------
    if st.session_state.logged_in:
        st.sidebar.write(f"🔑 Logged in as: **{st.session_state.role.title()}**")
        if st.sidebar.button("Log Out"):
            st.session_state.role = None
            st.session_state.logged_in = False
            st.experimental_rerun()

        # Role-specific dashboards
        if st.session_state.role == "athlete":
            show_athlete_profile()
        elif st.session_state.role == "coach":
            show_coach_profile()
        else:
            st.error("Unknown role. Logging out...")
            st.session_state.logged_in = False
            st.session_state.role = None
            st.experimental_rerun()

    # ---------- If not logged in, show login/signup ----------
    else:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

        st.subheader(f"{choice} as Athlete or Coach")
        selected_role = st.radio("Choose Role", ["Athlete", "Coach"])

        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if choice == 'Sign Up':
            username = st.text_input('Create Unique Name')
            if st.button('Create Profile'):
                if email and password and username:
                    # Simulate successful signup
                    st.session_state.role = selected_role.lower()
                    st.session_state.logged_in = True
                    st.success(f"Welcome, {username.title()} the {selected_role}!")
                    st.experimental_rerun()
                else:
                    st.error("Please fill in all fields.")

        elif choice == 'Login':
            if st.button('Login'):
                if email and password:
                    # Simulate successful login
                    st.session_state.role = selected_role.lower()
                    st.session_state.logged_in = True
                    st.success(f"Welcome back, {selected_role}!")
                    st.experimental_rerun()
                else:
                    st.error("Please enter email and password.")

# ---------- Sample Role-Based Pages ----------
def show_athlete_profile():
    st.title("🏃 Athlete Dashboard")
    st.write("This is your personalized Athlete profile page.")
    st.info("Here you can track workouts, view stats, and update your profile.")

def show_coach_profile():
    st.title("📋 Coach Dashboard")
    st.write("This is your personalized Coach profile page.")
    st.info("Here you can manage athletes, set schedules, and view performance metrics.")
