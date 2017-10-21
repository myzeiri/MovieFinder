from get_next_line import get_next_line
from scrape_text import get_page_text
from get_title import get_title
from add_movie_details import add_movie_details
from movie import Movie

url = 'http://gatewayfilmcenter.org/now-showing/coming-soon/'
header = "Coming Soon:"

#The reference string is the only consistent movie identifier
reference = "Opening at GFC:"
chunk_size = 7      #Number of lines from movie title to reference string


def scrape_movies():
	print("Getting page text...")
	text = get_page_text(url, header)
	print("Text downloaded.")

	#Opening from file for testing
	#with open ("soup_output.txt", "r") as myfile:
		#text = myfile.read()

	scraped_movies = []     #[title, opening date]

	ref_index = text.find(reference) 

	while (ref_index != -1):
		date_index = ref_index + len(reference) + 1
		date = get_next_line(text[date_index::])

		movie = get_title(text, ref_index, chunk_size)
		scraped_movies.append([movie, date])

		text = text[ref_index + len(reference)::]
		ref_index = text.find(reference)

	return scraped_movies


# Returns an array of movie objects.
# Scraped movies is the list of [[title, date]] created by the scraper.
def create_movie_list(scraped_movies):
	movie_list = []
	i = 0
	while (i < len(scraped_movies)):
		m = Movie(scraped_movies[i][0], scraped_movies[i][1])
		movie_list.append(m)
		
		i += 1


	add_movie_details(movie_list)

	return movie_list
