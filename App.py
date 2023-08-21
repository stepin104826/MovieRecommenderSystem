import pandas as pd
import streamlit as st
import pickle
import requests


movies_dict = pickle.load(open("movies.pkl","rb"))
movies_df = pd.DataFrame(movies_dict)

movies_info_dict = pickle.load(open("movies_info.pkl","rb"))
movies_info_df = pd.DataFrame(movies_info_dict)

movies_info1_dict = pickle.load(open("movie_info1.pkl","rb"))
movies_info1_df = pd.DataFrame(movies_info1_dict)

sim_matrix = pickle.load(open("similarity_matrix.pkl","rb"))

def get_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=b2ffd4bb9644a0a7de08aa8cdb41c0ab&language=en-US")
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/"+ data["poster_path"]

def recommend(movie):
    recommended = []
    recommended_movie_posters = []
    movie_index = movies_df[movies_df["title"] == movie].index[0]
    movie_sim_array = list(enumerate(sim_matrix[movie_index]))
    top5_most_similar = sorted(movie_sim_array, key=lambda x: x[1], reverse=True)[1:6]

    for id,movie in top5_most_similar:
        mov_id = movies_df["movie_id"][id]
        recommended.append(movies_df["title"][id])
        recommended_movie_posters.append(get_poster(mov_id))
    return recommended,recommended_movie_posters

st.title("TMDB Movie Recommender System")

option = st.sidebar.selectbox("Select a movie:",movies_df["title"])
option_id = movies_info_df[movies_info_df["title"]==option]["movie_id"].values[0]
overview = movies_info_df[movies_info_df["title"]==option]["overview"].values[0]
director = movies_info1_df[movies_info1_df["title"] == option]["crew"].values[0]
cast = movies_info1_df[movies_info1_df["title"] == option]["cast"].values[0]
rating = movies_info1_df[movies_info1_df["title"] == option]["vote_average"].values[0]
date =  movies_info1_df[movies_info1_df["title"] == option]["release_date"].values[0]
genre = movies_info1_df[movies_info1_df["title"] == option]["genres"].values[0][1:3]
budget = (movies_info1_df[movies_info1_df["title"] == option]["budget"].values[0])/1000000
link = movies_info1_df[movies_info1_df["title"] == option]["homepage"].values[0]
gen = movies_info1_df[movies_info1_df["title"] == option]["genres"].values[0][1]
# print(option_id,genres,director,rating,cast,date,budget,overview)

if st.button("Recommend more movies like "+ '"'+str(option)+'"'):
    names,posters = recommend(option)
    st.subheader("Similar "+str(gen)+" movies:")
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.caption(names[0])
        st.image(posters[0])
    with col2:
        st.caption(names[1])
        st.image(posters[1])
    with col3:
        st.caption(names[2])
        st.image(posters[2])
    with col4:
        st.caption(names[3])
        st.image(posters[3])
    with col5:
        st.caption(names[4])
        st.image(posters[4])

if option:
    with st.container():
        st.image(get_poster(option_id))

        st.sidebar.subheader("Title:")
        st.sidebar.text(option)

        st.sidebar.subheader("Storyline:")
        st.sidebar.text(overview)

        st.sidebar.subheader("Genre(s):")
        genres = []
        capital = 0
        genre = ["Adventure", "ScienceFiction"]
        genres = []
        capital = 0
        for g in genre:
            capital = 0
            for lett in g:
                if ord(lett) >= 65 and ord(lett) <= 90:
                    capital += 1
                    if capital > 1:
                        g = g.replace(str(lett), " " + str(lett))
                        genres.append(g)
                else:
                    continue
            if capital == 1:
                genres.append(g)
        for ele in genres:
                st.sidebar.text(ele)

        st.sidebar.subheader("TMDB Rating:")
        st.sidebar.text(rating)

        st.sidebar.subheader("Director:")
        capital_count = 0
        for ele in director:
            for letter in ele:
                if 65<=ord(letter)<=90:
                    capital_count+=1
                    if capital_count>1:
                        st.sidebar.text(ele.replace(letter," "+letter))

        st.sidebar.subheader("Cast")

        names = []
        capital_ct = 0
        for actor in cast:
            capital_ct = 0
            for let in actor:
                if 65 <= ord(let) <= 90:
                    capital_ct += 1
                    if capital_ct > 1:
                        actor = actor.replace(let, " " + let)
                        names.append(actor)
                else:
                    continue
            if capital_ct == 1:
                names.append(actor)

        for ele in names:
            st.sidebar.text(ele)

        st.sidebar.subheader("Budget:")
        st.sidebar.text("$"+str(round(budget,2))+" M")

        st.sidebar.subheader("Release Date:")
        st.sidebar.text(date)

        st.sidebar.subheader("Official Link:")
        st.sidebar.text(link)