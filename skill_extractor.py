skills_list = [
    "python",
    "machine learning",
    "sql",
    "data analysis",
    "java",
    "html",
    "css"
]

def extract_skills(text):
    found = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found.append(skill)

    return found