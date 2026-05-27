import streamlit as st


def require_login():
    if not st.session_state.get("logged_in", False):
        st.warning("Please login first.")
        st.switch_page("pages/Login.py")