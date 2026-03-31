# Personalized Course Recommendation System

##  Overview
This project implements a **Personalized Course Recommendation System** using the Udemy Course Recommendation Dataset.  
It applies **Content-Based Filtering**, **Popularity-Based Ranking**, and a **Hybrid Model** to recommend courses to learners.  

The goal is to demonstrate how AI/ML fundamentals can be applied to real-world education platforms (like Udemy or Vityarthi) to improve learner engagement and decision-making.

---

##  Problem Statement
Learners face difficulty choosing from thousands of online courses.  
Challenges include:
- **Information overload**: Too many options without guidance.
- **Cold start problem**: New users or new courses lack interaction history.
- **Data sparsity**: Many users rate or enroll in only a few courses.

This project addresses these challenges by building a recommender system that balances **relevance** (content similarity) and **popularity** (social proof).

---

##  Dataset
- **Source**: [Udemy Course Recommendation Dataset (Kaggle)](https://www.kaggle.com/datasets/evilspirit05/udemy-course-recommendation)  
- **Features**:
  - `course_id` → unique identifier  
  - `course_title` → name of the course  
  - `price` → free/paid  
  - `num_subscribers` → enrolled students  
  - `num_reviews` → total reviews  
  - `num_lectures` → number of lectures  
  - `level` → difficulty (Beginner, Intermediate, All Levels)  
  - `content_duration` → total hours  

---

##  Methodology

### 1. Content-Based Filtering
- Uses **TF-IDF vectorization** on course titles.
- Computes **cosine similarity** to recommend similar courses.

### 2. Popularity-Based Recommendation
- Ranks courses by `num_subscribers` and `num_reviews`.
- Provides “trending” or “most popular” courses.

### 3. Hybrid Model
- Combines content similarity with popularity scores.
- Produces balanced recommendations (relevant + popular).

---

##  Project Structure
```
Course-Recommender/
│── data/                  # Dataset
│   └── udemy_course_data.csv
│
│── notebooks/             # Jupyter notebooks
│   └── content_based.ipynb
│   └── popularity_based.ipynb
│   └── hybrid_model.ipynb
│
│                  # Python scripts
│   └── preprocess.py
│   └── recommender.py
│   └── hybrid.py
│
│── report/                # Documentation
│   └── project_report.md
│
│── requirements.txt       # Dependencies
│── README.md              # Project overview

```

---

##  Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/Adhya739/Course-Recommender.git
cd Course-Recommender
pip install -r requirements.txt
```

---

##  Usage

### Run scripts
```bash
python src/recommender.py --course_id 10
python src/hybrid.py --course_id 10
```

### Explore notebooks
- `content_based.ipynb` → TF-IDF + cosine similarity  
- `popularity_based.ipynb` → top courses by subscribers  
- `hybrid_model.ipynb` → combined recommendations  

---

##  Evaluation
- **Content-Based** → Precision@K, Recall@K (if user history simulated).  
- **Popularity-Based** → Overlap with top-reviewed courses.  
- **Hybrid** → Qualitative balance between relevance and popularity.  

Sample Output:
```
Content-Based: ["python for beginners", "advanced python programming", "data science with python"]
Popularity-Based: ["machine learning a-z", "python for data science", "deep learning bootcamp"]
Hybrid: ["python for beginners", "machine learning a-z", "data science with python", "deep learning bootcamp", "excel for beginners"]
```

---

 Future Work
- Add **Collaborative Filtering** (SVD, matrix factorization) with simulated user-course ratings.
- Handle **cold start problem** with default recommendations.
- Deploy as a **web app** using Flask/Streamlit.
- Integrate with platforms like **Vityarthi** for real-world testing.

---

