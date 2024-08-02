# MovieRecommenderSystem

## Overview
This project is a Streamlit-based web application that recommends movies based on user selection. It uses data from The Movie Database (TMDB) to provide movie information and recommendations.

## Features
- Movie selection from a comprehensive database
- Display of detailed movie information including:
  - Movie poster
  - Title
  - Storyline
  - Genre(s)
  - TMDB Rating
  - Director
  - Cast
  - Budget
  - Release Date
  - Official movie website link
- Recommendation of 5 similar movies with posters

## Technologies Used
- Python
- Pandas: For data manipulation
- Streamlit: For creating the web application interface
- Pickle: For loading pre-processed data
- Requests: For making API calls to TMDB

## Setup and Installation
1. Clone the repository
2. Install the required packages:
3. Ensure you have the following pickle files in your project directory:
- movies.pkl
- movies_info.pkl
- movie_info1.pkl
- similarity_matrix.pkl

## Usage
1. Run the Streamlit app:
2. Select a movie from the sidebar dropdown
3. View detailed information about the selected movie
4. Click the "Recommend more movies like [selected movie]" button to see similar movie recommendations

## API Usage
This project uses the TMDB API to fetch movie posters. Make sure you have a valid API key from TMDB.

## Data
The project uses pre-processed data stored in pickle files. These files contain movie information and a similarity matrix for recommendations.
