"""
	Right now this pulls all the text from the 'Coming Soon' section
	of Gateway and puts the movie titles + opening dates in a list. 

	Ultimately this should be its own function.


	TO-DO:
		-Rewrite with REGEX
		-Pull links for each movie 
		-Create a movie class that contains info like the title, the url,
		 the opening date, IMDB rating, genre
		-Write output as a neatly formated HTML page 
"""
from get_next_line import get_next_line
from scrape_text import get_page_text
from get_title import get_title
from create_movie_list import scrape_movies, create_movie_list

scraped_movies = scrape_movies()

movie_list = create_movie_list(scraped_movies)

print(movie_list)





#print("Movies found:")
#for i in range(len(scraped_movies)):
#	print(scraped_movies[i])
