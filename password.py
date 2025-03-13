import streamlit as st
import random
import string

# Custom CSS for background and styling
st.markdown(
    """
    <style>
    body {
        background-color: #1E1E1E;
        color: #EAEAEA;
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button {
        background-color: #FF8C00;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #FFA500;
    }
    .stSlider>div {
        color: #FFD700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Password generation function
def generate_password(base_word, length, use_digits, use_special):
    character = string.ascii_letters
    if use_digits:
        character += string.digits
    if use_special:
        character += string.punctuation

    random_part = ''.join(random.choice(character) for _ in range(length - len(base_word)))
    return base_word + random_part

# App Title
st.title("🔐 Password Generator by Aleena Amir")

# User input for personalization
name = st.text_input("Enter Your Name")
birthday = st.text_input("Enter Your Birthday (DDMMYYYY )")

# Combine user inputs for base word
base_word = (name[:3] + birthday[-4:]).strip()
if len(base_word) > 6:
    base_word = base_word[:6]  


length = st.slider("Select Your Password Length", min_value=8, max_value=50, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Generate Password Button
if st.button("Generate Password"):
    if not base_word:
        st.warning("Please enter at least your Name or Birthday for personalization.")
    else:
        password = generate_password(base_word, length, use_digits, use_special)
        st.success(f"Generated Password: `{password}`")
