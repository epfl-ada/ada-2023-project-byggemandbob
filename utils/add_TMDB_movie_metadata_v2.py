import tmdbsimple as tmdb
from tqdm import tqdm
import pandas as pd
from datetime import datetime
import re
from dotenv import load_dotenv
import os

load_dotenv()
#headers_movie_metadata = ["Wikipedia Movie ID", "Freebase Movie ID", "Movie name", "Movie release date",
 #                         "Movie box office revenue", "Movie runtime", "Movie languages", "Movie countries",
 #                         "Movie genres"]

movie_metadata_TMDB = pd.read_csv('../modified_data/movie_metadata_TMDB.csv')
movie_metadata_TMDB = movie_metadata_TMDB.dropna(subset=['TMDB_id'])

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")

# Load API key
tmdb.API_KEY = TMDB_API_KEY
tmdb.REQUESTS_TIMEOUT = 5  # seconds, for both connect and read

# runtime, revenue, budget, imdb_id, genres

# Initialize the TMDb objectmovie_metadata_TMDB = movie_metadata_TMDB.dropna(subset=['TMDB_id'])
#movie = tmdb.Movies(19995)

# Get the movie details
#movie_info = movie.info()

# You can access various information about the movie like this


saved_progress = []
start_index = 35000

#saved_progress = pd.read_json('progress_v2.json')['index'].tolist()
#start_index = saved_progress[-1] + 1  # Start from the next index

for index, row in tqdm(movie_metadata_TMDB.iterrows(), total=len(movie_metadata_TMDB), desc="Processing"):
    if index < start_index:
        continue
    try:
        movie = tmdb.Movies(row['TMDB_id'])
        movie_info = movie.info()

        #movie_metadata_TMDB.loc[index, 'TMDB_id'] = match['id']
        movie_metadata_TMDB.loc[index,'TMDB_runtime'] = movie_info['runtime']
        movie_metadata_TMDB.loc[index,'TMDB_revenue'] = movie_info['revenue']
        movie_metadata_TMDB.loc[index,'TMDB_budget'] = movie_info['budget']
        movie_metadata_TMDB.loc[index,'TMDB_IMDB_id'] = movie_info['imdb_id']

        # Convert list of genres to a string representation
        genres_str = ', '.join([genre['name'] for genre in movie_info['genres']])
        # Assign values to DataFrame
        movie_metadata_TMDB.loc[index, 'TMDB_genres'] = genres_str
        #movie_metadata_TMDB.loc[index,'TMDB_genres'] = movie_info['genres']

       # print("TEST")
       # print("Title:", movie_info['title'])
       # print("Runtime:", movie_info['runtime'])
       # print("Revenue:", movie_info['revenue'])
       # print("Budget:", movie_info['budget'])
       # print("IMDB_id:", movie_info['imdb_id'])
       # print("Genres:", movie_info['genres'])


        saved_progress.append(index)

            # Save progress periodically (in case of interruption)
        if index % 50 == 0:
            progress_df = pd.DataFrame({'index': saved_progress})
            progress_df.to_json('progress_v2.json')
            movie_metadata_TMDB.to_csv('movie_metadata_TMDB_v2.csv', index=False)

    except Exception as e:
        print(f"Error at index {index}: {str(e)}")
    # print("index:",index)
    # if index >= 105:
    #    break

# Save final progress
progress_df = pd.DataFrame({'index': saved_progress})
progress_df.to_json('progress_v2.json')

# Save your final DataFrame
movie_metadata_TMDB.to_csv('movie_metadata_TMDB_v2_DONE.csv', index=False)
