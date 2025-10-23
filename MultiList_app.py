# streamlit_app.py (Final version)

import streamlit as st

# 1. Configuration 
st.set_page_config(
    page_title="My Multipage App",
    page_icon="👋",
    layout="wide"
)

# --- 2. Define Home Page Content as a Function ---
def home_page_content():
    st.title("Welcome to the Home Page 🏡")
    st.markdown("---") 
    st.header("App Navigation Demo")
    st.write("การนำทางทำงานได้แล้ว กรุณาเลือกหน้าจากแถบด้านข้าง (Sidebar).")
    st.markdown("""
    ### Pages Available:
    - **Profile:** ข้อมูลส่วนตัว
    - **Hobby:** งานอดิเรก
    """)

# 3. Define Pages with st.Page()
pages = [
    # หน้า Home: เรียกใช้ function ที่สร้างไว้ด้านบน
    st.Page(home_page_content, title="Home", icon="🏠"), 
    
    # หน้าย่อย: ต้องระบุ path ให้ถูกต้อง 
    # (สมมติชื่อไฟล์ใน pages/ คือ profile.py และ hobby.py)
    st.Page("pages/profile.py", title="Profile", icon="👤"), 
    st.Page("pages/hobby.py", title="Hobby", icon="🎮"),
]

# 4. Create Navigation
st.navigation(pages)

# *** ห้ามมีโค้ดเนื้อหาของ Home Page ด้านล่างนี้อีก ***
