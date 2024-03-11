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

st.title("My garally")
st.markdown("---")
st.markdown("Google Drive上の特定のタグを持つ写真をAPIで取得して、一覧を表示する予定")
