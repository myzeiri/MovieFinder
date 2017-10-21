#Figure out how to use api
#Figure out how to use requests

import json
import urllib.request
from movie import Movie

base_url = "http://theapache64.xyz:8080/movie_db/search?keyword="


def add_movie_details(movie_array):
	#need while loop to create a movie using the title array and api
	for movie in movie_array:
		title = movie.formatted_title

		response = urllib.request.urlopen(base_url + title)
		try:
			str_response = response.read().decode('utf-8')
			movie_data = json.loads(str_response)
		except:
			#print("Response error")
			continue

		try:
			if (movie_data["error"] == "True"):
				#print("Error: movie not found online.")
				print(movie_data)

			else:
				movie.genre = movie_data["data"]["genre"]
				movie.rating = movie_data["data"]["rating"]

		except:
			#print(title + " didn't load.")
			continue
		
