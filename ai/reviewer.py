import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)


def review_code(question, code):
    prompt = f"""
    You are a senior software engineering interviewer.

    Review the candidate's solution.

    Coding Question:
    {question}

    Candidate Solution:
    {code}

    Provide structured feedback:

    1. Correctness
    2. Bugs / Issues
    3. Time Complexity
    4. Space Complexity
    5. Optimization Suggestions
    6. Final Interview Score (out of 10)

    Be clear and professional.
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
        return f"❌ AI review unavailable: {str(e)}"