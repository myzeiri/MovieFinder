import json
import urllib.request
from movie import Movie

base_url = "http://theapache64.xyz:8080/movie_db/search?keyword="

def add_movie_details(movie_array):
    """ Uses apache64's movie database API to find the genre and
        IMDB rating for each movie in movie_array
    """

    for movie in movie_array:
        title = movie.formatted_title

        response = urllib.request.urlopen(base_url + title)
        try:
            str_response = response.read().decode('utf-8')
            movie_data = json.loads(str_response)
        except:
            continue

        try:
            if (movie_data["error"] == "True"):
                print(movie_data)

            else:
                movie.genre = movie_data["data"]["genre"]
                movie.rating = movie_data["data"]["rating"]

        except:
            continue
