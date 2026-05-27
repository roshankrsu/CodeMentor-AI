import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import require_login
from db.mongo import db

require_login()

st.title("📊 Dashboard")

user = st.session_state.user

reviews_col = db["reviews"]
practice_col = db["practice_history"]

user_reviews  = list(reviews_col.find({"user_id": str(user["_id"])}))
user_practice = list(practice_col.find({"user_id": str(user["_id"])}))

# ── Derived stats ─────────────────────────────────────────────────────────────
total_problems = len(user_practice)
total_reviews  = len(user_reviews)
avg_score      = 0
weak_topic     = "N/A"
best_topic     = "N/A"
topic_scores   = {}

if user_reviews:
    avg_score = round(
        sum(r["score"] for r in user_reviews) / len(user_reviews), 1
    )

    for r in user_reviews:
        topic = r.get("topic", "Unknown")
        topic_scores.setdefault(topic, []).append(r["score"])

    avg_by_topic = {t: sum(v) / len(v) for t, v in topic_scores.items()}
    weak_topic   = min(avg_by_topic, key=avg_by_topic.get)
    best_topic   = max(avg_by_topic, key=avg_by_topic.get)

# ── Metric row ────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Problems Solved", total_problems)
col2.metric("AI Reviews",      total_reviews)
col3.metric("Avg Score",       f"{avg_score}/10")
col4.metric("Weak Topic",      weak_topic)

st.divider()

if not user_reviews:
    st.info("No review data yet. Start practicing to see your stats here!")
    if st.button("Go to Practice", type="primary"):
        st.switch_page("pages/Practice.py")
    st.stop()

# ── Charts ────────────────────────────────────────────────────────────────────
df = pd.DataFrame(user_reviews)

chart_col, score_col = st.columns([3, 2])

with chart_col:
    topic_counts = df["topic"].value_counts().reset_index()
    topic_counts.columns = ["Topic", "Count"]

    fig_bar = px.bar(
        topic_counts,
        x="Topic",
        y="Count",
        title="Problems Attempted by Topic",
        color="Count",
        color_continuous_scale="teal",
    )
    fig_bar.update_layout(
        coloraxis_showscale=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=40, b=20, l=0, r=0),
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with score_col:
    avg_df = pd.DataFrame(
        [(t, round(sum(v) / len(v), 1)) for t, v in topic_scores.items()],
        columns=["Topic", "Avg Score"],
    ).sort_values("Avg Score", ascending=False)

    fig_score = px.bar(
        avg_df,
        x="Avg Score",
        y="Topic",
        orientation="h",
        title="Avg Score by Topic",
        color="Avg Score",
        color_continuous_scale="RdYlGn",
        range_color=[0, 10],
    )
    fig_score.update_layout(
        coloraxis_showscale=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=40, b=20, l=0, r=0),
        yaxis=dict(autorange="reversed"),
    )
    st.plotly_chart(fig_score, use_container_width=True)

st.divider()

# ── Recommendation ────────────────────────────────────────────────────────────
rec_col, strength_col = st.columns(2)

with rec_col:
    st.subheader("🎯 AI Recommendation")
    st.warning(
        f"**Focus on {weak_topic}** — your average score there is lowest. "
        "Try a few targeted problems to build confidence."
    )

with strength_col:
    st.subheader("💪 Your Strength")
    st.success(
        f"**{best_topic}** is your strongest area. "
        "Keep it sharp while working on weaker topics."
    )

st.divider()

# ── Recent feedback ───────────────────────────────────────────────────────────
st.subheader("🗂 Recent AI Feedback")

recent = list(reversed(user_reviews[-5:]))

for i, review in enumerate(recent):
    topic      = review.get("topic", "Unknown")
    score      = review.get("score", "—")
    feedback   = review.get("feedback", "No feedback available.")
    difficulty = review.get("difficulty", "")

    label = f"**{topic}**"
    if difficulty:
        label += f" · {difficulty}"
    label += f" · Score: {score}/10"

    with st.expander(label, expanded=(i == 0)):
        st.write(feedback)