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

print("Welcome to the Gateway Film Scraper.")
print("Enter the genres you are interested in seperated by commas.")

genres_input = input()
genres = genres_input.split(",")

# Get the movie information
scraped_movies = scrape_movies()
movie_list = create_movie_list(scraped_movies)

users_picks = []

for m in movie_list:
	for g in genres:
		if g in m.genre:
			users_picks.append(m)
			break


for m in users_picks:
	m.prettyPrint()
