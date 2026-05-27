import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import fitz

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)


def extract_resume_text(uploaded_file):
    doc = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in doc:
        text += page.get_text()

    return text


def analyze_resume(resume_text):
    prompt = f"""
    You are an expert ATS resume reviewer.

    Analyze this software engineering resume:

    {resume_text}

    Provide:

    1. ATS Score (out of 100)
    2. Strong Points
    3. Weak Points
    4. Missing Skills / Keywords
    5. Grammar / Formatting Issues
    6. Suggested Improvements
    7. Best Matching Roles
    8. Final Verdict
    """

    try:
        chat = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile"
        )

        return chat.choices[0].message.content

    except Exception as e:
        return f"❌ Resume analysis unavailable: {str(e)}"