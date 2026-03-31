from recommender import content_based_recommend, courses

def popular_courses(top_n=5):
    return courses.sort_values("num_subscribers", ascending=False).head(top_n)[["course_title","num_subscribers"]]

def hybrid_recommend(idx, top_n=5):
    content_recs = content_based_recommend(idx, top_n*2)
    pop_recs = popular_courses(top_n*2)["course_title"].tolist()
    final_recs = list(set(content_recs + pop_recs))[:top_n]
    return final_recs

if __name__ == "__main__":
    print("Hybrid Recommendations:", hybrid_recommend(10))
