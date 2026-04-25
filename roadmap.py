# Master skill database
skill_database = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "data analysis",
    "power bi",
    "excel",
    "tensorflow",
    "pandas",
    "numpy",
    "statistics",
    "tableau",
    "java",
    "html",
    "css",
    "javascript"
]

def find_skill_gap(resume_skills, job_text):

    job_text = job_text.lower()

    required_skills = []

    # Find skills present in job description
    for skill in skill_database:
        if skill in job_text:
            required_skills.append(skill)

    # Find missing skills
    missing = []

    for skill in required_skills:
        if skill not in resume_skills:
            missing.append(skill)

    return missing


skills_master_list = [
    "python",
    "machine learning",
    "sql",
    "data analysis",
    "java",
    "html",
    "css",
    "deep learning",
    "statistics",
    "power bi",
    "excel"
]


def find_skill_gap(user_skills, job_description):

    missing = []
    job_text = job_description.lower()

    for skill in skills_master_list:
        if skill in job_text and skill not in user_skills:
            missing.append(skill)

    return missing


learning_resources = {

    "machine learning": [
        ("Coursera ML Course", "https://www.coursera.org/learn/machine-learning"),
        ("YouTube ML Playlist", "https://www.youtube.com/results?search_query=machine+learning+tutorial"),
        ("ML Projects Practice", "https://www.kaggle.com")
    ],

    "python": [
        ("Python for Everybody", "https://www.coursera.org/specializations/python"),
        ("Python Full Course", "https://www.youtube.com/results?search_query=python+full+course")
    ],

    "sql": [
        ("SQL Course Coursera", "https://www.coursera.org/learn/sql-for-data-science"),
        ("SQL Practice", "https://leetcode.com")
    ],

    "data analysis": [
        ("Google Data Analytics", "https://www.coursera.org/professional-certificates/google-data-analytics"),
        ("Pandas Tutorials", "https://www.youtube.com/results?search_query=pandas+tutorial")
    ]
}




def suggest_learning(missing_skills):

    suggestions = {}

    for skill in missing_skills:
        skill_lower = skill.lower()

        if skill_lower in learning_resources:
            suggestions[skill] = learning_resources[skill_lower]

    return suggestions



learning_resources = {
    "machine learning": [
        "Coursera Machine Learning Course",
        "YouTube Machine Learning Playlist",
        "Build ML Mini Projects"
    ],

    "python": [
        "Python for Everybody (Coursera)",
        "YouTube Python Full Course",
        "Practice in HackerRank"
    ],

    "sql": [
        "SQL for Data Science (Coursera)",
        "YouTube SQL Tutorial",
        "Practice in LeetCode"
    ],

    "data analysis": [
        "Google Data Analytics Certificate",
        "YouTube Pandas Tutorials",
        "Practice Kaggle Projects"
    ]
}


def suggest_learning(missing_skills):
    """
    Returns a dictionary where each missing skill maps to a list of (Course Name, URL) tuples.
    """
    learning_resources = {
        "python": [
            ("Coursera Python for Everybody", "https://www.coursera.org/specializations/python"),
            ("YouTube Python Tutorial Playlist", "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU")
        ],
        "sql": [
            ("SQL for Data Science - Coursera", "https://www.coursera.org/learn/sql-for-data-science"),
            ("SQL Tutorial - W3Schools", "https://www.w3schools.com/sql/")
        ],
        "java": [
            ("Java Programming Masterclass - Udemy", "https://www.udemy.com/course/java-the-complete-java-developer-course/"),
            ("Java Tutorial - TutorialsPoint", "https://www.tutorialspoint.com/java/index.htm")
        ],
        "data analysis": [
            ("Data Analysis with Python - Coursera", "https://www.coursera.org/learn/data-analysis-with-python"),
            ("Data Analysis Tutorial - YouTube", "https://www.youtube.com/watch?v=r-uOLxNrNk8")
        ],
        "power bi": [
            ("Microsoft Power BI Guided Learning", "https://learn.microsoft.com/en-us/power-bi/guided-learning/"),
            ("Power BI Tutorial - YouTube", "https://www.youtube.com/watch?v=AGrl-H87pRU")
        ],
        "machine learning": [
            ("Coursera Machine Learning by Andrew Ng", "https://www.coursera.org/learn/machine-learning"),
            ("YouTube ML Playlist", "https://www.youtube.com/playlist?list=PLAwxTw4SYaPn2cq6t8auXZnVYpYYuL7Iw"),
            ("Build ML Mini Projects", "https://github.com/yourusername/ml-projects")
        ],
        "excel": [
            ("Excel for Beginners - Udemy", "https://www.udemy.com/course/microsoft-excel-2013-from-beginner-to-advanced/"),
            ("Excel Tutorial - YouTube", "https://www.youtube.com/watch?v=rwbho0CgEAE")
        ],
        "react": [
            ("React JS Crash Course", "https://www.youtube.com/watch?v=w7ejDZ8SWv8"),
            ("React Official Docs", "https://reactjs.org/docs/getting-started.html")
        ],
        "node.js": [
            ("Node.js Tutorial for Beginners", "https://www.youtube.com/watch?v=RLtyhwFtXQA"),
            ("Node.js Official Docs", "https://nodejs.org/en/docs/")
        ],
        "django": [
            ("Django for Beginners", "https://djangoforbeginners.com/"),
            ("Django Official Docs", "https://docs.djangoproject.com/en/4.2/intro/tutorial01/")
        ]
    }

    # Create dictionary only for the missing skills provided
    return {skill: learning_resources.get(skill, []) for skill in missing_skills}
def suggest_learning(missing_skills):
    """
    Returns a dictionary where each missing skill maps to a list of (Course Name, URL) tuples.
    """
    learning_resources = {
        "python": [
            ("Coursera Python for Everybody", "https://www.coursera.org/specializations/python"),
            ("YouTube Python Tutorial Playlist", "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU")
        ],
        "sql": [
            ("SQL for Data Science - Coursera", "https://www.coursera.org/learn/sql-for-data-science"),
            ("SQL Tutorial - W3Schools", "https://www.w3schools.com/sql/")
        ],
        "java": [
            ("Java Programming Masterclass - Udemy", "https://www.udemy.com/course/java-the-complete-java-developer-course/"),
            ("Java Tutorial - TutorialsPoint", "https://www.tutorialspoint.com/java/index.htm")
        ],
        "data analysis": [
            ("Data Analysis with Python - Coursera", "https://www.coursera.org/learn/data-analysis-with-python"),
            ("Data Analysis Tutorial - YouTube", "https://www.youtube.com/watch?v=r-uOLxNrNk8")
        ],
        "power bi": [
            ("Microsoft Power BI Guided Learning", "https://learn.microsoft.com/en-us/power-bi/guided-learning/"),
            ("Power BI Tutorial - YouTube", "https://www.youtube.com/watch?v=AGrl-H87pRU")
        ],
        "machine learning": [
            ("Coursera Machine Learning by Andrew Ng", "https://www.coursera.org/learn/machine-learning"),
            ("YouTube ML Playlist", "https://www.youtube.com/playlist?list=PLAwxTw4SYaPn2cq6t8auXZnVYpYYuL7Iw"),
            ("Build ML Mini Projects", "https://github.com/yourusername/ml-projects")
        ],
        "excel": [
            ("Excel for Beginners - Udemy", "https://www.udemy.com/course/microsoft-excel-2013-from-beginner-to-advanced/"),
            ("Excel Tutorial - YouTube", "https://www.youtube.com/watch?v=rwbho0CgEAE")
        ],
        "react": [
            ("React JS Crash Course", "https://www.youtube.com/watch?v=w7ejDZ8SWv8"),
            ("React Official Docs", "https://reactjs.org/docs/getting-started.html")
        ],
        "node.js": [
            ("Node.js Tutorial for Beginners", "https://www.youtube.com/watch?v=RLtyhwFtXQA"),
            ("Node.js Official Docs", "https://nodejs.org/en/docs/")
        ],
        "django": [
            ("Django for Beginners", "https://djangoforbeginners.com/"),
            ("Django Official Docs", "https://docs.djangoproject.com/en/4.2/intro/tutorial01/")
        ]
    }

    # Create dictionary only for the missing skills provided
    return {skill: learning_resources.get(skill, []) for skill in missing_skills}


def get_resume_feedback(skills, score):
    feedback = []

    if score < 50:
        feedback.append("Add more technical skills")
        feedback.append("Include at least 2 projects")
    
    if "python" not in skills:
        feedback.append("Learn and add Python skill")
    
    if "machine learning" not in skills:
        feedback.append("Add Machine Learning project")
    
    feedback.append("Add GitHub or portfolio link")
    feedback.append("Use action words like Developed, Built, Designed")

    return feedback


def score_breakdown(skills):
    skill_score = len(skills) * 10
    project_score = 20 if len(skills) > 3 else 10
    experience_score = 20 if len(skills) > 5 else 10

    total = skill_score + project_score + experience_score

    return skill_score, project_score, experience_score, total


