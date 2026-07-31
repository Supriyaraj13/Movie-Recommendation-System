import streamlit as st
import pickle
import pandas as pd

# Load data
@st.cache_resource
def load_data():
    with open("movie_data.pkl", "rb") as file:
        movies = pickle.load(file)

    with open("similarity_matrix.pkl", "rb") as file:
        similarity_matrix = pickle.load(file)

    return movies, similarity_matrix


movies, similarity_matrix = load_data()


# Recommendation function
def recommend_movies(movie_title, number_of_recommendations=5):

    movie_index = movies[movies["title"] == movie_title].index[0]

    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = [
        score for score in similarity_scores
        if score[0] != movie_index
    ]

    recommendations = []

    for index, score in similarity_scores[:number_of_recommendations]:
        recommendations.append(
            {
                "Movie": movies.iloc[index]["title"],
                "Similarity Score": round(score, 3)
            }
        )

    return pd.DataFrame(recommendations)


# ---------------- Streamlit UI ----------------

st.title("🎬 Movie Recommendation System")

st.write(
    "Select a movie and discover similar movies using "
    "a content-based recommendation system powered by "
    "TF-IDF and Cosine Similarity."
)

selected_movie = st.selectbox(
    "Choose a Movie",
    movies["title"]
)

if st.button("Recommend Movies"):

    recommendations = recommend_movies(selected_movie)

    st.success(f"Movies similar to **{selected_movie}**")

    st.dataframe(
        recommendations,
        use_container_width=True
    )