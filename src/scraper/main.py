"""
	TO-DO:
		-Rewrite with REGEX
		-Pull links for each movie 
		-Write output as a neatly formated HTML page 
"""
from get_next_line import get_next_line
from scrape_text import get_page_text
from get_title import get_title
from create_movie_list import scrape_movies, create_movie_list

scraped_movies = scrape_movies()

movie_list = create_movie_list(scraped_movies)


file = open("output.txt", "w")

for m in movie_list:


file.close()

