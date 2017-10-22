import re
class Movie: 
    """ This is the movie class which contains title, opening date, genre, rating
        for each scraped movie.
    """

    def __init__(self, original_title, opening_date):
        self.original_title = original_title
        self.formatted_title = self.format_title()
        self.opening_date = opening_date
        self.genre = "genre"
        self.rating = "rating"

    def format_title(self):
        formatted_title = re.sub(r"\(\d{4}\).*", "", self.original_title)
        formatted_title = formatted_title.strip()
        formatted_title = formatted_title.replace(" ", "+")
        return formatted_title.replace("NFF:", "")

    def prettyPrint(self):
        print(self.original_title)
        print("\t" + self.opening_date)
        print("\t" + self.genre)
        print("\tRating = " + self.rating)
