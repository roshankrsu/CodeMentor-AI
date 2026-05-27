# 💻 CodeMentor AI

CodeMentor AI is an AI-powered placement preparation platform designed to help students prepare for software engineering interviews through coding practice, AI code review, resume analysis, and progress tracking.

---

## 🚀 Features

### 🧠 AI Coding Interview Practice
Generate realistic coding interview questions based on:

- Topic selection (Arrays, Strings, Graphs, DP, etc.)
- Difficulty level (Easy / Medium / Hard)
- FAANG-style interview problem format

Each generated problem includes:

- Clear problem statement
- Constraints
- Sample test cases
- Edge cases
- Hints
- Expected complexity

---

### ⚡ AI Code Review
Solve coding problems directly in the built-in code editor and receive instant AI feedback on:

- Correctness
- Bugs / logical mistakes
- Time complexity
- Space complexity
- Optimization suggestions
- Interview score out of 10

---

### 📄 AI Resume Analyzer
Upload your resume PDF and receive AI-powered analysis including:

- ATS Score
- Strengths
- Weaknesses
- Missing keywords
- Formatting suggestions
- Grammar improvements
- Role fit recommendations

---

### 📊 Dashboard Analytics
Track your placement preparation progress with:

- Problems solved
- AI review count
- Average performance score
- Weak topics
- Practice analytics

---

### 🔐 Secure Authentication
Includes complete authentication system with:

- User registration
- Login
- Password hashing using bcrypt
- JWT-based authentication
- Persistent login using encrypted cookies
- Logout functionality

---

## 🛠 Tech Stack

### Frontend
- Streamlit
- Streamlit Ace Editor

### Backend
- Python

### Database
- MongoDB Atlas

### Authentication
- JWT (JSON Web Tokens)
- bcrypt
- Encrypted Cookie Manager

### AI
- Groq API
- Llama 3.3 70B

### Resume Parsing
- PyMuPDF

### Data Visualization
- Pandas
- Plotly

---

## 📂 Project Structure

```bash
CodeMentor-AI/
│
├── app.py
├── .env
├── requirements.txt
│
├── db/
│   └── mongo.py
│
├── utils/
│   ├── auth.py
│   └── helpers.py
│
├── ai/
│   ├── generator.py
│   ├── reviewer.py
│   └── resume_analyzer.py
│
├── pages/
│   ├── 1_Register.py
│   ├── 2_Login.py
│   ├── 3_Practice.py
│   ├── 4_Dashboard.py
│   ├── 5_Logout.py
│   └── 6_Resume_Analyzer.py