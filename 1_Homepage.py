import streamlit as st

st.set_page_config(
    page_title="MultiList App",
    page_icon="👋",
    layout= "wide"
)

def home_page_content():
    # Header Section
    col_main_title, col_icon = st.columns([0.9, 0.1])
    with col_main_title:
        st.title("My Multipage Portfolio Dashboard ✨")
    with col_icon:
        st.markdown("# 🚀") 

    st.markdown("---") 

    # Key Metrics / Status Indicators
    st.header("Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Status", value="Online", delta="Stable")
        st.caption("Application is running on Streamlit.")

    with col2:
        st.metric(label="Total Pages", value="3", delta="Ready to Explore")
        st.caption("Home, Profile, and Hobby.")

    with col3:
        st.metric(label="Streamlit Version", value="1.50.0", delta_color="off")
        st.caption("Latest framework features supported.")

    st.markdown("---") 
    
    # Navigation Guide Section
    st.header("App Guide: Getting Started")

    with st.container(border=True):
        st.subheader("Welcome! Please Explore.")
        st.info("แอปพลิเคชันนี้แสดงความสามารถของ Streamlit ในการสร้างหลายหน้า (Multipage) โดยใช้โครงสร้างไฟล์มาตรฐาน")

        st.markdown(
            """
            ### 📌 Pages Available:
            - **Profile (👤):** ดูข้อมูลส่วนตัวและทักษะที่สำคัญ
            - **Hobby (🎮):** สำรวจงานอดิเรกและความสนใจ
            """
        )
        st.write("คลิกที่เมนูในแถบด้านข้างซ้ายมือเพื่อไปยังหน้าต่างๆ ได้เลยครับ!")

home_page_content()
