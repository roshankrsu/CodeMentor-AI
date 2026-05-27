import streamlit as st
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

st.title("Logout")

if st.button("Logout"):
    if "auth_token" in cookies:
        del cookies["auth_token"]
        cookies.save()

    st.session_state.clear()

    st.success("Logged out successfully")
    st.rerun()