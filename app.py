import streamlit as st
import pickle
import pandas as pd
import requests
from annotated_text import annotated_text


moviesd=pickle.load(open('moviesd.pkl','rb'))

similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(moviesd)
st.title('Movie Recommender System')

def fetch_poster(movie_id):
     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1869cbd1765e4063a89087377d6182fb&language=en-US'.format(movie_id))
     data=response.json()
     return "https://image.tmdb.org/t/p/w500"+data['poster_path']


def recommend(movie):
     movie_index=movies[movies['title']==movie].index[0]
     distances=similarity[movie_index]
     movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:7]
     recommended_movie_list=[]
     recommended_movie_poster=[]
     for i in movie_list:
          movie_id=movies.iloc[i[0]].movie_id
          # fetch poster from api
          recommended_movie_poster.append(fetch_poster(movie_id))
          recommended_movie_list.append(movies.iloc[i[0]].title)
     return recommended_movie_list,recommended_movie_poster


selected_movie_name = st.selectbox(
     ' ',
     movies['title'].values)

if st.button('Recommend'):
     names,poster= recommend(selected_movie_name)
     col1,col2,col3 = st.columns(3)
    
     with col1:
          st.subheader(names[0])
          st.image(poster[0])
     with col2:
          st.subheader(names[1])
          st.image(poster[1])
     with col3:
          st.subheader(names[4])
          st.image(poster[4])
     with col1:
          st.subheader(names[2])
          st.image(poster[2])
     with col2:
          st.subheader(names[3])
          st.image(poster[3])
     with col3:
          st.subheader(names[5])
          st.image(poster[5])

