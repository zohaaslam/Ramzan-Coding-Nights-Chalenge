import streamlit as st  # streamlit is a library for builduing web apps

import streamlit as st

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

# Fuction to convert units based on predefined conversion factors or forulas
def convert_units(value, unit_from, unit_to):
    
    conversion = {
         "meters_kilometers":  0.001,  #1 meter = 0.001 kilometer
        "kilometers_meters": 1000, # kilometer = 1000 meter
        "grams_kilograms": 0.001, #1 gram = 0.001 kilogram
        "kilograms_grams": 1000   #1 kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}" # Generate a key based on the input and output units


    # Logic to convert units
    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        return "Conversion not supported" # return a message if the conversion is not supported
    

st.title("UNIT CONVERTER ⭐🔥") # Set the title of the web app

# user input: numerical value to convert
value = st.number_input("Enter the value:" min_value=1.0, step=1.0)

# dropdown to select unit to convert from
unit_from = st.selectbox("Convert from", ["meters","kilometers","grams","kilograms"])

# dropdown to select unit to convert to
unit_to = st.selectbox("Convert to:", ["meters","kilometers","grams","kilograms"])


# button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to) # call the conversion function
    st.write(f"Converted value: {result}") # display the result


