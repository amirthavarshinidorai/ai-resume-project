import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load jobs CSV
jobs = pd.read_csv("dataset/job_title_des.csv")

def recommend_jobs(skills):
    """
    Recommend top 5 jobs based on skills
    """
    documents = jobs["Job Description"].tolist()
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(documents)

    skill_text = " ".join(skills)
    skill_vec = tfidf.transform([skill_text])

    similarity = cosine_similarity(skill_vec, tfidf_matrix)[0]
    jobs["match_score"] = similarity
    jobs_sorted = jobs.sort_values(by="match_score", ascending=False)
    return jobs_sorted.drop_duplicates(subset=["Job Title"]).head(5)


