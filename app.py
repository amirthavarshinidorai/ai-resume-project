import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd

from pdf_generator import generate_pdf
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from recommender import recommend_jobs
from roadmap import find_skill_gap, suggest_learning, get_resume_feedback

# ---------------- LOGIN STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- CHAT HISTORY ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- LOGIN ----------------
def login_page():
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# ---------------- CHATBOT ----------------
def chatbot_response(user_input, skills, score, job_data):

    user_input = user_input.lower()

    if "skill" in user_input:
        return f"You have skills: {', '.join(skills)}"

    elif "job" in user_input:
        jobs = [j["Job Role"] for j in job_data]
        return f"Best roles: {', '.join(jobs)}"

    elif "weak" in user_input:
        if score < 50:
            return "Weakness: Low skills and no strong projects."
        elif score < 75:
            return "Weakness: Need more real-world projects."
        else:
            return "Good resume, but add advanced projects."

    elif "missing" in user_input:
        missing = []
        for j in job_data:
            if j["Missing Skills"]:
                missing.extend(j["Missing Skills"].split(", "))
        return f"Missing skills: {', '.join(set(missing))}"

    elif "learning" in user_input or "plan" in user_input:

        all_missing = []
        for j in job_data:
            if j["Missing Skills"]:
                all_missing.extend(j["Missing Skills"].split(", "))

        if all_missing:
            plan = "📚 Learning Plan:\n\n"
            for i, skill in enumerate(set(all_missing)):
                plan += f"Month {i+1}: Learn {skill}\n"
            return plan

        return "You already have required skills 🎉"

    elif "interview" in user_input:
        if score > 75:
            return "You are ready for interviews 👍"
        elif score > 50:
            return "Somewhat ready, improve projects."
        else:
            return "Not ready yet, need more preparation."

    elif "improve" in user_input or "resume" in user_input:
        return """
- Add 2-3 strong projects
- Add GitHub/portfolio
- Add more technical skills
- Use action words (Built, Developed)
- Mention achievements
"""

    else:
        return f"""
I understood: {user_input}

Score: {score}%
Skills: {', '.join(skills)}

👉 Improve projects + learn missing skills 🚀
"""

# ---------------- LOGIN CHECK ----------------
if not st.session_state.logged_in:
    login_page()
    st.stop()

# ---------------- APP ----------------
st.set_page_config(page_title="AI Resume System", layout="wide")
st.title("🚀 AI Resume Job Recommendation System")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file:

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("Resume Uploaded")

    # ---------------- SKILLS ----------------
    resume_text = extract_text_from_pdf("temp_resume.pdf")
    skills = extract_skills(resume_text)

    st.subheader("🧠 Skills")
    st.write(", ".join(skills))

    # ---------------- SCORE ----------------
    score = round((len(skills)/11)*100, 2)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'suffix': "%"},
        title={'text': "Resume Score"}
    ))
    st.plotly_chart(fig)

    # ---------------- JOBS ----------------
    recommended_jobs = recommend_jobs(skills)
    job_data = []

    if not recommended_jobs.empty:

        top_jobs = recommended_jobs.head(3)

        for _, row in top_jobs.iterrows():

            job_title = row["Job Title"]
            job_desc = row["Job Description"]

            missing_skills = find_skill_gap(skills, job_desc)

            feasibility = 100 if not missing_skills else round(
                (len(skills)/(len(skills)+len(missing_skills)))*100, 2
            )

            job_data.append({
                "Job Role": job_title,
                "Match %": round(row["match_score"]*100, 2),
                "Feasibility": feasibility,
                "Missing Skills": ", ".join(missing_skills) if missing_skills else ""
            })

            st.subheader(f"💼 {job_title}")

            if missing_skills:
                st.warning(f"Missing: {', '.join(missing_skills)}")
            else:
                st.success("No missing skills")

            # ---------------- LEARNING ----------------
            if missing_skills:
                learning = suggest_learning(missing_skills)
                for i, skill in enumerate(missing_skills):
                    st.write(f"📅 Month {i+1}: Learn {skill}")
                    for r in learning.get(skill, []):
                        if isinstance(r, tuple):
                            st.markdown(f"- [{r[0]}]({r[1]})")

        st.dataframe(pd.DataFrame(job_data))

    # ---------------- FEEDBACK ----------------
    feedback = get_resume_feedback(skills, score)

    st.subheader("📄 Suggestions")
    for f in feedback:
        st.write("•", f)

    # ---------------- CHATBOT ----------------
    st.subheader("🤖 AI Career Assistant")

    user_input = st.text_input("Ask anything")

    if st.button("Send"):
        if user_input:
            response = chatbot_response(user_input, skills, score, job_data)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", response))

    for sender, msg in st.session_state.chat_history:
        if sender == "You":
            st.write(f"🧑 {msg}")
        else:
            st.write(f"🤖 {msg}")

    # ---------------- DOWNLOAD ----------------
    st.subheader("📥 Download Report")

    if st.button("Generate PDF"):
        generate_pdf("report.pdf", skills, score, job_data, feedback)

        with open("report.pdf", "rb") as file:
            st.download_button(
                "⬇️ Download Report",
                file,
                file_name="AI_Report.pdf",
                mime="application/pdf"
            )