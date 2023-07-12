import streamlit as st;
from datetime import date as dt;
from PIL import Image

st.set_page_config(
    page_title="Calculator",
    page_icon="📱"
)
st.title("Welcome to Streamlit Calculator")
img=Image.open("Cal.png")
st.image(img)

st.sidebar.success("Select a page above")
