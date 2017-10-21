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

url = 'http://gatewayfilmcenter.org/now-showing/coming-soon/'
header = "Coming Soon:"

#The reference string is the only consistent movie identifier
reference = "Opening at GFC:"
chunk_size = 7      #Number of lines from movie title to reference string

print("Getting page text...")
text = get_page_text(url, header)
print("Text downloaded.")

#Opening from file for testing
#with open ("soup_output.txt", "r") as myfile:
    #text = myfile.read()


movie_list = []     #[title, opening date]

ref_index = text.find(reference) 

while (ref_index != -1):
    date_index = ref_index + len(reference) + 1
    date = get_next_line(text[date_index::])

    movie = get_title(text, ref_index, chunk_size)
    movie_list.append([movie, date])

    text = text[ref_index + len(reference)::]
    ref_index = text.find(reference)


print("Movies found:")
for i in range(len(movie_list)):
    print(movie_list[i])
