import streamlit as st

# **ห้ามใส่ st.set_page_config() ในหน้าย่อย**

st.markdown("# 👤 User Profile") 
st.write("---") 

# ข้อมูลเบื้องต้น
st.header("Basic Information")

# ใช้ st.columns เพื่อจัดวางรูปภาพและข้อมูลให้อยู่ในแถวเดียวกัน
col_img, col_info = st.columns([1, 2])

with col_img:
    # ใช้ Placeholder URL ที่สั้นและเสถียร
    image_url_placeholder = "https://scontent.fbkk5-6.fna.fbcdn.net/v/t39.30808-1/484031329_3435497556587241_6639043766402110181_n.jpg?stp=dst-jpg_s200x200_tt6&_nc_cat=102&ccb=1-7&_nc_sid=e99d92&_nc_ohc=2m-3oZKrcLoQ7kNvwGG32DI&_nc_oc=AdnRqQq_IP0pctPKCaQK6s0hjO6P1jzFLzPPGzrsSJZsiQX8fF69njxh3WPgl3OnrRM&_nc_zt=24&_nc_ht=scontent.fbkk5-6.fna&_nc_gid=wNBQmVFbQDc8w_RwGbqBAQ&oh=00_AfefCwVzWc3FlRvUxwkKy0d1nBj_0TFW_UIXRo-9zMmNOA&oe=68FFAAF7"
    
    st.image(image_url_placeholder, caption="Profile Picture", width=150)
    
with col_info:
    st.info("ข้อมูลส่วนตัว")
    st.markdown(f"""
    - **Name:** Pongsatorn Bumrer
    - **Major:** Computer science
    - **Email:** s6610886122@pkru.ac.th
    - **Location:** Phuket, Thailand
    """)


st.write("---")

# ส่วนทักษะ
st.header("Skills & Expertise")
skills = {
    "Python": 60,
    "Streamlit": 40,
    "Machine Learning": 50,
    "SQL": 50
}

# ใช้ st.columns เพื่อจัดเรียง progress bar ให้ดูเป็นระเบียบยิ่งขึ้น
skill_cols = st.columns(2) 
skills_list = list(skills.items())

for i, (skill, level) in enumerate(skills_list):
    with skill_cols[i % 2]: # สลับกันแสดงใน 2 คอลัมน์
        st.progress(level, text=f"**{skill}** ({level}%)")

st.write("---")

# ส่วนติดต่อ
st.header("Contact")
st.markdown("[Connect on Facebook](https://www.facebook.com/170147.ElNotch/)")
st.markdown("[Visit GitHub](https://github.com/Pongsatorn-Notch)")
