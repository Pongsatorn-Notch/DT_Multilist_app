import streamlit as st

# ตั้งค่าหน้าเพจ (คุณสามารถตั้งค่าได้ในทุกหน้า แต่ st.set_page_config() ควรอยู่ในหน้าแรก)
# สำหรับ Multipage App โดยปกติควรตั้งค่าหลักใน Entrypoint file
# st.set_page_config(page_title="User Profile", page_icon="👤") 

# ส่วนหลักของหน้า Profile
st.markdown("# 👤 User Profile") 
st.write("---") # เส้นคั่น

# ข้อมูลเบื้องต้น
st.header("Basic Information")
st.columns(2)[0].image("https://via.placeholder.com/150", caption="Profile Picture") # รูปโปรไฟล์ปลอม
st.info("คุณสามารถแสดงข้อมูลส่วนตัวที่นี่")

st.markdown("""
- **Name:** John Doe
- **Title:** Data Scientist
- **Email:** john.doe@example.com
- **Location:** Bangkok, Thailand
""")

st.write("---")

# ส่วนทักษะ
st.header("Skills & Expertise")
skills = {
    "Python": 90,
    "Streamlit": 85,
    "Machine Learning": 75,
    "SQL": 70
}

for skill, level in skills.items():
    st.progress(level, text=f"**{skill}** ({level}%)")

st.write("---")

# ส่วนติดต่อ
st.header("Contact")
st.markdown("[Connect on LinkedIn](https://www.linkedin.com/)")
st.markdown("[Visit GitHub](https://www.github.com/)")
