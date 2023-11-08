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

# runtime, revenue, budget, imdb_id, genres

#details = tmdb.Movies()
#response = details.movie_id=19995)
# Initialize the TMDb object
movie = tmdb.Movies(19995)

# Get the movie details
movie_info = movie.info()

# You can access various information about the movie like this
print("Title:", movie_info['title'])
print("Overview:", movie_info['overview'])
print("Release Date:", movie_info['release_date'])
print("Vote Average:", movie_info['vote_average'])
