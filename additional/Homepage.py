import streamlit as st

# Page setup
st.set_page_config(page_title="Eat Sleep Breathe Sports", layout="centered")

# Custom CSS for style
st.markdown("""
    <style>
    .hero-text {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        color: #FF6600;
    }
    .tagline {
        text-align: center;
        font-size: 1.3em;
        margin-bottom: 30px;
    }
    .nav {
        background-color: #003366;
        padding: 1rem;
        color: white;
        text-align: center;
        font-size: 1rem;
    }
    .nav span {
        margin: 0 20px;
    }
    .signup-button {
        background-color: #FF6600;
        color: white;
        padding: 0.6rem 1.5rem;
        font-weight: bold;
        border-radius: 5px;
        text-align: center;
        margin: auto;
        display: block;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<div class='nav'>
    <span>Providing Knowledge</span>
    <span>Cultivating Passion</span>
    <span>Advocates for Life</span>
</div>
""", unsafe_allow_html=True)

# Logo Image (Optional)
st.image("logo_or_mockup.png", use_column_width=True)  # Replace with your own image path

# Hero Section
st.markdown("<div class='hero-text'>EAT SLEEP BREATHE SPORTS</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Providing Knowledge · Cultivating Passion · Advocates for Life</div>", unsafe_allow_html=True)

# Call to Action
st.markdown("<a href='#' class='signup-button'>Get Started</a>", unsafe_allow_html=True)
