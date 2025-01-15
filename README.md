
# Content-Based-Movies-Recommendation-System

Welcome to the **Movie Recommender System**, an ML-powered web application that suggests movies similar to your favorite ones. This project combines machine learning techniques and interactive web development to deliver personalized recommendations.

**Web App Link**: [Movie Recommender System](https://content-based-movies-recommendation.onrender.com/)

**Kaggle Link**: [Kaggle Demonstration of Recommendation System](https://www.kaggle.com/code/utkarshshkla/content-based-movie-recommendation-system)

---

## **Table of Contents**
1. [Machine Learning Workflow](#machine-learning-workflow)
   - Preprocessing
   - Feature Engineering
   - Text Vectorization
   - Similarity Matrix
   - Recommendation Generation
2. [Frontend and Deployment](#frontend-and-deployment)
   - Streamlit Code
   - Render Deployment

---

## **Machine Learning Workflow**

This project primarily employs **content-based filtering** to recommend movies by analyzing the metadata of films. Below are the steps followed:

### **1. Data Collection and Loading**
- **Datasets Used**: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) having`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`
- Loaded using **Pandas** to create DataFrames for easy manipulation and analysis.

### **2. Preprocessing**
- **Merging Datasets**: Combined the `movies` and `credits` datasets on the `title` column to create a unified dataset.
- **Column Selection**: Focused on columns like `genres`, `keywords`, `cast`, `crew`, and `overview`. These attributes capture the essence of a movie.
- **Tags Generation**:
  - Combined the above-selected columns into a single feature `tags`.
  - Processed text to lowercase, removed stopwords, and applied stemming to reduce redundancy.

### **3. Text Vectorization**
- Implemented **Bag of Words (BoW)** to convert the `tags` column into numerical vectors.
- Created a high-dimensional feature space to capture textual relationships between movies.

### **4. Similarity Matrix**
- Used **Cosine Similarity** to compute pairwise similarity between movies based on their vectorized tags.
- This matrix serves as the backbone for ranking movies in terms of relevance to the user’s input.

### **5. Recommendation Generation**
- When a user selects a movie, the app identifies its index, retrieves its similarity scores, and ranks the top 5 most similar movies.

### **6. Tools and Libraries**
- **Pandas**: For data handling and preprocessing.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For vectorization (BoW) and similarity computation.

---

## **Frontend and Deployment**

The frontend and deployment of the project focus on delivering an intuitive interface and ensuring seamless accessibility.

### **Streamlit Code**
The application was developed using **Streamlit**, a lightweight Python web app framework. Here's a breakdown of its functionality:
1. **User Input**:
   - Dropdown menu (`st.selectbox`) populated with movie titles for user selection.
2. **Recommendations Display**:
   - When a movie is selected and the "Recommend" button is clicked, the app fetches the top 5 similar movies.
   - Integrated with **The Movie Database (TMDB) API** to fetch movie posters dynamically.
3. **Interactive Layout**:
   - Used `st.columns` to display posters and titles side-by-side for a visually engaging experience.

## Deployment  
The application was deployed using **Streamlit**, a cloud-based platform for hosting web apps.

Render offers ease of deployment with:  
- **Automatic updates** from GitHub repositories  
- **Scalable infrastructure**  
