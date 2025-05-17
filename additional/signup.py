import streamlit as st
from utils.auth import create_user

st.set_page_config(page_title="Sign Up", layout="centered")

st.title("Create Your ESB Account")

name = st.text_input("Full Name")
username = st.text_input("Email or Username")
role = st.selectbox("Choose Role", ["Athlete", "Coach", "Legend"])
password = st.text_input("Password", type="password")

if st.button("Sign Up"):
    if create_user(username, password, name, role):
        st.success("Account created! Please log in.")
        st.switch_page("pages/Login.py")
    else:
        st.error("That username is already taken.")
