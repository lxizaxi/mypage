import streamlit as st

#----------------------Hide Streamlit footer----------------------------
hide_streamlit_style = """
<style>
[data-testid="stToolbar"] {visibility: hidden !important;}
footer {visibility: hidden !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#--------------------------------------------------------------------

st.title("Zenn article archives")
st.markdown("---")
st.markdown("zennの記事をAPIで取得して、一覧を表示する予定")
