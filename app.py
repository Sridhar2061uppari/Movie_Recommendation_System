import streamlit as st
import pickle
import pandas as pd
import requests
#https://api.themoviedb.org/3/movie/65?api_key=e8e78c8a47412cfd34f577e96710d27e&language=en-US
def fetch_poster(movie_id):
    response = 'https://api.themoviedb.org/3/movie/{}?api_key=e8e78c8a47412cfd34f577e96710d27e&language=en-US'.format(movie_id)
    data = requests.get(response)
    data=data.json()
    #st.text(data)
    #st.text('https://api.themoviedb.org/3/movie/{}?api_key=e8e78c8a47412cfd34f577e96710d27e&language=en-US'.format(movie_id))
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies_names = []
    recommended_movies_posters = []
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies_names, recommended_movies_posters

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommendation System")

option=st.selectbox(
    "Welcome",
movies['title'].values)

if st.button("Recommend"):
    recommended_movie_names, recommended_movie_posters=recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])