import streamlit as st
import pathlib

st.set_page_config(page_title="Price Comparison App", layout="wide")

# Load your HTML file
html_data = pathlib.Path("mini.html").read_text(encoding="utf-8")

# Remove Streamlit padding/margins
st.markdown(
    """
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }
        iframe {
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Render HTML full width & full height
st.components.v1.html(html_data, height=2000, scrolling=True)
