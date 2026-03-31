import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from preprocess import load_data, preprocess_courses

courses = load_data()
tfidf, tfidf_matrix = preprocess_courses(courses)

def content_based_recommend(idx, top_n=5):
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_courses = [courses.iloc[i[0]]["course_title"] for i in sim_scores[1:top_n+1]]
    return top_courses

if __name__ == "__main__":
    print("Recommendations:", content_based_recommend(10))
