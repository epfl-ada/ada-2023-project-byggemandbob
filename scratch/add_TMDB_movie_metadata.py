import tmdbsimple as tmdb
from tqdm import tqdm
import pandas as pd
from datetime import datetime
import re
from dotenv import load_dotenv
import os

load_dotenv()
headers_movie_metadata = ["Wikipedia Movie ID", "Freebase Movie ID", "Movie name", "Movie release date",
                          "Movie box office revenue", "Movie runtime", "Movie languages", "Movie countries",
                          "Movie genres"]

movie_metadata = pd.read_csv('../data/movie.metadata.tsv', sep="\t", names=headers_movie_metadata)


TMDB_API_KEY = os.environ.get("TMDB_API_KEY")

# Load API key
tmdb.API_KEY = TMDB_API_KEY
tmdb.REQUESTS_TIMEOUT = 5  # seconds, for both connect and read

# Create a list to save progress
saved_progress = []

# Determine where to resume (if applicable)
start_index = 28000  # You can adjust this if you need to start from a specific index

# If you have a saved progress file, you can use it to resume
# For example, if you have a 'progress.json' file containing previously processed indices:
#saved_progress = pd.read_json('progress.json')['index'].tolist()
#start_index = saved_progress[-1] + 1  # Start from the next index

# Create a DataFrame to store your data
movie_metadata_TMDB = movie_metadata.copy()

for index, row in tqdm(movie_metadata_TMDB.iterrows(), total=len(movie_metadata_TMDB), desc="Processing"):
    # Skip previously processed indices
    #if index in saved_progress:
    #    continue
    if index < start_index:
        continue
    try:
        if not pd.isna(row["Movie release date"]):
            search = tmdb.Search()
            response = search.movie(query=row["Movie name"])

            # convert dataframe release to datetime
            #movie_release_date = datetime.strptime(row["Movie release date"], "%Y-%m-%d").date()
            movie_release_date_str = row["Movie release date"]
            if len(movie_release_date_str) == 4:  # Handle "YYYY" format
                movie_release_date = datetime.strptime(movie_release_date_str, "%Y").date()
            elif len(movie_release_date_str) == 7:  # Handle "YYYY-DD" format
                movie_release_date = datetime.strptime(movie_release_date_str, "%Y-%m").date()
            else:  # Assume it's in the format "YYYY-MM-DD"
                movie_release_date = datetime.strptime(movie_release_date_str, "%Y-%m-%d").date()
            # convert query elements to datetime


            #date_list_converted = [datetime.strptime(each_date['release_date'], "%Y-%m-%d").date() for each_date in search.results]

            # handle if release_date is empty.
            date_list_converted = [datetime.strptime(each_date['release_date'], "%Y-%m-%d").date() for each_date in
                                   search.results if each_date.get('release_date')]

            # create list of differences in time
            differences = [abs(movie_release_date - each_date) for each_date in date_list_converted]
            # if differences is empty skip
            if not differences:
                continue
            minimum_index = differences.index(min(differences))  # Index of the closest match
            match = search.results[minimum_index]
            # print(f"Closest match: {match['title']} (Release Date: {match['release_date']})")

            # add info in dataframe about the movie

            movie_metadata_TMDB.loc[index, 'TMDB_id'] = match['id']
            movie_metadata_TMDB.loc[index, 'TMDB_original_language'] = match['original_language']
            movie_metadata_TMDB.loc[index, 'TMDB_original_title'] = match['original_title']
            movie_metadata_TMDB.loc[index, 'TMDB_overview'] = match['overview']
            movie_metadata_TMDB.loc[index, 'TMDB_popularity'] = match['popularity']
            movie_metadata_TMDB.loc[index, 'TMDB_release_date'] = match['release_date']
            movie_metadata_TMDB.loc[index, 'TMDB_title'] = match['title']
            movie_metadata_TMDB.loc[index, 'TMDB_vote_average'] = match['vote_average']
            movie_metadata_TMDB.loc[index, 'TMDB_vote_count'] = match['vote_count']
            # Save the index as progress
            saved_progress.append(index)

            # Save progress periodically (in case of interruption)
            if index % 50 == 0:
                progress_df = pd.DataFrame({'index': saved_progress})
                progress_df.to_json('progress.json')
                movie_metadata_TMDB.to_csv('movie_metadata_TMDB.csv', index=False)

    except Exception as e:
        print(f"Error at index {index}: {str(e)}")
    #print("index:",index)
    #if index >= 105:
    #    break

# Save final progress
progress_df = pd.DataFrame({'index': saved_progress})
progress_df.to_json('progress.json')

# Save your final DataFrame
movie_metadata_TMDB.to_csv('movie_metadata_TMDB.csv', index=False)