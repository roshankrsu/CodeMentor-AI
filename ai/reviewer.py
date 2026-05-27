import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def review_code(question, code):
    prompt = f"""
    You are a technical interviewer.

    Coding Question:
    {question}

    Candidate's Solution:
    {code}

    Review the solution and provide:

    1. Correctness
    2. Bugs or mistakes
    3. Time complexity
    4. Space complexity
    5. Optimization suggestions
    6. Final score out of 10
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

    except Exception:
        return "❌ AI review unavailable."