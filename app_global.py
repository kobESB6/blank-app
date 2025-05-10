import streamlit as st
try:
    from menu import menu
except ImportError:
    def menu():
        pass  # Placeholder function if menu.py is missing

# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "coach", "super-admin"],
    key="_role",
    on_change=set_role,
)

menu() # Render the dynamic menu!

# Login 
def login():
    st.header("Log in")

if st.button("Log in"):
    st.session_state.role = set_role
    st.rerun
# Log Out 
    def logout():
        st.session_state.role = None
        st.rerun()

# Define Pages
role = st.session_state.role

# Define Accounts - gives each page a title and icon (nav menu)
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

# Define request pages 

request_1 = st.Page(
    "request/request_1.py",
    title="Request 1",
    icon=":material/help:",
    default=(role == "Requester"),  
)

request_2 = st.Page(
    "request/request_2.py", 
    title="Request 2",
    icon=":material/bug_report:"
)
respond_1 = st.Page(
    "respond/respond_1.py",
    title="Respond 1",
    icon=":material/healing:",
    default=(role == "Responder"),
)
respond_2 = st.Page(
    "respond/respond_2.py",
    title="Respond 2",
    icon=":material/handyman:",
    default=(role == "Responder"),
)
admin_1 = st.Page(
    "admin/admin_1.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)
admin_2 = st.Page(
    "admin/admin_2.py",
    title="Admin 2",
    icon=":material/security:",
    default=(role == "Admin"),
)
account_pages = [logout_page, settings]
request_pages = [request_1, request_2]
respond_pages = [respond_1, respond_2]
admin_pages = [admin_1, admin_2]

st.title("Request Manager")

st.logo()# <-- Add Logo Here

# initialize dictionary of pages
page_dict = {}

# Dictionary of allowed pages by checking user roles
if st.session_state.role in ["Requester", "Admin"]:
    page-dict["Request"] = request_pages
if st.session_state.role in ["Respoder", "Admin"]:
     page-dict["Respond"] = respond_pages    
if st.session_state.role =="Admin":
     page-dict["Admin"] = admin_pages    

# Check if the user is allowed access and add the account pages
if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
    
# Fallback to login page if the user isn't logged in
else:
    pg = st.navigation([st.Page(login)])
# Execute the page returned by st. navigation

pg.run()

