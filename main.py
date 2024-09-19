import streamlit as st
import joblib as job

df  = job.load('movies_Data.pkl')
similarity = job.load('similarity.pkl')

st.title('Movie Recommendation System')
selected=st.selectbox("Choose the Movie", df['title'].tolist())

def recommended(movie):
    index=df[df['title']==movie].index[0]
    distances=similarity[index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    for i in movies_list:
        l.append(df.iloc[i[0]]['title'])

    return l

print()  
if st.button('Recommend'):
    for i in recommended(selected):
        st.write(i)


