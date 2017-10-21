#Figure out how to use api
#Figure out how to use requests

import json
#import urllib
import urllib.request
from movie import Movie

base_url = "http://theapache64.xyz:8080/movie_db/search?keyword="

def add_movie_details(movie_array):
	#need while loop to create a movie using the title array and api
	for movie in movie_array:
		title = movie.title
		#have to use the title with whatever api we are using and get a map
		movie_data = json.load(urllib.request.urlopen(base_url+title))

		#urllib.urlopen(base_url+titlea)

		#Use map to populate movie object
		movie.genre = movie_data["data"]["genre"]
		movie.rating = movie_data["data"]["rating"]
