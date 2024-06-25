import streamlit as st
from pages import page1
from pages import page2
from utils.helper_functions import greet

def main():
    st.title("简单的Streamlit应用")
    st.sidebar.title("导航")
    page = st.sidebar.selectbox("选择页面", ["主页", "页面1", "页面2"])

    if page == "主页":
        st.write("欢迎来到主页！")
    elif page == "页面1":
        page1.show_page1()
    elif page == "页面2":
        page2.show_page2()
    st.sidebar.write(greet("用户"))

if __name__ == "__main__":
    main()
