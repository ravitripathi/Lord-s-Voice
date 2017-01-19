import requests as rq
from bs4 import BeautifulSoup
#with open('data.txt') as f:

url = 'https://www.goodreads.com/work/quotes/1492580-bhagavadg-t'
page = rq.get(url)
data = { "quotes" : [] }
soup = BeautifulSoup(page.text, 'html.parser')

for i in soup.find_all("div", class_="quoteText"):
	print i.contents[0]
	data.update("quote" : "")

print data
