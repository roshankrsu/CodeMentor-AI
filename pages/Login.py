import streamlit as st

if st.session_state.get("logged_in"):
    st.switch_page("pages/Practice.py")
from utils.auth import login_user
from streamlit_cookies_manager import EncryptedCookieManager
import os
from dotenv import load_dotenv

load_dotenv()

cookies = EncryptedCookieManager(
    prefix="codementor/",
    password=os.getenv("JWT_SECRET")
)

if not cookies.ready():
    st.stop()

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if not email or not password:
        st.error("All fields are required")
    else:
        success, result = login_user(email, password)

        if success:
            st.write("Token being saved:", result["token"])

            cookies["auth_token"] = result["token"]
            cookies.save()

            st.session_state.logged_in = True
            st.session_state.user = result["user"]

            st.success("Login successful")

        else:
            st.error(result)