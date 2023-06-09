import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage

from pages import stock_tracker, mpt_tutors
# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Logo.jpg')
display = np.array(display)
st.image(display)
st.title("Stock trading Opportunities in Doha")
# col1 = st.columns(1)
# col1, col2 = st.columns(2)
# col1.image(display, width = 400)
# col2.title("Data Storyteller Application")

# Add all your application here
app.add_page("Stock Stats", stock_tracker.app)
app.add_page("Tutor Stats", mpt_tutors.app)


# The main app
app.run()
