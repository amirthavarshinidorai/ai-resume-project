import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "dataset", "job_title_des.csv")

# 🔥 SAFE CHECK (IMPORTANT)
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Dataset missing at: {file_path}")

jobs = pd.read_csv(file_path)

def recommend_jobs(skills):

    documents = jobs["Job Description"].astype(str).tolist()

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(documents)

    skill_text = " ".join(skills)
    skill_vec = tfidf.transform([skill_text])

    similarity = cosine_similarity(skill_vec, tfidf_matrix)[0]

    jobs["match_score"] = similarity

    jobs_sorted = jobs.sort_values(by="match_score", ascending=False)

    return jobs_sorted.drop_duplicates(subset=["Job Title"]).head(5)
