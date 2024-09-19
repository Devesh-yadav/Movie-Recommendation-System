import streamlit as st
import joblib as job
import requests


def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=eb927d0dd3531172677f691d0d69d4f7')
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']


df  = job.load('movies_Data.pkl')
similarity = job.load('similarity.pkl')

left, center, right = st.columns([0.5, 99, 0.5])  # Adjust the weights for more or less padding
with center:
    st.title('Movie Recommendation System')

for _ in range(2):
    st.write("") 
selected=st.selectbox("Choose the Movie", df['title'].tolist())

def recommended(movie):
    index=df[df['title']==movie].index[0]
    distances=similarity[index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    l_poster=[]
    for i in movies_list:
        l.append(df.iloc[i[0]]['title'])
        l_poster.append(fetch_poster(df.iloc[i[0]].movie_id))

    return l,l_poster

print()  
if st.button('Recommend'):
    name,poster=recommended(selected)
    c1,c2,c3,c4,c5=st.columns(5)
    cols=[c1,c2,c3,c4,c5]

    for i in range(5):
        with cols[i]:
            st.write(name[i])
            st.image(poster[i])

