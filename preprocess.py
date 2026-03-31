import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data():
    courses = pd.read_csv("data/udemy_course_data.csv")
    return courses

def preprocess_courses(courses):
    courses["course_title"] = courses["course_title"].str.lower()
    courses["level"] = courses["level"].fillna("All Levels")
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(courses["course_title"])
    return tfidf, tfidf_matrix
