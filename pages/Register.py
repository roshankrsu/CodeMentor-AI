import streamlit as st
from utils.auth import create_user
if st.session_state.get("logged_in"):
    st.switch_page("pages/Practice.py")

st.title("Register")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    if not name or not email or not password:
        st.error("All fields are required")
    else:
        success, message = create_user(name, email, password)

        if success:
            st.success(message)
        else:
            st.error(message)