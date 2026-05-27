import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from utils.auth import verify_token
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="CodeMentor AI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

cookies = EncryptedCookieManager(
    prefix="codementor/",
    password=os.getenv("JWT_SECRET")
)

if not cookies.ready():
    st.stop()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

token = cookies.get("auth_token")

if token and not st.session_state.logged_in:
    user = verify_token(token)
    if user:
        st.session_state.logged_in = True
        st.session_state.user = user


# ── HERO ─────────────────────────────────────────────────────────────────────
st.title("💻 CodeMentor AI")
st.subheader("Ace your next coding interview — with AI by your side.")
st.write(
    "Practice with AI-generated questions, get instant code reviews, "
    "and polish your resume. Everything you need for placement prep, in one place."
)

st.divider()

# ── FEATURES ─────────────────────────────────────────────────────────────────
st.subheader("What you can do")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**🧠 AI Coding Practice**")
    st.write(
        "Generate interview questions by topic, difficulty, and style. "
        "Simulate real coding rounds and track your progress over time."
    )

with col2:
    st.info("**⚡ Instant Code Review**")
    st.write(
        "Paste your solution and get feedback on correctness, bugs, "
        "time & space complexity, and optimization — instantly."
    )

with col3:
    st.info("**📄 Resume Analyzer**")
    st.write(
        "Upload your resume and receive an ATS score, keyword gap analysis, "
        "and role-specific improvement suggestions."
    )

st.divider()

# ── WHY ───────────────────────────────────────────────────────────────────────
st.subheader("Why CodeMentor AI?")

col_l, col_r = st.columns(2)

with col_l:
    st.write("**Built to help you get placed:**")
    st.write("✅ AI-powered placement preparation")
    st.write("✅ Real coding interview simulation")
    st.write("✅ Resume improvement suggestions")
    st.write("✅ Personalized, instant feedback")
    st.write("✅ Progress tracking dashboard")

with col_r:
    st.write("**Designed for:**")
    st.write("🎯 Computer Science students")
    st.write("🎯 Campus placement & drive prep")
    st.write("🎯 Software engineering aspirants")
    st.write("🎯 Anyone leveling up for interviews")

st.divider()

# ── CTA ───────────────────────────────────────────────────────────────────────
if not st.session_state.logged_in:
    st.subheader("Ready to start?")
    st.write("Create a free account and begin practicing today.")

    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("🚀 Get Started", use_container_width=True, type="primary"):
            st.switch_page("pages/Register.py")
    with col2:
        if st.button("Login", use_container_width=True):
            st.switch_page("pages/Login.py")

else:
    name = ""
    if isinstance(st.session_state.user, dict):
        name = st.session_state.user.get("name", "")

    st.subheader(f"Welcome back{', ' + name if name else ''}! 👋")
    st.write("Pick up where you left off.")

    if st.button("▶ Continue Practicing", type="primary"):
        st.switch_page("pages/Practice.py")

st.divider()
st.caption("CodeMentor AI · AI-Powered Coding Interview Preparation Platform")