import streamlit as st

st.set_page_config(
    page_title="My Multipage App",
    page_icon="👋",
)

# กำหนดหน้าต่างๆ
pages = [
    st.Page("MultiList_app.py", title="Home", icon="🏠"),
    st.Page("pages/1_Profile.py", title="Profile", icon="👤"),
    st.Page("pages/2_Hobby.py", title="Hobby", icon="🎮"),
]

# สร้างเมนูนำทาง
st.navigation(pages)

st.title("Welcome to the Home Page")

st.write("Click on a page in the sidebar to navigate.")
