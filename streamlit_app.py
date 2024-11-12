import streamlit as st

st.title("ESB Coaches Corner Profile")
st.write(
    
    "This a Direct Access Profile... Limited Access Let's start building this Profile!"
)
st.text_input("Name")
st.text_input("Date of Birth")
st.text_input("Name of School")
st.text_input("Height")
st.text_input("Weight")
add_slider = st.slider("40 time", 4.3, 5.8, (4.3, 5.0)
                       )
st.text_input("GPA")
st.text_input("Postiion")
st.button("Submit")
upload =st.file_uploader("Upload info about Student Athlete images,articles,")
st.camera_input("⚡️Game Action Image")

