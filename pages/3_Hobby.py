import streamlit as st
import pandas as pd

# ส่วนหลักของหน้า Hobby
st.markdown("# 🕹️ My Hobbies & Interests") 
st.write("---") 




# งานอดิเรกหลัก
st.header("Major Hobbies")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎮 Gaming")  
    st.write("ชอบการเล่นวิดีโอเกมหลายประเภท โดยเฉพาะเกมแนว Strategy และ RPG") 
    st.code("Platform: PC (Steam, Epic), Console: PS5") 

with col2:
    st.subheader("💻 Coding & Tech Projects")
    st.write("การเรียนรู้เทคโนโลยีใหม่ๆ และสร้างโปรเจกต์เล็กๆ ด้วย Python และ Streamlit")
    st.code("Skills: Python, Streamlit, Data Viz")

st.write("---")

# งานอดิเรกอื่นๆ ในรูปแบบตาราง
st.header("Other Interests")

data = {
    # อัปเดตตาราง หาก Gaming กลายเป็นงานอดิเรกหลักแล้ว
    'Hobby': ['Reading', 'Cooking', 'Hiking', 'Watching Movies'], 
    'Frequency': ['Weekly', 'Daily', 'Monthly', 'Occasionally'],
    'Note': ['Sci-fi and Fantasy', 'Thai and Italian food', 'Exploring local trails', 'Action and Sci-fi genres']
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True, hide_index=True)

st.write("---")

# ส่วนที่ให้ผู้ใช้โต้ตอบ
st.header("What's your favorite hobby?")
user_hobby = st.text_input("Enter your hobby here:")

if user_hobby:
    st.success(f"That's great! **{user_hobby}** sounds like fun.")
