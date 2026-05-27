import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)


def generate_question(topic, difficulty):
    prompt = f"""
    You are an expert FAANG coding interviewer.

    Generate ONE high-quality coding interview question.

    Requirements:
    - Topic must be exactly: {topic}
    - Difficulty must be exactly: {difficulty}
    - Question should be realistic like LeetCode / Google / Amazon interview style
    - Problem must be clearly defined
    - No ambiguity
    - Include all constraints
    - Include examples
    - Include explanation

    Return STRICTLY in this format:

    ## Problem Statement
    Clear and complete problem description.

    ## Constraints
    - input size
    - value ranges
    - realistic constraints

    ## Example 1
    Input:
    Output:
    Explanation:

    ## Example 2
    Input:
    Output:
    Explanation:

    ## Edge Cases
    Important corner cases.

    ## Hint
    Helpful hint without full solution.

    ## Expected Complexity
    Expected time and space complexity.

    Generate only ONE question.
    """

    try:
        chat = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.4
        )

        return chat.choices[0].message.content

    except Exception:
        return "❌ AI service temporarily unavailable."