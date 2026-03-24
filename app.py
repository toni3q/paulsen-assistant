import os
import time
from dotenv import load_dotenv

import streamlit as st
import pandas as pd

from google import genai
from google.genai import types

st.set_page_config(page_title="Paulsen AI Assistant", layout="centered")

st.title("Paulsen AI")
st.subheader("This is an AI Assistant that helps you write professional emails with no effort.")
st.space("small")

# main prompt feeded to the model.
user_prompt = st.text_input(
    'Give as a prompt, let us know what the content of the email should be.',
    placeholder='Insert your prompt'
)

# keep this in mind since we are not including the mood in the prompt right now.
# we could paste the mood into the prompt and feed it to the model directly, without configuring it each time.
user_mood = st.multiselect(
    'Pick your preference', 
    ['Friendly', 'Professional', 'Aggressive', 'Serious', 'Lovely'],
    max_selections=3,
    accept_new_options=True,
)

def get_output():
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        client = genai.Client(api_key=api_key)
        model_id = "gemini-3-flash-preview"

        response = client.models.generate_content(
            model = model_id,
            contents = user_prompt,
        )

        full_response = response.text
        st.write(full_response)

st.space("small")   
st.button(
    type="primary",
    label="Generate response", 
    help="Generate a response based on your prompt configuration.", 
    on_click=get_output()
)
