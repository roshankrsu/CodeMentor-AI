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
    Write a clear and complete problem statement.

    ## Constraints
    Include realistic constraints like:
    - input size
    - value ranges
    - time complexity expectations

    ## Example 1
    Input:
    ...
    Output:
    ...
    Explanation:
    ...

    ## Example 2
    Input:
    ...
    Output:
    ...
    Explanation:
    ...

    ## Edge Cases
    Mention important edge cases.

    ## Hint
    Give a useful hint without revealing full solution.

    ## Expected Complexity
    Mention expected time and space complexity.

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

    except Exception as e:
        return f"❌ AI service temporarily unavailable: {str(e)}"