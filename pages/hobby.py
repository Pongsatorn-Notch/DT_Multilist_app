import streamlit as st
import pandas as pd

# ส่วนหลักของหน้า Hobby
st.markdown("# 🎨 My Hobbies & Interests")
st.write("---") 

# งานอดิเรกหลัก
st.header("Major Hobbies")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📸 Photography")
    st.write("ชอบการถ่ายภาพวิวทิวทัศน์ โดยเฉพาะช่วง Golden Hour และการถ่ายภาพบุคคล")
    # คุณสามารถเพิ่มรูปภาพได้
    # st.image("path/to/my_photo.jpg", caption="Sunrise Shot")
    st.code("Camera: Sony A7 IV, Lens: 24-70mm")

with col2:
    st.subheader("💻 Coding & Tech Projects")
    st.write("การเรียนรู้เทคโนโลยีใหม่ๆ และสร้างโปรเจกต์เล็กๆ ด้วย Python และ Streamlit")
    st.code("Skills: Python, Streamlit, Data Viz")

st.write("---")

# งานอดิเรกอื่นๆ ในรูปแบบตาราง
st.header("Other Interests")

data = {
    'Hobby': ['Reading', 'Cooking', 'Hiking', 'Gaming'],
    'Frequency': ['Weekly', 'Daily', 'Monthly', 'Occasionally'],
    'Note': ['Sci-fi and Fantasy', 'Thai and Italian food', 'Exploring local trails', 'Strategy games']
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True, hide_index=True)

st.write("---")

# ส่วนที่ให้ผู้ใช้โต้ตอบ (Interactive element)
st.header("What's your favorite hobby?")
user_hobby = st.text_input("Enter your hobby here:")

if user_hobby:
    st.success(f"That's great! **{user_hobby}** sounds like fun.")
