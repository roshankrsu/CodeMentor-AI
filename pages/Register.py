import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_cookies_manager import EncryptedCookieManager
from utils.auth import create_user, login_after_registration

load_dotenv()

cookies = EncryptedCookieManager(
    prefix="codementor/",
    password=os.getenv("JWT_SECRET") or st.secrets["JWT_SECRET"]
)

if not cookies.ready():
    st.stop()

if st.session_state.get("logged_in"):
    st.switch_page("pages/Practice.py")

st.title("Register")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    if not name or not email or not password:
        st.error("All fields are required")

    else:
        success, result = create_user(name, email, password)

        if success:
            auth_data = login_after_registration(email)

            st.session_state.logged_in = True
            st.session_state.user = auth_data["user"]

            cookies["auth_token"] = auth_data["token"]
            cookies.save()

            st.success("Registration successful!")
            st.switch_page("pages/Practice.py")

        else:
            st.error(result)