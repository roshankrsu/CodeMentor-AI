import streamlit as st
from streamlit_ace import st_ace
from utils.helpers import require_login
from ai.generator import generate_question
from ai.reviewer import review_code

require_login()

st.title("Coding Practice")
st.write(f"Welcome {st.session_state.user['name']}")

topic = st.selectbox(
    "Choose Topic",
    [
        "Arrays",
        "Strings",
        "Linked List",
        "Stack",
        "Queue",
        "Trees",
        "Graphs",
        "Dynamic Programming",
        "SQL",
        "Python"
    ]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

if "question" not in st.session_state:
    st.session_state.question = None

if "code" not in st.session_state:
    st.session_state.code = ""

if st.button("Generate Question"):
    with st.spinner("Generating question..."):
        question = generate_question(topic, difficulty)

        if question:
            st.session_state.question = question
            st.session_state.code = ""

if st.session_state.question:
    st.markdown(st.session_state.question)

    st.subheader("Write Your Solution")

    code = st_ace(
        language="python",
        theme="monokai",
        height=400,
        key="code_editor",
        value=st.session_state.code
    )

    st.session_state.code = code

    if st.button("Review My Code"):
        if not st.session_state.code.strip():
            st.warning("Please write some code first.")
        else:
            with st.spinner("AI reviewing your solution..."):
                feedback = review_code(
                    st.session_state.question,
                    st.session_state.code
                )

                if feedback:
                    st.markdown("## AI Feedback")
                    st.markdown(feedback)