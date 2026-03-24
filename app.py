import streamlit as st
import pandas as pd

st.subheader("Paulsen")
st.text("This is an AI Assistant that helps you write professional emails with no effort.")

st.divider()

userPrompt = st.text_input(
    'Give as a prompt, let us know what the content of the email should be.',
    placeholder='Insert your prompt'
    )

userMood = st.multiselect(
    'Pick your preference', 
    ['Friendly', 'Professional', 'Aggressive', 'Serious', 'Lovely'],
    max_selections=3,
    accept_new_options=True,
    )