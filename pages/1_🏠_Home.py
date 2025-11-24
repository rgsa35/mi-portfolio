import streamlit as st
from PIL import Image

st.title("🏠 Welcome")
st.write("## Hi! I'm Gaby, a future Data Analyst 📊✨")

st.write("""
I am passionate about data analysis, visualization, and building dashboards.
I am currently learning **Python**, **SQL**, **Pandas**, **Streamlit**, and **Power BI**.
""")

# ----- PHOTO -----
col1, col2 = st.columns([1,2])

with col1:
    st.image("assets/profile.png", caption="My photo", width=180)

with col2:
    st.write("### About Me")
    st.write("""
    - 🔍 I enjoy understanding how data works  
    - 📊 I love creating clear and meaningful visualizations  
    - 🎯 I am building my professional portfolio  
    - 💻 Currently learning Python and Streamlit  
    """)

st.success("Feel free to explore the other sections from the menu!")