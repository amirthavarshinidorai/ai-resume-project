import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "dataset", "job_title_des.csv")

    if not os.path.exists(file_path):
        return None

    return pd.read_csv(file_path)

def recommend_jobs(skills):

    jobs = load_data()

    if jobs is None:
        return pd.DataFrame()

    documents = jobs["Job Description"].astype(str).tolist()

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(documents)

    skill_text = " ".join(skills)
    skill_vec = tfidf.transform([skill_text])

    similarity = cosine_similarity(skill_vec, tfidf_matrix)[0]

    jobs["match_score"] = similarity

    jobs_sorted = jobs.sort_values(by="match_score", ascending=False)

    return jobs_sorted.drop_duplicates(subset=["Job Title"]).head(5)