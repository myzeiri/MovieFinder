import re
class Movie: 
	#This is the movie class which will contain title, opening date, genre, rating#

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



#"NFF: Dont Fuck in the Woods"

#m = Movie("Title test (2000) in 50mm", "tomorrow")
#print(m.original_title)
#print(m.formatted_title)

