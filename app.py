
import os
import random
from datetime import date

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

st.set_page_config(
    page_title="Little Study Studio",
    page_icon="🌷",
    layout="wide"
)

# ---------- SOFT, LIGHT DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700&display=swap');

.stApp {
    background: #FAF7F0;
    color: #493F46;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stHeader"] {
    background: #FAF7F0;
}
[data-testid="stSidebar"] {
    background: #F0E9F6;
    border-right: 1px solid #E5D9EC;
}
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3 {
    color: #55445B !important;
    font-family: 'Playfair Display', serif !important;
}
p, label, span {
    font-family: 'DM Sans', sans-serif;
}
.hero {
    background: linear-gradient(120deg, #E8DDF6, #F7DFD7 55%, #F8EBCB);
    border: 1px solid #EADBE9;
    border-radius: 26px;
    padding: 35px;
    margin: 10px 0 26px;
}
.eyebrow {
    color: #856D92;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}
.hero h1 {
    color: #59455E !important;
    font-size: clamp(32px, 4vw, 48px);
    line-height: 1.2;
    margin: 12px 0;
}
.hero p {
    color: #786679;
    font-size: 15px;
    max-width: 670px;
}
.section-label {
    color: #88758D;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin: 24px 0 12px;
}
.paper-card {
    background: #FFFFFF;
    border: 1px solid #EEE5EA;
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
    box-shadow: 0 5px 18px rgba(109, 81, 105, 0.045);
}
.lavender-card {
    background: #EDE4F8;
    border: 1px solid #E2D4F1;
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
}
.peach-card {
    background: #F9E4DB;
    border: 1px solid #F0D7CC;
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
}
.sage-card {
    background: #E3EDDF;
    border: 1px solid #D5E4CF;
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
}
.butter-card {
    background: #F7EFCF;
    border: 1px solid #EEE3B9;
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
}
.card-label {
    color: #89798C;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
}
.card-number {
    color: #59475F;
    font-size: 30px;
    font-weight: 800;
    margin: 9px 0 4px;
}
.card-note {
    color: #817383;
    font-size: 12px;
}
.feature {
    background: #FFFFFF;
    border: 1px solid #EEE5EA;
    border-radius: 18px;
    padding: 20px;
    min-height: 140px;
}
.feature-icon {
    font-size: 27px;
}
.feature-title {
    color: #604D65;
    font-weight: 800;
    margin: 8px 0 5px;
}
.feature-text {
    color: #897D8B;
    font-size: 13px;
    line-height: 1.6;
}
div.stButton > button {
    background: #9A7BB5;
    color: white;
    border: 1px solid #9A7BB5;
    border-radius: 13px;
    min-height: 45px;
    font-weight: 700;
}
div.stButton > button:hover {
    background: #82639F;
    border-color: #82639F;
    color: white;
}
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] > div {
    background: #FFFFFF;
    border-color: #E4D8E7;
    border-radius: 10px;
}
.stTextInput input, .stTextArea textarea {
    color: #55445B;
}
[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 15px;
    border: 1px solid #EEE5EA;
    border-radius: 15px;
}
[data-testid="stMetricLabel"] {
    color: #88758D;
}
[data-testid="stMetricValue"] {
    color: #59475F;
}
div[data-testid="stTabs"] button {
    color: #796483;
}
.stProgress > div > div > div {
    background: #A78BC4;
}
hr {
    border-color: #E9DFE8;
}
.small-note {
    color: #8D7F8D;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("# 🌷 Study Studio")
    st.caption("A LITTLE SPACE TO GROW")
    st.divider()

    student = st.text_input("Your name", "Student")
    exam_date = st.date_input(
        "Next exam date", value=date.today()
    )
    hours = st.slider(
        "Daily study time (hours)", 1, 12, 4
    )

    st.divider()
    st.markdown("### 🌱 Your intention")
    st.write("Small steps. Gentle progress. One topic at a time.")
    st.caption("Made with Python, Streamlit & an LLM")

# ---------- HERO ----------
st.markdown("""
<div class="hero">
  <div class="eyebrow">✿ YOUR PERSONAL STUDY SANCTUARY</div>
  <h1>Make room for your dreams.</h1>
  <p>
    A calmer way to prepare for exams. Organize your topics,
    understand what needs attention, and let your AI study
    companion help you take the next small step.
  </p>
  <div style="color:#826A8A;font-size:14px;font-weight:600;">
    A little progress every day adds up. ♡
  </div>
</div>
""", unsafe_allow_html=True)

days_left = max((exam_date - date.today()).days, 0)

# ---------- DASHBOARD ----------
st.markdown(
    '<div class="section-label">YOUR LITTLE DASHBOARD ✧</div>',
    unsafe_allow_html=True
)

a, b, c, d = st.columns(4, gap="medium")

dashboard = [
    (a, "lavender-card", "📅", "EXAM COUNTDOWN",
     f"{days_left} days", "One day at a time"),
    (b, "peach-card", "☕", "DAILY STUDY GOAL",
     f"{hours} hours", "Your time, your pace"),
    (c, "sage-card", "🌱", "TODAY'S INTENTION",
     "Keep going", "Progress over perfection"),
    (d, "butter-card", "✨", "STUDY MODE",
     "You can do this", "Begin with one topic")
]

for col, style, emoji, label, value, note in dashboard:
    with col:
        st.markdown(f"""
        <div class="{style}">
          <div style="font-size:23px">{emoji}</div>
          <div class="card-label">{label}</div>
          <div class="card-number" style="font-size:23px">{value}</div>
          <div class="card-note">{note}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------- MOTIVATIONAL NOTE ----------
st.markdown("")
st.markdown("""
<div style="
background:#FFFFFF;
border:1px solid #EEE5EA;
border-radius:18px;
padding:23px 26px;
text-align:center;">
  <div style="font-size:26px;">🌷 ✧ 📖 ✧ 🌷</div>
  <div style="
  font-family:'Playfair Display',serif;
  font-size:25px;color:#705779;margin:10px 0;">
    You don't have to be perfect.
  </div>
  <div style="color:#928194;font-size:14px;">
    You just have to begin. Your future self will thank you. ♡
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- SUBJECT DETAILS ----------
st.markdown(
    '<div class="section-label">LET’S MAKE A PLAN ✿</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    st.subheader("📚 Your study snapshot")
    subject = st.text_input(
        "Which subject are we working on?",
        "Design and Analysis of Algorithms"
    )
    topics = st.text_area(
        "Topics you need to study (separate with commas)",
        "Divide and Conquer, Recurrence Relations, "
        "Greedy Algorithms, Dynamic Programming"
    )

    x, y, z = st.columns(3)
    with x:
        marks = st.slider("Previous test score (%)", 0, 100, 45)
    with y:
        confidence = st.slider("Confidence (1–5)", 1, 5, 2)
    with z:
        completion = st.slider("Syllabus completed (%)", 0, 100, 40)

# ---------- READINESS ----------
weakness = (100 - marks) / 100
low_confidence = (5 - confidence) / 4
incomplete = (100 - completion) / 100
urgency = 1 / (days_left + 1)

risk = round(100 * (
    0.35 * weakness
    + 0.25 * low_confidence
    + 0.25 * incomplete
    + 0.15 * min(urgency * 7, 1)
))

st.markdown(
    '<div class="section-label">YOUR PROGRESS, WITHOUT THE PRESSURE 🌿</div>',
    unsafe_allow_html=True
)

p1, p2 = st.columns([1, 1], gap="large")

with p1:
    with st.container(border=True):
        st.markdown("### 🌿 Syllabus garden")
        st.write("Every topic you finish is a little win.")
        st.progress(completion / 100)
        st.markdown(f"**{completion}%** of your syllabus completed")
        st.caption("Keep growing, one topic at a time.")

with p2:
    with st.container(border=True):
        st.markdown("### 🪻 Preparation check-in")
        st.write("A gentle estimate based on your answers.")
        st.progress(risk / 100)
        st.markdown(f"**{risk}/100** preparation risk score")
        if risk >= 65:
            st.warning("Let's focus on your weakest areas first.")
        elif risk >= 40:
            st.info("A little structure and practice can help.")
        else:
            st.success("Keep revising and protect your progress.")

st.caption(
    "This score uses simple rules. It is not a validated "
    "prediction of exam performance."
)

# ---------- AI FEATURES ----------
st.markdown(
    '<div class="section-label">YOUR AI STUDY COMPANION ✨</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="feature">
  <div class="feature-icon">🧠 &nbsp; 📖 &nbsp; 💭</div>
  <div class="feature-title">You bring the questions. We'll work through them together.</div>
  <div class="feature-text">
    Generate a personalized revision plan, ask for simple explanations,
    or practise with questions made for your syllabus.
  </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs([
    "🌷 My study plan",
    "💬 Ask my AI tutor"
])

api_key = os.getenv("GROQ_API_KEY")


def call_ai(prompt):
    if not api_key:
        st.error(
            "API key not found. Check that GROQ_API_KEY is set "
            "in your .env file beside app.py."
        )
        return None

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a kind and practical college study tutor. "
                        "Use encouraging, simple language, useful examples, "
                        "clear headings, and realistic study schedules. "
                        "Never guarantee marks or invent student results."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_completion_tokens=2200
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(
            "The AI request failed. Check your API key, internet, "
            "available model, and API usage limits."
        )
        st.caption(str(e))
        return None


with tab1:
    st.markdown("### 🌸 A plan made for you")
    st.write("Let's turn your remaining time into small, achievable steps.")

    if st.button("✨ Create my study plan", use_container_width=True):
        if not subject.strip() or not topics.strip():
            st.warning("Enter your subject and topics first.")
        else:
            prompt = f"""
Create a personalized exam preparation plan.

Student: {student}
Subject: {subject}
Exam date: {exam_date}
Days remaining: {days_left}
Daily study hours: {hours}
Topics: {topics}
Previous test score: {marks}/100
Confidence: {confidence}/5
Syllabus completed: {completion}%
Rule-based preparation risk: {risk}/100

Provide:
1. A kind, realistic assessment.
2. Ranked topics and reasons for prioritization.
3. A daily schedule fitting the available hours and days.
4. Active recall and revision methods.
5. Five practice questions with answers.
6. Three small actions to begin today.

If the exam is today, give a last-minute plan.
Use beginner-friendly language. Do not guarantee results.
"""
            with st.spinner("🌷 Your AI tutor is preparing your plan..."):
                answer = call_ai(prompt)

            if answer:
                st.session_state["study_plan"] = answer

    if "study_plan" in st.session_state:
        st.markdown("---")
        st.markdown("### 📖 Your study plan")
        st.markdown(st.session_state["study_plan"])
        st.download_button(
            "📥 Save my plan",
            st.session_state["study_plan"],
            file_name="my_study_plan.txt",
            mime="text/plain"
        )

with tab2:
    st.markdown("### 💌 What would you like help with?")
    question = st.text_area(
        "Ask your AI tutor",
        placeholder=(
            "For example: Explain dynamic programming like I'm a beginner "
            "and give me three practice questions."
        ),
        height=120
    )

    if st.button("💬 Ask my AI tutor", use_container_width=True):
        if not question.strip():
            st.warning("Write a question first.")
        else:
            prompt = f"""
Subject: {subject}
Topics: {topics}
Exam date: {exam_date}
Days remaining: {days_left}
Daily study time: {hours} hours
Student question: {question}

Explain clearly for a college beginner. Use examples where helpful.
"""
            with st.spinner("💭 Thinking through your question..."):
                answer = call_ai(prompt)

            if answer:
                st.markdown("### ✨ Here's your answer")
                st.markdown(answer)

# ---------- FOOTER ----------
st.markdown("""
<div style="
text-align:center;
padding:30px 10px;
color:#9A889C;
font-size:13px;">
  MADE WITH ♡ FOR EVERY STUDENT CHASING A DREAM
  <br><br>
  Little Study Studio · Learn gently. Grow steadily. 🌷
</div>
""", unsafe_allow_html=True)
