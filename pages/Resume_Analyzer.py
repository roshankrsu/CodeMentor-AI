import streamlit as st
from utils.helpers import require_login
from ai.resume_analyzer import extract_resume_text, analyze_resume

require_login()

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and get AI-powered ATS analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_resume_text(uploaded_file)

            analysis = analyze_resume(resume_text)

            st.markdown("## Resume Analysis Report")
            st.markdown(analysis)