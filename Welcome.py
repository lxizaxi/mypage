import streamlit as st
from PIL import Image

#----------------------Hide Streamlit footer----------------------------
hide_streamlit_style = """
<style>
[data-testid="stToolbar"] {visibility: hidden !important;}
footer {visibility: hidden !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#--------------------------------------------------------------------

st.image(image := Image.open("images/space_shuttle.jpg"), use_column_width=True)
st.title("Welcome 🚀")
st.subheader("Always under construction.")
st.markdown("---")
