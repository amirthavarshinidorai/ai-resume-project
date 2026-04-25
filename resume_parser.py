print("Program Started")

import PyPDF2
from skill_extractor import extract_skills
from roadmap import find_skill_gap


def extract_text_from_pdf(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text


# -------- Resume Path --------
resume_path = "resumes/my resume.pdf"


# -------- Extract Resume Text --------
resume_text = extract_text_from_pdf(resume_path)


# -------- Extract Skills --------
skills = extract_skills(resume_text)

print("\nSkills Found:")
print(skills)


# -------- Recommend Jobs --------
recommended_jobs = recommend_jobs(skills)

print("\nRecommended Jobs:")
print(recommended_jobs[["Job Title", "match_score"]])


# -------- Skill Gap Analysis --------
top_job_description = recommended_jobs.iloc[0]["Job Description"]

missing = find_skill_gap(skills, top_job_description)

print("\nMissing Skills For Top Job:")
print(missing)

resume_text = extract_text_from_pdf(resume_path)

print("\n--- Resume Text Preview ---")
print(resume_text[:500])
