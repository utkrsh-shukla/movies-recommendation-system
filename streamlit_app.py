import streamlit as st
import pandas as pd
import requests
import pickle
import gdown

api_key  =  st.secrets['API_KEY']
# Direct download link for the Google Drive file
similarity_file_id = "1dUjDsAuvVfn0-QVXiYdo5QeaOXF185EX"
gdown.download(f"https://drive.google.com/uc?export=download&id={similarity_file_id}", "similarity.pkl", quiet=False)

st.title('Movie Recommender System')
movies_df = pd.DataFrame(pickle.load(open('movie_list.pkl', 'rb')))

# Load the similarity file from the downloaded file
with open("similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

def fetch_poster(movies_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key={api_key}')
    data = response.json()
    return f'https://image.tmdb.org/t/p/original/{data["poster_path"]}'

def recommend(movie_name, movies_df=movies_df):
    movie_index = movies_df[movies_df['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]]['movie_id']
        movie_title = movies_df.iloc[i[0]]['title']
        recommended_movies.append(movie_title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    st.write('Recommended Movies:')
    col = st.columns(5)
    for i in range(5):
        p, m = recommended_movies_posters[i], recommended_movies[i]
        col[i].image(p)
        col[i].write(m)

movies_list = movies_df['title'].values

st.write('Enter the name of the movie you like:')
selected_movie = st.selectbox('', movies_list)

if st.button('Recommend'):
    recommend(selected_movie)
