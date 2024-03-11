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

st.title("Who am I?")
co_1, co_2, co_3 = st.columns(3)
with co_1:
    st.image(image := Image.open("images/icon2.jpg"), width=200)
with co_2:
    st.markdown("""
    ##### |Name|
    lxizaxi
    ##### |Now Interest|
    Python, Golang, AWS, ...

    <a href="https://github.com/lxizaxi"><img src="https://simpleicons.org/icons/github.svg" width="30"/></a>
    <a href="https://twitter.com/lxizaxi"><img src="https://simpleicons.org/icons/x.svg" width="30"/></a>
    <a href="https://zenn.dev/lxizaxi"><img src="https://simpleicons.org/icons/zenn.svg" width="30"/></a>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
### AWS Certifications
- [x] AWS Certified Cloud Practitioner
- [x] AWS Certified Solutions Architect - Associate
- [x] AWS Certified SysOps Administrator – Associate
- [x] AWS Certified Developer - Associate
- [x] AWS Certified Solutions Architect - Professional
- [ ] AWS Certified DevOps Engineer - Professional
- [ ] AWS Certified Advanced Networking - Specialty
- [ ] AWS Certified Machine Learning - Specialty
- [x] AWS Certified Security – Specialty
""")