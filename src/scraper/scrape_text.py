from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_page_text(url, header):
	""" Returns the all the text from the url after the header string """

	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soup = BeautifulSoup(webpage, "html.parser")

	page_text = soup.get_text()
	start = page_text.find(header)

	return page_text[start::]
