#Figure out how to use api
#Figure out how to use requests

import json
import urllib2

base_url = ""

def add_movie_details(movie_array):
	#need while loop to create a movie using the title array and api
	for movie in movie_array:
		title = movie.title
		#have to use the title with whatever api we are using and get a map
		movie_data = json.load(urllib2.urlopen(base_url+title))
		#Use map to populate movie object
		movie.genre = movie_data["data"]["genre"]
		movie.rating = movie_data["data"]["rating"]
