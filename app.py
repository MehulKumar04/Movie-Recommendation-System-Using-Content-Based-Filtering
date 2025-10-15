import pickle
import streamlit as st
import pandas as pd
import numpy as np
import requests # Keeping requests import just in case, but it's not used below

# --- Configuration ---
# Set a generic placeholder URL that is known to be accessible.
PLACEHOLDER_IMAGE_URL = "https://placehold.co/500x750/1f77b4/ffffff?text=Movie+Poster"


# --- Helper Function (No longer calls external API) ---

def recommend(movie, movies_df, similarity_matrix):
    """
    Finds and returns the top 10 most similar movie titles.
    Poster fetching logic is removed due to connection issues.
    """
    try:
        # 1. Find index of the selected movie
        index = movies_df[movies_df['title'] == movie].index[0]
    except IndexError:
        # Return error message if movie title is not found
        return ["Movie not found in list. Please try another title."], [PLACEHOLDER_IMAGE_URL]

    # 2. Get and sort distances (similarities)
    distances = sorted(list(enumerate(similarity_matrix[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    
    # 3. Iterate over the top 10 results (excluding the first item, which is the movie itself)
    for i in distances[1:11]:
        # We only need the title here, as we are no longer fetching posters
        recommended_movie_names.append(movies_df.iloc[i[0]].title)

    # Return the names list and a list of placeholder URLs for the Streamlit display loop
    recommended_movie_posters = [PLACEHOLDER_IMAGE_URL] * len(recommended_movie_names)

    return recommended_movie_names, recommended_movie_posters


# --- Main Streamlit App Logic ---

st.set_page_config(layout="wide", page_title="Movie Recommender")
st.header('Movie Recommender System')

try:
    # --- MODEL LOADING (Paths adjusted to include 'model/' subdirectory) ---
    # NOTE: Ensure your files 'movie_dict.pkl' and 'similarity.pkl' are placed 
    # inside a subfolder named 'model'.
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl','rb'))
except FileNotFoundError:
    st.error("Model files not found. Please ensure 'movie_dict.pkl' and 'similarity.pkl' are in a 'model' directory.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model artifacts. Check file contents. Error: {e}")
    st.stop()


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation', type="primary"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, movies, similarity)
    
    # Use the modern st.columns (10 columns for 10 recommendations)
    cols = st.columns(10)
    
    for i in range(10):
        with cols[i]:
            # Display title above the image
            st.text(recommended_movie_names[i])
            # Display the placeholder image, now using use_container_width
            st.image(recommended_movie_posters[i], use_container_width=True, caption=recommended_movie_names[i])

st.markdown("---")
st.caption("Content-based recommendation. Poster fetching disabled due to external API connection issues.")
