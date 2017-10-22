from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from add_movie_details import add_movie_details
from movie import Movie

url = 'http://gatewayfilmcenter.org/now-showing/coming-soon/'
header = "Coming Soon:"

#The reference string is the only consistent movie identifier
reference = "Opening at GFC:"
chunk_size = 7      #Number of lines from movie title to reference string


def get_page_text(url, header):
    """ Returns the all the text from the url after the header string """

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")

    page_text = soup.get_text()
    start = page_text.find(header)

    return page_text[start::]


def get_next_line(string):
    """ Returns everything from the start of string to the first null byte """
    
    return string[:string.find("\n")]


def get_title(text, ref_index, line_count):
    """ Returns the first movie title string in text using 
        reference as a target. 

        The start of the movie title is line_count number of lines ahead of
        the start of reference. 
    """
    if (ref_index < 0):
        return

    #Move up line_count lines to the start of the movie title
    count = 0
    while count < line_count:
        char = text[ref_index]

        if char == "\n":
            count += 1

        ref_index -= 1

    return get_next_line(text[ref_index + 2::])


def scrape_movies():
    """ Returns an array containing [title, opening date] for each film. """

    print("Getting page text...")
    text = get_page_text(url, header)
    print("Text downloaded.")

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



def create_movie_list(scraped_movies):
    """ Returns an array of movie objects.
        Scraped movies is the list of [[title, date]] created by the scraper. 
    """

    movie_list = []
    i = 0
    while (i < len(scraped_movies)):
        m = Movie(scraped_movies[i][0], scraped_movies[i][1])
        movie_list.append(m)
        
        i += 1


    add_movie_details(movie_list)

    return movie_list
