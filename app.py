import streamlit as st
import pathlib

# Load your main HTML file
html_data = pathlib.Path("mini.html").read_text(encoding="utf-8")

st.set_page_config(page_title="Price Comparison App", layout="wide")

st.components.v1.html(html_data, height=900, scrolling=True)
