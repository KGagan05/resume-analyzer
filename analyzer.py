from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_skills(text):
    skills = ["python","machine learning","deep learning","nlp","sql"]
    text = text.lower()
    return [s for s in skills if s in text]

def analyze_resume(resume_text, job_description):

    texts = [resume_text, job_description]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    score = round(similarity * 100, 2)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    missing = list(set(job_skills) - set(resume_skills))

    return score, resume_skills, missing