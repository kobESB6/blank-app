import streamlit as st
from streamlit_option_menu import option_menu
import app_login



st.set_page_config(
    page_title="Eat Sleep Breathe Sports",
)

class MultiApp:
    def __init__(self):
        self.apps = []  # List of apps

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function,
        })

    def run(self):
        with st.sidebar:   #navigation sidebar
            app = option_menu(
                menu_title='ESB SPORTS',
                options=['Home','about us','Profiles', 'Signup/Login', ],
                icons=['house-fill', 'info-circle', 'person-circle', 'trophy-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == 'Home':
            home.app()
        elif app == 'Signup/Login':
            app_login.app()
        elif app == 'about us':
            aboutUs.app()
        elif app == 'Profiles':
            profile.app()

# Run the app
app_instance = MultiApp()
app_instance.run()