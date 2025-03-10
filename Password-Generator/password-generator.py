import streamlit as st
import random 
import string

st.markdown(
    """
    <style>
    .stApp {
        background-color: #E6E6FA;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

# function to generate a password based on the user's preferences
def generator_password(Length, use_digits, use_special):
    characters = string.ascii_letters  #Includes all letters (a-z, A-Z)

    if use_digits:
        characters += string.digits # Adds numbers (0-9) if selected


    if use_special:
        characters += string.punctuation   # Adds special characters (!, @, #, $, %, ^,&, *)


# generate a random password of the sppecified length using the characters define above
    return "".join(random.choice(characters) for _ in range(Length))       


st.title("Password Generator✨⭐")
length = st.slider("Select Password Length",min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generator Password "):
    password = generator_password(length, use_digits, use_special)
    st.write(f"Generated password : `{password}`")


st.write("------------------------------")

st.write("Build with ❤ Zoha Aslam")